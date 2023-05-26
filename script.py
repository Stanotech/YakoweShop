from PIL import Image

# Open an image file
image = Image.open('1.jpg')

# Get the thumbnail
thumbnail = image.thumbnail((100, 100))

# Save the thumbnail to a new file
image.save('2.jpg')
