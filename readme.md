# book record organizer 📖
a circular linked list system designed to efficiently organize book records, featuring invalid year filtering, record insertions, and cleanup capabilities.

## features 👾
- **year extraction:** creates a `{year}.txt` file containing records based on a specified year.
- **record deletion:** removes consecutive repeated records from the list to maintain data integrity.
- **author records:** generates a new list that includes only the records from a specified author.
- **insertion before isbn:** inserts a book object before a record with a given isbn number.
- **insertion between isbns:** inserts a book object between two specified isbn numbers, provided both are found in the list.
- **isbn swaps:** swaps the positions of two isbn numbers in the list if they exist.
- **commit changes:** saves the updated list to a file named `commit.txt` upon command.
- **stop talking:** terminates the conversation and exits the program.

## running the project 🏁
to get the project up and running on your local machine, follow these steps:

- **ensure python is installed:** must have [python version ^3.11](https://www.python.org/downloads/) installed.
- **clone the repository:**
```bash
git clone https://github.com/barbaraeguche/book-record-organizer.git
```
- **navigate to the project directory:**
```bash
cd book-record-organizer
```
- **run the project:**
```bash
python3 driver.py
```

## gallery 📸
<details>
  <summary>showcase</summary>

  - **initial run**
  ![init](https://github.com/user-attachments/assets/606431a7-8c27-47e3-aebb-95f7b88e7b30)

  - **option 2**
  ![option 2](https://github.com/user-attachments/assets/356ddeaf-7a31-4aba-b1d4-1f2abea51312)

  - **option 3**
  ![option 3](https://github.com/user-attachments/assets/863fc0a0-ba9d-4c4c-9400-bac0d83d1cb2)

  - **option 5**
  ![option 5](https://github.com/user-attachments/assets/6f9764c9-b6a1-4094-9706-b8202cc28c17)
</details>
