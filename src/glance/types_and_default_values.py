from typing import TypeVar
import numpy as np
from PIL import Image
from matplotlib.figure import Figure

ImageTypes = TypeVar("Image", np.ndarray, Image.Image, Figure)
DEFAULT_CMAP = "viridis"
