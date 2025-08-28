import requests

def fetch_and_display_users(num_users):  
    try:
        # API endpoint
        url = "https://jsonplaceholder.typicode.com/users"

        # GET request
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # raise exception if bad status (404, 500, etc.)

        # Convert JSON response to Python (list of dictionaries)
        users = response.json()

        # Handle out-of-bounds case
        if num_users > len(users):
            print(f"Requested {num_users} users, but only {len(users)} available.")
            num_users = len(users)

        # Loop through required number of users
        for user in users[:num_users]:
            try:
                name = user["name"]
                email = user["email"]
                city = user["address"]["city"]
                print(f"Name: {name}, Email: {email}, City: {city}")
            except KeyError as e:
                print(f"Missing key in user data: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None
    except ValueError:
        print(" Failed to parse JSON response.")
        return None


# Example calls (testing)
if __name__ == "__main__":
    print("Fetching 3 users:\n")
    fetch_and_display_users(3)

    print("\nFetching 15 users (out-of-bounds test):\n")
    fetch_and_display_users(15)
