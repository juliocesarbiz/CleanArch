# pylint: disable=no-member
# pylint: disable=wildcard-import
from pathlib import Path
import os
import importlib

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Caminho absoluto para o diretório atual do script (env.py)
current_dir = Path(__file__).resolve().parent

# Caminho absoluto para o diretório entities
entities_dir = current_dir.parent.parent / "cleanarch" / "src" / "infra" / "db" / "entities"

# Verifica se o diretório existe
if not entities_dir.exists():
    raise FileNotFoundError(f"O diretório {entities_dir} não foi encontrado.")

# Importa dinamicamente todos os módulos no diretório entities
for module in entities_dir.glob("*.py"):
    if module.name == "__init__.py":
        continue
    module_name = module.stem  # Remove a extensão .py
    importlib.import_module(f"src.infra.db.entities.{module_name}")

# Importa o pacote que contém todas as entidades
#from src.infra.db.entities.user_group import UserGroup  
#from src.infra.db.entities.users import Users


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# No topo do env.py
from src.infra.db.settings.base import Base  # ajuste o caminho conforme sua estrutura
target_metadata = Base.metadata



# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
