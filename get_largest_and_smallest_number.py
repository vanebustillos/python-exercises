
#Function to get the largest value of a list of numbers
def get_largest_number(list):
    #Set initial value
    largest = -1
    #Iterate the list
    for i in list:
        #If the item is larger than the current number stored in the variable, then, the new largest value is the current item
        if i > largest:
            largest = i
    print('The largest number is:',largest)

#Function to get the smallest value of a list of numbers
def get_smallest_number(list):
    #Set initial value
    smallest = None
    #Iterate the list
    for i in list:
        #If the item is smaller than the current number stored in the variable, then, the new smallest value is the current item
        if smallest is None or i < smallest:
            smallest = i
    print('The smallest number is:',smallest)

list = [2,34,56,87,12,99,20]

#Invoke the functions
get_largest_number(list)
get_smallest_number(list)