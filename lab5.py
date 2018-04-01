
import os

user = {}

def Clear_Screen():
    os.system('CLS')

def Read_File():
    with open("in.txt") as file:
        for line in file:
            key, *value = line.split()
            user[int(key)] = value

def Delete_Item_list():
    Clear_Screen()
    print("Удаление")
    while True:
        num_elem = numerize(input("Введите ID для удаления: "))
        if isinstance(num_elem, int):
            break
    user.pop(num_elem)
    for key in range(num_elem + 1, len(user) + 1):
        user[key - 1] = user.pop(key)
    print("Удалено")
    Write_File()
    input(' ')
    return

def Write_File():
    with open('in.txt', 'w') as out:
        for key, val in user.items():
            out.write(' '.join([str(key)] + val) + '\n')

def registration():
    Clear_Screen()
    print("Регистрация пользователя")
    count_user = len(user)
    while True:
        while True:
            login = input("Введите новый логин: ")
            if (isNotEmpty(login) != False):
                break
        rev_d = dict((v, k) for k, vals in user.items() for v in vals)
        if rev_d.get(login) != None:
            print("Пользователь с таким логином уже есть!")
        else:
            break
    while True:
        password = input("Введите пароль: ")
        if (isNotEmpty(password) != False):
            break
    user[count_user] = [login, password, "user"]
    Write_File()
    input(' ')

def Reset_Password():
    Clear_Screen()
    print("Сбрасывание пароля")
    Show_Users_List()
    while True:
        idUser = numerize(input("Введите ID пользователя: "))
        if isinstance(idUser, int):
            break
    if (idUser >= len(user)) and (idUser < 0):
        print("ID не существует!")
    else:
        user[idUser][1] = "qwerty"
        print("Пароль сброшен на qwerty!")
        Write_File()
    input(' ')
    return

def Show_Users_List():
    Clear_Screen()
    print("ID\tЛогин\tПароль\tРоль")
    with open("in.txt", "r") as file:
         content = file.read()
         print(content)
    input(' ')
    return

def Change_Login(id):
    Clear_Screen()
    print("Изменение логина")
    while True:
        while True:
            login_change = input("Введите новый логин: ")
            if (isNotEmpty(login_change) != False):
                break
        rev_d = dict((v, k) for k, vals in user.items() for v in vals)
        if rev_d.get(login_change) != None:
            print("Пользователь с таким логином уже есть!")
        else:
            break
    user[id][0] = login_change
    Write_File()
    print("Логин успешно изменен!")
    input(' ')
    return

def Change_Password(id):
    Clear_Screen()
    check_pas = True
    print("Изменение пароля")
    while True:
        user[id][1] = input("Введите новый пароль: ")
        if (isNotEmpty( user[id][1])!=False):
            break
    print("Пароль успешно изменен!")
    Write_File()
    input(' ')
    return

def User_Panel(useId):
    Clear_Screen()
    while True:
        Clear_Screen()
        print("Добро пожаловать, " + user[useId][0] + "! (пользователь)")
        print("1. Изменить логин\n2. Изменить пароль\n3. Выйти с аккаунта\n4. Выход из программы")
        while True:
            num = numerize(input("Введите номер: "))
            if isinstance(num, int):
                break
        if num == 1:
            Change_Login(useId)
        elif num == 2:
            Change_Password(useId)
        elif num == 3:
            break
        elif num == 4:
            exit(0)
    return

def Change_Role():
    Clear_Screen()
    print("Изменить пароль\логин\роль пользователя")
    Show_Users_List()
    while True:
        idUser = numerize(input("Введите ID пользователя: "))
        if isinstance(idUser, int):
            break
    if (idUser >= len(user)) and (idUser < 0):
            print("ID не существует! Введите правильный id.")
    else:
        while True:
            print("1. Изменить роль пользователя\n2. Изменить логин пользователя\n3. Изменить пароль пользователя\n4. Выход из редактирования\n")
            while True:
                num = numerize(input("Ваш выбор: "))
                if isinstance(num, int):
                    break
            if num == 1:
               print("Роль:\n\t1. Администратор\n\t2. Пользователь\n")
               while True:
                  num = numerize(input("Выберите роль: "))
                  if isinstance(num, int):
                     break
               temp = "user"
               if num == 1:
                  temp = "admin"
               user[idUser][2] = temp
               Write_File()
               print("Успешно заменено")
            elif num == 2:
                 Change_Login(idUser)
            elif num == 3:
                 Change_Password(idUser)
            elif num ==4:
                break
            else:
                print("Такого пункта меню нет!")
    input(' ')
    return

def Admin_Panel(adminId):
    Clear_Screen()
    while True:
        Clear_Screen()
        print("Добро пожаловать, "+user[adminId][0]+"! (администратор)")
        print("1. Создать пользователя\n2. Изменить логин\n3. Изменить пароль\n4. Сбросить пароль\n5. Вывести список пользователей\n6. Изменить роль/пароль/логин\n7. Удалить пользователя\n8. Выйти с аккаунта\n9. Выход из программы\n")
        while True:
            num = numerize(input("Ваш выбор: "))
            if isinstance(num, int):
                break
        if num == 1:
            registration()
        elif num == 2:
            Change_Login(adminId)
        elif num == 3:
            Change_Password(adminId)
        elif num == 4:
            Reset_Password()
        elif num == 5:
            Show_Users_List()
        elif num == 6:
            Change_Role()
        elif num == 7:
            Delete_Item_list()
        elif num == 8:
            break
        elif num == 9:
            exit(0)
        else:
            print("Такого пункта меню нет!")

def loginIn():
    Clear_Screen()
    print("Вход в систему")

    while True:
       login = input("Введите логин: ")
       if (isNotEmpty(login) != False):
           break
    while True:
       password = input("Введите пароль: ")
       if (isNotEmpty(password) != False):
            break

    for i in range(len(user)):
        if (login == user[i][0]) and (password == user[i][1]):
            print("Вы вошли в систему!")
            if user[i][2] == "admin":
                Admin_Panel(i)
            else:
                User_Panel(i)
            return
    print("Логин или пароль были введены не верно! Введите пароль или логин заново")
    return

def isNotEmpty(s):
    return bool(s and s.strip())

def numerize(s):
    try:
        return int(s)
    except ValueError:
        return None

def Main():
    Clear_Screen()
    Read_File()
    while True:
        print("Mеню:\n1. Регистрация в системе\n2. Вход в программу\n3. Выход из программы\n")
        while True:
            choice = numerize(input("Введите номер: "))
            if isinstance(choice, int):
                break
        if choice == 1:
            registration()
        elif choice == 2:
            loginIn()
        elif choice == 3:
            print("Выход из программы выполнен...")
            break
        else:
            print("Такого номера в списке нет!")
    input('')
    return

Main()