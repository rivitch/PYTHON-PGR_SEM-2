print("\nНапишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.\nФункцию hex используйте для проверки своего результата.\n")

num = int(input("Введите число :"))
#print(hex(num))
base =16
orig = num
res = ""
list_1 = ["a","b","c","d","e",'f']
while num:
    if num%base<=9:
        res = str(num%base)+res
    else:
        res = str(list_1[num%base-10])+res
    #print(num%base)
    num //= base   
print(f"Число {orig} в {base}-ичной системе счисления будет : {res}")
print("\nПроверка с помощью функции hex: ")
print(hex(orig)[2:])
