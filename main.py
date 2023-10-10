# {"certPinnedAppList":[],"status":"success","steering_config_name":"Netskope_test_group"}
# Goal is to get the appname and app domains

# The following are dictionary options: 'action' 'appName' 'app_domains' 'mode' 'processName' 'rowID' 'tunnel_domains'

# Tunnel mode bypasses proxy but processes the traffic on the Netskope server, direct mode processes it locally
import re
def read_file():
    with open("nsbypass.json", "r") as r:
        index = 0
        output = ""
        x = eval(r.read())
        for i in range(len(x)):
            z = x[index]
            if z['app_domains'] == ['*']:
                z['app_domains'] = "No Domains"
            if z['tunnel_domains'] == [] or ['*']:
                z['tunnel_domains'] = "No tunnel domains"
            output += f"{z['mode']}: {z['appName']} {z['processName']}\n"
            index += 1
    r.close
    with open("Output.txt", 'w') as w:
        w.write("Netskope_test_group:\n\n" + "Mode | App Name | Process Name\n" + output)
    w.close
    return "Output has been written to: 'Output.txt'"
    

print(read_file())

with open("Output.txt", "r") as r:
    for line in r.readlines():
        if bool(re.search("^tunnel", line)) is True:
            print(line, end="")

