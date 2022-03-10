from dataclasses import dataclass

__DIGITS__ = 4


@dataclass
class OHLCV:
    time: int
    open: float
    high: float
    low: float
    close: float
    volume: float


@dataclass
class LSTMDataFormat:
    bpx1: float  # open - close positive variation index
    bpx2: float  # open - close negative variation index
    div: float  # open - close exponent
    hc: float  # high - close variation
    dhc: float  # high - close exponent
    cl: float  # close - low variation
    dcl: float  # close - low exponent


class OHLCVDerivate:
    pipsAvg: float
    LSTMDataFormatBars: list = []

    def __init__(self, ohlcvList: list):
        self.pipsAvg = self.calculatePipsAverage(ohlcvList=ohlcvList)
        for ohlcv in ohlcvList:
            bpx = (ohlcv.open - ohlcv.close) / self.pipsAvg / 2 + 0.5
            hc = (ohlcv.high - ohlcv.close) / self.pipsAvg
            cl = (ohlcv.close - ohlcv.low) / self.pipsAvg
            div = 0
            dhc = 0
            dcl = 0

            if bpx > 1:
                div = 1 - (1 / bpx)
                bpx = 1
            if bpx < 0:
                div = 1 - (1 / (1 - bpx))
                bpx = 0
            bpx1 = bpx * 2 - 1 if bpx > 0.5 else 0
            bpx2 = 1 - bpx * 2 if bpx < 0.5 else 0

            if not hc:
                hc = 0
            if hc > 1:
                dhc = 1 - (1 / hc)
                hc = 1
            if hc < 0:
                dhc = 1 - (1 / (1 - hc))
                hc = 0

            if not cl:
                cl = 0
            if cl > 1:
                dcl = 1 - (1 / cl)
                cl = 1
            if cl < 0:
                dcl = 1 - (1 / (1 - cl))
                cl = 0
            LSTMDataFormatBar = LSTMDataFormat(
                bpx1=bpx1, bpx2=bpx2, div=div, hc=hc, dhc=dhc, cl=cl, dcl=dcl
            )
            self.LSTMDataFormatBars.append(LSTMDataFormatBar)

    def calculatePipsAverage(self, ohlcvList: list):
        sum_delta_hl = 0
        print(ohlcvList)
        for ohlcv in ohlcvList:
            delta_hl = ohlcv.high - ohlcv.low
            sum_delta_hl += delta_hl
        return sum_delta_hl / len(ohlcvList) * 10 ** __DIGITS__

    def getLSTMBars(self) -> list:
        return self.LSTMDataFormatBars
