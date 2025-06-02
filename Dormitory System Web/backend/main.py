from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_303_SEE_OTHER
import os

from modules import student  # import your student logic
from modules import room

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

# Show all rooms
@app.get("/rooms", response_class=HTMLResponse)
def room_list(request: Request):
    rooms = room.load_rooms()
    return templates.TemplateResponse("rooms.html", {"request": request, "rooms": rooms})

# Show add form
@app.get("/rooms/add", response_class=HTMLResponse)
def add_room_form(request: Request):
    return templates.TemplateResponse("add_room.html", {"request": request})

# Handle add form
@app.post("/rooms/add")
def add_room(id: str = Form(...), capacity: int = Form(...)):
    room_data = {"id": id, "capacity": capacity, "occupied": 0}
    room.add_room(room_data)
    return RedirectResponse(url="/rooms", status_code=HTTP_303_SEE_OTHER)

# Edit room form
@app.get("/rooms/edit/{room_id}", response_class=HTMLResponse)
def edit_room_form(room_id: str, request: Request):
    r = room.get_room_by_id(room_id)
    if not r:
        return RedirectResponse(url="/rooms", status_code=HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("edit_room.html", {"request": request, "room": r})

# Update room
@app.post("/rooms/edit/{room_id}")
def edit_room(room_id: str, capacity: int = Form(...), occupied: int = Form(...)):
    room.update_room(room_id, {"capacity": capacity, "occupied": occupied})
    return RedirectResponse(url="/rooms", status_code=HTTP_303_SEE_OTHER)

# Delete room
@app.post("/rooms/delete/{room_id}")
def delete_room(room_id: str):
    room.delete_room(room_id)
    return RedirectResponse(url="/rooms", status_code=HTTP_303_SEE_OTHER)
