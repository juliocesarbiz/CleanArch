from sqlalchemy import Column, String, Integer
from src.infra.db.settings.base import Base

class Groups(Base):
    __tablename__ = 'groups'

    id_group = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    active_user = Column(String, nullable=False)
    user_comments = Column(String, nullable=True)

    def __repr__(self):
        return f'Groups [
        id_group={self.id_group}, 
        description={self.description}, 
        active_user={self.active_user},
        user_comments={self.user_comments}
        ]'