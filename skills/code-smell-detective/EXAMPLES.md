# EXAMPLES.md — Code Smell Detective

## Purpose

This document provides examples for the Code Smell Detective skill.

---

## Example 1: Long Method

### Input

```python
def process_order(order):
    if not order.items:
        raise ValueError("empty order")
    total = 0
    for item in order.items:
        total += item.price * item.quantity
    if order.customer.is_vip:
        total = total * 0.9
    print("saving order")
    database.save(order)
    email.send(order.customer.email, "Order confirmed")
    return {"status": "ok", "total": total}
```

### Detective Finding

The method shows signs of a Long Method and mixed responsibilities.

### Evidence

- Validation is handled inline.
- Pricing calculation is handled inline.
- Persistence is handled inline.
- Notification is handled inline.
- Response formatting is handled inline.

### Impact

The method has several reasons to change: pricing rules, validation rules, persistence behavior, notification behavior, and response format.

### Refactoring Plan

1. Add tests for current behavior.
2. Extract `validate_order(order)`.
3. Extract `calculate_total(order)`.
4. Extract `save_order(order)`.
5. Extract `send_confirmation(order)`.
6. Keep `process_order` as orchestration only.

---

## Example 2: Feature Envy

### Input

```python
def customer_discount(order):
    if order.customer.loyalty_points > 1000 and order.customer.years_active > 3:
        return 0.15
    return 0.0
```

### Detective Finding

This function may show Feature Envy because it uses `customer` data to make a customer-specific decision.

### Refactoring Option

Move the decision closer to the customer:

```python
class Customer:
    def discount_rate(self):
        if self.loyalty_points > 1000 and self.years_active > 3:
            return 0.15
        return 0.0
```

---

## Example 3: God Object

### Symptoms

A class called `ApplicationManager`:

- Reads configuration
- Validates users
- Calculates invoices
- Sends email
- Writes audit logs
- Calls payment providers
- Generates reports

### Detective Finding

This is likely a God Object because one class owns many unrelated responsibilities.

### First Safe Step

Group methods by responsibility and extract the least risky cohesive service first, such as `AuditLogger` or `EmailNotifier`.
