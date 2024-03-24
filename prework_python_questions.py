# #question 1
def hello_username(user_name):
    """Display a simple greating to user"""
   
    print("hello_"+user_name.upper()+ "!")

hello_username('username')

# #Question 2
def first_odds():
    
    current_number = 0
    while current_number < 100:
        current_number += 1

        if current_number % 2 == 0:
            continue

        print(current_number)

first_odds()
#Question 3
def max_num_in_list(a_list):
    """Display the max number in list"""

    list = (1,9,12,25,452,7,254)

    print(max(list))

max_num_in_list(list)

#Question 4
def is_leap_year(a_year):
    """Return if a given year is a leap year"""

    year = (2024)

    if year % 4 == 0:
        print(True)
    elif year % 100 != 0:
        print(False)
    elif year % 400 == 0:
        print(True)

is_leap_year(2024)

#Question 5
def is_consecutive(a_list):
    """Display whether list is consecutive"""

    arr = [1,4,5,6,7,8,9,11]
   
    for i in range(0, len(arr)-1):
        if arr[i]+1 == arr[i+1] or arr[i]-1 == arr[i+1]:
           output = "This list is consecutive" 
    else:
           output = "This list is NOT consecutive"
    print(output)
   
is_consecutive(list)

# This was was difficult because I could not figure out how to show the if statement of whether or not the interger is plus 1 or -1, making it consecutive to the previous or subsequent number.
#I found a few ways to do it but this way seemed to make the most since to me. I understand what arr (array of numbers and i for integer means) The output made since too, assigning the outputs pertaining to the if else statements then printing the right answer.

