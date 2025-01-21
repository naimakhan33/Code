from time import *
import random as r

def mistake(paratest,usertest):
    error = 0
    for i in range(len(paratest)):
         try:
             if paratest[i] != usertest[i]:
                error = error + 1
         except :
                error = error + 1

def speed_time (time_start , end_time,userinput):
     time_delay = end_time - time_start
     time_R = round( time_delay ,2) #2 digits ROf
     speed = len(userinput)/time_R
     return round(speed)

test = [" A paragraph is a self-contained unit of discourse in writing dealing with a particular point or ideas."
"my name is khan", "welcome to apna clg."]
test1 = r.choice(test)
print("typing speed")
print(test1)
print()
print()
time_1 = time()
testinput = input("enter:")
time_2 = time()

print('speed:', speed_time(time_1, time_2, testinput), "w/sec")
print("Error:", mistake(test1, testinput))


