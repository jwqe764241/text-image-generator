from datetime import datetime
from PIL import Image, ImageColor, ImageFont, ImageDraw, ImageFilter

from generator import TextImageGenerator
from transform import Rotate, Padding
from character import get_actually_used_hangul, get_english_alphabet

texts = ["아야어여오요우유으이가나다라마",
		"안녕하세요 저는 김기준입니다.",
		"테스트",
		"ㄴ미ㅏ엄니엄니ㅏ;어민어;민"]
path = "C:\\Users\\jwqe764241\\Desktop\\images"

generator = TextImageGenerator(ImageFont.truetype(font="H2GTRE.TTF", size=30))

actually_used_hangul = get_actually_used_hangul()
english_alphabet = get_english_alphabet()

for i in range(len(texts)):
	image = generator.generate(texts[i], 'RGB', (0, 0, 0), (255, 255, 255),
	[
		Rotate(45, resample=Image.BILINEAR, expand=True, fillcolor=(255, 255, 255)),
		Padding(100, 10, 100, 10)
	])
	dt = datetime.now()
	image.save(path + "\\" + dt.strftime("%Y.%m.%d %H.%M.%S.%f") + ".jpg", quality=100)

"""
for i in range(len(english_alphabet)):
#for i in range(1):
	image = generator.generate(english_alphabet[i], 'RGB', (0, 0, 0), (255, 255, 255),
	[
		Rotate(45, resample=Image.BILINEAR, expand=True, fillcolor=(255, 255, 255)),
		Padding(10, 10, 10, 10)
	])
	if i < 26 :
		image.save(path + "\\" + english_alphabet[i] + "_upper.jpg", quality=100)
	else :
		image.save(path + "\\" + english_alphabet[i] + "_lower.jpg", quality=100)
"""

"""
for i in range(len(actually_used_hangul)):
	image = generator.generate(actually_used_hangul[i], 'RGB', (0, 0, 0), (255, 255, 255),
	[
		Rotate(45, resample=Image.BILINEAR, expand=True, fillcolor=(255, 255, 255)),
		Padding(10, 10, 10, 10)
	])
	image.save(path + "\\" + actually_used_hangul[i] + ".jpg", quality=100)
"""