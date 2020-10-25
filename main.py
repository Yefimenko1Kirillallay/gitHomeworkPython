# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/





    print('''
    1.Домашняя работа на #1
           2. Дано число. Если оно от -10 до 10 не включительно, то увеличить его на 5, иначе уменьшить на 10.
           3. Пользователь вводит номер месяца, вывести название месяца.
           4. Робот может перемещаться в четырех направлениях 
           («11» — север, «12» — запад, «13» — юг, «14» — восток)
            и принимать три цифровые команды: 0 — продолжать движение,
             1 — поворот налево, –1 — поворот направо. Дан число 
             (11, 12, 13 или 14) — исходное направление робота и целое число N (0, 1 или -1)
              — посланная ему команда. Вывести направление робота после выполнения полученной команды 
              (то есть север, запад, юг или восток).\n''')
    dght=int(input("Введите число номер задания dght :\n"))
    firm = True
while firm == True:

    if dght==1:

        gh="Silence is golden";
        NomberOne=34;
        NomberTwo=5;

        print(gh,"\n",NomberOne,'+',NomberTwo,'=', NomberTwo+NomberOne)
        print(NomberOne,'*',NomberTwo,'=', NomberTwo*NomberOne)

        f=int(input("В ведите число f") );
        y=int(input("В ведите число y") );
        dg=int(input("В ведите число dg") );

        print(f,'*',2,'=',f*2,"\n",y,'-',3,'=',y-3,"\n",dg,'2','=',dg,'*',dg,'=',dg*dg,"\n",(f*2),'+',(y-3),'+',(dg*dg),'=',(f*2)+(y-3)+(dg*dg))

        print('''
        AAAAAAAA
        AAAAAAAA
        AAAAAAAA
        AAAAAAAA
        AAAAAAAA\n''')

        break
    if dght==2:

        print('''
        2. Дано число. Если оно от -10 до 10 не включительно, то увеличить его на 5, иначе уменьшить на 10.''')

        Nomber3=int(input("write nomber"))

        if Nomber3>-11and Nomber3<10:
            print(Nomber3,'+',5,'=',Nomber3+5)
        else:
            print(Nomber3,'-',10,'=',Nomber3-10)
        break
    if dght == 3:
        print('''3. Пользователь вводит номер месяца, вывести название месяца.''')

        NomberOfMonth = int(input("write Month"))

        if NomberOfMonth >0 and NomberOfMonth<13:

            if NomberOfMonth ==1:
                print("Январь")
            elif NomberOfMonth ==2:
                print("Февраль")
            elif NomberOfMonth ==3:
                print("Март")
            elif NomberOfMonth ==4:
                print("Апрел")
            elif NomberOfMonth ==5:
                print("Май")
            elif NomberOfMonth ==6:
                print("Июнь")
            elif NomberOfMonth ==7:
                print("Июль")
            elif NomberOfMonth ==8:
                print("Август")
            elif NomberOfMonth ==9:
                print("Сентябрь")
            elif NomberOfMonth ==10:
                print("Октябрь")
            elif NomberOfMonth ==11:
                print("Ноябрь")
            elif NomberOfMonth ==12:
                print("Декабрь")
                break
    if dght == 4:
        print(''' 4. Робот может перемещаться в четырех направлениях 
       («11» — север, «12» — запад, «13» — юг, «14» — восток)
        и принимать три цифровые команды: 0 — продолжать движение,
         1 — поворот налево, –1 — поворот направо. Дан число 
         (11, 12, 13 или 14) — исходное направление робота и целое число N (0, 1 или -1)
          — посланная ему команда. Вывести направление робота после выполнения полученной команды 
          (то есть север, запад, юг или восток).\n''')

        print("«11» — север, «12» — запад, «13» — юг, «14» — восток")
        pologenie=int(input("Введите первоночальное напровление робота : "))
        N = int(input("Введите N -команду роботу  -1 ,0, 1 : "))

    if  pologenie >=14 and pologenie >=11:

        if pologenie==11 :
            if N== -1:
                print("направлениe Роботa на восток")
            if N== 0:
                print("направлениe Роботa на север")
            if N== 1:
                print("направлениe Роботa на запад")

        if pologenie==12 :
            if N== -1:
                print("направлениe Роботa на север ")
            if N== 0:
                print("направлениe Роботa на запад")
            if N== 1:
                print("направлениe Роботa на юг")

        if pologenie==13 :
            if N== -1:
                print("направлениe Роботa на запад")
            if N== 0:
                print("направлениe Роботa на юг")
            if N== 1:
                print("направлениe Роботa на восток")

        if pologenie==14 :
            if N== -1:
                print("направлениe Роботa на юг")
            if N== 0:
                print("направлениe Роботa на восток")
            if N== 1:
                print("направлениe Роботa на север")

    break
