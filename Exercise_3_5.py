import random

def generateTrials(blocks, masked, sides):
	for block in range(blocks):
		trials= []
		i = 0
		while i < 2:
			for side in sides:
				for mask in masked:
					trial =",".join([str(block), mask, side])
					trials.append(trial)
			i = i + 1
		random.shuffle(trials)
		for trial in trials:
			print trial
	return trials


masked = ['masked', 'masked', 'nonmasked']
sides = ['left', 'right']
blocks = 5

trials = generateTrials(blocks, masked, sides)
