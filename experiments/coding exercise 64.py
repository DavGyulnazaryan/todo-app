new_member = input("Add a new member: ")

# Read existing members
file = open("members.txt", "r")
existing_members = file.readlines()
file.close()

# Add new member
existing_members.append(new_member + "\n")

# Write updated list back to file
file = open("members.txt", "w")
file.writelines(existing_members)
file.close()
