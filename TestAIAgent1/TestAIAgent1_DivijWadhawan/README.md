# AI Agent Template

A template for building AI agents using LangGraph and image generation capabilities. This template provides a structured foundation for implementing custom AI workflows with proper isolation and deployment capabilities.

## Overview

This template helps you:
- Build AI agents using the LangGraph wrapper GRU library
- Generate images as part of your AI workflow
- Package and deploy your agent as a Docker container
- Maintain configuration separately from code
- Quick bootstrapping using GRU CLI

## Directory Structure

```
.
├── .dockerignore          # Specifies files to exclude from Docker build
├── .env.example           # file with required credentials
├── Dockerfile            # Instructions for building Docker image
├── README.md            # This documentation
├── config.yaml          # Agent configuration settings
├── requirements.txt     # Python package dependencies
└── src/                # Source code directory
    └── main.py         # Main entry point for your agent
```

## Prerequisites

- Docker installed on your machine
- Python 3.9 or higher
- GRU CLI installed (`pip install gru-cli`)
- API keys for required services (OpenAI, Stability AI, etc.)

## Getting Started

1. **Create Project Structure**
   ```bash
   # Creates the basic folder structure and template files
   gru agent create_bootstrap
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Your Agent**
   - Set up your `.env` file with required credentials
   - Modify `config.yaml` for agent-specific settings

4. **Implement Your Workflow**
   - Open `src/main.py`
   - Implement your LangGraph workflow
   ```python
   def main():
       # 1. Initialize your agent
       # 2. Define workflow steps
       # 3. Execute the workflow
   ```

## Building and Deploying

1. **Build Docker Image**
   ```bash
   docker build -t registry.canso.ai/agent-name:version .
   ```

2. **Push to Registry**
   ```bash
   docker push registry.canso.ai/agent-name:version
   ```

## Best Practices

1. **Code Organization**
   - Keep `main.py` focused on workflow logic
   - Use utils directory for helper functions
   - Separate configuration from code

2. **Docker Best Practices**
   - Keep images minimal
   - Use appropriate base images
   - Include only necessary files

3. **Security**
   - Never commit API keys or `.env` files
   - Use environment variables for secrets
   - Keep dependencies updated
   - Follow least privilege principle

## Common Issues

1. **GRU CLI Issues**
   - Ensure latest version is installed
   - Check command syntax
   - Verify Python environment

2. **Docker Build Issues**
   - Verify Dockerfile syntax
   - Check registry permissions
   - Ensure all required files are present

---

**Note**: This template is designed to be a starting point. Modify it according to your specific needs and requirements.
