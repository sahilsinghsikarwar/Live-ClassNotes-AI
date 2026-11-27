import os
from getpass import getpass
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.getenv("SUPABASE_URL")
secret_key = os.getenv("SUPABASE_SECRET_KEY")

if not url or not secret_key:
    raise ValueError("Supabase credentials missing in .env")

supabase = create_client(url, secret_key)

teachers = [
    {
        "name": "Sahil Singh",
        "email": "sahilsikarwar138@gmail.com",
        "id": "2454be5e-b6a9-4c35-8216-725bd530faa3"
    },
    {
        "name": "Sakshi Negi",
        "email": "negisakshi256@gmail.com",
        "id": "6794fcdd-3f0d-4c6c-8b0a-a9fce344ef65"
    }
]

for teacher in teachers:
    print(f"\nSet password for {teacher['name']} ({teacher['email']})")
    password = getpass("Enter password: ")
    confirm = getpass("Confirm password: ")

    if password != confirm:
        print("Passwords do not match. Skipped.")
        continue

    if len(password) < 8:
        print("Password must be at least 8 characters.")
        continue

    try:
        supabase.auth.admin.update_user_by_id(
            teacher["id"],
            {
                "password": password,
                "email_confirm": True,
                "user_metadata": {
                    "full_name": teacher["name"],
                    "name": teacher["name"]
                }
            }
        )
        print(f"Password and metadata successfully updated for {teacher['name']} ({teacher['email']})")

    except Exception as e:
        print(f"Failed for {teacher['email']}: {e}")
