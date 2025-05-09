class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
def stock_purchase_history():
    stock_list = [
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]

    stock_dict = {}
    for stock in stock_list:
        stock_dict[stock.get_symbol()] = stock

    print(f"{'Symbol':<10} {'Company Name'}")
    print("-" * 30)
    for symbol, stock in stock_dict.items():
        print(f"{symbol:<10} {stock.get_company_name()}")