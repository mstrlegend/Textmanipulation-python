import re
# {"certPinnedAppList":[],"status":"success","steering_config_name":"Netskope_test_group"}
# Goal is to get the appname and app domains
"""
while True:
    with open("Text-File.txt", "r") as r, open("Output", "a+") as f:
        print(re.findall("{(.*)},", r))
"""

x = '{"action":1,"appName":"Amazon CloudDrive","app_domains":["drive.amazon.com","cdws.us-east-1.amazonaws.com","cdws.us-west-2.amazonaws.com","drive.amazonaws.com"],"mode":"tunnel","processName":"AmazonCloudDrive.exe","rowID":"151","tunnel_domains":["drive.amazonaws.com","cdws.us-east-1.amazonaws.com","cdws.us-west-2.amazonaws.com","drive.amazon.com"]}'

action_an = str(re.findall("{(.*)}", x))
appName = str(re.search(r"\"appName\":\"(.*)\",\"app_domains\"", action_an).groups(1)).strip("(',')")
print(appName)

appDomains = str(re.search(r"\"app_domains\":\[(.*\")],\"mode\"", action_an).groups(1)).strip("(',')")
print(appDomains)