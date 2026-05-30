import yfinance as yf

class Stock:
    def __init__(self, name,per,avg :int):
        self.name = name               
        self.per = per
        self.avg = avg
        self.data = yf.download(self.name, period=f"{self.per}mo")
        list=(self.data[:self.avg]["Close"].values)
        self.sma = sum(list)/self.avg 
        self.prev = (sum(list[:-1]))/(self.avg-1)
        alpha=2/(self.avg + 1)
        current = self.data["Close"].iloc[self.avg].values
        
        self.ema = (current * alpha) + (self.prev * (1 - alpha))
        list1 =(self.data[:14]["Close"].values)
        gain = []
        loss = []
        for i in range(len(list1)):
            if(i == 0):
                continue
            diff=list1[i]-list1[i-1]
            if(diff > 0):
                gain.append(diff)
            else:
                loss.append(abs(diff))
        if(len(gain) != 0):
            avggain = sum(gain)/len(gain)
        else:
            print("no gain")
            avggain = 0
        if(len(loss) != 0):
            avgloss = sum(loss)/len(loss)
        else:
            print("no loss")
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
        print(f"the ema would be : {self.ema}")
        print(f"the 14 days rsi of the stock {self.name} is : {self.rsa}")
s1=input("enter the symbol of the stock you want the data for:")
time=int(input("enter the time duration in months "))
avg=int(input("enter the number of days you want the sma and ema for"))
stock1 = Stock(s1,time,avg)
stock1.summary()
                  

