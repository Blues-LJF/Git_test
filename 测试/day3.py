import openpyxl
from RPA.Browser import Browser
 
# 读取Excel文件
wb = openpyxl.load_workbook('data.xlsx')
sheet = wb.active
 
# 初始化浏览器
browser = Browser()
 
# 打开Web应用程序
browser.open('https://example.com')
 
# 循环读取Excel中的数据并输入到Web应用程序中
for row in sheet.iter_rows(values_only=True):
    username = row[0]
    password = row[1]
 
    # 输入用户名和密码
    browser.input_text('username_input', username)
    browser.input_text('password_input', password)
 
    # 点击登录按钮
    browser.click_button('login_button')
 
# 关闭浏览器
browser.close()