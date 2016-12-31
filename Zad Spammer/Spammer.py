# Michal Wierzchowski -- Spammer 1.0

import urllib2, re

links = ['http://www.wz.uw.edu.pl/pracownicy',
         'http://filozofia.amu.edu.pl/dyzury/',
         'http://www.ncbr.gov.pl/lista-pracownikow-ncbr/',
         'http://www.fizyka.umk.pl/fizyka/?q=node/458'
         ]
emails = []
a_emails = []
p = re.compile(r'[a-zA-Z0-9-_.]+@[a-z0-9-.]+.[a-z0-9]{1,6}')
try:
    for link in links:    
        response = urllib2.urlopen(link)
        ps = response.read()
        result = p.findall(ps)
        emails = emails + result
        
    plik = open('mails.txt', 'a')

    plik.write('Pobrano: ' + str(len(emails))+' emaili:\n\n')
    for mail in emails:
        x=mail.index('@')
        a_mail = mail[0] + '...' + mail[x-1] + mail[x: ]
        a_emails.append(a_mail)
        plik.write(a_mail+'\n')
except:
    import sys
    print sys.exc_info()[0]
    import traceback
    print traceback.format_exc()
     
finally:
    plik.close()
    print "Press Enter to continue ..." 
    raw_input()
