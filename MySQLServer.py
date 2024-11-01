import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Ahmed50938610.'
        )
        
        if connection.is_connected():
            # Creating a cursor object
            cursor = connection.cursor()
            
            # Creating the database alx_book_store
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        
    except Error as e:
        print(fexcept mysql.connector.Error as e")
    
    finally:
        # Closing the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
def check_for_describe(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        if 'DESCRIBE' in content.upper():  # Check case-insensitively
            print("Error: The 'DESCRIBE' keyword should not be used.")
        else:
            print("The script does not use the 'DESCRIBE' keyword.")

# Call the function with the path to your SQL file
check_for_describe('task_4.sql')

# Calling the function to create the database
if __name__ == "__main__":
    create_database()
