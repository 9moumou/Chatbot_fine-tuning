##include
import re

##define

main_path = "C:/Users/themo/Desktop/Mieux/AI/Chatbot_Theo/" #the path to the actual .py file

group_time_pattern = "../../...., ..:.. - " #the pattern to detect for suppressing time info for groups

personal_time_pattern = "\[../../.... ..:..:..] " #the pattern to detect for suppressing time info for personal chats

Theo_aliases = ["theo", "théo"] #the different ways to refer to Theo in the chat (only the fist part is needed for detection) : eg. theo instead of theo chen
Others_aliases = ["Youssef","matheo","Simon"] #the different ways to refer to others chat members (only the fist part is needed for detection)

##func
def nb_line(file_name, path=main_path):
    file_text = open(path+file_name, "r", encoding="utf-8")
    lines = file_text.readlines()
    print("there is", len(lines), "lines")
    return(len(lines))

def pop_replace_chat(file_name, pattern, replacement="", path=main_path, new_file_name=None):
    """
    This function opens an exported WhatsApp chat and writes it in a new text file after replacing a pattern. If no replacement is provided, the pattern is removed.
    Arguments:
        file_name -- name of the text file to be opened
        path -- path to the directory containing the text file (default is main_path)
    Returns: nothing
    Comments: The function uses regular expressions to find and replace the specified pattern in each line of the chat.
    """
    file_text = open(path+file_name, "r", encoding="utf-8")
    if new_file_name is not None:
        new_file = open(path+new_file_name, "w", encoding="utf-8")
    else:
        new_file = open(path+"replaced_"+file_name, "w", encoding="utf-8")

    lines = file_text.readlines()
    for line in lines:
        out = re.sub(pattern, replacement, line)
        new_file.write(out)
    file_text.close()
    new_file.close()
    return

def class_messages(file_name, path=main_path):
    """
    This function opens an exported WhatsApp chat and returns a list of messages with personal info removed.
    Messages are lists of [dest, content]. dest is either the target -> 1 (here Theo) or another person -> 0.
    Arguments:
        file_name -- name of the text file to be opened
        path -- path to the directory containing the text file (default is main_path)
    comments: this function will go wrong if the first line is not a message (eg. group created, changed name etc.)
    """
    messages = []
    alliases = Theo_aliases + Others_aliases
    n = len(Theo_aliases)
    bol = False

    file_text = open(path+file_name, "r", encoding="utf-8")
    lines = file_text.readlines()
    
    for line in lines:
        if (":" in line):
            for k in range(len(alliases)):
                recherche = re.search("^"+alliases[k]+".*: ", line, re.IGNORECASE)
                if (recherche!=None):
                    messages.append([k<n, line[recherche.end():]])
                    bol = True
                    break
            if not bol:
                messages[-1][1] += line
            bol = False
        else:
            messages[-1][1] += line
    file_text.close()
    return messages
##exec

pop_replace_chat("WhatsApp_Chat_Theo-Youssef.txt", pattern=personal_time_pattern, new_file_name="tempo.txt")

MESS = class_messages("tempo.txt")
print(MESS)
#nb_line("WhatsApp_Chat_Theo-Youssef.txt")


