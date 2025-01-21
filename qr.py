import qrcode
import PIL
# Create a QR code for the given URL
url = "https://www.youtube.com/watch?v=PyDn2gU9DJo"
img = qrcode.make(url)

# Save the generated QR code image to a file
img.save("img.png")

