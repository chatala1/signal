# GitHub Copilot Agents

This directory contains configuration files for GitHub Copilot agents used in the Wire repository. These agents are specialized AI assistants designed to help with specific aspects of software development.

## Available Agents

### Coding Agent (`coding-agent.yml`)

A specialized agent focused on code development, testing, and maintenance.

**Capabilities:**
- Code writing and refactoring
- Code review and debugging
- Test creation and execution
- Documentation updates
- Security best practices

**Supported Languages:**
- Python
- JavaScript
- HTML/CSS
- YAML
- Markdown
- Bash

**When to Use:**
- Writing new features or components
- Fixing bugs and issues
- Refactoring existing code
- Adding tests for untested code
- Improving code quality
- Updating documentation

**Key Principles:**
1. **Minimal Changes**: Make the smallest changes necessary to solve the problem
2. **Security First**: Always consider security implications
3. **Test Coverage**: Ensure changes are properly tested
4. **Documentation**: Keep documentation up to date
5. **Code Quality**: Follow established patterns and best practices

## Using Agents

### In GitHub Copilot Chat

You can invoke agents in GitHub Copilot Chat using the `@` mention syntax:

```
@coding-agent Please help me implement a new feature for parsing RSS feeds
```

### In Pull Requests

Agents can automatically assist with:
- Code review comments
- Suggesting improvements
- Identifying potential issues
- Recommending best practices

### In Issues

Tag agents in issue comments to get specialized help:

```
@coding-agent Can you analyze this bug and suggest a fix?
```

## Agent Configuration

Each agent is configured using a YAML file with the following structure:

```yaml
name: Agent Name
description: Brief description of the agent's purpose
version: 1.0.0
capabilities: [list of capabilities]
languages: [list of programming languages]
instructions: |
  Detailed instructions for the agent's behavior
context_files: [list of files the agent should reference]
tools: [list of tools the agent uses]
preferences: {agent behavior settings}
```

## Adding New Agents

To add a new specialized agent:

1. Create a new YAML file in this directory (e.g., `new-agent.yml`)
2. Define the agent's name, description, and capabilities
3. Provide detailed instructions for the agent's behavior
4. List relevant context files and tools
5. Set appropriate preferences
6. Update this README with information about the new agent

## Best Practices

### For Agent Configuration

- **Clear Instructions**: Provide specific, actionable guidance
- **Context Awareness**: Reference relevant documentation and files
- **Focused Scope**: Keep agents specialized rather than general-purpose
- **Consistent Formatting**: Follow the established YAML structure
- **Version Control**: Update version numbers when making significant changes

### For Using Agents

- **Specific Requests**: Provide clear context and requirements
- **Right Agent**: Choose the agent best suited for your task
- **Provide Context**: Include relevant information about the problem
- **Review Output**: Always review agent suggestions before applying them
- **Iterate**: Work with agents iteratively for complex tasks

## Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [AGENTS.md](/AGENTS.md) - General AI agent guidelines
- [copilot-instructions.md](../copilot-instructions.md) - Repository Copilot instructions
- [README.md](/README.md) - Project overview

## Maintenance

Agents should be reviewed and updated periodically to:
- Reflect changes in the codebase
- Incorporate new best practices
- Add support for new languages or tools
- Improve instructions based on usage patterns
- Update context files and resources

---

Last updated: 2025-12-08
