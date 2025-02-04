from gawp.server import show_html_in_browser
from gawp.html import create_html_with_image
from gawp.types_and_default_values import ImageTypes, DEFAULT_CMAP
from IPython.display import display, HTML


def in_web(image: ImageTypes, cmap: str = DEFAULT_CMAP):
    show_html_in_browser(create_html_with_image(image, cmap))


def inline(image: ImageTypes, cmap: str = DEFAULT_CMAP):
    display(HTML(create_html_with_image(image, cmap, inline=True)))
