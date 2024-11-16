#Exemplu 1
name = 'Apetrei Laura'
age = 30

#Exemplu 2
rate = 1.68
value =int(500)
payment =rate*value

#Exemplu 3
rate = 1.68
value_day =100
value_night =50
payment =(rate*value_day)+(rate/2*value_night)

#Exemplu 4
rate = 1.68
value_day = 358
value_night = 103
#Payment for electricity for the current month
payment = rate * value_day + rate / 2 * value_night

#Exemplu 5
first_name ='Laura'
last_name ='Apetrei'

#Exemplu 6
first_name ='Laura'
last_name ='Apetrei'
full_name =first_name+' ' +last_name

#Exemplu 7
first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
message = f"Dear {first_name}, we inform you that you have purchased a ticket to travel to the island of Mauritius. Departure June 31 of this year. Have a passport at {full_name}. We are looking forward to seeing you!"
print(message)

#Exemplu 8 -Booleen
is_active =True
is_delete =False

#Exemplu 9
name = input("Your name? ")
email =input("Your email")
age =int(input("Your age"))
height =float(input("Your height"))
is_active =True

#Exemplu 10
is_next = None
num = int(input("Enter the number of points: "))
if num >=83:
    is_next=True
else:
    is_next=False

#Exemplu 11
work_experience = int(input("Enter your full work experience in years: "))
if 1 < work_experience <= 5:
    developer_type = "Middle"
elif work_experience <= 1:
    developer_type = "Junior"
else:
    developer_type = "Senior"

print("Developer level:", developer_type)
