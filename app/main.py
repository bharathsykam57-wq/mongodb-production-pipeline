from app.services.user_service import add_user, get_all_users

def main():
    print("Starting MongoDB Production App...")

    new_user = {
        "name": "BHARATH",
        "role": "Data Scientist",
        "skills": ["Python", "MongoDB", "ML"],
        "source": "Python App"
    }

    inserted_id = add_user(new_user)
    print("Inserted User ID:", inserted_id)

    print("\nFetching all users from database:")
    users = get_all_users()

    for user in users:
        print(user)


if __name__ == "__main__":
    main()
