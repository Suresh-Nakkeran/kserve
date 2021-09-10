#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    KFServing

    Python SDK for KFServing  # noqa: E501

    The version of the OpenAPI document: v0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kserve.configuration import Configuration


class V1alpha2XGBoostSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'nthread': 'int',
        'resources': 'V1ResourceRequirements',
        'runtime_version': 'str',
        'storage_uri': 'str'
    }

    attribute_map = {
        'nthread': 'nthread',
        'resources': 'resources',
        'runtime_version': 'runtimeVersion',
        'storage_uri': 'storageUri'
    }

    def __init__(self, nthread=None, resources=None, runtime_version=None, storage_uri=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha2XGBoostSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._nthread = None
        self._resources = None
        self._runtime_version = None
        self._storage_uri = None
        self.discriminator = None

        if nthread is not None:
            self.nthread = nthread
        if resources is not None:
            self.resources = resources
        if runtime_version is not None:
            self.runtime_version = runtime_version
        self.storage_uri = storage_uri

    @property
    def nthread(self):
        """Gets the nthread of this V1alpha2XGBoostSpec.  # noqa: E501

        Number of thread to be used by XGBoost  # noqa: E501

        :return: The nthread of this V1alpha2XGBoostSpec.  # noqa: E501
        :rtype: int
        """
        return self._nthread

    @nthread.setter
    def nthread(self, nthread):
        """Sets the nthread of this V1alpha2XGBoostSpec.

        Number of thread to be used by XGBoost  # noqa: E501

        :param nthread: The nthread of this V1alpha2XGBoostSpec.  # noqa: E501
        :type: int
        """

        self._nthread = nthread

    @property
    def resources(self):
        """Gets the resources of this V1alpha2XGBoostSpec.  # noqa: E501


        :return: The resources of this V1alpha2XGBoostSpec.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this V1alpha2XGBoostSpec.


        :param resources: The resources of this V1alpha2XGBoostSpec.  # noqa: E501
        :type: V1ResourceRequirements
        """

        self._resources = resources

    @property
    def runtime_version(self):
        """Gets the runtime_version of this V1alpha2XGBoostSpec.  # noqa: E501

        XGBoost KFServer docker image version which defaults to latest release  # noqa: E501

        :return: The runtime_version of this V1alpha2XGBoostSpec.  # noqa: E501
        :rtype: str
        """
        return self._runtime_version

    @runtime_version.setter
    def runtime_version(self, runtime_version):
        """Sets the runtime_version of this V1alpha2XGBoostSpec.

        XGBoost KFServer docker image version which defaults to latest release  # noqa: E501

        :param runtime_version: The runtime_version of this V1alpha2XGBoostSpec.  # noqa: E501
        :type: str
        """

        self._runtime_version = runtime_version

    @property
    def storage_uri(self):
        """Gets the storage_uri of this V1alpha2XGBoostSpec.  # noqa: E501

        The URI of the trained model which contains model.bst  # noqa: E501

        :return: The storage_uri of this V1alpha2XGBoostSpec.  # noqa: E501
        :rtype: str
        """
        return self._storage_uri

    @storage_uri.setter
    def storage_uri(self, storage_uri):
        """Sets the storage_uri of this V1alpha2XGBoostSpec.

        The URI of the trained model which contains model.bst  # noqa: E501

        :param storage_uri: The storage_uri of this V1alpha2XGBoostSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and storage_uri is None:  # noqa: E501
            raise ValueError("Invalid value for `storage_uri`, must not be `None`")  # noqa: E501

        self._storage_uri = storage_uri

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha2XGBoostSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha2XGBoostSpec):
            return True

        return self.to_dict() != other.to_dict()
