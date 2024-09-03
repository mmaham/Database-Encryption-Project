from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import sqlite3
import base64

# Use a fixed key for both encryption and decryption
encryption_key = b'Sixteen byte key'

# Function to encrypt data using AES
def encrypt_data(data, key):
    data_bytes = data.encode('utf-8')
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data_bytes, AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    return base64.b64encode(iv + ciphertext).decode('utf-8')

# Main function to store patient data
def store_patient_data():
    name = input("Enter patient name: ")
    dob = input("Enter patient date of birth (YYYY-MM-DD): ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    date = input("Enter the date of record (YYYY-MM-DD): ")
    medical_conditions = input("Enter medical conditions: ")
    prescription = input("Enter prescription: ")

    encrypted_name = encrypt_data(name, encryption_key)
    encrypted_dob = encrypt_data(dob, encryption_key)
    encrypted_gender = encrypt_data(gender, encryption_key)

    conn = sqlite3.connect('patient_data.db')
    c = conn.cursor()

    c.execute("INSERT INTO Patients (Name, DOB, Age, Gender, Date, MedicalConditions, Prescription) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (encrypted_name, encrypted_dob, age, encrypted_gender, date, medical_conditions, prescription))
    conn.commit()
    conn.close()

    print("Patient data has been encrypted and stored in the database.")

if __name__ == "__main__":
    store_patient_data()
