def primos():
    for number in range(2,101):
        if number == 2 or number == 3 or number % 2 >= 1 and number % 3 >= 1 and number % 5 >= 1:
            print(number)
        

primos()