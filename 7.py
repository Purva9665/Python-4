try:
    file= open("sample.txt","r")
    read1 = file.readline()
    read2 = file.readline()
    file.close()
    print("Reading file content: ")
    print(f"Line 1: {read1}")
    print(f"Line 2: {read2}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

