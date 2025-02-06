import os
from dotenv import load_dotenv
import getpass

from langchain_community.agent_toolkits.github.toolkit import GitHubToolkit
from langchain_community.utilities.github import GitHubAPIWrapper

# Load environment variables from .env file
load_dotenv()

# List of required environment variables
required_env_vars = [
    "GITHUB_APP_ID",
    "GITHUB_APP_PRIVATE_KEY",
    "GITHUB_REPOSITORY",
]

# Check and prompt for missing variables
for env_var in required_env_vars:
    if not os.getenv(env_var):
        os.environ[env_var] = getpass.getpass(f"Enter value for {env_var}: ")

# Example: Access the environment variables
app_id = os.getenv("GITHUB_APP_ID")
private_key_path = os.getenv("GITHUB_APP_PRIVATE_KEY")
repository = os.getenv("GITHUB_REPOSITORY")

print(f"App ID: {app_id}")
print(f"Private Key Path: {private_key_path}")
print(f"Repository: {repository}")

github = GitHubAPIWrapper()
toolkit = GitHubToolkit.from_github_api_wrapper(github)

tools = toolkit.get_tools()

for tool in tools:
  print(tool.name)