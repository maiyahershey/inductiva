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


class UserCreate(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "api_key",
            "email",
            "username",
        }

        class properties:
            username = schemas.StrSchema
            email = schemas.StrSchema
            api_key = schemas.StrSchema
            is_active = schemas.BoolSchema
            is_admin = schemas.BoolSchema

            class bucket_name(
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
                ) -> 'bucket_name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )

            is_internal = schemas.BoolSchema
            __annotations__ = {
                "username": username,
                "email": email,
                "api_key": api_key,
                "is_active": is_active,
                "is_admin": is_admin,
                "bucket_name": bucket_name,
                "is_internal": is_internal,
            }

    api_key: MetaOapg.properties.api_key
    email: MetaOapg.properties.email
    username: MetaOapg.properties.username

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["username"]
    ) -> MetaOapg.properties.username:
        ...

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["email"]
    ) -> MetaOapg.properties.email:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["api_key"]
    ) -> MetaOapg.properties.api_key:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["is_active"]
    ) -> MetaOapg.properties.is_active:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["is_admin"]
    ) -> MetaOapg.properties.is_admin:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["bucket_name"]
    ) -> MetaOapg.properties.bucket_name:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["is_internal"]
    ) -> MetaOapg.properties.is_internal:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(
        self,
        name: typing.Union[typing_extensions.Literal["username", "email",
                                                     "api_key", "is_active",
                                                     "is_admin", "bucket_name",
                                                     "is_internal",], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["username"]
    ) -> MetaOapg.properties.username:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: typing_extensions.Literal["email"]
    ) -> MetaOapg.properties.email:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["api_key"]
    ) -> MetaOapg.properties.api_key:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["is_active"]
    ) -> typing.Union[MetaOapg.properties.is_active, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["is_admin"]
    ) -> typing.Union[MetaOapg.properties.is_admin, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["bucket_name"]
    ) -> typing.Union[MetaOapg.properties.bucket_name, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["is_internal"]
    ) -> typing.Union[MetaOapg.properties.is_internal, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[typing_extensions.Literal["username", "email",
                                                     "api_key", "is_active",
                                                     "is_admin", "bucket_name",
                                                     "is_internal",], str]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict,],
        api_key: typing.Union[MetaOapg.properties.api_key, str,],
        email: typing.Union[MetaOapg.properties.email, str,],
        username: typing.Union[MetaOapg.properties.username, str,],
        is_active: typing.Union[MetaOapg.properties.is_active, bool,
                                schemas.Unset] = schemas.unset,
        is_admin: typing.Union[MetaOapg.properties.is_admin, bool,
                               schemas.Unset] = schemas.unset,
        bucket_name: typing.Union[MetaOapg.properties.bucket_name, dict,
                                  frozendict.frozendict, str, date, datetime,
                                  uuid.UUID, int, float, decimal.Decimal, bool,
                                  None, list, tuple, bytes, io.FileIO,
                                  io.BufferedReader,
                                  schemas.Unset] = schemas.unset,
        is_internal: typing.Union[MetaOapg.properties.is_internal, bool,
                                  schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                               frozendict.frozendict, str, date, datetime,
                               uuid.UUID, int, float, decimal.Decimal, None,
                               list, tuple, bytes],
    ) -> 'UserCreate':
        return super().__new__(
            cls,
            *_args,
            api_key=api_key,
            email=email,
            username=username,
            is_active=is_active,
            is_admin=is_admin,
            bucket_name=bucket_name,
            is_internal=is_internal,
            _configuration=_configuration,
            **kwargs,
        )
