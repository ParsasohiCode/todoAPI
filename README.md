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
     ```
   - Make sure to replace the placeholder values with your actual database credentials
   - Never commit the `.env` file to version control

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
├── .env.example        # Example environment variables
├── .env                # Environment variables (not in git)
├── static/
│   └── css/
│       ├── style.css   # Main styles
│       └── login.css   # Login page styles
└── templates/
    ├── index.html      # Todo list page
    └── login.html      # Login page
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

To set up your environment:
1. Copy `.env.example` to `.env`
2. Update the values in `.env` with your actual configuration
3. Never commit `.env` to version control

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
https://roadmap.sh/projects/todo-list-api

## License

This project is licensed under the MIT License - see the LICENSE file for details.
