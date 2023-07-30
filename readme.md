# Docify - AI-Enhanced Documentation

## Project Overview

Docify is an AI-Enhanced Documentation project aimed at leveraging the power of LLMs to augment the quality of documentation in open source projects. The central goal of our project is to refine existing documentations, making them more comprehensive, accurate, and user-friendly. This will not only make open source projects more approachable but also foster an environment that encourages contribution.

## Key Features

- **Automated Documentation Enhancement:** The project is designed to automatically review and refine documentation, eliminating manual effort and ensuring consistency.
- **LLM Augmentation:** By leveraging LLMs, our system provides accurate and meaningful enhancements to existing documentation.
- **Wide-Ranging Support:** The project is versatile enough to cater to a broad spectrum of open source projects, making it a universally applicable tool.

## Getting Started

### Prerequisites

To use AI-Enhanced Documentation, please ensure you have met the following prerequisites:

- Python 3.9 or higher installed on your system
- Claude/OpenAI credits

### Installation

1. **Clone the repository:** Use the git command in your terminal

2. **Install the required Python packages:** Use the pip command in your terminal

```bash
pip install -r requirements.txt
```

## Usage

There are a set of keys required to run this repo. Place the keys in an .env file.
- `ANTHROPIC_API_KEY` - powers our chains
- `PINECONE_API_KEY` - for storing the documentation embeddings
- `OPENAI_API_KEY` - for creating embeddings
- `GITHUB_ACCESS_TOKEN` - for scraping open-source repository documentation structure

### Step 1: Crawl the file structure of the github project. You need to set up the repo properties in src/utils

```bash
python src/scripts/crawl.py
```

### Step 2: Run main.py to create documents. They will be written to langdoc/docs. You can also autodeploy with vercel.

```bash
python src/main.py
```

## Contributing

We actively encourage and welcome contributions from the community. Here's how you can contribute:

1. **Fork the Project**
2. **Create your Feature Branch:** `git checkout -b feature/AmazingFeature`
3. **Commit your Changes:** `git commit -m 'Add some AmazingFeature'`
4. **Push to the Branch:** `git push origin feature/AmazingFeature`
5. **Open a Pull Request**
