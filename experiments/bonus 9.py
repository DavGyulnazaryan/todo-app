
password = input("Greq dzer passwordy: ")
patasxany_obshi = {}

if len(password) >= 8:
    patasxany_obshi.append(True)
else:
    patasxany_obshi.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True


patasxany_obshi.append(digit)

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

patasxany_obshi.append(uppercase)

print(patasxany_obshi)

if all(patasxany_obshi) == True
    print("Lavna yngers")
else:
    print("yngers uzumes mihatel porc")


