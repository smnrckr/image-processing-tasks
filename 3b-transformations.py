import numpy as np
import matplotlib.pyplot as plt
import math

def create_cube_points(size=1):
    s = size / 2
    points = np.array([
        [-s, -s, -s, 1],
        [ s, -s, -s, 1],
        [ s,  s, -s, 1],
        [-s,  s, -s, 1],
        [-s, -s,  s, 1],
        [ s, -s,  s, 1],
        [ s,  s,  s, 1],
        [-s,  s,  s, 1]
    ], dtype=np.float64).T 
    return points

def create_transformation_matrices(scale=(1,1,1), rotate=(0,0,0), translate=(0,0,0)):
    sx, sy, sz = scale
    rx, ry, rz = [math.radians(a) for a in rotate]
    tx, ty, tz = translate

    scale_matrix = np.array([
        [sx, 0,  0,  0],
        [0,  sy, 0,  0],
        [0,  0,  sz, 0],
        [0,  0,  0,  1]
    ])

    rot_x = np.array([
        [1, 0, 0, 0],
        [0, math.cos(rx), -math.sin(rx), 0],
        [0, math.sin(rx),  math.cos(rx), 0],
        [0, 0, 0, 1]
    ])

    rot_y = np.array([
        [math.cos(ry), 0, math.sin(ry), 0],
        [0, 1, 0, 0],
        [-math.sin(ry), 0, math.cos(ry), 0],
        [0, 0, 0, 1]
    ])

    rot_z = np.array([
        [math.cos(rz), -math.sin(rz), 0, 0],
        [math.sin(rz),  math.cos(rz), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    translation_matrix = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])

    rotation_matrix = rot_z @ rot_y @ rot_x
    combined = translation_matrix @ rotation_matrix @ scale_matrix

    return {
        "scale": scale_matrix,
        "rotate": rotation_matrix,
        "translate": translation_matrix,
        "combined": combined
    }

def apply_transformation(points, matrix):
    transformed = matrix @ points
    transformed /= transformed[3]
    return transformed

def draw_cube(ax, points, title):
    edges = [
        (0,1), (1,2), (2,3), (3,0),
        (4,5), (5,6), (6,7), (7,4),
        (0,4), (1,5), (2,6), (3,7)
    ]
    x, y, z = points[:3]

    for i, j in edges:
        ax.plot([x[i], x[j]], [y[i], y[j]], [z[i], z[j]], color="blue")

    ax.set_title(title)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    ax.set_box_aspect([1, 1, 1])
    ax.grid(True)

def main():
    cube_points = create_cube_points(size=1)

    scale = (1.5, 1.5, 1.5)
    rotate = (30, 45, 60)
    translate = (1, 1, 1)

    matrices = create_transformation_matrices(scale, rotate, translate)

    transformed_shapes = {
        "Orijinal Küp": cube_points,
        "Ölçeklenmiş": apply_transformation(cube_points, matrices["scale"]),
        "Döndürülmüş": apply_transformation(cube_points, matrices["rotate"]),
        "Ötelenmiş": apply_transformation(cube_points, matrices["translate"]),
        "Tüm Dönüşümler": apply_transformation(cube_points, matrices["combined"])
    }

    fig = plt.figure(figsize=(20, 10))
    for i, (title, points) in enumerate(transformed_shapes.items(), 1):
        ax = fig.add_subplot(2, 3, i, projection='3d')
        draw_cube(ax, points, title)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
