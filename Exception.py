#exception = An event that interrupts the flow of a program
#            (ZeroDivisionError, TypeError, ValueError)
#            1.try, 2.except, 3.finally

try:
    num = int(input("Enter a number: "))
    print(1 / num)
except ZeroDivisionError:
     print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter number only please!")

finally:
    print("Do some cleanup here")






















