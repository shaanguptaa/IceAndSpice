<div align="center">

# ![IceAndSpice Banner](https://github.com/shaanguptaa/IceAndSpice/assets/84842443/0e5986fb-0486-4b57-b1c1-1bce2f32541d)

A full-stack restaurant management web application built with **Django**, featuring online ordering, table reservations, user authentication, and an admin dashboard.

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-iceandspice.onrender.com-success?style=for-the-badge)](https://iceandspice.onrender.com)

![License](https://img.shields.io/github/license/shaanguptaa/IceAndSpice?style=for-the-badge)
![GitHub Stars](https://img.shields.io/github/stars/shaanguptaa/IceAndSpice?style=for-the-badge)
![GitHub Forks](https://img.shields.io/github/forks/shaanguptaa/IceAndSpice?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/shaanguptaa/IceAndSpice?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-3.2-092E20?style=for-the-badge&logo=django)

</div>

---

# 📖 About

**IceAndSpice** is a full-stack restaurant management system built with **Django** that enables customers to browse menus, place orders, reserve tables, and manage their profiles. The application also provides an administrative dashboard for efficiently managing menu items, reservations, customer orders, events, and promotional offers.

---

# ✨ Features

## 👤 Customer Features

- 🔐 User Registration & Authentication
- 👤 User Profile Management
- 🍽 Browse Menu by Categories
- 🛒 Shopping Cart
- 🧾 Place Food Orders
- 📅 Table Reservation System
- 🎉 Events & Special Offers
- ⭐ Customer Feedback

---

## 👨‍💼 Admin Features

- 📊 Admin Dashboard
- 🍕 Menu Management
- 📦 Order Management
- 🪑 Reservation Management
- 🎊 Events & Offers Management
- 👥 User Management (Django Admin)

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Backend | Django |
| Language | Python |
| Frontend | HTML, CSS, JavaScript, Bootstrap |
| Database | SQLite |
| Authentication | Django Authentication |
| Deployment | Render |
| Server | Gunicorn |
| Static Files | WhiteNoise |

---

# 🚀 Live Demo

### https://iceandspice.onrender.com/

---

# 📂 Project Structure

```text
IceAndSpice/
│
├── accounts/          # Authentication & profiles
├── menu/              # Menu management
├── orders/            # Cart & ordering
├── reservation/       # Table reservations
├── feedback/          # Customer feedback
├── events/            # Events & offers
├── static/
├── templates/
├── manage.py
└── requirements.txt
```

---

# ⚙️ Getting Started

## Clone the Repository

```bash
git clone https://github.com/shaanguptaa/IceAndSpice.git

cd IceAndSpice
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

---

## Apply Database Migrations

```bash
python manage.py migrate
```

---

## Create an Admin User

```bash
python manage.py createsuperuser
```

---

## Start the Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

# 📸 Preview

<div align="center">

![IceAndSpice Demo](https://github.com/shaanguptaa/IceAndSpice/assets/84842443/95bb1b2c-a566-4c05-9897-1c836cf0eb41)

</div>

---

# 🎯 Key Functionalities

- User Authentication & Authorization
- CRUD Operations
- Shopping Cart
- Order Processing
- Reservation Booking
- Feedback Management
- Event & Offer Management
- Django Admin Dashboard
- Responsive UI

---

# 🗺 Roadmap

- [x] Authentication
- [x] Shopping Cart
- [x] Order Management
- [x] Reservations
- [x] Events & Offers
- [x] Feedback System
- [ ] Online Payment Integration
- [ ] Email Notifications
- [ ] Order Tracking
- [ ] Wishlist
- [ ] Customer Reviews & Ratings
- [ ] REST API
- [ ] Docker Support

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/my-feature
```

3. Commit your changes

```bash
git commit -m "Add my feature"
```

4. Push the branch

```bash
git push origin feature/my-feature
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

Made with ❤️ using Django

</div>