filenames = ["1. Rax data.txt","2. Reports.txt","3. Presentations.txt"]

for filename in filenames:
    filename = filename.replace(".","-",1)
    print(filename)