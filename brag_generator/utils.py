import openpyxl
from typing import List
from pydantic import BaseModel
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from django.conf import settings

class PersonalReflection(BaseModel):
    what_i_am_most_proud_of: List[str]
    areas_i_am_focused_on_for_growth: List[str]

class WorkAccomplishments(BaseModel):
    goals_of_this_quarter: List[str]
    goals_of_this_month: List[str]
    official_project_accomplishments: List[str]
    personal_project_accomplishments: List[str]
    personal_reflection: PersonalReflection

class EmployeeInfo(BaseModel):
    work_accomplishments: WorkAccomplishments
    learning: List[str]
    utilized_skills: List[str]

def extract_employee_data(file_path: str, employee_name: str, month: str, column_name: str = 'What I did  yesterday?') -> List[str]:
    try:
        workbook = openpyxl.load_workbook(file_path, data_only=True)
        found_values = []

        for sheet_name in workbook.sheetnames:
            if month.lower() not in sheet_name.lower():
                continue

            sheet = workbook[sheet_name]
            header = [cell.value for cell in sheet[1]]
            
            try:
                col_index = header.index(column_name)
            except ValueError:
                continue

            for row in sheet.iter_rows(min_row=2, values_only=True):
                if employee_name in row:
                    value = row[col_index]
                    if value:
                        found_values.append(value)

        return found_values
    except Exception as e:
        raise Exception(f"Error extracting data: {str(e)}")

def generate_brag_document(employee_data: List[str]) -> EmployeeInfo:
    agent = create_agent(
        model=ChatOpenAI(
            model="gemini-2.5-flash-lite",
            base_url=settings.GEMINI_API_BASE_URL,
            api_key=settings.GEMINI_API_KEY,
        ),
        tools=[],
        response_format=EmployeeInfo,
        system_prompt="""You are an AI assistant that creates professional brag documents from raw input notes, emphasizing achievements, learning, and utilized skills. Follow these instructions:

**Instructions:**

1. **Input:** Raw notes about accomplishments, learning, and skills.
2. **Output:** A brag document in three sections:
3. **Caution:** Never ever add any irrelavant information which are not in the working history. Genearate only based on the provided employee information.

**Output Structure:**

* **WORK ACCOMPLISHMENTS**
  * Focus on specific results, improvements, or contributions.
  * Use past tense and action-oriented language.
  * Do not add ticket number or Task number (e.g. KR-619 etc.).
  There are five subcategories such as 'Goals of this Quarter', 'Goals of this Month', 'Official Project Accomplishments', 'Personal Project Accomplishments' and 'Personal Reflection'. Inside 'Personal Reflection', there are two subcategories such as 'What I'm Most Proud Of' and 'Areas I'm Focused On For Growth'.



* **LEARNING**

  * Convert raw notes about courses, books, or self-study into bullet points.
  * Highlight practical knowledge, skills gained, or tools explored.

* **UTILIZED SKILLS**

  * Extract technologies, frameworks, or tools used.
  * Present as a comma-separated list or bullets.

**Formatting Rules:**

* Do **not** include a title/header; start with the first section.
* Every line must be a single bullet point.
* Keep language professional, precise, and specific.
* Avoid vague statements; emphasize measurable or observable impact.
* Do not add more than 10 bullet points for any section. Do not add more than 7 skills.
* Use section headers exactly as: `WORK ACCOMPLISHMENTS`, `LEARNING`, `UTILIZED SKILLS`.

    """
    )
    
    response = agent.invoke(
        {"messages": [{"role": "user", "content": f"Here is the employee information: {' '.join(employee_data)}"}]}
    )
    
    return response["structured_response"]
