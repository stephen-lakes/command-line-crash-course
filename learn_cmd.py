import random


game_commands = {'q': 'quit', 'h': 'hint', 's' : 'start over' }


words = open('words.txt', 'r')

for word in words:
    print(word)


condition = True
question = "random question"
answer = "random question"


while condition:
    
    print(question)
    
    ans = input("answer to the question: ")

    if ans == answer:
        print("correct")
        
    elif ans == 'q':
        print("Exiting the shell")    
        break
    
    else:
        print("Incorrect")
    
