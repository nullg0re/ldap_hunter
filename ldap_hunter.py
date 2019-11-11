#!/usr/bin/python
import argparse
from ldap3 import Server, Connection, ALL
from colorama import Fore, Style

def get_args():
	p = argparse.ArgumentParser(description="Recon tool via LDAP Queries")
	p.add_argument('-u','--username',type=str,help='username',required=True)
	p.add_argument('-p','--password',type=str,help='password',required=True)
	p.add_argument('-d','--domain',type=str,help='domain.com',required=True)
	p.add_argument('-t','--target',type=str,help='target domain controller',required=True)
	p.add_argument('--exchange',action='store_true',default=False,help='hunt for exchange servers',required=False)
	p.add_argument('--mssql',action='store_true',default=False,help='hunt for mssql servers',required=False)

	args = p.parse_args()

	return args

def find_exchange(dcstring, conn, args):
	conn.search('cn=Configuration,%s' % dcstring, '(objectCategory=msExchExchangeServer)', attributes = ['adminDisplayName'])

	print(Fore.GREEN+Style.BRIGHT+"[+] Exchange Servers Found:"+Style.RESET_ALL)

	for entry in conn.response:
		try:
			print(Fore.GREEN+"%s.%s" % (entry['attributes']['adminDisplayName'],args.domain) + Style.RESET_ALL)
		except Exception as e:
			continue

def find_mssql(dcstring, conn, args):
	conn.search('%s' % dcstring, '(servicePrincipalName=*mssql*)')

	print(Fore.GREEN+Style.BRIGHT+"[+] MSSQL Servers Found:"+Style.RESET_ALL)

#	print conn.response

	for entry in conn.response:
		try:
			print(Fore.GREEN+"%s.%s" % (entry['dn'].split('CN')[1].strip('=').strip(','),args.domain) +Style.RESET_ALL)
		except Exception as e:
			continue


def main():
	args = get_args()

	if args.exchange == False and args.mssql == False:
		print(Fore.RED+"[!] --exchange or --mssql must be used. Exiting..."+Style.RESET_ALL)
		exit()
	else:
		dcstring = ','.join(['dc=%s' % i for i in args.domain.split('.')])

		server = Server(args.target, get_info=ALL)
		conn = Connection(server, user="%s\\%s" % (args.domain, args.username), password="%s" % args.password, authentication="NTLM", auto_bind=True)

		if args.exchange:
			find_exchange(dcstring, conn, args)
		elif args.mssql:
			find_mssql(dcstring, conn, args)


if __name__ == '__main__':
	main()
