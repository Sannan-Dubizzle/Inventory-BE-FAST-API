from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import event

class LineItem(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="order.id")
    quantity: int = Field(default=0)
    product_id: int = Field(foreign_key="product.id")

    product: "Product" = Relationship(back_populates="line_items")
    order: "Order" = Relationship(back_populates="line_items")

    def __init__(self, **data):
        super().__init__(**data)
        if "quantity" not in data:
            self.quantity = 0
        self.product.available_quantity -= self.quantity

@event.listens_for(LineItem, "before_insert")
def validate_quantity(mapper, connection, target):
    print(target.quantity)
    print(target.product.available_quantity)
    if target.product.available_quantity < 0:
        raise ValueError("Insufficient product quantity available.")