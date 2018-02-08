def repetition(letters, numberBeforeSwitch, numRepetitions):
	for rep in range(numRepetitions):
		for letter in letters:
			for num in range(numberBeforeSwitch):
				print letter 

repetition(['a', 'b', 'c'], 2, 3)
