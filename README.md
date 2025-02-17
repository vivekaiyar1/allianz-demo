# API to create VNET and multiple subnets

### Prerequisites
    pip install azure.identity
    pip install azure.mgmt.network
    pip install azure.mgmt.network
    A json file with vnet and subnet name and address_prefix

# Usage
### To create vnet and subnet:
    python azure_vnet_create.py
### To get vnet and subnet details:
    python azure_vnet_get.py
    
    Before the script is executed please set the values of the tenant ID, client ID, client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
    Also set the values of subscription id and resource group as environment variables: AZURE_SUBSCRIPTION_ID
    and AZURE_RESOURCE_GROUP. The value of subscription id can be obtained from the portal.
