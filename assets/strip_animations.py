import re
import sys

def strip_animate(filename):
    with open(filename, 'r') as f:
        content = f.read()
    
    # Remove all <animate ... /> tags
    # We will use regex to find <animate ... /> and remove it, but keep the parent polygon's end tag </polygon>
    
    # Also some animations might be in `<animate ...></animate>` format but here they are `<animate ... />`
    cleaned = re.sub(r'<animate[^>]*/>', '', content)
    
    # We need to make sure we don't leave empty `<polygon ...></polygon>` if we can just close it, 
    # but the browser parses `<polygon ...></polygon>` fine even if empty.
    
    with open(filename, 'w') as f:
        f.write(cleaned)
    print(f"Stripped animations from {filename}")

strip_animate('panel-3d-city.svg')
strip_animate('panel-skyline.svg')
