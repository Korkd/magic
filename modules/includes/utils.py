from PIL import Image
import ImageFont, ImageDraw

colors = {
    "b": (203,194,191),
    "u":(170,224,250),
    "g":(155,211,174),
    "r":(249,170,143),
    "w":(255,251,213)
    }

def CreateManaSymbol(color, dimensions):
    x = 500
    y = 500
    r = 500
    color = color.lower()
    if len(color) is 2:
        pos = (-155, -80)
        size = 1000
    else:
        pos = (-70, -210)
        size = 1300
    
    image = Image.new("RGBA", (1025,1025), (255,255,255, 0))
    usr_font = ImageFont.truetype("MTG.ttf", size)
    d_usr = ImageDraw.Draw(image)
    d_usr.ellipse((x-r, y-r, x+r+20, y+r+20), fill=(20,20,20,200))

    if color.isdigit():
        pos = (pos[0]+20, pos[1])
        d_usr.ellipse((x-r, y-r, x+r, y+r), fill=colors["b"])
    elif len(color) == 2:
        if color[0] == "p":
            d_usr.ellipse((x-r, y-r, x+r, y+r), fill=colors[color[1]])
        elif not color.isdigit():
            d_usr.pieslice((x-r, y-r, x+r, y+r), 135, -45, fill=colors[color[0] if color[0].isalpha() else "b"])
            d_usr.pieslice((x-r, y-r, x+r, y+r), -45, 135, fill=colors[color[1] if color[1].isalpha() else "b"])
    else:
        d_usr.ellipse((x-r, y-r, x+r, y+r), fill=colors["b" if color == "x" else color])
    
    if len(color) is 2:
        if color.isdigit():
            d_usr.text(pos, color[0],(0,0,0), font=usr_font)
            pos = (pos[0]+360, pos[1])
            d_usr.text(pos, color[1],(0,0,0), font=usr_font)
        elif color[0] == "p":
            d_usr.text((-20, -43), "P",(0,0,0), font=usr_font)
        else:
            usr_font = ImageFont.truetype("MTG.ttf", 600)
            pos = (60, 0)
            d_usr.text(pos, color[0],(0,0,0), font=usr_font)
            pos = (pos[0]+360, pos[1]+360)
            d_usr.text(pos, color[1],(0,0,0), font=usr_font)
    else:
        if color == 'b':
            pos = (pos[0]+10, pos[1])
        d_usr.text(pos, color,(0,0,0), font=usr_font)
    img_resized = image.resize((dimensions,dimensions), Image.ANTIALIAS)
    img_resized.save(color.upper()+".png")


#CreateManaSymbol("W", 100);
#CreateManaSymbol("B", 100);
#CreateManaSymbol("R", 100);
#CreateManaSymbol("G", 100);
#CreateManaSymbol("U", 100);
#CreateManaSymbol("PU", 100);
#CreateManaSymbol("3", 100);
#CreateManaSymbol("15", 100);
#CreateManaSymbol("2R", 100);
#CreateManaSymbol("GW", 100);
#CreateManaSymbol("GU", 100);
#CreateManaSymbol("BG", 100);
#CreateManaSymbol("RW", 100);
#CreateManaSymbol("WU", 100);
#CreateManaSymbol("WB", 100);
#CreateManaSymbol("RW", 100);
#CreateManaSymbol("UB", 100);
#CreateManaSymbol("UR", 100);
#CreateManaSymbol("BR", 100);
#CreateManaSymbol("X", 100);