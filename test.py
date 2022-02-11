x = '(        )'
def zet(string: str):
    mas_x = []
    num1 = 0
    num2 = 0
    for character in string:
        mas_x.append(character)

    for character in mas_x:
        if character == '(':
            num1 += 1
        elif character == ')':
            num2 += 1
        else:
            None

    if num1 == num2:
        return True
    else:
        return False


print(zet(x))




