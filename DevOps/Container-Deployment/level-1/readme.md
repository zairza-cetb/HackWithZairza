# Level 1: Simple Dockerfiles

Create basic Docker container configurations for different application stacks. Focus on understanding Dockerfile syntax, image building, and running containerized applications.

## Project Options

### Option 1: Node.js Application Container
Containerize a simple Node.js Express application.

**Requirements:**
- Base image: node:18-alpine
- Install dependencies
- Expose port 3000
- Run application with npm start

**Dockerfile Structure:**
```
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```


### Option 2: Python Flask Application Container
Containerize a Python Flask application.

**Requirements:**
- Base image: python:3.11-slim
- Install dependencies from requirements.txt
- Expose port 5000
- Run with Flask development server

### Option 3: Static Website Container
Serve static HTML/CSS/JS files using Nginx.

**Requirements:**
- Base image: nginx:alpine
- Copy static files to /usr/share/nginx/html
- Expose port 80
- Configure Nginx if needed

## Technical Requirements

1. **Dockerfile must include:**
   - Appropriate base image
   - Working directory setup
   - Dependency installation
   - Application code copy
   - Port exposure
   - Startup command

2. **.dockerignore file:**
```
node_modules
npm-debug.log
.git
.env
*.md
```
3. **Build and run successfully:**
```
docker build -t projectname:1.0 .
docker run -p 8080:3000 projectname:1.0
```


## Submission Requirements

Create folder `ProjectName_YourGitHubUsername` containing:

1. **Dockerfile** - Container configuration
2. **Application files** - Source code
3. **.dockerignore** - Files to exclude
4. **README.md** - Documentation with:
   - Build instructions
   - Run commands
   - Port mappings
   - Environment variables (if any)
5. **build_log.txt** - Output from successful build

## Best Practices

- Use specific image tags, not `latest`
- Minimize image layers
- Use multi-stage builds for production
- Set non-root user for security
- Document exposed ports
- Keep images small

## Example README.md Template
```
# Project Name
Brief description of the application.

# Build
docker build -t myapp:1.0 .

# Run
docker run -d -p 8080:3000 myapp:1.0

# Access
Open browser to http://localhost:8080

# Environment Variables
PORT: Application port (default: 3000)
```


## Learning Resources

- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Docker Build Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Docker Image Optimization](https://docs.docker.com/build/building/best-practices/)
