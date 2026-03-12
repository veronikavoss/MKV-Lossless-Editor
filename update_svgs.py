import os
import re

svGs = [
    "end_button.svg", "end_point.svg", "frame_next.svg", "frame_pre.svg", 
    "next.svg", "open.svg", "pause.svg", "play.svg", "pre.svg", "reset.svg", 
    "start_button.svg", "start_point.svg", "stop.svg", "volume_max.svg", "volume_mute.svg"
]

basedir = r"d:\Coding\Gemini\mkvsplitter\assets"
for s in svGs:
    p = os.path.join(basedir, s)
    if not os.path.exists(p):
        print(f"File not found: {s}")
        continue
        
    with open(p, "r", encoding="utf-8") as f:
        data = f.read()
    
    # Remove XML style blocks which Qt ignores
    data = re.sub(r'<style\b[^>]*>.*?</style>', '', data, flags=re.DOTALL|re.IGNORECASE)
    
    # Replace class="s0" or similar with fill="#FFFFFF" on paths
    # Because fill attributes are what Qt supports
    data = re.sub(r'class="[^"]+"', 'fill="#FFFFFF"', data)
    
    # If a path has no fill attribute and no class attribute, add fill="#FFFFFF"
    data = re.sub(r'<path(?![^>]*\bfill=)[^>]*>', lambda m: m.group(0).replace('<path', '<path fill="#FFFFFF"'), data)
    
    with open(p, "w", encoding="utf-8") as f:
        f.write(data)
    
print("Updated basic SVGs to white.")
