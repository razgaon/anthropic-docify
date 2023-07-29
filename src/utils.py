import os

def get_all_paths(directory):
    paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mdx"):
                paths.append(
                    "https://python.langchain.com/docs"
                    + (
                        os.path.join(root, file)
                        .replace(directory, "")
                        .replace(".mdx", "")
                        .replace("index", "")
                    )
                )

    return paths
