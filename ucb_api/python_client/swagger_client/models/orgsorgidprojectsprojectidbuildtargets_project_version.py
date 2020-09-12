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


class OrgsorgidprojectsprojectidbuildtargetsProjectVersion(object):
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
        'name': 'str',
        'filename': 'str',
        'project_name': 'str',
        'platform': 'str',
        'size': 'float',
        'created': 'str',
        'last_mod': 'str',
        'bundle_id': 'str',
        'udids': 'list[str]',
        'links': 'object'
    }

    attribute_map = {
        'name': 'name',
        'filename': 'filename',
        'project_name': 'projectName',
        'platform': 'platform',
        'size': 'size',
        'created': 'created',
        'last_mod': 'lastMod',
        'bundle_id': 'bundleId',
        'udids': 'udids',
        'links': 'links'
    }

    def __init__(self, name=None, filename=None, project_name=None, platform=None, size=None, created=None, last_mod=None, bundle_id=None, udids=None, links=None):  # noqa: E501
        """OrgsorgidprojectsprojectidbuildtargetsProjectVersion - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._filename = None
        self._project_name = None
        self._platform = None
        self._size = None
        self._created = None
        self._last_mod = None
        self._bundle_id = None
        self._udids = None
        self._links = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if filename is not None:
            self.filename = filename
        if project_name is not None:
            self.project_name = project_name
        if platform is not None:
            self.platform = platform
        if size is not None:
            self.size = size
        if created is not None:
            self.created = created
        if last_mod is not None:
            self.last_mod = last_mod
        if bundle_id is not None:
            self.bundle_id = bundle_id
        if udids is not None:
            self.udids = udids
        if links is not None:
            self.links = links

    @property
    def name(self):
        """Gets the name of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501

        automatically generated name for the build  # noqa: E501

        :return: The name of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.

        automatically generated name for the build  # noqa: E501

        :param name: The name of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def filename(self):
        """Gets the filename of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501

        filename for the primary artifact  # noqa: E501

        :return: The filename of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.

        filename for the primary artifact  # noqa: E501

        :param filename: The filename of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def project_name(self):
        """Gets the project_name of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501

        name of the project  # noqa: E501

        :return: The project_name of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.

        name of the project  # noqa: E501

        :param project_name: The project_name of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def platform(self):
        """Gets the platform of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501


        :return: The platform of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.


        :param platform: The platform of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :type: str
        """
        allowed_values = ["ios", "android", "webplayer", "webgl", "standaloneosxintel", "standaloneosxintel64", "standaloneosxuniversal", "standalonewindows", "standalonewindows64", "standalonelinux", "standalonelinux64", "standalonelinuxuniversal"]  # noqa: E501
        if platform not in allowed_values:
            raise ValueError(
                "Invalid value for `platform` ({0}), must be one of {1}"  # noqa: E501
                .format(platform, allowed_values)
            )

        self._platform = platform

    @property
    def size(self):
        """Gets the size of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501

        size of the the primary build artifact in bytes  # noqa: E501

        :return: The size of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.

        size of the the primary build artifact in bytes  # noqa: E501

        :param size: The size of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :type: float
        """

        self._size = size

    @property
    def created(self):
        """Gets the created of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501

        creation date  # noqa: E501

        :return: The created of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.

        creation date  # noqa: E501

        :param created: The created of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def last_mod(self):
        """Gets the last_mod of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501

        last modified date  # noqa: E501

        :return: The last_mod of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._last_mod

    @last_mod.setter
    def last_mod(self, last_mod):
        """Sets the last_mod of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.

        last modified date  # noqa: E501

        :param last_mod: The last_mod of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :type: str
        """

        self._last_mod = last_mod

    @property
    def bundle_id(self):
        """Gets the bundle_id of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501

        a unique identifier (com.example.name)  # noqa: E501

        :return: The bundle_id of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :rtype: str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.

        a unique identifier (com.example.name)  # noqa: E501

        :param bundle_id: The bundle_id of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :type: str
        """

        self._bundle_id = bundle_id

    @property
    def udids(self):
        """Gets the udids of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501

        iPhone unique identifiers that are able to install this build  # noqa: E501

        :return: The udids of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :rtype: list[str]
        """
        return self._udids

    @udids.setter
    def udids(self, udids):
        """Sets the udids of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.

        iPhone unique identifiers that are able to install this build  # noqa: E501

        :param udids: The udids of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :type: list[str]
        """

        self._udids = udids

    @property
    def links(self):
        """Gets the links of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501

        links to build artifacts  # noqa: E501

        :return: The links of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :rtype: object
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.

        links to build artifacts  # noqa: E501

        :param links: The links of this OrgsorgidprojectsprojectidbuildtargetsProjectVersion.  # noqa: E501
        :type: object
        """

        self._links = links

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
        if issubclass(OrgsorgidprojectsprojectidbuildtargetsProjectVersion, dict):
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
        if not isinstance(other, OrgsorgidprojectsprojectidbuildtargetsProjectVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
