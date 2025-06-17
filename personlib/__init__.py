from .person import Person

# default database dir — can be changed by user after import
DB_DIR: str = "db"
JSON_INDENT: int = 4

__all__ = ["Person", "DB_DIR", "JSON_INDENT"]

