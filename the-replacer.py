import glob, os 
from PIL import Image
def asciiConvert(image, type, saveas, scale):
    scale = int(scale)

    # opens and gets image size
    img = Image.open(image)
    w, h = img.size
    
    # resizes the image (by downscaling)
    img.resize((w//scale, h//scale)).save("resized.%s" % type)
    
    # opens a new image
    img = Image.open("resized.%s" % type)
    
    #list with correct length and height (WHICH IS THE SAME SIZE AS THE RESIZED IMAGE)
    grid = []
    for i in range(h):
        grid.append(["X"] * w)

    pix = img.load()
    for y in range(h):
        for x in range(w):
            if sum()

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        im.thumbnail(size)
        im.save(file + ".thumbnail", "JPEG")
