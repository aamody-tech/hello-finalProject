from PIL import Image, ImageDraw
import random


def generate_art():
    print("Generating Art!")
    image_size_px = 128
    padding_px = int(12.8)  # 10%
    image_bg_color = (255, 255, 255)
    image = Image.new("RGB", size=(image_size_px, image_size_px), color=image_bg_color)

    # Draw Some Lines
    draw = ImageDraw.Draw(image)
    points = []

    # Generate Points
    for thisthing in range(10):
        random_point = (
            random.randint(padding_px, image_size_px - padding_px),
            random.randint(padding_px, image_size_px - padding_px),
        )
        points.append(random_point)

    # Draw The Points
    for i, point in enumerate(points):
        p1 = point

        if i == len(points) - 1:
            p2 = points[0]
        else:
            p2 = points[i + 1]

        line_xy = (p1, p2)
        line_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        draw.line(line_xy, fill=line_color)

    image.save("test_image.png")


if __name__ == "__main__":
    generate_art()
