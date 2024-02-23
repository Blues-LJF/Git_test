import requests
from bs4 import BeautifulSoup
import re
from openpyxl import Workbook


def get_html(url):
    """获取页面HTML内容"""
    response = requests.get(url)
    response.raise_for_status()  # 如果请求失败会抛出HTTPError异常
    return response.text


def parse_links(html):
    """从HTML中解析出所有链接"""
    soup = BeautifulSoup(html, "html.parser")
    links = [a["href"] for a in soup.find_all("a", href=True)]
    return links


def output_excel(links):
    # 创建新的工作簿
    workbook = Workbook()
    # 选择活动工作表（默认为第一个工作表）
    worksheet = workbook.active
    # 行号
    columnNum = 1
    # 循环写入Excel文件
    if columnNum == 1:
        worksheet["A" + str(columnNum)] = "链接"
    for link in links:
        isHttp = bool(re.match(r"^http[s]?://", link))
        if isHttp:
            columnNum += 1
            print(columnNum)
            # 写入数据
            worksheet["A" + str(columnNum)] = link
            # print(link)

    # 保存文件
    workbook.save("D:\Desktop\个人\output.xlsx")


def main():
    url = "https://www.kastking.com/"
    html = get_html(url)
    links = parse_links(html)
    print("Found {} links on the page.".format(len(links)))
    output_excel(links)


if __name__ == "__main__":
    main()
