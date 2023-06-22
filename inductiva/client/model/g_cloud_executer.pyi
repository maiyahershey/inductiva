# coding: utf-8

"""
    InductivaWebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from inductiva.client import schemas  # noqa: F401


class GCloudExecuter(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Google Cloud executer.
    """


    class MetaOapg:
        required = {
            "vm_type",
            "memory",
            "cpu_count_logical",
            "cpu_count_physical",
            "uuid",
            "host_type",
            "vm_name",
        }
        
        class properties:
            uuid = schemas.StrSchema
            cpu_count_logical = schemas.IntSchema
            cpu_count_physical = schemas.IntSchema
            memory = schemas.IntSchema
            
            
            class host_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def GCLOUD(cls):
                    return cls("gcloud")
            vm_type = schemas.StrSchema
            vm_name = schemas.StrSchema
            __annotations__ = {
                "uuid": uuid,
                "cpu_count_logical": cpu_count_logical,
                "cpu_count_physical": cpu_count_physical,
                "memory": memory,
                "host_type": host_type,
                "vm_type": vm_type,
                "vm_name": vm_name,
            }
    
    vm_type: MetaOapg.properties.vm_type
    memory: MetaOapg.properties.memory
    cpu_count_logical: MetaOapg.properties.cpu_count_logical
    cpu_count_physical: MetaOapg.properties.cpu_count_physical
    uuid: MetaOapg.properties.uuid
    host_type: MetaOapg.properties.host_type
    vm_name: MetaOapg.properties.vm_name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpu_count_logical"]) -> MetaOapg.properties.cpu_count_logical: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cpu_count_physical"]) -> MetaOapg.properties.cpu_count_physical: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["memory"]) -> MetaOapg.properties.memory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["host_type"]) -> MetaOapg.properties.host_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vm_type"]) -> MetaOapg.properties.vm_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vm_name"]) -> MetaOapg.properties.vm_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uuid", "cpu_count_logical", "cpu_count_physical", "memory", "host_type", "vm_type", "vm_name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpu_count_logical"]) -> MetaOapg.properties.cpu_count_logical: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cpu_count_physical"]) -> MetaOapg.properties.cpu_count_physical: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["memory"]) -> MetaOapg.properties.memory: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["host_type"]) -> MetaOapg.properties.host_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vm_type"]) -> MetaOapg.properties.vm_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vm_name"]) -> MetaOapg.properties.vm_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uuid", "cpu_count_logical", "cpu_count_physical", "memory", "host_type", "vm_type", "vm_name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        vm_type: typing.Union[MetaOapg.properties.vm_type, str, ],
        memory: typing.Union[MetaOapg.properties.memory, decimal.Decimal, int, ],
        cpu_count_logical: typing.Union[MetaOapg.properties.cpu_count_logical, decimal.Decimal, int, ],
        cpu_count_physical: typing.Union[MetaOapg.properties.cpu_count_physical, decimal.Decimal, int, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, ],
        host_type: typing.Union[MetaOapg.properties.host_type, str, ],
        vm_name: typing.Union[MetaOapg.properties.vm_name, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GCloudExecuter':
        return super().__new__(
            cls,
            *_args,
            vm_type=vm_type,
            memory=memory,
            cpu_count_logical=cpu_count_logical,
            cpu_count_physical=cpu_count_physical,
            uuid=uuid,
            host_type=host_type,
            vm_name=vm_name,
            _configuration=_configuration,
            **kwargs,
        )
