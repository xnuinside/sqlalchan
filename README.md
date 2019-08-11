Toy-example how possible to customize SQLAlchemy Class definition and mapping your custom metaclass that inherit from SQLAlchemy DeclarativeMeta Class. 

In example, we use simple class annotations to define tables, instead of huge

    from sqlalchemy import Column, Integer, String

    class User(Base):
         __tablename__ = 'users'
    
         id = Column(Integer, primary_key=True)
         name = Column(String)
         fullname = Column(String)
         nickname = Column(String)


Examples in 'examples' dir.
Main code in 'converter.py'

To check example: 

1. define your DB in example/db.py 
2. add sqlalchan in your PYTHONPATH
3. run python example/db.py
