import random

print("=================================")
print("COMMAND LINE CRASH COURSE")
print("=================================")


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



def game_commands():
    game_cmd = {'Q': 'quit', 'H': 'hint', 'M' : 'main menu' }
    for cmd_key in game_cmd:
            print(f" {cmd_key} for {game_cmd[cmd_key]} ")

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

def level_one():
    while True:

                snippets = list(PHARASES.keys())
                random.shuffle(snippets)

                for snippet in snippets:
                    phrase = PHARASES[snippet]

                    answer, question = convert(snippet, phrase)

                    print(question)

                    input("> ")
                    print(f"ANSWER: {answer}\n\n")
    

    

condition = True

while condition:

    print("Type 'C' to view game commands")


    command = input("> ")

    if command.lower() == "c":
        game_commands()


    elif command.lower() == 'm':

        print("======== MAIN MENU ==============")
        
        print("Choose 1 for the basic, choose 2 for intermediate, choose 3 for advance")

        chosen_level = input("> ")

        if chosen_level == "1":
            level_one()
            

        
        else:
            print("INVALID LEVEL")

    elif command.lower() == "q":

        print("Are you sure you want to exit")
        confirm = input(" 'y' for yes 'n' for no > ")
        if confirm.lower() == 'y':
            break

    else:

        print("INVALID COMMAND")

        
