import io
import os

from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

# 準備字型
pdfmetrics.registerFont(TTFont('kai', 'font/kaiu.ttf'))

# 準備黏憑 PDF
# filename = input("請輸入檔案名稱：")
filename = 'temp'
if os.path.isfile(f"黏貼憑證_{filename}.pdf"):
    existing_num = 1
    while os.path.isfile(f"黏貼憑證_{filename}_{existing_num}.pdf"):
        existing_num += 1
    filename = f"黏貼憑證_{filename}_{existing_num}.pdf"
else:
    filename = f"黏貼憑證_{filename}.pdf"

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=A4)
# font/kaiu.ttf (kai) 12.96pt
can.setFont('kai', 12.96)

def eventNameInput(eventName: str):
    can.drawString(136.2*mm, 245.2*mm, eventName)

def groupNameInput(groupName: str):
    can.drawString(136.2*mm, 239.2*mm, groupName)

def singleInput(purpose_or_item: str):
    can.drawString(113.3*mm, 227.2*mm, purpose_or_item)

def multipleInput(purpose_or_item: str, unit_price: int, quantity: int, item_unit: str, total_price: int,
                  base_x: float = 113.3*mm, base_y: float = 221.2*mm, interval: float = 6.0*mm,
                  line_num: float = 0, comma: bool = False):
    if comma:
        unit_price = f"{unit_price:,}"
        total_price = f"{total_price:,}"

    if len(purpose_or_item) > 8:
        can.drawString(base_x, base_y-line_num*interval, purpose_or_item)
        can.drawString(base_x+22.9*mm, base_y-(line_num+1)*interval, f"{unit_price}元 × {quantity}{item_unit} = {total_price}元")
        return 2
    else:
        can.drawString(base_x, base_y-line_num*interval, purpose_or_item)
        can.drawString(base_x+22.9*mm, base_y-line_num*interval, f"{unit_price}元 × {quantity}{item_unit} = {total_price}元")
        return 1
    

# test input
eventNameInput("活動名稱一二三四五六七八九十")
groupNameInput("活動股別一二三四五六七八九十")
line_num = 0
line_num += singleInput("單一項目一二三四五六七八九十")
line_num += multipleInput("多個項目一二三四五六七八九十", 100, 10, '個', 1000, line_num=line_num, comma=True)
line_num += multipleInput("abcdefgh", 100, 10, '個', 1000, line_num=line_num, comma=True)
line_num += multipleInput("abcdefghi", 100, 10, '個', 1000, line_num=line_num, comma=True)
line_num += multipleInput("中文英混打", 100, 10, '個', 10000, line_num=line_num, comma=True)

# edit done
can.save()

packet.seek(0)

new_pdf = PdfReader(packet)
existing_pdf = PdfReader(open("黏貼憑證用紙.pdf", "rb"))

output = PdfWriter()

page = existing_pdf.pages[0]
page.merge_page(new_pdf.pages[0])
output.add_page(page)

# 輸出黏憑 PDF
outputStream = open(filename, "wb")
output.write(outputStream)
outputStream.close()
