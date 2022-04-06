
def textGame():
    a = input("Where do you want to go, USA or Egypt ? : \n")
    if a == "USA":
        b = input("where do you want to go in USA?\n type 1 for california or 2 for las vegas :")
        if b == 1 :
            print("welcome to the california:") 
            c  = input("where do you want to stay :\n Type 1 for Hotel or 2 for become a homeless :")
            if c == 1 : 
                print("Wecome to the hotel california!  such a lovely place!  such a lovely place ")
            else:
                print("You are a wild animal who don't want a home!")
        elif b == 2 :
            print('Welcome the sin city Las Vegas ')
            d = input('what do you want to do in las vegas: \n 1 for casino 2 for nothing')
            if d == 1 : 
                print("there is a house in sin city! they called the rising sun...to shun.....(sing along)")
            elif d == 2 :
                print("thanks for the visit!!now go to hell")
        else:
            print("Wrong Input!")
    elif a == 'Egypt':
        print("welcome to the Egypt")
        g = input("what will you do in Egypt?: \n 1 for travel 2 for become a Mummy ")
        if g == 1 :
            print("go for it...have a good trip")
        elif g==2:
            print("Mummies are coming to make you a Mummy")
        else:
            print("Wrong input")
    else:
        print("wrong input")    
    return textGame

textGame()