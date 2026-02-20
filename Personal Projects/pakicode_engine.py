variables = {}

TEXT_RED = "\x1b[31m"
TEXT_RESET = "\x1b[0m"

def seperate(file_contents):
    return file_contents.split(";")

def print_all_lines(lines):
    for i in lines: print(i)

# runs the code from the 'pakicode_code' file
def run():
    with open("Docs/pakicode_code.txt", "r") as file:
        lines = seperate(file.read())
        for i in lines: process_line(i, lines.index(i))

# a function used to process a line into code
def process_line(line, index):
    words = line.split(" ")
    functions = []

    for i in words:
        i = i.strip()
        if i != "" and i != " ":
            if i != "var":           

                if "(" in i: # Removes the parantheses for variable assignment
                    i = i.replace("(", " ")
                    i = i.replace(")", "")

                if '"' in i: # combines all words in a string to one variable
                    for j in range(len(words) - words.index(i)) + words.index(i):
                        word = words[j]
                        if '"' in word:
                            pass # logic for string combination goes here

                # turns the word into a function-ready format
                func = i.split(" ")
                if len(func) > 1 and check_if_var(func[1], index + 1):
                    func[1] =  variables[func[1]]

                functions.append(func)
            else: 
                create_var(words)

    for i in functions:
        get_function(i)

# converts key into a runnable function
def get_function(key):
    match key[0]:
        case "print": pc_print(key[1])
        case "pystart"

# a simple print method
def pc_print(input):
    input = input.replace('"', "")
    print(input)

def pygameStart():
    pass

def create_var(line):
    variables[line[1]] = line[2]

# checks if some input is a variable, returns true if so and false if not
def check_if_var(input, lineIndex):
    global variables
    
    if not isinstance(input, int) and not isinstance(input, float) and not isinstance(input, bool):
        if '"' in input:
            print("This is a string")
            return False
        else:
            if input in variables.keys():
                print("This is a variable")
                return True
            else:
                throw_error(f"The variable '{input}' does not exist. Are you perhaps missing quotation marks?", lineIndex)

def throw_error(errorString, lineIndex):
    global TEXT_RED
    global TEXT_RESET
    print(f"{TEXT_RED}{errorString}")
    print(f"Error on line {lineIndex}{TEXT_RESET}")

run()