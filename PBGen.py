#Password Bank Generator
#Created by: b0y54m0k
#Python Version: 2.7

characters = "ABCDEFGHI" #Insert characters included in password (NEEDS USER MODIFICATION)
length = 6 #Length of the password (NEEDS USER MODIFICATION)

lenChar = len(characters) #To determine how many characters are included
totalPassword = lenChar ** length #Total password combinations

listChar = list(characters)

text_file = open("Password-Bank.txt", "w")

#startPassword = "PREFIX" + "" #Change PREFIX and to prefix of target password bank and uncomment (NEEDS USER MODIFICATION)
startPassword = "" #use this if no need of password prefix (NEEDS USER MODIFICATION)

password = startPassword

listPasswordNum = []

#Start initial Password
for i in range(0,length):
	listPasswordNum+=[0]
	print listPasswordNum

for column in range(length-2,-1,-1): #-1 is to reverse the count
	while listPasswordNum[column]<lenChar:
		for row in range(0,lenChar):
			listPasswordNum[column+1]=row
			for j in range(0,length):
				password+=characters[listPasswordNum[j]]
			print password
			text_file.write(password + "\n")
			password=startPassword
			
		listPasswordNum[column]+=1
