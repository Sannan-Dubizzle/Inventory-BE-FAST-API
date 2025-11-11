from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..db import SessionDep
from ..models import LineItem, Order, Product, Customer

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)


class CreateOrderRequest(BaseModel):
    customer_id: int
    items: list[dict[str, Any]]


@router.get("/")
def get_oroders(session: SessionDep):
    return {
        "orders": session.get_all(Order)
    }


@router.get("/{order_id}")
def get_order(order_id: int, session: SessionDep):
    return {"order": session.get(Order, order_id)}


@router.post("/")
def create_order(request: CreateOrderRequest, session: SessionDep):
    try:
        line_items = [LineItem(product=session.get(Product, item['product_id']), quantity=item['quantity']) for item in
                      request.items]
        customer = session.get(Customer, request.customer_id)
        order = Order(line_items=line_items, customer=customer)
        session.add(order)
        session.commit()
        session.refresh(order)
        return {"order": order}
    except ValueError as e:
        session.rollback()  # important to rollback after the exception
        raise HTTPException(status_code=422, detail=str(e))
