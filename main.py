"""
This is a script to filter the netskope nsbypass.json file

The nsbypass.json file describes the configuration of the traffic steering bypass policy

There are two modes: Tunnel and Direct

Tunnel mode bypasses proxy but processes the traffic on the Netskope server, direct mode processes it locally

The following are filtering options: 'action' 'appName' 'app_domains' 'mode' 'processName' 'rowID' 'tunnel_domains'

Just copy and paste, or add to the scripts directory, the nsbypass.json file
"""


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
    return "Output has been written to: 'Output.txt'\n"

print(read_file())

with open("output.txt", "r") as r:
    global ordered_result
    ordered_result = ""
    lines = r.readlines()
    for line in lines:
        if bool(re.search("^tunnel", line)):
            ordered_result += line
    for line in lines:
        if bool(re.search("^direct", line)):
            ordered_result += line
    print(ordered_result)

