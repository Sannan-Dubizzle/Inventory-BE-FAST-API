from sqlmodel import Field, SQLModel, Relationship

class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    price: float = Field(nullable=False, default=0.0)
    available_quantity: int = Field(default=0)
    line_items: list["LineItem"] = Relationship(back_populates="product")