from src.infrastructure.memory_repo import InMemoryOrderRepository
from src.use_cases.create_order import CreateOrderUseCase


def main():
    repository = InMemoryOrderRepository()
    use_case = CreateOrderUseCase(order_repo=repository)

    cart = [
        {"id": "B201", "title": "Монитор 24 дюйма", "price": 7800.0, "quantity": 1},
        {"id": "B202", "title": "USB-C кабель", "price": 650.0, "quantity": 2},
    ]

    result = use_case.execute(order_id="ORD-FRIEND-001", raw_items=cart)
    print("=== Результат выполнения Use Case ===")
    print(f"ID заказа: {result['order_id']}")
    print(f"Количество позиций: {result['items_count']}")
    print(f"Сумма без скидки: {result['subtotal']} руб.")
    print(f"Итого к оплате: {result['final_amount']} руб.")
    print(f"Статус: {result['status']}")


if __name__ == "__main__":
    main()
