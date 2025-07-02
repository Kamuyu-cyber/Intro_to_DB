import mysql.connector
from mysql.connector import Error

def create_database_and_tables():
    connection = None
    cursor = None
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",  # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )
        
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        
        # Use the database
        cursor.execute("USE alx_book_store")
        
        # Create Authors table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Authors (
                author_id INT PRIMARY KEY AUTO_INCREMENT,
                author_name VARCHAR(215) NOT NULL
            )
        """)
        
        # Create Books table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Books (
                book_id INT PRIMARY KEY AUTO_INCREMENT,
                title VARCHAR(130) NOT NULL,
                author_id INT,
                price DOUBLE NOT NULL,
                publication_date DATE,
                FOREIGN KEY (author_id) REFERENCES Authors(author_id)
            )
        """)
        
        # Create Customers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Customers (
                customer_id INT PRIMARY KEY AUTO_INCREMENT,
                customer_name VARCHAR(215) NOT NULL,
                email VARCHAR(215) NOT NULL,
                address TEXT
            )
        """)
        
        # Create Orders table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Orders (
                order_id INT PRIMARY KEY AUTO_INCREMENT,
                customer_id INT,
                order_date DATE NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
            )
        """)
        
        # Create Order_Details table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Order_Details (
                orderdetailid INT PRIMARY KEY AUTO_INCREMENT,
                order_id INT,
                book_id INT,
                quantity DOUBLE NOT NULL,
                FOREIGN KEY (order_id) REFERENCES Orders(order_id),
                FOREIGN KEY (book_id) REFERENCES Books(book_id)
            )
        """)
        
        # Commit the changes
        connection.commit()
        print("All tables created successfully in 'alx_book_store' database!")
        
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        # Close cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection is not None and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database_and_tables()
