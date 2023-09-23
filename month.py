month = input("Enter the month please: ")
months = {
        "1":"january",
        "2":"febrary",
        "3":"march"
}
oupput = ""
for i in month:
    oupput += months.get(i, "!") + " "
print(oupput)