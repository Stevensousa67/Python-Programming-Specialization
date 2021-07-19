# In the lectures for this week you were shown how to make a contact sheet for digital photographers, and how you can
# take one image and create nine different variants based on the brightness of that image. In this assignment you are
# going to change the colors of the image, creating variations based on a single photo. There are many complex ways to
# change a photograph using variations, such as changing a black and white image to either "cool" variants, which have
# light purple and blues in them, or "warm" variants, which have touches of yellow and may look sepia toned. In this
# assignment, you'll be just changing the image one color channel at a time
# For instance, a pixel represented as (200, 100, 50) is a sort of burnt orange color. So the top row of changes would
# create three alternative pixels, varying the first channel (red). one at (20, 100, 50), one at (100, 100, 50), and one
# at (180, 100, 50). The next row would vary the second channel (blue), and would create pixels of color values (200,
# 10, 50), (200, 50, 50) and (200, 90, 50).
# Note: A font is included for your usage if you would like! It's located in the file `readonly/fanwood-webfont.ttf`

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from IPython.display import display

# read image and convert to RGB
image = Image.open("readonly/msi_recruitment.gif")
image = image.convert('RGB')

# Set font for pics
font = ImageFont.truetype(r'readonly/fanwood-webfont.ttf', 50)

# Create empty list where colored pics will populate
colored_pics = []

# For loop that will iterate over the same pic 9 times and apply different coloring on each one
for pic in range(1, 10):

    # Create intensity for each pic in a row (each row has 3 pics)
    if pic % 3 == 1:
        intensity = 0.1

    elif pic % 3 == 2:
        intensity = 0.5

    elif pic % 3 == 0:
        intensity = 0.9

    # Create channel for each row (there will be a total of 3 rows)
    if pic <= 3:
        channel = 0
    elif pic <= 6:
        channel = 1
    elif pic <= 9:
        channel = 2

    # Create copy of original pic to keep original intact
    copy_of_original = image.copy()

    # Create "print statement to put on each pic"
    text = "channel {} intensity {}".format(channel, intensity)

    # Place "print statement on pic"
    ImageDraw.Draw(copy_of_original).text((0, copy_of_original.height - 45), text, font=font, align='left')

    # Get RGB values from pic
    r, g, b = copy_of_original.split()

    # Get correct RGB modification to apply on pic
    if channel == 0:
        r = r.point(lambda x: x * intensity)
    elif channel == 1:
        g = g.point(lambda x: x * intensity)
    elif channel == 2:
        b = b.point(lambda x: x * intensity)

    # Apply RGB correction to pic
    copy_of_original = Image.merge('RGB', (r, g, b))
    colored_pics.append(copy_of_original)

# create a contact sheet from different brightnesses
first_image = colored_pics[0]
contact_sheet = PIL.Image.new(first_image.mode, (first_image.width * 3, first_image.height * 3))
x = 0
y = 0

for img in colored_pics:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y))
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x + first_image.width == contact_sheet.width:
        x = 0
        y = y + first_image.height
    else:
        x = x + first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width / 2), int(contact_sheet.height / 2)))
display(contact_sheet)
