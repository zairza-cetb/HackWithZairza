# Level 2: Docker Compose Configurations

Build multi-container applications using Docker Compose. Orchestrate services including web applications, databases, and caching layers with proper networking and volume management.

## Project Options

### Option 1: MERN Stack Application
Full-stack application with MongoDB, Express, React, and Node.js.

**Services:**
- Frontend (React): Port 3000
- Backend (Node.js/Express): Port 5000
- Database (MongoDB): Port 27017

### Option 2: Python Django with PostgreSQL
Django application with PostgreSQL database and Redis cache.

**Services:**
- Web (Django): Port 8000
- Database (PostgreSQL): Port 5432
- Cache (Redis): Port 6379

### Option 3: Node.js API with MySQL
RESTful API with MySQL database and persistent storage.

**Services:**
- API (Node.js): Port 3000
- Database (MySQL): Port 3306

## Docker Compose Structure
```
version: '3.8'

services:
web:
build: ./web
ports:
- "3000:3000"
environment:
- DB_HOST=database
- DB_PORT=5432
depends_on:
- database
volumes:
- ./web:/app
networks:
- app-network

database:
image: postgres:15-alpine
environment:
- POSTGRES_USER=user
- POSTGRES_PASSWORD=password
- POSTGRES_DB=mydb
volumes:
- db-data:/var/lib/postgresql/data
networks:
- app-network

volumes:
db-data:

networks:
app-network:
driver: bridge
```


## Technical Requirements

1. **Multiple services defined**
2. **Service dependencies configured**
3. **Environment variables for configuration**
4. **Named volumes for data persistence**
5. **Custom network for service communication**
6. **Health checks for critical services**
7. **Restart policies defined**

## Submission Requirements

Create folder `ProjectName_YourGitHubUsername` containing:

1. **docker-compose.yml** - Main orchestration file
2. **Dockerfiles** - Individual service containers
3. **.env.example** - Environment variables template
4. **README.md** - Complete setup guide
5. **init.sql** or seed data (if applicable)

## README.md Must Include

- Service descriptions
- Prerequisites
- Setup instructions
- Start/stop commands
- Port mappings
- Environment variables
- Access URLs
- Troubleshooting tips

## Commands Reference
```
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f [service_name]

# Stop all services
docker-compose down

# Rebuild services
docker-compose up -d --build

# Remove volumes
docker-compose down -v
```


## Best Practices

- Use environment files for configuration
- Implement health checks
- Set resource limits
- Use named volumes for persistence
- Configure restart policies
- Document all services
- Use specific image versions

## Learning Resources

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Compose File Reference](https://docs.docker.com/compose/compose-file/)
- [Networking in Compose](https://docs.docker.com/compose/networking/)
