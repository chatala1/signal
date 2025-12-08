# GitHub Copilot Agent Usage Guide

This guide provides practical examples of how to use the coding agent in the Wire repository.

## Quick Start

The coding agent is automatically available in GitHub Copilot when working in this repository. You can interact with it through various GitHub interfaces.

## Usage Examples

### 1. In GitHub Copilot Chat

#### Example: Writing a New Feature
```
@coding-agent I need to add a function to parse JSON feed data. 
Can you help me implement this following the repository's coding standards?
```

#### Example: Code Review
```
@coding-agent Please review this code change and suggest improvements
based on the repository's best practices:

[paste code snippet]
```

#### Example: Bug Fixing
```
@coding-agent I'm getting an error when fetching RSS feeds. 
The error is: [error message]. Can you help me debug this?
```

#### Example: Adding Tests
```
@coding-agent Can you help me write unit tests for the feed parsing function? 
The tests should cover edge cases and follow the existing test patterns.
```

### 2. In Pull Request Comments

The coding agent can assist with PR reviews:

```
@coding-agent Can you review the changes in this PR and check if they 
follow our security best practices?
```

### 3. In Issues

Tag the agent for specialized help:

```
@coding-agent This issue involves modifying the RSS feed parser. 
What approach would you recommend that aligns with our minimal changes principle?
```

## Best Practices

### Provide Clear Context

**Good:**
```
@coding-agent I need to add error handling to the fetch_feed.py script.
The script currently doesn't handle network timeouts. Can you suggest
a minimal change that adds timeout handling?
```

**Less Effective:**
```
@coding-agent Fix the feed script
```

### Reference Specific Files

**Good:**
```
@coding-agent In scripts/fetch_feed.py, lines 25-40, can you help me 
refactor this function to make it more maintainable?
```

### Ask for Explanations

```
@coding-agent Can you explain what this code block does and suggest 
if there's a more pythonic way to write it?
```

### Request Validation

```
@coding-agent Can you check if this implementation follows the 
security guidelines in AGENTS.md?
```

## Common Tasks

### Adding a New Feature

1. Describe the feature requirements clearly
2. Ask the agent to suggest an implementation approach
3. Request code that follows repository standards
4. Ask for tests to be included
5. Request documentation updates

**Example:**
```
@coding-agent I need to add support for Atom feeds in addition to RSS.
Can you help me:
1. Suggest where to add this functionality
2. Implement it following our minimal changes principle
3. Add appropriate tests
4. Update any necessary documentation
```

### Debugging

1. Provide the error message or unexpected behavior
2. Include relevant code snippets
3. Mention what you've already tried
4. Ask for debugging steps or fixes

**Example:**
```
@coding-agent The feed parsing is failing with "KeyError: 'link'" when 
processing some feeds. I've checked that the feed is valid XML. Can you 
help me add proper error handling for missing keys?
```

### Refactoring

1. Identify the code that needs refactoring
2. Explain why it needs to be refactored
3. Ask for suggestions that maintain functionality
4. Request tests to verify behavior is preserved

**Example:**
```
@coding-agent The fetch_feed.py function is getting too long (>100 lines).
Can you suggest how to break it into smaller, focused functions while
maintaining the existing behavior?
```

### Security Review

1. Describe the security concern
2. Ask for specific security checks
3. Request recommendations for fixes

**Example:**
```
@coding-agent Can you review the user input handling in this code
and check for potential security vulnerabilities? Specifically,
I'm concerned about injection attacks.
```

## Tips for Effective Agent Interaction

1. **Be Specific**: Provide clear, detailed information about what you need
2. **Provide Context**: Include relevant code, error messages, and background
3. **Reference Standards**: Mention the coding standards or guidelines to follow
4. **Iterate**: Work with the agent iteratively for complex tasks
5. **Review Output**: Always review and test agent suggestions before applying
6. **Ask Questions**: Don't hesitate to ask for clarifications or alternatives
7. **Mention Constraints**: Specify any limitations or requirements upfront

## Limitations

- Agents provide suggestions based on configuration and training data
- Always review agent output before applying changes
- For critical changes, consider peer review in addition to agent assistance
- Agents may not have context about recent changes; provide that explicitly
- Test thoroughly after applying agent suggestions

## Feedback and Improvements

If you notice that the agent:
- Doesn't follow the repository guidelines
- Makes inappropriate suggestions
- Needs additional context or capabilities

Please create an issue or update the agent configuration in `.github/agents/coding-agent.yml`.

## Additional Resources

- [Agent Configuration](./coding-agent.yml) - Full agent configuration
- [Agents README](./README.md) - Overview of all agents
- [AGENTS.md](/AGENTS.md) - General AI agent guidelines
- [Copilot Instructions](../copilot-instructions.md) - Repository Copilot instructions

---

For more information about GitHub Copilot, visit the [official documentation](https://docs.github.com/en/copilot).
