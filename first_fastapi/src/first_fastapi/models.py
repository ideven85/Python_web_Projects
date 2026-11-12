from typing import Optional
from datetime import datetime
from sqlalchemy import DateTime, func, Sequence
from sqlmodel import SQLModel, Field

# 1. Attach Sequence to SQLModel.metadata so create_all() builds it automatically
item_id_sequence = Sequence("item_id_sequence", metadata=SQLModel.metadata)


class Base(SQLModel):
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        sa_column_kwargs={"server_default": item_id_sequence.next_value()},
    )
    # 2. Fixed type hint from Optional[int] -> Optional[datetime]
    created_at: Optional[datetime] = Field(
        default=None,
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={"server_default": func.now(), "nullable": False},
    )
    # 3. Fixed type hint to Optional[datetime] and added onupdate
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={
            "server_default": func.now(),
            "onupdate": func.now(),
            "nullable": False,
        },
    )


class ItemBase(SQLModel):
    name: str = Field(index=True, unique=True, max_length=255)
    description: Optional[str] = None
    price: int
    on_offer: bool = Field(default=False)


class Item(Base, ItemBase, table=True):
    __tablename__ = "items"


class ItemCreate(ItemBase):
    pass


class ItemResponse(Base, ItemBase):
    id: int
