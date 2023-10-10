import json
# {"certPinnedAppList":[],"status":"success","steering_config_name":"Netskope_test_group"}
# Goal is to get the appname and app domains

# The following are dictionary options: 'action' 'appName' 'app_domains' 'isRegex' 'mode' 'processName' 'rowID' 'tunnel_domains'

def read_file():
    with open("Text-File.txt", "r") as r:
        index = 0
        output = ""
        x = eval(r.read())
        for i in range(len(x)):
            z = x[index]
            if z['app_domains'] == ['*']:
                z['app_domains'] = "No Domains"
            output += f"{z['appName']}: {z['app_domains']}\n"
            index += 1
    r.close
    with open("Output", '+w') as w:
        w.write(output)
    w.close
    return "Output has been written to: 'Output.txt'"
    

print(read_file())