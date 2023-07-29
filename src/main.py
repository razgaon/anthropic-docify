from crawler import WebpageCrawler, SourceType
import logging
import pandas as pd
import os


def get_all_paths(directory):
    paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mdx'):
                paths.append('https://python.langchain.com/docs' + (os.path.join(root, file).replace(directory, '').replace('.mdx', '')))
    return paths


logging.basicConfig(format='%(asctime)s %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.INFO)

def main():
    directory = '/Users/razgaon/Desktop/langchain/docs/docs_skeleton/docs'  # replace with your directory path
    langchain_paths = get_all_paths(directory)
    count = len(langchain_paths)
    done = 0
    urls = [
        *langchain_paths
    ]
    rows = []

    for url in urls:        
        crawler = WebpageCrawler(source_type=SourceType.Official, use_unstructured=False)
            
        rows.append(crawler.generate_row(url))
        done += 1
        print(f'{done}/{count}')
    
    df = pd.DataFrame(rows)
    df.to_csv('./data.csv', index=False)

if __name__ == "__main__":
    main()