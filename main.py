from subprocess import call

words = [
"fieljazair#99"]

def try_connect(ssid):
    for word in words:
        connectone(ssid,word)
def connectone(ssid,password):
    setnetwork = "netsh wlan set hostednetwork mode=allow ssid={0} key={1}".format(ssid,password)

    connect = "netsh wlan connect name="+ ssid
    call(setnetwork)

    result = call(connect)
    print result



try_connect("Linksys05289")
