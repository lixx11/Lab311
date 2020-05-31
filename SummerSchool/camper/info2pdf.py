# some reportlab classes and functions
from reportlab.lib import fonts, colors
from reportlab.lib.pagesizes import A4, inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

import os

###########################################################
# adding Chinese font
###########################################################
fontPath = os.path.join(os.path.dirname(__file__), 'fonts')
pdfmetrics.registerFont(TTFont('songti', os.path.join(fontPath, 'simsun.ttc')))
pdfmetrics.registerFont(TTFont('heiti', os.path.join(fontPath, 'simhei.ttf')))

###########################################################
# predefine some text style
###########################################################
style_sheet = getSampleStyleSheet()
style_sheet.add(ParagraphStyle(name='MyTitleStyle',
                               fontName='heiti',
                               fontSize=16,
                               leading=20,
                               spaceAfter=16,
                               alignment=TA_CENTER))
style_sheet.add(ParagraphStyle(name='MySignatureStyle',
                               fontName='songti',
                               fontSize=14,
                               leading=18,
                               spaceBefore=16,
                               alignment=TA_RIGHT))

###########################################################
# dummy student information in a dictionary
###########################################################
demo_info = {
    'name': '李旭', 
    'gender': '女', 
    'id_number': '2015310310',
    'email': '18888888888@139.com',
    'phone_number': '18888888888',
    'school': '清华大学',
    'department': '工程物理系',
    'major': '工程物理',
    'major_number': '100',
    'admission_date': '202006',
    'graduation_date': '202007',
    'average_score': '99.5',
    'major_rank': '1',
    'english_level': 'CET-6 600',
    'first_institute': '工物系',
    'first_degree': '博士',
    'first_major': '化学工程与技术',
    'first_interest': '同位素分离、应用与机械',
    'first_advisor': '某某某',
    'second_institute': '工物系',
    'second_degree': '博士',
    'second_major': '化学工程与技术',
    'second_interest': '同位素分离、应用与机械',
    'second_advisor': '某某某',
    'third_institute': '工物系',
    'third_degree': '博士',
    'third_major': '化学工程与技术',
    'third_interest': '同位素分离、应用与机械',
    'third_advisor': '某某某',
}


###########################################################
# save student information in pdf file
###########################################################

def info2pdf(filename, info):
    '''
    build a pdf file from information provided

    input: filename (string)
           info (dictionary)
    output: void
    '''
    doc = SimpleDocTemplate(filename, pagesize=A4)
    # container for the 'Flowable' objects
    elements = []

    data = [
        ['基本信息', '', '', '', '', ''],
        ['姓名：'+info['name'], '', '性别：'+info['gender'], '身份证号：'+info['id_number'], '', ''],
        ['电子邮箱：'+info['email'], '', '', '手机号码：'+info['phone_number'], '', ''],
        ['本科阶段信息', '', '', '', '', ''],
        ['学校：'+info['school'], '', '', '院系：'+info['department'], '', ''],
        ['专业：'+info['major'], '', '', '专业人数：'+info['major_number']+'人', '', ''],
        ['入学时间：'+info['admission_date'], '', '', '拟毕业时间：'+info['graduation_date'], '', ''],
        ['平均成绩：'+info['average_score'], '', '专业排名：'+info['major_rank'], '', '英语水平：'+info['english_level'], ''],
        ['志愿信息', '', '', '', '', ''],
        ['第一志愿', info['first_wish'], '', '', '', ''],
        ['第二志愿', info['second_wish'], '', '', '', ''],
        ['第三志愿', info['third_wish'], '', '', '', ''],
        ['注意：请将申请材料纸质版邮寄到清华大学工程物理系\n教学办，邮寄材料截至日期为2020年6月23日（请用EMS或\n顺丰邮寄，以当地邮戳为准，请尽早寄出），邮寄地址为\n北京市海淀区清华大学刘卿楼213工程物理系教学办', '', '', '', '本人签字：\n\n日期：', '']
    ]

    rowHeight = [0.5] * 9 + [0.7] * 3 + [1.2]
    for i in range(len(rowHeight)):
        rowHeight[i] *= inch

    t = Table(data, 6 * [1.1 * inch], rowHeight)

    t.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('FONT', (0, 0), (-1, -1), 'songti'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SPAN', (0, 0), (5, 0)),
        ('SPAN', (0, 1), (1, 1)),
        ('SPAN', (3, 1), (5, 1)),
        ('SPAN', (0, 2), (2, 2)),
        ('SPAN', (3, 2), (5, 2)),
        ('SPAN', (0, 3), (5, 3)),
        ('SPAN', (0, 4), (2, 4)),
        ('SPAN', (3, 4), (5, 4)),
        ('SPAN', (0, 5), (2, 5)),
        ('SPAN', (3, 5), (5, 5)),
        ('SPAN', (0, 6), (2, 6)),
        ('SPAN', (3, 6), (5, 6)),
        ('SPAN', (0, 7), (1, 7)),
        ('SPAN', (2, 7), (3, 7)),
        ('SPAN', (4, 7), (5, 7)),
        ('SPAN', (0, 8), (5, 8)),
        ('SPAN', (1, 9), (5, 9)),
        ('SPAN', (1, 10), (5, 10)),
        ('SPAN', (1, 11), (5, 11)),
        ('SPAN', (0, 12), (3, 12)),
        ('SPAN', (4, 12), (5, 12)),
        ('ALIGN', (0, 0), (5, 0), 'CENTER'),
        ('ALIGN', (0, 3), (5, 3), 'CENTER'),
        ('ALIGN', (0, 8), (5, 8), 'CENTER'),
        ('GRID', (0, 0), (5, 11), 0.25, colors.black),
    ]))
    elements.append(Paragraph('2020年清华大学核学科夏令营报名确认表',
                              style=style_sheet['MyTitleStyle']))
    elements.append(t)
    elements.append(Paragraph('清华大学工程物理系研究生办',
                              style=style_sheet['MySignatureStyle']))
    elements.append(Paragraph('清华大学核能与新能源技术研究院研究生办',
                              style=style_sheet['MySignatureStyle']))
    # write the document to disk
    doc.build(elements)


if __name__ == '__main__':
    info2pdf('test_function.pdf', demo_info)
