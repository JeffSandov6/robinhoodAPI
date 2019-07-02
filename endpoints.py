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

  def stock_market_data(self, stock_id):
    return self.robinhood_url + "marketdata/fundamentals/{_stockid}/".format(_stockid = stock_id)

  def account_info(self):
    return self.robinhood_url + "accounts/"

  def portfolio(self, account_number):
    return self.robinhood_url + "accounts/{_accountnumber}/".format(_accountnumber = account_number) + "portfolio/"

  def positions(self, account_number):
    return self.robinhood_url + "accounts/{_accountnumber}/".format(_accountnumber = account_number) + "positions/"