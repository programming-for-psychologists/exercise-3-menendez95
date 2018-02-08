
def generateTrials(blocks, masked, sides):
	for block in range(blocks):
		for side in sides:
			for mask in masked:
				trial =",".join([str(block), mask, side])
				print trial

masked = ['masked', 'masked', 'nonmasked']
sides = ['left', 'right']
blocks = 5

generateTrials(5, masked, sides)