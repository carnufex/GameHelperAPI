import numpy as np
from scipy.spatial import distance
from typing import Union
from src.utils.typings import Coordinate, GrayImage, GrayPixel, Waypoint, WaypointList
from src.utils.core import hashit, hashitHex, locate
from src.utils.coordinate import getCoordinateFromPixel, getPixelFromCoordinate
from src.utils.image import save
from .config import availableTilesFrictions, breakpointTileMovementSpeed, coordinates, dimensions, floorsImgs, floorsLevelsImgsHashes, floorsPathsSqms, nonWalkablePixelsColors, tilesFrictionsWithBreakpoints, walkableFloorsSqms
from .extractors import getMapImage
from .locators import getMapToolsPosition
from .typings import FloorLevel, TileFriction


# TODO: add unit tests
# TODO: add perf
# TODO: get by cached images coordinates hashes
def getCoordinate(screenshot: GrayImage, previousCoordinate: Coordinate = None) -> Union[Coordinate, None]:
    floorLevel = getFloorLevel(screenshot)
    if floorLevel is None:
        return None
    MapToolsPosition = getMapToolsPosition(screenshot)
    if MapToolsPosition is None:
        return None
    MapImage = getMapImage(screenshot, MapToolsPosition)
    MapHashedImg = hashitHex(MapImage)
    # TODO: use get instead
    if MapHashedImg in coordinates:
        return coordinates[MapHashedImg]
    if previousCoordinate is not None:
        prevCoord = findCoordinateFromPreviousPosition(screenshot, previousCoordinate, MapImage, floorLevel)
        if prevCoord is not None:
            return prevCoord
    imgCoordinate = locate(floorsImgs[floorLevel], MapImage, confidence=0.75)
    if imgCoordinate is None:
        return None
    xImgCoordinate = imgCoordinate[0] + dimensions['halfWidth']
    yImgCoordinate = imgCoordinate[1] + dimensions['halfHeight']
    xCoordinate, yCoordinate = getCoordinateFromPixel(
        (xImgCoordinate, yImgCoordinate))
    return (xCoordinate, yCoordinate, floorLevel)


def findCoordinateFromPreviousPosition(screenshot: GrayImage, previousCoordinate: Coordinate, mapImage: GrayImage, floorLevel: int) -> Union[Coordinate, None]:
    try:
        (previousCoordinateXPixel, previousCoordinateYPixel) = getPixelFromCoordinate(
            previousCoordinate)
        (yStart, yEnd, xStart, xEnd, paddings) = getPaddings(previousCoordinateXPixel, previousCoordinateYPixel)
        areaImgToCompare = floorsImgs[floorLevel][yStart:yEnd, xStart:xEnd]
        areaFoundImg = locate(
            areaImgToCompare, mapImage, confidence=0.9)
        if areaFoundImg:
            currentCoordinateXPixel = previousCoordinateXPixel - \
                paddings["xStart"] + areaFoundImg[0]
            currentCoordinateYPixel = previousCoordinateYPixel - \
                paddings["yStart"] + areaFoundImg[1]
            (currentCoordinateX, currentCoordinateY) = getCoordinateFromPixel(
                (currentCoordinateXPixel, currentCoordinateYPixel))
            return (currentCoordinateX, currentCoordinateY, floorLevel)
        else:
            print("didnt fint img")
    except:
        print("exception in previousCoordinate")
        return None

def getPaddings(previousCoordinateXPixel: int, previousCoordinateYPixel: int) -> tuple:
    
    paddings = {"yStart": 20, "xStart": 20, "yEnd": 20, "xEnd": 20}
    yStart = previousCoordinateYPixel - \
        (dimensions['halfHeight'] + paddings["yStart"])
    if yStart < 0: # this will have to be applied to all edges later, not just top.
        yStart = 0
        paddings["yStart"] = 0
    yEnd = previousCoordinateYPixel + \
        (dimensions['halfHeight'] + 1 + paddings["yEnd"])
    xStart = previousCoordinateXPixel - \
        (dimensions['halfWidth'] + paddings["xStart"])
    xEnd = previousCoordinateXPixel + \
        (dimensions['halfWidth'] + paddings["xEnd"])
    return (yStart, yEnd, xStart, xEnd, paddings)

# TODO: add unit tests
# TODO: add perf
def getFloorLevel(screenshot: GrayImage) -> Union[FloorLevel, None]:
    MapToolsPosition = getMapToolsPosition(screenshot)
    if MapToolsPosition is None:
        return None
    left, top, width, height = MapToolsPosition
    left = left + width + 8
    top = top - 7
    height = 67
    width = 2
    floorLevelImg = screenshot[top:top + height, left:left + width]
    floorImgHash = hashit(floorLevelImg)
    if floorImgHash not in floorsLevelsImgsHashes:
        return None
    return floorsLevelsImgsHashes[floorImgHash]


# TODO: add unit tests
# TODO: add perf
def getClosestWaypointIndexFromCoordinate(coordinate: Coordinate, waypoints: WaypointList) -> Union[int, None]:
    closestWaypointIndex = None
    closestWaypointDistance = 9999
    for waypointIndex, waypoint in enumerate(waypoints):
        if len(waypoint['coordinate']) == 0 or waypoint['coordinate'][2] != coordinate[2]:
            continue
        waypointDistance = distance.cdist(
            [(waypoint['coordinate'][0], waypoint['coordinate'][1])], [(coordinate[0], coordinate[1])]).flatten()[0]
        if waypointDistance < closestWaypointDistance:
            closestWaypointIndex = waypointIndex
            closestWaypointDistance = waypointDistance
    return closestWaypointIndex


# TODO: add perf
def getBreakpointTileMovementSpeed(charSpeed: int, tileFriction: TileFriction) -> int:
    tileFrictionNotFound = tileFriction not in tilesFrictionsWithBreakpoints
    if tileFrictionNotFound:
        closestTilesFrictions = np.flatnonzero(
            availableTilesFrictions > tileFriction)
        tileFriction = availableTilesFrictions[closestTilesFrictions[0]] if len(
            closestTilesFrictions) > 0 else 250
    availableBreakpointsIndexes = np.flatnonzero(
        charSpeed >= tilesFrictionsWithBreakpoints[tileFriction])
    if len(availableBreakpointsIndexes) == 0:
        return breakpointTileMovementSpeed[1]
    return breakpointTileMovementSpeed.get(availableBreakpointsIndexes[-1] + 1)


# TODO: add unit tests
# TODO: add perf
def getTileFrictionByCoordinate(coordinate: Coordinate) -> TileFriction:
    xOfPixelCoordinate, yOfPixelCoordinate = getPixelFromCoordinate(
        coordinate)
    floorLevel = coordinate[2]
    tileFriction = floorsPathsSqms[floorLevel,
                                   yOfPixelCoordinate, xOfPixelCoordinate]
    return tileFriction


# TODO: add unit tests
# TODO: add perf
def isCloseToCoordinate(currentCoordinate: Coordinate, possibleCloseCoordinate: Coordinate, distanceTolerance: int = 10) -> bool:
    (xOfCurrentCoordinate, yOfCurrentCoordinate, _) = currentCoordinate
    XYOfCurrentCoordinate = (xOfCurrentCoordinate, yOfCurrentCoordinate)
    (xOfPossibleCloseCoordinate, yOfPossibleCloseCoordinate, _) = possibleCloseCoordinate
    XYOfPossibleCloseCoordinate = (
        xOfPossibleCloseCoordinate, yOfPossibleCloseCoordinate)
    euclideanDistance = distance.cdist(
        [XYOfCurrentCoordinate], [XYOfPossibleCloseCoordinate])
    return euclideanDistance <= distanceTolerance


# TODO: add unit tests
# TODO: add perf
# TODO: 2 coordinates was tested. Is very hard too test all coordinates(16 floors * 2560 mapWidth * 2048 mapHeight = 83.886.080 pixels)
def isCoordinateWalkable(coordinate: Coordinate) -> bool:
    (xOfPixel, yOfPixel) = getPixelFromCoordinate(coordinate)
    return (walkableFloorsSqms[coordinate[2], yOfPixel, xOfPixel]) == 1


# TODO: add unit tests
# TODO: add perf
def isNonWalkablePixelColor(pixelColor: GrayPixel) -> bool:
    return np.isin(pixelColor, nonWalkablePixelsColors)
