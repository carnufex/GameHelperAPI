from src.repositories.statusBar.core import getManaPercentage, getHpPercentage, getIsParalyzed
from src.repositories.skills.core import getHp, getMana


def updatePlayerStatusMiddleware(context):
    context['player']['hp'] = getHp(context['screenshot'])
    context['player']['hpPc'] = getHpPercentage(context['screenshot'])
    context['player']['mp'] = getMana(context['screenshot'])
    context['player']['mpPc'] = getManaPercentage(context['screenshot'])
    context['player']['isParalyzed'] = getIsParalyzed(context['screenshot'])
    return context
