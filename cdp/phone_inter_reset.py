class phone_inter:
    def __init__(self, cdp_neig, separator):
        self.cdp_neig = cdp_neig
        self.separator = separator
    def find(self):
        data = self.cdp_neig
        f = open('Final_Phone_interfaces_results.txt', "w+")
        lines = data.split('\n')
        result = 'Phone Interfaces' + '\n'             
        for i in lines:
            if '#' in i and 'sho cdp n' in i:
                #print(i)
                devicelist = i.split('#')
                devicestring = devicelist[0]
                print('')
                print(self.separator * 30)
                print(devicestring)
                print(self.separator * 30)
                print('')
                print('config t')
                #write to a file
                f.write('' + '\n' )
                f.write(self.separator * 30 + '\n' )
                f.write(devicestring + '\n' )
                f.write(self.separator * 30 + '\n' )
                f.write('' + '\n' )
                f.write('config t' + '\n' )
                result += '' + '\n'             
                result += self.separator * 30 + '\n' 
                result += devicestring + '\n' 
                result += self.separator * 30 + '\n' 
                result += '' + '\n' 
                result += 'config t' + '\n' 
            if 'SEP' in  i:
                #print(i)
                interfacelist = i.split(" ")
                #print(interfacelist)
                interfacestring = 'interface ' + interfacelist[2] + ' ' + interfacelist[3]
                print(interfacestring)
                print('shut')
                print('no shut')
                #write to a file
                f.write(interfacestring + '\n' )
                f.write('shut' + '\n' )
                f.write('no shut' + '\n' )
                result += interfacestring + '\n'              
                result += 'shut' + '\n' 
                result += 'no shut' + '\n' 
        f.close()
        return result

#p = phone_inter(data, "~")
#p.find()
#fphone = p.find()
#fphone
def reset(cdp_detail):
    p = phone_inter(cdp_detail, "~")
    result = p.find()
    return result 