from email.mime import base
import os

## User input 
base_dir = input("Enter the path of your choice: ")
#print("base_dir: " + base_dir)

## Creating base directory for container storage
base_dir_mode = 0o755
try:
    os.makedirs(base_dir, base_dir_mode, exist_ok = True)
    print("Directory '% s' created" % base_dir)
except: OSError as error:
    print("Directory '% s' could not be created" % base_dir)

## Creating the Elastic nodes directories
es_dir = input("Enter directory name for elastic storage: ")
#print("es_dir: " + es_dir)

es_dir_mode = 0o755
es_dir_name = os.path.join(base_dir, es_dir)

try:
    os.makedirs(es_dir_name, es_dir_mode, exist_ok = True)
    print("Directory '% s' created" % es_dir_name)
except: OSError as error:
    print("Directory '% s' could not be created" % es_dir_name)

es_nodes_num = int(input("Number of Elastic nodes: "))
es_nodes_list = []

for x in range(es_nodes_num):
    x = x+1
    x_str = str(x)
    es_nodes_list.append(input("es0"+x_str))
    
#print(es_nodes_list)

for node in es_nodes_list:
    es_nodes_name = os.path.join(es_dir_path, node)
    try:
        os.makedirs(es_dir_name, es_nodes_name)
        print("Directory '% s' created" % es_nodes_name)
    except: OSError as error:
        print("Directory '% s' could not be created" % es_nodes_name)

## Creating the Wazuh directories
wazuh_cluster = input("Wazuh 'Standalone' or 'Cluster':" )
wazuh_dir = 'wazuh'
wazuh_dir_mode = 0o770
wazuh_dir_name = os.path.join(base_dir, wazuh_dir, wazuh_dir_mode)
wazuh_mgr_dir = 'manager'
wazuh_mgr_dir_name = os.path.join(wazuh_dir,wazuh_mgr_dir)
wazuh_wkr_dir = 'worker'
wazuh_wkr_dir_name = os.path.join(wazuh_dir,wazuh_wkr_dir)
if wazuh_cluster == 'cluster':
    try:
        os.makedirs(wazuh_mgr_dir_name)
        print("Directory '% s' created" % wazuh_dir_name)
    except: OSError as error:
        print("Directory '% s' could not be created" % wazuh_mgr_dir_name)
    try:
        os.makedirs(wazuh_wkr_dir_name)
        print("Directory '% s' created" % wazuh_wkr_dir_name)
    except: OSError as error:
        print("Directory '% s' could not be created" % wazuh_wkr_dir_name)
elif wazuh_cluster == 'standalone':
    try:
        os.makedirs(wazuh_mgr_dir_name)
        print("Directory '% s' created" % wazuh_dir_name)
    except: OSError as error:
        print("Directory '% s' could not be created" % wazuh_mgr_dir_name)



    
    
    
#print("wazuh_cluster: " + wazuh_cluster)






#


