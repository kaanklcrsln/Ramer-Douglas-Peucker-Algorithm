import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from rdp import rdp
import matplotlib.dates as mdates

stock = 'AMZN'
start = '2020-11-01'

df = yf.download(stock, start=start)

nfx = [] 
nfy = []  

for index, row in df.iterrows():
    nfx.append(mdates.date2num(index)) 
    nfy.append(row['Close'])

nfx = np.array(nfx)
nfy = np.array(nfy)

rdpp = rdp(np.column_stack((nfx, nfy)), epsilon=0.2)

nfx_datetime = [mdates.num2date(ts) for ts in rdpp[:, 0]]

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Close'], label="Original Data")
plt.plot(nfx_datetime, rdpp[:, 1], label="RDP Simplified Data")
plt.legend()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30))
plt.xticks(rotation=45)
plt.show()
