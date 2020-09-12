# swagger_client.ProjectsApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_project**](ProjectsApi.md#add_project) | **POST** /orgs/{orgid}/projects | Create project
[**archive_project**](ProjectsApi.md#archive_project) | **DELETE** /orgs/{orgid}/projects/{projectid} | Archive project
[**get_audit_log_for_project**](ProjectsApi.md#get_audit_log_for_project) | **GET** /orgs/{orgid}/projects/{projectid}/auditlog | Get audit log
[**get_billing_plans_for_project**](ProjectsApi.md#get_billing_plans_for_project) | **GET** /orgs/{orgid}/projects/{projectid}/billingplan | Get billing plan
[**get_env_variables_for_project**](ProjectsApi.md#get_env_variables_for_project) | **GET** /orgs/{orgid}/projects/{projectid}/envvars | Get environment variables
[**get_project**](ProjectsApi.md#get_project) | **GET** /orgs/{orgid}/projects/{projectid} | Get project details
[**get_project_by_upid**](ProjectsApi.md#get_project_by_upid) | **GET** /projects/{projectupid} | Get project details
[**get_ssh_key_for_project**](ProjectsApi.md#get_ssh_key_for_project) | **GET** /orgs/{orgid}/projects/{projectid}/sshkey | Get SSH Key
[**get_stats_for_project**](ProjectsApi.md#get_stats_for_project) | **GET** /orgs/{orgid}/projects/{projectid}/stats | Get project statistics
[**list_projects_for_org**](ProjectsApi.md#list_projects_for_org) | **GET** /orgs/{orgid}/projects | List all projects (org)
[**list_projects_for_user**](ProjectsApi.md#list_projects_for_user) | **GET** /projects | List all projects (user)
[**set_env_variables_for_project**](ProjectsApi.md#set_env_variables_for_project) | **PUT** /orgs/{orgid}/projects/{projectid}/envvars | Set environment variables
[**update_project**](ProjectsApi.md#update_project) | **PUT** /orgs/{orgid}/projects/{projectid} | Update project details


# **add_project**
> object add_project(orgid, options)

Create project

Create a project for the specified organization

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
options = NULL # object | Options for project create/update

try:
    # Create project
    api_response = api_instance.add_project(orgid, options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **options** | [**object**](.md)| Options for project create/update | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_project**
> str archive_project(orgid, projectid)

Archive project

This will archive the project in Cloud Build ONLY. Use with caution - this process is not reversible. The projects UPID will be removed from Cloud Build allowing the project to be reconfigured.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier

try:
    # Archive project
    api_response = api_instance.archive_project(orgid, projectid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->archive_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_log_for_project**
> list[InlineResponse2006] get_audit_log_for_project(orgid, projectid, per_page=per_page, page=page)

Get audit log

Retrieve a list of historical settings changes for this project

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
per_page = 25 # float | Number of audit log records to retrieve (optional) (default to 25)
page = 1 # float | Skip to page number, based on per_page value (optional) (default to 1)

try:
    # Get audit log
    api_response = api_instance.get_audit_log_for_project(orgid, projectid, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_audit_log_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **per_page** | **float**| Number of audit log records to retrieve | [optional] [default to 25]
 **page** | **float**| Skip to page number, based on per_page value | [optional] [default to 1]

### Return type

[**list[InlineResponse2006]**](InlineResponse2006.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing_plans_for_project**
> object get_billing_plans_for_project(orgid, projectid)

Get billing plan

Get the billing plan for the specified project

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier

try:
    # Get billing plan
    api_response = api_instance.get_billing_plans_for_project(orgid, projectid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_billing_plans_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_env_variables_for_project**
> dict(str, str) get_env_variables_for_project(orgid, projectid)

Get environment variables

Get all configured environment variables for a given project

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier

try:
    # Get environment variables
    api_response = api_instance.get_env_variables_for_project(orgid, projectid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_env_variables_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 

### Return type

**dict(str, str)**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> object get_project(orgid, projectid, include=include)

Get project details

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
include = 'include_example' # str | Extra fields to include in the response (optional)

try:
    # Get project details
    api_response = api_instance.get_project(orgid, projectid, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **include** | **str**| Extra fields to include in the response | [optional] 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_by_upid**
> object get_project_by_upid(projectupid)

Get project details

Gets the same data as /orgs/{orgid}/project/{projectid} but looks up the project by the Unity Project ID. This value is returned in the project's guid field.

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
projectupid = 'projectupid_example' # str | Project UPID - Unity global id

try:
    # Get project details
    api_response = api_instance.get_project_by_upid(projectupid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_by_upid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectupid** | **str**| Project UPID - Unity global id | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssh_key_for_project**
> object get_ssh_key_for_project(orgid, projectid)

Get SSH Key

Get the ssh public key for the specified project

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier

try:
    # Get SSH Key
    api_response = api_instance.get_ssh_key_for_project(orgid, projectid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_ssh_key_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats_for_project**
> object get_stats_for_project(orgid, projectid)

Get project statistics

Get statistics for the specified project

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier

try:
    # Get project statistics
    api_response = api_instance.get_stats_for_project(orgid, projectid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_stats_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects_for_org**
> list[object] list_projects_for_org(orgid, include=include)

List all projects (org)

List all projects that belong to the specified organization. Add \"?include=settings\" as a query parameter to include the project settings with the response. 

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
include = 'include_example' # str | Extra fields to include in the response (optional)

try:
    # List all projects (org)
    api_response = api_instance.list_projects_for_org(orgid, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->list_projects_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **include** | **str**| Extra fields to include in the response | [optional] 

### Return type

**list[object]**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects_for_user**
> list[object] list_projects_for_user(include=include)

List all projects (user)

List all projects that you have permission to access across all organizations. Add \"?include=settings\" as a query parameter to include the project settings with the response. 

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
include = 'include_example' # str | Extra fields to include in the response (optional)

try:
    # List all projects (user)
    api_response = api_instance.list_projects_for_user(include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->list_projects_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Extra fields to include in the response | [optional] 

### Return type

**list[object]**

### Authorization

[apikey](../README.md#apikey), [filetoken](../README.md#filetoken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_env_variables_for_project**
> dict(str, str) set_env_variables_for_project(orgid, projectid, envvars)

Set environment variables

Set all configured environment variables for a given project

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
envvars = NULL # object | Environment variables

try:
    # Set environment variables
    api_response = api_instance.set_env_variables_for_project(orgid, projectid, envvars)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->set_env_variables_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **envvars** | **object**| Environment variables | 

### Return type

**dict(str, str)**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> object update_project(orgid, projectid, options)

Update project details

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
api_instance = swagger_client.ProjectsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
options = NULL # object | Options for project create/update

try:
    # Update project details
    api_response = api_instance.update_project(orgid, projectid, options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **options** | [**object**](.md)| Options for project create/update | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

