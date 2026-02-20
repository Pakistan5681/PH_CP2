variables = {}

TEXT_RED = "\x1b[31m"

def seperate(file_contents):
    return file_contents.split(";")

def print_all_lines(lines):
    for i in lines: print(i)

def run():
    with open("Docs\\pakicode_code.txt", "r") as file:
        lines = seperate(file.read())
        for i in lines: process_line(i)

def process_line(line):
    words = line.split(" ")

    for i in words:
        if i != "" and i != " ":
            if i != "var":
                i = i.strip()

                if "(" in i:
                    i = i.replace("(", " ")
                    i = i.replace(")", "")

                func = i.split(" ")

                get_function(func)
            else: 
                create_var(words)

def get_function(key):
    match key[0]:
        case "print": pc_print(key[1])

def pc_print(input):
    input = input.replace('"', "")
    input = input.replace("'", "")
    print(input)

def create_var(line):
    variables[line[1]] = line[2]
    print(f"{line[1]} = {line[2]}")
    print(variables[line[1]])

def check_if_var(input):
    global variables
    global TEXT_RED
    if not isinstance(input, int) and not isinstance(input, float) and not isinstance(input, bool):
        if '"' in input:
            return False
        else:
            if input in variables.keys():
                return True
            else:
                print(f{TEXT_RED})

run()