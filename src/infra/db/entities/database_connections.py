from sqlalchemy import Column, String, Integer, JSON
from src.infra.db.settings.base import Base

class DatabaseConnection(Base):
    __tablename__ = 'database_connections'

    id = Column(Integer, primary_key=True, autoincrement=True)
    db_type = Column(String(50), nullable=False)  # Ex: 'oracle', 'postgresql', 'mysql'
    host = Column(String(100), nullable=False)    # Endereço do host
    port = Column(Integer, nullable=False)       # Porta do banco de dados
    user = Column(String(50), nullable=False)    # Usuário do banco de dados
    password = Column(String(50), nullable=False) # Senha do banco de dados
    db_name = Column(String(50), nullable=False) # Nome do banco de dados
    extra_config = Column(JSON, nullable=True)   # Configurações extras (ex: tipo de conexão Oracle)

    def __repr__(self):
        return (f'DatabaseConnection [id={self.id}, db_type={self.db_type}, '
                f'host={self.host}, port={self.port}, user={self.user}, '
                f'db_name={self.db_name}, extra_config={self.extra_config}]')