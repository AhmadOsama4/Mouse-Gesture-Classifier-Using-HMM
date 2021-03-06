import xml.etree.ElementTree as ET


#return a list of lists with points (X, Y)
def parseFile(filename, trainORtest):
	if trainORtest == 'train':
		filename = 'TrainingData/' + filename
	else:
		filename = 'TestData/' + filename

	tree = ET.parse(filename)
	root = tree.getroot()
	X = []
	Y = []

	for sequence in root.iter('Sequence'):
		xpoints = []
		ypoints = []
		for point in sequence.iter('Point'):
			x = point.find('X').text
			y = point.find('Y').text
			xpoints.append(int(x))
			ypoints.append(int(y))

		X.append(xpoints)
		Y.append(ypoints)

	return X, Y
