from clr import AddReference
AddReference("System")
AddReference("QuantConnect.Algorithm")
AddReference("QuantConnect.Common")

from System import *
from QuantConnect import *
from QuantConnect.Algorithm import *
import numpy as np
from BollKCAlphaModel import BollKeltnerChannelsAlphaModel
from Risk.MaximumDrawdownPercentPerSecurity import MaximumDrawdownPercentPerSecurity
from Risk.TrailingStopRiskManagementModel import TrailingStopRiskManagementModel
from QuantConnect.Data.UniverseSelection import * 
from Selection.FundamentalUniverseSelectionModel import FundamentalUniverseSelectionModel

class BasicTemplateFrameworkAlgorithm(QCAlgorithmFramework):

    def Initialize(self):
        
        # Set requested data resolution
        self.UniverseSettings.Resolution = Resolution.Daily
        # self.SetStartDate(2010, 1, 1)   #Set Start Date
        # self.SetEndDate(2018, 12, 31)    #Set End Date
          
        ####### FORWARD TEST #######  
        # self.SetStartDate(2019, 1, 1)   #Set Start Date
        # self.SetEndDate(2020, 8, 16)    #Set End Date
        
        ####### Out of sample test #######
        self.SetStartDate(2020, 8, 16)   #Set Start Date
        
        self.cash = 20000
        self.riskPercentage = 0.02 
        self.SetCash(self.cash) #Set Strategy Cash
        
        stocks = ["AAPL", "HD", "AMZN", "BAC", "DIS", "T","COST", "GOOGL", \
        "AXP", "MA", "KO", "MCHP", "BA", "CVX", "CRM","MO", "MMM", "JNJ", "ASML", "FISV", "MRK"] #"MRK" "PEP" "BKNG""AXP", "INTC", "MA", "KO", "MCHP", "BA", "CVX", "CRM","MO", "MMM", "JNJ", "ASML", "FISV", "MRK"] #"MRK" "PEP" "BKNG"
        # stocks = ["MSFT", "MCD", "AAPL", "HD", "AMZN", "BAC", "DIS", "T","COST", "GOOGL", "AXP", "QCOM", "INTC", "MA", "KO", "MCHP"] #best +429%
        # stocks = ["INTC"] #JD(2015)  NVDA TXN #S&P500: MMM JNJ VZ(good%) MRK  PEP  
        # NASDAQ  ASML FISV CME(good%) ADP(good%, old good) INTU(good%, old good) BKNG SBUX(good %) ### CHTR TXN TSMC
        symbols = []
        
        self.SetBrokerageModel(BrokerageName.AlphaStreams)
        
        for stock in stocks:
            symbols.append(Symbol.Create(stock, SecurityType.Equity, Market.USA))
        
        self.SetUniverseSelection( ManualUniverseSelectionModel(symbols) )
        # self.SetUniverseSelection(MyUniverseSelectionModel())
        self.SetAlpha(BollKeltnerChannelsAlphaModel(resolution=Resolution.Daily, lookback=250, consolidationPeriod=1))
        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel()) 
        self.SetExecution(ImmediateExecutionModel())
        self.SetRiskManagement(MaximumDrawdownPercentPerSecurity(0.03))
        # self.SetRiskManagement(TrailingStopPerSecurity(0.03))
        
    def OnOrderEvent(self, orderEvent):
        if orderEvent.Status == OrderStatus.Filled:
            # self.Debug("Purchased Stock: {0}".format(orderEvent.Symbol))
            pass
 
# Parameter pass through models        
#https://www.quantconnect.com/forum/discussion/4763/qcalgorithmframework-attribute-to-be-used-in-other-modules-like-alpha-execution-etc/p1
#

class MyUniverseSelectionModel(FundamentalUniverseSelectionModel):

    def __init__(self):
        super().__init__(True, None, None)

    def SelectCoarse(self, algorithm, coarse):
        filtered = [x for x in coarse if x.HasFundamentalData > 0 and x.Price > 0]
        sortedByDollarVolume = sorted(filtered, key=lambda x: x.DollarVolume, reverse=True)
        return [x.Symbol for x in sortedByDollarVolume][:100]

    def SelectFine(self, algorithm, fine):
        return [f.Symbol for f in fine] 
