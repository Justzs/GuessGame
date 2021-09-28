from random import randrange

class MyGame:
    def __init__(self):
        random_number = randrange(100)
        
        i=1
        for _ in range(10):
            io = int(input("Guess number : "))
            if(io == random_number):
                print("===========================")
                print("===========================\n")
                print("Secret number is", random_number ,"\nYou win!" , "\nYou guessed it in" , i ,"tries.\n")
                print("===========================")
                print("===========================")
                break
            elif(io < random_number):
                print("Your guess is low.")
            elif(io > random_number):
                print("Your gusee is hight.")

            if(i == 10):
                print("Secret number is", random_number)
                print("You lose")
                break

            i+=1

# Launch ...
if __name__ == '__main__':
    app = MyGame()
