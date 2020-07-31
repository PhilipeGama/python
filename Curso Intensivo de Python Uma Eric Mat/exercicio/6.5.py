print('Frases')
paises = {
		'brasil':'amazonas',
		'estados unidos': 'mississippi',
		'china':'yangtze',
		'volga':'rússia',
	}

for pais,rio in paises.items():
	print(' O ' + rio.title() + ' corre pelo ' + pais.title())

print('\nPaíses')
for pais in paises.keys():
	print(' '+pais.title())

print('\nRios')
for rio in paises.values():
	print(' '+rio.title())