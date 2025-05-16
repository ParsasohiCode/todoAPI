# Todo Application

A modern, user-friendly Todo application built with FastAPI and MySQL. This application allows users to manage their tasks with a beautiful and intuitive interface.

## Features

- 🔐 User Authentication with Session Management
- ✨ Modern and Clean UI
- ✅ Create, Read, Update, and Delete todos
- 🎯 Mark todos as complete/incomplete
- 👤 User-specific todo lists
- 📱 Responsive design
- ⚡ Fast and efficient

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: MySQL
- **Frontend**: HTML, CSS
- **Templates**: Jinja2
- **Styling**: Custom CSS with modern design principles
- **Session Management**: Starlette Session Middleware

## Prerequisites

- Python 3.7+
- MySQL Server
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone http://github.com/ParsasohiCode/todoAPI
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

4. Set up environment variables:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` with your actual database credentials:
     ```env
     # Database Configuration
     DB_HOST=localhost
     DB_USER=your_username
     DB_PASSWORD=your_password
     DB_NAME=todo_db

     # Application Settings
     APP_PORT=8000
     APP_HOST=0.0.0.0
     
     # Security
     SECRET_KEY=your-secure-secret-key-here
     ```
   - Make sure to replace the placeholder values with your actual database credentials
   - Generate a secure SECRET_KEY for session management
   - Never commit the `.env` file to version control

5. Create the required database tables:
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    last_login TIMESTAMP
);

CREATE TABLE todos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(50) NOT NULL
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

1. **Authentication**
   - Access the application at `http://localhost:8000`
   - Register a new account or login with existing credentials
   - Your session will be maintained securely using encrypted cookies

2. **Managing Todos**
   - Add new todos using the input field at the top
   - View only your personal todos
   - Mark todos as complete/incomplete using the "Complete" button
   - Delete todos using the "Delete" button
   - View creation dates for each todo

3. **Logout**
   - Click the "Logout" button in the top-left corner to end your session
   - You'll be redirected to the login page

## Project Structure

```
todoAPI/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment variables
├── .env                # Environment variables (not in git)
├── static/
│   └── css/
│       ├── style.css   # Main styles
│       └── login.css   # Login page styles
└── templates/
    ├── index.html      # Todo list page
    ├── login.html      # Login page
    └── register.html   # Registration page
```

## Environment Variables

The application uses the following environment variables (configured in `.env`):

| Variable | Description | Default |
|----------|-------------|---------|
| DB_HOST | Database host | localhost |
| DB_USER | Database username | - |
| DB_PASSWORD | Database password | - |
| DB_NAME | Database name | todo_db |
| APP_PORT | Application port | 8000 |
| APP_HOST | Application host | 0.0.0.0 |
| SECRET_KEY | Session encryption key | - |

To set up your environment:
1. Copy `.env.example` to `.env`
2. Update the values in `.env` with your actual configuration
3. Generate a secure SECRET_KEY for session management
4. Never commit `.env` to version control

## Features in Detail

### Authentication & Session Management
- Secure login system with session-based authentication
- Encrypted session cookies for user data
- Protected routes requiring authentication
- Automatic session expiration

### Todo Management
- Create new todos
- View user-specific todo lists
- Mark todos as complete/incomplete
- Delete todos
- View todo creation dates

### Security Features
- Session-based authentication
- Encrypted session data
- Protected routes
- Secure password storage
- User-specific data isolation

## Contributing

Feel free to submit issues and enhancement requests!
https://roadmap.sh/projects/todo-list-api

## License

This project is licensed under the MIT License - see the LICENSE file for details.
