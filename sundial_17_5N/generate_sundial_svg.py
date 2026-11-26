"""
Horizontal Sundial Dial & Gnomon Generator for Latitude 17.5 deg N (Hyderabad)
Author: Dr Ravi Raja Pothineni (ASTRO)
Usage: python generate_sundial_svg.py
Output: horizontal_sundial_17_5N.svg (A4 printable)
"""
import math

LATITUDE_DEG = 17.5
PHI = math.radians(LATITUDE_DEG)
WIDTH, HEIGHT = 800, 560
CX, CY = 400, 440
RADIUS = 300

svg_lines = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
    '<rect width="100%" height="100%" fill="white"/>',
    f'<text x="400" y="40" text-anchor="middle" font-family="Arial" font-size="18" font-weight="bold">Horizontal Sundial Dial (Latitude {LATITUDE_DEG} deg N - Hyderabad)</text>',
    f'<text x="400" y="62" text-anchor="middle" font-family="Arial" font-size="12">Align 12:00 Noon line to True Geographic North | Gnomon angle = {LATITUDE_DEG} deg</text>',
    f'<path d="M {CX - RADIUS} {CY} A {RADIUS} {RADIUS} 0 0 1 {CX + RADIUS} {CY}" fill="none" stroke="#1B365D" stroke-width="2"/>',
    f'<line x1="{CX - RADIUS - 20}" y1="{CY}" x2="{CX + RADIUS + 20}" y2="{CY}" stroke="#1B365D" stroke-width="1.5"/>',
]

# Hour lines from 6 AM (-6) to 6 PM (+6)
for h in range(-6, 7):
    hour_angle = math.radians(15.0 * h)
    # tan(theta) = sin(phi) * tan(H)
    theta = math.atan2(math.sin(PHI) * math.sin(hour_angle), math.cos(hour_angle))
    x2 = CX + RADIUS * math.sin(theta)
    y2 = CY - RADIUS * math.cos(theta)
    lx = CX + (RADIUS + 24) * math.sin(theta)
    ly = CY - (RADIUS + 24) * math.cos(theta)
    clock_hour = (12 + h) if (12 + h) <= 12 else (h)
    label = f"{clock_hour}:00"
    svg_lines.append(f'<line x1="{CX}" y1="{CY}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#2B6CB0" stroke-width="1.4"/>')
    svg_lines.append(f'<text x="{lx:.2f}" y="{ly:.2f}" text-anchor="middle" dominant-baseline="middle" font-family="Arial" font-size="12" font-weight="bold">{label}</text>')

# Printable right-triangle gnomon template in upper-left corner
gx, gy, g_base = 60, 210, 180
g_height = g_base * math.tan(PHI)
svg_lines.extend([
    f'<polygon points="{gx},{gy} {gx + g_base},{gy} {gx + g_base},{gy - g_height:.2f}" fill="#EDF2F7" stroke="#1B365D" stroke-width="1.5"/>',
    f'<text x="{gx + g_base/2:.1f}" y="{gy + 16}" text-anchor="middle" font-family="Arial" font-size="11">Cut &amp; fold Gnomon (Angle = {LATITUDE_DEG} deg)</text>',
    '</svg>'
])

with open("horizontal_sundial_17_5N.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(svg_lines))

print("Generated horizontal_sundial_17_5N.svg successfully.")
