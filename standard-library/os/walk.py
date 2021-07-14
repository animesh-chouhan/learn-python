import os


def get_filepaths(directory):
    file_paths = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths


print(get_filepaths("/home/animesh/Test"))
