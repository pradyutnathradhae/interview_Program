import time

def first_mod(n):
    print("*", end="")
    for i in range((n - 3)//2):
        print(" ", end="")

    for i in range((n + 1)//2):
        print("*", end = "")
    print("")

def secnd_mod(n):
    for i in range((n-3)//2):
        print("*", end= "")
        for j in range((n - 3)//2):
            print(" ", end="")
        print("*")

def thrd_mod(n):
    for i in range(n):
        print("*", end="")
    print("")

def forth_mod(n):
    for i in range((n-3)//2):
        for j in range((n-1)//2):
            print(" ", end="")
        print("*", end="")
        for j in range((n-3)//2):
            print(" ", end="")
        print("*")

def fifth_mod(n):
    for i in range((n+1)//2):
        print("*", end="")
    for i in range((n-3)//2):
        print(" ",end="")
    print("*")
        
if __name__ == "__main__":
    n = int(input("Enter any odd number between 5 to 15 :-  "))
    print("Loding Pattern ....")
    time.sleep(3)
    if(n > 15):
        print("Image is too big to Load!")
        print("Failed!")
    elif(n < 5):
        print("Image is too small to Load!")
        print("Failed!")
    else:
        if(n%2 == 0):
            print("Can't process  with even number!")
            print("Failed!")
        else:
            print()
            first_mod(n)
            secnd_mod(n)
            thrd_mod(n)
            forth_mod(n)
            fifth_mod(n)
            print()
            print("Successful!")
    
