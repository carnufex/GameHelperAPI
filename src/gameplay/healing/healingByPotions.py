from src.gameplay.core.tasks.useHotkey import sendHotkey
from src.repositories.actionBar.core import slotIsAvailable
from time import time



# TODO: add unit tests
def healingByPotions(context):
   
    if context['healing']['potions']['hp']['enabled']:
        if context['player']['hpPc'] <= context['healing']['potions']['hp']['hpPc'] and slotIsAvailable(context['screenshot'], 1):
            if time() - context['lastUsed']['pot'] > 1:
                sendHotkey(
                    context['healing']['potions']['hp']['hotkey'], context['pycwnd'])
                context['lastUsed']['pot'] = time()
                return context
    if context['healing']['potions']['mp']['enabled']:
        if  context['player']['mpPc'] <= context['healing']['potions']['mp']['mpPc'] and slotIsAvailable(context['screenshot'], 2):
            if time() - context['lastUsed']['pot'] > 1:
                sendHotkey(
                    context['healing']['potions']['mp']['hotkey'], context['pycwnd'])
                context['lastUsed']['pot'] = time()
                return context
    return context