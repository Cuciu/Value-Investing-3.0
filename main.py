from bs4 import BeautifulSoup
import requests
import re
from flask import Flask

def Convert(string):
    li = list(string.split(","))
    return li

def Average(lst):
    return sum(lst) / len(lst)

url = 'https://www.macrotrends.net/stocks/charts/VIV/telefonica-brasil-sa/income-statement'
res = requests.get(url)
html_string = BeautifulSoup(res.content, 'html.parser')
html_string = str(html_string)

app = Flask(__name__)
@app.route('/')
def hello():

    # NET INCOME
    StringNetIncome0 = re.search('Net Income(.*)EBITDA', html_string)
    StringNetIncome = re.search('div>",(.*)},{"', StringNetIncome0.group(1))
    NetIncome = str(StringNetIncome.group(1).replace('"', ''))
    a = NetIncome.count(':')
    b = Convert(NetIncome)
    ListNetIncome = []
    NetIncomeGrowth = []
    for i in range(0, a):
        var, var2 = [b[i] for j in (i, i + 1)]
        c = list(var.split(":"))
        e, f = [c[j] for j in (0, 1)]
        ListNetIncome.append(f)
    for x in range(0, a - 1):
        NetIncomeGrowth1 = 100 * (float(ListNetIncome[x]) - float(ListNetIncome[x + 1])) / float(ListNetIncome[x + 1])
        NetIncomeGrowth.append(NetIncomeGrowth1)
        if x == 4:
            NetIncomeGrowth5 = 100 * (float(ListNetIncome[x - 4]) - float(ListNetIncome[x])) / float(ListNetIncome[x])
            print(" 5 Years Net Income Growth Rate {}%".format(NetIncomeGrowth5))
            r1 = str("5 Years Net Income Growth Rate {}%".format(NetIncomeGrowth5))
        if x == 9:
            NetIncomeGrowth10 = 100 * (float(ListNetIncome[x - 9]) - float(ListNetIncome[x])) / float(ListNetIncome[x])
            r2 = str(" 10 Years Net Income Growth Rate {}%".format(NetIncomeGrowth10))
    r3 = str("List of Net Income growth rates {}".format(NetIncomeGrowth))

    # EPS
    StringEPS0 = re.search('eps-earnings-per-share-diluted(.*)}];', html_string)
    StringEPS = re.search('div>",(.*)}];', StringEPS0.group(0))
    EPS = str(StringEPS.group(1).replace('"', ''))
    a1 = EPS.count(':')
    b1 = Convert(EPS)
    listofEPS = []
    listofEPSGrowth = []
    for i in range(0, a1):
        var, var2 = [b1[i] for j in (i, i + 1)]
        c1 = list(var.split(":"))
        e1, f1 = [c1[j] for j in (0, 1)]
        listofEPS.append(f1)
    print(listofEPS)
    for x in range(0, a1 - 1):
        EPSGrowth = (float(listofEPS[x]) - float(listofEPS[x + 1])) * 100
        listofEPSGrowth.append(EPSGrowth)
        if x == 4:
            EPSGrowth5 = 100 * (float(listofEPS[x - 4]) - float(listofEPS[x])) / float(listofEPS[x])
            r4 = str(" 5 Years Growth Rate {}%".format(EPSGrowth5))
        if x == 9:
            EPSGrowth10 = 100 * (float(listofEPS[x - 9]) - float(listofEPS[x])) / float(listofEPS[x])
            r5 = str(" 10 Years Growth Rate {}%".format(EPSGrowth10))
    r6 = str("list of growth rates {}".format(listofEPSGrowth))
    r = str([r1, '/n',r2,r3,r4,r5,r6])
    return r;
