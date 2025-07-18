# 📝 Django Blog App

**Django Blog App** is a web-based blogging platform built using Django. It allows users to register, create, update, and delete blog posts with secure authentication and profile management. Designed using Django’s class-based views and a robust backend structure, this app provides a responsive and user-friendly interface for sharing ideas and content.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

---

## Project Overview

**Django Blog App** was developed to demonstrate a full-featured blog platform using Django's MVC/MVT architecture. It includes user authentication, profile updates, blog post management, and secure authorization. The platform ensures that only authorized users can edit or delete their posts and features a clean UI with paginated blog posts and user-specific views.

---

## ✨ Features

- 🔐 **User Registration & Login**: Secure authentication with Django's built-in auth system.
- 👤 **Profile Management**: Update username, email, and profile picture.
- ✍️ **Create, Read, Update, Delete Posts**: Users can manage their own posts with class-based views.
- 📄 **Post Detail Pages**: View individual posts with timestamp and author info.
- 🔎 **User-Based Filtering**: Filter posts by specific users.
- ✅ **Authorization Checks**: Only authors can edit or delete their own posts.
- 💬 **Flash Messages**: Success and error messages using Django's message framework.
- 📚 **Pagination**: Easily browse large sets of posts.

---

## Tech Stack

- **Framework**: Django (Python)
- **Frontend**: HTML5, CSS3, Bootstrap
- **Database**: SQLite (default), PostgreSQL compatible
- **Image Handling**: Pillow (for profile pictures)
- **Other Packages**: Django Messages Framework, Crispy Forms (optional)

---

## System Architecture

- **Authentication**: Built-in Django auth for secure registration, login, logout.
- **Views**: Class-Based Views (ListView, DetailView, CreateView, UpdateView, DeleteView) for clean code separation.
- **User Profile**: Extended user model via `OneToOneField` to store extra profile info.
- **Static & Media Files**: Profile pictures handled via media directory; Bootstrap and custom styles in static directory.
- **URL Routing**: Modular `urls.py` files for blog and users apps.
  
---

## Getting Started

### Prerequisites

- Python 3.8+
- Django
- pip
- Git

### Installation

1. **Clone the Repository**
    ```bash
   git clone https://github.com/yourusername/django-blog-app.git
   cd django-blog-app
    ```

2. **Create Virtual Environment & Activate**
    ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   # source venv/bin/activate    # macOS/Linux
    ```

3. **Install Requirements**
    ```bash
   pip install -r requirements.txt
    ```

4. **Apply Migrations**
    ```bash
   python manage.py makemigrations
   python manage.py migrate
    ```

5. **Create Superuser**
    ```bash
   python manage.py createsuperuser
    ```

6. **Run the Server**
    ```bash
   python manage.py runserver
    ```

---

## Usage

- Visit: \`http://127.0.0.1:8000/\`
- Register a new account or login.
- View posts from all users on the homepage.
- Create, update, or delete your posts.
- Go to your profile to update username, email, or upload profile picture.
- Click on a username to view posts by that specific user.
- Only post authors can see update/delete buttons on their posts.
  
---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create your feature branch:
    ```bash
   git checkout -b feature/my-feature
    ```
3. Commit your changes:
    ```bash
   git commit -m "Add my feature"
    ```
4. Push to the branch:
    ```bash
   git push origin feature/my-feature
    ```
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Authors

- Mahnoor Shahid

---

## Acknowledgments

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Corey Schafer’s Django Series on YouTube](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
- The amazing open-source Django community

---

## Contact

For questions or collaboration, feel free to open an issue or reach out directly via GitHub.
