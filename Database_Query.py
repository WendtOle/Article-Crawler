from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

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

Session = sessionmaker(bind=engine)
session = Session()

allArticles = session.query(Articles).all()

print(len(allArticles))