# swagger_client.PublicApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_change_logs**](PublicApi.md#get_change_logs) | **GET** /changelogs | Get the Unity Cloud Build changelogs


# **get_change_logs**
> list[InlineResponse200] get_change_logs(type_limit=type_limit, search=search, per_page=per_page, page=page, skip=skip)

Get the Unity Cloud Build changelogs

Retrieves all changelog lines 

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
# Configure HTTP basic authorization: filetoken
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.PublicApi(swagger_client.ApiClient(configuration))
type_limit = 'type_limit_example' # str | Specific type of message used to limit the results (optional)
search = 'search_example' # str | Regex string to use to restrict the results via search (optional)
per_page = 25 # float | Number of audit log records to retrieve (optional) (default to 25)
page = 1 # float | Skip to page number, based on per_page value (optional) (default to 1)
skip = 0 # float | Alternative to page, will fully define start index of results rather than calculating based on page/per_page values (optional) (default to 0)

try:
    # Get the Unity Cloud Build changelogs
    api_response = api_instance.get_change_logs(type_limit=type_limit, search=search, per_page=per_page, page=page, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->get_change_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_limit** | **str**| Specific type of message used to limit the results | [optional] 
 **search** | **str**| Regex string to use to restrict the results via search | [optional] 
 **per_page** | **float**| Number of audit log records to retrieve | [optional] [default to 25]
 **page** | **float**| Skip to page number, based on per_page value | [optional] [default to 1]
 **skip** | **float**| Alternative to page, will fully define start index of results rather than calculating based on page/per_page values | [optional] [default to 0]

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[apikey](../README.md#apikey), [filetoken](../README.md#filetoken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

