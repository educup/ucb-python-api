# OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_bundles** | **bool** | enable asset bundle builds for this target | [optional] 
**base_path** | **str** | base path relative to Assets folder where asset bundles are output. Default is &#39;AssetBundles&#39; | [optional] 
**build_asset_bundle_options** | **str** | comma separated list of flags from BuildAssetBundleOptions. see https://docs.unity3d.com/ScriptReference/BuildAssetBundleOptions.html | [optional] 
**copy_to_streaming_assets** | **bool** | copy bundles to streaming assets folder, which will be packaged into the exported player. | [optional] 
**copy_bundle_patterns** | **list[str]** | array of patterns to match (C# Regular Expressions) when copying asset bundle files. By default, all bundles will be copied. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


