import random

def positive_message():

	happy = [
			"The world seem connected!",
			"Hope you'll smile today!",
			"Play Maiden and Spell!",
			"Play Guilty Gear Xrd & Strive!",
			"Play Street Fighter Third Strike!",
			"Play Cofee Talk!",
			"Fill your cup half full!",
			"I'm not much of a programmer, so thanks for dotting(?)",
			"!!!!!!!!!",
			"You look great you know!",
			"Shout-out to my monochromatic friend!",
			"Make sure you communicate in your relationships!",
			"Sometimes it's good to take a break!",
			"Rock & roll!",
			"Breakcore!",
			"Cheese!",
			"Made in Revolt!",
			"h!!!",
			"Make sure you get a good night's rest."
	]

	random.shuffle(happy)
	
	return happy[0]


def negative_message():

	sad = [

			"The world seems sullen.",
			"An off feeling emerges.",
			"The cup is half empty.",
			"AI will take over.",
			"Sometimes I fear showing you the color.",
			"Sometimes the scorpion can't help but to sting the frog.",
			"It can get annoying making these messages.",
			"It's okay to yell sometimes.",
			"My brain is becoming a 2D object",
			"I've ran out of ideas..."

	]
	
	random.shuffle(sad)

	return sad[0]

