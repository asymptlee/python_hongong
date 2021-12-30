def print_n_times(n, *values):
    
    for i in range(n):

        for elem in values:
            print(elem)

        print()


print_n_times(3, "Hi~~", "Funny", "Python Programming")

