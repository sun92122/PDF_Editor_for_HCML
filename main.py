from PDFEditor import PDFMaker

# test
pdf = PDFMaker()
pdf.eventNameInput('活動名稱')
pdf.groupNameInput('社團名稱')
pdf.singleInput('活動目的')
pdf.multipleInput('活動目的', 10000, 1000, '次', 1000000)
pdf.multipleInput('活動項目', 100000, 10000, '次', 10000000)
pdf.multipleInput('活動目的', 1000000, 100000, '次', 100000000, comma=True)
pdf.updateFilename('test')
pdf.save()