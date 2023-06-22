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


class GCloudHostInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Info about Google Cloud machine hosting the executer.
    """


    class MetaOapg:
        required = {
            "vm_id",
            "vm_type",
            "preemptible",
            "vm_metadata",
            "host_type",
            "vm_name",
        }
        
        class properties:
            
            
            class host_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def GCLOUD(cls):
                    return cls("gcloud")
            vm_type = schemas.StrSchema
            vm_name = schemas.StrSchema
            vm_id = schemas.StrSchema
            preemptible = schemas.BoolSchema
            vm_metadata = schemas.DictSchema
            __annotations__ = {
                "host_type": host_type,
                "vm_type": vm_type,
                "vm_name": vm_name,
                "vm_id": vm_id,
                "preemptible": preemptible,
                "vm_metadata": vm_metadata,
            }
    
    vm_id: MetaOapg.properties.vm_id
    vm_type: MetaOapg.properties.vm_type
    preemptible: MetaOapg.properties.preemptible
    vm_metadata: MetaOapg.properties.vm_metadata
    host_type: MetaOapg.properties.host_type
    vm_name: MetaOapg.properties.vm_name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["host_type"]) -> MetaOapg.properties.host_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vm_type"]) -> MetaOapg.properties.vm_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vm_name"]) -> MetaOapg.properties.vm_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vm_id"]) -> MetaOapg.properties.vm_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preemptible"]) -> MetaOapg.properties.preemptible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vm_metadata"]) -> MetaOapg.properties.vm_metadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["host_type", "vm_type", "vm_name", "vm_id", "preemptible", "vm_metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["host_type"]) -> MetaOapg.properties.host_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vm_type"]) -> MetaOapg.properties.vm_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vm_name"]) -> MetaOapg.properties.vm_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vm_id"]) -> MetaOapg.properties.vm_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preemptible"]) -> MetaOapg.properties.preemptible: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vm_metadata"]) -> MetaOapg.properties.vm_metadata: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["host_type", "vm_type", "vm_name", "vm_id", "preemptible", "vm_metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        vm_id: typing.Union[MetaOapg.properties.vm_id, str, ],
        vm_type: typing.Union[MetaOapg.properties.vm_type, str, ],
        preemptible: typing.Union[MetaOapg.properties.preemptible, bool, ],
        vm_metadata: typing.Union[MetaOapg.properties.vm_metadata, dict, frozendict.frozendict, ],
        host_type: typing.Union[MetaOapg.properties.host_type, str, ],
        vm_name: typing.Union[MetaOapg.properties.vm_name, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GCloudHostInfo':
        return super().__new__(
            cls,
            *_args,
            vm_id=vm_id,
            vm_type=vm_type,
            preemptible=preemptible,
            vm_metadata=vm_metadata,
            host_type=host_type,
            vm_name=vm_name,
            _configuration=_configuration,
            **kwargs,
        )
