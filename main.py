import subprocess
import shutil
import os
import time
from tqdm import tqdm

def run_git_command(command):
    try:
        return subprocess.check_output(command, shell=True, text=True).strip()
    except subprocess.CalledProcessError as e:
        print(f"Error Running command '{command}': {e}")
        return ""

def clone_repo(repo_url, target_dir):
    if os.path.exists(target_dir):
        print(f"Removing existing directory: {target_dir}")
        force_remove_directory(target_dir)
    
    print(f"Cloning repository: {repo_url}")
    try:
        subprocess.run(f"git clone {repo_url} {target_dir}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository: {e}")
        exit(1)

def force_remove_directory(path):
    try:
        # Remove read-only attribute if it exists
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    os.chmod(file_path, 0o777)  # Make sure the file is writable
                    os.remove(file_path)  # Attempt to remove the file
                except PermissionError:
                    pass  # Handle any permission error silently
            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    os.chmod(dir_path, 0o777)  # Make sure the directory is writable
                    os.rmdir(dir_path)  # Remove the directory
                except PermissionError:
                    pass  # Handle any permission error silently
        shutil.rmtree(path, ignore_errors=True)  # Forcefully remove the directory
        print(f"Successfully removed directory: {path}")
    except Exception as e:
        print(f"Error during directory removal: {e}")

def get_tags():
    return run_git_command("git tag").split("\n")

def get_commit_between_tags(tag1, tag2):
    try:
        command = f"git log {tag1}..{tag2} --pretty=format:'%s'"
        return run_git_command(command).split("\n")
    except Exception as e:
        print(f"Error getting commits b/w {tag1} and {tag2}: {e}")
        return []

def generate_changelog(output_directory):
    try:
        tags = get_tags()
        if not tags or len(tags) < 2:
            print("Not enough tags to generate a changelog.")
            return
        
        changelog = []
        
        # Adding tqdm progress bar to track the iteration over tags
        for i in tqdm(range(len(tags) - 1, 0, -1), desc="Processing commits", unit=" tag"):
            commits = get_commit_between_tags(tags[i - 1], tags[i])
            if commits:
                changelog.append(f"## Changes between {tags[i - 1]} and {tags[i]}:\n")
                changelog.extend([f"- {commit}" for commit in commits])
                changelog.append("")  # Add a newline for spacing
        
        changelog_text = "\n".join(changelog)
        changelog_path = os.path.join(output_directory, "CHANGELOG.md")
        with open(changelog_path, "w", encoding="utf-8") as file:
            file.write(changelog_text)
        
        print(f"Changelog generated and saved to {changelog_path}")

    except Exception as e:
        print(f"Error generating changelog: {e}")

def main():
    repo_url = input("Enter the GitHub repository URL: ").strip()
    target_dir = "temp_repo"
    original_dir = os.getcwd()

    clone_repo(repo_url, target_dir)

    os.chdir(target_dir)
    generate_changelog(original_dir)
    os.chdir(original_dir)

    print("Cleaning up temporary files...")
    # Give time to ensure that the file system has released the directory lock
    time.sleep(1)
    force_remove_directory(target_dir)  # Force removal of the directory
    print("Temporary repository folder removed.")

if __name__ == "__main__":
    main()
