from datetime import datetime
from sqlalchemy import MetaData, String, TIMESTAMP, ForeignKey, Table, Column, Integer, JSON


metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON)
)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email"),
    Column("user_name"),
    Column("password", String, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow()),
    Column("role_id", Integer, ForeignKey("roles.id")),
)

