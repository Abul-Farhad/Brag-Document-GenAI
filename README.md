# Brag Document Generator - Django Full Stack

A full-stack Django web application that generates professional brag documents from Excel-based daily scrum reports using AI.

## Features
- **Web Interface**: User-friendly form to upload Excel files and generate documents
- **AI-Powered Generation**: Uses LangChain and Gemini API for intelligent document creation
- **Document History**: View all previously generated brag documents
- **Export Options**: Download documents as Markdown files
- **Admin Panel**: Manage documents through Django admin interface
- **Structured Output**: Organized sections for:
  - Work accomplishments (quarterly/monthly goals, projects, reflections)
  - Learning progress
  - Utilized skills

## Tech Stack
- **Backend**: Django 5.2
- **AI**: LangChain + Gemini API
- **Database**: SQLite (default)
- **Frontend**: HTML, CSS, JavaScript
- **File Processing**: openpyxl

## Setup

1. Create and activate virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Linux/Mac
   # or
   .venv\Scripts\activate  # On Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables in `.env`:
   ```
   GEMINI_API_KEY=your_key_here
   GEMINI_API_BASE_URL=gemini_base_url
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Start development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application:
   - Main app: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### Generate Brag Document
1. Navigate to the home page
2. Enter employee name
3. Enter month (e.g., "September")
4. Upload Excel file with scrum reports
5. Click "Generate Document"
6. View or export the generated document

### View History
- Click "History" in navigation to see all generated documents
- View details or export any document as Markdown

## Project Structure
```
Brag-Document_GenAI/
├── brag_document_project/     # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── brag_generator/            # Main Django app
│   ├── models.py              # Database models
│   ├── views.py               # View logic
│   ├── urls.py                # URL routing
│   ├── utils.py               # AI and Excel utilities
│   └── admin.py               # Admin configuration
├── templates/                 # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── history.html
│   └── view_document.html
├── static/                    # Static files
│   └── css/
│       └── style.css
├── media/                     # Uploaded files
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables
```

## API Endpoints

- `GET /` - Home page with generation form
- `POST /generate/` - Generate brag document (JSON API)
- `GET /history/` - View document history
- `GET /document/<id>/` - View specific document
- `GET /export/<id>/` - Export document as Markdown

## Requirements
- Python 3.8+
- Django 4.2+
- openpyxl
- langchain
- langchain-openai
- pydantic
- python-dotenv
- django-cors-headers

## Notes
- Excel files must contain sheets named with the month (e.g., "September 2024")
- The column "What I did yesterday?" is used by default for data extraction
- Generated documents are stored in the database with JSON fields
- Uploaded Excel files are saved in the media directory
