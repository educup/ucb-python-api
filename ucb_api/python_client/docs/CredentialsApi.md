# swagger_client.CredentialsApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_credentials_android**](CredentialsApi.md#add_credentials_android) | **POST** /orgs/{orgid}/projects/{projectid}/credentials/signing/android | Upload Android Credentials
[**add_credentials_android_for_org**](CredentialsApi.md#add_credentials_android_for_org) | **POST** /orgs/{orgid}/credentials/signing/android | Upload Android Credentials
[**add_credentials_ios**](CredentialsApi.md#add_credentials_ios) | **POST** /orgs/{orgid}/projects/{projectid}/credentials/signing/ios | Upload iOS Credentials
[**add_credentials_ios_for_org**](CredentialsApi.md#add_credentials_ios_for_org) | **POST** /orgs/{orgid}/credentials/signing/ios | Upload iOS Credentials for organization
[**add_credentials_osx**](CredentialsApi.md#add_credentials_osx) | **POST** /orgs/{orgid}/projects/{projectid}/credentials/signing/osx | Upload OSX Credentials
[**add_credentials_osx_for_org**](CredentialsApi.md#add_credentials_osx_for_org) | **POST** /orgs/{orgid}/credentials/signing/osx | Upload OSX Credentials for organization
[**delete_android**](CredentialsApi.md#delete_android) | **DELETE** /orgs/{orgid}/projects/{projectid}/credentials/signing/android/{credentialid} | Delete Android Credentials
[**delete_android_for_org**](CredentialsApi.md#delete_android_for_org) | **DELETE** /orgs/{orgid}/credentials/signing/android/{credentialid} | Delete Android Credentials for organization
[**delete_ios**](CredentialsApi.md#delete_ios) | **DELETE** /orgs/{orgid}/projects/{projectid}/credentials/signing/ios/{credentialid} | Delete iOS Credentials
[**delete_ios_for_org**](CredentialsApi.md#delete_ios_for_org) | **DELETE** /orgs/{orgid}/credentials/signing/ios/{credentialid} | Delete iOS Credentials for organization
[**delete_osx**](CredentialsApi.md#delete_osx) | **DELETE** /orgs/{orgid}/projects/{projectid}/credentials/signing/osx/{credentialid} | Delete OSX Credentials
[**delete_osx_for_org**](CredentialsApi.md#delete_osx_for_org) | **DELETE** /orgs/{orgid}/credentials/signing/osx/{credentialid} | Delete OSX Credentials for organization
[**get_all_android**](CredentialsApi.md#get_all_android) | **GET** /orgs/{orgid}/projects/{projectid}/credentials/signing/android | Get All Android Credentials
[**get_all_android_for_org**](CredentialsApi.md#get_all_android_for_org) | **GET** /orgs/{orgid}/credentials/signing/android | Get All Android Credentials for an organization
[**get_all_ios**](CredentialsApi.md#get_all_ios) | **GET** /orgs/{orgid}/projects/{projectid}/credentials/signing/ios | Get All iOS Credentials
[**get_all_ios_for_org**](CredentialsApi.md#get_all_ios_for_org) | **GET** /orgs/{orgid}/credentials/signing/ios | Get All iOS Credentials for an oganization
[**get_all_osx**](CredentialsApi.md#get_all_osx) | **GET** /orgs/{orgid}/projects/{projectid}/credentials/signing/osx | Get All OSX Credentials
[**get_all_osx_for_org**](CredentialsApi.md#get_all_osx_for_org) | **GET** /orgs/{orgid}/credentials/signing/osx | Get All OSX Credentials for an oganization
[**get_one_android**](CredentialsApi.md#get_one_android) | **GET** /orgs/{orgid}/projects/{projectid}/credentials/signing/android/{credentialid} | Get Android Credential Details
[**get_one_android_for_org**](CredentialsApi.md#get_one_android_for_org) | **GET** /orgs/{orgid}/credentials/signing/android/{credentialid} | Get Android Credential Details for organization
[**get_one_ios**](CredentialsApi.md#get_one_ios) | **GET** /orgs/{orgid}/projects/{projectid}/credentials/signing/ios/{credentialid} | Get iOS Credential Details
[**get_one_ios_for_org**](CredentialsApi.md#get_one_ios_for_org) | **GET** /orgs/{orgid}/credentials/signing/ios/{credentialid} | Get iOS Credential Details for organization
[**get_one_osx**](CredentialsApi.md#get_one_osx) | **GET** /orgs/{orgid}/projects/{projectid}/credentials/signing/osx/{credentialid} | Get OSX Credential Details
[**get_one_osx_for_org**](CredentialsApi.md#get_one_osx_for_org) | **GET** /orgs/{orgid}/credentials/signing/osx/{credentialid} | Get OSX Credential Details for organization
[**update_android**](CredentialsApi.md#update_android) | **PUT** /orgs/{orgid}/projects/{projectid}/credentials/signing/android/{credentialid} | Update Android Credentials
[**update_android_for_org**](CredentialsApi.md#update_android_for_org) | **PUT** /orgs/{orgid}/credentials/signing/android/{credentialid} | Update Android Credentials for organization
[**update_ios**](CredentialsApi.md#update_ios) | **PUT** /orgs/{orgid}/projects/{projectid}/credentials/signing/ios/{credentialid} | Update iOS Credentials
[**update_ios_for_org**](CredentialsApi.md#update_ios_for_org) | **PUT** /orgs/{orgid}/credentials/signing/ios/{credentialid} | Update iOS Credentials for organization
[**update_osx**](CredentialsApi.md#update_osx) | **PUT** /orgs/{orgid}/projects/{projectid}/credentials/signing/osx/{credentialid} | Update OSX Credentials
[**update_osx_for_org**](CredentialsApi.md#update_osx_for_org) | **PUT** /orgs/{orgid}/credentials/signing/osx/{credentialid} | Update OSX Credentials for organization


# **add_credentials_android**
> object add_credentials_android(orgid, projectid, label, file, alias, keypass, storepass)

Upload Android Credentials

Upload a new android keystore for the project. NOTE: you must be a manager in the project's organization to add new credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
label = 'label_example' # str | Label for the uploaded credential
file = '/path/to/file.txt' # file | Keystore file
alias = 'alias_example' # str | Keystore alias
keypass = 'keypass_example' # str | Keystore keypass
storepass = 'storepass_example' # str | Keystore storepass

try:
    # Upload Android Credentials
    api_response = api_instance.add_credentials_android(orgid, projectid, label, file, alias, keypass, storepass)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->add_credentials_android: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **label** | **str**| Label for the uploaded credential | 
 **file** | **file**| Keystore file | 
 **alias** | **str**| Keystore alias | 
 **keypass** | **str**| Keystore keypass | 
 **storepass** | **str**| Keystore storepass | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_credentials_android_for_org**
> object add_credentials_android_for_org(orgid, label, file, alias, keypass, storepass)

Upload Android Credentials

Upload a new android keystore for an organization. NOTE: you must be a manager in the organization to add new credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
label = 'label_example' # str | Label for the uploaded credential
file = '/path/to/file.txt' # file | Keystore file
alias = 'alias_example' # str | Keystore alias
keypass = 'keypass_example' # str | Keystore keypass
storepass = 'storepass_example' # str | Keystore storepass

try:
    # Upload Android Credentials
    api_response = api_instance.add_credentials_android_for_org(orgid, label, file, alias, keypass, storepass)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->add_credentials_android_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **label** | **str**| Label for the uploaded credential | 
 **file** | **file**| Keystore file | 
 **alias** | **str**| Keystore alias | 
 **keypass** | **str**| Keystore keypass | 
 **storepass** | **str**| Keystore storepass | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_credentials_ios**
> object add_credentials_ios(orgid, projectid, label, file_certificate, file_provisioning_profile, certificate_pass=certificate_pass)

Upload iOS Credentials

Upload a new iOS certificate and provisioning profile for the project. NOTE: you must be a manager in the project's organization to add new credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
label = 'label_example' # str | Label for the uploaded credentials
file_certificate = '/path/to/file.txt' # file | Certificate file (.p12)
file_provisioning_profile = '/path/to/file.txt' # file | Provisioning Profile (.mobileprovision)
certificate_pass = 'certificate_pass_example' # str | Certificate (.p12) password (optional)

try:
    # Upload iOS Credentials
    api_response = api_instance.add_credentials_ios(orgid, projectid, label, file_certificate, file_provisioning_profile, certificate_pass=certificate_pass)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->add_credentials_ios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **label** | **str**| Label for the uploaded credentials | 
 **file_certificate** | **file**| Certificate file (.p12) | 
 **file_provisioning_profile** | **file**| Provisioning Profile (.mobileprovision) | 
 **certificate_pass** | **str**| Certificate (.p12) password | [optional] 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_credentials_ios_for_org**
> object add_credentials_ios_for_org(orgid, label, file_certificate, file_provisioning_profile, certificate_pass=certificate_pass)

Upload iOS Credentials for organization

Upload a new iOS certificate and provisioning profile for the organization. NOTE: you must be a manager in the organization to add new credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
label = 'label_example' # str | Label for the uploaded credentials
file_certificate = '/path/to/file.txt' # file | Certificate file (.p12)
file_provisioning_profile = '/path/to/file.txt' # file | Provisioning Profile (.mobileprovision)
certificate_pass = 'certificate_pass_example' # str | Certificate (.p12) password (optional)

try:
    # Upload iOS Credentials for organization
    api_response = api_instance.add_credentials_ios_for_org(orgid, label, file_certificate, file_provisioning_profile, certificate_pass=certificate_pass)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->add_credentials_ios_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **label** | **str**| Label for the uploaded credentials | 
 **file_certificate** | **file**| Certificate file (.p12) | 
 **file_provisioning_profile** | **file**| Provisioning Profile (.mobileprovision) | 
 **certificate_pass** | **str**| Certificate (.p12) password | [optional] 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_credentials_osx**
> object add_credentials_osx(orgid, projectid, label, certificate, apple_id_username, apple_id_password, certificate_pass=certificate_pass, entitlements_file=entitlements_file, provider_name=provider_name)

Upload OSX Credentials

Upload a new OSX certificate and provisioning profile for the project. NOTE: you must be a manager in the project's organization to add new credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
label = 'label_example' # str | Label for the uploaded credentials
certificate = '/path/to/file.txt' # file | Certificate file (.p12)
apple_id_username = 'apple_id_username_example' # str | Apple ID Username
apple_id_password = 'apple_id_password_example' # str | Apple ID Password
certificate_pass = 'certificate_pass_example' # str | Certificate (.p12) password (optional)
entitlements_file = '/path/to/file.txt' # file | Entitlements File (.entitlements) (optional)
provider_name = 'provider_name_example' # str | Provider Name (optional)

try:
    # Upload OSX Credentials
    api_response = api_instance.add_credentials_osx(orgid, projectid, label, certificate, apple_id_username, apple_id_password, certificate_pass=certificate_pass, entitlements_file=entitlements_file, provider_name=provider_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->add_credentials_osx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **label** | **str**| Label for the uploaded credentials | 
 **certificate** | **file**| Certificate file (.p12) | 
 **apple_id_username** | **str**| Apple ID Username | 
 **apple_id_password** | **str**| Apple ID Password | 
 **certificate_pass** | **str**| Certificate (.p12) password | [optional] 
 **entitlements_file** | **file**| Entitlements File (.entitlements) | [optional] 
 **provider_name** | **str**| Provider Name | [optional] 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_credentials_osx_for_org**
> object add_credentials_osx_for_org(orgid, label, certificate, apple_id_username, apple_id_password, certificate_pass=certificate_pass, entitlements_file=entitlements_file, provider_name=provider_name)

Upload OSX Credentials for organization

Upload a new OSX certificate and provisioning profile for the organization. NOTE: you must be a manager in the organization to add new credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
label = 'label_example' # str | Label for the uploaded credentials
certificate = '/path/to/file.txt' # file | Certificate file (.p12)
apple_id_username = 'apple_id_username_example' # str | Apple ID Username
apple_id_password = 'apple_id_password_example' # str | Apple ID Password
certificate_pass = 'certificate_pass_example' # str | Certificate (.p12) password (optional)
entitlements_file = '/path/to/file.txt' # file | Entitlements file (.entitlements) (optional)
provider_name = 'provider_name_example' # str | Provider Name (optional)

try:
    # Upload OSX Credentials for organization
    api_response = api_instance.add_credentials_osx_for_org(orgid, label, certificate, apple_id_username, apple_id_password, certificate_pass=certificate_pass, entitlements_file=entitlements_file, provider_name=provider_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->add_credentials_osx_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **label** | **str**| Label for the uploaded credentials | 
 **certificate** | **file**| Certificate file (.p12) | 
 **apple_id_username** | **str**| Apple ID Username | 
 **apple_id_password** | **str**| Apple ID Password | 
 **certificate_pass** | **str**| Certificate (.p12) password | [optional] 
 **entitlements_file** | **file**| Entitlements file (.entitlements) | [optional] 
 **provider_name** | **str**| Provider Name | [optional] 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_android**
> str delete_android(orgid, projectid, credentialid)

Delete Android Credentials

Delete specific android credentials for a project. NOTE: you must be a manager in the project's organization to delete credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try:
    # Delete Android Credentials
    api_response = api_instance.delete_android(orgid, projectid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->delete_android: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_android_for_org**
> str delete_android_for_org(orgid, credentialid)

Delete Android Credentials for organization

Delete specific android credentials for an organization. NOTE: you must be a manager in the organization to delete credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try:
    # Delete Android Credentials for organization
    api_response = api_instance.delete_android_for_org(orgid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->delete_android_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ios**
> str delete_ios(orgid, projectid, credentialid)

Delete iOS Credentials

Delete specific ios credentials for a project. NOTE: you must be a manager in the project's organization to delete credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try:
    # Delete iOS Credentials
    api_response = api_instance.delete_ios(orgid, projectid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->delete_ios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ios_for_org**
> str delete_ios_for_org(orgid, credentialid)

Delete iOS Credentials for organization

Delete specific ios credentials. NOTE: you must be a manager in the project's organization to delete credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try:
    # Delete iOS Credentials for organization
    api_response = api_instance.delete_ios_for_org(orgid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->delete_ios_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_osx**
> str delete_osx(orgid, projectid, credentialid)

Delete OSX Credentials

Delete specific OSX credentials for a project. NOTE: you must be a manager in the project's organization to delete credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try:
    # Delete OSX Credentials
    api_response = api_instance.delete_osx(orgid, projectid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->delete_osx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_osx_for_org**
> str delete_osx_for_org(orgid, credentialid)

Delete OSX Credentials for organization

Delete specific OSX credentials. NOTE: you must be a manager in the project's organization to delete credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try:
    # Delete OSX Credentials for organization
    api_response = api_instance.delete_osx_for_org(orgid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->delete_osx_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

**str**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_android**
> list[InlineResponse2008] get_all_android(orgid, projectid)

Get All Android Credentials

Get all credentials available for the project. A user in the projects org will see all credentials uploaded for any project within the org, whereas a user with project-level permissions will only see credentials assigned to the specific project. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier

try:
    # Get All Android Credentials
    api_response = api_instance.get_all_android(orgid, projectid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_all_android: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 

### Return type

[**list[InlineResponse2008]**](InlineResponse2008.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_android_for_org**
> list[InlineResponse2008] get_all_android_for_org(orgid)

Get All Android Credentials for an organization

Get all credentials available for the organization. A list of projects using a credential is included in the links element. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier

try:
    # Get All Android Credentials for an organization
    api_response = api_instance.get_all_android_for_org(orgid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_all_android_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 

### Return type

[**list[InlineResponse2008]**](InlineResponse2008.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ios**
> list[InlineResponse2009] get_all_ios(orgid, projectid)

Get All iOS Credentials

Get all credentials available for the project. A user in the projects org will see all credentials uploaded for any project within the org, whereas a user with project-level permissions will only see credentials assigned to the specific project. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier

try:
    # Get All iOS Credentials
    api_response = api_instance.get_all_ios(orgid, projectid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_all_ios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 

### Return type

[**list[InlineResponse2009]**](InlineResponse2009.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_ios_for_org**
> list[InlineResponse2009] get_all_ios_for_org(orgid)

Get All iOS Credentials for an oganization

Get all credentials available for the project. A user in the projects org will see all credentials uploaded for any project within the org, whereas a user with project-level permissions will only see credentials assigned to the specific project. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier

try:
    # Get All iOS Credentials for an oganization
    api_response = api_instance.get_all_ios_for_org(orgid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_all_ios_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 

### Return type

[**list[InlineResponse2009]**](InlineResponse2009.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_osx**
> list[InlineResponse20010] get_all_osx(orgid, projectid)

Get All OSX Credentials

Get all credentials available for the project. A user in the projects org will see all credentials uploaded for any project within the org, whereas a user with project-level permissions will only see credentials assigned to the specific project. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier

try:
    # Get All OSX Credentials
    api_response = api_instance.get_all_osx(orgid, projectid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_all_osx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 

### Return type

[**list[InlineResponse20010]**](InlineResponse20010.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_osx_for_org**
> list[InlineResponse20010] get_all_osx_for_org(orgid)

Get All OSX Credentials for an oganization

Get all credentials available for the project. A user in the projects org will see all credentials uploaded for any project within the org, whereas a user with project-level permissions will only see credentials assigned to the specific project. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier

try:
    # Get All OSX Credentials for an oganization
    api_response = api_instance.get_all_osx_for_org(orgid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_all_osx_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 

### Return type

[**list[InlineResponse20010]**](InlineResponse20010.md)

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_android**
> object get_one_android(orgid, projectid, credentialid)

Get Android Credential Details

Get specific android credential details

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try:
    # Get Android Credential Details
    api_response = api_instance.get_one_android(orgid, projectid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_one_android: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_android_for_org**
> object get_one_android_for_org(orgid, credentialid)

Get Android Credential Details for organization

Get specific organization android credential details

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try:
    # Get Android Credential Details for organization
    api_response = api_instance.get_one_android_for_org(orgid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_one_android_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_ios**
> object get_one_ios(orgid, projectid, credentialid)

Get iOS Credential Details

Get specific iOS credential details

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try:
    # Get iOS Credential Details
    api_response = api_instance.get_one_ios(orgid, projectid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_one_ios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_ios_for_org**
> object get_one_ios_for_org(orgid, credentialid)

Get iOS Credential Details for organization

Get specific iOS credential details

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try:
    # Get iOS Credential Details for organization
    api_response = api_instance.get_one_ios_for_org(orgid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_one_ios_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_osx**
> object get_one_osx(orgid, projectid, credentialid)

Get OSX Credential Details

Get specific OSX credential details

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try:
    # Get OSX Credential Details
    api_response = api_instance.get_one_osx(orgid, projectid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_one_osx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_osx_for_org**
> object get_one_osx_for_org(orgid, credentialid)

Get OSX Credential Details for organization

Get specific OSX credential details

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
credentialid = 'credentialid_example' # str | Credential Identifier

try:
    # Get OSX Credential Details for organization
    api_response = api_instance.get_one_osx_for_org(orgid, credentialid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->get_one_osx_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **credentialid** | **str**| Credential Identifier | 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_android**
> object update_android(orgid, projectid, credentialid, label=label, file=file, alias=alias, keypass=keypass, storepass=storepass)

Update Android Credentials

Update an android keystore for the project. NOTE: you must be a manager in the project's organization to add new credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier
label = 'label_example' # str | Label for the uploaded credential (optional)
file = '/path/to/file.txt' # file | Keystore file (optional)
alias = 'alias_example' # str | Keystore alias (optional)
keypass = 'keypass_example' # str | Keystore keypass (optional)
storepass = 'storepass_example' # str | Keystore storepass (optional)

try:
    # Update Android Credentials
    api_response = api_instance.update_android(orgid, projectid, credentialid, label=label, file=file, alias=alias, keypass=keypass, storepass=storepass)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->update_android: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 
 **label** | **str**| Label for the uploaded credential | [optional] 
 **file** | **file**| Keystore file | [optional] 
 **alias** | **str**| Keystore alias | [optional] 
 **keypass** | **str**| Keystore keypass | [optional] 
 **storepass** | **str**| Keystore storepass | [optional] 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_android_for_org**
> object update_android_for_org(orgid, credentialid, label=label, file=file, alias=alias, keypass=keypass, storepass=storepass)

Update Android Credentials for organization

Update an android keystore for the organization. NOTE: you must be a manager in the organization to update credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
credentialid = 'credentialid_example' # str | Credential Identifier
label = 'label_example' # str | Label for the uploaded credential (optional)
file = '/path/to/file.txt' # file | Keystore file (optional)
alias = 'alias_example' # str | Keystore alias (optional)
keypass = 'keypass_example' # str | Keystore keypass (optional)
storepass = 'storepass_example' # str | Keystore storepass (optional)

try:
    # Update Android Credentials for organization
    api_response = api_instance.update_android_for_org(orgid, credentialid, label=label, file=file, alias=alias, keypass=keypass, storepass=storepass)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->update_android_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **credentialid** | **str**| Credential Identifier | 
 **label** | **str**| Label for the uploaded credential | [optional] 
 **file** | **file**| Keystore file | [optional] 
 **alias** | **str**| Keystore alias | [optional] 
 **keypass** | **str**| Keystore keypass | [optional] 
 **storepass** | **str**| Keystore storepass | [optional] 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ios**
> object update_ios(orgid, projectid, credentialid, label=label, file_certificate=file_certificate, file_provisioning_profile=file_provisioning_profile, certificate_pass=certificate_pass)

Update iOS Credentials

Update an iOS certificate / provisioning profile for the project. NOTE: you must be a manager in the project's organization to update credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier
label = 'label_example' # str | Label for the updated credentials (optional)
file_certificate = '/path/to/file.txt' # file | Certificate file (.p12) (optional)
file_provisioning_profile = '/path/to/file.txt' # file | Provisioning Profile (.mobileprovision) (optional)
certificate_pass = 'certificate_pass_example' # str | Certificate (.p12) password (optional)

try:
    # Update iOS Credentials
    api_response = api_instance.update_ios(orgid, projectid, credentialid, label=label, file_certificate=file_certificate, file_provisioning_profile=file_provisioning_profile, certificate_pass=certificate_pass)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->update_ios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 
 **label** | **str**| Label for the updated credentials | [optional] 
 **file_certificate** | **file**| Certificate file (.p12) | [optional] 
 **file_provisioning_profile** | **file**| Provisioning Profile (.mobileprovision) | [optional] 
 **certificate_pass** | **str**| Certificate (.p12) password | [optional] 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ios_for_org**
> object update_ios_for_org(orgid, credentialid, label=label, file_certificate=file_certificate, file_provisioning_profile=file_provisioning_profile, certificate_pass=certificate_pass)

Update iOS Credentials for organization

Update an iOS certificate / provisioning profile. NOTE: you must be a manager in the project's organization to update credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
credentialid = 'credentialid_example' # str | Credential Identifier
label = 'label_example' # str | Label for the updated credentials (optional)
file_certificate = '/path/to/file.txt' # file | Certificate file (.p12) (optional)
file_provisioning_profile = '/path/to/file.txt' # file | Provisioning Profile (.mobileprovision) (optional)
certificate_pass = 'certificate_pass_example' # str | Certificate (.p12) password (optional)

try:
    # Update iOS Credentials for organization
    api_response = api_instance.update_ios_for_org(orgid, credentialid, label=label, file_certificate=file_certificate, file_provisioning_profile=file_provisioning_profile, certificate_pass=certificate_pass)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->update_ios_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **credentialid** | **str**| Credential Identifier | 
 **label** | **str**| Label for the updated credentials | [optional] 
 **file_certificate** | **file**| Certificate file (.p12) | [optional] 
 **file_provisioning_profile** | **file**| Provisioning Profile (.mobileprovision) | [optional] 
 **certificate_pass** | **str**| Certificate (.p12) password | [optional] 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_osx**
> object update_osx(orgid, projectid, credentialid, label=label, certificate=certificate, certificate_pass=certificate_pass, entitlements_file=entitlements_file, provider_name=provider_name, apple_id_username=apple_id_username, apple_id_password=apple_id_password)

Update OSX Credentials

Update an OSX certificate / provisioning profile for the project. NOTE: you must be a manager in the project's organization to update credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
projectid = 'projectid_example' # str | Project identifier
credentialid = 'credentialid_example' # str | Credential Identifier
label = 'label_example' # str | Label for the updated credentials (optional)
certificate = '/path/to/file.txt' # file | Certificate file (.p12) (optional)
certificate_pass = 'certificate_pass_example' # str | Certificate (.p12) password (optional)
entitlements_file = '/path/to/file.txt' # file | Entitlements File (.entitlements) (optional)
provider_name = 'provider_name_example' # str | Provider Name (optional)
apple_id_username = 'apple_id_username_example' # str | Apple ID Username (optional)
apple_id_password = 'apple_id_password_example' # str | Apple ID Password (optional)

try:
    # Update OSX Credentials
    api_response = api_instance.update_osx(orgid, projectid, credentialid, label=label, certificate=certificate, certificate_pass=certificate_pass, entitlements_file=entitlements_file, provider_name=provider_name, apple_id_username=apple_id_username, apple_id_password=apple_id_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->update_osx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **projectid** | **str**| Project identifier | 
 **credentialid** | **str**| Credential Identifier | 
 **label** | **str**| Label for the updated credentials | [optional] 
 **certificate** | **file**| Certificate file (.p12) | [optional] 
 **certificate_pass** | **str**| Certificate (.p12) password | [optional] 
 **entitlements_file** | **file**| Entitlements File (.entitlements) | [optional] 
 **provider_name** | **str**| Provider Name | [optional] 
 **apple_id_username** | **str**| Apple ID Username | [optional] 
 **apple_id_password** | **str**| Apple ID Password | [optional] 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_osx_for_org**
> object update_osx_for_org(orgid, credentialid, label=label, certificate=certificate, certificate_pass=certificate_pass, entitlements_file=entitlements_file, provider_name=provider_name, apple_id_username=apple_id_username, apple_id_password=apple_id_password)

Update OSX Credentials for organization

Update an OSX certificate / provisioning profile. NOTE: you must be a manager in the project's organization to update credentials. 

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
orgid = 'orgid_example' # str | Organization identifier
credentialid = 'credentialid_example' # str | Credential Identifier
label = 'label_example' # str | Label for the updated credentials (optional)
certificate = '/path/to/file.txt' # file | Certificate file (.p12) (optional)
certificate_pass = 'certificate_pass_example' # str | Certificate (.p12) password (optional)
entitlements_file = '/path/to/file.txt' # file | Entitlements File (.entitlements) (optional)
provider_name = 'provider_name_example' # str | Provider Name (optional)
apple_id_username = 'apple_id_username_example' # str | Apple ID Username (optional)
apple_id_password = 'apple_id_password_example' # str | Apple ID Password (optional)

try:
    # Update OSX Credentials for organization
    api_response = api_instance.update_osx_for_org(orgid, credentialid, label=label, certificate=certificate, certificate_pass=certificate_pass, entitlements_file=entitlements_file, provider_name=provider_name, apple_id_username=apple_id_username, apple_id_password=apple_id_password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->update_osx_for_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgid** | **str**| Organization identifier | 
 **credentialid** | **str**| Credential Identifier | 
 **label** | **str**| Label for the updated credentials | [optional] 
 **certificate** | **file**| Certificate file (.p12) | [optional] 
 **certificate_pass** | **str**| Certificate (.p12) password | [optional] 
 **entitlements_file** | **file**| Entitlements File (.entitlements) | [optional] 
 **provider_name** | **str**| Provider Name | [optional] 
 **apple_id_username** | **str**| Apple ID Username | [optional] 
 **apple_id_password** | **str**| Apple ID Password | [optional] 

### Return type

**object**

### Authorization

[apikey](../README.md#apikey), [permissions](../README.md#permissions)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain, text/html, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

