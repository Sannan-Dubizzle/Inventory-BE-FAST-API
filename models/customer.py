from sqlmodel import Field, SQLModel, Relationship


class Customer(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    address: str = Field(nullable=False)

    orders: list["Order"] = Relationship(back_populates="customer")