# swagger_client.BuildsApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_delete_build_artifacts**](BuildsApi.md#batch_delete_build_artifacts) | **POST** /orgs/{orgid}/projects/{projectid}/artifacts/delete | Delete artifacts for a batch of builds
[**cancel_all_builds**](BuildsApi.md#cancel_all_builds) | **DELETE** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds | Cancel all builds
[**cancel_build**](BuildsApi.md#cancel_build) | **DELETE** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds/{number} | Cancel build
[**cancel_builds_for_org**](BuildsApi.md#cancel_builds_for_org) | **DELETE** /orgs/{orgid}/builds | Cancel builds for org
[**create_share**](BuildsApi.md#create_share) | **POST** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds/{number}/share | Create a new link to share a project
[**delete_all_build_artifacts**](BuildsApi.md#delete_all_build_artifacts) | **DELETE** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds/artifacts | Delete all artifacts associated with all non-favorited builds for a specified buildtargetid (_all is allowed).
[**delete_build_artifacts**](BuildsApi.md#delete_build_artifacts) | **DELETE** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds/{number}/artifacts | Delete all artifacts associated with a specific build
[**get_audit_log**](BuildsApi.md#get_audit_log) | **GET** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds/{number}/auditlog | Get audit log
[**get_audit_log_for_build_target**](BuildsApi.md#get_audit_log_for_build_target) | **GET** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/auditlog | Get audit log
[**get_build**](BuildsApi.md#get_build) | **GET** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds/{number} | Build Status
[**get_build_log**](BuildsApi.md#get_build_log) | **GET** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds/{number}/log | Get build log
[**get_build_steps**](BuildsApi.md#get_build_steps) | **GET** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds/{number}/steps | Get the build steps for a given build
[**get_builds**](BuildsApi.md#get_builds) | **GET** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds | List all builds
[**get_builds_for_org**](BuildsApi.md#get_builds_for_org) | **GET** /orgs/{orgid}/builds | List all builds for org
[**get_share**](BuildsApi.md#get_share) | **GET** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds/{number}/share | Get the share link
[**resign_build_artifact**](BuildsApi.md#resign_build_artifact) | **POST** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds/{number}/resign | Re-sign a build artifact
[**revoke_share**](BuildsApi.md#revoke_share) | **DELETE** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds/{number}/share | Revoke a shared link
[**start_builds**](BuildsApi.md#start_builds) | **POST** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds | Create new build
[**update_build**](BuildsApi.md#update_build) | **PUT** /orgs/{orgid}/projects/{projectid}/buildtargets/{buildtargetid}/builds/{number} | Update build information


# **batch_delete_build_artifacts**
> str batch_delete_build_artifacts(orgid, projectid, options)

Delete artifacts for a batch of builds

Delete all artifacts associated with the builds identified by the provided build target ids and build numbers. Builds marked as do not delete or that are currently building will be ignored. 

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
options = swagger_client.Options8() # Options8 | Options to specify what builds to delete

try:
    # Delete artifacts for a batch of builds
    api_response = api_instance.batch_delete_build_artifacts(orgid, projectid, options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->batch_delete_build_artifacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **options** | [**Options8**](Options8.md)| Options to specify what builds to delete | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_all_builds**
> str cancel_all_builds(orgid, projectid, buildtargetid)

Cancel all builds

Cancel all builds in progress for this build target (or all targets, if '_all' is specified as the buildtargetid). Canceling an already finished build will do nothing and respond successfully. 

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name

try:
    # Cancel all builds
    api_response = api_instance.cancel_all_builds(orgid, projectid, buildtargetid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->cancel_all_builds: %s\n" % e)
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

# **cancel_build**
> str cancel_build(orgid, projectid, buildtargetid, number)

Cancel build

Cancel a build in progress. Canceling an already finished build will do nothing and respond successfully. 

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
number = 'number_example' # str | Build number or in some cases _all

try:
    # Cancel build
    api_response = api_instance.cancel_build(orgid, projectid, buildtargetid, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->cancel_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **number** | **str**| Build number or in some cases _all | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_builds_for_org**
> str cancel_builds_for_org(orgid)

Cancel builds for org

Cancel all in progress builds for an organization. Canceling an already finished build will do nothing and respond successfully. 

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier

try:
    # Cancel builds for org
    api_response = api_instance.cancel_builds_for_org(orgid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->cancel_builds_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_share**
> object create_share(orgid, projectid, buildtargetid, number)

Create a new link to share a project

Create a new short link to share a project. If this is called when a share already exists, that share will be revoked and a new one created.

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
number = 'number_example' # str | Build number or in some cases _all

try:
    # Create a new link to share a project
    api_response = api_instance.create_share(orgid, projectid, buildtargetid, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->create_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **number** | **str**| Build number or in some cases _all | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_build_artifacts**
> str delete_all_build_artifacts(orgid, projectid, buildtargetid)

Delete all artifacts associated with all non-favorited builds for a specified buildtargetid (_all is allowed).

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name

try:
    # Delete all artifacts associated with all non-favorited builds for a specified buildtargetid (_all is allowed).
    api_response = api_instance.delete_all_build_artifacts(orgid, projectid, buildtargetid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->delete_all_build_artifacts: %s\n" % e)
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

# **delete_build_artifacts**
> str delete_build_artifacts(orgid, projectid, buildtargetid, number)

Delete all artifacts associated with a specific build

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
number = 'number_example' # str | Build number or in some cases _all

try:
    # Delete all artifacts associated with a specific build
    api_response = api_instance.delete_build_artifacts(orgid, projectid, buildtargetid, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->delete_build_artifacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **number** | **str**| Build number or in some cases _all | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_log**
> list[InlineResponse2006] get_audit_log(orgid, projectid, buildtargetid, number, per_page=per_page, page=page)

Get audit log

Retrieve a list of settings changes between the last and current build.

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
number = 'number_example' # str | Build number or in some cases _all
per_page = 25 # float | Number of audit log records to retrieve (optional) (default to 25)
page = 1 # float | Skip to page number, based on per_page value (optional) (default to 1)

try:
    # Get audit log
    api_response = api_instance.get_audit_log(orgid, projectid, buildtargetid, number, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->get_audit_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **number** | **str**| Build number or in some cases _all | 
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

# **get_audit_log_for_build_target**
> list[InlineResponse2006] get_audit_log_for_build_target(orgid, projectid, buildtargetid, per_page=per_page, page=page)

Get audit log

Retrieve a list of historical settings changes for this build target.

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
per_page = 25 # float | Number of audit log records to retrieve (optional) (default to 25)
page = 1 # float | Skip to page number, based on per_page value (optional) (default to 1)

try:
    # Get audit log
    api_response = api_instance.get_audit_log_for_build_target(orgid, projectid, buildtargetid, per_page=per_page, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->get_audit_log_for_build_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
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

# **get_build**
> object get_build(orgid, projectid, buildtargetid, number, include=include)

Build Status

Retrieve information for a specific build. A Build resource contains information related to a build attempt for a build target, including the build number, changeset, build times, and other pertinent data. 

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
# Configure OAuth2 access token for authorization: permissions
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
number = 'number_example' # str | Build number or in some cases _all
include = 'include_example' # str | Extra fields to include in the response (optional)

try:
    # Build Status
    api_response = api_instance.get_build(orgid, projectid, buildtargetid, number, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->get_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **number** | **str**| Build number or in some cases _all | 
 **include** | **str**| Extra fields to include in the response | [optional] 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [filetoken](../README.md#filetoken), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_log**
> get_build_log(orgid, projectid, buildtargetid, number, offsetlines=offsetlines, linenumbers=linenumbers, last_line_number=last_line_number, compact=compact, with_html=with_html)

Get build log

Retrieve the plain text log for a specifc build.

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
number = 'number_example' # str | Build number or in some cases _all
offsetlines = 1 # float | Stream log from the given line number (optional) (default to 1)
linenumbers = false # bool | Include log line numbers in the text output (optional) (default to false)
last_line_number = 0 # float | The last line number seen, numbering will continue from here (optional) (default to 0)
compact = false # bool | Return the compact log, showing only errors and warnings (optional) (default to false)
with_html = false # bool | Surround important lines (errors, warnings) with SPAN and CSS markup  (optional) (default to false)

try:
    # Get build log
    api_instance.get_build_log(orgid, projectid, buildtargetid, number, offsetlines=offsetlines, linenumbers=linenumbers, last_line_number=last_line_number, compact=compact, with_html=with_html)
except ApiException as e:
    print("Exception when calling BuildsApi->get_build_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **number** | **str**| Build number or in some cases _all | 
 **offsetlines** | **float**| Stream log from the given line number | [optional] [default to 1]
 **linenumbers** | **bool**| Include log line numbers in the text output | [optional] [default to false]
 **last_line_number** | **float**| The last line number seen, numbering will continue from here | [optional] [default to 0]
 **compact** | **bool**| Return the compact log, showing only errors and warnings | [optional] [default to false]
 **with_html** | **bool**| Surround important lines (errors, warnings) with SPAN and CSS markup  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build_steps**
> list[InlineResponse20011] get_build_steps(orgid, projectid, buildtargetid, number)

Get the build steps for a given build

Retrieves all build steps for a build, this replaces the old method where we would manually download the build report artifacts and allows us to add more functionality into build steps. 

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
number = 'number_example' # str | Build number or in some cases _all

try:
    # Get the build steps for a given build
    api_response = api_instance.get_build_steps(orgid, projectid, buildtargetid, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->get_build_steps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **number** | **str**| Build number or in some cases _all | 

### Return type

[**list[InlineResponse20011]**](InlineResponse20011.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_builds**
> list[OrgsorgidprojectsprojectidbuildtargetsBuilds] get_builds(orgid, projectid, buildtargetid, include=include, per_page=per_page, page=page, build_status=build_status, platform=platform, show_deleted=show_deleted, only_favorites=only_favorites, clean_build=clean_build)

List all builds

List all running and finished builds, sorted by build number (optionally paginating the results). Use '_all' as the buildtargetid to get all configured build targets. The response includes a Content-Range header that identifies the range of results returned and the total number of results matching the given query parameters. 

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
include = 'include_example' # str | Extra fields to include in the response (optional)
per_page = 25 # float | Number of audit log records to retrieve (optional) (default to 25)
page = 1 # float | Skip to page number, based on per_page value (optional) (default to 1)
build_status = '' # str | Query for only builds of a specific status (optional) (default to )
platform = '' # str | Query for only builds of a specific platform (optional) (default to )
show_deleted = false # bool | Query for builds that have been deleted (optional) (default to false)
only_favorites = false # bool | Query for builds that have been favorited (optional) (default to false)
clean_build = true # bool | Query for builds that have either been built clean or using caches (optional)

try:
    # List all builds
    api_response = api_instance.get_builds(orgid, projectid, buildtargetid, include=include, per_page=per_page, page=page, build_status=build_status, platform=platform, show_deleted=show_deleted, only_favorites=only_favorites, clean_build=clean_build)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->get_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **include** | **str**| Extra fields to include in the response | [optional] 
 **per_page** | **float**| Number of audit log records to retrieve | [optional] [default to 25]
 **page** | **float**| Skip to page number, based on per_page value | [optional] [default to 1]
 **build_status** | **str**| Query for only builds of a specific status | [optional] [default to ]
 **platform** | **str**| Query for only builds of a specific platform | [optional] [default to ]
 **show_deleted** | **bool**| Query for builds that have been deleted | [optional] [default to false]
 **only_favorites** | **bool**| Query for builds that have been favorited | [optional] [default to false]
 **clean_build** | **bool**| Query for builds that have either been built clean or using caches | [optional] 

### Return type

[**list[OrgsorgidprojectsprojectidbuildtargetsBuilds]**](OrgsorgidprojectsprojectidbuildtargetsBuilds.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_builds_for_org**
> list[OrgsorgidprojectsprojectidbuildtargetsBuilds] get_builds_for_org(orgid, include=include, per_page=per_page, page=page, build_status=build_status, platform=platform, show_deleted=show_deleted, only_favorites=only_favorites, clean_build=clean_build)

List all builds for org

List all running and finished builds, sorted by build number (optionally paginating the results). The response includes a Content-Range header that identifies the range of results returned and the total number of results matching the given query parameters. 

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
include = 'include_example' # str | Extra fields to include in the response (optional)
per_page = 25 # float | Number of audit log records to retrieve (optional) (default to 25)
page = 1 # float | Skip to page number, based on per_page value (optional) (default to 1)
build_status = '' # str | Query for only builds of a specific status (optional) (default to )
platform = '' # str | Query for only builds of a specific platform (optional) (default to )
show_deleted = false # bool | Query for builds that have been deleted (optional) (default to false)
only_favorites = false # bool | Query for builds that have been favorited (optional) (default to false)
clean_build = true # bool | Query for builds that have either been built clean or using caches (optional)

try:
    # List all builds for org
    api_response = api_instance.get_builds_for_org(orgid, include=include, per_page=per_page, page=page, build_status=build_status, platform=platform, show_deleted=show_deleted, only_favorites=only_favorites, clean_build=clean_build)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->get_builds_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **include** | **str**| Extra fields to include in the response | [optional] 
 **per_page** | **float**| Number of audit log records to retrieve | [optional] [default to 25]
 **page** | **float**| Skip to page number, based on per_page value | [optional] [default to 1]
 **build_status** | **str**| Query for only builds of a specific status | [optional] [default to ]
 **platform** | **str**| Query for only builds of a specific platform | [optional] [default to ]
 **show_deleted** | **bool**| Query for builds that have been deleted | [optional] [default to false]
 **only_favorites** | **bool**| Query for builds that have been favorited | [optional] [default to false]
 **clean_build** | **bool**| Query for builds that have either been built clean or using caches | [optional] 

### Return type

[**list[OrgsorgidprojectsprojectidbuildtargetsBuilds]**](OrgsorgidprojectsprojectidbuildtargetsBuilds.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_share**
> object get_share(orgid, projectid, buildtargetid, number)

Get the share link

Gets a share link if it exists

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
number = 'number_example' # str | Build number or in some cases _all

try:
    # Get the share link
    api_response = api_instance.get_share(orgid, projectid, buildtargetid, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->get_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **number** | **str**| Build number or in some cases _all | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resign_build_artifact**
> list[OrgsorgidprojectsprojectidbuildtargetsBuilds] resign_build_artifact(orgid, projectid, buildtargetid, number)

Re-sign a build artifact

Re-sign a build artifact using the most recent credentials associated with the buildtarget. 

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
number = 'number_example' # str | Build number or in some cases _all

try:
    # Re-sign a build artifact
    api_response = api_instance.resign_build_artifact(orgid, projectid, buildtargetid, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->resign_build_artifact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **number** | **str**| Build number or in some cases _all | 

### Return type

[**list[OrgsorgidprojectsprojectidbuildtargetsBuilds]**](OrgsorgidprojectsprojectidbuildtargetsBuilds.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_share**
> str revoke_share(orgid, projectid, buildtargetid, number)

Revoke a shared link

Revoke a shared link, both {buildtargetid} and {number} may use _all to revoke all share links for a given buildtarget or entire project.

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
number = 'number_example' # str | Build number or in some cases _all

try:
    # Revoke a shared link
    api_response = api_instance.revoke_share(orgid, projectid, buildtargetid, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->revoke_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **number** | **str**| Build number or in some cases _all | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_builds**
> list[OrgsorgidprojectsprojectidbuildtargetsBuilds] start_builds(orgid, projectid, buildtargetid, options=options)

Create new build

Start the build process for this build target (or all targets, if '_all' is specified as the buildtargetid), if there is not one currently in process.  If a build is currently in process that information will be related in the 'error' field. 

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
options = swagger_client.Options9() # Options9 | Options for starting the builds. You can specify a platform and label only when  starting a local (_local) build. A local build will return immediately and be  marked as successful.  (optional)

try:
    # Create new build
    api_response = api_instance.start_builds(orgid, projectid, buildtargetid, options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->start_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **options** | [**Options9**](Options9.md)| Options for starting the builds. You can specify a platform and label only when  starting a local (_local) build. A local build will return immediately and be  marked as successful.  | [optional] 

### Return type

[**list[OrgsorgidprojectsprojectidbuildtargetsBuilds]**](OrgsorgidprojectsprojectidbuildtargetsBuilds.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_build**
> object update_build(orgid, projectid, buildtargetid, number, options)

Update build information

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
api_instance = swagger_client.BuildsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
buildtargetid = 'buildtargetid_example' # str | unique id auto-generated from the build target name
number = 'number_example' # str | Build number or in some cases _all
options = swagger_client.Options10() # Options10 | Options for build update

try:
    # Update build information
    api_response = api_instance.update_build(orgid, projectid, buildtargetid, number, options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildsApi->update_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **buildtargetid** | **str**| unique id auto-generated from the build target name | 
 **number** | **str**| Build number or in some cases _all | 
 **options** | [**Options10**](Options10.md)| Options for build update | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

