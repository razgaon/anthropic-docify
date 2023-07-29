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
