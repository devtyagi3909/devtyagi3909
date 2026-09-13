import sys

ascii_art = r"""
       .zeeeeee..        
    .e$*"    "*$e.       
  .$"            "$.     
 .$                $.    
4$                  $F   
4$                  $F   
 $       (o)  (o)   $    
 4r        ()       J    
  $     \      /   $     
  "$c    '----'  c$"     
    "$$$e......e$$"      
       ""*$$$$*""        
"""

lines = ascii_art.strip('\n').split('\n')
tspan_elements = ""
for i, line in enumerate(lines):
    escaped_line = line.replace('<', '&lt;').replace('>', '&gt;').replace(' ', '&#160;')
    tspan_elements += f'<tspan x="30" dy="{20 if i > 0 else 0}">{escaped_line}</tspan>\n'

svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" width="800" height="400">
<rect width="100%" height="100%" fill="#0d1117" rx="15" />
<style>
    .key {{ fill: #ff7b72; font-weight: bold; }}
    .val {{ fill: #c9d1d9; }}
    .ascii {{ fill: #c9d1d9; font-family: 'Courier New', Courier, monospace; white-space: pre; }}
</style>
<g font-family="Courier, monospace" font-size="14" fill="#c9d1d9">
<text x="30" y="50" class="ascii" xml:space="preserve">
{tspan_elements}
</text>
<text x="350" y="50" font-weight="bold" fill="#58a6ff">devtyagi<tspan fill="#c9d1d9">@</tspan><tspan fill="#3fb950">ai-engineer</tspan></text>
<text x="350" y="70">-------------------------</text>
<text x="350" y="100"><tspan class="key">OS</tspan><tspan class="val">: Neural OS (Arch-based)</tspan></text>
<text x="350" y="120"><tspan class="key">Host</tspan><tspan class="val">: Cortex-M9 Brain Interface</tspan></text>
<text x="350" y="140"><tspan class="key">Uptime</tspan><tspan class="val">: 24/7 Model Training</tspan></text>
<text x="350" y="160"><tspan class="key">Packages</tspan><tspan class="val">: 9999 (pip), 101 (conda)</tspan></text>
<text x="350" y="180"><tspan class="key">Shell</tspan><tspan class="val">: zsh (AI assisted)</tspan></text>
<text x="350" y="200"><tspan class="key">Resolution</tspan><tspan class="val">: 4K Vision</tspan></text>
<text x="350" y="220"><tspan class="key">DE</tspan><tspan class="val">: PyTorch &amp; JAX</tspan></text>
<text x="350" y="240"><tspan class="key">WM</tspan><tspan class="val">: Transformer Architecture</tspan></text>
<text x="350" y="260"><tspan class="key">Theme</tspan><tspan class="val">: Dark Mode (Always)</tspan></text>
<text x="350" y="280"><tspan class="key">Terminal</tspan><tspan class="val">: Alacritty</tspan></text>
<text x="350" y="300"><tspan class="key">CPU</tspan><tspan class="val">: Brain (1 Trillion Parameters)</tspan></text>
<text x="350" y="320"><tspan class="key">GPU</tspan><tspan class="val">: 8x NVIDIA H100 80GB (Dreaming)</tspan></text>
<text x="350" y="340"><tspan class="key">Memory</tspan><tspan class="val">: 100TB VRAM</tspan></text>
</g>
</svg>
"""

with open('neofetch.svg', 'w') as f:
    f.write(svg_template)
print("Generated neofetch.svg")
