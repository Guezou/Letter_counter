
class counter:

	word = input(str("Dites n'importe quoi, allez-y, lancez-vous ! ------> "))	
	
	def vowels_counter():
		vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y", "é", "è", "à", "ô"]
		space = " "
		v_counter = 0
		

		for letter in counter.word:
			if letter in vowels:
				v_counter += 1

			elif space in letter:
				v_counter + 0
			
		if space in counter.word:
			print("il y a {} voyelles dans votre phrase ".format(v_counter))
		else:
			print("il y a {} voyelles dans votre mot ".format(v_counter, counter.word))
	

		
	def consonant_counter():
    
    
		consonant = ["b","c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s","t", "v", "w", "x", "z","B","C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S","T", "V", "W", "X", "Z"]
		space = " "
		c_counter = 0
		

		for letter in counter.word:
			if letter in consonant:
				c_counter += 1
			elif space in letter:
				c_counter + 0
			
		if space in counter.word:
			print("il y a {} consonnes dans votre phrase {}".format(c_counter))
		else:
			print("il y a {} consonnes dans votre mot ".format(c_counter))	
	
	

