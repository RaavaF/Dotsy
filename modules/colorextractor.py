from colorthief import ColorThief

path = 'dot/dot.png'

def GetRGB():
	Image = ColorThief(path)
	ImageRGB = (Image.get_color(quality=1))
	return ImageRGB
	
def GetHex():
	Image = ColorThief(path)
	ImageRGB = (Image.get_color(quality=1))
	ImageHex = (f"{ImageRGB[0]:02x}{ImageRGB[1]:02x}{ImageRGB[2]:02x}")
	return ImageHex

def GetHSV():

	Image = ColorThief(path)
	
	ImageRGB = (Image.get_color(quality=1))

	red, green, blue = ImageRGB[0] / 225, ImageRGB[1] / 225, ImageRGB[2] / 225

	cmax = max(red, green, blue) 
	cmin = min(red, green, blue)
	difference = cmax-cmin

	if cmax == cmin:
		hue = 0
	
	elif cmax == red:
		hue = (60 * ((green - blue) / difference) + 360) % 360

	elif cmax == green:
		hue = (60 * ((blue - red) / difference) + 120) % 360

	elif cmax == blue:
		hue = (60 * ((red - green) / difference) + 240) % 360

	if cmax == 0:
		saturation = 0
	else:
		saturation = (difference / cmax) * 100

	value = cmax * 100
	
	hue = round(hue)
	saturation = round(saturation)
	value = round(value)
	
	return hue, saturation, value

