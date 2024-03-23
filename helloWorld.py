import datetime
year = int(input('Please enter your year of birth:'))
current_year = datetime.datetime.now().year
age = current_year - year
print("You are {} years old.".format(age))