<h3>This repo has two utility<h3> 

1. auth0_create_user.py which create user in auth0 account using auth0 management API

   To run this utility :
      * Create your own payload and replace the existing one, payload should have createUser scope
      * Replace domain and CLIENT_SECRET_KEY' with your credentials.
      

2. ldiftocsv.py is used to pull data from LDAP Directory server and convert into CSV then import CSV to Postgres DB
   
   To run this utility:
      * Replace HOSTNAME , LDAP_PORT , YOUR_DN , BASE_DN with LDAP credentials
      * You can also edit attrs list 
      * To connect with Postgres DB replace 'POSTGRES_DB_NAME' 'POSTGRES_USER' and 'POSTGRES_HOSTNAME' with postgres credntials 
        For non sudo users postgres password require.
