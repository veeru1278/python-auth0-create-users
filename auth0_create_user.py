#pip install auth0-python
#pip install pyjwt
# Python 2.7 or more require

from auth0.v2.management import Auth0
import base64
import jwt



def create_payload(domain):	
	#Use your own payload
	payload={
	 "aud": "n3P1N0hxICmzN259aCC6j8IvFmi80oEy",
	 "scopes":{ 
	   "users": {
	     "actions": [
	       "create",
	       "read"
	     ]
	   },
	   "connections": {
	     "actions": [
	       "read"
	     ]
	   }
	 },
	 "iat": 1477312421,
	 "jti": "74aa696bf46ba1a36c744610ae033df5"
	}
        return payload


def create_jwt(payload, secret):
	dsecret=base64.urlsafe_b64decode(secret)
	token=jwt.encode(payload, dsecret , algorithm='HS256')
	return token


def create_user(token, domain):
    auth0 = Auth0(domain, token)
    print "Provide following params to create a user:"
    print ""
    print "Enter connection name: "
    connection_name=raw_input()
    print ""
    print "Enter email: "
    email=raw_input()
    print ""
    print "Enter user Name:"
    username=raw_input()
    print ""
    print "Enter password:"
    password=raw_input()
    print ""

    create_user_payload={
      "connection": connection_name,
      "email": email,
      "password": password
    }
    auth0.users.create(create_user_payload)
    print auth0.users.list()



def main():
    domain='sso1.auth0.com'
    secret='CLIENT_SECRET_KEY'
    payload=create_payload(domain)
    token=create_jwt(payload, secret)
    create_user(token, domain)


if __name__=='__main__':
    main()

