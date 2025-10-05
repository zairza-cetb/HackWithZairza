# Level 4: Complete Deployment Pipelines with Monitoring

Build production-ready deployment pipelines integrating automated testing, building, deployment, monitoring, and alerting. Implement comprehensive DevOps practices with logging and health monitoring.

## Project Options

### Option 1: Full-Stack Application with Monitoring
Complete pipeline deploying to cloud platform with monitoring stack.

**Components:**
- GitHub Actions CI/CD
- Docker containers
- Cloud deployment (AWS/Azure/GCP)
- Prometheus for metrics
- Grafana for visualization
- Loki for logging

### Option 2: Microservices Deployment Pipeline
Multi-service application with service mesh and monitoring.

**Components:**
- Multiple service repositories
- Shared workflow templates
- Container registry
- Health checks and readiness probes
- Centralized logging
- Alert manager

### Option 3: Blue-Green Deployment with Rollback
Zero-downtime deployment with automated rollback capability.

**Components:**
- Dual environment setup
- Health check validation
- Automated traffic switching
- Rollback on failure
- Performance monitoring

## Pipeline Architecture
```
name: Production Deployment

on:
push:
branches: [ main ]

jobs:
test:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v3
- name: Run tests
run: npm test
- name: Upload coverage
uses: codecov/codecov-action@v3

build:
needs: test
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v3
- name: Build Docker image
run: docker build -t myapp:${{ github.sha }} .
- name: Push to registry
run: docker push myapp:${{ github.sha }}

deploy:
needs: build
runs-on: ubuntu-latest
steps:
- name: Deploy to production
run: |
kubectl set image deployment/myapp myapp=myapp:${{ github.sha }}
kubectl rollout status deployment/myapp
- name: Run health checks
run: ./scripts/health-check.sh

monitor:
needs: deploy
runs-on: ubuntu-latest
steps:
- name: Configure monitoring
run: ./scripts/setup-monitoring.sh
- name: Send notification
uses: 8398a7/action-slack@v3
with:
status: ${{ job.status }}
```


## Monitoring Stack Configuration

**docker-compose.monitoring.yml:**
```
version: '3.8'

services:
prometheus:
image: prom/prometheus:latest
ports:
- "9090:9090"
volumes:
- ./prometheus.yml:/etc/prometheus/prometheus.yml
- prometheus-data:/prometheus

grafana:
image: grafana/grafana:latest
ports:
- "3000:3000"
environment:
- GF_SECURITY_ADMIN_PASSWORD=admin
volumes:
- grafana-data:/var/lib/grafana

loki:
image: grafana/loki:latest
ports:
- "3100:3100"
volumes:
- loki-data:/loki

volumes:
prometheus-data:
grafana-data:
loki-data:
```


## Technical Requirements

1. **Complete CI/CD pipeline** with all stages
2. **Automated testing** at multiple levels
3. **Container orchestration** with health checks
4. **Monitoring and alerting** configured
5. **Logging aggregation** implemented
6. **Rollback strategy** defined
7. **Security scanning** in pipeline
8. **Performance metrics** collected
9. **Documentation** for all components

## Submission Requirements

Create folder `ProjectName_YourGitHubUsername` containing:

1. **.github/workflows/** - Complete workflow files
2. **docker-compose.yml** - Application services
3. **docker-compose.monitoring.yml** - Monitoring stack
4. **prometheus.yml** - Metrics configuration
5. **grafana-dashboards/** - Dashboard JSON files
6. **scripts/** - Deployment and health check scripts
7. **README.md** - Complete documentation
8. **ARCHITECTURE.md** - System architecture diagram
9. **RUNBOOK.md** - Operational procedures

## Health Check Implementation
```
#!/bin/bash

health-check.sh
ENDPOINT="http://myapp.example.com/health"
MAX_RETRIES=5
RETRY_DELAY=10

for i in $(seq 1 $MAX_RETRIES); do
response=$(curl -s -o /dev/null -w "%{http_code}" $ENDPOINT)
if [ $response -eq 200 ]; then
echo "Health check passed"
exit 0
fi
echo "Attempt $i failed, retrying..."
sleep $RETRY_DELAY
done

echo "Health check failed after $MAX_RETRIES attempts"
exit 1
```


## Monitoring Metrics

**Application Metrics:**
- Request rate and latency
- Error rates
- Resource utilization (CPU, memory)
- Active connections

**Infrastructure Metrics:**
- Container health status
- Disk usage
- Network throughput
- Database connections

## Alert Configuration

Configure alerts for:
- High error rates (> 5%)
- Response time degradation (> 1s)
- Container restarts
- Resource exhaustion
- Failed deployments

## Learning Resources

- [Prometheus Documentation](https://prometheus.io/docs/)
- [Grafana Documentation](https://grafana.com/docs/)
- [Kubernetes Deployment Strategies](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [GitHub Actions Advanced Workflows](https://docs.github.com/en/actions/using-workflows/about-workflows)
