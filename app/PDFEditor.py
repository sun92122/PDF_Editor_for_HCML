import io
import os

from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def chineseCount(string: str):
    count = len(string)
    for char in string:
        if ord(char) > 127:
            count += 1
    return count

def chineseSplit(string: str, max_len: int):
    count = 0
    for i in range(len(string)):
        if ord(string[i]) > 127:
            count += 2
        else:
            count += 1
        if count > max_len:
            return string[:i], string[i:]
    return string, ''

def fileNameCheck(filename: str, prefix: str = '黏貼憑證', suffix: str = '.pdf'):
    if filename != '':
        filename = f"_{filename}"

    if os.path.isfile(f"{prefix}{filename}{suffix}"):
        existing_num = 1
        while os.path.isfile(f"{prefix}{filename}_{existing_num}{suffix}"):
            existing_num += 1
        filename = f"{prefix}{filename}_{existing_num}{suffix}"
    else:
        filename = f"{prefix}{filename}{suffix}"

    return filename

class PDFMaker:
    def __init__(self):
        # 準備字型
        pdfmetrics.registerFont(TTFont('kai', 'font/kaiu.ttf'))
        self.filename = ''
        self.filename = fileNameCheck(self.filename)
        self.packet = io.BytesIO()
        self.can = canvas.Canvas(self.packet, pagesize=A4)
        self.can.setFont('kai', 12.96)
        self.line_num = 0
        self.line_height = 6.0*mm
        self.comma = False
        self.base_x = 113.3*mm
        self.base_y = 227.2*mm

    def eventNameInput(self, eventName: str):
        self.can.drawString(136.2*mm, 245.2*mm, eventName)

    def groupNameInput(self, groupName: str):
        self.can.drawString(136.2*mm, 239.2*mm, groupName)

    def singleInput(self, purpose_or_item: str):
        if chineseCount(purpose_or_item) > 32:
            purpose_or_item, purpose_or_item2 = chineseSplit(purpose_or_item, 32)
            self.can.drawString(self.base_x, self.base_y, purpose_or_item)
            self.can.drawString(self.base_x, self.base_y-self.line_height, purpose_or_item2)
            self.line_num = 1
        else:
            self.can.drawString(self.base_x, self.base_y, purpose_or_item)
            self.line_num = 0

    def multipleInput(self, purpose_or_item: str, unit_price: int, quantity: int, item_unit: str, total_price: int):
        swift_width = 22.9*mm
        if self.comma:
            unit_price = f"{unit_price:,}"
            total_price = f"{total_price:,}"
        
        price_str = f"{unit_price}元 × {quantity}{item_unit} = {total_price}元"
        price_str_len = chineseCount(price_str)
        
        # print purpose_or_item
        self.can.drawString(self.base_x, self.base_y-self.line_num*self.line_height, purpose_or_item)

        # print price_str
        if chineseCount(purpose_or_item) > 10 or price_str_len > 23:
            if price_str_len > 23:
                self.can.drawString(self.base_x, self.base_y-(self.line_num+1)*self.line_height, price_str)
            else:
                self.can.drawString(self.base_x+swift_width, self.base_y-(self.line_num+1)*self.line_height, price_str)
            self.line_num += 2
        else:
            self.can.drawString(self.base_x+swift_width, self.base_y-self.line_num*self.line_height, price_str)
            self.line_num += 1
    
    def blankLine(self, line_num: int = 1):
        self.line_num += line_num
    
    def save(self):
        self.can.save()
        self.packet.seek(0)
        new_pdf = PdfReader(self.packet)
        existing_pdf = PdfReader(open("黏貼憑證用紙.pdf", "rb"))

        output = PdfWriter()

        page = existing_pdf.pages[0]
        page.merge_page(new_pdf.pages[0])
        output.add_page(page)

        # 輸出黏憑 PDF
        outputStream = open(self.filename, "wb")
        output.write(outputStream)
        outputStream.close()

    def updateFilename(self, filename: str):
        self.filename = fileNameCheck(filename)
    
    def updateLineHeight(self, line_height: float):
        self.line_height = line_height
    
    def updateComma(self, comma: bool):
        self.comma = comma
    
    def reset(self):
        self.packet = io.BytesIO()
        self.can = canvas.Canvas(self.packet, pagesize=A4)
        self.can.setFont('kai', 12.96)
        self.line_num = 0