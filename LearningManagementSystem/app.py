import openpyxl
from flask import Flask, render_template, request, redirect
from modules.trainee import Trainee
from modules.courses import Course
from modules.trainer import Trainer
from modules.manager import Manager
from modules.enrollment import Enrollment
from modules.attendance import Attendance

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/trainee', methods=['GET', 'POST'])
def create_trainee():
    if request.method == 'POST':
        trainee_id = request.form['trainee_id']
        name = request.form['name']
        course = request.form['course']
        degree = request.form['degree']
        work_experience = request.form['work_experience']
        t = Trainee(trainee_id, name, course, degree, work_experience)
        t.save_to_excel()
        return redirect('/')
    return render_template('create_trainee.html')


@app.route('/trainer', methods=['GET', 'POST'])
def create_trainer():
    if request.method == 'POST':
        trainer_id = request.form['trainer_id']
        full_name = request.form['full_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        t = Trainer(trainer_id, full_name, email, phone_number)
        t.save_to_excel()
        return redirect('/')
    return render_template('create_trainer.html')

@app.route('/course', methods=['GET', 'POST'])
def create_course():
    if request.method == 'POST':
        course_id = request.form['course_id']
        course_description = request.form['course_description']
        c = Course(course_id, course_description)
        c.save_to_excel()
        return redirect('/')
    return render_template('create_course.html')


@app.route('/manager', methods=['GET', 'POST'])
def create_manager():
    if request.method == 'POST':
        trainer_id = request.form['trainer_id']
        full_name = request.form['full_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        managed_courses = request.form['managed_courses']
        m = Manager(trainer_id, full_name, email, phone_number, managed_courses.split(','))
        m.save_to_excel()
        return redirect('/')
    return render_template('create_manager.html')


@app.route('/enrollment', methods=['GET', 'POST'])
def create_enrollment():
    if request.method == 'POST':
        trainee_id = request.form['trainee_id']
        course_id = request.form['course_id']
        e = Enrollment(trainee_id, course_id)
        e.save_to_excel()
        return redirect('/')
    # get trainees and courses for dropdown menu
    trainees = Trainee.get_all_from_excel()
    courses = Course.get_all_from_excel()
    return render_template('create_enrollment.html', trainees=trainees, courses=courses)


@app.route('/attendance', methods=['GET'])
def view_attendance():
    # Get the date for which to display attendance data
    date = request.args.get('date')

    # Load the workbook
    try:
        wb = openpyxl.load_workbook('MasterRecord.xlsx')
    except FileNotFoundError:
        return 'Error: File not found'

    # Get the sheet for the given date
    try:
        ws = wb[date]
    except KeyError:
        return f'Error: No attendance data found for {date}'

    # Extract attendance data from the sheet
    attendance_data = []
    for row in ws.iter_rows(min_row=2):
        trainee_id = row[0].value
        trainee_name = row[1].value
        attendance_status = row[2].value
        attendance_data.append((trainee_id, trainee_name, attendance_status))

    # Render the attendance template with the attendance data
    return render_template('view_attendance.html', date=date, attendance_data=attendance_data)


if __name__ == '__main__':
    app.run(debug=True)
