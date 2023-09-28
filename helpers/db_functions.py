import sqlite3

def createDb():
    conn = sqlite3.connect('bulk-upload.db')
    cursor = conn.cursor()

    # Create a table to store webhook data
    cursor.execute('''CREATE TABLE IF NOT EXISTS webhook_data (
                    id TEXT,
                    transcription_url TEXT,
                    received BOOLEAN
                    )''')
    conn.commit()
    conn.close()

def addEntry(id, transcription_url):
# Insert data into the SQLite database
    conn = sqlite3.connect('bulk-upload.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO webhook_data (id, transcription_url, received) VALUES (?, ?, ?)", (id,transcription_url, False))
    conn.commit()
    conn.close()

def printTable():
    # Connect to your SQLite database
    conn = sqlite3.connect('bulk-upload.db')  # Replace 'your_database.db' with your database file name
    cursor = conn.cursor()

    # Replace 'your_table' with the name of your table
    table_name = 'webhook_data'

    # Fetch all rows from the table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Print the table data
    for row in rows:
        print(row)

    # Close the database connection
    conn.close()

def update_received_status(id):
    conn = sqlite3.connect('bulk-upload.db')
    cursor = conn.cursor()

    # Update the received status to True for the matching ID
    cursor.execute("UPDATE webhook_data SET received = 1 WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def get_status():
    conn = sqlite3.connect('bulk-upload.db')
    cursor = conn.cursor()

    # Count the number of rows with received = 1
    cursor.execute("SELECT COUNT(*) FROM webhook_data WHERE received = 1")
    received_count = cursor.fetchone()[0]

    # Count the total number of rows
    cursor.execute("SELECT COUNT(*) FROM webhook_data")
    total_count = cursor.fetchone()[0]

    conn.close()

    if received_count == total_count:
        return f"All {total_count} transcription text files have been received."
    else:
        return f"{received_count} of the {total_count} transcription text files have been received."