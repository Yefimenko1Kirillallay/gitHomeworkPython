

print('''Начав тренировки, лыжник в первый день пробежал 10 км.
 Каждый следующий день он увеличивал пробег на 10% от пробега предыдущего дня. Определите: 
 1)  пробег лыжника за второй, третий, ..., десятый день тренировок; 
 2) какой суммарный путь он пробежал за первые 7 дней тренировок. 
 3) суммарный путь за n дней тренировок; 
 4) в какой день ему следует прекратить увеличивать пробег, если он не должен превышать 80 км?''''')

NomberZadania=int(input("Введите NomberZadania 1 или 2 или 3 или 4 - "))

KMl=10
sumadays=0

if NomberZadania==1:
    kmschothik = 10
    for i in range(2,11):
        KMl=KMl+KMl/10
        print("За",i,"день лыжник пробег",round(KMl,2),"km")




elif NomberZadania == 2:
        for i in range(1, 8):
            KMl = KMl + KMl / 10
            sumadays=sumadays+KMl
            if i==7:
                print("За",7, "дней лыжник пробег", round(sumadays, 2), "km")


elif NomberZadania == 3:
    ndays=int(input("Введите число n дней : "))
    for i in range(1, ndays+1):
        KMl = KMl + KMl / 10
        sumadays = sumadays + KMl
        if i == ndays:
            print("За", ndays, "дней лыжник пробег", round(sumadays, 2), "km")

elif NomberZadania==4:
    daystop = 1
    kmschothik = 10
    for i in range(10,81):
        daystop = daystop + 1
        i=i+i/10
        kmschothik+=i
        if kmschothik>80:
            daystop-=1
            print("На", daystop, "дне лыжнику придётся прекратить тренировку.Так как он проехал:",kmschothik-i,"km, а на следуйщий день он проедет :",kmschothik,"km.")
            break
