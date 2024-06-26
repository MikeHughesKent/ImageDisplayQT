ImageDisplayQT
====================================
ImageDisplayQT is a PyQT widget for live scientific image display in Python QT Graphical User Interfaces.

It was designed as a simple and lightweight widget that allows real-time display of monochrome or RGB images. Features include a status bar, with pixel value inspection, a draggable region of interest, zoom and pan, and several types of overlay. Monochrome images can be displayed using any colormap from matplotlib.
Simple line graphs can also be displayed in the same widget, although without the functionality of comprehensive packages such as matplotlib.

Install using::

    pip install ImageDisplayQT
    
Example bare-bones GUIs showing how to use the widget are `available on github <https://github.com/MikeHughesKent/ImageDisplayQT/tree/main/examples>`_.  

ImageDisplayQT is developed mainly by `Mike Hughes <https://research.kent.ac.uk/applied-optics/hughes/>`_'s lab in the `Applied Optics Group <https://research.kent.ac.uk/applied-optics>`_, School of Physics and Astronomy, University of Kent. The package was originally developed for GUIs for in endoscopic microscopy, including fluorescence endomicroscopy and 
holographic endomicroscopy. 

The project is hosted on `github <https://github.com/MikeHughesKent/ImageDisplayQT/>`_. Bug reports, contributions and pull requests are welcome. 




^^^^^^^^
Contents
^^^^^^^^

.. toctree::
   :maxdepth: 2
   
   getting_started
   example
   overlays
   customisation
   graphs
   
* :ref:`genindex`


*Acknowledgements: Funding to Mike Hughes's lab from EPSRC (Ultrathin fluorescence microscope in a needle, EP/R019274/1), Royal Society (Ultrathin Inline Holographic Microscopy).*   





