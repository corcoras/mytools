
domain_name = ".donayrespontia"

def get_desc(cdp_detail):
    devices = {}
    cdp_lines = cdp_detail.split('\n')
    for i in cdp_lines:
        if "Device ID:" in i:
            device_value = (str(i.split(" ")[2:3]))
            devices[device_value] = {}
        if "IP address" in i:
            my_ip = i.split(" ")
            my_ip = my_ip[4]
            devices[device_value]["IP"] = my_ip
        if "Platform:" in i:
            platform = i.split(" ")
            platform = platform[2]
            if "IP" in platform:
                phone = i.split(" ")
                platform = "Phone " + phone[4]
            devices[device_value]["platform"] = platform
        if "Interface:" in i:
            interface = i.split(" ")
            interface = interface[1]
            devices[device_value]["interface"] = interface
        if "outgoing" in i:
            outgoing = i.split(" ")
            outgoing = (outgoing[7])
            devices[device_value]["outgoing"] = outgoing
    return devices


#devices_detail = get_desc(cdp_detail)

def make_interface_description(devices):
    rawresult = ''
    cleanresult = ''
    result = ''
    for p_id, p_info in devices.items():
        print("\nID: ", p_id)
        for key in p_info:
            print(key + ":", p_info[key])
    for p_id, p_info in devices.items():
        for key in p_info:
            if key == "interface":
                device_name = p_id
                #print("\n")
                result += ('\n')
                #print("inter ", p_info[key])
                rawresult = "inter " + p_info[key] + '\n'
                cleanresult = rawresult.replace(",", "").replace("[", "").replace("]", "").replace("'", "")  
                result += cleanresult
                #print(" desc " + device_name.replace(domain_name, "") + " "  + p_info["platform"] + " " + p_info["IP"] + " "  + p_info['outgoing'])

                rawresult = " desc " + device_name.replace(domain_name, "") + " "  + p_info["platform"] + " " + p_info["IP"]  + p_info['outgoing'] + '\n'
                cleanresult = rawresult.replace(",", "").replace("[", "").replace("]", "").replace("'", "").replace('\\r','').replace('.nis.cdk.com', '')
                result += cleanresult
                #c.replace(",", "").replace("[", "").replace("]", "").replace("'", "")  
                result += '\n'  
                
    return result
#make_interface_description(devices_detail)

def cdp(cdp_detail):
  devices_detail = get_desc(cdp_detail)
  result = make_interface_description(devices_detail)
  #result = str(result)
  return result 
