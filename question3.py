#A program that reads two numbers from the user and prints the product digit by digit.

def main():

    firstnum=int(input("Enter first number : "))

    secondnum=int(input("Enter second number : "))

    product=firstnum*secondnum

    for digit in str(product):

        print(digit)


main()
          
