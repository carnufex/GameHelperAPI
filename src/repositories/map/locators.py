from typing import Union
from src.repositories.map.config import images
from src.utils.typings import BBox, GrayImage
from src.utils.core import cacheObjectPosition, locate


# TODO: add unit tests
# TODO: add perf
@cacheObjectPosition
def getMapToolsPosition(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['tools'])
