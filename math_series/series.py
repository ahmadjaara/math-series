#fibo_series function 

def fibo_series(n) :

    """
    input: n integer index for fibonacci series element 
    output: fibonacci series element 
    
    description:
    fibo_series take an integer and return the element in the fibonacci series that has that index 
    for example:
        fibonacci series : index==> 0,1,2,3,4,5,6,7 //fibonacci series ==>  0,1,1,2,3,5,8,13  

        fibo_series(5) ==> return 5

    """
    try:
        if n==0 or n==1:
            return n
        else:
            return fibo_series(n-1) +fibo_series(n-2)
    except TypeError:
        return(False)



#luc_number function 

def luc_number(l):

    """
    input: n integer index for lucas series element 
    output: lucas series element 
    
    description:
    luc_number take an integer and return the element in the lucas series that has that index 
    for example:
        lucas series : index==> 0,1,2,3,4,5,6,7 //lucas series ==>  2,1,3,4,7,11,18  

        luc_number(5) ==> return 11

    """
    try:
        if l ==0 :
            return 2
        elif l ==1 :
            return 1
        else:
            return luc_number(l-1) + luc_number(l-2)
    except TypeError:
        return(False)


#sum_series function

def sum_series(k,x=0,y=1):

    """ 
        input : K ==>  Integer represent the index for fibonacci series or lucas series
                x,y==> two optional parameters will have default values of 0 and 1 
                      ==> these two parameter determine the series type 
                        ==> x,y=0,1   series type:fibonacci series
                        ==> x,y=2,1   series type:lucas series  

        output: integer element ==>for lucas or fibonacci series 
        
        example 
            if x,y=0,1 (default value) ==> output fibo_series(k) ==> 0,1,1,2,35,8,13
            if x,y=2,1 ==> output luc_series(number) ==> 2,1,3,4,7,11,18

    """
   
    try:
        if x==0 and y==1:
            return fibo_series(k)
        elif x==2 and y==1:
            return luc_number(k)
        else:
            return """please enter x,y=0,1 for fibonacci series or enter x,y=2,1 for lucas series """
    except TypeError:
       return(False) 

