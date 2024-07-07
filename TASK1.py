def add(x,y):
    z=x+y
    return z

def sub(x,y):
    z=x-y
    return z
def mul(x,y):
    z=x*y
    return z

def div(x,y):
    z=x/y                                        
    return z
nextcalc=input("YOU WANT TO DO CALCULATION y/n:-")

print("###############OPERATIONS################# \n 1.ADDITION \n 2.SUBTRACTION \n 3.MULTIPLICATION \n 4.DIVISION")
while nextcalc=="y":
    choice=input("ENTER OPERATION YOU WANT TO PEROFORM:-  ")
    if choice in ('1','2','3','4'):
        
        try :
            
             num1=float(input("ENTER FIRST NUMBER:="))
             num2=float(input("ENTER SECOND NUMBER:="))
        except ValueError:
             print("!!!!!!!!ENTER VALID INPUT!!!!!!!!!!!!")
             continue
        if choice=='1':
            print(num1, "+", num2,"=", add(num1,num2))
        elif choice=='2':
            print(num1,"-",num2,"=",sub(num1,num2))
        elif choice=='3':
            print(num1,"*",num2,"=",mul(num1,num2))
        elif choice=='4':
            print(num1,"%",num2,"=",div(num1,num2))
            
        nextcalc=input("YOU WANT TO DO ANOTHER CALCULATION y/n")
        if nextcalc=="n":
            break
    else:
        print("!!!!!!!!!invalid input!!!!!!!!!!!")
            


