changingParam = ['Gender','Occupation','BMI Category']
changingValues = [['Male','Female'],['Software Engineer','Doctor','Sales Representative','Teacher', 'Nurse' , 'Engineer' ,'Accountant' ,'Scientist', 'Lawyer' ,'Salesperson', 'Manager'],['Overweight' ,'Normal' ,'Obese', 'Normal Weight']]

def generateProfile(data):
    Person_Profile = []
    for x in data:
        if x in changingParam:
            X_index = changingParam.index(x)
            newStrings = x.replace('_'," ") + '  :  ' + changingValues[X_index][int(data[x])]
        else:
            newStrings = x.replace('_'," ") + '  :  ' + data[x]
        Person_Profile.append(newStrings)
    return Person_Profile

def generateOutput(prediction):
    base = 'From the given profile our model has predicted : '
    choice = ['The person does not have any Sleeping Disorder','The person does have Sleep Apnea', 'The person does have Insomnia']
    
    return base + choice[prediction]