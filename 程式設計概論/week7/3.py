import os


def list_directory_contents(directory_path, extension=None):
    if not os.path.exists(directory_path):
        print(f"目錄 '{directory_path}' 不存在")
        return

    contents = os.listdir(directory_path)

    files = []
    directories = []
    filtered_files = []

    for item in contents:
        full_path = os.path.join(directory_path, item)
        if os.path.isfile(full_path):
            files.append(item)

            if extension and item.endswith(extension):
                filtered_files.append(item)
        elif os.path.isdir(full_path):
            directories.append(item)

    print("資料夾列表:")
    if directories:
        for dirname in directories:
            print(dirname)

    print("檔案列表:")
    if files:
        for filename in files:
            print(filename)

    if extension:
        print(f"副檔名{extension}的檔案:")
        if filtered_files:
            for filename in filtered_files:
                print(filename)
        else:
            print(f"(找不到{extension}的檔案)")


while True:
    directory = input("\n請輸入要列出的目錄路徑直接按 Enter結束")
    if not directory:
        break

    extension = input("請輸入要過濾的副檔名例如 .txt")

    if extension and not extension.startswith("."):
        extension = "." + extension

    list_directory_contents(directory, extension)
