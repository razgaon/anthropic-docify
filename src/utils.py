import os
import requests

from env_var import GITHUB_ACCESS_TOKEN

LANGCHAIN_BASE = "https://python.langchain.com/docs"

# def get_all_paths(directory):
#     paths = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith(".mdx"):
#                 paths.append(
#                     LANGCHAIN_BASE
#                     + (
#                         os.path.join(root, file)
#                         .replace(directory, "")
#                         .replace(".mdx", "")
#                         .replace("index", "")
#                     )
#                 )

#     return paths

def get_documentation_urls_from_github(owner: str, repo_name: str, repo_doc_root_path: str, current_path:str, rendered_doc_base_url:str):
    paths = []    
    headers = {'Authorization': f'Bearer {GITHUB_ACCESS_TOKEN}'}
    url = f'https://api.github.com/repos/{owner}/{repo_name}/contents/{repo_doc_root_path}/{current_path}'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        files = response.json()
        for file in files:            
            if file['type'] == 'dir':
                # if the file is a directory, get the files in it
                filename = os.path.basename(file['path'])
                paths.extend(get_documentation_urls_from_github(owner, repo_name, repo_doc_root_path, os.path.join(current_path, filename), rendered_doc_base_url))
            elif file['name'].endswith(".mdx"):
                rendered_doc_path = file['path'].replace(repo_doc_root_path, '').replace(".mdx", "").replace("index", "")[1:]
                url = f"{rendered_doc_base_url}/{rendered_doc_path}"
                paths.append(url)
                response = requests.get(url)
                if response.status_code != 200:
                    print(f"Error hitting {url}")
    else:
        print(f"Error getting document {url=} from github. Status Code: {response.status_code}. Response: {response.text}")

    return paths

def save_output(output_path: str, content: str) -> None:
    # Get the parent directory
    parent_dir = os.path.dirname(output_path)
    # Create the parent directory if it doesn't exist
    os.makedirs(parent_dir, exist_ok=True)
    # Now you can safely write to the file
    with open(output_path, 'w') as f:
        f.write(content)