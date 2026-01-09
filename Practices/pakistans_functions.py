def idiot_proof_general(input_statement, output_type = "integer", incorrect_input_message = "That input is invalid"):
        """
        Takes user input until it is the desired output type

        Input statement is what is printed out to the player

        OutputType decides the accepted output type

        It can be: 'integer', 'float', or 'boolean'
        """
        out = ""
        output_type = output_type.strip().lower()

        while True:        
            if output_type == "integer":
                out = input(input_statement).strip()
                isNegative = False

                if "-" in out:
                    isNegative = True  
                    out = out.replace("-", "")

                if out.isdecimal():
                    if isNegative:
                       return int(f"-{out}") 
                    else:
                         return int(out)
            elif output_type == "float":
                out = input(input_statement).strip()
                isNegative = False
                isDecimal = False

                if "." in out:
                    isDecimal = True
                    decimalLocal = out.index(".")
                    out = out.replace(".", "")

                    if decimalLocal == 0:
                        print(incorrect_input_message)
                        continue
                if "-" in out:
                    isNegative = True  
                    out = out.replace("-", "")

                if out.isdecimal():
                    if isDecimal:
                        out = insert_string(out, ".", decimalLocal - 1)
                    if isNegative: 
                        return float(f"-{out}") 
                    else:
                         return float(out)

                    
            elif output_type == "boolean":
                out = input(input_statement).strip().lower()
            else: raise Exception(f"'{output_type}' is not a valid output type")

            print(incorrect_input_message)

def idiot_proof_specific(input_statement, correct_inputs, incorrect_input_message = "That input is invalid"):
    """
    Takes user input until it matches one of the variables in correct_inputs (a list)
    """

    out = input(input_statement)

    while not out in correct_inputs:
        print(incorrect_input_message)

        out = input(input_statement)

    return out

def insert_string(string, string_to_insert, index):
    """
    Inserts a string/character into another string after a specific index.

    Does not delete the character already at that location
 
    """

    if not isinstance(string, str) or not isinstance(string_to_insert, str):
        raise Exception("string and string_to_insert must be strings")
    
    part1 = string[:index]
    part2 = string[index:]

    return part1 + string_to_insert + part2
