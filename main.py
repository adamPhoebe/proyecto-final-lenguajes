import ui
import backend
import util as u
import time as t

running = True

## ---- INITIAL ROUTINE ---- ##

ui.cls()
print(ui.bold(u.SPLASH) + "\n\n")
print(ui.title("Quien Quiere Ser Millonario? - Final Project for Programming Languages by Elian Avila Osorio, 24/11/2023."))
t.sleep(5)

## ------------------------- ##
## - MAIN PROGRAM FUNCTION - ##

def program(x):
    ui.cls()
    if x == 0:
        print(ui.title("Goodbye!"))
    elif x == 1:
        print(ui.italic(f"Current number of people applying for the program: {backend.peopleToPass*2}"))
        print(ui.italic(f"Minimum: 4 - Maximum: 10000"))
        ppl = None
        while ppl is None:
            ppl = ui.inputRange(minv=4, maxv=10000, prompt=ui.bold("Enter the number of people to apply for the program: "))
        backend.peopleToPass = int(ppl/2)
        if backend.peopleToPass % 2 == 1:
            print(ui.error("EDITSIMPARAMS_NOTEVEN"))
        backend.peopleToPass += backend.peopleToPass % 2
        ui.printfoot()
        print(ui.dlg("Number of people that will apply for the program", int(backend.peopleToPass*2), ""))
        print(ui.dlg("Number of people that will participate in the program", int(backend.peopleToPass), ""))
        print(ui.dlg("Number of days to simulate", int(backend.peopleToPass/2), ""))
        y = 0
        while y == 0:
            y = ui.yesno(ui.title("Return to main menu? [Y/N]: "))
    elif x == 2:
        print(ui.dlg("Number of people that will apply for the program", int(backend.peopleToPass*2), ""))
        print(ui.dlg("Number of people that will participate in the program", int(backend.peopleToPass), ""))
        print(ui.dlg("Number of days to simulate", int(backend.peopleToPass/2), ""))
        if ui.yesno(ui.title("Do you want to simulate the game with these parameters? [Y/N]: ")) == 1:
            print(ui.italic("Simulating..."))
            backend.simulateDuration()
            print(ui.italic("All done! Transcript, results, and logs are stored in 'transcript.txt'."))
            y = 0
            while y == 0:
                y = ui.yesno(ui.title("Return to main menu? [Y/N]: "))
        else:
            print(ui.italic("Returning to main menu..."))
            ui.wait(2)
    elif x == 3:
        print(ui.bold(u.SPLASH) + "\n\n")
        print(ui.title("Quien Quiere Ser Millonario? - Final Project for Programming Languages by Elian Avila Osorio, 24/11/2023."))
        print()
        print(ui.dlg("Programming done by", "Elian Avila Osorio"))
        print(ui.dlg("Date of version", "24 November, 2023"))
        y = 0
        while y == 0:
            y = ui.yesno(ui.title("Return to main menu? [Y/N]: "))

## ------------------------- ##

while running:
    ui.cls()
    ui.title("Choose an option:")
    x = ui.choices(["Exit program.",
                    "Edit simulation parameters.",
                    "Generate log transcript.",
                    "Show credits."])
    program(x)
    if x == 0:
        running = False