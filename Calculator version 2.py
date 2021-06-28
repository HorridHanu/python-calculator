#CODE LANGUAGE IS PYTHON
#CODE BY HANU
#EDUCATIONAL PURPOSE ONLY!
#PROGRAME DATE : 20/JUNE/2021
#CODE FOR FAULTY CALCULATOR.



from datetime import datetime

now = datetime.now()                                                         #time NOW
time = now.strftime("%H:%M")                              #FORMAT to show time
print("\nTIME- "+time)

date= now.strftime("%d-%m-%y")
print("DATE- ",date)



def addtion(num1,num2):                                   #define function for add
     print("After Addtion Answer Is",num1 + num2)

def substraction(num1,num2):                              #define function for substract
    print('After Substaction Answer Is:',num1-num2)

def multiply(num1,num2):                                  #define function for multiply
    print('After Multiply Answer Is;',num1*num2)

def divide(num1,num2):                                    #define function for divide
    print('After Divide Answer Is;',num1/num2)



print("Hello Sir!")
print("\t<!!Press for Operation!!>")
print("\t1.Addition.")
print("\t2.Substraction.")
print("\t3.Multiply.")
print("\t4.Divide.")
print("\t5.Exit!")



while True:
    choice=int(input("\nEnter your choice(1-5): "))             #enter the choice
    if choice==5:
        print("Thanks for using!")
        break                                              #break loop if choice is 5



    num1= float(input("Enter the operand 1: "))
    num2= float(input("Enter the operand 2: "))



    if choice==1:                                          #for addition
        addtion(num1,num2)

    elif choice==2:                                        #for substraction
        substraction(num1,num2)

    elif choice==3:                                        #for multiply
        multiply(num1,num2)

    elif choice==4:                                        #for divide
        if num2==0:
            print("Ans Is Not define")                            #for if denominator is 0
        else:
            divide(num1,num2)


    else:                                                  #if choice is out of range
        print("Invalid choice TRY AGAIN!")

