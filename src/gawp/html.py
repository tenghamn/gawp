from gawp.types_and_default_values import ImageTypes, DEFAULT_CMAP
from gawp.html_template import HTML_TEMPLATE
import numpy as np
from functools import singledispatch
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from matplotlib.figure import Figure
from PIL import Image
from io import BytesIO
import base64


def create_html_with_image(image: ImageTypes, cmap: str = DEFAULT_CMAP, inline=False):
    pil_image = _convert_to_pil_image(image, cmap)
    buffer = BytesIO()
    pil_image.save(buffer, format="PNG")
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    img_src = f"data:image/png;base64,{img_base64}"
    return HTML_TEMPLATE.replace("zooom_container_height", "100vh" if not inline else "auto").replace(
        'src="/api/placeholder/800/600"', f'src="{img_src}"'
    )


@singledispatch
def _convert_to_pil_image(image: ImageTypes, cmap: str = DEFAULT_CMAP):
    return f"Unknown type: {image}"


@_convert_to_pil_image.register
def _(image: np.ndarray, cmap: str = DEFAULT_CMAP):
    if len(image.shape) == 2:
        image = cm.get_cmap(cmap)(Normalize()(image), bytes=True)
    return Image.fromarray(image)


@_convert_to_pil_image.register
def _(image: Image.Image, cmap: str = DEFAULT_CMAP):
    return image


@_convert_to_pil_image.register
def _(image: Figure, cmap: str = DEFAULT_CMAP):
    buf = BytesIO()
    image.savefig(buf, format="png")
    buf.seek(0)
    return Image.open(buf)
