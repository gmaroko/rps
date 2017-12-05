#Random Python Scripts
#(c) 2017 Maroko Gideon
#www.gmaroko.me
#marokogideon@gmail.com
#Dec '17

from twilio.rest import Client
def main():
    account_sid,auth_token = input("Account sid >"), input("Auth. token >")
    _client = Client(account_sid, auth_token)
    account_num, client_no= input("Twilio numbe>"), input("Send to >")
    
    message = _client.messages.create(\
        body = "{}".format(input("Message >")),\
        from_ = account_num, to = client)    

if __name__ == "__main__":
    main()
