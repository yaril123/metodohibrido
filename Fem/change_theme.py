import os
import glob
import re

directory = "/Users/davidcapdevila/Metodohibrido3/Fem"
html_files = glob.glob(os.path.join(directory, "*.html"))

# We want to replace gold/yellow colors with pink/feminine colors
replacements = {
    "#facc15": "#f472b6", # yellow-400 to pink-400
    "#ca8a04": "#db2777", # yellow-600 to pink-600
    "yellow-400": "pink-400",
    "yellow-500": "pink-500",
    "yellow-600": "pink-600",
    "yellow-700": "pink-700",
    "timer-yellow": "timer-pink"
}

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
        
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

