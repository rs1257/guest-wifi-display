#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
from driver.epd2in13_V4 import EPD
from driver.epdconfig import module_exit
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)

try:    
    epd = EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)

    # Drawing on the image
    font22 = ImageFont.truetype('RobotoMono-Regular.ttf', 22)

    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), "Tap or scan to join", font = font22, fill = 0)
    draw.text((0, 26), "Ryan's Mesh Guest", font = font22, fill = 0)
    bmp = Image.open('wifi.bmp')
    image.paste(bmp, (int(epd.width/2 + 60), 50))

    qr = Image.open('qr.bmp')
    image.paste(qr, (40, 50)) 

    epd.display(epd.getbuffer(image))
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    module_exit(cleanup=True)
    exit()