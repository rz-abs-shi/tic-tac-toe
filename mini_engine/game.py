from mini_engine.exceptions import ExitGameInterrupt


class IGame:
    def run_loop(self):
        self.start()

        try:
            while self.update():
                pass
        except ExitGameInterrupt:
            print("Game exited.")

    def start(self):
        pass

    def update(self):
        pass
