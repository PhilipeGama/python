pessoa_0 = {'first_name' : 'john',
			 'last_name' : 'doe',
			 'age' : 25,
			 'city': 'atlanta', 
			  }

pessoa_1 = {'first_name' : 'maria',
			 'last_name' : 'joaquina',
			 'age' : 30,
			 'city': 'rio de janeiro', 
			  }

pessoa_2 = {'first_name' : 'pedro',
			 'last_name' : 'rizo',
			 'age' : 20,
			 'city': 'manaus', 
			  }

peoples = [pessoa_0,pessoa_1,pessoa_2]

for pessoa in peoples:
	print('Name: '+pessoa['first_name'].title()+' '+pessoa['last_name'].title())
	print('Age: '+ str(pessoa['age']))
	print('City: '+pessoa['city'].title())
	print('\n')