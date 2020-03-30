from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String


class MockType:
    pass


# not just mock for type map
bigint = MockType()

# not customizable already column
c_int = lambda column_name: Column(column_name, Integer)

# customizable
c_str = lambda _len = 32, **kwargs: lambda column_name: Column(
    column_name, String(_len), **kwargs)
