
def add(number1, number2):
    return number1 + number2

def sub(numberOne, numberTwo):
    return numberOne - numberTwo

def divide(numberOne, numberTwo):
    if numberTwo == 0:
        raise ValueError
    return numberOne/numberTwo

def concatStr(strOne: str, strTwo: str):
    space = ' '
    return f'{strOne.lower()} {strTwo.lower()}'

