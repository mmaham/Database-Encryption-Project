import sqlite3

# Function to setup the database
def setup_database():
    conn = sqlite3.connect('patient_data.db')
    c = conn.cursor()

    # Create Users table
    c.execute('''CREATE TABLE IF NOT EXISTS Users
                 (Username TEXT PRIMARY KEY, Password TEXT, Role TEXT)''')

    # Create Patients table
    c.execute('''CREATE TABLE IF NOT EXISTS Patients
                 (Name TEXT, DOB TEXT, Age TEXT, Gender TEXT, Date TEXT, MedicalConditions TEXT, Prescription TEXT)''')

    conn.commit()
    conn.close()

# Run the setup function
setup_database()

print("Database setup complete.")
