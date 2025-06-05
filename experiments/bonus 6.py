contents = ["esi arajin axper jan",
            "esi erkrord ynger jan",
            "esel errord mec axper"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)