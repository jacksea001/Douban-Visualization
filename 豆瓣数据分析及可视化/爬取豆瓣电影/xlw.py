# -*- codeing = utf-8 -*-
# @Time : 2021/3/25 20:36
# @Author : jack_sea
# @File : xlw.py
# @Software : PyCharm

import xlwt
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i, j, "%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))
workbook.save('student.xls')


