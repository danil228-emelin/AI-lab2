from swiplserver import PrologThread


class GetAllMan:
    def run(self, prolog: PrologThread):
        res = prolog.query(self.query())
        if not res:
            self.failure(res)
        else:
            self.success(res)

    def __init__(self, man: str):
        self.man = man

    def query(self):
        return f'father(\"{self.man}\",_)'

    def success(self, res):
        if (res):
            print(f"{self.man} have kids")
        else:
            print(f"{{self.man}} no kids,alone wolf")


    def failure(self, res):
        print(f'{self.man} don\'t have kids,alone wolf')