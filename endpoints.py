class Endpoints:
  robinhood_url = "https://api.robinhood.com/"

  def login_endpoint(self):
    return self.robinhood_url + "oauth2/token/"

  def transfers(self):
    return self.robinhood_url + "ach/transfers/"

  def dividends(self):
    return self.robinhood_url + "dividends/"