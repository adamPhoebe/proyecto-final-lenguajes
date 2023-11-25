import os
import time as t
import util

def wait(n):
    t.sleep(max(0, (n*2)-1))

ANSIdisable = False

CLR = ["\033[0m",""]
BLD = ["\033[1m",""]
DIM = ["\033[2m",""]
ITL = ["\033[3m",""]
UND = ["\033[4m",""]
BLK = ["\033[5m",""]
REV = ["\033[7m",""]
HID = ["\033[8m",""]
STK = ["\033[9m",""]

def cls():
    print(clr())                     # STYLE CLEAR
    print("\033[H\033[2J", end="")   # ANSI CLEAR
    os.system('clear')               # OS CLEAR
    #print("\033[H")                 # RETURN TO HOME POSITION

def fg(color):
    return f"\033[38;5;{color}m"

def bg(color):
    return f"\033[48;5;{color}m"

def color(fgc, bgc):
    return fg(fgc) + bg(bgc)

def rgb(fgc=None, bgc=None):
    if bgc == None:
        fr, fg, fb = fgc
        return "\033[38;2;{fr};{fg};{fb}m"
    elif fgc == None:
        br, bg, bb = bgc
        return "\033[48;2;{br};{bg};{bb}m"
    elif (bgc == None) and (fgc == None):
        return ""
    else:
        fr, fg, fb = fgc
        br, bg, bb = bgc
        return "\033[38;2;{fr};{fg};{fb}m" + "\033[48;2;{br};{bg};{bb}m"
    
## -------------------- ##

def clr():
    return CLR[int(ANSIdisable)]

def bold(c):
    return BLD[int(ANSIdisable)] + str(c) + clr()

def dim(c):
    return DIM[int(ANSIdisable)] + str(c) + clr()

def italic(c):
    return ITL[int(ANSIdisable)] + str(c) + clr()

def under(c):
    return UND[int(ANSIdisable)] + str(c) + clr()

def blink(c):
    return BLK[int(ANSIdisable)] + str(c) + clr()

def reverse(c):
    return REV[int(ANSIdisable)] + str(c) + clr()

def hidden(c):
    return HID[int(ANSIdisable)] + str(c) + clr()

def strike(c):
    return STK[int(ANSIdisable)] + str(c) + clr()

## -------------------- ##

def title(c):
    return bold(italic(c))

def dlg(spk, c, tab="\t"):
    return str(tab) + title(str(spk) + ": ") + str(c)

def numbul(l, startNum=1):
    outstr = ""
    for num, i in enumerate(l):
        outstr += f'{title(num + startNum)}. {italic(i)}' + "\n"
    return outstr
    
def answers(lst, startNum=1):
    l = []
    outstr = ""
    for i in lst:
        l.append((">"+i).replace(">",""))
    for num, i in enumerate(l):
        outstr += f'{title(num + startNum)}. {italic(i)}' + "\n"
    return outstr

def format(cont, type, moneysign="$", moneylabel="COP"):
    if type == "money":
        outstr = str("{:20,.2f}".format(cont))[:-3]
        outstr = moneysign + outstr.strip() + " " + moneylabel
        return outstr
    elif type == "id":
        outstr = str("{:20,.2f}".format(cont))[:-3]
        outstr = outstr.strip().replace(",",".")
        return outstr
    
def choices(arr, inputPrompt="", startNum=0):
    for num,i in enumerate(arr):
        print(f'{num+startNum}. {i}')
    return inputRange(minv=0, maxv=len(arr)-1, prompt=inputPrompt)
    
def error(err, debugInfo=""):
    global ANSIdisable
    ANSIdisableCache = ANSIdisable is True
    ANSIdisable = False
    def formatError(title, content):
        return f'{color(1, 15)} {title}: {clr() + fg(1)} {content} {clr()}' 
    def formatWarning(title, content):
        return f'{color(8, 11)} {title}: {clr() + fg(3)} {content} {clr()}' 
    
    if err == "INPUTRANGE_NOTNUMERIC":
        return formatError("Not Numeric", "Please input a numeric value.")
    elif err == "INPUTRANGE_NOTINRANGE":
        return formatError("Not In Range", "Please input a value in range.")
    elif err == "SIMULATEDAY_ASKFAIL":
        return formatWarning("Simulation Error", "A small error ocurred in simulating this day. Retrying...")
    
    elif err == "INPUTRANGE_ISFLOAT":
        return formatWarning("Input is Float", f"The decimal values will be {bold('round') + fg(3)}ed out.{clr()}")
    elif err == "EDITSIMPARAMS_NOTEVEN":
        return formatWarning("Input is Odd", "Your input will be turned into an even number for better team distribution.")
    ANSIdisable = ANSIdisableCache
        
def isNumber(num):
    neg = 1
    if num[:1] == "-":
       neg = -1
       num = num[1:]
    if num.isnumeric():
        return int(num) * neg
    elif num.replace(".", "", 1).isnumeric():
        return float(num) * neg
    else:
        return None

def inputRange(minv=0, maxv=float('inf'), prompt="", autoClamp=False):
    x = input(prompt)
    if isNumber(x) is not None:
        x = float(x)
        if minv <= x <= maxv:
            if x.is_integer() is False:
                print(error("INPUTRANGE_ISFLOAT"))
                wait(2)
            return int(round(x))
        elif autoClamp == True:
            if x.is_integer() is False:
                print(error("INPUTRANGE_ISFLOAT"))
                wait(2)
            return util.clamp(int(round(x)), minv, maxv)
        else:
            print(error("INPUTRANGE_NOTINRANGE"))
            wait(2)
            return None
    else:
        print(error("INPUTRANGE_NOTNUMERIC"))
        wait(2)
        return None
    
def yesno(inputPrompt=""):
    x = input(inputPrompt)
    if x.lower() in ["y", "yes", "yup", "yep", "si", "s", "sip", "ye", "yeah", "yea", "yee", "1"]:
        return 1
    else:
        return 0

def foot(c=""):
    return (f"##-------------{c}------------##")

def printfoot(c=""):
    print(f"##-------------{c}------------##")