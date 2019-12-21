list_of_office = {'1' : 'google_kazakstan.txt',
				'2' : 'google_uar.txt',
				'3' : 'google_kyrgyzstan.txt',
				'4' : 'google_san_francisco.txt',
				'5' : 'google_paris.txt',
				'6' : 'google_germany.txt',
				'7' : 'google_moscow.txt',
				'8' : 'google_sweden.txt' }

user = input("")
if user == "Hello":
	print(list_of_office)
	choice = int(input("Which office do you prefer: "))
else:
	print("Wrong input!")

input_text = input("This text will be in your choosen file: ")

if choice == 1:
	with open  ("google_kazakstan.txt", 'w') as file_object:
		file_object.write(input_text)

elif choice == 2:
	with open  ("google_uar.txt", 'w') as file_object:
		file_object.write(input_text)

elif choice == 3:
	with open  ("google_kyrgyzstan.txt", 'w') as file_object:
		file_object.write(input_text)

elif choice == 4:
	with open  ("google_san_francisco.txt", 'w') as file_object:
		file_object.write(input_text)

elif choice == 5:
	with open  ("google_paris.txt", 'w') as file_object:
		file_object.write(input_text)

elif choice == 6:
	with open  ("google_germany.txt", 'w') as file_object:
		file_object.write(input_text)

elif choice == 7:
	with open  ("google_moscow.txt", 'w') as file_object:
		file_object.write(input_text)

elif choice == 8:
	with open  ("google_sweden.txt", 'w') as file_object:
		file_object.write(input_text)
else:
	print("Wrong input!")