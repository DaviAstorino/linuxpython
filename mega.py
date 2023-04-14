import random
while True:
    a =int (input("quantos jogos:"))
    if a == 0:
        quit()
    for y in range(1,a+1):
        print("jogo",y,":")
        num=" "
        for b in range(1,15):
            c=random.randint(0,25)
            num=num+" "+str(c)
        print(num)
            
