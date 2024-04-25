from PIL import Image
 
def most_common_used_color(img):
    """img = Image object"""
    # Get width and height of Image
    width, height = img.size
 
    # Initialize Variable
    r_total = 0
    g_total = 0
    b_total = 0
 
    count = 0
 
    # Iterate through each pixel
    for x in range(0, width):
        for y in range(0, height):
            # r,g,b value of pixel
            r, g, b = img.getpixel((x, y))
 
            r_total += r
            g_total += g
            b_total += b
            count += 1
 
    return (r_total/count, g_total/count, b_total/count)

def convert_img_to_rgb(img_link):
    """img = string that represents file path to image"""
    img = Image.open(img_link)
    img = img.convert('RGB')
    img_colors = most_common_used_color(img)    
    return img_colors