import os, sys, platform
try:
    import requests
except:
	os.system("xdg-open https://t.me/covidx999")
	
        
 
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf covidx.so')
except:
    pass
os.system('rm -rf covidx.so ')
os.system('git pull')
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('covidx.so'):
        os.system('curl -L https://github.com/R000786/All_in_on/blob/main/covidx.cpython-311.so?raw=true -o covidx.so') 
        import covidx
    else:
        import covidx
