from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Float, Integer


type_mapping = {
    str: String,
    float: Float,
    int: Integer
    # add your type here
}


class BaseMeta(DeclarativeMeta):
    def __init__(cls, classname, bases, dict_):
        # add your changes/additions to classes before it go to SQLAlchemy parser
        # you can make this way multiple table generations from one class, if needed and etc
        cls.__tablename__ = cls.__name__.lower() + "s" if not cls.__name__.endswith(
            'y') else cls.__name__.lower()[:-1] + "ies"
        DeclarativeMeta.__init__(cls, classname, bases, dict_)


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
        return Column(column_name, type_mapping[_ann_type])
    else:
        # if we have a class in globals
        if _ann_type.__name__ in globals():
            return relationship(_ann_type.__name__, order_by=f"{_ann_type.__name__}.id", uselist=False)


class BaseMetaDefaultPrimary(BaseMeta):
    """second meta class child of previous custom - to separate features:
         BaseMeta - only add auto generation for table names
         BaseMetaDefaultPrimary - set 'id' field as primary, and translate class annotations to SQLAlchemy Column
    """
    def __init__(cls, classname, bases, dict_):
        if '__annotations__' in cls.__dict__:
            cls.__annotations__['id'] = str
            for annotation in cls.__annotations__:
                setattr(cls, annotation, get_type(BaseMetaDefaultPrimary, annotation,
                                                  cls.__annotations__[annotation]))
                if annotation == 'id':
                    cls.__dict__[annotation].primary_key = True
        BaseMeta.__init__(cls, classname, bases, dict_)


Model = declarative_base(metaclass=BaseMetaDefaultPrimary)
