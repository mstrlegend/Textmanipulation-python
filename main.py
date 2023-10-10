# {"certPinnedAppList":[*all configs are stored here*],"status":"success","steering_config_name":"Netskope_test_group"} is the header of the file
# Goal is to get the the below features from a standard netskope nsbypass config file

# The following are dictionary options: 'action' 'appName' 'app_domains' 'mode' 'processName' 'rowID' 'tunnel_domains'

# Tunnel mode bypasses proxy but processes the traffic on the Netskope server, direct mode processes it locally
import re
def read_file():
    with open("nsbypass.json", "r") as r:
        index = 0
        output = ""
        x = eval(re.search(r"certPinnedAppList\":\[(.*)]\,\"status\":\"success\"", r.read()).group(1))
        for i in range(len(x)):
            z = x[index]
            output += f"{z['mode']}: {z['appName']} - {z['processName']}\n"
            index += 1
    r.close
    with open("output.txt", 'w') as w:
        w.write("Netskope_test_group:\n\n" + "Mode | App Name | Process Name\n" + output)
    w.close
    return "Output has been written to: 'Output.txt'"

print(read_file())

with open("output.txt", "r") as r:
    for line in r.readlines():
        if bool(re.search("^direct", line)) is True:
            print(line, end="")

