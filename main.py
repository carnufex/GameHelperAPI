from src.gameplay.threads.gameThread import GameThread
from context import context

def main():
    contextInstance = context
    gameThread = GameThread(contextInstance)
    gameThread.mainloop()

if __name__ == '__main__':
    main()