from curses import start_color
from PIL import Image, ImageDraw, ImageChops
import random
import colorsys


def choose_color():  # did not end up using this fxn - added it directly to the generate_art fxn
    print(
        "What color do you want to start the picture with? (R = red, B = blue, Y = yellow)"
    )
    start_color = input()
    print("Great choice? What about your end color? (R = red, B = blue, G = green")
    end_color = input()

    if start_color == "R" or start_color == "red":
        r = random.random(255)
        g = 0
        b = 0
    elif start_color == "G" or start_color == "green":
        r = 0
        g = random.random(255)
        b = 0
    elif start_color == "B" or start_color == "blue":
        r = 0
        g = 0
        b = random.random(255)

    float_hsv = colorsys.rgb_to_hsv(r, g, b)
    hsv = [int(x / 255) for x in float_hsv]

    return tuple(hsv)
    # *********turn converted rgb to hsv to make saturation and value = 1

    return tuple(rgb)


def interpolate(start_color, end_color, factor: float):
    reciprocal = 1 - factor
    return (
        int(start_color[0] * reciprocal + end_color[0] * factor),
        int(start_color[1] * reciprocal + end_color[1] * factor),
        int(start_color[2] * reciprocal + end_color[2] * factor),
    )


def generate_art(path: str):
    print(
        "What color do you want to start the picture with? (R = red, B = blue, Y = yellow)"
    )
    start_color = input()

    if start_color == "R" or start_color == "red":
        start_color = (
            random.randint(0, 255),
            random.randint(0, 0),
            random.randint(0, 0),
        )
    elif start_color == "G" or start_color == "green":
        start_color = (
            random.randint(0, 0),
            random.randint(0, 255),
            random.randint(0, 0),
        )
    elif start_color == "B" or start_color == "blue":
        start_color = (
            random.randint(0, 0),
            random.randint(0, 0),
            random.randint(0, 255),
        )

    print("Great choice! What about your end color? (R = red, B = blue, G = green")
    end_color = input()

    if end_color == "R" or end_color == "red":
        end_color = (
            random.randint(0, 255),
            random.randint(0, 0),
            random.randint(0, 0),
        )
    elif end_color == "G" or end_color == "green":
        end_color = (
            random.randint(0, 0),
            random.randint(0, 255),
            random.randint(0, 0),
        )
    elif end_color == "B" or end_color == "blue":
        end_color = (
            random.randint(0, 0),
            random.randint(0, 0),
            random.randint(0, 255),
        )

    image_size_px = 128
    padding_px = int(12.8)  # 10%
    image_bg_color = (0, 0, 0)
    # start_color = random_color()
    # end_color = random_color()
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

    # Draw bounding box
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])

    # Center the image
    delta_x = min_x - (image_size_px - max_x)
    delta_y = min_y - (image_size_px - max_y)

    for i, point in enumerate(points):
        points[i] = (point[0] - delta_x // 2, point[1] - delta_y // 2)

    # Draw The Points
    thickness = 0
    n_points = len(points) - 1
    for i, point in enumerate(points):

        # OVERLAY CANVAS
        overlay_Image = Image.new(
            "RGB", size=(image_size_px, image_size_px), color=image_bg_color
        )
        overlay_draw = ImageDraw.Draw(overlay_Image)
        p1 = point

        if i == len(points) - 1:
            p2 = points[0]
        else:
            p2 = points[i + 1]

        line_xy = (p1, p2)
        color_factor = i / n_points
        line_color = interpolate(start_color, end_color, color_factor)
        #        line_color = (
        #           random.randint(0, 255),
        #          random.randint(0, 255),
        #         random.randint(0, 255),
        #    )
        thickness += 1
        overlay_draw.line(line_xy, fill=line_color, width=thickness)
        image = ImageChops.add(image, overlay_Image)

    image.save(path)


if __name__ == "__main__":
    # for i in range(10):
    #    generate_art(f"test_image_{i}.png")
    generate_art("test_image.png")


# Draw bounding box to check for centering (after "center the image")
#    min_x = min([p[0] for p in points])
#    max_x = max([p[0] for p in points])
#    min_y = min([p[1] for p in points])
#    max_y = max([p[1] for p in points])
#    draw.rectangle((min_x, min_y, max_x, max_y), outline=(255, 0, 0))
