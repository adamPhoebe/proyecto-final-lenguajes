import random as rng
import ui

class Person:
    def __init__(self, name, id, age) -> None:
        self.name = name
        self.id   = id
        self.age  = age

        self.money         = 0
        self.bank          = 0
        self.lastQuestion  = [0,""]
        self.lastDay       = 0
        self.wildcardsUsed = 0

        self.timeClass = rng.randint(30, 60)

        self.wildcardProb = 1
        self.wildcards = [0,1,2]

        self.integrity = rng.randint(10,60) # WILDCARD GENERAL PROBABILITY IS CALLED INTEGRITY CUZ YOU GOTTA HAVE PRETTY LOW INTEGRITY TO USE ONE.

    def __str__(self):
        outstr = f'{ui.bold(self.name)}, ID {self.id}, age {self.age}' + "\n" + f'Money: {ui.format(self.bank * 100000, "money")} - Took to answer: {self.timeClass} seconds.'
        outstr += "\n"
        return outstr
    
    def logstr(self, tab=""):
        outstr = tab + f'{self.name}, ID {ui.format(self.id, "id")}, age {self.age}' + f"\n{tab}" 
        outstr += f'Money: {ui.format(self.bank * 100000, "money")} - Took to answer last question: {self.timeClass} seconds.' + f"\n{tab}"
        outstr += f'Last question answered: Question #{self.lastQuestion[0]+1}, in day {self.lastDay+1}. {self.lastQuestion[1]}'
        outstr += "\n"
        return outstr
    
    def answer(self, diff):
        # CALCULATE WILDCARD PROBABILITY #
        wid = None
        if rng.randrange(15) > diff and len(self.wildcards) != 0 and rng.randint(0, 100) > self.integrity: # IF WE HAVE WILDCARDS AVAILABLE, THE DIFFICULTY IS HIGH, AND OUR INTEGRITY IS LOW, WE USE A WILDCARD.
            wid = rng.choice(self.wildcards)
            self.wildcards.remove(wid)
        self.wildcard(wid)
        ans = {
            "correct":  diff * 4 * self.wildcardProb < rng.randint(0,100),
            "time":     diff * 3 + rng.randint(10,25),
            "wildcard": wid,
            "wildcardResponse": int(rng.randrange(15) > diff and rng.randint(0, 100) > self.integrity),
            "optout": rng.randrange(15) > diff and rng.randint(0, 100) < self.integrity and diff > 5
        }
        self.timeClass = ans["time"]
        return ans
    
    def wildcard(self, wid=None): #wid = wildcard ID:
        if wid is not None:
            self.wildcardsUsed += 1

        if wid == 0:   # 50/50 Wildcard
            self.wildcardProb = 0.5
        elif wid == 1: # Public Opinion Wildcard
            self.wildcardProb = 2/3
        elif wid == 2: # Lifeline Wildcard
            self.wildcardProb = 0.75
        else:          # Reset Wildcard Probability
            self.wildcardProb = 1

    def transferToBank(self):
        self.bank += self.money + 1
        self.money = 0
        self.bank -= 1