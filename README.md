# dynamic book record organizer 📖
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

## pictures 📸
  - initial run
  ![init](https://github.com/user-attachments/assets/d31b574d-8bb5-412b-b640-ec7dd6c0e5c9)

  - option 2
  ![option 2](https://github.com/user-attachments/assets/951074f8-4a97-4449-ae8a-ff7e0c9396b4)

  - option 3
  ![option 3](https://github.com/user-attachments/assets/bc4da696-b9d7-4d5d-bb3e-ba29998f5ce3)

  - option 5
  ![option 5](https://github.com/user-attachments/assets/8ff2f821-db88-4d04-ba82-8a9be9a0a73c)
