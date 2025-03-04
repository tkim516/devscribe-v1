import requests
import base64
from io import BytesIO

def extract_github_file(owner, repo, file_path, token=None):
    """
    Fetches a specific file from a GitHub repository.
    
    Args:
        owner (str): The owner of the repository (e.g., 'octocat').
        repo (str): The name of the repository (e.g., 'Hello-World').
        file_path (str): The path to the file in the repo (e.g., 'src/main.py').
        token (str, optional): GitHub personal access token for authentication.

    Returns:
        BytesIO: File-like object containing the file's content.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        file_data = response.json()
        file_content = base64.b64decode(file_data["content"])  # Decode base64 content
        return BytesIO(file_content)  # Return file-like object

    else:
        raise Exception(f"Error fetching file: {response.status_code} {response.text}")





