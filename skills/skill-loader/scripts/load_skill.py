#!/usr/bin/env python3
"""
Skill Loader Script
Loads an overview of all available skills into the context.
If a skill name is provided, it loads that specific skill's full documentation.

Usage:
    python load_skill.py          # Load overview of all skills
    python load_skill.py <name>   # Load specific skill details
"""

import os
import sys
import re
from pathlib import Path

def get_skill_info(skill_dir):
    readme_path = skill_dir / "README.md"
    if not readme_path.exists():
        return None
    
    try:
        content = readme_path.read_text(encoding='utf-8')
    except Exception:
        return None
    
    # Default values
    name = skill_dir.name
    description = "No description available."
    
    # Try to parse YAML frontmatter
    frontmatter_match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        name_match = re.search(r'^name:\s*(.*)$', frontmatter, re.MULTILINE)
        desc_match = re.search(r'^description:\s*(.*)$', frontmatter, re.MULTILINE)
        if name_match:
            name = name_match.group(1).strip().strip('"').strip("'")
        if desc_match:
            description = desc_match.group(1).strip().strip('"').strip("'")
    else:
        # Fallback to first heading and first non-empty line
        lines = content.split('\n')
        found_heading = False
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith('#'):
                found_heading = True
                if not name or name == skill_dir.name:
                    name = line.lstrip('#').strip()
                continue
            if found_heading and not line.startswith('>') and not line.startswith('!['):
                description = line
                break
                
    return {"id": skill_dir.name, "name": name, "description": description}

def main():
    skills_dir = Path("/workspace/skills")
    
    if not skills_dir.exists():
        print(f"Error: Skills directory not found at {skills_dir}")
        return 1

    # If an argument is provided, load specific skill
    if len(sys.argv) > 1:
        skill_id = sys.argv[1]
        skill_path = skills_dir / skill_id / "README.md"
        
        if not skill_path.exists():
            print(f"Error: Skill '{skill_id}' not found.")
            return 1
            
        print(f"\n--- LOADING SPECIFIC SKILL: {skill_id} ---")
        print(skill_path.read_text(encoding='utf-8'))
        print(f"\n--- SKILL {skill_id} FULLY LOADED ---")
        return 0

    # Otherwise, load overview
    print("\n--- LOADING SKILLS REPOSITORY OVERVIEW ---")
    print("Below is a list of available skills in the repository. Each entry includes the skill ID, name, and a brief description.")
    print("To use a skill, refer to its ID. If you need detailed instructions or the full workflow for a skill, please read its specific README.md file.")
    print("\n| Skill ID | Name | Description |")
    print("| :--- | :--- | :--- |")
    
    skills = []
    for d in sorted(skills_dir.iterdir()):
        if d.is_dir():
            info = get_skill_info(d)
            if info:
                skills.append(info)
    
    for s in skills:
        print(f"| {s['id']} | {s['name']} | {s['description']} |")
    
    print("\n--- OVERVIEW LOADED ---")
    print("💡 HINT: If you need to perform a task covered by one of these skills, you can read more details in `skills/<skill_id>/README.md` or run `python skills/skill-loader/scripts/load_skill.py <skill_id>` to load it fully.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
