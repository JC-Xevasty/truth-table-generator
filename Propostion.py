from itertools import product

prop = []
numOfProp = "0"
truthValues = []
tempProp = ""


def instructions():
    print("╔═══════════════════════════════════════════════════════════════════╗")
    print("║                       TRUTH TABLE GENERATOR                       ║")
    print("╠═══════════════════════════════════════════════════════════════════╣")
    print("║[1] Enter the number of propositions to be used in the expression. ║")
    print("║    ► Number should be 2 - 5 only.                                 ║")
    print("║ ————————————————————————————————————————————————————————————————— ║")
    print("║[2] Enter the propositions to be used in the expression.           ║")
    print("║    ► Propositions entered should be separated by space.           ║")
    print("║    ► Proposition should be an uppercase letter.                   ║")
    print("║    ► Uppercase 'T' and 'F' letters can't be used as propositions. ║")
    print("║    ► Proposition can't be repeated.                               ║")
    print("║ ————————————————————————————————————————————————————————————————— ║")
    print("║[3] Enter the expression to be evaluated.                          ║")
    print("║    ► All propositions entered must be used.                       ║")
    print("║    ► Correct pairing of parentheses must be observed.             ║")
    print("╠═════════════════════════════════╦═════════════════════════════════╣")
    print("║       OPERATORS / VALUES        ║            KEYWORDS             ║")
    print("║ ——————————————————————————————— ║ ——————————————————————————————— ║")
    print("║            NEGATION             ║               not               ║")
    print("║           CONJUNCTION           ║               and               ║")
    print("║           DISJUNCTION           ║               or                ║")
    print("║           IMPLICATION           ║             implies             ║")
    print("║              TRUE               ║            T or True            ║")
    print("║              FALSE              ║            F or False           ║")
    print("╚═════════════════════════════════╩═════════════════════════════════╝")


def checkPropositionSyntax(checkProp):
    flag = False
 
    while not flag:
        if checkProp.count("True") == 0:
            if checkProp.count("T") > 0:
                checkProp = checkProp.replace("T", "True")
        else:
            checkProp = checkProp.replace("True", "true")
            if checkProp.count("T") > 0:
                checkProp = checkProp.replace("T", "True")
            checkProp = checkProp.replace("true", "True")

        if checkProp.count("False") == 0:
            if checkProp.count("F") > 0:
                checkProp = checkProp.replace("F", "False")
        else:
            checkProp = checkProp.replace("False", "false")
            if checkProp.count("F") > 0:
                checkProp = checkProp.replace("F", "False")
            checkProp = checkProp.replace("false", "False")
        
        proposition = checkProp
        flag1 = False   # Checks if the proposition syntax is correct
        flag2 = False   # Checks if each open parentheses has a corresponding close parentheses
        flag3 = False   # Checks if all the propositions (variables are used)

        # Checks if the proposition syntax is valid
        check = validProposition(checkProp)
        if check:
            flag1 = True
        else:
            print("  [ Invalid proposition entered. ]")

        # Counting the open and close parentheses
        oPar = checkProp.count("(")
        cPar = checkProp.count(")")

        if oPar != cPar:
            print("  [ Parentheses are not properly entered. ]")
        else:
            flag2 = True

        checkProp = checkProp.replace("and", "").replace("or", "")
        checkProp = checkProp.replace("not", "").replace("implies", "")
        checkProp = checkProp.replace("(", "").replace(")", "")
        checkProp = checkProp.replace("True", " ").replace("False", " ")
        checkProp = checkProp.replace(" ", "")

        # Checking if each variable are used in the proposition
        for item in prop:
            if checkProp.count(item) > 0:
                checkProp = checkProp.replace(item, "")
            else:
                print("  [ Proposition [", item, "] is not used. ]")
                checkProp = checkProp + item

        if len(checkProp) == 0:
            flag3 = True
        else:
            for i in checkProp:
                print("  [ Proposition [", i, "] can't be used. ]")
                

        # If all flags are TRUE, then the proposition entered is valid
        if flag1 and flag2 and flag3:
            break
        else:
            print()
            checkProp = input("Enter proposition: ")

    return proposition


def validProposition(checkProp):
    flag = False
    # Evaluating all implication in the proposition
    checkProp = implication(checkProp)

    try:
        for i in range(len(prop)):
            checkProp = checkProp.replace(prop[i], "True")
        eval(checkProp)
        flag = True

    except:
        flag = False

    return flag


def implication(checkProp):

    num = checkProp.count('implies')
    while num > 0:
        opars = checkProp.count('(', 0, checkProp.find('implies'))
        cpars = checkProp.count(')', 0, checkProp.find('implies'))

        # Checks if there is no closing parentheses before the implies
        if cpars == 0:
            checkProp = checkProp.replace('(', '$', (checkProp.count('(', 0, checkProp.find('implies'))) - 1)
            # Checks if there is also no open parentheses before the implies
            if opars == 0:
                checkProp = '( not ( ' + checkProp
                checkProp = checkProp + ')'
            else:
                checkProp = checkProp.replace('(', '( not ( ', 1)
            checkProp = checkProp.replace('$', '(')
            checkProp = checkProp.replace('implies', ') or', 1)
        else:
            x = opars - cpars
            # Checks if there is a open parentheses without a close parentheses before the implies
            if x == 0:
                checkProp = checkProp.replace('(', '( not (', 1)
                checkProp = checkProp.replace('implies', ') or', 1)
            else:
                checkProp = checkProp.replace('(', '$', checkProp.count('(', 0, checkProp.find('implies')) - 1)
                checkProp = checkProp.replace('(', '( not (', 1)
                checkProp = checkProp.replace('$', '(')
                checkProp = checkProp.replace('implies', ') or', 1)

        num = num - 1
    return checkProp


def displayTruthTable(checkProp):

    truthValues = list(product([False, True], repeat=numOfProp))

    space = 1

    for i in range(len(prop)):
        space = space + 8
    space = space + len(checkProp) + 5

    displayHeader(space, checkProp)

    checkProp = implication(checkProp)

    for item in truthValues:
        spaceleft = space
        tempProp = checkProp
        for x in range(len(prop)):
            checkProp = checkProp.replace((prop[x]), str(item[x]))

        print("║ ", end="")

        for y in range(len(item)):
            print("│", item[y], end=" ")
            spaceleft = spaceleft - 8
            if item[y] == True:
                print(" ", end="")
        print("│", end="")
        spaceleft = spaceleft - 1

        for i in range(int(spaceleft / 2) - 3):
            print(" ", end="")

        print(eval(checkProp), end="")

        spaceleft = spaceleft - ((spaceleft / 2) - 3) - 5

        while spaceleft > 1:
            print(" ", end="")
            spaceleft = spaceleft - 1

        if eval(checkProp):
            print(" ", end="")

        print("║")

        checkProp = tempProp

    print("╚", end="")
    for i in range(space):
        print("═", end="")
    print("╝")


def displayHeader(space, checkProp):
    print()
    print("╔", end="")
    for i in range(space):
        print("═", end="")
    print("╗")

    print("║", end="")
    for i in range(int(space / 2) - 5):
        print(" ", end="")

    print("TRUTH TABLE", end="")

    spaceleft = space
    spaceleft = spaceleft - ((space / 2) - 5) - 11
    while spaceleft > 0:
        print(" ", end="")
        spaceleft = spaceleft - 1
    print("║")

    print("╠", end="")
    for i in range(space):
        print("═", end="")
    print("╣")

    print("║ ", end="")

    spaceleft = space

    for item in prop:
        print("│  ", item, end="   ")
        spaceleft = spaceleft - 8
    print("│ ", checkProp, end="")
    spaceleft = spaceleft - len(checkProp) - 3

    while spaceleft > 1:
        print(" ", end="")
        spaceleft = spaceleft - 1

    print("║")

    print("╠", end="")
    for i in range(space):
        print("═", end="")
    print("╣")


####################################
#            MAIN CODE             #
####################################

instructions()
# Checking number of propositions
while numOfProp.isdigit():
    numOfProp = input("Enter number of propositions to be used: ")
    if numOfProp.isdigit():
        numOfProp = int(numOfProp)
        if numOfProp < 2 or numOfProp > 5:
            print("  [ Two to five propositions only. ]\n")
            numOfProp = "0"
        else:
            break
    else:
        print("  [ Invalid number of Propositions. ]\n")
        numOfProp = "0"

# Checking propositions to be used
while True:
    print()
    prop = input("Enter propositions to be used: ").split()

    if len(prop) != numOfProp:
        print("  [ Entered propositions doesn't match number. ]")
    else:
        lowercase = "".join(prop)
        duplicates = ""
        lower = ""
        containsTorF = ""

        # Checks if the proposition entered is a letter
        letterCheck = False
        while not letterCheck:
            for i in range(len(prop)):
                if prop[i].isalpha():
                    if i == len(prop) - 1:
                        letterCheck = True
                else:
                    print("  [ Proposition [", prop[i], "] should be a letter. ]")
                    if i == len(prop) - 1:
                        prop = input("\nEnter propositions to be used: ").split()

        # Checks if the proposition entered is a single character
        singleLetter = False
        while not singleLetter:
            for i in range(len(prop)):
                if len(prop[i]) > 1:
                    print("  [ Proposition [", prop[i], "] should be a single letter. ]")
                    if i == len(prop) - 1:
                        prop = input("\nEnter propositions to be used: ").split()
                else:
                    if i == len(prop) - 1:
                        singleLetter = True

        # Checks if the proposition entered is an uppercase letter
        if lowercase != lowercase.upper():
            for x in prop:
                if x.islower():
                    if lower.count(x) == 0:
                        lower = lower + x
                        print("  [ Proposition [", x, "] should be in uppercase. ]")

        # Checks if the proposition entered is a T or F
        for x in prop:
            if x == "T" or x == "F":
                if containsTorF.count(x) == 0:
                    containsTorF = containsTorF + x
                    print("  [ Variable [", x, "] can't be used. ]")

        # Checks if there are proposition that are repeated
        for x in prop:
            if prop.count(x) > 1:
                if duplicates.count(x) == 0:
                    duplicates = duplicates + x
                    print('  [ Proposition [', x, '] is duplicated. ]')

        if letterCheck and singleLetter and lower == "" and duplicates == "" and containsTorF == "":
            break

# Checking proposition

print()
proposition = input("Enter proposition: ")

proposition = checkPropositionSyntax(proposition)

displayTruthTable(proposition)

