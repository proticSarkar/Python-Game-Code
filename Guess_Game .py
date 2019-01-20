import random
winning_number = random.randint(1,100)

guess = int(input("Guess Your Number : "))
print (" ")
for i in range (1,100) :
    
    if guess == winning_number :
        print (" ")
        print ("You Win ... !")
        print (f"You tried {i} times ...")
        break
    elif guess > winning_number :
        print ("Too high ... ")
        print ("--------")
        print (" ")
        guess = int(input("Guess Your Number : "))
        continue
       
    else :
        print ("Too Low ... ")
        print ("--------")
        print (" ")
        guess = int(input(" Guess Your Number : "))
        continue
        
        
