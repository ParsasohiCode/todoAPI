import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database connection configuration
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

def create_database():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS todolist")
        print("Database created successfully")
        
        # Use the database
        cursor.execute("USE todolist")
        
        # Create todos table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                completed BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                password_hash VARCHAR(255) NOT NULL,
                last_login TIMESTAMP
            )
        """)
        
        # Insert sample data into todos
        sample_todos = [
            ('Buy groceries', False),
            ('Finish project', True),
            ('Call the bank', False)
        ]
        
        cursor.executemany("""
            INSERT INTO todos (title, completed) 
            VALUES (%s, %s)
        """, sample_todos)
        
        # Insert sample users
        sample_users = [
            ('testuser1', 'dummyhash1'),
            ('testuser2', 'dummyhash2')
        ]
        
        cursor.executemany("""
            INSERT INTO users (username, password_hash) 
            VALUES (%s, %s)
        """, sample_users)
        
        # Commit the changes
        conn.commit()
        print("Tables created and sample data inserted successfully")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Database connection closed")

if __name__ == "__main__":
    create_database() 