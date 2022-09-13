"""

    Meraki Dashboard API Python3 script to change SSID passwords.
    
   DISCLAIMER: This script is edited from the original script by Meraki
"""

from __future__ import absolute_import, division, print_function
from tkinter import EXCEPTION
__author__ = "Murtadha Marzouq"
__version__ = "1.0"

import os
import json
import time
import sys
import pandas as pd
import requests
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from meraki_sdk.exceptions.api_exception import APIException

x_cisco_meraki_api_key = ""
meraki = MerakiSdkClient(x_cisco_meraki_api_key)
networks_controller = meraki.networks
devices_controller = meraki.devices
ssids_controller = meraki.ssids
base_url = "https://api.meraki.com/api/v0/networks/"
# full url -> "https://api.meraki.com/api/v0/networks/{networkID}/ssids/{SSID number}"
headers = {
    "X-Cisco-Meraki-API-Key": x_cisco_meraki_api_key,
    "Content-Type": "application/json",
}

t_ssid = "WQ_Guest"  # Change this to match the SSID to modify
Org_List = []
Name_List = []
SSID_URLS = []
SSID_List = []


def get_orgs(meraki):
    # Get the list of organizations
    try:
        org_result = meraki.organizations.get_organizations()
        # print(json.dumps(org_result, indent=4))
        return org_result
    except APIException as e:
        print(e)


def org_info(orgs):
    # Get name and ID
    try:
        for orgs in orgs:
            Name = orgs["name"]
            Org = orgs["id"]
            print(f"Found '{Name}' with ID '{Org}'.")
            return (Name, Org)
    except:   
        print(f"Something bad happened. Exit script...")
    
def net_names(net_cont, t_org):
    # Obtain network names and IDs in target organization
    collect = {}
    net_dict = {}
    net_list = []
    print("Looking for network names and ID's...\n")
    collect["organization_id"] = t_org
    try:
        result = networks_controller.get_organization_networks(collect)
        # print(json.dumps(result, indent=4))
        for result in result:
            Net_Name = result["name"]
            Net_id = result["id"]
            print(f"""Found network '{Net_Name}' with net id '{Net_id}'.""")
            net_dict[Net_Name] = Net_id
            net_list.append(Net_id)
        print("\nNetwork ID search complete...")
        return (net_dict, net_list)
    except APIException as e:
        print(e)



def pd_ssid_csv(jsonFile):
    file_name = "ssid.csv"
    date = pd.to_datetime("today").normalize()
    hms = time.strftime("%H:%M:%S")
    pdHead = pd.DataFrame(
        jsonFile,
        index=[0],
        columns=[
            "authMode",
            "enabled",
            "name",
            "psk",
            "wpaEncryptionMode",
            "date",
            "time",
        ],
    )
    pdHead["date"] = date
    pdHead["time"] = hms
    pdHead.to_csv(file_name)
    print("Dataframe", pdHead, sep="\n")
    return


def gen_url(base_url, ssid_nets, ssid_tar):
    ssid_net_str = ""
    for ssid in ssid_nets:
        ssid_net_str = ssid
    ssid_num = str(ssid_tar)
    change_url = base_url + ssid_net_str + "/ssids/" + ssid_num
    return change_url


def payload(new_ssid):
    payld = '{"psk": "' + new_ssid + '"}'
    return payld


def modify_psk(change_url, header, payld):
    print(payld)
    try:
        response = requests.put(change_url, headers=header, data=payld)
        put_response = response.text.encode("utf8")
        print(put_response)
    except APIException as e:
        print(e)

def backup_config(ssid_result, filename):
    # Backup existing settings to local file
    try:
        print("Backing up current settings to local file...")
        with open(filename, "w", encoding="utf-8") as outfile:
            json.dump(ssid_result, outfile, indent=4)
    finally:
        outfile.close()

def ssid_search(ssid_result, ssid_name, network):
    for ssid in ssid_result:
        if ssid["name"] == ssid_name:
            ssid_number = ssid["number"]
            ssid_password = ssid["psk"]
            payload = '{"psk": "' + NEW_SSID_PASSWORD + '"}'
        
            change_url = base_url + network + "/ssids/" + str(ssid_number)
            # Backup existing settings to local file using the network ID
            backup_config(ssid_result, f'${network}.json')
            # ADDING THE URLS TO THE LIST
            SSID_URLS.append(change_url)
            # ADDING THE NETWORKS TO THE LIST
            Name_List.append(network)
            # Change the SSID password
            print("Changing the SSID password...")
            modify_psk(change_url, headers, payload)
            print("SSID password changed successfully!" + " " + ssid_name + " " + ssid_password)
            return (ssid_number, ssid_name, ssid_password)
        else:
            print("SSID not found")
            #CHECK THIS LINE: PROBLEM
            





# New Password 
NEW_SSID_PASSWORD = "#THISISMYPASS123#" 
#SSID_To_Change = "WQ_Guest"
#SSID_To_Change = "WB_Guest"
SSID_To_Change = "WQGuest"

if __name__ == "__main__":
    # Get the list of organizations
    orgs = get_orgs(meraki)
    print(orgs)
    print("Obtained list of Orgs...")
    # print(json.dumps(orgs, indent=4))

    org_name, org_id = org_info(orgs)
    # Get list of Networks
    net_dict, net_list = net_names(networks_controller, org_id)
    print("Obtained list of Networks...")
    # print(json.dumps(net_dict, indent=4))
    # for each network in the list, get the SSIDs
    for net in net_list:
        print(net)
        ssid_result = ssids_controller.get_network_ssids(net)
        # for each SSID in the list, check if it is the SSID we want to change
        ssid_number, ssid_name, ssid_password = ssid_search(ssid_result, SSID_To_Change,net)
        
     #    # generating the PAYLOAD (JSON) for the PUT request
     #    payload = '{"psk": "' + NEW_SSID_PASSWORD + '"}'
        
     #    change_url = base_url + net + "/ssids/" + str(ssid_number)
     #    # Backup existing settings to local file using the network ID
     #    backup_config(ssid_result, f'${net}.json')
     #    # ADDING THE URLS TO THE LIST
     #    SSID_URLS.append(change_url)
     #    # ADDING THE NETWORKS TO THE LIST
     #    Name_List.append(net)
     #    # Change the SSID password
     #    print("Changing the SSID password...")
	    # modify_psk(change_url, headers, payload)
     #    print("SSID password changed successfully!" + " " + ssid_name + " " + ssid_password)

    
	# SANITY CHECK
	#######################################


        
    
    
    
    
        
    
    
    

     
 
