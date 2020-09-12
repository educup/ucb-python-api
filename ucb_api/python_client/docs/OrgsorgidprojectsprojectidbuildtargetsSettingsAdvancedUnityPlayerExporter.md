# OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityPlayerExporter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scene_list** | **list[str]** | A list of scenes to build overriding those specified in the Build Settings menu of your Unity project. | [optional] 
**build_options** | **list[str]** | Unity Editor build options. Use BuildOptions.Development and BuildOptions.AllowDebugging to create a development build. | [optional] 
**export** | **bool** | Enable exporting a player from Unity (i.e. running BuildPipeline.BuildPlayer). In general, this should be true, unless you are doing something like an asset bundle only build or unit test only build without generating an actual build artifact. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


