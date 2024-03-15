
Getting Started
===============

Import the ``ImageDisplay`` class::

    from image_display import ImageDisplay

Create an instance of ``ImageDisplay``::

    imDisplay = ImageDisplay()

and then add this widget to your GUI, eg. using ``addWidget``.

To update the image display, call::

    imDisplay.set_image(img)

where ``img`` is either a 2D numpy array containing a monochrome image or a 3D numpy array containing a colour image with the third dimensions containing the red, green and blue channels.

Toggle the status bar visibility using ``set_status_bar``, for example::

    imDisplay.set_status_bar(True)

Toggle the zoom facility using the mouse scroll wheel (or pinch zoom) using ``set_zoom_enabled``, for example::

    imDisplay.set_zoom_enabled(True)

Once zoomed you can pan by holding the middle or right mouse buttons.

Toggle the ability to draw a rectangular region of interest by holding the left mouse button and dragging using ``set_roi_enabled``, for example::

    imDisplay.set_roi_enabled(True)

You can set the colormap to be any Matplotlib colormap, for example::

    imDisplay.set_colormap('hsv')
    
You can choose whether or not the image intensity is autoscaled to use the full dynamic range using ``autoscale_enabled``, for example::

    imDisplay.autoscale_enabled(True)
    
Images are always displayed as 8bit images. If autoscale is set to ``True`` then the smallest and largest image pixel values will be mapped to 0 and 255 respectively. For colour images, all three channels are scaled in the same way.

If autoscale is set to ``False`` then no mapping will occur by default, the input image will simply be cast to an 8 bit unsigned image. This can be changed using ``set_display_range``::

    imDisplay.set_display_range(min, max)

Where image pixel values of ``min`` and below will be mapped to 0, and ``max`` and above to 255.   
