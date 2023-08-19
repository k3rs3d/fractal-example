# Mandelbrot Set Generator Example 

This Python script generates an image of the Mandelbrot set, a famous fractal. The image is saved as "mandelbrot.png."

## Requirements

The script requires the following Python libraries:

- PIL (Python Imaging Library)
- NumPy

You can install these dependencies using pip, like so:
`pip install pillow numpy`

## How it Works

- Defining Parameters: The script starts by defining various parameters for the image, including the width, height, complex plane bounds, maximum iterations, and color contrast.
- Generating the Fractal: A nested loop iterates over each pixel in the image. For each pixel, the script converts the pixel's coordinates to a complex number c and iterates the sequence z[n+1] = z[n]^2 + c until either abs(z) becomes greater than 2 or the maximum number of iterations is reached. The iteration count is then used to determine the color of the pixel, using the defined color contrast.
- Creating and Saving the Image: The pixel data is converted to a PIL Image object and saved as "mandelbrot.png."

## Usage

Simply run the script to generate a new Mandelbrot image: 

`python main.py`

Of course, you can change the parameters at the top of the script to adjust the size, color, and detail of the image.
