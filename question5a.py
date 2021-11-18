#Program that reads a grade between 1 and 5.

def grading():

    
    n=int(input("Enter grade(1-5) :"))   

    
    description=["Fail","Poor","Fair","Good","Excellent"]

    
    grade=description[n-1]

    
    print(grade)
        
    
grading()
