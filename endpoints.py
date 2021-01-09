class Endpoints:
  robinhood_url = "https://api.robinhood.com/"

  def login_endpoint(self):
    return self.robinhood_url + "oauth2/token/"

  def transfers(self):
    return self.robinhood_url + "ach/transfers/"

  def dividends(self):
    return self.robinhood_url + "dividends/"

  def top_movers(self):
    return self.robinhood_url + "midlands/tags/tag/top-movers/"

  def instruments(self):
    return self.robinhood_url + "instruments/"

  def stock_data(self, stock_id):
    return self.robinhood_url + "marketdata/fundamentals/{_stockid}/".format(_stockid = stock_id)

  def stock_news(self, stock_id):
    return self.robinhood_url + "midlands/news/{_stockid}/".format(_stockid = stock_id)

  def stock_ratings(self, stock_id):
    return self.robinhood_url + "midlands/ratings/{_stockid}/".format(_stockid = stock_id)

  def account_info(self):
    return self.robinhood_url + "accounts/"

  def portfolio(self, account_number):
    return self.robinhood_url + "accounts/{_accountnumber}/".format(_accountnumber = account_number) + "portfolio/"
    # return self.robinhood_url + "portfolios/" #this does the same thing as above
    
  def positions(self, account_number):
    # return self.robinhood_url + "accounts/{_accountnumber}/".format(_accountnumber = account_number) + "positions/"
    return self.robinhood_url + "positions/?nonzero=true"

  def orders(self):
    return self.robinhood_url + "orders/"
  
  
  