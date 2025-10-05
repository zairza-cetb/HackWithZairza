# Level 3: GitHub Actions CI/CD Workflows

Create automated CI/CD pipelines using GitHub Actions. Implement workflows for testing, building, and deploying applications with automated triggers on push and pull requests.

## Project Options

### Option 1: Node.js CI Pipeline
Automated testing and Docker image building for Node.js application.

**Workflow Steps:**
- Checkout code
- Setup Node.js environment
- Install dependencies
- Run linting
- Run tests
- Build Docker image
- Push to Docker Hub

### Option 2: Python Application CI/CD
Complete pipeline with testing, building, and deployment.

**Workflow Steps:**
- Code checkout
- Python setup
- Dependency installation
- Unit tests with pytest
- Code coverage report
- Docker build and push

### Option 3: Multi-Stage Build and Deploy
Advanced workflow with staging and production environments.

**Workflow Steps:**
- Test on pull requests
- Build on merge to main
- Deploy to staging automatically
- Manual approval for production

## GitHub Actions Workflow Structure
```
name: CI/CD Pipeline

on:
push:
branches: [ main, develop ]
pull_request:
branches: [ main ]

jobs:
test:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v3
- name: Setup Node.js
    uses: actions/setup-node@v3
    with:
        node-version: '18'
    
- name: Install dependencies
    run: npm ci 

- name: Run tests
    run: npm test

- name: Run linting
    run: npm run lint

build:
needs: test
runs-on: ubuntu-latest
if: github.event_name == 'push'

steps:
  - uses: actions/checkout@v3
  
  - name: Login to Docker Hub
    uses: docker/login-action@v2
    with:
      username: ${{ secrets.DOCKER_USERNAME }}
      password: ${{ secrets.DOCKER_PASSWORD }}
      
  - name: Build and push
    uses: docker/build-push-action@v4
    with:
      context: .
      push: true
      tags: username/app:latest
```


## Technical Requirements

1. **Workflow triggers defined** (push, pull_request)
2. **Multiple jobs configured** (test, build, deploy)
3. **Job dependencies set** (needs keyword)
4. **Secrets management** for credentials
5. **Conditional execution** based on events
6. **Error handling** and notifications
7. **Caching** for dependencies

## Submission Requirements

Create folder `ProjectName_YourGitHubUsername` containing:

1. **.github/workflows/ci-cd.yml** - Main workflow
2. **Application code** - Project files
3. **Dockerfile** - Container configuration
4. **README.md** - Setup and workflow documentation
5. **test files** - Automated tests
6. **Screenshots** - Workflow execution results

## Secrets Configuration

Required secrets in GitHub repository settings:
```
DOCKER_USERNAME - Docker Hub username
DOCKER_PASSWORD - Docker Hub password or token
```


## Workflow Best Practices

- Use specific action versions
- Cache dependencies for faster builds
- Run tests before building
- Use matrix strategy for multiple versions
- Implement proper error handling
- Add status badges to README
- Use environment-specific secrets

## Status Badge

Add to README.md:

## Learning Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- [Starter Workflows](https://github.com/actions/starter-workflows)
