import requests
r=requests.get("https://financialmodelingprep.com/api/v3/financials/income-statement/AAPL")
print(r.text)