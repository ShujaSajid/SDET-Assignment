"""
Function to return the sum of all 
the integers below N which are 
multiples of either X or Y
"""

def find_sum(n, x, y):
    sum = 0
    for i in range(0, n, 1):
         
        # If i in a multiple of x or y
        if (i % x == 0 or i % y == 0):
            sum += i 
    return sum

"""
Now to reverse the obtained sum of the multiples
"""

def reverse_integer(Number):
    reverse = 0
    while(Number > 0):
        reminder = Number %10
        reverse = (reverse *10) + reminder
        Number = Number //10
    return reverse
"""
The driver code i am using python 3.9.1 
with also the commented out test case
"""
if __name__ == '__main__':
    n = int(input("Enter the value of N :"))
    x = int(input("Enter the value of X :"))
    y = int(input("Enter the value of Y :"))
   
    sumMultiples= find_sum(n, x, y)
    
    print(f"The Sum of multiples of {x} and {y} is {sumMultiples}")
    reverse = reverse_integer(sumMultiples)

    print(f"The reverse of the obtainde {sumMultiples} is {reverse}")

    """
    TEST CASE
    n = 10
    x = 3
    y = 5
   
    sumMultiples= find_sum(n, x, y)
    
    print(f"The Sum of multiples of {x} and {y} is {sumMultiples}")
    reverse = reverse_integer(sumMultiples)

    print(f"The reverse of the obtainde {sumMultiples} is {reverse}")


    """


