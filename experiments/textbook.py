def convert_to_percentage(value, total):
    percent = (value / total) * 100
    percent = round(percent, 1)
    return f"{percent}%"

print(convert_to_percentage(22.9, 50))









