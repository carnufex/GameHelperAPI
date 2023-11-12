from src.repositories.map import config
from src.utils.typings import BBox, GrayImage


# TODO: add unit tests
# TODO: add perf
def getMapImage(screenshot: GrayImage, MapToolsPosition: BBox) -> GrayImage:
    x0 = MapToolsPosition[0] - config.dimensions['width'] - 11
    x1 = x0 + config.dimensions['width']
    y0 = MapToolsPosition[1] - 50
    y1 = y0 + config.dimensions['height']
    return screenshot[y0:y1, x0:x1]