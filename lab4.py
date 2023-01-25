employees_num = int(input('введите число сотруднников, которые отправляются домой:  '))
sum = 0
distance_list = []
price_list = []
for i in range(employees_num):
    distance = int(input('введите расстояние до дома {0}-го сотрудника в км: '.format(i+1))) #вносим данные в список
    distance_list.append(distance)
for i in range(employees_num):
    price = int(input('Введите тариф {0}-го такси за 1 км:  '.format(i+1)))
    price_list.append(price)
c_distance_list = distance_list[:] #создаём копии списков
c_price_list = price_list[:]
index_list_d = []
index_list_p = []
#заполняем списки индексами в порядке возр/убыв значений переменных
max_distance = 0
for i in range(employees_num):
    index = c_distance_list.index(max(c_distance_list)) 
    index_list_d.append(index)   #создаём списки, где будут хранится индексы наших значений
    c_distance_list[index] = 0
for i in range(employees_num):
    index = c_price_list.index(min(c_price_list))
    index_list_p.append(index)
    c_price_list[index] = 10**10
#для i-го клиента в паре списков с индексам (расстояние по убыванию/цена по возрастанию) ищем нужный индекс такси 
print('такси для клиента 1, 2, 3, ...:')
for i in range(employees_num):
    taxi_num = index_list_p[index_list_d.index(i)]
    print(taxi_num+1)
for i in range(employees_num):
    sum += distance_list[index_list_d[i]]*price_list[index_list_p[i]]
print('необходимо всего заплатить:') #дополняем программу кодом вывода кол-ва денег словами
W1a = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
W1b = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
W2 = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
W3 = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
W4 = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
W5 = ["тысяча", "тысячи", "тысяч"]
W6 = ["рубль", "рубля", "рублей"]

a1 = sum // 100000 #вычисляем для каждого разряда численное значение и даем имя переменной
a2 = (sum // 10000) % 10
a3 = (sum // 1000) % 10
a4 = (sum // 100) % 10
a5 = (sum // 10) % 10
a6 = sum % 10
# в каждый разряд записываем значение и сопоставляем со списком, в котором словами прописаны числа, а также валюта в нужном падеже
poz = ""
if a1 != 0:
    i1 = a1 - 1
    poz += W4[i1] + " "

if a2 == 1 and a3 == 0:
    poz += W3[0] + " "

if a2 != 1:
    if a2 != 0:
        i2 = a2 - 1
        poz += W3[i2] + " "

if a3 != 0:
    if a2 == 1:
        i3 = a3 - 1
        poz += W2[i3] + " " + W5[2] + " "
    else:
        i3 = a3 - 1
        poz += W1b[i3] + " "
        if a3 == 1:
            poz += W5[0] + " "
        elif 1 < a3 < 5:
            poz += W5[1] + " "
        else:
            poz += W5[2] + " "

if (a3 == 0) and (a2 or a1 != 0):
    poz += W5[2] + " "

if a4 != 0:
    i4 = a4 - 1
    poz += W4[i4] + " "

if a5 == 1 and a6 == 0:
    poz += W3[0] + " "

if a5 != 1:
    if a5 != 0:
        i5 = a5 - 1
        poz += W3[i5] + " "

if a6 != 0:
    if a5 == 1:
        i6 = a6 - 1
        poz += W2[i6] + " " + W6[2]
    else:
        i6 = a6 - 1
        poz += W1a[i6] + " "
        if a6 == 1:
            poz += W6[0] + " "
        elif 1 < a6 < 5:
            poz += W6[1] + " "
        else:
            poz += W6[2] + " "

if (a6 == 0) and (a5 or a4 or a3 or  a2 or a1 !=0):
    poz += W6[2]

poz = poz.capitalize() # выводим сумму с большой буквы
print(poz) # печатаем сумму с наименованием валюты в нужном падеже
