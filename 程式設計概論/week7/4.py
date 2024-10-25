import os


def search_files(directory, keyword):
    found = False

    for root, dirs, files in os.walk(directory):
        for name in files + dirs:
            if keyword.lower() in name.lower():
                rel_path = os.path.relpath(os.path.join(root, name), directory)
                print(rel_path)
                found = True

    if not found:
        print("oh nonono")


current_directory = os.getcwd()

while True:
    keyword = input("search key word, q to quit: ")
    if keyword.lower() == "q":
        break

    search_files(current_directory, keyword)
