def find_number(limit):
    print("Searching...")
    for num in range(1, limit):
        if num == 3:
            print("Found 3!")
            return "SUCCESS"
        print("Checked:", num)
    return "NOT FOUND"

def start_search():
    print("App Shuru")
    status = find_number(5)
    print("Status:", status)

# Execution shuru ekhane
start_search()