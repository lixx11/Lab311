# some reportlab classes and functions
from reportlab.lib import fonts, colors
from reportlab.lib.pagesizes import A4, inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_RIGHT, TA_CENTER

###########################################################
# adding Chinese font
###########################################################
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
fontPath = '/Users/lixuanxuan/repository/Lab311/GraduateAdmission/student_info/fonts/'
pdfmetrics.registerFont(TTFont('songti', fontPath+'simsun.ttc'))
pdfmetrics.registerFont(TTFont('heiti', fontPath+'simhei.ttf'))

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
info = {'name': '李旭', 'id': '2015310310', # basic information
        'score_politics': '8', 'score_english': '10', # scores
        'score_third': '5', 'test_name_third': '数学',
        'score_prof': '5', 'test_name_prof': '物理',
        'score_total': '28', 
        'orignial_target_major': '北京大学工程物理系', # targets
        'target_1': '核能与核技术工程（085226）（清华本部）核能方向', 
        'target_2': '核能与核技术工程（085226）（清华本部）核燃料方向（定向）',
        'target_3': '安全工程（085224）（深圳研究生院）公共安全',
        'target_4': '安全工程（085224）（深圳研究生院）核能安全',
        'target_5': '核能与核技术工程（085226）（清华本部）核技术方向',
        'chosen_test_name': '数学'}

###########################################################
# save student information in pdf file
###########################################################

def info2pdf(filename, info=info):
    '''
    build a pdf file from information provided

    input: filename (string)
           info (dictionary)
    output: void
    '''
    doc = SimpleDocTemplate(filename, pagesize=A4)
    # container for the 'Flowable' objects
    elements = []
     
    data = [['', '', '', '', '', ''],
           ['考生姓名：', info['name'], '', '', '考生编号：', info['id']],
           ['', '', '', '', '', ''],
           ['初试\n成绩', '政治', '英语', info['test_name_third'], info['test_name_prof'], '总成绩'],
           ['', info['score_politics'], info['score_english'], info['score_third'], info['score_prof'], info['score_total']],
           ['原报考专业', info['orignial_target_major'], '', '', '', ''],
           ['', '', '', '', '', ''],
           ['调剂\n志愿\n选择', '第一志愿', info['target_1'], '', '', ''],
           ['', '第二志愿', info['target_2'], '', '', ''],
           ['', '第三志愿', info['target_3'], '', '', ''],
           ['', '第四志愿', info['target_4'], '', '', ''],
           ['', '第五志愿', info['target_5'], '', '', ''],
           ['考试科目', info['chosen_test_name'], '', '', '', ''],
           ['', '', '', '', '', ''],       
           ['请打印签字确认，并于x月x日交至系教务\n（调剂志愿一旦提交，不能修改）', '', '', '', '本人签字：', ''],
           ['', '', '', '', '日期：', ''],
           ['', '', '', '', '', '']]

    rowHeight = [0.1, 0.5, 0.1, 0.5, 0.5, 0.5, 0.1, 0.5,0.5,0.5,0.5,0.5,0.5, 0.3, 0.5, 0.5, 0.3]
    for i in range(len(rowHeight)):
        rowHeight[i] *= inch

    t = Table(data, 6*[1.1*inch], rowHeight )

    t.setStyle(TableStyle([('BOX', (0,0), (-1,-1), 1, colors.black),
                           ('FONT', (0,0), (-1,-1), 'songti'),
                           ('FONTSIZE', (0,0), (-1,-1), 12),
                           ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                           ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
                           ('SPAN', (0, 3), (0,4)), # span for row title
                           ('SPAN', (0, 7), (0,11)),
                           ('SPAN', (1,5), (5,5)), # span for long message
                           ('SPAN', (2,7), (5,7)),
                           ('SPAN', (2,8), (5,8)),
                           ('SPAN', (2,9), (5,9)),
                           ('SPAN', (2,10), (5,10)),
                           ('SPAN', (2,11), (5,11)),
                           ('SPAN', (1,12), (5,12)),
                           ('SPAN', (0,14), (2,15)), # span for notification
                           ('GRID', (0,3), (5, 5), 0.25, colors.black), # grid for some cells
                           ('GRID', (0,7), (5,12), 0.25, colors.black),
                           ('ALIGN', (4,-3), (4,-2), 'LEFT'), # change align for some cells
                           ('ALIGN', (2,7), (5,11), 'LEFT'),
                           ('FONTSIZE', (1,7), (5,11), 10), # change fontsize for some long names
                           ]))
    elements.append(Paragraph('清华大学工程物理系研究生入学考试调剂确认单', style=style_sheet['MyTitleStyle']))
    elements.append(t)
    elements.append(Paragraph('清华大学工程物理系研究生办', style=style_sheet['MySignatureStyle']))
    # write the document to disk
    doc.build(elements)


if __name__ == '__main__':
    info2pdf('test_function.pdf', info)
