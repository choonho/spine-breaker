
class Provider:
    def __init__(self, cfg):
        self.name = self.__class__.__name__
        self.cfg = cfg

    def stopServer(self, **kargs):
        """
        Stop Server"
        """
