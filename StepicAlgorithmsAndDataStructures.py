#Курс по алгоритмам и структурам данных https://stepik.org/lesson/318098/step/2?unit=300846
# Начало 19.11.23 Конец

#1
#A = '705'
#B = int(A, 8)
#print(bin(B))

#2
#temperature = int(input())

#if temperature < -25:
#    result = "жутко холодно"
#elif temperature >= -26 and temperature < 0:
#    result = "холодно"
#elif temperature >= 0 and temperature < 10:
#    result = "прохладно"
#elif temperature >= 10 and temperature < 25:
#    result = "тепло"
#else:
#    result = "жара"

#print(result)

#3
#line = input()
#numbers = list(map(int, line.split()))
#even_number = next(number for number in numbers if number % 2 == 0)
#print(even_number)

#4

#N = int(input())

#min_number_ending_with_3 = float('inf')

#for _ in range(N):
#    number = int(input())
#    if number % 10 == 3 and number < min_number_ending_with_3:
#        min_number_ending_with_3 = number
#print(min_number_ending_with_3)

#5
#numbers_str = input()

#numbers = list(map(int, numbers_str.split()))

#count_even = 0
#count_odd = 0

#for number in numbers:
#    if number % 2 == 0:
#        count_even += 1
#    else:
#        count_odd += 1

#if count_even == count_odd:
#    result = "equal"
#elif count_even > count_odd:
#    result = "even"
#else:
#    result = "odd"

#print(result)




#input()
#print()



#Курс олимипиадное программирование

#1

#a = int(input())
#b = int(input())
#print(a % b, -a % b, a % -b, -a % -b)

#2

#n, k = map(int, input().split())
