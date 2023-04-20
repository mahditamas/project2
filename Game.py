import random
""" sang = 1 , kaghaz = 2 , gheychi = 3"""
n = 0 #number of user wins
j = 0 #number of cpu wins
cpu_score = 0 #cpu point
user_score = 0 #user point
user =0 #user choice
cpu =0 #cpu choice


while not ((abs(n - j) == 5) and (abs(user_score - cpu_score ) >= 50)):
    user = int(input("Enter your choice (sang = 1 , kaghaz = 2 , gheychi = 3) :")) 
    cpu = (random.randrange(1, 4))
    if user == 1:
        if cpu == 1:
            print('user and cpu is equal')

        elif cpu == 2:
            print('the computer won')

            j += 1
            n = 0
            cpu_score += (2 ** (j - 1))

        elif cpu == 3:
            print('the user won')

            n = n + 1
            j = 0
            user_score += (2 ** (n - 1))

    elif user == 2:
        if cpu == 1:
            print('the user won')

            n = n + 1
            j = 0
            user_score += (2 ** (n - 1))

        elif cpu == 2:
            print('user and cpu is equal')

        elif cpu == 3:
            print('the computer won')

            j += 1
            n = 0
            cpu_score += (2 ** (j - 1))


    elif user == 3:
        if cpu == 1:
            print('the computer won')

            j += 1
            n = 0
            cpu_score += (2 ** (j - 1))

        elif cpu == 2:
            print('the user won')

            n = n + 1
            j = 0
            user_score += (2 ** (n - 1))

        elif cpu == 3:
            print('user and cpu is equal')

    print("cpu score ::", cpu_score)
    print("user score :", user_score)