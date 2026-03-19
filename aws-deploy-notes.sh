# AWS Deployment — Month 1 Manual Steps
#
# Before the CI/CD pipeline is wired up (Month 4), use these commands
# to push and deploy manually. Run these from your terminal.
#
# Prerequisites:
#   - AWS CLI installed: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
#   - Docker Desktop running
#   - AWS account created + IAM user with programmatic access
#   - Run: aws configure  (paste your Access Key ID and Secret)

# ── Step 1: Create an ECR repository ─────────────────────────────────────────
# Run this ONCE to create the registry that stores your Docker images.
aws ecr create-repository \
  --repository-name shqip-backend \
  --region us-east-1

# ── Step 2: Log Docker in to ECR ──────────────────────────────────────────────
# Replace 123456789012 with your actual AWS account ID (find it in the AWS console top-right)
aws ecr get-login-password --region us-east-1 \
  | docker login --username AWS --password-stdin \
    123456789012.dkr.ecr.us-east-1.amazonaws.com

# ── Step 3: Build and push your image ─────────────────────────────────────────
# Build the image
docker build -t shqip-backend ./backend

# Tag it for ECR
docker tag shqip-backend:latest \
  123456789012.dkr.ecr.us-east-1.amazonaws.com/shqip-backend:latest

# Push it
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/shqip-backend:latest

# ── Step 4: Create ECS cluster ────────────────────────────────────────────────
# Use Fargate — serverless containers, you don't manage the server.
aws ecs create-cluster \
  --cluster-name shqip-cluster \
  --capacity-providers FARGATE

# ── Step 5: Create a task definition ─────────────────────────────────────────
# Do this in the AWS console (ECS → Task Definitions → Create new)
# Key settings:
#   - Launch type: Fargate
#   - CPU: 256 (.25 vCPU) — cheapest option, fine for development
#   - Memory: 512 MB
#   - Container image: paste your ECR URI from Step 2
#   - Port: 8000
#   - Environment variables: paste your .env values here

# ── Step 6: Create an ECS service ─────────────────────────────────────────────
# Do this in the AWS console (ECS → your cluster → Services → Create)
# Key settings:
#   - Desired tasks: 1
#   - Assign a public IP: yes (for now — Month 4 adds a load balancer)

# ── Useful commands ────────────────────────────────────────────────────────────

# Check running ECS tasks
aws ecs list-tasks --cluster shqip-cluster

# See logs for a running task
aws logs tail /ecs/shqip-backend --follow

# Force a new deployment (re-pulls the latest image)
aws ecs update-service \
  --cluster shqip-cluster \
  --service shqip-backend-service \
  --force-new-deployment
