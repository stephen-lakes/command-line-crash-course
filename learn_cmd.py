import random

print("=================================")
print("COMMAND LINE CRASH COUSRSE")
print("=================================")

game_commands = {'Q': 'quit', 'H': 'hint', 'M' : 'main menu' }

PHARASES = {
    "mkdir %%%":
        "Make a folder named %%% in the current folder",
    "rmdir %%%":
        "Remove/Delete the folder named %%% ",
    "cd %%%":
        "Navigate to the %%% directory",
    "touch ***":
        "Create a file named ***in the current folder",
    "rm *** ***":
        "Remove the following files ***, *** from the current directory",
    "unlink ***":
        "Delete the *** file",
    "clear":
        "Clear the terminal or command line",
    "ls":
        "List all the files in the current directory",
    "cd ..":
        "Navigate a directory updward, closer to the root directory",
    
    
}

WORDS_FILE = open('words.txt', 'r')
WORDS = []

for word in WORDS_FILE:
    #WORDS.append(str(word.strip(), encoding="utf-8"))
    WORDS.append(word)

def convert(snippet, phrase):

    folder_names = [ w.capitalize() for w in random.sample(WORDS, snippet.count("%%%")) ]
    file_names = random.sample(WORDS, snippet.count("***"))
    results = []

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake folder names 
        for word in folder_names:
            result = result.replace("%%%", word, 1)

        # fake file names
        for word in file_names:
            result = result.replace("***", word, 1)

        results.append(result)
    
    return results


condition = True

while condition:

    print("Type 'C' to view game commands")


    command = input("> ")

    if command.lower() == "c":

        for command_key in game_commands:
            print(f" {command_key} for {game_commands[command_key]} ")

    elif command.lower() == 'm':

        print("======== MAIN MENU ==============")
        
        print("Choose 1 for the basic, choose 2 for intermediat, choose 3 for advance")

        level = input("> ")

        if level == "1":
            while True:

                snippets = list(PHARASES.keys())
                random.shuffle(snippets)

                for snippet in snippets:
                    phrase = PHARASES[snippet]

                    answer, question = convert(snippet, phrase)

                    print(question)

                    input("> ")
                    print(f"ANSWER: {answer}\n\n")



                



        
        else:
            print("INVALID COMMAND")

    elif command.lower() == "q":

        print("Are you sure you want to exit")
        confirm = input(" 'y' for yes 'n' for no > ")
        if confirm.lower() == 'y':
            break

    else:

        print("INVALID COMMAND")

        
