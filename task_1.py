print("\nTo-Do-List")
list1 = []
while True: #loop for continuous working of code until mentioned to exit

    print("\n1.Display list \n2.Add to list \n3.Remove from list \n4.Clear list \n5.Exit")
    choice=input("Select an option(1-5) : ")
    if choice=='5':
        ext=input("Confirm exit (y/n) : ")
        if ext == 'y':
            print("Exiting To-Do-List, Goodbye 👋")
            break
        elif ext == 'n':
            continue
        else:
            print("\033[1;31mInvalid input\033[0m")
    elif choice=='1':
        if len(list1)==0:
            print("Your To-Do-List is empty, choose option '2' to add tasks to your To-Do-List")
        else:
            max_length = max(len(item) for item in list1) #getting max length of element in list to make border
            border = "_" * (max_length + 10)
            print(border)
            print(f"| {'To-Do List'.center(max_length + 6)} |")
            print(border)
            print(f"|index| {'Task'.ljust(max_length)} |")
            print(border)
            for i in range(len(list1)):
                print(f"| {i+1:3} | {list1[i].ljust(max_length)} |\n{border} ")

    elif choice=='2':
        task=input("Enter task to add to list : ")
        if task: #checking if entered input is empty
            list1.append(task)
            print(f"'{task}' added to your To-Do List.")
        else:
            print("Empty input is not allowed. Try again.")

    elif choice=='3':
        if len(list1)==0:
            print("Your To-Do-List is empty, choose option '2' to add tasks to your To-Do-List")
        else:
            rem_option=input("How do you want to remove \n1.By value \n2.By index \nEnter an option(1/2) : ")
            if rem_option=='1':
                try:
                    rem_task=input("Enter the task to remove : ")
                    list1.remove(rem_task)
                    print(f"{rem_task} removed from your To-Do-List")
                except ValueError:
                    print("Enter a valid task")
            elif rem_option=='2':
                try: #try block for making sure only integers are read as index value to remove
                    index=int(input("Enter the index of the task to remove : "))
                    if index in range(len(list1)+1):
                        print(f"Task {list1[index-1]} from position {index} removed from your To-Do-List")
                        del list1[index-1] #index-1 because index of list starts with '0' but is displayed from '1' onwards for users
                    else:
                        print("\033[1;31mInvalid index\033[0m")
                except ValueError:
                    print("\033[1;31mInvalid input, please enter a valid number\033[0m")
            else:
                print("\033[1;31mInvalid input\033[0m")

    elif choice=='4':
        clear = input("Confirm clearing (y/n) : ")
        if clear == 'y':
            if len(list1)==0:
                print("Your To-Do-List is already empty, choose option '2' to add tasks to your To-Do-List")
            else:
                list1.clear()
                print("Your To-Do-List is cleared")
        elif clear=='n':
            continue
        else:
            print("\033[1;31mInvalid input\033[0m")

    else:
            print("\033[1;31mInvalid input\033[0m")
