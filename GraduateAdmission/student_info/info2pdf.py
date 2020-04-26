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
info = {'name': '李旭', 'sex': '女', 'id': '2015310310',  # basic information
        'university': '北京大学',
        'major': '计算机系',
        'graduation_time': '2018',
        'mobile': '18810188101',
        'email': 'nmt@qq.com',
        'score_politics': '8', 'score_english': '10',  # scores
        'score_third': '5', 'test_name_third': '数学',
        'score_prof': '5', 'test_name_prof': '物理',
        'score_total': '28',
        'original_target_test': '参加',
        'original_target_major': '北京大学-工程物理系',  # targets
        'target_1': '核能与核技术工程（085226）（清华本部）核能方向',
        'target_2': '核能与核技术工程（085226）（清华本部）核燃料方向（定向）',
        'target_3': '安全工程（085224）（深圳研究生院）公共安全',
        'target_4': '安全工程（085224）（深圳研究生院）核能安全',
        'target_5': '核能与核技术工程（085226）（清华本部）核技术方向',
        'target_6': '核能与核技术工程（085226）（清华本部）核技术方向',
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
            ['考生姓名：', info['name'], '性别', info['sex'], '考生编号：', info['id']],
            ['本科学校：' + info['university'], '', '本科专业:' + info['major'],
                '', '毕业时间：' + info['graduation_time'] + '年', ''],
            ['手机号码：' + info['mobile'], '', '', '邮箱：' + info['email'], '', ''],
            ['', '', '', '', '', ''],
            ['初试\n成绩', '政治', '英语', info['test_name_third'],
                info['test_name_prof'], '总成绩'],
            ['', info['score_politics'], info['score_english'], info['score_third'], info['score_prof'],
             info['score_total']],
            ['原报考专业', info['original_target_major'], '',
                '', '原院系复试', info['original_target_test']],
            ['', '', '', '', '', ''],
            ['调剂\n志愿\n选择', '第一志愿', info['target_1'], '', '', ''],
            ['', '第二志愿', info['target_2'], '', '', ''],
            ['', '第三志愿', info['target_3'], '', '', ''],
            ['', '第四志愿', info['target_4'], '', '', ''],
            ['', '第五志愿', info['target_5'], '', '', ''],
            ['', '第六志愿', info['target_6'], '', '', ''],
            ['考试科目', info['chosen_test_name'], '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '请在5月4日前将签字电子版发送邮件至: \ngwyjs@mail.tsinghua.edu.cn, \n纸质版本同时寄出，邮寄地址为: \n清华大学工程物理系教学办\n（清华大学刘卿楼213办公室）', '', '', '本人签字：', ''],
            ['', '', '', '', '日期：', ''],
            ['', '', '', '', '', '']]

    rowHeight = [0.1, 0.5, 0.4, 0.4, 0.1, 0.4, 0.4, 0.5, 0.1,
                 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.3, 0.6, 0.6, 0.3]
    for i in range(len(rowHeight)):
        rowHeight[i] *= inch

    t = Table(data, 6 * [1.1 * inch], rowHeight)

    t.setStyle(TableStyle([('BOX', (0, 0), (-1, -1), 1, colors.black),
                           ('FONT', (0, 0), (-1, -1), 'songti'),
                           ('FONTSIZE', (0, 0), (-1, -1), 12),
                           ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                           # span for row title
                           ('SPAN', (0, 5), (0, 6)),
                           ('SPAN', (0, 9), (0, 14)),
                           # span for long message
                           ('SPAN', (0, 2), (1, 2)),  # basic information
                           ('SPAN', (2, 2), (3, 2)),
                           ('SPAN', (4, 2), (5, 2)),
                           ('SPAN', (0, 3), (2, 3)),
                           ('SPAN', (3, 3), (5, 3)),
                           ('SPAN', (1, 7), (3, 7)),
                           # target majors
                           ('SPAN', (2, 9), (5, 9)),
                           ('SPAN', (2, 10), (5, 10)),
                           ('SPAN', (2, 11), (5, 11)),
                           ('SPAN', (2, 12), (5, 12)),
                           ('SPAN', (2, 13), (5, 13)),
                           ('SPAN', (2, 14), (5, 14)),
                           ('SPAN', (1, 15), (5, 15)),
                           # span for notification
                           ('SPAN', (1, 17), (3, 18)),
                           # grid for some cells
                           ('GRID', (0, 2), (5, 3), 0.25, colors.black),
                           ('GRID', (0, 5), (5, 7), 0.25, colors.black),
                           ('GRID', (0, 9), (5, 15), 0.25, colors.black),
                           # change align for some cells
                           ('ALIGN', (0, -3), (4, -2), 'LEFT'),
                           ('ALIGN', (2, 9), (5, 14), 'LEFT'),
                           # change fontsize for some long names
                           ('FONTSIZE', (0, 2), (5, 3), 11),  # basic info
                           ('FONTSIZE', (1, 9), (5, 14), 10),  # target majors
                           ('FONTSIZE', (1, 5), (5, 5), 10),  # scores
                           ]))
    elements.append(Paragraph('2020工程物理系硕士调剂志愿确认表',
                              style=style_sheet['MyTitleStyle']))
    elements.append(t)
    elements.append(Paragraph('清华大学工程物理系研究生办',
                              style=style_sheet['MySignatureStyle']))
    # write the document to disk
    doc.build(elements)


if __name__ == '__main__':
    info2pdf('test_function.pdf', info)
