import csv
import os


# ================= FILE PATH =================

def get_file_path(filename):

    base_dir = os.path.dirname(os.path.abspath(__file__))

    folder = os.path.join(base_dir, "other_files")

    return os.path.join(folder, filename)


# ================= READ CSV =================

def read_csv():

    path = get_file_path("sales_data.csv")

    records = []

    try:

        with open(path, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                try:
                    row["Sales"] = int(row["Sales"])
                    records.append(row)

                except:
                    continue

    except FileNotFoundError:
        print("CSV file not found.")

    return records


# ================= DISPLAY RECORDS =================

def display_records(records):

    if not records:
        print("No data found.")
        return

    print("\nRecords:\n")

    for r in records:
        print(r["ID"], r["Name"], r["Sales"])


# ================= TOTAL SALES =================

def total_sales(records):

    total = sum(r["Sales"] for r in records)

    print("Total Sales:", total)


# ================= AVERAGE SALES =================

def average_sales(records):

    if not records:
        return

    avg = sum(r["Sales"] for r in records) / len(records)

    print("Average Sales:", round(avg, 2))


# ================= SORT RECORDS =================

def sort_records(records):

    sorted_data = sorted(records, key=lambda x: x["Sales"], reverse=True)

    print("\nSorted Records (High to Low):")

    for r in sorted_data:
        print(r["Name"], r["Sales"])

    return sorted_data


# ================= EXPORT CLEANED CSV =================

def export_csv(records):

    path = get_file_path("cleaned_data.csv")

    with open(path, "w", newline="") as file:

        fieldnames = ["ID", "Name", "Sales"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for r in records:
            writer.writerow(r)

    print("Cleaned CSV exported.")


# ================= MAIN MENU =================

def main_menu():

    records = read_csv()

    while True:

        print("\n====== CSV DATA PROCESSOR ======")
        print("1. Display Records")
        print("2. Calculate Total Sales")
        print("3. Calculate Average Sales")
        print("4. Sort Records")
        print("5. Export Cleaned CSV")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_records(records)

        elif choice == "2":
            total_sales(records)

        elif choice == "3":
            average_sales(records)

        elif choice == "4":
            records = sort_records(records)

        elif choice == "5":
            export_csv(records)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


# ================= PROGRAM START =================

if __name__ == "__main__":
    main_menu()