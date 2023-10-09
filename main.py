import re
# {"certPinnedAppList":[],"status":"success","steering_config_name":"Netskope_test_group"}
# Goal is to get the appname and app domains
"""
with open("Text-File.txt", "r") as r:
    while True:
        action_an = str(re.findall("{(.*)},", r.read()))
        appName = str(re.search(r"\"appName\":\"(.*)\",\"app_domains\"", action_an).groups(1)).strip("(',')")
        print(appName)
"""

x = '{"action":1,"appName":"Amazon CloudDrive","app_domains":["drive.amazon.com","cdws.us-east-1.amazonaws.com","cdws.us-west-2.amazonaws.com","drive.amazonaws.com"],"mode":"tunnel","processName":"AmazonCloudDrive.exe","rowID":"151","tunnel_domains":["drive.amazonaws.com","cdws.us-east-1.amazonaws.com","cdws.us-west-2.amazonaws.com","drive.amazon.com"]},{"action":1,"appName":"[NTG_NoInternet_Apps_Bypass]","app_domains":["*"],"isRegex":"false","mode":"direct","processName":"Bitsadmin.exe","rowID":"custom_11","tunnel_domains":[]},{"action":1,"appName":"[NTG_NoInternet_Apps_Bypass]","app_domains":["*"],"isRegex":"false","mode":"direct","processName":"CertOC.exe","rowID":"custom_11","tunnel_domains":[]},{"action":1,"appName":"[NTG_NoInternet_Apps_Bypass]","app_domains":["*"],"isRegex":"false","mode":"direct","processName":"CertReq.exe","rowID":"custom_11","tunnel_domains":[]},{"action":1,"appName":"[NTG_NoInternet_Apps_Bypass]","app_domains":["*"],"isRegex":"false","mode":"direct","processName":"Certutil.exe","rowID":"custom_11","tunnel_domains":[]},{"action":1,"appName":"[NTG_NoInternet_Apps_Bypass]","app_domains":["*"],"isRegex":"false","mode":"direct","processName":"Cmd.exe","rowID":"custom_11","tunnel_domains":[]},'

action_an = str(re.findall("{(.*)}", x)).split()
appName = str(re.search(r"\"appName\":\"(.*)\",\"app_domains\"", action_an).groups(1))
print(appName + "\n")

appDomains = str(re.search(r"\"app_domains\":\[(.*\")],\"mode\"", action_an).groups(1))
print(appDomains + "\n")
