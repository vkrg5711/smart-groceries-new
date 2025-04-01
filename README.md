# smart-groceries-new
# smart-groceries-List application

---

## 🛒 Smart Groceries – Application Overview

Smart Groceries is a Django-based web application for collaborative grocery list management.  
It enables individual users to create and manage their own grocery lists while also supporting **sharing functionality** via secure token-based access.

---

### 🔐 Authentication & Authorization

- Users can register and log in using Django’s built-in authentication system.
- Once logged in, users can only access and manage their own grocery lists.
- Access to shared grocery lists is controlled using a secure **share token**, which acts like a temporary public link.

---

### 🧺 Grocery List Management

- Users can create grocery lists with items (e.g., Milk, Eggs).
- Each list is uniquely tied to the user.
- Supported actions include:
  -  Create new list
  -  Edit list details and items
  - Delete items or entire lists
  -  View recent items

---

### 🔗 Sharing Functionality

- Lists can be shared using a token-based link via the `get_share_link()` feature.
- Others can view shared lists using the `share_list()` view, which validates the token securely.
- These functions are implemented inside a **custom reusable library module** (`library/sharing.py`).

---

### 🧠 Custom Library Module

The file `library/sharing.py` includes a class `SharingManager` that:
- Handles creation of share tokens
- Returns the associated list securely using a view function

This separation improves reusability and maintainability of sharing-related logic.

---

### ⚙ Configuration & Setup

All settings are located in:
- `groceries/settings.py` – Django project settings
- `grocery/views.py` – Application views and logic
- `grocery/models.py` – Models for grocery lists and share tokens

---

### 📦 Installed Requirements

All required Python packages are listed in `req.txt`.  
To install them, run:

```bash
pip install -r groceries/req.txt
```

This includes:
- `Django` (web framework)
- `uuid` (for generating share tokens – part of Python stdlib)
- Any image/static management libraries (optional)

---

### 🚀 How to Run the Project

1. Clone or download the repository
2. Navigate into the `groceries` directory
3. Install dependencies:
   ```bash
   pip install -r req.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```

Then, access the application at:  
http://127.0.0.1:8000/

---

### ✅ Summary

Smart Groceries combines user-specific data management with secure list sharing and extensible utility modules. It demonstrates strong separation of concerns between view logic, data models, and business utilities.

