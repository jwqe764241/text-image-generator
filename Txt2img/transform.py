from PIL import Image, ImageColor, ImageFont, ImageDraw, ImageFilter
import numpy as np
import cv2

#interface for transform text image
class Transform:
	def transform(self, image):
		pass

#rotate image
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

#add padding at image
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

#add gaussian noise at image
class GaussianNoise(Transform):
	def __init__(self, mean, std):
		self.__mean = mean
		self.__std = std

	def transform(self, image):
		cv_image = np.asarray(image)

		noise =  np.random.normal(self.__mean, self.__std, size=cv_image.shape)
		noise = noise.astype(cv_image.dtype)

		cv_image = cv_image + noise

		return Image.fromarray(cv_image)
