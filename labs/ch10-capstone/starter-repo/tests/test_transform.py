import pandas as pd
from labs.ch10_capstone.starter_repo.src.customer_orders_etl.transform import clean_orders

def test_clean_orders_removes_invalid_quantity_and_status():
    df = pd.DataFrame({
        "order_id": ["O1", "O2", "O3"],
        "quantity": [2, -1, 1],
        "unit_price": [100, 100, 100],
        "discount_pct": [0, 0, 0],
        "order_status": ["DELIVERED", "DELIVERED", "UNKNOWN"]
    })
    cleaned = clean_orders(df)
    assert len(cleaned) == 1
    assert cleaned.iloc[0]["order_id"] == "O1"
    assert cleaned.iloc[0]["net_amount"] == 200
