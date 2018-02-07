# coding: utf-8
import datetime
from wand.image import Image
import subprocess
import os

PDF_SOURCE = '2018_code_calendar.pdf[{}]'  # pdf路径
BACKGROUND_SOURCE = 'example.jpg'  # 壁纸路径


PAGE_OFFSET = 6  # 周历从PDF文档的第7页开始
MARGIN_LEFT = 100  # 周历的左边距
MARGIN_TOP = 10  # 周历的上边距

current_week = datetime.datetime.now().isocalendar()[1]  # 获取当前是第几周
page = PAGE_OFFSET + current_week  # 获取周历在PDF文档中的页号

if not os.path.exists('output'):
    os.mkdir('output')

OUTPUT = os.path.join('output', BACKGROUND_SOURCE)

with Image(filename=PDF_SOURCE.format(page), resolution=200) as calendar:
    with Image(filename=BACKGROUND_SOURCE) as background:
        background.composite_channel('default_channels', calendar, 'blend', MARGIN_LEFT, MARGIN_TOP)
        background.save(filename=OUTPUT)

subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri",
                 "file:///"+os.path.abspath(OUTPUT)])
