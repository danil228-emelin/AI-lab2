from swiplserver import PrologThread


class GetAllFriends:
    def run(self, prolog: PrologThread):
        res = prolog.query(self.query())
        if not res:
            self.failure(res)
        else:
            self.success(res)

    def __init__(self, man: str):
        self.man = man

    def query(self):
        return f'can_be_friends(\"{self.man}\",X)'

    def success(self, res):
        if (res):
            print(f"{self.man} can have friends")

    def failure(self, res):
        print(f"{self.man} can't find friends.He took all women or has a lot of enemies")
