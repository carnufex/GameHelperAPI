from time import time


class BaseTask:
    def __init__(self, delayBeforeStart=0, delayAfterComplete=0, delayOfTimeout=0, isRootTask=False, manuallyTerminable=False, name='baseTask', parentTask=None, shouldTimeoutTreeWhenTimeout=False):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.terminable = True
        self.delayBeforeStart = delayBeforeStart
        self.delayAfterComplete = delayAfterComplete
        self.delayOfTimeout = delayOfTimeout
        self.isRetrying = False
        self.isRootTask = isRootTask
        self.manuallyTerminable = manuallyTerminable
        self.name = name
        self.parentTask = parentTask
        self.retryCount = 0
        self.rootTask = None
        self.shouldTimeoutTreeWhenTimeout = shouldTimeoutTreeWhenTimeout
        self.status = 'notStarted'
        self.statusReason = None

    def setParentTask(self, parentTask):
        self.parentTask = parentTask
        return self

    def setRootTask(self, rootTask):
        self.rootTask = rootTask
        return self

    def shouldIgnore(self, _) -> bool:
        return False

    def shouldManuallyComplete(self, _) -> bool:
        return False

    def shouldRestart(self, _) -> bool:
        return False

    def do(self, context):
        return context

    def did(self, _) -> bool:
        return True

    def ping(self, context):
        return context

    def onBeforeStart(self, context):
        return context

    def onBeforeRestart(self, context):
        return context

    def onIgnored(self, context):
        return context

    def onInterrupt(self, context):
        return context

    def onComplete(self, context):
        return context

    def onTimeout(self, context):
        return context
