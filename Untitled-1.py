import json
import os
import time

# Nama file JSON
FILE_NAME = "data.json"

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Fungsi untuk membaca file JSON
def read_json_file():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"Assignment": {}}  # Jika file tidak ditemukan, buat struktur awal
    except json.JSONDecodeError:
        return {"Assignment": {}}  # Jika file kosong atau rusak

# Fungsi untuk menulis ke file JSON
def write_json_file(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Menu utama
def menu():
    clear_screen()  # Membersihkan layar sebelum menampilkan menu
    print("\nLoading menu...")
    time.sleep(0.5)  # Animasi kecil
    print("1. Add Assignment\n2. Remove Assignment\n3. View Assignments\n4. Update Assignment Status\n5. Exit\n")
    askmenu = input("Enter your choice: ")
    if askmenu == "1":
        add_assignment()
    elif askmenu == "2":
        remove_assignment()
    elif askmenu == "3":
        view_assignments()
    elif askmenu == "4":
        update_assignment_status()
    elif askmenu == "5":
        exit()
    else:
        print("Invalid input. Please try again.")
        time.sleep(1)
        menu()

# Menambahkan tugas baru
def add_assignment():
    clear_screen()  # Membersihkan layar sebelum menambahkan tugas
    print("\nPreparing to add assignment...")
    time.sleep(0.5)
    assignment = input("Enter assignment: ")
    due_date = input("Enter due date: ")
    status = "sedang dikerjakan"  # Status default saat tugas dibuat

    # Baca data lama dari file
    data = read_json_file()

    # Tambahkan tugas baru ke Assignment
    task_id = f"Task {len(data['Assignment']) + 1}"  # ID untuk tugas baru
    data["Assignment"][task_id] = {
        "assignment": assignment,
        "due_date": due_date,
        "status": status
    }

    # Simpan data ke file
    write_json_file(data)

    print("Adding assignment...")
    time.sleep(0.5)
    print("Assignment added.")
    time.sleep(1)
    menu()

# Menghapus tugas
def remove_assignment():
    clear_screen()  # Membersihkan layar sebelum menghapus tugas
    print("\nPreparing to remove an assignment...")
    time.sleep(0.5)
    print("List Assignments:")
    data = read_json_file()

    if not data["Assignment"]:
        print("No assignments found.")
    else:
        for task_id, details in data["Assignment"].items():
            print(f"{task_id}: {details['assignment']} (Due Date: {details['due_date']}, Status: {details['status']})")
    
    task_id = input("Enter Task ID to remove (e.g., Task 1): ")

    # Hapus tugas jika ada
    if task_id in data["Assignment"]:
        print(f"Removing {task_id}...")
        time.sleep(0.5)
        del data["Assignment"][task_id]
        write_json_file(data)
        print(f"{task_id} removed.")
    else:
        print("Task not found.")

    time.sleep(1)
    menu()

# Melihat daftar tugas
def view_assignments():
    clear_screen()  # Membersihkan layar sebelum menampilkan daftar tugas
    print("\nLoading assignments...")
    time.sleep(0.5)
    data = read_json_file()

    if not data["Assignment"]:
        print("No assignments found.")
    else:
        for task_id, details in data["Assignment"].items():
            print(f"{task_id}: {details['assignment']} (Due Date: {details['due_date']}, Status: {details['status']})")

    input("\nPress Enter to return to menu...")
    menu()

# Memperbarui status tugas
def update_assignment_status():
    clear_screen()  # Membersihkan layar sebelum memperbarui status
    print("\nUpdating assignment status...")
    time.sleep(0.5)
    data = read_json_file()

    if not data["Assignment"]:
        print("No assignments found.")
    else:
        for task_id, details in data["Assignment"].items():
            print(f"{task_id}: {details['assignment']} (Due Date: {details['due_date']}, Status: {details['status']})")

        task_id = input("Enter Task ID to update (e.g., Task 1): ")

        if task_id in data["Assignment"]:
            print(f"Current Status: {data['Assignment'][task_id]['status']}")
            new_status = input("Enter new status (e.g., sedang dikerjakan/sudah dikerjakan): ")
            data["Assignment"][task_id]["status"] = new_status
            write_json_file(data)
            print(f"Status for {task_id} updated to '{new_status}'.")
        else:
            print("Task not found.")

    time.sleep(1)
    menu()

# Fungsi keluar
def exit():
    clear_screen()  # Membersihkan layar saat keluar
    print("\nExiting the program...")
    time.sleep(0.5)
    print("Goodbye!")
    quit()

# Jalankan menu utama
menu()
