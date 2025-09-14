# Tasks
# 1.
my_int_one = 1
my_int_two = 5
my_int_three = my_int_one + my_int_two
print(my_int_three)

# 2.
my_alt_int_one = int(input("enter first integer: "))
my_alt_int_two = int(input("enter second integer: "))
my_alt_int_three = my_alt_int_one + my_alt_int_two
print(my_alt_int_three)

# 3.
def fizzbuzz_failure_message(i):
    i_str = str(i)
    
    if i % 3 == 0 and i % 5 == 0:
        return i_str + " should be fizzbuzz!"
    elif i % 3 == 0:
        return i_str + " should be fizz!"
    elif i % 5 == 0:
        return i_str + " should be buzz!"
    else:
        return "It should have been " + i_str + "!"

def fizzbuzz_input_check(i, user_input):
    return i % 3 == 0 and i % 5 == 0 and user_input == "fizzbuzz" or i % 3 == 0 and i % 5 != 0 and user_input == "fizz" or i % 3 != 0 and i % 5 == 0 and user_input == "buzz" or i % 3 != 0 and i % 5 != 0 and int(user_input) == i

def fizzbuzz_main():
    print("-=-=-=-=-=-=-=-=-")
    print("-=-=-=-=-=-=-=-=-")
    print("Welcome to FizzBuzz")
    print("3..2..1..GO!")

    for i in range(1, 17):
        if i == 16:
            print("Congratulations! You Won FizzBuzz!")
            break

        elif i >= 1 and i < 16:
            user_input = input("The next item is: ")

            if fizzbuzz_input_check(i, user_input):
                continue

            else:
                print("Bzzt! Game Over! " + fizzbuzz_failure_message(i))
                break

fizzbuzz_main()

# 4.
def shopping_list_output(my_shopping_list):
    output_message = "List contains: "
            
    for i in range(0, len(my_shopping_list)):
        space = ""
        
        if i > 0 and space == "":
            space = ", "
            
        output_message = output_message + space + my_shopping_list[i]
        
    print(output_message)

def shopping_list_add_items(my_shopping_list):
    should_add_item = ""
    inner_shopping_list = my_shopping_list

    while should_add_item != "n":
        should_add_item = input("Do you want to add another item? (y/n): ")

        if should_add_item == "y":
            new_item = input("Please enter the new item: ")
            inner_shopping_list.append(new_item)
            continue
        
        elif should_add_item == "n":
            break
        
        else:
            print("you entered an incorrect option, please try again!")
            continue
    
    return inner_shopping_list
            
def shopping_list_main():
    my_shopping_list = []
    have_all_ingredients = ""

    print("-=-=-=-=-=-=-=-=-")
    print("-=-=-=-=-=-=-=-=-")
    print("Welcome to the shopping list function!")

    while have_all_ingredients != "y":
        have_all_ingredients = input("Do you have all the items in your list? (y/n): ")

        if have_all_ingredients == "y":
            shopping_list_output(my_shopping_list)
            break
            
        elif have_all_ingredients == "n":
            my_shopping_list = shopping_list_add_items(my_shopping_list)    
            continue
        
        else:
            print("you entered an incorrect option, please try again!")
            continue

shopping_list_main()

# 5.
def shopping_list_remove_items(my_shopping_list):
    should_remove_item = ""
    inner_shopping_list = my_shopping_list

    while should_remove_item != "n":
        should_remove_item = input("Do you want to remove an item? (y/n): ")

        if should_remove_item == "y":
            item = input("Please enter the item to remove: ")
            try:
                inner_shopping_list.remove(item)
            except:
                print("This item is not in your list!")

            continue
        
        elif should_remove_item == "n":
            break
        
        else:
            print("you entered an incorrect option, please try again!")
            continue
    
    return inner_shopping_list

def shopping_list_alt_main():
    my_shopping_list = []
    have_all_ingredients = ""

    print("-=-=-=-=-=-=-=-=-")
    print("-=-=-=-=-=-=-=-=-")
    print("Welcome to the shopping list function (alternate)!")

    while have_all_ingredients != "y":
        have_all_ingredients = input("Do you have all the items in your list? (y/n): ")

        if have_all_ingredients == "y":
            shopping_list_output(my_shopping_list)
            my_shopping_list = shopping_list_remove_items(my_shopping_list) 
            shopping_list_output(my_shopping_list)
            break
            
        elif have_all_ingredients == "n":
            my_shopping_list = shopping_list_add_items(my_shopping_list)    
            continue
        
        else:
            print("you entered an incorrect option, please try again!")
            continue

shopping_list_alt_main()
