#A program that lists powers of 2 and 1/x for numbers 1 t0 10.

def main():

    for x in range(1,11):
      

        print("{0}\t{1}\t{2:0.3f}".format(x,2**x,1/x))

main()
