AWS DEPLOYMENT ARCHITECTURE

Application:
- FastAPI
- LangGraph
- Gemini
- RAG
- Celery

AWS Mapping:

FastAPI
    -> ECS / Fargate

Docker image
    -> Amazon ECR

PostgreSQL
    -> Amazon RDS

Redis
    -> Amazon ElastiCache

Logs
    -> Amazon CloudWatch

Secrets
    -> AWS Secrets Manager

Networking
    -> Amazon VPC

External access
    -> Application Load Balancer


Network design:

Internet
    |
    v
Public Application Load Balancer
    |
    v
Private ECS/Fargate services
    |
    +---- RDS PostgreSQL
    |
    +---- ElastiCache Redis
    |
    +---- Celery workers


CI/CD:

Developer
    |
    v
GitHub
    |
    v
GitHub Actions
    |
    +---- Run tests
    |
    +---- Build Docker image
    |
    v
Amazon ECR
    |
    v
ECS/Fargate