from src.utils.core import getScreenshot


def updateScreenshotMiddleware(context):
    context['screenshot'] = getScreenshot()
    return context
