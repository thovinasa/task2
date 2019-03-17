from PIL import ImageFont, ImageDraw, Image
import at
def txt_to_img(txt,out):
	image = Image.new('RGB', (500, 300), color = (73, 109, 137))
	fontsize = 1 

	img_fraction = 0.5

	font = ImageFont.truetype('open-sans/OpenSans-Regular.ttf', fontsize)
	while font.getsize(txt)[0] < img_fraction*image.size[0]:
	    fontsize += 1
	    font = ImageFont.truetype('open-sans/OpenSans-Regular.ttf', fontsize)

	fontsize -= 1
	draw = ImageDraw.Draw(image)
	draw.text((10,10), txt,font = ImageFont.truetype('open-sans/OpenSans-Regular.ttf',fontsize), fill=(255,255,0)) 
	out="out/"+out+".png"
	image.save(out)
	print out
	at.afftrans(out)

