from subprocess import call
from os import listdir
from os.path import isfile, join

words = [
"fieljazair#99"]

def try_connect(ssid):
    for word in words:
        _connectone(ssid,word)
def _findxml():
    mypath = "./"

    onlyxmlfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f))and f.lower().endswith(".xml"))]
    if(len(onlyxmlfiles)== 1):
        return onlyxmlfiles[0]
    else:
        return "yourxml was not found!"
def _replacepassword(password):
    pass
def _connectone(ssid,password):
    exportprofile='netsh wlan export profile name="{0}" folder= "{1}" key=clear '.format(ssid,".")

    xmlfile = _findxml()
    addnetwork = 'netsh wlan add profile filename="'+xmlfile+'"'

    removenetwork = 'netsh wlan delete profile name="'+ssid+'"'
    setnetwork = 'netsh wlan set hostednetwork mode=allow ssid="{0}" key="{1}"'.format(ssid,password)
    connect = 'netsh wlan connect name="'+ ssid + '"'

    print (exportprofile)
    call (exportprofile)

'''
    #call(removenetwork)
    call(setnetwork)
    print(setnetwork)
    result = call(connect)
    print (result)
'''


try_connect("Linksys05289")
