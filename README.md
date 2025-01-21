# gawp

A lightweight Python package that enables interactive, zoomable image viewing directly from Jupyter notebooks using a web-based interface.

## Features

- Open images in a new browser tab from Jupyter notebooks
- Smooth zoom and pan functionality
- Support for common image formats (numpy, PIL, matplotlib)

## Installation

Install using pip:

```bash
pip install gawp
```

## Usage

Basic usage in a Jupyter notebook:

```python
import gawp

# Create an image of numpy type (also works wit PIL images)
image = ski.data.coins()

gawp.in_web(image)
```
or use a matplotlib figure:
```python
import gawp
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x*x

fig = plt.figure()
ax = plt.axes()

ax.scatter(x,y)

gawp.in_web(fig)
```

## Development

Contributions are welcome! To contribute:

1. Clone the repository
2. Create a new branch for your feature
3. Add your changes and tests
4. Submit a pull request

## Requirements

- Python 3.8+
- Jupyter Notebook or JupyterLab
- Pillow
- Numpy
- Matplotlib
- scikit-image
- webbrowser (standard library)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, feature requests, or questions:
1. Check the [GitHub Issues](https://github.com/tenghamn/gawp/issues)
