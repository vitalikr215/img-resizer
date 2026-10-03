# Image resizer

A simple Python script for resizing and changing image aspect ratio. Using *pip* package [pillow](https://pillow.readthedocs.io/en/latest/) for images manipulations

## The purpose and background of an application

I'am quite often publishing a posts on Youtube community page of my channel. But there are specific requirements for images that could be uploaded there. Those images aspect ratio should be 2:5 or 5:2 and have an image size restrictions. As my phone camera has aspect ratio 4:3 or 3:4 and "bigger" than Youtube required, I have to resize them. Also I have to add transparent paddings so my images won't be cut. Before used image editor for this purpose, and now finally decided to automate this.

## Usage
First you have to create a virtual environment via
`source venv/bin/activate`

Than
`pip install -r requirements.txt`

And than
`python3 img-resizer <filename> [resize_coef] [canvas_resize_coef]`

_resize_coef_ - means how many times you want to decrease your image size (both height and width). By default it's *2*

_canvas_resize_coef_ - a coeficient to change aspect ratio of an image. By default it's 1.78 (it's "magic number" to convert 3:4 to and 2:5 or 4:3 to 5:2). This coeficient needed for calculation of transparent padding size, so the 4:3 or 3:4 image won't be cut
