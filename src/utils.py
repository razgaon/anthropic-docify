import os

LANGCHAIN_BASE = "https://python.langchain.com/docs"

def get_all_paths(directory):
    paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mdx"):
                paths.append(
                    LANGCHAIN_BASE
                    + (
                        os.path.join(root, file)
                        .replace(directory, "")
                        .replace(".mdx", "")
                        .replace("index", "")
                    )
                )

    return paths

def save_output(output_path: str, content: str) -> None:
    # Get the parent directory
    parent_dir = os.path.dirname(output_path)
    # Create the parent directory if it doesn't exist
    os.makedirs(parent_dir, exist_ok=True)
    # Now you can safely write to the file
    with open(output_path, 'w') as f:
        f.write(content)