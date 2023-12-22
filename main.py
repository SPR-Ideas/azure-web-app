"""
    Description : An test application for Azure Web app .
"""

from fastapi import FastAPI
import uvicorn
import pyobdc

app = FastAPI()

# Set your database connection parameters
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'



def connect_to_db():

    # Construct the connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    # Try to establish a connection
    try:
        # Establish the database connection
        connection = pyodbc.connect(connection_string)

        # Create a cursor from the connection
        cursor = connection.cursor()

        # Example: Execute a simple SQL query
        cursor.execute("SELECT @@version;")
        row = cursor.fetchone()

        # Display the result
        print("Connected to SQL Server. Server version:", row[0])

    except pyodbc.Error as e:
        # Handle any connection errors
        print("Error connecting to SQL Server:", e)

    finally:
        # Close the connection, whether successful or not
        if connection:
            connection.close()
            print("Connection closed.")


@app.get("/heath-check")
def health_check():
    """Returns Hello world"""
    return "hello world"

app.get("/")
def homePage():
    """
        Returns the Home Page.
    """
    return "Home page"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
