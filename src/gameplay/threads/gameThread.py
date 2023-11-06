from time import time
import traceback
from src.gameplay.healing.healingBySpells import healingBySpells
from src.gameplay.healing.healingByPotions import healingByPotions
from src.gameplay.middlewares.playerStatus import updatePlayerStatusMiddleware
from src.gameplay.middlewares.screenshotMiddleware import updateScreenshotMiddleware
from src.utils.makePycwnd import getPycwnd

class GameThread:
    def __init__(self, context):
        self.context = context

    def mainloop(self):
        self.context = self.init(self.context)
        while True:
            try:
                if self.context['pause']:
                    continue
                try:
                    fps = 1 / (time() - loop_time)
                    print(f'FPS {fps}', flush=True)
                except:
                    pass
                loop_time = time()
                self.context = self.updateContext(self.context)
                self.context= healingByPotions(self.context)
                self.context = healingBySpells(self.context)
                # print(self.context)
            except:
                print('An exception occurred:', traceback.format_exc())
    


    def updateContext(self, context):
        context = updateScreenshotMiddleware(context)
        context = updatePlayerStatusMiddleware(context)
        return context
    
    def init(self, context):
        context['pycwnd'] = getPycwnd()
        return context