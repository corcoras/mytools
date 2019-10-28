from django.http import HttpResponse
from django.shortcuts import render
from cdp.forms import RawProductForm
from cdp import cdp_function as cdp
from cdp import phone_inter_reset as phone
from .forms import ProductForm, CDP_Form
from .models import Product, CDP

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request)
    print(args, kwargs)
    #return HttpResponse("<h1>Hello World!</h1>")
    context = {
        'name': 'Shaun',
        'number': 123,
        'list': ["dog", "cat", "fish", "mouse"]
    }
    return render(request, "home.html", context)

def product_create_view2(request):
  form = RawProductForm()
  if request.method =="POST":
    my_form = RawProductForm(request.POST)
    if my_form.is_valid():
      #now the data is good
      print(my_form.cleaned_data)
      Product.objects.create(**my_form.cleaned_data)
    else:
      print(my_form.errors)

  context = {
    "form": form
  }
  return render(request, "my_forms.html", context)

def cdp_view2(request):
  cmf = 'cmf'
  client_name = 'Sullivan Pontiac'
  device_name = 'Cisco 3560'
  device_ip = '204.125.23.1'
  cdp_scrape = 'paste cdp detail here'
  result = 'interface description result'
  if request.method == "POST":
    cmf = request.POST.get('cmf')
    client_name = request.POST.get('client_name')
    device_name = request.POST.get('device_name')
    device_ip = request.POST.get('device_ip')
    cdp_scrape = request.POST.get('cdp_scrape')
    #result = request.POST.get('result')
    result = cdp.cdp(cdp_scrape)
    #print(cmf)
    CDP.objects.create(
      cmf = cmf,
      client_name = client_name,
      device_name = device_name,
      device_ip = device_ip,
      cdp_scrape = cdp_scrape,
      interface_description = result
    )
  context ={ 
    'cmf': cmf,
    'client_name': client_name,
    'device_name': device_name,
    'device_ip': device_ip,
    'cdp_scrape': cdp_scrape,
    'result': result
  }
  return render(request, 'cdp_html_form.html', context)

def cdp_view(request):
  form = CDP_Form()
  cdp_result = ''
  if request.method=="POST":
    my_form = CDP_Form(request.POST)
    if my_form.is_valid():
      #print(my_form.cleaned_data)
      cdp_detail = request.POST.get('cdp_scrape')
      cdp_result = request.POST.get('interface_description')
      cdp_string = str(cdp_detail)
      cdp_result = cdp.cdp(cdp_string)
      print(cdp_result)
      CDP.objects.create(**my_form.cleaned_data)
        # context = {
        #   'form': my_form,
        #   'result': cdp_result
        # }
    else:
      print(my_form.errors)
  context = {
    'form': form,
    'result': cdp_result
  }
  return render(request, 'cdp_form.html', context)

def phone_inter_reset(request):
  cmf = 'cmf'
  client_name = 'Sullivan Pontiac'
  directory = '/dev'
  result = 'interface description result'
  if request.method=="POST":
    cmf = request.POST.get('cmf')
    print(cmf)
    client_name = request.POST.get('client_name')
    print(client_name)
    directory = request.POST.get('directory')
    print(directory)
    #separator = request.POST.get('separator')
    cdp_scrape = request.POST.get('cdp_scrape')
    print(cdp_scrape)
    #result = request.POST.get('result')
    result = phone.reset(cdp_scrape)
    print(result)
  context = {
    'cmf': cmf,
    'client_name': client_name,
    'directory': directory,
    'result': result
  }
  return render(request, 'phone_inter_reset.html', context)
  #return render(request, 'cdp_form.html', context)



# def product_create_view(request):
#     cdp_result = "empty if GET"
#     #print(request.GET)
#     #print(request.POST)
#     if request.method == "POST":
#         title = request.POST.get('title')
#         title_string = str(title)
#         #print(f"my print statement {title_string}")
#         cdp_result = cdp.cdp(title_string)
#         #cdp_result = "here is some data!!!"
#         #print(cdp_result)
#         context = {
#             "cdp": cdp_result
#         }
#     else:
#         context = {'form': form}
#     return render(request, 'home.html', context)

# def contact_view(request, *args, **kwargs):
#     print(f"this is {request}")
#     return HttpResponse("<h1>Hello from Contact</h1>")

cdpDetail = '''

s1-33049702#sho cdp n det
-------------------------
Device ID: s4-33049702-BODY.nis.cdk.com
VTP Management Domain: ''
Entry address(es):
  IP address: 198.249.131.50
Platform: cisco WS-C2960X-24PS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/1/2,  Port ID (outgoing port): GigabitEthernet1/0/26
Holdtime : 129 sec
 
Version :
Cisco IOS Software, C2960X Software (C2960X-UNIVERSALK9-M), Version 15.2(2)E5, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Thu 02-Jun-16 01:31 by prod_rel_team
 
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000059DC8F8600FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
  IP address: 198.249.131.50
 
-------------------------
Device ID: SEP0021D8BA0965
Entry address(es):
  IP address: 172.30.6.12
Platform: Cisco IP Phone 7942,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/45,  Port ID (outgoing port): Port 1
Holdtime : 146 sec
Second Port Status: Up
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 2405, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: SEP0021555542E6
Entry address(es):
  IP address: 172.30.6.2
Platform: Cisco IP Phone 7962,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/29,  Port ID (outgoing port): Port 1
Holdtime : 134 sec
Second Port Status: Down
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 17126, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: SEP002155554A89
Entry address(es):
  IP address: 172.30.6.196
Platform: Cisco IP Phone 7962,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/15,  Port ID (outgoing port): Port 1
Holdtime : 123 sec
Second Port Status: Up
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 19081, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: s2-33049702.nis.cdk.com
Entry address(es):
  IP address: 198.249.131.57
Platform: cisco WS-C2960X-48FPS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/1/3,  Port ID (outgoing port): GigabitEthernet1/0/50
Holdtime : 129 sec
 
Version :
Cisco IOS Software, C2960X Software (C2960X-UNIVERSALK9-M), Version 15.2(2)E5, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Thu 02-Jun-16 01:31 by prod_rel_team
 
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000002C3124DFC380FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
  IP address: 198.249.131.57
 
-------------------------
Device ID: SEP0021D8BA0FC9
Entry address(es):
  IP address: 172.30.6.253
Platform: Cisco IP Phone 7942,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/16,  Port ID (outgoing port): Port 1
Holdtime : 177 sec
Second Port Status: Down
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 4041, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: SEP002155554ADC
Entry address(es):
  IP address: 172.30.6.66
Platform: Cisco IP Phone 7962,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/28,  Port ID (outgoing port): Port 1
Holdtime : 177 sec
Second Port Status: Down
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 19164, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: SEP0021D8BA1304
Entry address(es):
  IP address: 172.30.6.8
Platform: Cisco IP Phone 7942,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/43,  Port ID (outgoing port): Port 1
Holdtime : 125 sec
Second Port Status: Down
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 4868, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: SEP00215554F395
Entry address(es):
  IP address: 172.30.6.232
Platform: Cisco IP Phone 7962,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/32,  Port ID (outgoing port): Port 1
Holdtime : 177 sec
Second Port Status: Down
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 62357, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: SEP0021D8BA1363
Entry address(es):
  IP address: 172.30.6.104
Platform: Cisco IP Phone 7942,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/46,  Port ID (outgoing port): Port 1
Holdtime : 123 sec
Second Port Status: Down
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 4963, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: SEP0021D8BA0968
Entry address(es):
  IP address: 172.30.6.172
Platform: Cisco IP Phone 7942,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/39,  Port ID (outgoing port): Port 1
Holdtime : 132 sec
Second Port Status: Down
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 2408, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: SEP0021D8BA1454
Entry address(es):
  IP address: 172.30.6.96
Platform: Cisco IP Phone 7942,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/8,  Port ID (outgoing port): Port 1
Holdtime : 128 sec
Second Port Status: Up
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 5204, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: SEP0022905BE42D
Entry address(es):
  IP address: 172.30.6.227
Platform: Cisco IP Phone 7962,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/34,  Port ID (outgoing port): Port 1
Holdtime : 153 sec
Second Port Status: Down
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 58413, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: SEP002155554AA2
Entry address(es):
  IP address: 172.30.6.146
Platform: Cisco IP Phone 7962,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/37,  Port ID (outgoing port): Port 1
Holdtime : 151 sec
Second Port Status: Down
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 19106, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: SEP002155554233
Entry address(es):
  IP address: 172.30.6.90
Platform: Cisco IP Phone 7962,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/10,  Port ID (outgoing port): Port 1
Holdtime : 124 sec
Second Port Status: Up
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 16947, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: SEP002155554B5B
Entry address(es):
  IP address: 172.30.6.218
Platform: Cisco IP Phone 7962,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/33,  Port ID (outgoing port): Port 1
Holdtime : 174 sec
Second Port Status: Down
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 19291, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: SEP1C17D3C250C6
Entry address(es):
  IP address: 172.30.6.160
Platform: Cisco IP Phone 7942,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/35,  Port ID (outgoing port): Port 1
Holdtime : 153 sec
Second Port Status: Down
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 20678, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: SEP002155554234
Entry address(es):
  IP address: 172.30.6.251
Platform: Cisco IP Phone 7962,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/31,  Port ID (outgoing port): Port 1
Holdtime : 124 sec
Second Port Status: Down
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 16948, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: r2.fortwayne-hon.donayres.donayrespontia
Entry address(es):
  IP address: 198.249.131.60
Platform: Cisco CISCO2921/K9,  Capabilities: Router Switch IGMP
Interface: GigabitEthernet1/0/2,  Port ID (outgoing port): GigabitEthernet0/0
Holdtime : 167 sec
 
Version :
Cisco IOS Software, C2900 Software (C2900-UNIVERSALK9-M), Version 15.2(4)M5, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2013 by Cisco Systems, Inc.
Compiled Fri 13-Sep-13 14:59 by prod_rel_team
 
advertisement version: 2
VTP Management Domain: ''
Duplex: full
 
-------------------------
Device ID: SEP0021D8BA21A4
Entry address(es):
  IP address: 172.30.6.4
Platform: Cisco IP Phone 7942,  Capabilities: Host Phone Two-port Mac Relay
Interface: GigabitEthernet1/0/25,  Port ID (outgoing port): Port 1
Holdtime : 130 sec
Second Port Status: Down
 
Version :
SCCP42.8-4-2S
 
advertisement version: 2
Duplex: full
Power drawn: 6.300 Watts
Power request id: 8612, Power management id: 3
Power request levels are:6300 0 0 0 0
 
-------------------------
Device ID: r3.fortwayne-hon.donayres.donayrespontia
Entry address(es):
  IP address: 198.249.131.59
Platform: Cisco CISCO2951/K9,  Capabilities: Router Switch IGMP
Interface: GigabitEthernet1/0/3,  Port ID (outgoing port): GigabitEthernet0/0
Holdtime : 137 sec
 
Version :
Cisco IOS Software, C2951 Software (C2951-UNIVERSALK9-M), Version 15.2(4)M5, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2013 by Cisco Systems, Inc.
Compiled Fri 13-Sep-13 15:26 by prod_rel_team
 
advertisement version: 2
VTP Management Domain: ''
Duplex: full
 
-------------------------
Device ID: r1.fortwayne-hon.donayres.donayrespontia
Entry address(es):
  IP address: 198.249.131.47
Platform: Cisco CISCO2921/K9,  Capabilities: Router Switch IGMP
Interface: GigabitEthernet1/0/1,  Port ID (outgoing port): GigabitEthernet0/0
Holdtime : 139 sec
 
Version :
Cisco IOS Software, C2900 Software (C2900-UNIVERSALK9-M), Version 15.2(4)M5, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2013 by Cisco Systems, Inc.
Compiled Fri 13-Sep-13 14:59 by prod_rel_team
 
advertisement version: 2
VTP Management Domain: ''
Duplex: full
 
-------------------------
Device ID: s3-33049702-BDC.nis.cdk.com
Entry address(es):
  IP address: 198.249.131.56
Platform: cisco WS-C2960X-24PS-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/1/1,  Port ID (outgoing port): GigabitEthernet1/0/25
Holdtime : 166 sec
 
Version :
Cisco IOS Software, C2960X Software (C2960X-UNIVERSALK9-M), Version 15.2(2)E5, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2016 by Cisco Systems, Inc.
Compiled Thu 02-Jun-16 01:31 by prod_rel_team
 
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF0000000000000059DC8F0400FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
  IP address: 198.249.131.56
 
-------------------------
Device ID: s8.fortwayne-pon.donayres.donayrespontia
Entry address(es):
  IP address: 198.249.131.40
Platform: cisco WS-C2960-24PC-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/1/4,  Port ID (outgoing port): GigabitEthernet0/1
Holdtime : 150 sec
 
Version :
Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE7, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2013 by Cisco Systems, Inc.
Compiled Mon 28-Jan-13 10:22 by prod_rel_team
 
advertisement version: 2
Protocol Hello:  OUI=0x00000C, Protocol ID=0x0112; payload len=27, value=00000000FFFFFFFF010221FF000000000000189C5D2C7080FF0000
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es):
  IP address: 198.249.131.40
 
-------------------------
Device ID: UCMB-33049701.localdomain
Entry address(es):
  IP address: 207.185.238.113
Platform: 7828I3,  Capabilities: Host
Interface: GigabitEthernet1/0/4,  Port ID (outgoing port): eth0
Holdtime : 121 sec
 
Version :
Linux 2.4.21-47.ELsmp #1 SMP Wed Jul 5 20:38:41 EDT 2006 CCM:6.1.3.1000-16
 
 
advertisement version: 2
Duplex: full
 
 
Total cdp entries displayed : 25
s1-33049702#
'''