users = {
	'aeinstein':{
		'first': 'albert',
		'last': 'einstein',
		'location': 'pricenton',
		'favorite_food': 'atum',
	},

	'mcurie':{
		'first': 'marie',
		'last': 'curie',
		'location':'paris',
		'favorite_food': 'pizza',
	},
}

for username,user_info in users.items():
	print('Username: ' + username)
	full_name = user_info['first'] + ' ' + user_info['last']
	location = user_info['location']
	favorite_food = user_info['favorite_food']
	print('\tFull name: '+ full_name.title())
	print('\tLocation: '+ location.title())
	print('\tFavorite food: ' + favorite_food.title())
	
