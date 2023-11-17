from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.gameplay.core.tasks.useHotkey import UseHotkeyTask
from src.repositories.actionBar.core import hasCooldownByName, hasHealingCooldown
from time import time
from src.wiki.spells import spells

healingOrchestrator: TasksOrchestrator
previousHeal = time()
def initHealingOrchestrator(context):
    global healingOrchestrator
    healingOrchestrator = context['orchestrators']['healing']

# TODO: add unit tests
def healingBySpells(context):
    currentTask = healingOrchestrator.getCurrentTask(context)
    if currentTask is not None:
        if currentTask.status == 'completed':
            healingOrchestrator.reset()
        else:
            healingOrchestrator.do(context)
            return
        
    if context['healing']['spells']['criticalHealing']['enabled']:
        if context['player']['hpPc'] <= context['healing']['spells']['criticalHealing']['hpPc'] and context['player']['mp'] >= spells[context['healing']['spells']['criticalHealing']['spell']]['manaNeeded'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['criticalHealing']['spell']):
            healingOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['spells']['criticalHealing']['hotkey'], context['pycwnd']))
            return
    if context['healing']['spells']['mediumHealing']['enabled']:
        if context['player']['hpPc'] <= context['healing']['spells']['mediumHealing']['hpPc'] and context['player']['mp'] >= spells[context['healing']['spells']['mediumHealing']['spell']]['manaNeeded'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['mediumHealing']['spell']):
            healingOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['spells']['mediumHealing']['hotkey'], context['pycwnd']))
            return   
    if context['healing']['spells']['lightHealing']['enabled']:
        if context['player']['hpPc'] <= context['healing']['spells']['lightHealing']['hpPc'] and context['player']['mp'] >= spells[context['healing']['spells']['lightHealing']['spell']]['manaNeeded'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['lightHealing']['spell']):
            healingOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['spells']['lightHealing']['hotkey'], context['pycwnd']))
            return
    if context['player']['isParalyzed']:
        if context['player']['mp'] >= spells[context['healing']['spells']['paralyze']['spell']]['manaNeeded']:
            healingOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['spells']['paralyze']['hotkey'], context['pycwnd']))
            return
