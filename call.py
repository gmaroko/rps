#Random Python Scripts
#(c) 2017 Maroko Gideon
#www.gmaroko.me
#marokogideon@gmail.com
#Dec 2017

from twilio.rest import Client
def main():
    url_voice = ""
    account_sid,auth_token = input("Account sid >"), input("Auth. token >")
    _client = Client(account_sid, auth_token)
    account_num, client_no= input("Twilio numbe>"), input("Number to call >")
    
    call = _client.calls.create(from_ = account_num, to = client, url=url_voice)
    

if __name__ == "__main__":
    main()
