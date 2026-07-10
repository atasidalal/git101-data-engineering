def is_valid_order_status(status: str) -> bool:
    return status in {"PLACED", "SHIPPED", "DELIVERED", "CANCELLED", "RETURNED"}
