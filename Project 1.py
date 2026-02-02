import random
'''
1 for R
-1 for P
0 for S
'''
while True:
    computer = random.choice([1,-1,0])
    youstr = input("Enter your choice: ")
    youDict = {
        "R" : 1,
        "P" : -1,
        "S" : 0
    }
    reverseDict = {
        1 : "R",
        -1 : "P",
        0 : "S"
    }
    you = youDict[youstr]

    print(f"You choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

    if(computer == you):    
        print("It's a draw")
    else:
        if(computer == -1 and you == 1):
            print("you lose") 
        elif(computer == -1 and you == 0):
            print("you win") 
        elif(computer == 1 and you == -1):
                print("you win")
        elif(computer == 1 and you == 0):
            print("you lose") 
        elif(computer == 0 and you == 1):
            print("you win")
        elif(computer == 0 and you == -1):
            print("you lose") 
        else:
            print("something went wrong !") 
     