from swiplserver import PrologThread


class GetAllWoman:
    def run(self, prolog: PrologThread):
        res = prolog.query(self.query())
        if not res or len(res) == 0:
            self.failure(res)
        else:
            self.success(res)

    def __init__(self, woman: str):
        self.woman = woman

    def query(self):
        return f'woman_is_bad(\"{self.woman}\")'

    def success(self, res):

        for el in res:
            if (el):
                print(f"{self.woman} will broke your heart.She is a bad woman")
                return
        print(f"{self.woman} is a good woman.Start secong stage - meriage")
    def failure(self, res):
        print(f'{self.woman} is clear,stage second - meriage.')