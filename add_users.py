import sqlite3

# Function to add users to the database
def add_users():
    users = [
        ('admin', 'adminpassword', 'Admin'),
        ('tier1', 'tier1password', 'Tier1'),
        ('tier2', 'tier2password', 'Tier2')
    ]

    conn = sqlite3.connect('patient_data.db')
    c = conn.cursor()

    # Insert users into the Users table
    c.executemany("INSERT INTO Users (Username, Password, Role) VALUES (?, ?, ?)", users)

    conn.commit()
    conn.close()

    print("Users have been added to the database.")

# Run the add users function
add_users()
