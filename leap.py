#Program to check whether a given year is leap year or not.
def leap(a):
    if (a%4==0 and a%400==0):
        return (a, 'is a leap year')
    elif (a%100!=0 and a%4==0):
        return (a, 'is a leap year')
    else:
        return (a, 'is not a leap year')
