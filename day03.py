#연습문제 6.5_03
guess_me = 5
for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me :
        print("found it !")
        break
    else:
        print ("oops")
        break

