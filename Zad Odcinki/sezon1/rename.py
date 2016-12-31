# Michal Wierzchowski -- Rename 1.0

import os, re

try:
    tab =  os.listdir('.')
    p = re.compile(r's01e[0-9][0-9]')
    for ep in tab:
        find = p.findall(ep)
        if len(find) > 0:
            s = find[0]
            x = s[-2]+s[-1]
            x =  int(x)
            os.rename(ep, 'Odcinek'+str(x)+'.avi')
except:
    import sys
    print sys.exc_info()[0]
    import traceback
    print traceback.format_exc()

finally:
    print "Press Enter to continue ..." 
    raw_input()     
