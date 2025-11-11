from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship


class Order(SQLModel, table=True):
    id: int = Field(primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    placed_at: datetime = Field(nullable=False)
    status: str = Field(nullable=False, default="pending")

    customer: "Customer" = Relationship(back_populates="orders")
    line_items: list["LineItem"] = Relationship(back_populates="order")

    def __init__(self, **data):
        super().__init__(**data)
        self.placed_at = datetime.now(timezone.utc)
        self.status = "pending"
