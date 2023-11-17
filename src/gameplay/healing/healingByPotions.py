from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.gameplay.core.tasks.useHotkey import UseHotkeyTask
from src.repositories.actionBar.core import slotIsAvailable
from time import time

itemOrchestrator: TasksOrchestrator

def initItemOrchestrator(context):
    global itemOrchestrator
    itemOrchestrator = context['orchestrators']['item']

# TODO: add unit tests
def healingByPotions(context):
    currentTask = itemOrchestrator.getCurrentTask(context)
    if currentTask is not None:
        if currentTask.status == 'completed':
            itemOrchestrator.reset()
        else:
            itemOrchestrator.do(context)
            return
        
    if context['healing']['potions']['hp']['enabled']:
        if context['player']['hpPc'] <= context['healing']['potions']['hp']['hpPc'] and slotIsAvailable(context['screenshot'], 9):
            itemOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['potions']['hp']['hotkey'], context['pycwnd']))
            return
    if context['healing']['potions']['mp']['enabled']:
        if  context['player']['mpPc'] <= context['healing']['potions']['mp']['mpPc'] and slotIsAvailable(context['screenshot'], 6):
            itemOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['potions']['mp']['hotkey'], context['pycwnd']))
            return