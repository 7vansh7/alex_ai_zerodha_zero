import yfinance as yf
from api.config import genai,safety_settings

stock = yf.Ticker("TCS.NS")
# print(stock.info)

model2 = genai.GenerativeModel('gemini-1.5-flash',safety_settings=safety_settings)
chat2 = model2.start_chat(history=[])
res = chat2.send_message("Do you know the ticker for tata steel nse ").text
print(res)

