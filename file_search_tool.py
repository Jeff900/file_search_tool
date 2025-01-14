import os
import re

def search_word_in_files(folder_path, search_word, show_all_matches=False, file_extension=None):
    """
    Searches for a specific word in all files within a given folder and its subfolders.

    :param folder_path: Path to the folder containing the files.
    :param search_word: The word to search for.
    :param show_all_matches: If True, shows all matches in a file instead of stopping at the first match.
    :param file_extension: If specified, only files with this extension will be searched (e.g., ".txt").
    """
    regex = re.compile(re.escape(search_word), re.IGNORECASE)
    total_files_scanned = 0
    total_matches_found = 0

    for root, _, files in os.walk(folder_path):
        for file_name in files:
            # Skip files if the extension doesn't match the filter
            if file_extension and not file_name.lower().endswith(file_extension.lower()):
                continue

            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    total_files_scanned += 1
                    match_found = False

                    for line_number, line in enumerate(file, start=1):
                        if regex.search(line):
                            print(f"Match found in: {file_path} (Line {line_number})")
                            total_matches_found += 1
                            match_found = True
                            if not show_all_matches:
                                break  # Stop searching this file if a match is found
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error accessing {file_path}: {e}")

    # Summary of the search results
    print("\n" + "-" * 60)
    print(f"Search completed.")
    print(f"Total files scanned: {total_files_scanned}")
    print(f"Total matches found: {total_matches_found}")
    print("-" * 60)

def main():
    """
    Main function to run the search with user inputs.
    """
    print("Welcome to the File Search Tool!")
    folder_path = input("Enter the folder path: ")
    search_word = input("Enter the word to search for: ")
    show_all_matches = input("Show all matches? (yes/no): ").strip().lower() == 'yes'
    file_extension = input("Filter by file extension (press Enter to skip): ").strip() or None

    search_word_in_files(folder_path, search_word, show_all_matches, file_extension)

if __name__ == "__main__":
    main()

