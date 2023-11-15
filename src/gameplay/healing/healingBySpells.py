from src.gameplay.core.tasks.useHotkey import sendHotkey
from src.repositories.actionBar.core import hasCooldownByName, hasHealingCooldown
from time import time
from src.wiki.spells import spells



# TODO: add unit tests
def healingBySpells(context):
    # if time() - context['lastUsed']['heal'] >= 1:
    if not hasHealingCooldown(context['screenshot']):
        if context['healing']['spells']['criticalHealing']['enabled']:
            if context['player']['hpPc'] <= context['healing']['spells']['criticalHealing']['hpPc'] and context['player']['mp'] >= spells[context['healing']['spells']['criticalHealing']['spell']]['manaNeeded'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['criticalHealing']['spell']):
                sendHotkey(
                    context['healing']['spells']['criticalHealing']['hotkey'], context['pycwnd'])
                context['lastUsed']['heal'] = time()
                return context
        if context['healing']['spells']['mediumHealing']['enabled']:
            if context['player']['hpPc'] <= context['healing']['spells']['mediumHealing']['hpPc'] and context['player']['mp'] >= spells[context['healing']['spells']['mediumHealing']['spell']]['manaNeeded'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['mediumHealing']['spell']):
                sendHotkey(
                    context['healing']['spells']['mediumHealing']['hotkey'], context['pycwnd'])
                context['lastUsed']['heal'] = time()
                return context        
        if context['healing']['spells']['lightHealing']['enabled']:
                if context['player']['hpPc'] <= context['healing']['spells']['lightHealing']['hpPc'] and context['player']['mp'] >= spells[context['healing']['spells']['lightHealing']['spell']]['manaNeeded'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['lightHealing']['spell']):
                    sendHotkey(
                        context['healing']['spells']['lightHealing']['hotkey'], context['pycwnd'])
                    context['lastUsed']['heal'] = time()
                    return context
        if context['player']['isParalyzed']:
            if context['player']['mp'] >= spells[context['healing']['spells']['paralyze']['spell']]['manaNeeded'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['paralyze']['spell']):
                sendHotkey(
                    context['healing']['spells']['paralyze']['hotkey'], context['pycwnd'])
                context['lastUsed']['heal'] = time()
                return context
    return context
