# Bollinger-Band-Keltner-Channel-Strategy
This strategy applies Bollinger Band together with Keltner Channel in order to locate stocks which are about to breakout in a daily basis. Simple moving average is used on Bollinger Band while exponential moving average is applied on Keltner Channel 

# Objective
The objective of this project is to test if Bollinger Band and Keltner Channel can capture some of the breakout of stocks. 

Both of the indicators capture the low volatility of a stock while the Keltner Channel follows the price of a stock more sensitively with an exponential moving average. It is observed that the Keltner Channel crosses over Bollinger Band whenever stocks breakout or start enter an uptrend. 

Thus, this project is to investigate if this strategy really works with several backtests. 

# Findings
By applying the Bollinger Band with Keltner Channel  together with candlestick patterns as well as other measures, the performance is captured by only calculating its successful rate. The strategy is regarded as successful if its price does not fall under its buying price within 5 days.

Since the signal seldom occurs in a daily basis, the strategy takes stocks from the pool of top 100 transaction volume in the US equity market.

Result is shown as below:

![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/alpha.png)

Interestingly, it is found that the strategy successfully capture most of the breakout either before or after the breakout happens. Below are a few examples with various chart patterns drawn.

<!-- Break Previous Top -->

# PYPL
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/PYPL.png)

# CSCO
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/CSCO.png)

# SHOP
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/SHOP.png)

# SQ
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/SQ.png)

# JNJ
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/JNJ.png)

# UNP
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/UNP.png)

# FPL
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/FPL.png)

# UNH
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/UNH.png)

# LLY
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/LLY_top.png)

# ABBV
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/ABBV_top.png)

# ZEN
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/ZEN_top.png)

# GE
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/GE.png)

# QCOM
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/QCOM.png)

# HD
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/HD.png)

# Low
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/Low.png)



# UBER

Signal is generated on 2021-01-14 for UBER
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/UBER_20210114.png)


Signal is generated on 2021-02-09 for UBER again
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/UBER_20210209.png)

# TXN
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/TXN.png)

<!-- Break Price Channel Top -->

# INTC
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/Intel.png)

# TSLA
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/TSLA.png)

# CAT
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/CAT.png)

# ADBE
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/ADBE.png)

# DHR
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/DHR.png)

# MRK
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/MRK.png)



# ABBV
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/ABBV.png)

# LLY
![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/LLY.png)




# Strategy
With the overall success rate over 50% with random stocks during backtest, I added an equal portfolio management strategy and a simple risk management model to this strategy. Also, a trailing stop loss by utilising different moving averages is introduced into the strategy. The result is shown below:

![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/Backtest.png)

In order to avoid overfitting with the fixed 100 equities, another stock universe is chosen, and the result is as following:


Finally, an out-of-sample test is carried out till 2021 with the best performing selection criteria and the result is attached below.

![alt text](https://github.com/kelvonlys/Bollinger-Band-Keltner-Channel-Strategy/blob/main/Out-of-sample%20test.png)


# Conclusion
The alpha signal generated by Bollinger Band and Keltner Channel seems to be effective with a consistent performance of over 50% success rate. A more advanced portfolio, execution and risk model can be introduced to the strategy in the future to make the strategy more competitive.




