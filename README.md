AI-Powered Homework Generator with Analytics

An automated pipeline that converts handwritten class notes (PDF) into structured homework sheets using Google's Gemini AI, with a SQL-backed analytics layer to track content generation trends over time.

Overview

This tool was built to support tutoring workflows: instead of manually reading notes and typing out practice questions, this pipeline reads handwritten PDF notes directly (using Gemini's vision capabilities), generates topic-relevant practice questions, formats them into a clean Word document, and logs every generation into a database for later analysis.

Features
PDF to Image Conversion — Converts multi-page handwritten notes into images for AI processing
Blank Page Filtering — Automatically detects and skips empty/near-blank pages to reduce processing load
AI-Powered Question Generation — Uses Google Gemini (vision-capable model) to read handwritten notes and generate concept-based practice questions
Automatic Topic Detection — Extracts the topic name directly from the notes content
Formatted Word Document Output — Generates a clean, properly formatted .docx file with headings, bold text, and code-block styling
SQLite Database Logging — Every generation run is logged with topic, question count, source file, and timestamp
SQL-Based Analytics — Query the database for total sheets generated, topic-wise breakdown, and recent activity
Data Visualization — Generates a bar chart (via Matplotlib) showing homework sheets generated per topic
Tech Stack
Python — Core language
Google Gemini API — AI-powered content generation with vision support
pdf2image / Poppler — PDF to image conversion
python-docx — Word document generation and formatting
SQLite — Lightweight database for tracking generation history
Matplotlib — Data visualization
NumPy — Image analysis (blank page detection)
How It Works
A handwritten PDF is placed in the project folder
The PDF is converted into page images
Blank/near-empty pages are automatically filtered out
The remaining pages are sent to Gemini AI along with a structured prompt
The AI returns a topic name and a list of practice questions
The response is parsed and formatted into a Word document
A record (topic, question count, timestamp) is logged into a SQLite database
Analytics can be viewed anytime via analytics.py, including a topic-wise bar chart
Setup
Clone the repository
git clone https://github.com/devanshSinghEng/homework-agent.git
cd homework-agent
Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate
Install dependencies
pip install pdfplumber python-docx google-genai python-dotenv pdf2image numpy matplotlib
Install Poppler (required for PDF to image conversion on Windows) and add it to your system PATH
Create a .env file in the project root with your Gemini API key
GEMINI_API_KEY=your_api_key_here
Usage
Place your handwritten notes PDF in the project folder and update PDF_FILENAME in main.py
Run the generator
python main.py
View analytics and generate the topic chart
python analytics.py
Output
homework_output.docx — Formatted homework sheet
homework_tracker.db — SQLite database with generation history
topic_chart.png — Bar chart of homework sheets by topic
Future Improvements
Batch processing of multiple PDFs in a single run
Streamlit-based interactive analytics dashboard
Difficulty-level tagging for generated questions
Author

Devansh Singh