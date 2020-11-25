# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# JCarnes,11.21.2020,Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        # TODO: DONE!
        """Adds task and priority to a dictionary; dictionary is then added to the list

        :param task: (string) to be added to dictionary
        :param priority: (string) to be added to dictionary
        :param list_of_rows: (list) of dictionary rows with keys Task and Priority
        :return (list) of dictionary rows"""

        dictionary_row = {"Task": task, "Priority": priority}
        list_of_rows.append(dictionary_row)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        # TODO: Done!
        """This function removes a task from a list of dictionaries with a key of "Task"

        :param task: (string) task to be removed from list
        :param list_of_rows: (list) of dictionaries with tasks and priorities
        :return: (list) of dictionary rows, number_removed (int)
        """

        number_removed = 0  # Counter to keep track of how many rows are removed
        i = 0  # Index Counter
        while i < len(list_of_rows):
            if list_of_rows[i]['Task'].lower() == task.lower().strip():
                number_removed += 1
                list_of_rows.pop(i)
                # Row counter should not increase if a row was removed as remaining elements have shifted indexes
            else:
                i += 1
        return list_of_rows, number_removed, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        # TODO: Done!
        """This function writes a list to a text file

        :param file_name: (string) with name of file
        :param list_of_rows: (list) you want saved to file
        :return: (tuple) containing list of rows that was saved to file and 'Success'
        """
        file = open(file_name, 'w')
        for rows in list_of_rows:
            file.write(rows["Task"] + ',' + rows["Priority"] + "\n")
        file.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        # TODO: Done!
        """ Get new task and priority from user

        :return: task, priority
        """
        print("Please enter a task and priority")
        task = input("Task: ")
        priority = input("Priority: ")
        return task.strip(), priority.strip()

    @staticmethod
    def input_task_to_remove():
        # TODO: Not done - break this up!
        """Removing a task from the list

        :return task: (string) of task to be removed
        """
        print("Please enter a task to be removed")
        task = input("Task: ").strip()
        return task

    @staticmethod
    def print_num_of_tasks_removed(task, number_removed):
        """Prints message to the based on the number of tasks removed from to do list

        :param task: (string) task to be removed from list
        :param number_removed: (int) number of times the task was removed from to do list
        :return: nothing
        """
        if number_removed == 1:
            print("The task " + task + " was removed!")
        elif number_removed > 1:
            print(str(number_removed) + ' Rows for the task ' + task + ' were removed!')
        else:
            print("The task " + task + " was not found!")

# Main Body of Script  ------------------------------------------------------ #


# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # TODO: Done!
        strTask, strPriority = IO.input_new_task_and_priority()
        Processor.add_data_to_list(strTask, strPriority, lstTable)
        IO.input_press_to_continue()
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # TODO: Done!
        strTask = IO.input_task_to_remove()
        num_removed_int = Processor.remove_data_from_list(strTask, lstTable)
        IO.print_num_of_tasks_removed(strTask, num_removed_int[-2])
        IO.input_press_to_continue()
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # TODO: Done!
            Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue("Data saved to File!")
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            # TODO: Done!
            strStatus = Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus[-1])
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break   # and Exit
