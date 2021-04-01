class Menu:  # Para simplificar los menus!
	def __init__(self, opciones, opcion = '0'):
		self.opciones = opciones  # string[]
		self.opcion = opcion
		self.print()

	def print(self):
		print('  E̲s̲c̲o̲ja̲ o̲pc̲i̲ó̲n̲:')
		for opcion in range(len(self.opciones)):
			print(f'[{opcion + 1}] {self.opciones[opcion]}')

		self.opcion = input('===> ')
