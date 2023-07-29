from crawler import WebpageCrawler
import logging
import pandas as pd
import os

def get_all_paths(directory):
    paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mdx'):
                paths.append('https://python.langchain.com/docs/' + (os.path.join(root, file).replace(directory, '').replace('.mdx', '')))
    return paths


logging.basicConfig(format='%(asctime)s %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.INFO)

def main():
    langchain_docs_dir = '' # Should be replaced with local langchain path
    langchain_paths = get_all_paths(langchain_docs_dir)

    urls = [
        *langchain_paths
    ]
    rows = []

    for url in urls:        
        crawler = WebpageCrawler(use_unstructured=False)
            
        rows.append(crawler.generate_row(url))
    
    df = pd.DataFrame(rows)
    df.to_csv('./data.csv', index=False)


if __name__ == "__main__":
    main()
