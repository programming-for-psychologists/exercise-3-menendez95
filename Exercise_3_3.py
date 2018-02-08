import random

def generateTrials(blocks, masked, sides):
	trials= []
	for block in range(blocks):
		for side in sides:
			for mask in masked:
				trial =",".join([str(block), mask, side])
				trials.append(trial)
	random.shuffle(trials)
	for trial in trials:
		print trial

masked = ['masked', 'masked', 'nonmasked']
sides = ['left', 'right']
blocks = 5

trials = generateTrials(blocks, masked, sides)
