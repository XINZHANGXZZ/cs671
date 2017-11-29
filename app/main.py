import generate

def get(filename):
	z = generate.load_all()
	output = generate.story(z, filename)
	return output
