# coding: utf-8
"""
    InductivaWebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from inductiva.client.paths.gcp_instances_group.delete import DeleteInstanceGroup
from inductiva.client.paths.gcp_instances_storage_task_id.delete import DeleteTaskDirectory
from inductiva.client.paths.gcp_instances_group_status.get import GetGroupStatus
from inductiva.client.paths.gcp_instances_group_name.get import GetInstanceGroup
from inductiva.client.paths.gcp_instances_price.get import GetInstancePrice
from inductiva.client.paths.gcp_instances_status.get import GetStatus
from inductiva.client.paths.gcp_instances_storage_size.get import GetStorageSize
from inductiva.client.paths.gcp_instances_groups.get import ListActiveUserInstanceGroups
from inductiva.client.paths.gcp_instances_storage_contents.get import ListStorageContents
from inductiva.client.paths.gcp_instances_group.post import RegisterInstanceGroup
from inductiva.client.paths.gcp_instances_group_elastic.post import StartElasticInstanceGroup
from inductiva.client.paths.gcp_instances_group_start.post import StartInstanceGroup


class InstanceApi(
        DeleteInstanceGroup,
        DeleteTaskDirectory,
        GetGroupStatus,
        GetInstanceGroup,
        GetInstancePrice,
        GetStatus,
        GetStorageSize,
        ListActiveUserInstanceGroups,
        ListStorageContents,
        RegisterInstanceGroup,
        StartElasticInstanceGroup,
        StartInstanceGroup,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
