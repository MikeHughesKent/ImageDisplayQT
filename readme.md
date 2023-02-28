# ImageDisplayQT
ImageDisplayQT is a PyQT widget for displaying live images in GUIs. It was orignially developed for scientific imaging applications, with features including zoom, 
pixel inspection, autoscaling, region of interest with live mean display, and the ability to add persistent overlays. 

It is lightweight and simple to use, requiring 
only a few lines of code to be added to your GUI. It can display images at video rate on modest hardware.

It currently only supports monochrome images, support for colour images and eventually stacks is planned in future.

Full documentation and pip install will be available soon.

It is developed mainly by [Mike Hughes](https://research.kent.ac.uk/applied-optics/hughes) 
at the [Applied Optics Group](https://research.kent.ac.uk/applied-optics/), School of Physics and Astronomy, University of Kent. 

The widget was originally developed for our in-house microscopy and imaging systems and will evolve with our requirements. Bug reports, contributions and pull requests are welcome.

## Getting started

Import the class:
```
from image_display import ImageDisplay
```
Create an instance:
```
imDisplay = ImageDisplay()
```
and then add this widget to your GUI.

To update the image, call:
```
imDisplay.set_mono_image(img)
```

where `img` is a 2D numpy array containing the image.

Toggle the status bar visibility using:

```
imDisplay.set_status_bar(True/False)
```

Toggle the zoom facility using the mouth scroll wheel (or pinch zoom):

```
imDisplay.set_zoom_enabled(True/False)
```
Once zoomed you can pan by holding the middle or right mouse buttons.

Toggle the ability to draw a rectangular region of interest by holding the left mouse button and dragging:

```
imDisplay.set_roi_enabled(True/False)
```

Set the colormap to be any Matplotlib colormap using:
```
imDisplay.set_colormap(colormapName)
```

Please see the example in the examples folder for more functionality, including overlays and autoscaling.


## Requirements

Required Packages:
* PyQt (tested on v5)
* Numpy
* PIL
* Matplotlib (for colormaps)


## Acknowledgements

Funding from EPSRC (Ultrathin fluorescence microscope in a needle, EP/R019274/1), Royal Society (Ultrathin Inline Holographic Microscopy) and University of Kent.