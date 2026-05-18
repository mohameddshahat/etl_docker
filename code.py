import requests
import pandas as pd
import sqlite3

# =========================
# Extract
# =========================

url = "https://dummyjson.com/users"

response = requests.get(url, timeout=10)

data = response.json()

users = data["users"]

df = pd.DataFrame(users)

print("Original Data:")
print(df.head())

# =========================
# Transform
# =========================

df = df[[
    "id",
    "firstName",
    "lastName",
    "email",
    "phone",
    "age"
]]

df["full_name"] = df["firstName"] + " " + df["lastName"]

df = df.drop(columns=["firstName", "lastName"])

print("\nTransformed Data:")
print(df.head())

# =========================
# Load
# =========================

conn = sqlite3.connect("/app/data/users.db")

df.to_sql(
    "users",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("\nData loaded successfully!")