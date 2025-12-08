#!/usr/bin/env python3
"""
Validation script for GitHub Copilot agent configurations.
This script checks that agent configuration files are properly formatted and contain required fields.
"""

import sys
import json
import yaml
from pathlib import Path


def validate_yaml_file(filepath):
    """Validate a YAML configuration file."""
    print(f"Validating {filepath}...")
    
    try:
        with open(filepath, 'r') as f:
            config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"  ❌ YAML syntax error: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Error reading file: {e}")
        return False
    
    # Check required fields
    required_fields = ['name', 'description', 'version', 'capabilities', 'instructions']
    missing_fields = [field for field in required_fields if field not in config]
    
    if missing_fields:
        print(f"  ❌ Missing required fields: {', '.join(missing_fields)}")
        return False
    
    # Check field types
    if not isinstance(config['name'], str):
        print(f"  ❌ 'name' must be a string")
        return False
    
    if not isinstance(config['description'], str):
        print(f"  ❌ 'description' must be a string")
        return False
    
    if not isinstance(config['capabilities'], list):
        print(f"  ❌ 'capabilities' must be a list")
        return False
    
    if not isinstance(config['instructions'], str):
        print(f"  ❌ 'instructions' must be a string")
        return False
    
    # Check version format (should be semantic versioning)
    version = str(config['version'])
    version_parts = version.split('.')
    if len(version_parts) != 3:
        print(f"  ⚠️  Warning: version should follow semantic versioning (major.minor.patch)")
    else:
        # Validate that each part is a valid integer
        for i, part in enumerate(version_parts):
            if not part.isdigit():
                print(f"  ⚠️  Warning: version part {i} ('{part}') should be a number")
                break
    
    # Validate optional fields if present
    if 'languages' in config and not isinstance(config['languages'], list):
        print(f"  ❌ 'languages' must be a list")
        return False
    
    if 'context_files' in config and not isinstance(config['context_files'], list):
        print(f"  ❌ 'context_files' must be a list")
        return False
    
    if 'tools' in config and not isinstance(config['tools'], list):
        print(f"  ❌ 'tools' must be a list")
        return False
    
    if 'preferences' in config and not isinstance(config['preferences'], dict):
        print(f"  ❌ 'preferences' must be a dictionary")
        return False
    
    # Check that context files exist
    if 'context_files' in config:
        agents_dir = Path(filepath).parent
        repo_root = agents_dir.parent.parent
        
        for context_file in config['context_files']:
            file_path = repo_root / context_file
            if not file_path.exists():
                print(f"  ⚠️  Warning: context file not found: {context_file}")
    
    print(f"  ✅ Valid agent configuration")
    return True


def validate_json_index(filepath):
    """Validate the agents.json index file."""
    print(f"Validating {filepath}...")
    
    try:
        with open(filepath, 'r') as f:
            index = json.load(f)
    except json.JSONDecodeError as e:
        print(f"  ❌ JSON syntax error: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Error reading file: {e}")
        return False
    
    # Check required fields
    if 'agents' not in index:
        print(f"  ❌ Missing 'agents' field")
        return False
    
    if not isinstance(index['agents'], list):
        print(f"  ❌ 'agents' must be a list")
        return False
    
    # Validate each agent entry
    for i, agent in enumerate(index['agents']):
        required_agent_fields = ['id', 'name', 'description', 'version', 'config_file']
        missing = [field for field in required_agent_fields if field not in agent]
        
        if missing:
            print(f"  ❌ Agent {i}: Missing fields: {', '.join(missing)}")
            return False
        
        # Check that config file exists
        agents_dir = Path(filepath).parent
        config_file = agents_dir / agent['config_file']
        if not config_file.exists():
            print(f"  ❌ Agent {i}: Config file not found: {agent['config_file']}")
            return False
    
    print(f"  ✅ Valid agents index")
    return True


def main():
    """Main validation function."""
    script_dir = Path(__file__).parent
    
    print("=" * 60)
    print("GitHub Copilot Agent Configuration Validator")
    print("=" * 60)
    print()
    
    all_valid = True
    
    # Find and validate all YAML agent configurations
    yaml_files = list(script_dir.glob("*.yml")) + list(script_dir.glob("*.yaml"))
    
    if not yaml_files:
        print("⚠️  No agent configuration files found (.yml or .yaml)")
    
    for yaml_file in yaml_files:
        if not validate_yaml_file(yaml_file):
            all_valid = False
        print()
    
    # Validate agents.json if it exists
    json_index = script_dir / "agents.json"
    if json_index.exists():
        if not validate_json_index(json_index):
            all_valid = False
        print()
    else:
        print("ℹ️  agents.json not found (optional)")
        print()
    
    # Summary
    print("=" * 60)
    if all_valid:
        print("✅ All validations passed!")
        return 0
    else:
        print("❌ Validation failed. Please fix the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
