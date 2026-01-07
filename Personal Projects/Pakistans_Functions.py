def idiot_proof_general(input_statement, output_type = "integer"):
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
                out = input(input_statement)
                isNegative = False

                if "-" in out:
                    isNegative = True  
                    out.replace("-", "")

                if out.isdecimal():
                    if isNegative:
                       return int(f"-{out}") 
                    else:
                         return int(out)
            elif output_type == "float":
                out = input(input_statement)
                isNegative = False
                isDecimal = False

                if "." in out:
                    isDecimal = True
                    
            elif output_type == "boolean":
                out = input(input_statement)
            else: raise Exception(f"'{output_type}' is not a valid output type")


print(idiot_proof_general("Do good pleb ", "nuts"))