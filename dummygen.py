import random as rng
import util as u
from person import Person

FSTN = [i for i in u.readLog("first-names").split("\n")]
LSTN = [i.capitalize() for i in u.readLog("last-names").split("\n")]

def genPeople(count):
    lop = []
    for i in range(count):
        new = {
            "name": f'{rng.choice(FSTN)} {rng.choice(LSTN)}',
            "id":   rng.randint(10000000, 9999999999),
            "age":  rng.randint(18, 60)
        }
        if new["name"][:2] == "Mc":
            new["name"] = new["name"][:2] + new["name"][2:].capitalize()
        lop.append(Person(new["name"], new["id"], new["age"]))
    return lop

