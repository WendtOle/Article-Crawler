from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///spiegelArticles.db')

Base = declarative_base()
Base.metadata.bind = engine


class Articles(Base):
    __tablename__ = "spiegelArticles"

    Id = Column(Integer, primary_key=True)
    Title = Column(String)
    Date = Column(String)
    Authors = Column(String)
    Content = Column(String)

Base.metadata.create_all()
print('Database was setup')