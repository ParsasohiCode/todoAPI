# Todo Application

A modern, user-friendly Todo application built with FastAPI and MySQL. This application allows users to manage their tasks with a beautiful and intuitive interface.

## Features

- 🔐 User Authentication
- ✨ Modern and Clean UI
- ✅ Create, Read, Update, and Delete todos
- 🎯 Mark todos as complete/incomplete
- 📱 Responsive design
- ⚡ Fast and efficient

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS
- **Templates**: Jinja2
- **Styling**: Custom CSS with modern design principles

## Prerequisites

- Python 3.7+
- MySQL Server
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd todoAPI
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your database credentials:
```env
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database_name
```

5. Create the required database tables:
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Running the Application

1. Start the FastAPI server:
```bash
python main.py
```

2. Open your browser and navigate to:
```
http://localhost:8000
```

## Usage

1. **Login**
   - Access the application at `http://localhost:8000`
   - Enter your username and password
   - Click "Login"

2. **Managing Todos**
   - Add new todos using the input field at the top
   - Mark todos as complete/incomplete using the "Complete" button
   - Delete todos using the "Delete" button
   - View creation dates for each todo

3. **Logout**
   - Click the "Logout" button in the top-left corner to end your session

## Project Structure

```
todoAPI/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── .env                # Environment variables
├── static/
│   └── css/
│       ├── style.css   # Main styles
│       └── login.css   # Login page styles
└── templates/
    ├── index.html      # Todo list page
    └── login.html      # Login page
```

## Features in Detail

### Authentication
- Secure login system
- Session management
- Protected routes

### Todo Management
- Create new todos
- Mark todos as complete/incomplete
- Delete todos
- View todo creation dates

### User Interface
- Clean and modern design
- Responsive layout
- Intuitive navigation
- Visual feedback for actions
- Error handling with user-friendly messages

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
