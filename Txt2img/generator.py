from PIL import Image, ImageColor, ImageFont, ImageDraw, ImageFilter

class Generator:
	def __init__(self, font):
		try:
			self.set_font(font)
		except TypeError:
			raise

	def set_font(self, font):
		if isinstance(font, ImageFont.FreeTypeFont) :
			self.__font = font
		else :
			raise TypeError("font must be instance of ImageFont.FreeTypeFont")

	def generate(self, text, mode='RGB', color=(0, 0, 0, 0), bgcolor=(255, 255, 255, 255), transforms = None):
		textsize = self.__font.getsize(text)
		image = Image.new(mode, textsize, bgcolor)
		image_draw = ImageDraw.Draw(image)
		image_draw.text((0, 0), text, color, self.__font)

		if isinstance(transforms, list):
			for transform in transforms :
				image = transform.transform(image)

		return image