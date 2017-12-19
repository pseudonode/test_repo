import yaml
import json

list = range(16)
  
dict = {'ip_addr':'10.10.10.10'}

list.append(dict)

dict2 = {'mask':'255.255.255.0'}

list.append(dict2)

list[-1]

list.append({})

list[-1]['admin_state'] = 'shutdown'

print "Printing Original List"
print list

print
print "Printing list in YAML format - Default Flow Style"
print yaml.dump(list, default_flow_style = True)

with open("ex6.yml", "w") as f:
  f.write(yaml.dump(list, default_flow_style = False))

print "Printing list in JSON format"
print json.dumps(list)

with open("ex6.json", "w") as f:
  f.write(json.dumps(list))
