import threading
from time import sleep, time
import traceback
from src.gameplay.middlewares.mapMiddleware import updateMapMiddleware
from src.gameplay.core.tasks.loot import pickUpLoot
from src.gameplay.healing.healingBySpells import healingBySpells, initHealingOrchestrator
from src.gameplay.healing.healingByPotions import healingByPotions, initItemOrchestrator
from src.gameplay.middlewares.playerStatus import updatePlayerStatusMiddleware
from src.gameplay.middlewares.screenshotMiddleware import updateScreenshotMiddleware
from src.gameplay.threads.keyListener import key_listener
from src.utils.makePycwnd import getPycwnd

class GameThread:
    def __init__(self, context):
        self.context = self.init(context)

    def mainloop(self):
        while True:
            try:
                if self.context['pause']:
                    continue
                try:
                    fps = 1 / (time() - loop_time)
                    print(f'FPS {int(fps)} - hppc {self.context["player"]["hpPc"]} - mppc {self.context["player"]["mpPc"]}  -   coord: {self.context["map"]["coordinate"]}', flush=True)
                except:
                    pass
                loop_time = time()
                self.context = self.updateContext(self.context)
                healingByPotions(self.context)
                healingBySpells(self.context)
                if self.context['trigger']['looting']:
                    pickUpLoot(self.context['pycwnd'])
                    self.context['trigger']['looting'] = False

                # self.context = self.wrapUp(self.context)
                endTime = time()
                diff = endTime - loop_time
                sleep(max(0.045 - diff, 0))
                # print(self.context)
            except:
                print('An exception occurred:', traceback.format_exc())
    
    def wrapUp(self, context):
        context['map']['previousCoordinate'] = context['map']['coordinate']
        return context

    def updateContext(self, context):
        context = updateScreenshotMiddleware(context)
        context = updatePlayerStatusMiddleware(context)
        # context = updateMapMiddleware(context)
        return context
    
        
    def callback(self, key):
        self.context['trigger'][key] = True
    
    def init(self, context):
        context['pycwnd'] = getPycwnd()
        initHealingOrchestrator(context)
        initItemOrchestrator(context)
        # Create a thread for the key listener and set it as a daemon thread
        key_listener_thread = threading.Thread(target=key_listener, daemon=True, args=(self.callback,))
        # Start the thread
        key_listener_thread.start()
        return context
