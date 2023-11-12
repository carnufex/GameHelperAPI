from src.repositories.map.core import getCoordinate


def updateMapMiddleware(context):
    previousCoord = None
    if context['map']['previousCoordinate'] is not None:
        previousCoord = context['map']['previousCoordinate']

    coord = getCoordinate(
        context['screenshot'], previousCoordinate=previousCoord)
    if coord is not None:
        context['map']['coordinate'] = coord
    return context