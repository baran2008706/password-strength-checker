password = input("enter your password: ")

score = 0

#we use len() so that we can check the length of the password
if len(password) >= 8:
    score += 1

#we use isupper() so that we can check if there are any upper-case letters in the password or not
if any(char.isupper() for char in password):
    score += 1
#using islower() to check if there are any lower-case letters in the password
if any(char.islower() for char in password):
    score += 1
#isdigit() checks whether all characters in the password are digits
if any(char.isdigit() for char in password):
    score += 1
#isalnum() checks whether all  characters in a string are letters or numbers
if any(char.isalnum() for char in password):
    score += 1
if score <= 2:
    print("weak password")
if 2 < score <= 4:
    print("medium password")
else:
    print("strong password")
