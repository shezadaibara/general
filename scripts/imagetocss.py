from PIL import Image

IMG_SRC = '/home/shezad/Pictures/Fullmetal_Alchemist_symbol_Wallpaper_r8l.jpg'


def image_to_css(input_file_path, div_id):
    """
    input_file_path : path to the jpg image file
    div_id : id of the div tag in the html file
    """
    try:
        ext = input_file_path.split('.')[-1]
        
        if ext.lower() not in ['jpg', 'jpeg']:
            raise Exception("Only jpg image files allowed")
        img = Image.open(input_file_path)
    
    except IOError as e:
        print 'ERROR : {}'.format(str(e))
    except Exception as e:
        print 'ERROR : {}'.format(str(e))
        
    pix = img.load()
    width, height = img.size
    css = """body {background: black;} """
    css = css + div_id + """ {
            position: absolute;
            top: 30px;
            left: 50%;
            margin-left: -200px;
            width: 0;
            height: 0;
            box-shadow:
            """
    css_list = []
    for y in xrange(0, height):
        for x in xrange(0, width):
            r,g,b = pix[x,y]
            css_list.append('{0}px {1}px 1px 1px rgb({2},{3},{4})'.format(x,y,r,g,b))
    css = css + ',\n'.join(css_list) + '\n}'
    fd = open('processed_css.txt' , 'w')
    fd.write(css)
    print 'Process completed the out'
    
    
    
    