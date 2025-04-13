import tkinter as tk
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

strokes = []  # list of strokes, each stroke is (x_list, y_list)
current_stroke = ([], [])

def start_stroke(event):
    current_stroke[0].append(event.x)
    current_stroke[1].append(event.y)

def draw_stroke(event):
    canvas.create_line(event.x, event.y, event.x + 1, event.y + 1)
    current_stroke[0].append(event.x)
    current_stroke[1].append(event.y)

def end_stroke(event):
    global strokes
    strokes.append((current_stroke[0][:], current_stroke[1][:]))
    current_stroke[0].clear()
    current_stroke[1].clear()

def get_square_bbox_with_padding(strokes, padding=20):
    x_all = []
    y_all = []

    for x, y in strokes:
        x_all.extend(x)
        y_all.extend(y)

    x_min, x_max = min(x_all), max(x_all)
    y_min, y_max = min(y_all), max(y_all)

    width = x_max - x_min
    height = y_max - y_min
    max_dim = max(width, height)

    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2

    half_dim = max_dim / 2 + padding

    square_x_min = int(max(x_center - half_dim, 0))
    square_x_max = int(min(x_center + half_dim, canvas_size))
    square_y_min = int(max(y_center - half_dim, 0))
    square_y_max = int(min(y_center + half_dim, canvas_size))

    return square_x_min, square_y_min, square_x_max, square_y_max

def submit():
    # Create image and draw strokes
    img = Image.new("RGB", (canvas_size, canvas_size), "white")
    draw = ImageDraw.Draw(img)

    for x, y in strokes:
        points = list(zip(x, y))
        draw.line(points, fill="black", width=2)

    # Calculate bounding box
    bbox = get_square_bbox_with_padding(strokes, padding=10)
    draw.rectangle(bbox, outline="red", width=2)

    # Show image with bounding box
    plt.imshow(img)
    plt.axis('off')
    plt.title("Doodle with Bounding Box")
    plt.show()

    # Save stroke data (optional)
    with open("my_drawing_strokes.txt", "w") as f:
        f.write(str(strokes))

    print("Drawing and bounding box complete!")

# --- Set up the UI ---
canvas_size = 256
root = tk.Tk()
root.title("Draw something!")

canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
canvas.pack()

canvas.bind("<Button-1>", start_stroke)
canvas.bind("<B1-Motion>", draw_stroke)
canvas.bind("<ButtonRelease-1>", end_stroke)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=10)

root.mainloop()
