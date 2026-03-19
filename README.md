# Shqip — Albanian Language Learning App

A full-stack language learning app for Albanian (Gheg & Tosk dialects),
built on AWS with Python FastAPI, React, and Docker.

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React + Tailwind CSS |
| Backend | Python FastAPI |
| Containerization | Docker + Docker Compose |
| Cloud | AWS (ECS, S3, CloudFront, RDS, Cognito, Bedrock, Polly) |
| CI/CD | GitHub Actions |
| Database | PostgreSQL (Amazon RDS) |

## Project Structure

```
shqip/
├── frontend/         # React app
├── backend/          # FastAPI app
├── .github/
│   └── workflows/    # GitHub Actions CI/CD
├── docker-compose.yml
└── README.md
```

## Getting Started (Month 1 Goal)

### Prerequisites
- Docker Desktop installed
- Node.js 18+ installed
- Python 3.11+ installed
- AWS account created
- AWS CLI installed and configured

### Run locally with Docker Compose

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/shqip.git
cd shqip

# Copy environment variables
cp backend/.env.example backend/.env
# (fill in your values in backend/.env)

# Start both frontend and backend
docker-compose up --build
```

- Frontend runs at: http://localhost:5173
- Backend runs at:  http://localhost:8000
- API docs run at:  http://localhost:8000/docs

### Run without Docker (local dev)

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## Month 1 Checklist

- [ ] App runs locally with Docker Compose
- [ ] FastAPI `/health` endpoint returns 200
- [ ] React frontend connects to backend
- [ ] Docker image builds without errors
- [ ] Image pushed to Amazon ECR manually
- [ ] App deployed to Amazon ECS (manually, no CI/CD yet)
- [ ] GitHub Actions workflow file created (full automation in Month 4)

## Environment Variables

See `backend/.env.example` for all required variables.
Never commit your `.env` file — it's in `.gitignore`.

## Dialects

| Code | Dialect | Region |
|---|---|---|
| `gheg` | Gheg | Northern Albania, Kosovo |
| `tosk` | Tosk | Southern Albania (standard) |
