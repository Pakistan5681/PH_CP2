import pakistans_functions as pf

def startMenu():
    print("1. Savings Time Calculator")
    print("2. Compound Interest Calculator")
    print("3. Budget Allocator")
    print("4. Sale Price Calculator")
    print("5. Tip Calculator")
    codeToRun = pf.idiot_proof_specific("Enter the number of the option ", ["1", "2", "3", "4", "5"])

    if codeToRun == "1": savings_time_calculator()
    elif codeToRun == "2": compund_interest_calculator()

    print(" ")

def savings_time_calculator():
    saveAmount = pf.idiot_proof_general("What amount do you want to save ", "float")
    print(" ")

    print("1. Weekly")
    print("2. Monthly")
    saveInterval = pf.idiot_proof_specific("Enter the number of the interval ", ["1", "2"])
    print(" ")

    amount_per_interval = pf.idiot_proof_general("How much do you want to contribute each time ", "float")
    print(" ")

    interval_count = saveAmount / amount_per_interval
    if saveInterval == "1":
        num_days = interval_count * 7
        print(f"It will take {interval_count} weeks or {num_days} days to save ${saveAmount}")
    else:
        num_days = interval_count * 30
        print(f"It will take {interval_count} weeks or about {num_days} days to save ${saveAmount}")

def compund_interest_calculator():
    def calc_interest(percentage, amount):
        if percentage < 10:
            percentage = f"1.0{percentage}"
        else:
            percentage = f"1.{percentage}"

        return round(amount * float(percentage), 2)

    starting_amount = round(pf.idiot_proof_general("How much money are you starting with ", "float"), 2)
    print(" ")
    percentage = pf.idiot_proof_num_range("What precentage is the intrest\nchoose a whole number value between 1 and 100 ", 1, 100, "integer")
    print(" ")
    num_years = pf.idiot_proof_general("How many years of intrest ")
    amount = starting_amount

    for i in range(num_years):
        amount = calc_interest(percentage, amount)
    
    print(f"Starting with ${starting_amount} at {percentage}% interest, in {num_years} years you will have ${amount}")

def budget_allocator():
    category_count = pf.idiot_proof_general("How many budget categories do you have?")
    categories = []

    for i in range(category_count):
        category = input(f"What is category {category_count + 1}")
        categories.append(category)

startMenu()