from gawp.server import show_html_in_browser
from gawp.html import create_html_with_image
from gawp.types_and_default_values import ImageTypes, DEFAULT_CMAP
from IPython.display import display, HTML

html = """
<html>
    <head>
        <title>Test Page</title>
    </head>
    <body>
        <h1>Hello World!</h1>
        <p>This is a test page.</p>
    </body>
</html>
"""


def in_web(image: ImageTypes, cmap: str = DEFAULT_CMAP):
    show_html_in_browser(create_html_with_image(image, cmap))


def inline(image: ImageTypes, cmap: str = DEFAULT_CMAP):
    display(HTML(create_html_with_image(image, cmap, inline=True)))
