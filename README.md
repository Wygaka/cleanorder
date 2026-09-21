<div align="center">

# CleanOrder

### Python / Clean Architecture / Order Use Case

<p>
  <img src="https://img.shields.io/badge/Python-161b22?style=for-the-badge&logo=python&logoColor=3776AB" alt="Python" />
  <img src="https://img.shields.io/badge/Clean_Architecture-161b22?style=for-the-badge&logo=python&logoColor=39d353" alt="Clean Architecture" />
  <img src="https://img.shields.io/badge/Windows-161b22?style=for-the-badge&logo=windows&logoColor=0078D4" alt="Windows" />
</p>

</div>

---

## 📌 About

**CleanOrder** is a small Python project that demonstrates a clean separation between domain logic, use cases and infrastructure.

The application creates an order from cart items, calculates the subtotal, applies a discount when the order amount is high enough and saves the order in an in-memory repository.

## 📁 Project structure

```txt
cleanorder/
├── main.py
└── src/
    ├── domain/
    │   └── models.py
    ├── infrastructure/
    │   └── memory_repo.py
    └── use_cases/
        ├── create_order.py
        └── interfaces.py
```

## ⚙️ Features

- create an order from raw cart data
- calculate subtotal by item price and quantity
- apply a 10% discount for orders from 5000 rubles
- save orders through a repository interface
- keep business logic separated from infrastructure

## 🚀 Run

Make sure Python is installed, then run:

```bash
python main.py
```

Example output:

```txt
=== Результат выполнения Use Case ===
ID заказа: ORD-FRIEND-001
Количество позиций: 2
Сумма без скидки: 9100.0 руб.
Итого к оплате: 8190.0 руб.
Статус: CREATED
```

## 🧠 How it works

The main flow is simple:

```txt
cart data
  ↓
CreateOrderUseCase
  ↓
Order / OrderItem
  ↓
InMemoryOrderRepository
```

## 🛠 Tech stack

- Python
- Dataclasses
- Clean Architecture basics
- In-memory repository

---

<div align="center">

Made by **Wygaka**

</div>
