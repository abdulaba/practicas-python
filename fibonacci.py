def fibonacci():
    my_list = list(range(2))
    counter = 0
    while len(my_list) < 51:
        my_list.append(my_list[-1] + my_list[-2])
        counter = my_list[-1]
        print(my_list)

fibonacci()