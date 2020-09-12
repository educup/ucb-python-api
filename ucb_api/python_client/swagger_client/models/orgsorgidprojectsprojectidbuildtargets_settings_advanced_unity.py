# coding: utf-8

"""
    Unity Cloud Build

    This API is intended to be used in conjunction with the Unity Cloud Build service. A tool for building your Unity projects in the Cloud.  See https://developer.cloud.unity3d.com for more information.  ## Making requests This website is built to allow requests to be made against the API. If you are currently logged into Cloud Build you should be able to make requests without entering an API key.   You can find your API key in the Unity Cloud Services portal by clicking on 'Cloud Build Preferences' in the sidebar. Copy the API Key and paste it into the upper left corner of this website. It will be used in all subsequent requests.  ## Clients The Unity Cloud Build API is based upon Swagger. Client libraries to integrate with your projects can easily be generated with the [Swagger Code Generator](https://github.com/swagger-api/swagger-codegen).  The JSON schema required to generate a client for this API version is located here:  ``` [API_URL][BASE_PATH]/api.json ```  ## Authorization The Unity Cloud Build API requires an access token from your Unity Cloud Build account, which can be found at https://build.cloud.unity3d.com/login/me  To authenticate requests, include a Basic Authentication header with your API key as the value. e.g.  ``` Authorization: Basic [YOUR API KEY] ```  ## Pagination Paged results will take two parameters. A page number that is calculated based upon the per_page amount. For instance if there are 40 results and you specify page 2 with per_page set to 10 you will receive records 11-20.  Paged results will also return a Content-Range header. For the example above the content range header would look like this:  ``` Content-Range: items 11-20/40 ```  ## Versioning The API version is indicated in the request URL. Upgrading to a newer API version can be done by changing the path.  The API will receive a new version in the following cases:    * removal of a path or request type   * addition of a required field   * removal of a required field  The following changes are considered backwards compatible and will not trigger a new API version:    * addition of an endpoint or request type   * addition of an optional field   * removal of an optional field   * changes to the format of ids  ## Identifiers It should not be assumed that any of the identifiers used in paths will be a perfect match for your user-entered information. If you see unexpected 403s or 404s from API calls then check your identifiers match the ones used by the API. In particular, `projectId` does NOT typically change when the project is renamed and in fact may not be a direct match for the project name even at initial creation time.  To avoid confusion we recommend that instead of using the human-readable autogenerated orgId and projectId available from the API you should instead use:   * org foreign key for `orgId` (available from project APIs as `orgFk` and org APIs as `coreForeignKey`)   * `guid` for `projectId`  All links generated by the API and the Dashboard should follow this format already, making it easy to figure out the correct parameters by making a comparison.  ## Rate Limiting Requests against the Cloud Build API are limited to a rate of 100 per minute. To preserve the quality of service throughout Cloud Build, additional rate limits may apply to some actions. For example, polling aggressively instead of using webhooks or making API calls with a high concurrency may result in rate limiting.  It is not intended for these rate limits to interfere with any legitimate use of the API. Please contact support at <cloudbuild@unity3d.com> if your use is affected by this rate limit.  You can check the returned HTTP headers for any API request to see your current rate limit status.   * __X-RateLimit-Limit:__ maximum number of requests per minute   * __X-RateLimit-Remaining:__ remaining number of requests in the current window   * __X-RateLimit-Reset:__ time at which the current window will reset (UTC epoch seconds)  Once you go over the rate limit you will receive an error response: ``` HTTP Status: 429 {   \"error\": \"Rate limit exceeded, retry in XX seconds\" } ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'pre_export_method': 'str',
        'post_export_method': 'str',
        'pre_build_script': 'str',
        'post_build_script': 'str',
        'scripting_define_symbols': 'str',
        'player_exporter': 'OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityPlayerExporter',
        'player_settings': 'OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityPlayerSettings',
        'editor_user_build_settings': 'OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityEditorUserBuildSettings',
        'asset_bundles': 'OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles',
        'addressables': 'OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAddressables',
        'run_unit_tests': 'bool',
        'run_edit_mode_tests': 'bool',
        'run_play_mode_tests': 'bool',
        'failed_unit_test_fails_build': 'bool',
        'unit_test_method': 'str',
        'enable_light_bake': 'bool'
    }

    attribute_map = {
        'pre_export_method': 'preExportMethod',
        'post_export_method': 'postExportMethod',
        'pre_build_script': 'preBuildScript',
        'post_build_script': 'postBuildScript',
        'scripting_define_symbols': 'scriptingDefineSymbols',
        'player_exporter': 'playerExporter',
        'player_settings': 'playerSettings',
        'editor_user_build_settings': 'editorUserBuildSettings',
        'asset_bundles': 'assetBundles',
        'addressables': 'addressables',
        'run_unit_tests': 'runUnitTests',
        'run_edit_mode_tests': 'runEditModeTests',
        'run_play_mode_tests': 'runPlayModeTests',
        'failed_unit_test_fails_build': 'failedUnitTestFailsBuild',
        'unit_test_method': 'unitTestMethod',
        'enable_light_bake': 'enableLightBake'
    }

    def __init__(self, pre_export_method=None, post_export_method=None, pre_build_script=None, post_build_script=None, scripting_define_symbols=None, player_exporter=None, player_settings=None, editor_user_build_settings=None, asset_bundles=None, addressables=None, run_unit_tests=None, run_edit_mode_tests=None, run_play_mode_tests=None, failed_unit_test_fails_build=None, unit_test_method=None, enable_light_bake=None):  # noqa: E501
        """OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity - a model defined in Swagger"""  # noqa: E501

        self._pre_export_method = None
        self._post_export_method = None
        self._pre_build_script = None
        self._post_build_script = None
        self._scripting_define_symbols = None
        self._player_exporter = None
        self._player_settings = None
        self._editor_user_build_settings = None
        self._asset_bundles = None
        self._addressables = None
        self._run_unit_tests = None
        self._run_edit_mode_tests = None
        self._run_play_mode_tests = None
        self._failed_unit_test_fails_build = None
        self._unit_test_method = None
        self._enable_light_bake = None
        self.discriminator = None

        if pre_export_method is not None:
            self.pre_export_method = pre_export_method
        if post_export_method is not None:
            self.post_export_method = post_export_method
        if pre_build_script is not None:
            self.pre_build_script = pre_build_script
        if post_build_script is not None:
            self.post_build_script = post_build_script
        if scripting_define_symbols is not None:
            self.scripting_define_symbols = scripting_define_symbols
        if player_exporter is not None:
            self.player_exporter = player_exporter
        if player_settings is not None:
            self.player_settings = player_settings
        if editor_user_build_settings is not None:
            self.editor_user_build_settings = editor_user_build_settings
        if asset_bundles is not None:
            self.asset_bundles = asset_bundles
        if addressables is not None:
            self.addressables = addressables
        if run_unit_tests is not None:
            self.run_unit_tests = run_unit_tests
        if run_edit_mode_tests is not None:
            self.run_edit_mode_tests = run_edit_mode_tests
        if run_play_mode_tests is not None:
            self.run_play_mode_tests = run_play_mode_tests
        if failed_unit_test_fails_build is not None:
            self.failed_unit_test_fails_build = failed_unit_test_fails_build
        if unit_test_method is not None:
            self.unit_test_method = unit_test_method
        if enable_light_bake is not None:
            self.enable_light_bake = enable_light_bake

    @property
    def pre_export_method(self):
        """Gets the pre_export_method of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501

        The fully-qualified name of a public static method you want us to call before we start the Unity build process. For example: ClassName.NeatMethod or NameSpace.ClassName.NeatMethod. No trailing parenthesis, and it can't have the same name as your Post-Export method!  # noqa: E501

        :return: The pre_export_method of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: str
        """
        return self._pre_export_method

    @pre_export_method.setter
    def pre_export_method(self, pre_export_method):
        """Sets the pre_export_method of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.

        The fully-qualified name of a public static method you want us to call before we start the Unity build process. For example: ClassName.NeatMethod or NameSpace.ClassName.NeatMethod. No trailing parenthesis, and it can't have the same name as your Post-Export method!  # noqa: E501

        :param pre_export_method: The pre_export_method of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: str
        """

        self._pre_export_method = pre_export_method

    @property
    def post_export_method(self):
        """Gets the post_export_method of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501

        The fully-qualified name of a public static method you want us to call after we finish the Unity build process (but before Xcode). For example: ClassName.CoolMethod or NameSpace.ClassName.CoolMethod. No trailing parenthesis, and it can't have the same name as your Post-Export method! This method must accept a string parameter, which will receive the path to the exported Unity player (or Xcode project in the case of iOS).  # noqa: E501

        :return: The post_export_method of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: str
        """
        return self._post_export_method

    @post_export_method.setter
    def post_export_method(self, post_export_method):
        """Sets the post_export_method of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.

        The fully-qualified name of a public static method you want us to call after we finish the Unity build process (but before Xcode). For example: ClassName.CoolMethod or NameSpace.ClassName.CoolMethod. No trailing parenthesis, and it can't have the same name as your Post-Export method! This method must accept a string parameter, which will receive the path to the exported Unity player (or Xcode project in the case of iOS).  # noqa: E501

        :param post_export_method: The post_export_method of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: str
        """

        self._post_export_method = post_export_method

    @property
    def pre_build_script(self):
        """Gets the pre_build_script of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501

        Relative path to the script that should be run before the build process starts.  # noqa: E501

        :return: The pre_build_script of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: str
        """
        return self._pre_build_script

    @pre_build_script.setter
    def pre_build_script(self, pre_build_script):
        """Sets the pre_build_script of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.

        Relative path to the script that should be run before the build process starts.  # noqa: E501

        :param pre_build_script: The pre_build_script of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: str
        """

        self._pre_build_script = pre_build_script

    @property
    def post_build_script(self):
        """Gets the post_build_script of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501

        Relative path to the script that should be run after the build process finishes.  # noqa: E501

        :return: The post_build_script of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: str
        """
        return self._post_build_script

    @post_build_script.setter
    def post_build_script(self, post_build_script):
        """Sets the post_build_script of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.

        Relative path to the script that should be run after the build process finishes.  # noqa: E501

        :param post_build_script: The post_build_script of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: str
        """

        self._post_build_script = post_build_script

    @property
    def scripting_define_symbols(self):
        """Gets the scripting_define_symbols of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501

        Enter the names of the symbols you want to define for iOS. These symbols can then be used as the conditions for #if directives just like the built-in ones. (i.e. #IF MYDEFINE or #IF AMAZON)  # noqa: E501

        :return: The scripting_define_symbols of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: str
        """
        return self._scripting_define_symbols

    @scripting_define_symbols.setter
    def scripting_define_symbols(self, scripting_define_symbols):
        """Sets the scripting_define_symbols of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.

        Enter the names of the symbols you want to define for iOS. These symbols can then be used as the conditions for #if directives just like the built-in ones. (i.e. #IF MYDEFINE or #IF AMAZON)  # noqa: E501

        :param scripting_define_symbols: The scripting_define_symbols of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: str
        """

        self._scripting_define_symbols = scripting_define_symbols

    @property
    def player_exporter(self):
        """Gets the player_exporter of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501


        :return: The player_exporter of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityPlayerExporter
        """
        return self._player_exporter

    @player_exporter.setter
    def player_exporter(self, player_exporter):
        """Sets the player_exporter of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.


        :param player_exporter: The player_exporter of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityPlayerExporter
        """

        self._player_exporter = player_exporter

    @property
    def player_settings(self):
        """Gets the player_settings of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501


        :return: The player_settings of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityPlayerSettings
        """
        return self._player_settings

    @player_settings.setter
    def player_settings(self, player_settings):
        """Sets the player_settings of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.


        :param player_settings: The player_settings of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityPlayerSettings
        """

        self._player_settings = player_settings

    @property
    def editor_user_build_settings(self):
        """Gets the editor_user_build_settings of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501


        :return: The editor_user_build_settings of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityEditorUserBuildSettings
        """
        return self._editor_user_build_settings

    @editor_user_build_settings.setter
    def editor_user_build_settings(self, editor_user_build_settings):
        """Sets the editor_user_build_settings of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.


        :param editor_user_build_settings: The editor_user_build_settings of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityEditorUserBuildSettings
        """

        self._editor_user_build_settings = editor_user_build_settings

    @property
    def asset_bundles(self):
        """Gets the asset_bundles of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501


        :return: The asset_bundles of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles
        """
        return self._asset_bundles

    @asset_bundles.setter
    def asset_bundles(self, asset_bundles):
        """Sets the asset_bundles of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.


        :param asset_bundles: The asset_bundles of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles
        """

        self._asset_bundles = asset_bundles

    @property
    def addressables(self):
        """Gets the addressables of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501


        :return: The addressables of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAddressables
        """
        return self._addressables

    @addressables.setter
    def addressables(self, addressables):
        """Sets the addressables of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.


        :param addressables: The addressables of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAddressables
        """

        self._addressables = addressables

    @property
    def run_unit_tests(self):
        """Gets the run_unit_tests of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501

        Run any unit tests your project has when a build happens.  # noqa: E501

        :return: The run_unit_tests of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: bool
        """
        return self._run_unit_tests

    @run_unit_tests.setter
    def run_unit_tests(self, run_unit_tests):
        """Sets the run_unit_tests of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.

        Run any unit tests your project has when a build happens.  # noqa: E501

        :param run_unit_tests: The run_unit_tests of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: bool
        """

        self._run_unit_tests = run_unit_tests

    @property
    def run_edit_mode_tests(self):
        """Gets the run_edit_mode_tests of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501

        Should Edit Mode unit tests be run? NOTE: requires runUnitTests to be true and building with Unity 5.6 or newer.  # noqa: E501

        :return: The run_edit_mode_tests of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: bool
        """
        return self._run_edit_mode_tests

    @run_edit_mode_tests.setter
    def run_edit_mode_tests(self, run_edit_mode_tests):
        """Sets the run_edit_mode_tests of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.

        Should Edit Mode unit tests be run? NOTE: requires runUnitTests to be true and building with Unity 5.6 or newer.  # noqa: E501

        :param run_edit_mode_tests: The run_edit_mode_tests of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: bool
        """

        self._run_edit_mode_tests = run_edit_mode_tests

    @property
    def run_play_mode_tests(self):
        """Gets the run_play_mode_tests of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501

        Should Play Mode unit tests be run? NOTE: requires runUnitTests to be true and building with Unity 5.6 or newer.  # noqa: E501

        :return: The run_play_mode_tests of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: bool
        """
        return self._run_play_mode_tests

    @run_play_mode_tests.setter
    def run_play_mode_tests(self, run_play_mode_tests):
        """Sets the run_play_mode_tests of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.

        Should Play Mode unit tests be run? NOTE: requires runUnitTests to be true and building with Unity 5.6 or newer.  # noqa: E501

        :param run_play_mode_tests: The run_play_mode_tests of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: bool
        """

        self._run_play_mode_tests = run_play_mode_tests

    @property
    def failed_unit_test_fails_build(self):
        """Gets the failed_unit_test_fails_build of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501

        Mark builds as failed if the unit tests do not pass.  # noqa: E501

        :return: The failed_unit_test_fails_build of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: bool
        """
        return self._failed_unit_test_fails_build

    @failed_unit_test_fails_build.setter
    def failed_unit_test_fails_build(self, failed_unit_test_fails_build):
        """Sets the failed_unit_test_fails_build of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.

        Mark builds as failed if the unit tests do not pass.  # noqa: E501

        :param failed_unit_test_fails_build: The failed_unit_test_fails_build of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: bool
        """

        self._failed_unit_test_fails_build = failed_unit_test_fails_build

    @property
    def unit_test_method(self):
        """Gets the unit_test_method of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501

        LEGACY - The Unity method to call when running unit tests (only supported in Unity 5.2 and lower).  # noqa: E501

        :return: The unit_test_method of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: str
        """
        return self._unit_test_method

    @unit_test_method.setter
    def unit_test_method(self, unit_test_method):
        """Sets the unit_test_method of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.

        LEGACY - The Unity method to call when running unit tests (only supported in Unity 5.2 and lower).  # noqa: E501

        :param unit_test_method: The unit_test_method of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: str
        """

        self._unit_test_method = unit_test_method

    @property
    def enable_light_bake(self):
        """Gets the enable_light_bake of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501

        Enable lightmap baking (disabled by default since it is very slow and usually unnecessary)  # noqa: E501

        :return: The enable_light_bake of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :rtype: bool
        """
        return self._enable_light_bake

    @enable_light_bake.setter
    def enable_light_bake(self, enable_light_bake):
        """Sets the enable_light_bake of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.

        Enable lightmap baking (disabled by default since it is very slow and usually unnecessary)  # noqa: E501

        :param enable_light_bake: The enable_light_bake of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity.  # noqa: E501
        :type: bool
        """

        self._enable_light_bake = enable_light_bake

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other