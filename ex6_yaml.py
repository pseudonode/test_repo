import yaml

list = range(16)
  
dict = {'ip_addr':'10.10.10.10'}

list.append(dict)

dict2 = {'mask':'255.255.255.0'}

list.append(dict2)

list.append({})

list[-1]['admin_state'] = 'shutdown'

print list

print yaml.dump(list)

print yaml.dump(list, default_flow_style = True)

with open("ex6.yml", "w") as f:
  f.write(yaml.dump(list)
