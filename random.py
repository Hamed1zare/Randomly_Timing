import random
computer_number = random.randint(10, 30)
attempts = 0
while True:
    user_number = int(input())
    attempts = attempts + 1
    if user_number == computer_number:
        print("afarin")
        break
    elif user_number < computer_number:
        print("up")
    elif user_number > computer_number:
        print("down")
print("try", attempts, "time")