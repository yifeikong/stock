import easyquotation
from pypinyin import lazy_pinyin
from futile.file import read_list_from_csv


def percentile(now, close):
    return "%.2f%%" % ((now - close) / close * 100)


q = easyquotation.use("sina")
stocks = read_list_from_csv("stocks.csv")
stocks = [s[0] for s in stocks]

for k, v in q.stocks(stocks).items():
    print(
        k,
        "".join(lazy_pinyin(v["name"])),
        v["now"],
        percentile(v["now"], v["close"]),
        v["time"],
    )
