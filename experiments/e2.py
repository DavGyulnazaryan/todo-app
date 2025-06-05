list_of_countries = ["Germany", "Italy", "Japan"]
folder_path = r"C:\Users\Davit Gyulnazaryan\PycharmProjects\todo_app"

for countries in list_of_countries:
    file_path = f"{folder_path}\\{countries}.txt"
    file = open(file_path, "w")
    file.write(countries)
    file.close