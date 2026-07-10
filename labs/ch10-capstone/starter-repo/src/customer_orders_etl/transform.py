VALID_STATUSES = {"PLACED", "SHIPPED", "DELIVERED", "CANCELLED", "RETURNED"}

def clean_orders(df):
    df = df.copy()
    df = df[df["quantity"] > 0]
    df = df[df["order_status"].isin(VALID_STATUSES)]
    df["net_amount"] = df["quantity"] * df["unit_price"] * (1 - df["discount_pct"] / 100)
    return df
