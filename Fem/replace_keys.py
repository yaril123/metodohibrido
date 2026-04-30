import os
import glob

directory = "/Users/davidcapdevila/Metodohibrido3/Fem"
html_files = glob.glob(os.path.join(directory, "*.html"))

replacements = {
    "'workoutHistory'": "'fem_workoutHistory'",
    '"workoutHistory"': '"fem_workoutHistory"',
    "'progressionFlags'": "'fem_progressionFlags'",
    '"progressionFlags"': '"fem_progressionFlags"',
    "'bilboCycleCount'": "'fem_bilboCycleCount'",
    '"bilboCycleCount"': '"fem_bilboCycleCount"',
    "'bilboPushCycleEnded'": "'fem_bilboPushCycleEnded'",
    '"bilboPushCycleEnded"': '"fem_bilboPushCycleEnded"',
    "'bilboPullCycleEnded'": "'fem_bilboPullCycleEnded'",
    '"bilboPullCycleEnded"': '"fem_bilboPullCycleEnded"',
    "'bilboResetFlags'": "'fem_bilboResetFlags'",
    '"bilboResetFlags"': '"fem_bilboResetFlags"',
    "'workoutProgress'": "'fem_workoutProgress'",
    '"workoutProgress"': '"fem_workoutProgress"',
    "'compactMode'": "'fem_compactMode'",
    '"compactMode"': '"fem_compactMode"',
    "'timerSounds'": "'fem_timerSounds'",
    '"timerSounds"': '"fem_timerSounds"',
    "'lastUpdated'": "'fem_lastUpdated'",
    '"lastUpdated"': '"fem_lastUpdated"',
    "'metodo-hibrido-data'": "'metodo-hibrido-fem-data'",
    '"metodo-hibrido-data"': '"metodo-hibrido-fem-data"'
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
