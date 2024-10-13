import json
import os

NOTES_FILE = "notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, 'r') as f:
        return json.load(f)

def save_notes(notes):
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=4)

def add_note():
    title = input("Enter the note title: ")
    content = input("Enter the note content: ")
    notes = load_notes()
    notes.append({"title": title, "content": content})
    save_notes(notes)
    print(f"Note '{title}' added!")

def view_notes():
    notes = load_notes()
    if not notes:
        print("No notes available.")
        return
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note['title']}\n   {note['content']}\n")

def search_notes():
    keyword = input("Enter a keyword to search: ").lower()
    notes = load_notes()
    found = [note for note in notes if keyword in note['title'].lower() or keyword in note['content'].lower()]
    if found:
        for note in found:
            print(f"{note['title']}\n{note['content']}\n")
    else:
        print("No matching notes found.")

def delete_note():
    title = input("Enter the title of the note to delete: ")
    notes = load_notes()
    notes = [note for note in notes if note['title'].lower() != title.lower()]
    save_notes(notes)
    print(f"Note '{title}' deleted, if it existed.")

def menu():
    while True:
        print("\nSimple Notes App")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            search_notes()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
