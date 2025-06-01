from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_303_SEE_OTHER
import os

from modules import student  # import your student logic

app = FastAPI()

# Set up template and static directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Home redirects to /students
@app.get("/", response_class=HTMLResponse)
def home():
    return RedirectResponse(url="/students")

# Student List Page
@app.get("/students", response_class=HTMLResponse)
def student_list(request: Request):
    students = student.load_students()
    return templates.TemplateResponse("students.html", {"request": request, "students": students})

# GET: Show the form
@app.get("/students/add", response_class=HTMLResponse)
def add_student_form(request: Request):
    return templates.TemplateResponse("add_student.html", {"request": request})

# POST: Handle form submission
@app.post("/students/add")
def add_student(
    id: str = Form(...),
    name: str = Form(...),
    room: str = Form(...)
):
    student_data = {"id": id, "name": name, "room": room}
    student.add_student(student_data)
    return RedirectResponse(url="/students", status_code=HTTP_303_SEE_OTHER)
