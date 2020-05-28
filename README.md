# Investing 3.0

Through this app you  will be able to apply some of the basic Value Investing formulas for most of the companies listed on https://www.macrotrends.net/
You can run it on your PC by installing Python 3.8 and the dependencies or simply deploy it as an app on Google App Engine on GCP.

# It Calculates:
* 5 Years Net Income Growth Rate 
* 10 Years Net Income Growth Rate 
* 5 Years EPS Growth Rate 
* 10 Years EPS Growth Rate 
* Current Liabilities / Current Cash Factor 
* Total Liabilities / Total Assets Factor 
* RORE for last 5 years
* Overpriced percentage

# Explaining the Current Liabilities / Current Cash Factor:
* How much _Current Liabilities_ represent from the _Current Cash_
* Inspired by _One Up On Wall Street: How to Use What You Already Know to Make Money in the Market by Peter Lynch, John Rothchild_

# Explaining the Total Liabilities / Total Assets Factor
* How much _Total Liabilities_ represent from the _Total Assets_
* Inspired by _One Up On Wall Street: How to Use What You Already Know to Make Money in the Market by Peter Lynch, John Rothchild_


# Explaining the Overpriced formula:
This formula was developed by myself in order to asses if the current price is corelated with the earnings of the company in the last five years.
Components:
* _Price5Years_ - Price 5 years ago
* _Investment_ = _NBShares_ * _Price5Years_
* _RetainedErnings_ = List of Retained earnings for the past 5 years
* _NetPresentValue_ is the NPV of Earnings calculated 5 years ago if all the estimated earnings and the estimating earnings were correct
* _TotalValueYears_ (estimated value gained in the 5 years) = Future Value (-_AverageInflation_, _NbofYears_, 0, -_NetPresentValue_) + * Future Value (-_AverageInflation_, _NbofYears_, 0, -_Investment_)
* _EstimatedPrice_ = _TotalValueYear_s / _NBShares_
* _Overpriced_ = (_PriceNow_ / _EstimatedPrice_) %

## Example of input:
* Base Link: https://www.macrotrends.net/stocks/charts/GOOGL/alphabet/
* Years: 5
* NB of Shares: 10
* Real Discount Rate: 0.05 (to be read as 5%)
* Average Inflation: 0.03 (to be read as 3%)

## Example of output:
* Nominal Discount Rate is 0.08%
* 5 Years Net Income Growth Rate 117.00%
* 10 Years Net Income Growth Rate 303.80%
* List of Net Income growth rates ['11.74', '142.74', '-34.99', '23.08', '11.96', '11.02', '18.59', '10.27', '14.49', '30.44', '54.25', '0.55', '36.60', '110.01']
* Last EPS 49.16
* List of yearly EPS ['49.16', '43.70', '18.00', '27.85', '22.84', '20.57', '18.79', '16.16', '14.88', '13.15', '10.21', '6.66', '6.64', '4.97', '2.51']
* 5 Years EPS Growth Rate 115.24%
* 10 Years EPS Growth Rate 273.84%
* List of EPS growth rates ['546.00', '2570.00', '-985.00', '501.00', '227.00', '178.00', '263.00', '128.00', '173.00', '294.00', '355.00', '2.00', '167.00', '246.00']
* current Liabilities 45221.00000
* current Cash 119675.00000
* Current Liabilities / Current Cash Factor 37.79%
* Total Liabilities / Total Assets Factor 26.99%
* P/E Ratio as of May 27, 2020 is 28.69
* RORE for last year is 5.88%
* RORE for previous year is 41.65%
* RORE for 3 years ago is -21.48%
* RORE for 4 years ago is 9.88%
* RORE for 5 years ago is 5.23%
* ROE quarterly was ['17.43%', '17.79%', '17.44%', '19.22%', '16.16%', '18.34%', '11.64%', '10.31%', '10.76%', '8.40%', '14.26%', '13.66%', '15.16%', '14.85%', '15.08%', '14.74%', '14.00%', '13.86%', '14.08%', '13.48%', '13.96%', '14.49%', '13.63%', '14.49%', '15.07%', '15.69%', '16.09%', '15.83%', '15.99%', '16.14%', '16.72%', '18.56%', '19.11%', '18.22%', '18.97%', '18.94%', '18.66%', '20.20%', '20.06%', '19.94%', '20.21%', '19.88%', '15.98%', '15.64%', '15.58%', '15.96%', '20.12%', '20.56%', '20.56%', '20.56%', '21.17%', '21.25%', '22.08%', '22.36%', '20.40%', '19.76%', '20.83%', '22.90%']%
* ROA quarterly was ['12.91%', '13.19%', '13.07%', '14.53%', '12.29%', '14.08%', '8.97%', '8.10%', '8.62%', '6.86%', '11.87%', '11.40%', '12.65%', '12.34%', '12.47%', '12.08%', '11.39%', '11.23%', '11.36%', '10.82%', '11.14%', '11.47%', '10.72%', '11.42%', '11.84%', '12.31%', '12.53%', '12.20%', '12.22%', '12.39%', '12.97%', '14.58%', '15.27%', '14.62%', '15.21%', '15.28%', '15.23%', '16.83%', '17.18%', '17.52%', '18.06%', '17.76%', '14.28%', '13.96%', '13.87%', '14.17%', '17.89%', '18.32%', '18.46%', '18.66%', '19.35%', '19.53%', '20.34%', '20.56%', '18.72%', '18.20%', '19.01%', '20.86%']%
* ROI quarterly was ['16.76%', '16.58%', '16.77%', '17.25%', '14.78%', '16.04%', '16.34%', '16.14%', '17.17%', '16.93%', '16.60%', '15.88%', '17.82%', '17.68%', '17.42%', '17.26%', '16.87%', '16.61%', '16.30%', '16.00%', '16.03%', '16.37%', '17.15%', '17.97%', '17.99%', '18.44%', '19.35%', '18.91%', '19.45%', '19.90%', '19.46%', '20.99%', '21.52%', '27.01%', '39.78%', '77.89%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%', 'inf%']%
* Current Price is 1420.28
* [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004]
* [1191.2169, 1122.0436, 939.7734, 763.2142, 619.9836, 713.9654, 884.2413, 642.8165, 568.9741, 535.623, 439.689, 464.852, 538.7504, 411.1921, 277.7611, 151.8013]
* Net present Value 1439.513714786778
* Total Value Years 7367.22
* P/E Ratio as of May 27, 2020 is 28.69
* Overpriced 92.78%

**Disclamer: Past performance is not necessarily indicative of future results. All investments carry risk and all investment decisions of an individual remain the responsibility of that individual. There is no guarantee that systems, indicators, or signals will result in profits or that they will not result in losses. All investors are advised to fully understand all risks associated with any kind of investing they choose to do.**
  
