#A program that finds the sum of number values of letters of a word.


def main():
    
    alph="abcdefghijklmnopqrstuvwxyz"
    
    word=input("Enter word :")

    word_lowercase=word.lower()
    
    
    total=0    

    for char in word_lowercase:

       value=alph.index(char)+1

       total=total+value

    print(total)

main()



        

        

    
