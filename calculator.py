def calculate_tip(bill: float, tip_percent: float, people: int = 1) -> dict:
    if bill < 0 or tip_percent < 0:
        raise ValueError("Bill and tip percent must be positive")
    if people < 1:
        raise ValueError("At least one person required")

    tip_total = round(bill * (tip_percent / 100), 2)
    total = round(bill + tip_total, 2)
    per_person = round(total / people, 2)

    return {"tip": tip_total, "total": total, "per_person": per_person}