# Technical Challenge – Python Junior Backend Developer

Thank you for your interest!

This technical test is designed to evaluate your backend development skills with Python. You'll be asked to build a REST API to manage user subscriptions, with basic CRUD functionality and some optional enhancements.

⏱ **Recommended time: up to 2 hours**

---

## 🚩 Objective

Implement these two operations:
- Create a subscription (POST).
- List all subscriptions (GET).

Everything else is **optional** and considered extra. Prioritize having these two endpoints working correctly.

---

## 📋 Basic Model

| Field   | Type    | Description                   |
|---------|---------|-------------------------------|
| id      | Integer | Auto-incrementing ID          |
| email   | String  | Required, basic format check  |
| name    | String  | Required                      |
| plan    | String  | Required                      |

- You can use any structure or in-memory storage (list or dictionary in Python).

---

## 📡 Required Endpoints

| Method | Route          | Description                  |
|--------|----------------|------------------------------|
| GET    | /subscriptions | List all subscriptions       |
| POST   | /subscriptions | Create a new subscription    |

---

## ✅ Minimal Validations

- `email` must contain an "@" (no need for advanced validation or uniqueness).
- `name` must not be empty.
- `plan` must exist (no restriction on valid values).

---

## 🧩 Optional Extras (if time permits)

- Validate email uniqueness.
- Restrict the allowed values of `plan`.
- Add endpoint to get subscription details by ID (GET /subscriptions/{id}).
- Support update and delete operations (PUT/DELETE).
- Add endpoint to toggle active status (PATCH).
- Split code into multiple files.
- Use a database, ORM, Pydantic for validations.
- Add detailed error handling.
- Include tests, Docker, logging, Makefile, pagination.

---

## 🏁 Running the Project

Brief example of installation and running your project:

```
cd subscription_api
pip install -r requirements.txt
uvicorn src.main:app --reload # For FastAPI

or flask run # For Flask
```

Good luck! We want to see how you approach a simple REST API and how you organize 
