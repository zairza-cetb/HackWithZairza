# Generative AI

This folder contains projects utilizing large language models and generative AI APIs. Projects are organized by complexity, from prompt engineering to building complete AI-powered applications with multi-modal capabilities.

## Project Levels

### Level 1: Prompt Library Curation
Curated collection of effective prompts for various use cases including coding, writing, debugging, and productivity. Focus on prompt engineering techniques and documentation.

**Skills:** Prompt engineering, documentation, use case analysis, result evaluation

### Level 2: Simple API Wrappers
Basic implementations wrapping ChatGPT or Claude APIs for specific tasks. Projects include command-line interfaces and simple Python/Node.js scripts.

**Skills:** API integration, HTTP requests, authentication, error handling, basic CLI

### Level 3: AI-Powered CLI Tools
Production-ready command-line tools leveraging AI for developer workflows. Projects include commit message generators, code explainers, and documentation assistants.

**Skills:** CLI development, API integration, argument parsing, file handling, output formatting

### Level 4: Multi-Modal AI Applications
Advanced applications processing both text and images using AI models. Projects combine multiple APIs and implement complex workflows.

**Skills:** Multi-modal processing, API orchestration, image handling, async operations, advanced features

## Prerequisites

- Programming knowledge (Python or JavaScript)
- Understanding of API requests
- API key from OpenAI or Anthropic
- Basic command-line usage

## API Requirements

**OpenAI (ChatGPT):**
- Account: https://platform.openai.com/signup
- API Key: https://platform.openai.com/api-keys
- Documentation: https://platform.openai.com/docs

**Anthropic (Claude):**
- Account: https://console.anthropic.com/
- API Key: https://console.anthropic.com/settings/keys
- Documentation: https://docs.anthropic.com/

## Security Best Practices

- Never commit API keys to repository
- Use environment variables for credentials
- Include `.env.example` with placeholder values
- Add `.env` to `.gitignore`
- Document API key setup in README

## Submission Format

Create a folder `ProjectName_YourGitHubUsername` containing:

- Source code files
- `README.md` with setup and usage instructions
- `.env.example` for API key template
- `requirements.txt` or `package.json` for dependencies
- Example outputs or screenshots

## Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic Claude API Guide](https://docs.anthropic.com/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
