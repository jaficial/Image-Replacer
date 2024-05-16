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
            if sum(pix[x, y]) == 0:
                grid[y][x] = '#'
            elif sum(pix[x, y]) == range(1, 100):
                grid[y][x] = "X"
            elif sum(pix[x, y]) == range(101, 200):
                grid[y][x] = "%"
            elif sum(pix[x, y]) == range(201, 300):
                grid[y][x] = "&"
            elif sum(pix[x, y]) == range(301, 400):
                grid[y][x] = "+"
            elif sum(pix[x,y]) == range(401, 500):
                grid[y][x] = "@"
            elif sum(pix[x, y]) == range(501, 600):
                grid[y][x] = "o"
            elif sum(pix[x, y]) == range(601, 700):
                grid[y][x] = "H"
            elif sum(pix[x, y]) == range(701, 800):
                grid[y][x] = "G"
            elif sum(pix[x, y]) == range(801, 900):
                grid[y][x] = "M" 
            elif sum(pix[x, y]) == range(901, 999):
                grid[y][x] = "W"
            else:
                grid[y][x] = ' '
    art = open(saveas, "w")

    for row in grid:
        art.write("".join(row) + "\n")
    art.close()

if __name__ == "__main__":
    asciiConvert('dogtest.jpeg', 'jpeg', 'dogtestASCII.txt', '3')

