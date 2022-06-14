class Matrix():

	def __init__(self, inp_matrix):
		total_row = len(inp_matrix)
		self.inp_matrix = inp_matrix
		if total_row > 0:
			row_1 = inp_matrix[0]
		else:
			raise #matrix is Empty
		for row in inp_matrix:
			if len(row) != len(row_1):
				raise #length of matrix rows are diferent 
		for el in row:
			if isinstance(el, int):
				pass
			else:
				raise #elemets of matrix are not int
		


	def __str__(self):
		result = ""
		for row in self.inp_matrix:
			for el in row:
				result += str(f'{el}\t')
			result += '\n'
		return result

	def __add__()



mat_1 = Matrix([[3, 5, 32], [2, 4, 6],[-1, 64, -8]])

x = str(mat_1)
print(x)




		


"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных 
в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
 класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки 
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д."""