import random
import time
import math

score = 0

print ("Level 1 - No Timer, Take your time!")

for question_num in range(1, 11):
    ops = ['+', '-', '*']
    rand=random.randint(1,12)
    rand2=random.randint(1,12)
    operation = random.choice(ops)
    maths = eval(str(rand) + operation + str(rand2))
    print('\nQuestion number: {}'.format(question_num))
    print ("The question is",rand,operation,rand2)


    d=int(input ("What is your answer:"))
    if d==maths:
        print ("Correct")
        score=score+1
    else:
        print ("Incorrect. The actual answer is",maths)
    
print("\n")

if (score<6):
    print("Bummer, you got ",(score)," out of 10. Try again to get a better score")
else:
    print("Well done! You got ",(score),"out of 10")




print("\n")
print("\n")




print ("You made it to Level 2! - You have 20 seconds to answer as much as you can.")

score1 = 0

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = ', {:02d}'.format(secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

countdown(20)

for question_num in range(1, 11):
    ops = ['+', '-', '*']
    rand=random.randint(1,12)
    rand2=random.randint(1,12)
    operation = random.choice(ops)
    maths = eval(str(rand) + operation + str(rand2))
    print('\nQuestion number: {}'.format(question_num))
    print ("The question is",rand,operation,rand2)


    d=int(input ("What is your answer:"))
    if d==maths:
        print ("Correct")
        score1=score1+1
    else:
        print ("Incorrect. The actual answer is",maths)

print("\n")

if (score1<6):
    print("Bummer, you got ",(score1)," out of 10. Try again to get a better score")
else:
    print("Well done! You got ",(score1),"out of 10")


    
print("\n")
print("\n")



print ("Last but not least Level 3! - You have 10 seconds to answer as much as you can. Good Luck!")

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = ', {:02d}'.format(secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

countdown(10)

score2 = 0

for question_num in range(1, 11):
    ops = ['+', '-', '*']
    rand=random.randint(1,12)
    rand2=random.randint(1,12)
    operation = random.choice(ops)
    maths = eval(str(rand) + operation + str(rand2))
    print('\nQuestion number: {}'.format(question_num))
    print ("The question is",rand,operation,rand2)


    d=int(input ("What is your answer:"))
    if d==maths:
        print ("Correct")
        score2=score2+1
    else:
        print ("Incorrect. The actual answer is",maths)

print("\n")

if (score2<6):
    print("Bummer, you got ",(score2)," out of 10. Try again to get a better score")
else:
    print("Well done! You got ",(score2),"out of 10")



print("\n")
print("\n")


print("You got ", (score+score1+score2)," out of 30")

