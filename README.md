Toy-example how possible to customize SQLAlchemy Class definition and mapping your custom metaclass that inherit from SQLAlchemy DeclarativeMeta Class. 

In example, we use simple class annotations to define tables, instead of huge classical SQLAlchemy classes. 

This: 
    from sqlalchemy import Column, Integer, String

    class User(Base):
         __tablename__ = 'users'
    
         id = Column(Integer, primary_key=True)
         name = Column(String)
         fullname = Column(String)
         nickname = Column(String)



Became this: 

    class User(Base):

        id: int
        name: str
        fullname: str
        nickname: str

Examples in 'examples' dir.
Main code in 'converter.py'

To run example: 

1. git clone this repo to your local machine
2. go to sources 
3. run:
    
    docker-compose -f test_docker_compose.yml up postgres_test
    
4. wait until DB will success created
    
5. In new terminal window run: 
    
    docker-compose -f test_docker_compose.yml up main

6. If you want to test insert - uncomment lines in 'db.py'
