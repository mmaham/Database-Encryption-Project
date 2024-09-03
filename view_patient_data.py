from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad
import sqlite3
import base64

# Function to decrypt data using AES
def decrypt_data(encrypted_data, key):
    encrypted_data_bytes = base64.b64decode(encrypted_data)
    iv = encrypted_data_bytes[:AES.block_size]
    ciphertext = encrypted_data_bytes[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = cipher.decrypt(ciphertext)
    return unpad(padded_data, AES.block_size).decode('utf-8')

# Function to get user credentials from the database
def get_user(username, password):
    conn = sqlite3.connect('patient_data.db')
    c = conn.cursor()
    c.execute("SELECT Role FROM Users WHERE Username=? AND Password=?", (username, password))
    user = c.fetchone()
    conn.close()
    return user

# Function to view patient data based on role
def view_patient_data():
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = get_user(username, password)

    if user is None:
        print("Invalid username or password.")
        return

    role = user[0]
    conn = sqlite3.connect('patient_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Patients")
    patients = c.fetchall()
    conn.close()

    key = get_random_bytes(16)  # 16 bytes (128 bits) for AES-128

    for patient in patients:
        name, dob, age, gender, date, medical_conditions, prescription = patient

        if role == 'Admin':
            name = decrypt_data(name, key)
            dob = decrypt_data(dob, key)
            gender = decrypt_data(gender, key)
        elif role == 'Tier1':
            name = decrypt_data(name, key)
            dob = decrypt_data(dob, key)
            gender = decrypt_data(gender, key)
            medical_conditions = '[ENCRYPTED]'
            prescription = '[ENCRYPTED]'
        elif role == 'Tier2':
            name = '[ENCRYPTED]'
            dob = '[ENCRYPTED]'
            gender = '[ENCRYPTED]'

        print(f"Name: {name}, DOB: {dob}, Age: {age}, Gender: {gender}, Date: {date}, Medical Conditions: {medical_conditions}, Prescription: {prescription}")

if __name__ == "__main__":
    view_patient_data()
