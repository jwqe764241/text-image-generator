from PIL import Image, ImageColor, ImageFont, ImageDraw, ImageFilter

#이미지 변형 인터페이스
class Transform:
	def transform(self, image):
		pass

#이미지 회전
class Rotate(Transform):
	def __init__(self, angle, resample=Image.NEAREST, expand=0, center=None, translate=None, fillcolor=None):
		self.__angle = angle
		self.__resample = resample
		self.__expand = expand
		self.__center = center
		self.__translate = translate
		self.__fillcolor = fillcolor

	def transform(self, image):
		return image.rotate(self.__angle, resample=self.__resample, expand=self.__expand, center=self.__center, translate=self.__translate, fillcolor=self.__fillcolor)

#이미지 여백
class Padding(Transform):
	def __init__(self, top=0, bottom=0, left=0, right=0):
		self.__top = top
		self.__bottom = bottom
		self.__left = left
		self.__right = right
	
	def transform(self, image, fillcolor=(255, 255, 255, 255)):
		width, height = image.size
		new_width = width + self.__left + self.__right
		new_height = height + self.__top + self.__bottom
		new_image = Image.new(image.mode, (new_width, new_height), fillcolor)
		new_image.paste(image, (self.__left, self.__top))
		return new_image