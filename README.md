# Summarizing - Text Summarization with Pegasus

> Automatic text summarization tool using Google's Pegasus model

## Overview

A Python tool that automatically summarizes long texts using Google's Pegasus-XSUM transformer model. Handles long documents by splitting them into chunks for effective summarization.

## Key Features

- **Automatic Summarization**: Pegasus-XSUM transformer model
- **Long Document Support**: Text chunking for lengthy documents
- **GPU Acceleration**: CUDA support for faster processing
- **File I/O**: Read and write text files

## Tech Stack

- Python 3.8+
- PyTorch
- Hugging Face Transformers
- google/pegasus-xsum model

## Quick Start

```bash
pip install torch transformers
python summarize.py
```

## Usage

```python
from summarize import summarize_korean_text, read_file, split_text

text = read_file("input.txt")
chunks = split_text(text, chunk_size=1000)
summaries = [summarize_korean_text(chunk, model, tokenizer) for chunk in chunks]
full_summary = " ".join(summaries)
```

## Project Structure

```
summarizing/
├── summarize.py          # Main summarization script
├── marco_job_abroad.txt  # Sample input text
└── practice/             # Practice and test code
```