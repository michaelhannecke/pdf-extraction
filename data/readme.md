# PDF Exctraction Pipeline

![PDF Extraction and Markup Pipeline](/docu/pdf-extraction.jpeg)


Extract pdf documents into markup language formatted data using docling and openai

## 🚀 Overview

This repository contains a Python-based pipeline designed to:

1.  **Extract Content**: Pull text and potentially structural information from PDF documents using `docling`. *(Future: Scrape content from web pages)*.
2.  **Convert to Markup**: Transform the extracted content into a clean, structured markup format (e.g., Markdown).
3.  **Generate Embeddings**: Create vector representations (embeddings) of the content using state-of-the-art models.
4.  **Store Embeddings**: Save these embeddings locally in a vector database (e.g., ChromaDB, FAISS) for efficient similarity search.

This pipeline is ideal for building knowledge bases, powering semantic search, or providing context for Retrieval-Augmented Generation (RAG) systems.

## ✨ Features

* **PDF Extraction**: Leverages `docling` for robust PDF content extraction.
* **Markup Conversion**: Standardizes extracted content into clean Markdown.
* **Embedding Generation**: Integrates with embedding models (e.g., Sentence Transformers).
* **Local Vector Store**: Uses a local vector database for easy setup and data privacy.
* **Modular Design**: Easily extensible to support more document types (web pages, DOCX) and processing steps.
* **Configurable**: Pipeline steps and models can be configured.

*(Coming Soon)*

* *Web Page Scraping*
* *Support for other document formats*
* *Advanced metadata extraction*
* *Customizable markup schemas*