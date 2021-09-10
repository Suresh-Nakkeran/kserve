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


class V1alpha2InferenceServiceSpec(object):
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
        'canary': 'V1alpha2EndpointSpec',
        'canary_traffic_percent': 'int',
        'default': 'V1alpha2EndpointSpec'
    }

    attribute_map = {
        'canary': 'canary',
        'canary_traffic_percent': 'canaryTrafficPercent',
        'default': 'default'
    }

    def __init__(self, canary=None, canary_traffic_percent=None, default=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha2InferenceServiceSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._canary = None
        self._canary_traffic_percent = None
        self._default = None
        self.discriminator = None

        if canary is not None:
            self.canary = canary
        if canary_traffic_percent is not None:
            self.canary_traffic_percent = canary_traffic_percent
        self.default = default

    @property
    def canary(self):
        """Gets the canary of this V1alpha2InferenceServiceSpec.  # noqa: E501


        :return: The canary of this V1alpha2InferenceServiceSpec.  # noqa: E501
        :rtype: V1alpha2EndpointSpec
        """
        return self._canary

    @canary.setter
    def canary(self, canary):
        """Sets the canary of this V1alpha2InferenceServiceSpec.


        :param canary: The canary of this V1alpha2InferenceServiceSpec.  # noqa: E501
        :type: V1alpha2EndpointSpec
        """

        self._canary = canary

    @property
    def canary_traffic_percent(self):
        """Gets the canary_traffic_percent of this V1alpha2InferenceServiceSpec.  # noqa: E501

        CanaryTrafficPercent defines the percentage of traffic going to canary InferenceService endpoints  # noqa: E501

        :return: The canary_traffic_percent of this V1alpha2InferenceServiceSpec.  # noqa: E501
        :rtype: int
        """
        return self._canary_traffic_percent

    @canary_traffic_percent.setter
    def canary_traffic_percent(self, canary_traffic_percent):
        """Sets the canary_traffic_percent of this V1alpha2InferenceServiceSpec.

        CanaryTrafficPercent defines the percentage of traffic going to canary InferenceService endpoints  # noqa: E501

        :param canary_traffic_percent: The canary_traffic_percent of this V1alpha2InferenceServiceSpec.  # noqa: E501
        :type: int
        """

        self._canary_traffic_percent = canary_traffic_percent

    @property
    def default(self):
        """Gets the default of this V1alpha2InferenceServiceSpec.  # noqa: E501


        :return: The default of this V1alpha2InferenceServiceSpec.  # noqa: E501
        :rtype: V1alpha2EndpointSpec
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this V1alpha2InferenceServiceSpec.


        :param default: The default of this V1alpha2InferenceServiceSpec.  # noqa: E501
        :type: V1alpha2EndpointSpec
        """
        if self.local_vars_configuration.client_side_validation and default is None:  # noqa: E501
            raise ValueError("Invalid value for `default`, must not be `None`")  # noqa: E501

        self._default = default

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
        if not isinstance(other, V1alpha2InferenceServiceSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha2InferenceServiceSpec):
            return True

        return self.to_dict() != other.to_dict()
