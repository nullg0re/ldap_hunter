# ldap_hunter
Search for sensitive targets via LDAP.  (Currently Exchange Servers and MSSQL Servers... Will be adding to this)

# Help Menu
```
./ldap_hunter.py -h
usage: ldap_hunter.py [-h] -u USERNAME -p PASSWORD -d DOMAIN -t TARGET
                      [--exchange] [--mssql]

Recon tool via LDAP Queries

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        username
  -p PASSWORD, --password PASSWORD
                        password
  -d DOMAIN, --domain DOMAIN
                        domain.com
  -t TARGET, --target TARGET
                        target domain controller
  --exchange            hunt for exchange servers
  --mssql               hunt for mssql servers
```
# Example Usage:
```
/ldap_hunter.py -u testuser1 -p Summer2019 -d tgore.com -t 192.168.204.132 --exchange
[+] Exchange Servers Found:
EXCHANGE.tgore.com

./ldap_hunter.py -u testuser1 -p Summer2019 -d tgore.com -t 192.168.204.132 --mssql
[+] MSSQL Servers Found:
MSSQL.tgore.com
```
