"""
Goal: Create code to allow a user to create a shopping list
Minimum requirements:
  * User can enter items which will be stored in the shopping list
  * User can exit item entry mode, which will cause the program to print the contents of the list
Stretch goals:
  * User can delete an item from the list
  * A command user can enter at any time to display the contents of the list

Advice:
  * You want to continue doing this for an unknown number of repetitions - what sort of loop would you use?
  * Remember that break will take you out of a loop, so you could say that if some string were entered - for instance 'exit' - you would do something and exit the loop
  * You're probably going to want to use input() and shopping_list.append()
  * Remember to do this one step at a time.
    * Make sure you can add a single item before you try to loop it.
    * Make sure the loop is working before you worry about how to do more advanced things

There is no automated checking on this one
"""

shopping_list = []

print('type "exit" at any time to finish shopping list')
print('press enter at any time to see your shopping list')

while True:
    user_input = input("What would you like to add to your shopping list?").lower()
    #print('input={}'.format(user_input))
    if user_input == '':
        print(shopping_list)
    elif user_input == 'exit':
        break
    else:
        shopping_list.append(user_input)



user_input2 = input(("Would you like to remove anything from your shopping list? Pick yes or no.").lower())

if user_input2 == "yes":
    while True:
        user_input3 = input("What would you like to remove from your shopping list?").lower()
        if user_input3 == "":
            print(shopping_list)
        elif user_input3 == "exit":
            break
        elif user_input3 not in shopping_list:
            print("That is not in your shopping list!")
        else:
            shopping_list.remove(user_input3)
elif user_input2 == "no":
    user_input4=input(("Are you finished with your shopping list? Pick yes or no.").lower())
    if user_input4 == "yes":
        print()
    elif user_input4 == "no":
        user_input5=input(("Would you like to add or remove items from your shopping list?").lower())
        if user_input5 == "add":
            while True:
                user_input6 = input("What would you like to add to your shopping list?").lower()
                if user_input6 == "":
                    print(shopping_list)
                elif user_input6 == 'exit':
                    break
                else:
                    shopping_list.append(user_input6)
        elif user_input5 == "remove":
            while True:
                user_input7 = input("What would you like to remove from your shopping list?").lower()
                if user_input7 == "":
                    print(shopping_list)
                elif user_input7 == "exit":
                    break
                elif user_input7 not in shopping_list:
                    print("That is not in your shopping list!")
                else:
                    shopping_list.remove(user_input7)
    elif user_input4 == "":
        print()
elif user_input2 == "":
    print()

print(shopping_list)










