from git import Repo
import os

def clone_repo(repo_url, destination_folder="temp_repo"):
    if os.path.exists(destination_folder):
        print(f"Deleting existing folder: {destination_folder}")
        import shutil
        shutil.rmtree(destination_folder)
    print(f"Cloning repository: {repo_url}")
    Repo.clone_from(repo_url, destination_folder)
    return destination_folder
