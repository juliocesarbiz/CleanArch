from sqlalchemy import Column, String, Integer
from src.infra.db.settings.base import Base

class Groups(Base):
    __tablename__ = 'groups'

    id_group = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    active_user = Column(String, nullable=False)
    user_comments = Column(String, nullable=True)
    
    def __repr__(self):
        return ('Groups [id_group={}, description={}, active_user={}, user_comments={}]'
            .format(self.id_group, self.description, self.active_user, self.user_comments))
