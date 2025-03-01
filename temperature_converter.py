conversiondirection = input("what is the conversion direction ?  ")
temperature =  int(input("what is the temperature ?  "))
if conversiondirection == "Celsius to Fahrenheit":
    temp = (temperature * 9/5) + 32 
    print ("the covert is  " + str(temp))
elif conversiondirection == "Fahrenheit to Celsius":
    temp = (temperature - 32) * 5/9
    print ("the covert is  " + str(temp)) 

    