def p1():
    name = 'Maxim'
    greeting = f'Привет, меня зовут {name}.'
    print(f'{greeting} Сейчас я изучаю тему строки')
def p2():
    s = 'Строки Python'
    s1 = s*7
    s2 = s + s1
    print(f'{s},{s1},{s2}')
def p3():
    string = input('Введите строку: ')
    first = string[0]
    last = string[-1]
    print(f'{first}|{last}')
def p4():
    string = input('Введите строку: ')
    new_string = string[-1] + string[1:-1] + string[0]
    print(f'{string}->{new_string}')
def p5():
    string = input('Введите строку: ')
    new_string = string[::-1]
    print(f'{string}->{new_string}')
def p6():
    string = input()
    string = string.split(' ')
    string[1] = string[1].replace('a', 'A')
    if string[1].count('a') == 0:
        print('ERROR!!!')
    print(f'{string[0].count("a")},{string[1]},{len(string[2])}')
def p7():
    string = input()
    if string.lower() == 'вниз':
        string = string.lower()
    elif string.lower() == 'вверх':
        string = string.upper()
    print(f'{string}')
def p8():
    string = input()
    if string.isupper() == True or string.islower() == True:
        print('False')
        return False
    elif string.isdigit() == True or string.isalpha() == True:
        print('False')
        return False    
    else:
        print('True')
        return True
def p9():
    string = input()
    if string.lower().startswith('привет'):
        print('И тебе привет!')
    elif string.lower().endswith('пока'):
        print('Досвидос!')

num = int(input('Выбери программу: '))
if num == 1:
    p1()
elif num == 2:
    p2()
elif num == 3:
    p3()
elif num == 4:
    p4()
elif num == 5:
    p5()
elif num == 6:
    p6()
elif num == 7:
    p7()
elif num == 8:
    p8()
elif num == 9:
    p9()