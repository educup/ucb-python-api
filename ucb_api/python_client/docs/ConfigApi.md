# swagger_client.ConfigApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_version**](ConfigApi.md#get_version) | **GET** /versions/unity/{key} | Get a unity version by value
[**list_scms_supporting_version_auto_detect**](ConfigApi.md#list_scms_supporting_version_auto_detect) | **GET** /versions/auto_detect_supported_scms | List all SCM types supporting auto detecting the project Unity version
[**list_unity_versions**](ConfigApi.md#list_unity_versions) | **GET** /versions/unity | List all unity versions
[**list_xcode_versions**](ConfigApi.md#list_xcode_versions) | **GET** /versions/xcode | List all xcode versions


# **get_version**
> object get_version(key)

Get a unity version by value

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
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | Unity Version key (e.g. 2019_2_0f1)

try:
    # Get a unity version by value
    api_response = api_instance.get_version(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Unity Version key (e.g. 2019_2_0f1) | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [filetoken](../README.md#filetoken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scms_supporting_version_auto_detect**
> list[str] list_scms_supporting_version_auto_detect()

List all SCM types supporting auto detecting the project Unity version

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
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # List all SCM types supporting auto detecting the project Unity version
    api_response = api_instance.list_scms_supporting_version_auto_detect()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->list_scms_supporting_version_auto_detect: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[apikey](../README.md#apikey), [filetoken](../README.md#filetoken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_unity_versions**
> list[InlineResponse2001] list_unity_versions()

List all unity versions

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
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # List all unity versions
    api_response = api_instance.list_unity_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->list_unity_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

[apikey](../README.md#apikey), [filetoken](../README.md#filetoken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_xcode_versions**
> list[InlineResponse2002] list_xcode_versions()

List all xcode versions

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
api_instance = swagger_client.ConfigApi(swagger_client.ApiClient(configuration))

try:
    # List all xcode versions
    api_response = api_instance.list_xcode_versions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->list_xcode_versions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

[apikey](../README.md#apikey), [filetoken](../README.md#filetoken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

