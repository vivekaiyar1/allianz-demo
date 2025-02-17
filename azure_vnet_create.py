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
vnet_address_prefix = d['vnet'][0]['address_prefix']
subnets = d['subnets'][0:]


def main():
    # Using DefaultAzureCredential - recommended for production
    credential=DefaultAzureCredential()
   
    resource_client = ResourceManagementClient(credential, SUBSCRIPTION_ID)

    client = NetworkManagementClient(credential, SUBSCRIPTION_ID)
    
    # Create Resource group if it does not exist
    resource_group = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME, {"location": "eastus"})
    print(resource_group)

    # Create VNet
    vnet_params = {
         "location": resource_group.location,
         "address_space": {"address_prefixes": [vnet_address_prefix]} 
    }
    
    response = client.virtual_networks.begin_create_or_update(RESOURCE_GROUP_NAME, vnet_name, vnet_params).result()
    print(response)

    for subnet in subnets:
        subnet_params = {
            "address_prefix": subnet['address_prefix']
        }
        client.subnets.begin_create_or_update(RESOURCE_GROUP_NAME, vnet_name, subnet['name'], subnet_params).result() 



if __name__ == "__main__":
    main()
