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


class InstanceGroup(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "machine_type",
            "spot",
            "name",
            "disk_size_gb",
            "num_instances",
        }

        class properties:
            name = schemas.StrSchema
            machine_type = schemas.StrSchema
            spot = schemas.BoolSchema
            disk_size_gb = schemas.IntSchema
            num_instances = schemas.IntSchema
            zone = schemas.StrSchema

            class resource_pool_id(
                    schemas.UUIDBase,
                    schemas.ComposedSchema,
            ):

                class MetaOapg:
                    format = 'uuid'
                    any_of_0 = schemas.StrSchema
                    any_of_1 = schemas.NoneSchema

                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                        ]

                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date,
                                         datetime, uuid.UUID, int, float,
                                         decimal.Decimal, bool, None, list,
                                         tuple, bytes, io.FileIO,
                                         io.BufferedReader,],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                                           frozendict.frozendict, str, date,
                                           datetime, uuid.UUID, int, float,
                                           decimal.Decimal, None, list, tuple,
                                           bytes],
                ) -> 'resource_pool_id':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            class image_name(
                    schemas.ComposedSchema,):

                class MetaOapg:
                    any_of_0 = schemas.StrSchema
                    any_of_1 = schemas.NoneSchema

                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                        ]

                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date,
                                         datetime, uuid.UUID, int, float,
                                         decimal.Decimal, bool, None, list,
                                         tuple, bytes, io.FileIO,
                                         io.BufferedReader,],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                                           frozendict.frozendict, str, date,
                                           datetime, uuid.UUID, int, float,
                                           decimal.Decimal, None, list, tuple,
                                           bytes],
                ) -> 'image_name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            class label(
                    schemas.ComposedSchema,):

                class MetaOapg:
                    any_of_0 = schemas.StrSchema
                    any_of_1 = schemas.NoneSchema

                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                        ]

                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date,
                                         datetime, uuid.UUID, int, float,
                                         decimal.Decimal, bool, None, list,
                                         tuple, bytes, io.FileIO,
                                         io.BufferedReader,],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                                           frozendict.frozendict, str, date,
                                           datetime, uuid.UUID, int, float,
                                           decimal.Decimal, None, list, tuple,
                                           bytes],
                ) -> 'label':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            __annotations__ = {
                "name": name,
                "machine_type": machine_type,
                "spot": spot,
                "disk_size_gb": disk_size_gb,
                "num_instances": num_instances,
                "zone": zone,
                "resource_pool_id": resource_pool_id,
                "image_name": image_name,
                "label": label,
            }

    machine_type: MetaOapg.properties.machine_type
    spot: MetaOapg.properties.spot
    name: MetaOapg.properties.name
    disk_size_gb: MetaOapg.properties.disk_size_gb
    num_instances: MetaOapg.properties.num_instances

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["machine_type"]
    ) -> MetaOapg.properties.machine_type:
        ...

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["spot"]
    ) -> MetaOapg.properties.spot:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["disk_size_gb"]
    ) -> MetaOapg.properties.disk_size_gb:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["num_instances"]
    ) -> MetaOapg.properties.num_instances:
        ...

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["zone"]
    ) -> MetaOapg.properties.zone:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["resource_pool_id"]
    ) -> MetaOapg.properties.resource_pool_id:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["image_name"]
    ) -> MetaOapg.properties.image_name:
        ...

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["label"]
    ) -> MetaOapg.properties.label:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[typing_extensions.Literal["name", "machine_type",
                                                     "spot", "disk_size_gb",
                                                     "num_instances", "zone",
                                                     "resource_pool_id",
                                                     "image_name", "label",],
                           str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
            self, name: typing_extensions.Literal["name"]
    ) -> MetaOapg.properties.name:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["machine_type"]
    ) -> MetaOapg.properties.machine_type:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: typing_extensions.Literal["spot"]
    ) -> MetaOapg.properties.spot:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["disk_size_gb"]
    ) -> MetaOapg.properties.disk_size_gb:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["num_instances"]
    ) -> MetaOapg.properties.num_instances:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["zone"]
    ) -> typing.Union[MetaOapg.properties.zone, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["resource_pool_id"]
    ) -> typing.Union[MetaOapg.properties.resource_pool_id, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["image_name"]
    ) -> typing.Union[MetaOapg.properties.image_name, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["label"]
    ) -> typing.Union[MetaOapg.properties.label, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[typing_extensions.Literal["name", "machine_type",
                                                     "spot", "disk_size_gb",
                                                     "num_instances", "zone",
                                                     "resource_pool_id",
                                                     "image_name", "label",],
                           str]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict,],
        machine_type: typing.Union[MetaOapg.properties.machine_type, str,],
        spot: typing.Union[MetaOapg.properties.spot, bool,],
        name: typing.Union[MetaOapg.properties.name, str,],
        disk_size_gb: typing.Union[MetaOapg.properties.disk_size_gb,
                                   decimal.Decimal, int,],
        num_instances: typing.Union[MetaOapg.properties.num_instances,
                                    decimal.Decimal, int,],
        zone: typing.Union[MetaOapg.properties.zone, str,
                           schemas.Unset] = schemas.unset,
        resource_pool_id: typing.Union[MetaOapg.properties.resource_pool_id,
                                       dict, frozendict.frozendict, str, date,
                                       datetime, uuid.UUID, int, float,
                                       decimal.Decimal, bool, None, list, tuple,
                                       bytes, io.FileIO, io.BufferedReader,
                                       schemas.Unset] = schemas.unset,
        image_name: typing.Union[MetaOapg.properties.image_name, dict,
                                 frozendict.frozendict, str, date, datetime,
                                 uuid.UUID, int, float, decimal.Decimal, bool,
                                 None, list, tuple, bytes, io.FileIO,
                                 io.BufferedReader,
                                 schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, dict,
                            frozendict.frozendict, str, date, datetime,
                            uuid.UUID, int, float, decimal.Decimal, bool, None,
                            list, tuple, bytes, io.FileIO, io.BufferedReader,
                            schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                               frozendict.frozendict, str, date, datetime,
                               uuid.UUID, int, float, decimal.Decimal, None,
                               list, tuple, bytes],
    ) -> 'InstanceGroup':
        return super().__new__(
            cls,
            *_args,
            machine_type=machine_type,
            spot=spot,
            name=name,
            disk_size_gb=disk_size_gb,
            num_instances=num_instances,
            zone=zone,
            resource_pool_id=resource_pool_id,
            image_name=image_name,
            label=label,
            _configuration=_configuration,
            **kwargs,
        )
