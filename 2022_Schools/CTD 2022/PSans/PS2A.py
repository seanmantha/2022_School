
def calculate_bmi( weight, height): #the commands in the bracket are called parameters
    height = height / 100 #converting height from cm to m
    bmi = weight / (height ** 2)
    bmi_round = round (bmi , 1)
    return bmi_round
print ( calculate_bmi (2.5, 50)) #the commands in the bracket are called arguments



