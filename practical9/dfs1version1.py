import os, shutil

print(os.getcwd())
os.chdir("C:\\Users\\user\\PycharmProjects\\CP1404\\practical9\\FilesToSort")

format_list = []

for file in os.listdir(os.getcwd()):
    if os.path.isfile(file):
        file_list = file.split(".")
        if file_list[1] not in format_list:
            format_list.append(file_list[1])
            new_dir = os.path.join(os.getcwd(), file_list[1])
            os.mkdir(new_dir)
            from_file = os.path.join(os.getcwd(), file)
            to_file = os.path.join(new_dir, file)
            shutil.copyfile(from_file, to_file)
        elif file_list[1] in format_list:
            new_dir = os.path.join(os.getcwd(), file_list[1])
            from_file = os.path.join(os.getcwd(), file)
            to_file = os.path.join(new_dir, file)
            shutil.copyfile(from_file, to_file)
