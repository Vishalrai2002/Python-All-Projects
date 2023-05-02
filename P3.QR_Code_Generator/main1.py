import qrcode as qr
# simple step to make any type of qr 
img=qr.make("hello how are you")  # You can also pass a link in this ""
img.save("1.png") # save name as 1.png