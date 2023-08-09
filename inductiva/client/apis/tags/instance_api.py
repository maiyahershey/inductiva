# coding: utf-8
"""
    InductivaWebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from inductiva.client.paths.gcp_instances_group.post import CreateInstanceGroup
from inductiva.client.paths.gcp_instances.delete import DeleteInstance
from inductiva.client.paths.gcp_instances_group.delete import DeleteInstanceGroup
from inductiva.client.paths.gcp_instances_price.get import GetInstancePrice


class InstanceApi(
        CreateInstanceGroup,
        DeleteInstance,
        DeleteInstanceGroup,
        GetInstancePrice,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
