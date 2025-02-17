from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
import os
import json

# Environment variables for Azure credentials and resource group
SUBSCRIPTION_ID = os.environ.get("AZURE_SUBSCRIPTION_ID")
RESOURCE_GROUP_NAME = os.environ.get("AZURE_RESOURCE_GROUP") # Existing or to be created
# You might want to store these more securely (e.g., Azure Key Vault)
CLIENT_ID = os.environ.get("AZURE_CLIENT_ID")
CLIENT_SECRET = os.environ.get("AZURE_CLIENT_SECRET")
TENANT_ID = os.environ.get("AZURE_TENANT_ID")

with open('vnet.json') as f:
    d = json.load(f)

vnet_name = d['vnet'][0]['name']
subnets = d['subnets'][0:]


def main():
    # Using DefaultAzureCredential - recommended for production
    credential=DefaultAzureCredential()
   
    client = NetworkManagementClient(credential, SUBSCRIPTION_ID)
    
  
    get_vnet = client.virtual_networks.get(RESOURCE_GROUP_NAME, vnet_name)
    print("Get Vnet:\n{}".format(get_vnet))

    for subnet in subnets:
        get_subnet = client.subnets.get(RESOURCE_GROUP_NAME, vnet_name, subnet['name'])
        print("Get Subnet:\n{}".format(get_subnet))



if __name__ == "__main__":
    main()
