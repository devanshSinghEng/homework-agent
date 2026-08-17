Samajh gaya — problem ye hai ki README ke andar khud bhi ``` ``` (code blocks) hain, aur maine pura README ek aur bade ``` ``` ke andar wrap kar diya tha — isliye pehla internal ``` aate hi block "toot" gaya lag raha hai.

Fix: neeche jo content hai use **bina kisi outer wrapping ke** seedha copy karo (ye already valid Markdown hai, tumhari `.md` file ke andar jaake sahi render hoga):

---

# AI-Powered Homework Generator with Analytics

An automated pipeline that converts handwritten class notes (PDF) into structured homework sheets using Google's Gemini AI, with a SQL-backed analytics layer to track content generation trends over time.

## Overview

This tool was built to support tutoring workflows: instead of manually reading notes and typing out practice questions, this pipeline reads handwritten PDF notes directly (using Gemini's vision capabilities), generates topic-relevant practice questions, formats them into a clean Word document, and logs every generation into a database for later analysis.

## Features

- **PDF to Image Conversion** — Converts multi-page handwritten notes into images for AI processing
- **Blank Page Filtering** — Automatically detects and skips empty/near-blank pages to reduce processing load
- **AI-Powered Question Generation** — Uses Google Gemini (vision-capable model) to read handwritten notes and generate concept-based practice questions
- **Automatic Topic Detection** — Extracts the topic name directly from the notes content
- **Formatted Word Document Output** — Generates a clean, properly formatted `.docx` file with headings, bold text, and code-block styling
- **SQLite Database Logging** — Every generation run is logged with topic, question count, source file, and timestamp
- **SQL-Based Analytics** — Query the database for total sheets generated, topic-wise breakdown, and recent activity
- **Data Visualization** — Generates a bar chart (via Matplotlib) showing homework sheets generated per topic

## Tech Stack

- **Python** — Core language
- **Google Gemini API** — AI-powered content generation with vision support
- **pdf2image / Poppler** — PDF to image conversion
- **python-docx** — Word document generation and formatting
- **SQLite** — Lightweight database for tracking generation history
- **Matplotlib** — Data visualization
- **NumPy** — Image analysis (blank page detection)

## How It Works

1. A handwritten PDF is placed in the project folder
2. The PDF is converted into page images
3. Blank/near-empty pages are automatically filtered out
4. The remaining pages are sent to Gemini AI along with a structured prompt
5. The AI returns a topic name and a list of practice questions
6. The response is parsed and formatted into a Word document
7. A record (topic, question count, timestamp) is logged into a SQLite database
8. Analytics can be viewed anytime via `analytics.py`, including a topic-wise bar chart

## Setup

1. Clone the repository

       git clone https://github.com/devanshSinghEng/homework-agent.git
       cd homework-agent

2. Create and activate a virtual environment

       python -m venv venv
       .\venv\Scripts\Activate

3. Install dependencies

       pip install pdfplumber python-docx google-genai python-dotenv pdf2image numpy matplotlib

4. Install [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) (required for PDF to image conversion on Windows) and add it to your system PATH

5. Create a `.env` file in the project root with your Gemini API key

       GEMINI_API_KEY=your_api_key_here

## Usage

1. Place your handwritten notes PDF in the project folder and update `PDF_FILENAME` in `main.py`
2. Run the generator

       python main.py

3. View analytics and generate the topic chart

       python analytics.py

## Output

- `homework_output.docx` — Formatted homework sheet
- `homework_tracker.db` — SQLite database with generation history
- `topic_chart.png` — Bar chart of homework sheets by topic

## Future Improvements

- Batch processing of multiple PDFs in a single run
- Streamlit-based interactive analytics dashboard
- Difficulty-level tagging for generated questions

## Author

**Devansh Singh**
