# coding: utf-8

"""
kag

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

The version of the OpenAPI document: 1.0.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kag.common.rest.configuration import Configuration


class VertexRecordInstance(object):
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
        "type": "str",
        "id": "str",
        "properties": "object",
        "vectors": "object",
    }

    attribute_map = {
        "type": "type",
        "id": "id",
        "properties": "properties",
        "vectors": "vectors",
    }

    def __init__(
        self,
        type=None,
        id=None,
        properties=None,
        vectors=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """VertexRecordInstance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._id = None
        self._properties = None
        self._vectors = None
        self.discriminator = None

        self.type = type
        self.id = id
        self.properties = properties
        self.vectors = vectors

    @property
    def type(self):
        """Gets the type of this VertexRecordInstance.  # noqa: E501


        :return: The type of this VertexRecordInstance.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VertexRecordInstance.


        :param type: The type of this VertexRecordInstance.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type`, must not be `None`"
            )  # noqa: E501

        self._type = type

    @property
    def id(self):
        """Gets the id of this VertexRecordInstance.  # noqa: E501


        :return: The id of this VertexRecordInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VertexRecordInstance.


        :param id: The id of this VertexRecordInstance.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and id is None
        ):  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def properties(self):
        """Gets the properties of this VertexRecordInstance.  # noqa: E501


        :return: The properties of this VertexRecordInstance.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this VertexRecordInstance.


        :param properties: The properties of this VertexRecordInstance.  # noqa: E501
        :type: object
        """
        if (
            self.local_vars_configuration.client_side_validation and properties is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `properties`, must not be `None`"
            )  # noqa: E501

        self._properties = properties

    @property
    def vectors(self):
        """Gets the vectors of this VertexRecordInstance.  # noqa: E501


        :return: The vectors of this VertexRecordInstance.  # noqa: E501
        :rtype: object
        """
        return self._vectors

    @vectors.setter
    def vectors(self, vectors):
        """Sets the vectors of this VertexRecordInstance.


        :param vectors: The vectors of this VertexRecordInstance.  # noqa: E501
        :type: object
        """
        if (
            self.local_vars_configuration.client_side_validation and vectors is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `vectors`, must not be `None`"
            )  # noqa: E501

        self._vectors = vectors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (
                            (item[0], item[1].to_dict())
                            if hasattr(item[1], "to_dict")
                            else item
                        ),
                        value.items(),
                    )
                )
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
        if not isinstance(other, VertexRecordInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VertexRecordInstance):
            return True

        return self.to_dict() != other.to_dict()
