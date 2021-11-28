import random


PHARASES_BASICS = {
    "pwd":
        "print the current working directory",
    "clear":
        "Clear the terminal or command line",
    "ls":
        "List all files and directory",
    "hostname":
        "Check your computer's network name",
    "exit":
        "Exit the shell",
    "cd ~":
        "naviagte to the root directory",
    "cd ..":
        "Navigate a directory updward, closer to the root directory",
    "cd %%%":
        "Navigate to the %%% directory(folder)",
    "mkdir %%%":
        "Make a new directory(folder) named %%% in the current folder",
    "rmdir %%%":
        "Remove(Delete) the folder named %%% ",
    "touch ***":
        "Create a *** in the current folder",
    "unlink ***":
        "Delete the *** file",
    "rm *** ***":
        "Remove the following files ***, *** from the current directory",
    "cat ***":
        "print the content of the *** file",
        
}


PROJECT_FILE_NAMES = open('file_names.txt', 'r')
FILE_NAMES = []
for name in PROJECT_FILE_NAMES:
    FILE_NAMES.append(name.strip())


FOLDER_NAMES_FILE= open('project_names.txt', 'r')
FOLDER_NAMES = []
for name in FOLDER_NAMES_FILE:
    FOLDER_NAMES.append(name.strip())


condition = True


def game_commands():
    game_cmd = {'Q': 'quit', 'H': 'hint', 'M' : 'main menu' }
    for cmd_key in game_cmd:
            print(f" {cmd_key} for {game_cmd[cmd_key]} ")


def convert(snippet, phrase):
    """ Generate random filenames, folder names and fill the blanks in the snippet. """

    folder_names = [ w.capitalize() for w in random.sample(FOLDER_NAMES, snippet.count("%%%")) ]
    file_names = random.sample(FILE_NAMES, snippet.count("***"))
    results = []

    for sentence in snippet, phrase:
        result = sentence[:]

        # folder names 
        for word in folder_names:
            result = result.replace("%%%", word, 1)

        # file names
        for word in file_names:
            result = result.replace("***", word, 1)

        results.append(result)
    
    return results


def play_basics():
    """ Logic for basic Commands. """
    while condition:

                snippets = list(PHARASES_BASICS.keys())
                random.shuffle(snippets)

                for snippet in snippets:
                    phrase = PHARASES_BASICS[snippet]

                    answer, question = convert(snippet, phrase)

                    print(question)

                    input("> ")
                    print(f"\tANSWER: {answer}\n\n")
    

    
# keep leaning until you hit CTRL-D, CTRL-C or EOFError
def main():
    """ Main loop that runs the game. """

    print("=================================")
    print("COMMAND LINE CRASH COURSE")
    print("=================================")


    while condition:

        print("Type 'C' to view game commands")

        command = input("> ")

        if command.lower() == "c":
            game_commands()


        elif command.lower() == 'm':

            print("========================== MAIN MENU ===================================")
            print("Choose 1 for the basic, choose 2 for intermediate, choose 3 for advance")

            chosen_level = input("> ")

            if chosen_level == "1":
                play_basics()

            
            else:
                print("INVALID LEVEL")

        elif command.lower() == "q":

            print("Are you sure you want to exit")
            confirm = input(" 'y' for yes 'n' for no > ")
            if confirm.lower() == 'y':
                break

        else:

            print("INVALID COMMAND")



if __name__ == '__main__':
    main()