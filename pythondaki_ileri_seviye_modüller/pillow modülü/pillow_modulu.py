from PIL import Image,ImageFilter

image = Image.open("1661671159836.jpg")
image.save("ben.jpg")
image.rotate(180).save("ben2.jpg")
image.rotate(90).save("ben3.jpg")
image.convert(mode = "L").save("ben4.jpg")
degistir = (960,600)
image.thumbnail(degistir)
image.save("ben5.jpg")
image.filter(ImageFilter.GaussianBlur(3)).save("ben6.jpg")

kirpilicak_alan = (150,0,700,900)
image2 = Image.open("241116089_570182977441636_5017300570137861968_n.jpg")
image2.crop(kirpilicak_alan).save("bne1.jpg")