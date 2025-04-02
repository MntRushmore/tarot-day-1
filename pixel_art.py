# Use this tool or use index.html for a website
import random

COLORS = ["#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#FFD700", "#8A2BE2", "#00FFFF", "#FF4500", "#ADFF2F", "#FF69B4", "#7FFF00", "#FF1493", "#00BFFF", "#FFD700", "#FF6347"]

grid_size = 30
pixels = [[random.choice(COLORS) for _ in range(grid_size)] for _ in range(grid_size)]

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pixel Art Gen by Rushmore</title>
    <image src="tarot.png" alt="Tarot" style="width: 100px; height: 100px;">
    <style>
        table { border-collapse: collapse; }
        td { width: 20px; height: 20px; }
    </style>
</head>
<body>
    <h2>Tarot Day 1 - Pixel Art Gen</h2>
    <table>
"""

for row in pixels:
    html_content += "        <tr>" + "".join(f'<td style="background-color: {color};"></td>' for color in row) + "</tr>\n"

html_content += """    </table>
</body>
</html>
"""

with open("pixel_art.html", "w") as file:
    file.write(html_content)

print("Random pixel art generated! Open 'pixel_art.html' in your browser.")