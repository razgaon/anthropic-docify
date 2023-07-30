import argparse
import asyncio
import json

import requests

async def main():
    # Create the parser
    parser = argparse.ArgumentParser()

    # Add the arguments
    parser.add_argument('repository', type=str, help='The repository to fetech issues. E.g. "langchain-ai/langchain"')
    parser.add_argument('github_access_token', type=str, help='Github access token')

    # Parse the command line arguments
    args = parser.parse_args()

    headers = {'Authorization': f'Bearer {args.github_access_token}'}
    repo: str = args.repository
    
    issues_dict = {}
    
    # TODO: See how we want to handle comments
    comments_url = []

    page_number = 1
    while True:
        print(f"Fetching page {page_number}")
        issues_url = f"https://api.github.com/repos/{repo}/issues?per_page=100&page={page_number}"
        response = requests.get(issues_url, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching {issues_url=}: {response.text}")
            exit(1)
        
        issues = response.json()
        if len(issues) == 0:
            break
        
        for issue in issues:
            issues_dict[issue["number"]] = issue
            comments_url.append(issue["comments_url"])

        page_number += 1        

    with open(f"./src/data/{repo.replace('/', '_')}_issues.json", "w") as file:
        json.dump(issues_dict, file)

asyncio.run(main()) 