from nptyping import NDArray
from typing import Any, List, Tuple, Union

BBox = Tuple[int, int, int, int]
GrayImage = NDArray[Any, Any]
Coordinate = Tuple[int, int, int]
CoordinateList = List[Coordinate]
XYCoordinate = Tuple[int, int]
XYCoordinateList = List[Coordinate]
GrayPixel = int
Waypoint = Any
WaypointList = List[Waypoint]