from django.shortcuts import render
from prediction.ml_model import get_trained_model
from students.models import Student
from attendance.models import Attendance
from .models import DropoutPrediction

def predict_dropout(request):
    students = Student.objects.all()
    result = None

    if request.method == "POST" and 'student' in request.POST:
        student_id = request.POST.get('student')
        marks = float(request.POST.get('marks'))
        income = int(request.POST.get('income'))
        distance = float(request.POST.get('distance'))
        health = int(request.POST.get('health'))
        support = int(request.POST.get('support'))

        student = Student.objects.get(id=student_id)

        attendance = Attendance.objects.filter(student=student)
        total = attendance.count()
        present = attendance.filter(present=True).count()
        attendance_percent = (present / total * 100) if total > 0 else 0

        model = get_trained_model()
        data = [[attendance_percent, marks, income, distance, health, support]]
        prediction = model.predict(data)[0]

        result = "HIGH DROPOUT RISK 🚨" if prediction == 1 else "SAFE ✅"

        DropoutPrediction.objects.update_or_create(
            student=student,
            defaults={
                'attendance_percentage': attendance_percent,
                'marks': marks,
                'family_income': income,
                'distance_km': distance,
                'health_issue': bool(health),
                'parent_support': bool(support),
                'prediction': result
            }
        )

    return render(request, 'prediction/predict.html', {
        'students': students,
        'result': result
    })
