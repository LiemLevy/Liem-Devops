listforuser = input("Enter a list of numbers separated by commas: ")
listwork = listforuser.split(",")
bignumber = None
smallnumber = None
sum = 0
for number in listwork:
    number = int(number) 
    sum = sum + number
    if smallnumber is None:
        smallnumber = number
    if bignumber is None:
        bignumber = number
    if number < smallnumber:
        smallnumber = number
    if number > bignumber:
        bignumber = number
revertlist = []
for number in reversed(listwork):
    revertlist.append (number)



avg = sum / len(listwork)
print(sum)
print (avg)
print(f"The largest number is {bignumber}!")
print(f"The smallest number is {smallnumber}!")
print(revertlist)
