import sys
from PIL import Image
from pathlib import Path

resize_coef = 2
canvas_resize_coef = 1.78
args_num = len(sys.argv)


if args_num > 1:
  im = Image.open(sys.argv[1])
  filename = (Path(sys.argv[1]).stem)+"_.png"
  
  if args_num ==4:
    resize_coef = float(sys.argv[2])
    canvas_resize_coef = float(sys.argv[3])
  elif args_num==3:
    resize_coef = float(sys.argv[2])

  #print(f'widht: {im.width} height:{im.height}')
  #print(f"resize: {resize_coef} canvas: {canvas_resize_coef}")
  width = im.width
  height = im.height

  padding = 0
  new_width = int(width//resize_coef)
  new_heigh = int(width//resize_coef)
  
  
  im = im.resize((new_width, new_heigh))

  #in case of vertical image add transparent paddings to the left and right
  if height > width:
    padding = int(((new_width*canvas_resize_coef)-new_width)//2)
    
    canvas = Image.new(
      "RGBA",
      (new_width+padding*2, new_heigh),
      (0, 0, 0, 0)
    ) 
    canvas.paste(im ,(padding,0))    
    
  #in case of horizontal image add transparent paddings to top and bottom
  else: 
    padding = int(((new_heigh*canvas_resize_coef)-new_heigh)//2)

    canvas = Image.new(
      "RGBA",
      (new_width, new_heigh+padding*2),
      (0, 0, 0, 0)
    ) 
    canvas.paste(im ,(0,padding))    
  
  print(f'Added transparent paddings:{padding}px \n Saved to {filename}')    
  canvas.save(filename)
else:
  print ('Usage: img-resizer <filename> [resize_coef] [canvas_resize_coef]')