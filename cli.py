import datetime as dt
import os


# folder_path = "/Users/charanjeetsingh/Documents/Journal_App/Journal_App/.venv/JournalTexts"
current_datetime = dt.date.strftime(dt.datetime.today(), "%d-%m-%Y")
print(current_datetime)

while True:
    user_action = input("What action do you want to perform? new/open/edit/delete/exit: ").strip().lower()

    if user_action == "new":
        # ask the user to input the text
        user_text = input("Hi, Please enter today's journal below:\n")
        save_action = input("Would you like to save this? y/n:\n")
        if save_action == 'y':
            with open(f"{current_datetime}.txt", 'w') as file:
                file.write(user_text)
            print("File Saved!")
            continue
        elif user_action == 'n':
            break
            # return to the start of the program.

    elif user_action == "open":
        # give the list of files as option which one to open
        # nameof_files = pl.Path.
        # directory = '/Users/charanjeetsingh/Documents/Journal_App/Journal_App/.venv/'
        text_files = [f for f in os.listdir() if f.endswith('.txt')]
        for files in text_files:
            print(files)
        file_name = input("enter filename: ")
        with open(f"{file_name}", "r") as file:
            print(file.read())

    elif user_action == "edit":
        # show the list of files
        text_files = [f for f in os.listdir() if f.endswith('.txt')]
        for files in text_files:
            print(files)

        # take the input of file name
        file_name = input("Please enter the file name to edit: ")

        # edit the file
        with open(file_name, "r") as file:
            content = file.readlines()
            print(content)

        # Take the input from user
        additional_text = input("Enter more text below: ")

        # append the file
        content.append('\n' + additional_text)
        print(content)
        # Save the file

        with open(file_name, "w") as file:
            file.writelines(content)
            print("Edit complete!")

    elif user_action == "delete":
        # give a list of files
        text_files = [f for f in os.listdir() if f.endswith('.txt')]
        for files in text_files:
            print(files)

        # Ask the user to select the file which he wants to delete
        file_name = input("Please enter the file name to delete: ")
        os.remove(file_name)
        print(file_name, " deleted!")

    elif user_action == "exit":
        exit()

    else:
        print("You have entered a wrong value. Please try again")
        continue
