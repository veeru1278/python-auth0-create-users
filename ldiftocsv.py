#!/usr/bin/python
#yum install python-psycopg2
# Python 2.7 or more

import ldap
import csv
import psycopg2



def ldif_dict(host, dn, pw, base_dn, filter, attrs):
	con = ldap.initialize( host )
	# Bind to the server
	con.simple_bind_s( dn, pw )
	res = con.search_s( base_dn, ldap.SCOPE_SUBTREE, filter, attrs )
	# Close the connection
	con.unbind()
	#returned dictionary
	return res


def csv_postgres(res):

	securityQueNum=len(res[0][1]['securityQuestionAnswer'])
	with open('eggs.csv', 'wb') as csvfile:
	    mywriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	    for i in res:
	        for j in range(securityQueNum):
	            mywriter.writerow([i[1]['uid'][0],i[1]['cn'][0], i[1]['sn'][0], i[1]['userPassword'][0], i[1]['securityQuestionAnswer'][j]])
	conn = psycopg2.connect("dbname='POSTGRES_DB_NAME' user='POSTGRES_USER' host='POSTGRES_HOSTNAME'")
	cur=conn.cursor()
	f = open(r'/tmp/eggs.csv', 'r')
	cur.copy_from(f, 'migration', sep=",")
	cur.execute("select * from migration")
	conn.commit()
	conn.close()
	f.close()



def main():
	host='ldap://<HOSTNAME or IP>:<LDAP_PORT>'
	dn='YOUR_DN'
	pw='LDAP_PASSWORD'
	base_dn='BASE_DN'
	filter='(objectclass=person)'
	attrs=['uid','cn', 'sn', 'securityQuestionAnswer', 'userPassword']
	# This function converts ldif data in python dictionay resource
	res=ldif_dict(host, dn, pw, base_dn, filter, attrs)
        # This function Parse the resource (res) and convert into csv and transfre data to postgres
	csv_postgres(res)




if __name__=='__main__':
	main()
