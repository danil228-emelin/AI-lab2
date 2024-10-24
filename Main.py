from swiplserver import PrologMQI, create_posix_path
import re
from actions import GetAllWoman,GetAllMan,GetAllFriends
queries = [
    "does INPUT(Freya, Athena, Angroba) sleep with multiple men",
    "does INPUT(Kratos,Odin,Thor) have kids",
    "does INPUT(Kratos,Odin,Thor) can find friends"
]
patterns = {
    r"does (.+) sleep with multiple men": GetAllWoman.GetAllWoman,
    r"does (.+) have kids":GetAllMan.GetAllMan,
    r"does (.+) can find friends": GetAllFriends.GetAllFriends
}

BD_PATH=r"C:\Users\danil_emelin1\PycharmProjects\pythonProject3\god_of_war.pl"
with PrologMQI() as mqi:
    with mqi.create_thread() as prolog:
        path = create_posix_path(BD_PATH)
        prolog.query(f'consult("{path}")')
        print("Prolog db downloaded!")
        print("Examples")
        for q in queries:
            print(f"{q}")
        print("to stop- enter exit.")
        while True:
            query = input('$ ')
            if query.lower() == 'exit':
                break
            for pattern in patterns:
                match = re.match(pattern, query, re.IGNORECASE)
                if match is None:
                    continue
                processor = patterns[pattern](*match.groups())
                processor.run(prolog)
                break
            else:
                print("Неверный запрос")