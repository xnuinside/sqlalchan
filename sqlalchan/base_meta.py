from types import LambdaType

from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, String, Float, Integer
from uuid import uuid4
from sqlalchan.example.set_of_types import bigint

type_mapping = {
    str: String,
    float: Float,
    int: Integer,
    bigint: BigInteger,
    # add your type here
}


def get_type(meta, column_name, _ann_type):
    """
        convert Class annotation to SQLAlchemy Column object
    :param meta:
    :param column_name:
    :param _ann_type:
    :return:
    """
    if '__origin__' in _ann_type.__dict__ and _ann_type.__origin__ is list:
        if _ann_type.__args__[0].__name__ in globals():
            return relationship(_ann_type.__args__[0].__name__,
                                order_by=f"{_ann_type.__args__[0].__name__}.id")
    elif not isinstance(_ann_type, meta):
        # check do we have already pre-create type or just class annotation
        if isinstance(_ann_type, Column) or isinstance(_ann_type, LambdaType):
            return _ann_type(column_name)

        if column_name == 'id':
            return Column(column_name, type_mapping[_ann_type],
                          default=uuid4(), primary_key=True)
        else:
            return Column(column_name, type_mapping[_ann_type])

    else:
        # if we have a class in globals
        if _ann_type.__name__ in globals():
            return relationship(_ann_type.__name__, order_by=f"{_ann_type.__name__}.id", uselist=False)


class BaseMeta(DeclarativeMeta):
    def __init__(cls, classname, bases, dict_):
        # add your changes/additions to classes before it go to SQLAlchemy parser
        # you can make this way multiple table generations from one class, if needed and etc
        special = {'y': "ies", 's': 'es'}
        cls.__tablename__ = f'{cls.__name__.lower()}{special.get(cls.__name__[-1], "s")}'
        DeclarativeMeta.__init__(cls, classname, bases, dict_)


class BaseMetaDefaultPrimary(BaseMeta):
    """second meta class child of previous custom - to separate features:
         BaseMeta - only add auto generation for table names
         BaseMetaDefaultPrimary - set 'id' field as primary, and translate class annotations to SQLAlchemy Column
    """
    def __init__(cls, classname, bases, dict_):
        if '__annotations__' in cls.__dict__:
            cls.__annotations__['id'] = str
            for annotation in cls.__annotations__:
                setattr(cls, annotation, get_type(
                    BaseMetaDefaultPrimary, annotation, cls.__annotations__[annotation]))
        BaseMeta.__init__(cls, classname, bases, dict_)


Model = declarative_base(metaclass=BaseMetaDefaultPrimary)
