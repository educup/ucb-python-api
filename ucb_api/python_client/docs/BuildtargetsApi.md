# swagger_client.BuildtargetsApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_build_target**](BuildtargetsApi.md#add_build_target) | **POST** /orgs/{orgid}/projects/{projectid}/buildtargets | Create build target for a project
[**delete_build_target**](BuildtargetsApi.md#delete_build_target) | **DELETE** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid} | Delete build target
[**get_build_target**](BuildtargetsApi.md#get_build_target) | **GET** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid} | Get a build target
[**get_build_targets**](BuildtargetsApi.md#get_build_targets) | **GET** /orgs/{orgid}/projects/{projectid}/buildtargets | List all build targets for a project
[**get_build_targets_for_org**](BuildtargetsApi.md#get_build_targets_for_org) | **GET** /orgs/{orgid}/buildtargets | List all build targets for an org
[**get_env_variables_for_build_target**](BuildtargetsApi.md#get_env_variables_for_build_target) | **GET** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/envvars | Get environment variables
[**get_stats_for_build_target**](BuildtargetsApi.md#get_stats_for_build_target) | **GET** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/stats | Get build target statistics
[**set_env_variables_for_build_target**](BuildtargetsApi.md#set_env_variables_for_build_target) | **PUT** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/envvars | Set environment variables
[**update_build_target**](BuildtargetsApi.md#update_build_target) | **PUT** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid} | Update build target details


# **add_build_target**
> object add_build_target(orgid, projectid, options)

Create build target for a project

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
api_instance = swagger_client.BuildtargetsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
options = swagger_client.Options6() # Options6 | Options for build target create/update

try:
    # Create build target for a project
    api_response = api_instance.add_build_target(orgid, projectid, options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildtargetsApi->add_build_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **options** | [**Options6**](Options6.md)| Options for build target create/update | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_build_target**
> str delete_build_target(orgid, projectid, buildtargetid)

Delete build target

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
api_instance = swagger_client.BuildtargetsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name

try:
    # Delete build target
    api_response = api_instance.delete_build_target(orgid, projectid, buildtargetid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildtargetsApi->delete_build_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_target**
> object get_build_target(orgid, projectid, buildtargetid)

Get a build target

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
api_instance = swagger_client.BuildtargetsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name

try:
    # Get a build target
    api_response = api_instance.get_build_target(orgid, projectid, buildtargetid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildtargetsApi->get_build_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_targets**
> list[InlineResponse2007] get_build_targets(orgid, projectid, include=include, include_last_success=include_last_success)

List all build targets for a project

Gets all configured build targets for a project, regardless of whether they are enabled. Add \"?include=settings,credentials\" as a query parameter to include the build target settings and credentials with the response. 

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
api_instance = swagger_client.BuildtargetsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
include = 'include_example' # str | Extra fields to include in the response (optional)
include_last_success = false # bool | Include last successful build (optional) (default to false)

try:
    # List all build targets for a project
    api_response = api_instance.get_build_targets(orgid, projectid, include=include, include_last_success=include_last_success)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildtargetsApi->get_build_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **include** | **str**| Extra fields to include in the response | [optional] 
 **include_last_success** | **bool**| Include last successful build | [optional] [default to false]

### Return type

[**list[InlineResponse2007]**](InlineResponse2007.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_targets_for_org**
> list[InlineResponse2007] get_build_targets_for_org(orgid, include=include, include_last_success=include_last_success)

List all build targets for an org

Gets all configured build targets for an org, regardless of whether they are enabled. Add \"?include=settings,credentials\" as a query parameter to include the build target settings and credentials with the response. 

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
api_instance = swagger_client.BuildtargetsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
include = 'include_example' # str | Extra fields to include in the response (optional)
include_last_success = false # bool | Include last successful build (optional) (default to false)

try:
    # List all build targets for an org
    api_response = api_instance.get_build_targets_for_org(orgid, include=include, include_last_success=include_last_success)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildtargetsApi->get_build_targets_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **include** | **str**| Extra fields to include in the response | [optional] 
 **include_last_success** | **bool**| Include last successful build | [optional] [default to false]

### Return type

[**list[InlineResponse2007]**](InlineResponse2007.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_env_variables_for_build_target**
> dict(str, str) get_env_variables_for_build_target(orgid, projectid, buildtargetid)

Get environment variables

Get all configured environment variables for a given build target

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
api_instance = swagger_client.BuildtargetsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name

try:
    # Get environment variables
    api_response = api_instance.get_env_variables_for_build_target(orgid, projectid, buildtargetid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildtargetsApi->get_env_variables_for_build_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 

### Return type

**dict(str, str)**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_for_build_target**
> object get_stats_for_build_target(orgid, projectid, buildtargetid, build_status=build_status, clean_build=clean_build, limit=limit)

Get build target statistics

Get statistics for the specified build target

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
api_instance = swagger_client.BuildtargetsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
build_status = '' # str | Query for only builds of a specific status (optional) (default to )
clean_build = true # bool | Query for builds that have either been built clean or using caches (optional)
limit = 8.14 # float | Get stats for last limit builds (optional)

try:
    # Get build target statistics
    api_response = api_instance.get_stats_for_build_target(orgid, projectid, buildtargetid, build_status=build_status, clean_build=clean_build, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildtargetsApi->get_stats_for_build_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **build_status** | **str**| Query for only builds of a specific status | [optional] [default to ]
 **clean_build** | **bool**| Query for builds that have either been built clean or using caches | [optional] 
 **limit** | **float**| Get stats for last limit builds | [optional] 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_env_variables_for_build_target**
> dict(str, str) set_env_variables_for_build_target(orgid, projectid, buildtargetid, envvars)

Set environment variables

Set all configured environment variables for a given build target

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
api_instance = swagger_client.BuildtargetsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
envvars = NULL # object | Environment variables

try:
    # Set environment variables
    api_response = api_instance.set_env_variables_for_build_target(orgid, projectid, buildtargetid, envvars)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildtargetsApi->set_env_variables_for_build_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **envvars** | **object**| Environment variables | 

### Return type

**dict(str, str)**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_build_target**
> object update_build_target(orgid, projectid, buildtargetid, options)

Update build target details

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
api_instance = swagger_client.BuildtargetsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
options = swagger_client.Options7() # Options7 | Options for build target create/update

try:
    # Update build target details
    api_response = api_instance.update_build_target(orgid, projectid, buildtargetid, options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildtargetsApi->update_build_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **options** | [**Options7**](Options7.md)| Options for build target create/update | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

