# File Search Tool

![file_search_tool](assets/banner.png)

A Python tool for searching a specific word across multiple files in a folder and its subfolders. This utility scans files, displays matches, and provides a summary of the results, making it a great tool for text analysis or code auditing tasks.

---

## 📦 Project Structure

```plaintext
├── assets/               # Folder for assets like images and media
│   ├── banner.png        # Banner image for the README
├── file_search_tool.py   # Main script for running the tool
├── README.md             # Project documentation
```

---

## 🚀 Features

- **Search for a word:** Scan files in a folder and its subfolders for a specific word.  
- **Flexible search options:**  
   - Choose to display the first match or all matches per file.  
   - Optional file extension filtering (e.g., `.txt`, `.py`).  
- **User-Friendly Interface:** Prompts guide the user through the search process.  
- **Error Handling:** Skips files with restricted permissions or read issues.  
- **Clear Summary:** Displays the number of files scanned and matches found.

---

## 🛠️ Technologies Used

- Python 3.x  
- Core Libraries: `os`, `re`

---

## 📖 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/MaPitelli/file_search_tool.git
cd file_search_tool
```

### 2. Run the Script
```bash
python file_search_tool.py
```

### 3. Follow the Prompts:
- Enter the folder path where you want to search.  
- Provide the word to search for.  
- Choose whether to show all matches or stop after the first match per file.  
- (Optional) Specify a file extension filter (e.g., `.txt`).

### 4. Example Output:
```plaintext
Welcome to the File Search Tool!
Enter the folder path: /my-folder
Enter the word to search for: error
Show all matches? (yes/no): yes
Filter by file extension (press Enter to skip): .py

Match found in: /my-folder/script1.py (Line 23)
Match found in: /my-folder/script2.py (Line 10)
------------------------------------------------------------
Search completed.
Total files scanned: 5
Total matches found: 2
------------------------------------------------------------
```

---

## 📋 Project Functionality Overview

### `search_word_in_files(folder_path, search_word, show_all_matches=False, file_extension=None)`
- **folder_path**: Path to the folder where the search will occur.  
- **search_word**: The word or phrase to search for.  
- **show_all_matches**: If `True`, displays all matches in each file. If `False`, stops after the first match per file.  
- **file_extension**: Optional filter to scan only files with a specific extension (e.g., `.txt`).  

---

## ✅ Best Use Cases
- Code auditing and debugging.  
- Searching for keywords in documentation files.  
- Text analysis and log file inspection.  

---

## 📦 Requirements
- Python 3.x  
- No external libraries required.  

---

## 🛠️ Feedback
Your feedback is welcome! If you notice any bugs or have suggestions for improvements, feel free to open an issue in the repository.

---

## ✨ Contact

- **Author:** [Maíra Pitelli](https://github.com/MaPitelli)
- **Email:** mairapitelli@hotmail.com
- **LinkedIn:** [click here to check my LinkedIn profile](https://www.linkedin.com/in/mairapitelli/)
