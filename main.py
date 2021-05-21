from PIL import Image
import numpy as np

# Output image size (in pixels)
WIDTH = 640
HEIGHT = 480

# Complex plane bounds
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

# Parameters
MAX_ITERATIONS = 80
COLOR_CONTRAST = 10


img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)


# Generate Fractal
for x in range(WIDTH):
    for y in range(HEIGHT):
        # Convert pixel coordinate to complex number
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                    IM_START + (y / HEIGHT) * (IM_END - IM_START))
        z = complex(0, 0)
        iteration = 0
        while abs(z) < 2 and iteration < MAX_ITERATIONS:
            z = z * z + c
            iteration += 1
        r, g, b = iteration * COLOR_CONTRAST % 256, iteration * COLOR_CONTRAST * 2 % 256, iteration * COLOR_CONTRAST * 3 % 256
        img[y, x] = r, g, b

# Write the pixels to an image file
image = Image.fromarray(img)
image.save("mandelbrot.png")