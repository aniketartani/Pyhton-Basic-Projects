##OTP sender using python

import random
from twilio.rest import Client
otp=random.randint(1000,9999)
account_sid = '' ##Please enter ur aacount_sid id givien by twilio
auth_token = ''   ##Please enter your auth_token given by twilio
Client = Client(account_sid,auth_token)
message = Client.messages.create(
            body=('Hello shri sir:- '+str(otp)),
            from_ = 'twillo phone number', ##Please enter your virtual number given to you by twilio
            to = '+91 '  ##Please enter targets phone number here
)

"""
Explanation:-
1.We are gonna use two library in this code random,twilio
2.so first for generating a random otp we are gonna use randint function of random value which will give us
any value between a given range and we will store that value in variable named otp
3.Now for sending otp we will be using a type of API so we need to create a account on twilio link:-
3.Now for sending otp we will be using a type of API so we need to create a account on twilio link:-
####LINK:- https://www.twilio.com/try-twilio
4.After creating a account on above link we will get a account_sid id and auth_token on our id
5.after that we need to use free trial to get a number to sms the otp which we can get using the free trial of API
6.Next to it  we will be using client function described in twilio library which will need two argument account_sid and auth_token
7.After setting up the client with our user id and password we call function messages.create in twilio module which will take 3 argument
    a. Body in which we will be entering our message
    b.From_ in which we will be giving the number given by twilio so that it can send msg using that otp
    c.to which will be tacking the target phone number(where we need to send message)
"""
##Thanks For viewing contributed by:- Hemang Jiwnnani
