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
