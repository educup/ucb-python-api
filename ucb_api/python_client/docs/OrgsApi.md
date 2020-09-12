# swagger_client.OrgsApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_billing_plans**](OrgsApi.md#get_billing_plans) | **GET** /orgs/{orgid}/billingplan | Get billing plan
[**get_ssh_key_for_org**](OrgsApi.md#get_ssh_key_for_org) | **GET** /orgs/{orgid}/sshkey | Get SSH Key
[**regenerate_ssh_key**](OrgsApi.md#regenerate_ssh_key) | **POST** /orgs/{orgid}/sshkey | Regenerate SSH Key


# **get_billing_plans**
> object get_billing_plans(orgid)

Get billing plan

Get the billing plan for the specified organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: apikey
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: permissions
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.OrgsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier

try:
    # Get billing plan
    api_response = api_instance.get_billing_plans(orgid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->get_billing_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssh_key_for_org**
> object get_ssh_key_for_org(orgid)

Get SSH Key

Get the ssh public key for the specified org

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: apikey
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: permissions
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.OrgsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier

try:
    # Get SSH Key
    api_response = api_instance.get_ssh_key_for_org(orgid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->get_ssh_key_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_ssh_key**
> object regenerate_ssh_key(orgid)

Regenerate SSH Key

Regenerate the ssh key for the specified org *WARNING* this is a destructive operation that will permanently remove your current SSH key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: apikey
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: permissions
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.OrgsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier

try:
    # Regenerate SSH Key
    api_response = api_instance.regenerate_ssh_key(orgid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrgsApi->regenerate_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

