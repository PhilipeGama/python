pet_0 = {'tipo' : 'buldogue',
		'nome' : 'totó',
		'dono' : 'joao',
		}

pet_1 = {'tipo' : 'poodle',
		'nome' : 'lucio',
		'dono' : 'pedro',
		}

pet_2 = {'tipo' : 'beagle',
		'nome' : 'belinha',
		'dono' : 'ruan',
		}

pet_3 = {'tipo' : 'chihuahua',
		'nome' : 'tino',
		'dono' : 'jackson',
		}

pets = [pet_0,pet_1,pet_2,pet_3]

for pet in pets:
	
	print('Nome: '+pet['nome'].title())
	print('Tipo: '+pet['tipo'].title())
	print('Dono: '+pet['dono'].title())
	print('')