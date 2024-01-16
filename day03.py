#연습문제 6.5_2
guess_me = 7
number = 1
while (True):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print ("found it!")
        break
    else:
        print("oops")
        break
    number = number +1

