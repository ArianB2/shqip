# Development Dockerfile for local Docker Compose use.
# For production (Month 4), you'll use a multi-stage build that outputs static files
# and serves them via nginx — this one is dev-only with hot reload.

FROM node:20-alpine

WORKDIR /app

# Install dependencies first (cached layer — faster rebuilds)
COPY package*.json ./
RUN npm install

# Copy source
COPY . .

EXPOSE 5173

# Run Vite dev server with hot module replacement
CMD ["npm", "run", "dev"]
