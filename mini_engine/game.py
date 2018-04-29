
class IGame:

    def run_loop(self):

        self.start()

        while self.update():
            pass

    def start(self):
        pass

    def update(self):
        pass

