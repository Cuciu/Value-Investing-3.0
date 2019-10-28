from flask import Flask, render_template, request, redirect, url_for
from bs4 import BeautifulSoup
import requests
import re
import numpy as np

def Convert(string):
    li = list(string.split(","))
    return li

def Average(lst):
    return sum(lst) / len(lst)

def URLHandler(url0):
    res = requests.get(url0)
    html_string = BeautifulSoup(res.content, 'html.parser')
    html_string = str(html_string)
    return html_string

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      compurl = request.form['Base_Link']
      Years = int(request.form['Years'])
      NBShares = int(request.form['Number_Shares'])
      RealDiscountRate = request.form['RealDiscountRate']
      AverageInflation = float(request.form['AverageInflation'])
      NominalDiscountRate = float(request.form['NominalDiscountRate'])

      url1 = compurl + 'financial-statements'
      url2 = compurl + 'balance-sheet'
      url3 = compurl + 'pe-ratio'
      url4 = compurl + 'cash-flow-statement'
      url5 = compurl + 'stock-price-history'

      # Financial-Statements
      # NET INCOME
      StringNetIncome0 = re.search('Net Income(.*)EBITDA', URLHandler(url1))
      StringNetIncome = re.search('div>",(.*)},{"', StringNetIncome0.group(1))
      NetIncome = str(StringNetIncome.group(1).replace('"', ''))
      a = NetIncome.count(':')
      b = Convert(NetIncome)
      ListNetIncome = []
      NetIncomeGrowth = []
      for i in range(0, a):
          var = b[i]
          c = list(var.split(":"))
          e, f = [c[j] for j in (0, 1)]
          ListNetIncome.append(f)
      for x in range(0, a - 1):
          NetIncomeGrowth1 = "%.2f" % round(
              100 * (float(ListNetIncome[x]) - float(ListNetIncome[x + 1])) / float(ListNetIncome[x + 1]), 2)
          NetIncomeGrowth.append(NetIncomeGrowth1)
          if x == 4:
              NetIncomeGrowth5 = "%.2f" % round(
                  100 * (float(ListNetIncome[x - 4]) - float(ListNetIncome[x])) / float(ListNetIncome[x]), 2)
              NetIncome5yGrowth = str("5 Years Net Income Growth Rate {}%".format(NetIncomeGrowth5))
          if x == 9:
              NetIncomeGrowth10 = "%.2f" % round(
                  100 * (float(ListNetIncome[x - 9]) - float(ListNetIncome[x])) / float(ListNetIncome[x]), 2)
              NetIncome10yGrowth = str(" 10 Years Net Income Growth Rate {}%".format(NetIncomeGrowth10))
      NetIncomeGrowthList = str("List of Net Income growth rates {}".format(NetIncomeGrowth))

      # EPS
      StringEPS0 = re.search('eps-earnings-per-share-diluted(.*)}];', URLHandler(url1))
      StringEPS = re.search('div>",(.*)}];', StringEPS0.group(0))
      EPS = str(StringEPS.group(1).replace('"', ''))
      a1 = EPS.count(':')
      b1 = Convert(EPS)
      listofEPS = []
      listofEPSGrowth = []
      for i in range(0, a1):
          var = b1[i]
          c1 = list(var.split(":"))
          e1, f1 = [c1[j] for j in (0, 1)]
          listofEPS.append(f"{round(float(f1), 2):.2f}")
      lastEPSstr = str("Last EPS {}".format(listofEPS[0]))
      lastEPS = float(listofEPS[0])
      previousEPS = float(listofEPS[1])
      EPS = str("List of yearly EPS {}".format(listofEPS))
      for x in range(0, a1 - 1):
          EPSGrowth = "%.2f" % round(((float(listofEPS[x]) - float(listofEPS[x + 1])) * 100), 2)
          listofEPSGrowth.append(EPSGrowth)
          if x == 4:
              EPSGrowth5 = "%.2f" % round(
                  (100 * (float(listofEPS[x - 4]) - float(listofEPS[x])) / float(listofEPS[x])),
                  2)
              EPS5yGrowth = str(" 5 Years Growth Rate {}%".format(EPSGrowth5))
          if x == 9:
              EPSGrowth10 = "%.2f" % round(
                  (100 * (float(listofEPS[x - 9]) - float(listofEPS[x])) / float(listofEPS[x])),
                  2)
              EPS10yGrowth = str(" 10 Years Growth Rate {}%".format(EPSGrowth10))
      EPSGrowthList = str("List of EPS growth rates {}".format(listofEPSGrowth))

      # Balance Sheet
      # Current Liabilities/Cash Factor
      StringCurrentLiabilities0 = re.search('total-current-liabilities(.*)Long Term Debt', URLHandler(url2))
      StringCurrentLiabilities = re.search('div>",(.*)},{', StringCurrentLiabilities0.group(0))
      CurrentLiabilities = str(StringCurrentLiabilities.group(1).replace('"', ''))
      a1 = CurrentLiabilities.count(':')
      b1 = Convert(CurrentLiabilities)
      listCurrentLiabilities = []
      for i in range(0, a1):
          var = b1[i]
          c1 = list(var.split(":"))
          e1, f1 = [c1[j] for j in (0, 1)]
          listCurrentLiabilities.append(f"{round(float(f1), 2):.2f}")
      lastCurrentLiabilities = str(listCurrentLiabilities[0])
      CurrentLiabilities0 = str("current Liabilities {} ".format(lastCurrentLiabilities))

      StringCurrentCash0 = re.search('cash-on-hand(.*)Notes And Loans Receivable', URLHandler(url2))
      StringCurrentCash = re.search('div>",(.*)},{', StringCurrentCash0.group(0))
      CurrentCash = str(StringCurrentCash.group(1).replace('"', ''))
      a1 = CurrentCash.count(':')
      b1 = Convert(CurrentCash)
      listCurrentCash = []
      for i in range(0, a1):
          var = b1[i]
          c1 = list(var.split(":"))
          e1, f1 = [c1[j] for j in (0, 1)]
          listCurrentCash.append(f"{round(float(f1), 2):.2f}")
      lastCurrentCash = str(listCurrentCash[0])
      CurrentCash0 = str("current Cash {} ".format(lastCurrentCash))

      CurrentLiabilitiesCash_Factor = "%.2f" % round(
          (float(lastCurrentLiabilities) / float(lastCurrentCash)) * 100, 2)
      CurrentLiabilitiesCash_Factor0 = str(
          " Current Liabilities / Current Cash Factor {}%".format(CurrentLiabilitiesCash_Factor))

      # Total Liabilities/Assets Factor
      StringTotalLiabilities0 = re.search('total-liabilities(.*)common-stock-net', URLHandler(url2))
      StringTotalLiabilities = re.search('div>",(.*)},{', StringTotalLiabilities0.group(0))
      TotalLiabilities = str(StringTotalLiabilities.group(1).replace('"', ''))
      a1 = TotalLiabilities.count(':')
      b1 = Convert(TotalLiabilities)
      listTotalLiabilities = []
      for i in range(0, a1):
          var = b1[i]
          c1 = list(var.split(":"))
          e1, f1 = [c1[j] for j in (0, 1)]
          listTotalLiabilities.append(f"{round(float(f1), 2):.2f}")
      lastTotalLiabilities = str(listTotalLiabilities[0])

      StringTotaAssets0 = re.search('total-assets(.*)total-current-liabilities', URLHandler(url2))
      StringTotaAssets = re.search('div>",(.*)},{', StringTotaAssets0.group(0))
      TotaAssets = str(StringTotaAssets.group(1).replace('"', ''))
      a1 = TotaAssets.count(':')
      b1 = Convert(TotaAssets)
      listTotaAssets = []
      for i in range(0, a1):
          var = b1[i]
          c1 = list(var.split(":"))
          e1, f1 = [c1[j] for j in (0, 1)]
          listTotaAssets.append(f"{round(float(f1), 2):.2f}")
      lastTotaAssets = str(listTotaAssets[0])

      AllLiabilitiesAssets_Factor = "%.2f" % round((float(lastTotalLiabilities) / float(lastTotaAssets)) * 100, 2)
      AllLiabilitiesAssets_Factor0 = str(
          " Total Liabilities / Total Assets Factor {}%".format(AllLiabilitiesAssets_Factor))

      # P/E
      StringPE0 = re.findall('PE ratio as of(.*)</strong>', URLHandler(url3))
      StringPE1 = str(StringPE0[0])
      StringPE = str(StringPE1.replace('<strong>', ''))
      PE = str("P/E Ratio as of {}".format(StringPE))

      # RORE
      if 'common-stock-dividends-paid' in URLHandler(url4):
          StringDividends0 = re.search('common-stock-dividends-paid(.*)}];', URLHandler(url4))
          StringDividends = re.search('/div>"(.*)}', StringDividends0.group(0))
      else:
          StringDividends0 = re.search('Common Stock Dividends Paid(.*)}];', URLHandler(url4))
          StringDividends = re.search('popup_icon(.*)}', StringDividends0.group(0))

      Dividends = str(StringDividends.group(1).replace('"', ''))
      a1 = Dividends.count(':')
      b1 = Convert(Dividends)
      if b1[0] == '': del b1[0]
      listDividends = []
      for i in range(0, a1):
          var = b1[i]
          c1 = list(var.split(":"))
          e1, f1 = [c1[j] for j in (0, 1)]
          if f1 == '':
              listDividends.append(0)
          else:
              listDividends.append(f"{round(float(f1), 2):.2f}")

      RORE1 = "%.2f" % round(100 * (float(listofEPS[0]) - float(listofEPS[1])) / (
              float(listofEPS[0]) + float(listofEPS[1]) - float(listDividends[0]) - float(listDividends[1])), 2)
      RORE2 = "%.2f" % round(100 * (float(listofEPS[1]) - float(listofEPS[2])) / (
              float(listofEPS[1]) + float(listofEPS[2]) - float(listDividends[1]) - float(listDividends[2])), 2)
      RORE3 = "%.2f" % round(100 * (float(listofEPS[2]) - float(listofEPS[3])) / (
              float(listofEPS[2]) + float(listofEPS[3]) - float(listDividends[2]) - float(listDividends[3])), 2)
      RORE4 = "%.2f" % round(100 * (float(listofEPS[3]) - float(listofEPS[4])) / (
              float(listofEPS[3]) + float(listofEPS[4]) - float(listDividends[3]) - float(listDividends[4])), 2)
      RORE5 = "%.2f" % round(100 * (float(listofEPS[4]) - float(listofEPS[5])) / (
              float(listofEPS[4]) + float(listofEPS[5]) - float(listDividends[4]) - float(listDividends[5])), 2)

      RORE10 = str("RORE for last year is {}%".format(RORE1))
      RORE20 = str("RORE for previous year is {}%".format(RORE2))
      RORE30 = str("RORE for 3 years ago is {}%".format(RORE3))
      RORE40 = str("RORE for 4 years ago is {}%".format(RORE4))
      RORE50 = str("RORE for 5 years ago is {}%".format(RORE5))

      # Overpriced
      StringPrice0 = re.findall('content=(.*)&lt;/strong&gt', URLHandler(url5))
      StringPrice = StringPrice0[1].replace('&lt;strong&gt;', '')
      CurrentPrice = re.findall("\d+\.\d+", StringPrice)
      PriceNow = float(CurrentPrice[0])
      PriceNow0 = str("Current Price is {}".format(PriceNow))

      # Price 5 years ago
      soup = BeautifulSoup(URLHandler(url5), 'html.parser')
      stable = soup.find('table')
      header = stable.findAll('th')
      headers = [th.text for th in header]
      cells = []
      rows = stable.findAll('tr')
      for tr in rows:
          # Process the body of the table
          td = tr.findAll('td')
          for t in td:
              a = re.findall('>(.*)<', str(t))
              b = a[0]
              cells.append(b)
      Price5Years = float(cells[36])
      Price5YearsList = str("Prices list {}".format(cells))

      # NPV
      RetainedErnings = []
      for i in range(0, Years):
          a = NBShares * (float(listofEPS[i]) - float(listDividends[i]))
          RetainedErnings.append(f"{round(float(a), 2):.2f}")
      RetainedErnings = [float(i) for i in RetainedErnings]
      NetPresentValue = np.npv(NominalDiscountRate, RetainedErnings)
      NETPRESENT = str("Net present Value {}".format(NetPresentValue))
      # EstimatedPrice
      TotalValueYears = "%.2f" % round(
          np.fv(-AverageInflation, Years, 0, -NetPresentValue) + np.fv(-AverageInflation, Years, 0,
                                                                       -(NBShares * Price5Years)), 2)
      TOTALVALUE = str("Total Value Years {}".format(TotalValueYears))
      EstimatedPrice = "%.2f" % round((float(TotalValueYears) / float(NBShares)), 2)

      Overpriced = "%.2f" % round(100 * (PriceNow / float(EstimatedPrice) - 1), 2)
      OVERPRICED0 = str("Overpriced {}%".format(Overpriced))

      # Overpriced + Cash
      r = ['{}'.format(NetIncome10yGrowth), '{}'.format(NetIncomeGrowthList), '{}'.format(lastEPSstr),
          '{}'.format(EPS), '{}'.format(EPS5yGrowth), '{}'.format(EPS10yGrowth),
           '{}'.format(EPSGrowthList), '{}'.format(CurrentLiabilities0), '{}'.format(CurrentCash0),
           '{}'.format(CurrentLiabilitiesCash_Factor0),
           '{}'.format(PE), '{}'.format(RORE10), '{}'.format(RORE20), '{}'.format(RORE30), '{}'.format(RORE40),
           '{}'.format(RORE50),
           '{}'.format(PriceNow0), '{}'.format(Price5YearsList), '{}'.format(NETPRESENT), '{}'.format(TOTALVALUE),
           '{}'.format(PE), '{}'.format(OVERPRICED0)]
      # '\n'.join('{}'.format(item) for item in r)
      #z = str(r).split(',')
      #r = [('aaaa', NetIncome10yGrowth), ('Years', '5')]
      return render_template("result.html",result = r)

if __name__ == '__main__':
   app.run(debug = True)
