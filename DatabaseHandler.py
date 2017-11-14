from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Articles(Base):
    __tablename__ = "spiegelArticles"

    Id = Column(Integer, primary_key=True)
    Title = Column(String)
    Date = Column(String)
    Authors = Column(String)
    Content = Column(String)

class DatabaseHandler:
    def __init__(self,databaseURL):
        self.url = databaseURL
        self.setSession()

    def setSession(self):
        engine = create_engine(self.url)
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def addArticle(self,article):
        self.session.add(Articles(Title=article['title'], Date=article['date'],Authors=article['authors'],Content=article['content']))
        self.session.commit()
