import math
import SpaceClaim.Api.V22 as sc

# Parameters
a = 10.0  # semi-major axis
b = 5.0   # semi-minor axis
turns = 5
points_per_turn = 100
spacing = 1.0  # spiral spacing factor

# Create list of points
points = []
for i in range(turns * points_per_turn):
    theta = 2 * math.pi * i / points_per_turn
    r = spacing * theta / (2 * math.pi)  # Archimedean spiral-like growth
    x = a * r * math.cos(theta)
    y = b * r * math.sin(theta)
    z = 0  # flat on XY plane
    points.append(sc.Point.Create(x, y, z))

# Draw the spiral using a curve through points
design = sc.Application.GetActiveDocument().MainPart
curve = design.SketchCurve.CreateThroughPoints(points)
