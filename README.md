# Brag Document Generator

An AI-powered tool that generates professional brag documents from Excel-based daily scrum reports.

## Features
- Extracts employee information from Excel workbooks
- Generates structured brag documents with:
  - Work accomplishments
  - Learning progress
  - Utilized skills
- Uses LangChain and Gemini API for AI processing

## Setup

1. Create virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure environment variables in `.env`:
   ```
   GEMINI_API_KEY=your_key_here
   GEMINI_API_BASE_URL=gemini_base_url
   ```
   Note: You may use any openai-compatible LLM services.

## Usage

Place your scrum report Excel file in the project directory and run:
```
python main.py
```

## Requirements
- Python 3.x
- openpyxl
- langchain
- pydantic
- python-dotenv
