from database import get_engine, get_session
from services.user_service import create_user, list_users, get_user_by_id, delete_user

engine = get_engine()
session = get_session(engine)

print("Database connection done.\n")

print("Creating User: Fernando")
user = create_user(session, "Fernando")
print(f"User created: id={user.id}, name={user.name}\n")

print("Listing all users:")
users = list_users(session)
for u in users:
    print(f"- id={u.id}, name={u.name}")
print()

print("Testing getting a user by id")
user = get_user_by_id(session, 1)
print(f"Found user: id={user.id}, name={user.name}\n")

print("Deleting user Fernando")
delete_user(session, 1)
print("User deleted.\n")

print("Listing users after deletion:")
users = list_users(session)
for u in users:
    print(f"- id={u.id}, name={u.name}")
print()

print("USER SERVICE IS RUNNING CORRECTLY")