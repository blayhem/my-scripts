# This script prints random numbers WITHOUT REPETITION from 1 
# to *max* everytime the user presses enter.
import random as r
max = int(raw_input("Max number: "))+1
dic = {''}
while True:
    num = r.randrange(1,max,1)
    if num not in dic:
        print num,
        raw_input()
        dic.add(num)
    if len(dic)==max:
        exit()

