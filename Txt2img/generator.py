from PIL import Image, ImageColor, ImageFont, ImageDraw, ImageFilter

#텍스트 이미지 생성기
class Generator:
	def __init__(self, font):
		try:
			self.set_font(font)
		except TypeError:
			raise
	
	#폰트 설정
	def set_font(self, font):
		if isinstance(font, ImageFont.FreeTypeFont) :
			self.__font = font
		else :
			raise TypeError("font must be instance of ImageFont.FreeTypeFont")

	#이미지 생성
	def generate(self, text, mode='RGB', color=(0, 0, 0, 0), bgcolor=(255, 255, 255, 255), transforms = None):
		textsize = self.__font.getsize(text)
		image = Image.new(mode, textsize, bgcolor)
		image_draw = ImageDraw.Draw(image)
		image_draw.text((0, 0), text, color, self.__font)

		#transform 존재시 기본 생성된 이미지를 리스트 순서대로 변형함
		if isinstance(transforms, list):
			for transform in transforms :
				image = transform.transform(image)

		return image