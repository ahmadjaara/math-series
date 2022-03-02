from math_series.series import fibo_series 
from math_series.series import luc_number
from math_series.series import sum_series


"""
** fibonacci function :

if input number equal : 0,1,2,3,4,5,6,7 for example
output for each number : 0,1,1,2,35,8,13
description :recursion 

        if n==0 or n==1:
            return n
        else:
            return fibo_series(n-1) +fibo_series(n-2)
        **return false #if the input is string 

** lucas number :

if input number equal : 0,1,2,3,4,5,6,7 for example
output for each number: 2,1,3,4,7,11,18

        if l ==0 :
            return 2
        elif l ==1 :
            return 1
        else:
            return luc_number(l-1) + luc_number(l-2)
        **return false #if the input is string 

sum_series function :

input number: 0,1,2,3,4,5,6,7 for example 
and two optional parameters will have default values of 0 and 1 
parametr==> x,y 

output: if x,y=0,1 ==> output fibo_series(number) ==> 0,1,1,2,35,8,13
        if x,y=2,1 ==> output luc_series(number) ==> 2,1,3,4,7,11,18

"""




#tests for fibo_series function 


#test 1
def test_fibo_series_int1():
    actual= fibo_series(6)
    expected = 8
    assert actual == expected
#test 2
def test_fibo_series_int2():
    actual= fibo_series(7)
    expected = 13
    assert actual == expected
#test 3
def test_fibo_series_int2():
    actual= fibo_series(0)
    expected = 0
    assert actual == expected
#test 4 type error for string input
def test_fibo_series_str():
    actual =fibo_series("str")
    expected = False
    assert actual == expected




#test for luc_number function


#test 1
def test_luc_number_int1():
    actual =luc_number(5)
    expected = 11
    assert actual == expected
#test 2
def test_luc_number_int2():
    actual =luc_number(6)
    expected = 18
    assert actual == expected
#test 3
def test_luc_number_int3():
    actual =luc_number(0)
    expected = 2
    assert actual == expected
#test 4 type error for string input
def test_luc_number_str():
    actual =fibo_series("str")
    expected = False
    assert actual == expected
  

#test for sum_series 

def test_sum_series1():
    actual = sum_series(3)
    expected = 2
    assert actual == expected

def test_sum_series2():
    actual = sum_series(3,2,1)
    expected = 4
    assert actual == expected

def test_sum_series2():
    actual = sum_series(4,0,1)
    expected = 3
    assert actual == expected

def test_sum_series3():
    actual =sum_series(4,5,6)
    expected ="""please enter x,y=0,1 for fibonacci series or enter x,y=2,1 for lucas series """
    assert actual == expected

