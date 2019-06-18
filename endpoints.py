class Endpoints:
  robinhood_url = "https://api.robinhood.com/"

  def login_endpoint(self):
    return self.robinhood_url + "oauth2/token/"
