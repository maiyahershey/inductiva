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


class NewUser(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Dataclass that represents the input to create a new user.

Attributes:
    username: Unique username to identify the user.
    api_key: Token to authenticate the user.
    is_admin: Does the user have admin rights?
    """

    class MetaOapg:
        required = {
            "api_key",
            "username",
        }

        class properties:
            username = schemas.StrSchema
            api_key = schemas.StrSchema
            is_admin = schemas.BoolSchema
            __annotations__ = {
                "username": username,
                "api_key": api_key,
                "is_admin": is_admin,
            }

    api_key: MetaOapg.properties.api_key
    username: MetaOapg.properties.username

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["username"]
    ) -> MetaOapg.properties.username:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["api_key"]
    ) -> MetaOapg.properties.api_key:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["is_admin"]
    ) -> MetaOapg.properties.is_admin:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(self,
                    name: typing.Union[typing_extensions.Literal["username",
                                                                 "api_key",
                                                                 "is_admin",],
                                       str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["username"]
    ) -> MetaOapg.properties.username:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["api_key"]
    ) -> MetaOapg.properties.api_key:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["is_admin"]
    ) -> typing.Union[MetaOapg.properties.is_admin, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(self,
                      name: typing.Union[typing_extensions.Literal["username",
                                                                   "api_key",
                                                                   "is_admin",],
                                         str]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict,],
        api_key: typing.Union[MetaOapg.properties.api_key, str,],
        username: typing.Union[MetaOapg.properties.username, str,],
        is_admin: typing.Union[MetaOapg.properties.is_admin, bool,
                               schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                               frozendict.frozendict, str, date, datetime,
                               uuid.UUID, int, float, decimal.Decimal, None,
                               list, tuple, bytes],
    ) -> 'NewUser':
        return super().__new__(
            cls,
            *_args,
            api_key=api_key,
            username=username,
            is_admin=is_admin,
            _configuration=_configuration,
            **kwargs,
        )
