import sys
import re

def wrap_snake(input_path, output_path):
    with open(input_path, 'r') as f:
        svg_content = f.read()

    # The raw snake SVG from Platane/snk is roughly 854x170 or something similar.
    # It has its own <svg> tag. We will strip the XML declaration if any, 
    # but keep the <svg> tag so it embeds cleanly as a nested SVG.
    
    # We also want to replace the background color if it's there.
    svg_content = re.sub(r'fill:\s*#161b22', 'fill: #0D1117', svg_content)
    svg_content = re.sub(r'fill:\s*#0e4429', 'fill: #161B22', svg_content)
    svg_content = re.sub(r'fill:\s*#006d32', 'fill: #30363D', svg_content)
    svg_content = re.sub(r'fill:\s*#26a641', 'fill: #8B1D2C', svg_content)
    svg_content = re.sub(r'fill:\s*#39d353', 'fill: #FF2E4D', svg_content)
    
    # Just in case Platane/snk used palette colors, replace those too:
    svg_content = svg_content.replace('#161b22', '#0D1117')
    svg_content = svg_content.replace('#0e4429', '#161B22')
    svg_content = svg_content.replace('#006d32', '#30363D')
    svg_content = svg_content.replace('#26a641', '#8B1D2C')
    svg_content = svg_content.replace('#39d353', '#FF2E4D')

    # Remove any black/dark background rect that snk might add by default
    svg_content = re.sub(r'<rect[^>]*width="100%"[^>]*height="100%"[^>]*>', '', svg_content)
    
    # The wrapper SVG (FPGA Die style)
    # The snake is usually around 800-900px wide. We'll give it a 1240x340 frame.
    wrapper = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1240 340" width="1240" height="340" role="img" aria-label="Contribution Activity">
<rect width="1240" height="340" fill="#0D1117"/>
<!-- Borders -->
<rect x="0" y="0" width="3" height="340" fill="#FF2E4D" fill-opacity="0.8"/>
<rect x="1237" y="0" width="3" height="340" fill="#FF2E4D" fill-opacity="0.3"/>
<rect x="0" y="0" width="1240" height="2" fill="#FF2E4D" fill-opacity="0.5"/>
<rect x="0" y="338" width="1240" height="2" fill="#FF2E4D" fill-opacity="0.5"/>
<!-- Corner brackets -->
<g stroke="#FF2E4D" stroke-width="1.5" fill="none" stroke-opacity="0.8">
  <line x1="28" y1="326" x2="28" y2="312"/>
  <line x1="28" y1="326" x2="42" y2="326"/>
  <line x1="1212" y1="326" x2="1212" y2="312"/>
  <line x1="1212" y1="326" x2="1198" y2="326"/>
</g>
<!-- Header -->
<text x="28" y="24" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9" fill="#FF2E4D" letter-spacing="3">SILICON DIE // CONTRIBUTION TELEMETRY</text>
<text x="1212" y="24" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="9" fill="#FF2E4D" letter-spacing="3" text-anchor="end">REAL-TIME</text>
<rect x="28" y="30" width="1184" height="1" fill="#FF2E4D" fill-opacity="0.2"/>

<!-- Nested Snake SVG -->
<!-- We center it. 1240/2 = 620. Let's assume snake width is roughly 850. X = (1240-850)/2 = 195 -->
<!-- Y = 80 -->
<g transform="translate(195, 80)">
    {svg_content}
</g>

<!-- Scanning line over the whole board -->
<rect x="195" y="60" width="2" height="200" fill="#FF2E4D" fill-opacity="0.12">
  <animateTransform attributeName="transform" type="translate" values="0 0;850 0;0 0" dur="8s" repeatCount="indefinite"/>
</rect>
</svg>
'''
    with open(output_path, 'w') as f:
        f.write(wrapper)

if __name__ == '__main__':
    wrap_snake(sys.argv[1], sys.argv[2])
