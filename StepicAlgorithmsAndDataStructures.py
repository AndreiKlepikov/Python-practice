#Курс по алгоритмам и структурам данных https://stepik.org/lesson/318098/step/2?unit=300846
# Начало 19.11.23 Конец

#1
#A = '705'
#B = int(A, 8)
#print(bin(B))

#2
temperature = int(input())

if temperature < -25:
    result = "жутко холодно"
elif temperature >= -26 and temperature < 0:
    result = "холодно"
elif temperature >= 0 and temperature < 10:
    result = "прохладно"
elif temperature >= 10 and temperature < 25:
    result = "тепло"
else:
    result = "жара"

print(result)









#input()
#print()

