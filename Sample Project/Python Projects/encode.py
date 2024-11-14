'''
Author : Mohammad Hossein Radpour
Project.No : 06
'''
# This program will encode provided string base on index position 
# First we import random module
import random

def econde(text:str) -> str:
    mylist = []
    for index,value in enumerate(text): 
        if value == ' ':
            mylist.append('_'+str(index))
            continue
        mylist.append(value+str(index))
    random.shuffle(mylist)
    return ' '.join(mylist)

text = 'Hello This is test'
print(econde(text=text))
# After we get result put that into decode project in previous project