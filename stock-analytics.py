import yfinance as yf

class Stock:
    def __init__(self, name :str,per :int,avg :int):
        self.name = name               
        self.per = per
        self.avg = avg
        
    def fetch_data(self):    
        self.data = yf.download(self.name, period=f"{self.per}mo")

    def sma_data(self):    
        self.sma_list=(self.data[:self.avg]["Close"].values)
        self.sma = sum(self.sma_list)/self.avg

    def ema_data(self):
        self.prev = self.sma
        self.rolling_ema = []
        alpha = 2/(self.avg+1)
        for i in range(0,len(self.data)-self.avg):
            current = self.data["Close"].iloc[self.avg+i].values
            self.ema = (current * alpha) + (self.prev * (1 - alpha))
            self.prev = self.ema
            self.rolling_ema.append(self.ema)

        
    def rsi_data(self):    
        rsi_list =(self.data[:14]["Close"].values)
        gain = []
        loss = []
        for i in range(len(rsi_list)):
            if(i == 0):
                continue
            diff=rsi_list[i]-rsi_list[i-1]
            if(diff > 0):
                gain.append(diff)
            else:
                loss.append(abs(diff))
        if(len(gain) != 0):
            avggain = sum(gain)/len(gain)
        else:
            avggain = 0
        if(len(loss) != 0):
            avgloss = sum(loss)/len(loss)
        else:
            avgloss = 0
        if(avgloss != 0):
            rs = avggain/avgloss
            self.rsa = 100 - (100/(1 + rs))
        elif(avgloss == 0 and avggain == 0):
            self.rsa = 50
        else:
            self.rsa = 100
        

    def summary(self):
        print(f"the stock you entered is: {self.name}")
        print(f"the data for the duration of {self.per} months is : \n{self.data}")
        print(f"the sma of {self.name} for {self.avg} days is: {self.sma}")
        print(f"the list of rolling ema would be : \n{self.rolling_ema}")
        print(f"the 14 days rsi of the stock {self.name} is : {self.rsa}")


s1=input("enter the symbol of the stock you want the data for:")
time=int(input("enter the time duration in months "))
avg=int(input("enter the number of days you want the sma and ema for"))
stock1 = Stock(s1,time,avg)
stock1.fetch_data()
stock1.sma_data()
stock1.ema_data()
stock1.rsi_data()
stock1.summary()
                  

