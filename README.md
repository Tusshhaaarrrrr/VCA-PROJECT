# Changelog Generator

A Python-based Changelog Generator that automates the process of creating a changelog from Git commit messages. This tool clones a GitHub repository, extracts commit messages between tags, and generates a `CHANGELOG.md` file in the current working directory.

---

Features:

1. Automates Git operations:
      - Clones a GitHub repository.

- Extracts commit messages between Git tags.

2. Generates a formatted changelog:
      - Outputs the changelog to a `CHANGELOG.md` file in the root directory.

3. Cleans up temporary files and directories after execution.

4. Saves the changelog in the same directory where the script is executed.

---

Prerequisites:

1. Python: Ensure Python 3.6 or later is installed.

2. Git: Make sure Git is installed and added to your system's PATH.

---

Installation:

1. Clone this repository:

   ```
   git clone https://github.com/Tusshhaaarrrrr/VCA-PROJECT.git
   ```

2. Install dependencies:

- No external libraries required; Python's standard library is used.

---

Usage:

1. Run the script:
   ```
   python main.py
   ```
2. Enter the GitHub repository URL when prompted.

3. The changelog will be generated as `CHANGELOG.md` in the current directory.

---

Directory Structure:

- `temp_repo/`: Temporary repository clone (deleted after execution)

- `main.py`: Main script

- `CHANGELOG.md`: Generated changelog

---

Example Workflow:

1. Run the script and provide a valid GitHub repository URL.

2. The script will:

- Clone the repository into a temporary folder.

- Generate a changelog file with commit messages grouped by tags.

- Save the `CHANGELOG.md` file in the current directory.

3. The temporary repository folder will be deleted automatically after execution.

---

Contributing:

Contributions are welcome! Feel free to submit issues or pull requests for new features or improvements.
