from random import randint
str0=''
while len(str0)!=4:
  a = randint(0,9)
  b = randint(0,9)
  c = randint(0,9)
  d = randint(0,9)

  str0 = set(str(a)+str(b)+str(c)+str(d))
 # print(str0)

print('Игра Быки и Коровы')
print('Угадывай,я загадал...')
print('Введи число из 4 цифр')

att = 0
while True:
    att +=1
    print('Попытка номер:  ',att)
    str = input(':')

    #if str == 'answ':
     #   print(str0)
      #  continue

    if len(set(str)) != 4 or len(str)!=4:
        print('Цифр должно быть 4! Цифры не должны повторяться ')
        continue

    ck = list(str)
    ck0 = list(str0)

    bulls = 0
    for i in range(4):
        if ck[i] == ck0[i]:
            bulls +=1;
            ck[i] = ' ';
            ck0[i] = '*';
    if bulls ==4:
        print('Вы угадали!')
        break

    cows = 0
    for i in range(4):
        n = ck[i]
        for t in range(4):
            if n == ck0[t]:
                cows +=1
                ck0[t] = '*';
                break

    print('Быков:  ',bulls)
    print('Коров:  ',cows)