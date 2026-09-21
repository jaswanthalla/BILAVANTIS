def directory_size(files):
    if not files:
        return 0
    return files[0] + directory_size(files[1:])


print(directory_size([100, 200, 300])) 
