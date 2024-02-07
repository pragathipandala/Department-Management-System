from django.shortcuts import render,redirect
from adminapp.models import *
from datetime import datetime
import time
from facultyapp.models import *
from django.contrib import messages
from datetime import date
from django.db.models import Q


# Create your views here.
def faculty_dashboard(request):
    return render(request,'faculty_template/index.html')


def faculty_view_attendance(request):
    view  = Subject_Management.objects.all()
    if request.method == "POST":
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        subjects = request.POST.get('subject')
        date = request.POST.get("attdate")
        # print(subject, 'sjhc')
        view_att = Attendence_Management.objects.filter(Stu_Branch = branch, Stu_Sem = semester, Att_Subject = subjects, Att_Date = date )
        return render(request,'faculty_template/faculty-view-attendance-details.html',{'view_att':view_att, 'sub': subjects, 'v_attend' : view})
    return render(request,'faculty_template/faculty-view-attendance-details.html',{'v_attend' : view})



def faculty_add_attendance(request):
    current_date = time.strftime('%Y-%m-%d')
    subj  = Subject_Management.objects.all()
    if request.method == "POST":
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        subject_name = request.POST.get('subject')
        # print(subject_name, 'djufd', branch, "jygfdb")
        a = Student_Management.objects.filter(Branch_Name = branch, Semester = semester)
        for i in a:
            i.Subject = subject_name
            i.save()
        return render(request,'faculty_template/faculty-add-attendance.html', {'stu_details' : a,'subjj':subj, 'date':current_date,})
    
    return render(request,'faculty_template/faculty-add-attendance.html', {'subjj':subj, 'date':current_date,})
    # return render(request,'faculty_template/faculty-add-attendance.html', {'sub':subj})

def mark_attendance(req):
    students = Student_Management.objects.filter(~Q(Subject = ""))
    attendena = Attendence_Management.objects.all()
    if req.method == 'POST':
        for student in students:
            # for att in attendena:
            #     if att.Att_Date == date.today() and att.Student_Roll == student.
            atten_status = req.POST.get(str(student.Student_ID))
            # print(atten_status, "atten")
            try:
                if Attendence_Management.objects.get(Att_Date = date.today(), Student_Roll=student.Roll_No, Att_Subject=student.Subject, Student_Status='absent').exist():
                    print("already exists")
                    return redirect("faculty_add_attendance")
            except:
                print("yjhfjckxz")

            att = Attendence_Management(Att_Date = date.today(), Att_Subject = student.Subject, Student_Name  = student.Full_Name, Student_Foregin = student, Att_Status = atten_status, Stu_Sem = student.Semester, Stu_Branch = student.Branch_Name, Student_Roll = student.Roll_No, Student_Status = 'present')
            att.save()
            x = Attendence_Management.objects.filter(~Q(Att_Status = 0, Att_Date = date.today()))
            # print(x, 'status student')
            for i in x:
                i.Student_Status = 'absent'
                i.save()
            student.Subject = ""
            student.save()
        return redirect("faculty_add_attendance")
    return render(req, "faculty_template/faculty-add-attendance.html")



def faculty_add_marks(request):
    marks = Subject_Management.objects.all()
    if request.method == "POST":
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        assignment_name = request.POST.get('assignment')
        print(branch)
        a = Student_Management.objects.filter(Branch_Name = branch, Semester = semester)
        print(a,'no of objects')
        assi = Assignment_details(Assignment_Name = assignment_name, Assignment_Branch = branch, Assignment_Sem = semester)
        assi.save()
        for j in a:
            j.Marks_Assignment = assignment_name
            j.Marks = 1
            j.save()
            print(j)
            print(j.Marks_Assignment, "subject name ")
        return render(request,'faculty_template/faculty-add-marks.html', {'marks_details' : a, 'subjj':marks})
    return render(request,'faculty_template/faculty-add-marks.html',{'subjj':marks})


def mark_add(req):
    print("mark_add")
    students = Student_Management.objects.filter(Marks = 1)
    print(students)
    if req.method == 'POST':
        # ab = req.POST.get("name1")
        for student in students:
            atten_status = req.POST.get(str(student.Student_ID))
            print(atten_status, "marks")
            att = Marks_Management(Student_Subject = student.Marks_Assignment, Add_Marks = atten_status, Student_Name  = student.Full_Name, Stu_Foregin = student, Student_Semester = student.Semester, Student_Branch = student.Branch_Name, Student_Roll_No = student.Roll_No)
            att.save()
            student.Marks_Subject = ""
            student.Marks = 0
            student.save()
        return redirect("faculty_add_marks")
        
    return render(req, "faculty_template/faculty-add-marks.html")


def faculty_view_marks(request):
    view_m = Subject_Management.objects.all()
    view_assi = Assignment_details.objects.all()
    if request.method == "POST":
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        subject_name = request.POST.get('subject')
        view = Marks_Management.objects.filter(Student_Branch = branch, Student_Semester = semester, Student_Subject = subject_name)
        for i in view:
            i.Subject = subject_name
            i.save()
        return render(request,'faculty_template/faculty-view-marks.html',{'view_marks' : view, 'v_marks' : view_m, 'subjects' : subject_name, 'v_assi' : view_assi })
    return render(request,'faculty_template/faculty-view-marks.html',{'v_marks' : view_m, 'v_assi' : view_assi})

def faculty_logout(req):
    messages.info(req,"Logged Out")
    return redirect('faculty_login')