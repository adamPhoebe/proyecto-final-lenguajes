## ---------- DATA ----------- ##

questions = [
    "Who developed the game 'Undertale'?",
    "What is the largest desert in the world?",
    "Who is known as the 'Father of Computers'?",
    "What is the capital city of Canada?",
    "Which famous scientist developed the theory of relativity?",
    "What is the tallest mountain in the world?",
    "Who painted the famous artwork 'Starry Night'?",
    "What is the primary language spoken in Brazil?",
    "Which country is known as the 'Land of the Rising Sun'?",
    "Who wrote the famous novel '1984'?",
    "What is the chemical symbol for iron?",
    "What is the largest continent in the world?",
    "Who composed the Symphony No. 9 in D minor, Op. 125?",
    "What is the main ingredient in guacamole?",
    "Which famous scientist is credited with discovering gravity?",
    "What is the currency of the United Kingdom?",
    "Who is known as the 'Queen of Pop'?",
    "What is the world's second-largest country by land area?",
    "What is the smallest bone in the human body?",
    "Who painted 'The Persistence of Memory'?",
    "What is the national flower of Japan?",
    "Who wrote 'The Catcher in the Rye'?",
    "What is the largest bird in the world?",
    "Which city is known as the 'Big Apple'?",
    "Who discovered penicillin?",
    "What is the process of a caterpillar turning into a butterfly called?",
    "What is the longest bone in the human body?",
    "Who composed 'The Four Seasons'?",
    "What is the most widely spoken language in the world?",
    "Which planet is closest to the Sun?",
    "Who painted 'The Scream'?",
    "What is the currency of France?",
    "Who is known as the 'Bard of Avon'?",
    "What is the largest moon in the solar system?",
    "What is the largest organ in the human body?",
    "Who was the first female Prime Minister of the United Kingdom?",
    "What is the primary ingredient in sushi?",
    "Which famous artist is known for his cut-off ear?",
    "What is the national animal of Australia?",
    "Who wrote 'The Great Gatsby'?",
    "What is the world's largest coral reef system?",
    "What is the tallest tree in the world?",
    "Who discovered the theory of evolution?",
    "What is the capital city of Russia?",
    "What is the largest type of big cat in the world?",
    "What is the capital city of Australia?",
    "Which planet is known as the 'Red Planet'?",
    "Who painted the Mona Lisa?",
    "What is the smallest country in the world?",
    "Which gas is most abundant in the Earth's atmosphere?",
    "What is the largest mammal in the world?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the currency of Japan?",
    "What is the boiling point of water?",
    "Who is the author of 'To Kill a Mockingbird'?",
    "What is the longest river in the world?",
    "What is the chemical symbol for gold?",
    "Who is the first person to step on the moon?",
    "What is the capital city of Spain?",
    "What is the largest ocean in the world?"
]

classificationQuestions = [
    "What is a variable in programming?",
    "Explain the difference between a compiler and an interpreter.",
    "What is object-oriented programming (OOP) and its main principles?",
    "What are data structures? Provide examples.",
    "Explain the concept of recursion in programming.",
    "What is the difference between a function and a method?",
    "Describe the role of algorithms in computer science.",
    "What is version control and why is it important in software development?",
    "Explain the concept of 'Big O' notation and its significance in algorithms.",
    "What is a programming paradigm? Provide examples.",
    "What is meant by the term 'bug' in programming?",
    "Define the concept of inheritance in object-oriented programming.",
    "What is the purpose of a constructor in object-oriented programming?",
    "Explain the difference between stack and queue data structures.",
    "What is a callback function?",
    "Describe the difference between dynamic and static typing in programming languages.",
    "What is the role of a conditional statement in programming?",
    "Explain the concept of scope in programming.",
    "What is the significance of comments in code?",
    "Describe the purpose of the 'return' statement in functions.",
    "What is a pointer in programming?",
    "Explain the concept of 'polymorphism' in object-oriented programming.",
    "What is meant by 'exception handling' in programming?",
    "Describe the use of libraries and modules in programming.",
    "What are the advantages of using object-oriented programming?",
    "What is the difference between 'while' and 'for' loops?",
    "Explain the concept of a linked list.",
    "What is the role of a database in software development?",
    "What is the purpose of unit testing in programming?",
    "Describe the concept of abstraction in programming.",
    "What is the Pythagorean theorem?",
    "Define what a prime number is.",
    "Explain the concept of derivatives in calculus.",
    "What are the different types of triangles based on angles and sides?",
    "What is the Fibonacci sequence and where is it used?",
    "Describe the concept of probability in mathematics.",
    "What is the difference between mean, median, and mode?",
    "Define the term 'matrix' in mathematics.",
    "Explain the concept of exponents and their properties.",
    "What are the applications of logarithms in real life?",
    "What is the concept of integration in calculus?",
    "Define the term 'function' in mathematics.",
    "What is the significance of the number 'π' (pi) in mathematics?",#.encode("utf-8"),
    "Describe the concept of vectors in mathematics.",
    "What are the properties of a quadratic equation?",
    "Explain the concept of trigonometry.",
    "What is the formula to calculate the area of a circle?",
    "Define the concept of 'probability distribution'.",
    "Describe the concept of limits in calculus.",
    "What is the difference between permutations and combinations?",
    "Explain the concept of logarithmic functions.",
    "What is the concept of a geometric sequence?",
    "Describe the use of matrices in solving equations.",
    "What is the significance of the 'golden ratio'?",
    "Explain the concept of algebraic expressions and equations.",
    "What are the properties of a parallelogram?",
    "Describe the concept of the Cartesian coordinate system.",
    "What is the concept of 'slope' in mathematics?",
    "Explain the concept of factorials."
]

SPLASH = '''
  ___   __ __  ____    ___  ____        ___   __ __  ____    ___  ____     ___       _____   ___  ____      
 /   \ |  |  ||    |  /  _]|    \      /   \ |  |  ||    |  /  _]|    \   /  _]     / ___/  /  _]|    \     
|     ||  |  | |  |  /  [_ |  _  |    |     ||  |  | |  |  /  [_ |  D  ) /  [_     (   \_  /  [_ |  D  )    
|  Q  ||  |  | |  | |    _]|  |  |    |  Q  ||  |  | |  | |    _]|    / |    _]     \__  ||    _]|    /     
|     ||  :  | |  | |   [_ |  |  |    |     ||  :  | |  | |   [_ |    \ |   [_      /  \ ||   [_ |    \     
|     ||     | |  | |     ||  |  |    |     ||     | |  | |     ||  .  \|     |     \    ||     ||  .  \    
 \__,_| \__,_||____||_____||__|__|     \__,_| \__,_||____||_____||__|\_||_____|      \___||_____||__|\_|    
                                                                                                            
             ___ ___  ____  _      _       ___   ____    ____  ____   ____  ___   _____                     
            |   |   ||    || |    | |     /   \ |    \  /    ||    \ |    |/   \ /     |                    
            | _   _ | |  | | |    | |    |     ||  _  ||  o  ||  D  ) |  ||     ||  Y  |                    
            |  \_/  | |  | | |___ | |___ |  O  ||  |  ||     ||    /  |  ||  O  ||__|  |   v1.1                 
            |   |   | |  | |     ||     ||     ||  |  ||  _  ||    \  |  ||     |   |__|                    
            |   |   | |  | |     ||     ||     ||  |  ||  |  ||  .  \ |  ||     |    __                     
            |___|___||____||_____||_____| \___/ |__|__||__|__||__|\_||____|\___/    |__|
'''

# ------ FILE HANDLING ------ #

def log(content, filename="transcript", filetype="txt", end="\n"):
    f = open(f"{filename}.{filetype}", "a", encoding="utf-8")
    f.write(str(content) + str(end))
    f.close()

def readLog(filename="transcript", filetype="txt"):
    f = open(f"{filename}.{filetype}", "r", encoding="utf-8")
    fileContent = f.read()
    f.close()
    return fileContent

def clearLog(filename="transcript", filetype="txt"):
    f = open(f"{filename}.{filetype}", "w", encoding="utf-8")
    f.write("")
    f.close()

def lineNum(filename="transcript", filetype="txt"):
    f = open(f"{filename}.{filetype}", "r", encoding="utf-8")
    lnm = f.readlines()
    f.close()
    return lnm

# ----------- MATH ---------- #

def clamp(val, minv, maxv):
    return min(max(val, minv), maxv)