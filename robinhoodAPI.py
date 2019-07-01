import requests
import getpass
import json

from endpoints import Endpoints




#BELOW ARE THE REQUEST HEADERS
"""
  Content-Type: application/json
  Origin: https://robinhood.com
  Referer: https://robinhood.com/
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36
  X-Robinhood-API-Version: 1.265.0
"""


#jeffrysandoval24@gmail.com


class RobinhoodAPI():
  
  CLIENT_ID = "c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS" #constant
  username = None
  password = None
  session = None
  access_token = None  #the auth token
  refresh_token = None 
  #to find this device token, log out robinhood on your browser,
  #inspect, go to network, and where it says filter, type token
  #log in to robinhood and click on token, then go down to 
  #request payload, where you'll see the device token
  DEVICE_TOKEN = "bd16f778-5814-4f14-9e5c-e7b053584529"

  endpoint_manager = Endpoints()

  def __init__(self):
    self.session = requests.Session()

    self.session.headers = {
      "Accept": "*/*", #accept any type
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "en-US,en;q=0.9",
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
      "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
      "X-Robinhood-API-Version": "1.265.0",
      "Connection": "keep-alive"
    }
    
    print("input your login credentials below")
    is_logged_in = self.login()

    while(is_logged_in == False):
      print("incorrect credentials, try again!")
      is_logged_in = self.login()

    print("Login succesful")


  #as of now, we aren't doing any checking for the case that the user has 2FA enabled, but maybe later
  def login(self):
    self.username = input("Username: ")
    # self.password = input("Password: ")
    self.password = getpass.getpass()

    login_payload = {  #checked the auth token request payload content for appropriate fields
      "grant_type": "password",
      "scope": "internal",
      "client_id": self.CLIENT_ID,
      "expires_in": 86400,
      "device_token": self.DEVICE_TOKEN,
      "password": self.password,
      "username": self.username
    }

    response = self.session.post(self.endpoint_manager.login_endpoint(), data=login_payload)
    response_data = response.json()

    if(response.status_code != 200): #error checking for correct credentials
      return False


    if 'access_token' in response_data.keys() and 'refresh_token' in response_data.keys():
      self.access_token = response_data['access_token']
      self.refresh_token = response_data['refresh_token']
      self.session.headers['Authorization'] = 'Bearer ' + self.access_token
      return True
    
    return False


  def pretty_print_response(self, json_response):
    print(json.dumps(json_response, indent=4))


  ### GETTING USER DATA ###

  def get_transfer_history(self):
    response = self.session.get(self.endpoint_manager.transfers(), timeout=15)
    # response.raise_for_status()

    response_data = response.json()

    transfer_history = response_data['results']

    self.pretty_print_response(transfer_history)


  def get_dividends(self):
    response = self.session.get(self.endpoint_manager.dividends(), timeout=15)

    response_data = response.json()

    dividends_history = response_data['results']
    
    self.pretty_print_response(dividends_history)


  ### GET ROBINHOOD DATA ###

  

obj = RobinhoodAPI()

print(obj.get_transfer_history())
# print(obj.get_dividends())
