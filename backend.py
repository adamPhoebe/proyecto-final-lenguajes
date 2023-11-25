import random as rng
import util as u

import ui
import math
import dummygen

prizes = [   1,   2,   3,    5,   10,
            20,  30,  50,   70,  100,
           120, 200, 500, 1000, 3000] # MULTIPLY BY 100000

peopleToPass = 14
totalDaysPassed = 0
moneyGivenOut = 0

peopleThatCalled = [dummygen.genPeople(peopleToPass), dummygen.genPeople(peopleToPass)]

peopleThatPassed = []
peopleToCompete = []

u.clearLog()

def resetPeopleThatCalled():
    global peopleThatCalled
    peopleThatCalled = [dummygen.genPeople(peopleToPass), dummygen.genPeople(peopleToPass)]

def classificationStep():
    resetPeopleThatCalled()

    pit = tuple(zip(peopleThatCalled[0], peopleThatCalled[1]))

    u.log(ui.title("[CLASSIFICATION ROUNDS START!]"))

    u.log(f"[START CLASSIFICATION ROUNDS: A TOTAL OF {peopleToPass*2} PEOPLE ARE COMPETING.]\n")

    for i in pit:
        u.log(i[0].name + "\n    vs.   \n" + i[1].name + "")
        u.log(ui.dlg("Host", f'{i[0].name}, {i[1].name}, {rng.choice(u.classificationQuestions)}') ,"transcript")
        if i[0].timeClass > i[1].timeClass:
            peopleThatPassed.append(i[1])
            u.log("\t - "+f'{i[1].name} beat {i[0].name} in answering the classification question by {i[0].timeClass-i[1].timeClass} second(s).')
        elif i[0].timeClass < i[1].timeClass:
            peopleThatPassed.append(i[0])
            u.log("\t - "+f'{i[0].name} beat {i[1].name} in answering the classification question by {i[1].timeClass-i[0].timeClass} second(s).')
        else: # CHOOSE AT RANDOM IF BOTH ANSWERED AT THE SAME TIME.
            personThatWon = rng.choice([i[0], i[1]])
            u.log("\t - "+f"Both people answered at the same time, so {personThatWon.name} was chosen randomly.")
            peopleThatPassed.append(personThatWon)
        u.log("\n","transcript")
    u.log(f"\n[END CLASSIFICATION ROUNDS: {peopleToPass} PEOPLE HAVE ENTERED THE COMPETITION.]\n")
    u.log("[PEOPLE THAT WERE SELECTED:]")
    for i in peopleThatPassed:
        u.log(str(i))
    pairings = tuple(zip(peopleThatPassed[:math.ceil(peopleToPass/2)], peopleThatPassed[math.ceil(peopleToPass/2):]))
    u.log("[COMPETITION PAIRINGS:]")
    for i in pairings:
        u.log("\t"+f' - ({i[0].name} vs. {i[1].name})' + "\n")
        peopleToCompete.append(i)

def simulateDay():
    global totalDaysPassed
    competingPair = peopleToCompete[totalDaysPassed]

    u.log(ui.title(f'\n\n\n\nDAY #{totalDaysPassed+1} - {competingPair[0].name} vs. {competingPair[1].name}.'))
    askQuestions(competingPair)
    totalDaysPassed += 1
    
def finalLog():
    u.log("\n### ----------------------------------------- ###\n")
    u.log("[FINAL LOG:]")
    u.log("\t[PARTICIPANT'S STATUS:]")
    for i in peopleThatPassed:
        u.log("\t\t"+str(i))
    u.log("\t[MONEY GIVEN OUT OVERALL:]")
    u.log("\t\tIn total, the program gave out " + ui.format(moneyGivenOut * 100000, "money") + ".")

def askQuestions(personPair):
    questionsAsked = 0
    currentSafeguard = 0
    currentContestant = 0
    sets = [rng.randint(0,46), rng.randint(0,46)]
    moneyGiven = [0,0]
    hasLost = False


    def changeSafeguard():
        u.log(ui.dlg("Host",f"We've now passed a safeguard, you can now lose any question, and you'll still win {formattedMoney}."))
        nonlocal currentSafeguard
        currentSafeguard = prizes[questionsAsked]

    while questionsAsked < 14:
        curcon = personPair[currentContestant]
        curcon.wildcards = [0,1,2]

        u.log("\n")
        if currentContestant == 0:
            u.log(ui.foot("FIRST CONTESTANT'S TURN:"))
        else:
            u.log(ui.foot("SECOND CONTESTANT'S TURN:"))

        while hasLost is False:
            formattedMoney = ui.format(prizes[questionsAsked] * 100000, "money")

            u.log(ui.title(f"\n\t# -- -- -- QUESTION #{questionsAsked+1} -- -- -- #\n"))
            u.log(ui.dlg("Host", f"{curcon.name}, {u.questions[questionsAsked+sets[currentContestant]]}"))

            personAnswer = curcon.answer(questionsAsked)
            curcon.lastQuestion = [questionsAsked, u.questions[questionsAsked+sets[currentContestant]]]
            curcon.lastDay = totalDaysPassed

            if personAnswer["wildcard"] is not None:
                wildcardToPlay = ['50/50', 'Public Opinion', 'Lifeline'][personAnswer['wildcard']]
                wildcardResponse = ["Hmmm... I think I will not.", "I think I will."]
                u.log(ui.dlg("Host",f"It seems like our contestant has decided to use a wildcard."))
                u.log(ui.dlg(curcon.name,f"I want to play the {wildcardToPlay} wildcard."))
                u.log(ui.dlg("Host", f'Alright, the {wildcardToPlay} wildcard.'))
                if personAnswer['wildcard'] == 0:
                    u.log(ui.dlg("Host",f'Two options have been removed.'))
                elif personAnswer['wildcard'] == 1:
                    u.log(ui.dlg("Host",f'The public is weighing in... It looks like they want answer #{rng.randint(1,4)}! Will you choose that one?'))
                    u.log(ui.dlg(curcon.name, wildcardResponse[personAnswer["wildcardResponse"]]))
                    u.log(ui.dlg("Host", "Alright then! Choose your answer when you're ready."))
                else:
                    u.log(ui.dlg("Host",f'You can now call a friend or family member to help you.'))
                    u.log(ui.italic(f'\t - {curcon.name} is calling a {rng.choice(["friend", "family member"])}. It seems they wanted the answer #{rng.randint(1,4)}.'))
                    u.log(ui.dlg("Host",f'Alright! Will you choose that option?'))
                    u.log(ui.dlg(curcon.name, wildcardResponse[personAnswer["wildcardResponse"]]))
                    u.log(ui.dlg("Host", "Alright then! Choose your answer when you're ready."))

            if personAnswer["correct"]:
                u.log(ui.italic(f"\t - {curcon.name} answers correctly."))
                u.log(ui.dlg("Host",f'That is correct, well done {curcon.name}. You gain {formattedMoney}.'))
                if questionsAsked == 4 or questionsAsked == 9:
                    changeSafeguard()
                curcon.money = prizes[questionsAsked]
                if personAnswer["optout"]:
                    u.log(ui.dlg("Host", f"Huh? It appears our contestant wants to opt out! This means you'll go home with {formattedMoney}. Are you sure you want to opt out?"))
                    u.log(ui.dlg(curcon.name, "Yes."))
                    u.log(ui.dlg("Host", f"Alright then! If that's the case, then {curcon.name} is walking away with the money they've earned so far! Congratulations!"))
                    break
                questionsAsked += 1
                if questionsAsked == 15:
                    print(f"{curcon.name} has just won the grand prize on day {totalDaysPassed+1}!")
                    break
            else:
                u.log(ui.italic(f"\t - {curcon.name} answers incorrectly."))
                u.log(ui.dlg("Host",f"I'm afraid that is incorrect. Unfortunately, you lose all the money you've gained up to this point{['',' except for your safeguards'][min(currentSafeguard,1)]}."))
                curcon.money = currentSafeguard 
                moneyGiven[currentContestant] = currentSafeguard
                hasLost = True

        formattedMoney = ui.format(curcon.money * 100000, "money")

        if currentContestant == 0:
            u.log(ui.dlg("Host", f"And with that, {curcon.name} leaves with a total of {formattedMoney}. Thanks for participating, and let's move on to the next contestant."))
            moneyGiven[0] = curcon.money
            curcon.transferToBank()
            hasLost = False
            currentContestant = 1
            u.log(f'OH:{currentContestant}')
        else:
            u.log(ui.dlg("Host", f"And with that, {curcon.name} leaves with a total of {formattedMoney}. Thanks for participating, and thank you for watching the show. See ya next time!"))
            moneyGiven[1] = curcon.money
            curcon.transferToBank()
            break

        currentContestant = 1
        questionsAsked = 0

    u.log(f"[MONEY GIVEN OUT ON DAY {totalDaysPassed+1}]")
    u.log("\t" + f'{personPair[0].name} received {ui.format(moneyGiven[0] * 100000, "money")}.')
    u.log("\t" + f'{personPair[1].name} received {ui.format(moneyGiven[1] * 100000, "money")}.')
    u.log("\t" + f'In total, the program gave {ui.format((moneyGiven[0] + moneyGiven[1]) * 100000, "money")}.')

    global moneyGivenOut
    moneyGivenOut += moneyGiven[0] + moneyGiven[1]


def simulateDuration():
    ui.ANSIdisable = True
    u.clearLog("transcript")
    classificationStep()
    for i in range(int(peopleToPass/2)):
        simulateDay()
    finalLog()
    ui.ANSIdisable = False