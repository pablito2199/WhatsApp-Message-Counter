import os
import re

users = {}
numberLines = 0
chatName = ""


def readFile():
    global chatName, numberLines, users

    directory = input("Enter the directory for your chat file: ")
    chatName = str(os.path.split(directory)[1])
    chatName = chatName.replace("Chat de WhatsApp con ", "")
    file = open(directory, "r", encoding="utf8")
    lines = file.readlines()

    for line in lines:
        line = re.sub("[0-9]{1,2}/[0-9]{1,2}/[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2} - ", "", line)
        user = line[:line.find(": ")]
        if user in users:
            users[user] += 1
        numberLines += 1


if __name__ == "__main__":
    numberUsers = int(input("Enter the number of users: "))
    print("\n")
    for i in range(numberUsers):
        name = input(f"Enter the name of the user {i + 1}: ")
        users[name] = 0

    readFile()
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"\n##################################\n{chatName}\n##################################")
    for user in users:
        print(f"# {user}: {users[user]}")
    print(f"##################################\n# Total messages in the chat: {str(numberLines)}")
