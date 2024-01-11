from django.shortcuts import render,redirect
from django_hosts.resolvers import reverse
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from core.models import *
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('main')
        
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_auth = authenticate(request=request, email=email, password=password)
        if user_auth:
            login(request, user_auth)
            return redirect('main')
        else:
            return render(request, 'login.html')

@login_required    
def logout_view(request):
    logout(request)
    return redirect(reverse('home', host='static'))





#AUTHENTTICATION NEEDED
@login_required
def home(request,id=None):
    if request.method == 'GET':
        classes = Classes.objects.filter().order_by("-created_at")
        teachers = Teacher.objects.filter().order_by("created_at")
        students = Student.objects.filter().order_by("created_at")

        clas=None
        if id:
            clas = Classes.objects.get(id=id)

        context={
            "classes": classes,
            "teachers": teachers,
            "students":students,
            "clas":clas
        }
        return render(request, 'core/home.html',context)
    
    else:

        if 'create-classes' in request.POST:
            name = request.POST.get('name',None)
            teacher_assignee = request.POST.get('assignee',None)
            students = request.POST.get('students',None)

            class_ = Classes.objects.create(
                name = name,
                teacher = Teacher.objects.get(id=teacher_assignee)
            )

            if students:
                students = students.split(',')
                for student in students:
                    student = Student.objects.get(id=student)
                    class_.student.add(student)
            
            return redirect(reverse("main",host="app",args=[class_.id]))
        
        return redirect(reverse("main",host="app"))
    
@login_required
def class_manage(request,id):
    if request.method=="POST":
        classes = Classes.objects.get(id=id)
        if 'manage-classes' in request.POST:
            name = request.POST.get('name',None)
            teacher_assignee = request.POST.get('assignee',None)
            students = request.POST.get('students',None)
            
            classes.name=name
            classes.teacher = Teacher.objects.get(id=teacher_assignee)

            if students:
                classes.student.clear()
                students = students.split(',')
                for student in students:
                    student = Student.objects.get(id=student)
                    classes.student.add(student)

            classes.save()

        elif 'delete-classes' in request.POST:
            classes.delete()
            return redirect('main')

        elif 'delete-student' in request.POST:
            student_id = request.POST.get('student',None)
            student = Student.objects.get(id=student_id)
            classes.student.remove(student)

        elif 'download-classes' in request.POST:
            template_path = 'core/invoicePDF.html'
            response = HttpResponse(content_type='application/pdf')
            name_pdf = classes.name + ".pdf"
            response['Content-Disposition'] = 'attachment; filename='+name_pdf

            template = get_template(template_path)
            html = template.render({'clas':classes})

            pisa_status = pisa.CreatePDF(html, dest=response)

            return response
        
        return redirect(reverse('main',host='app',args=[str(id)]))
    
    return redirect('main')


@login_required
def student(request):
    if request.method == 'GET':
        page_slug='student'
        classes = Classes.objects.filter().order_by("-created_at")
        teachers = Teacher.objects.filter().order_by("created_at")
        students = Student.objects.filter().order_by("created_at")
        context={"classes": classes,
                "teachers": teachers,
                "students":students,
                'page_slug':page_slug}
        return render(request, 'core/student.html',context)
    else:
        name = request.POST.get('name',None)
        Student.objects.create(
                name = name
            )
        return redirect('student')
    
@login_required
def student_manage(request, id):
    if request.method == 'POST': 
        student = Student.objects.get(id=id)
        if 'delete-student' in request.POST:
            student.delete()
        if 'manage-student' in request.POST:
            name = request.POST.get("name",None)
            student.name = name
            student.save()

    return redirect('student')


@login_required
def teacher(request):
    if request.method == 'GET':
        page_slug='teacher'
        classes = Classes.objects.filter().order_by("-created_at")
        teachers = Teacher.objects.filter().order_by("created_at")
        students = Student.objects.filter().order_by("created_at")
        context={"classes": classes,
                "teachers": teachers,
                "students":students,
                'page_slug':page_slug}
        return render(request, 'core/teacher.html',context)
    else:
        name = request.POST.get('name',None)
        Teacher.objects.create(
                name = name
            )
        return redirect('teacher')
    
@login_required
def teacher_manage(request, id):
    if request.method == 'POST': 
        teacher = Teacher.objects.get(id=id)
        if 'delete-teacher' in request.POST:
            teacher.delete()
        if 'manage-teacher' in request.POST:
            name = request.POST.get("name",None)
            teacher.name = name
            teacher.save()

    return redirect('teacher')



@login_required
def download_classes(request):
    if request.method == 'GET':
        template_path = 'core/invoicePDF.html'
        response = HttpResponse(content_type='application/pdf')
        name_pdf = "ALL Classes" + ".pdf"
        response['Content-Disposition'] = 'attachment; filename='+name_pdf

        # Start the PDF document
        html = "<html><body>"

        classes = Classes.objects.filter().order_by("-created_at")
        for class_ in classes:
            template = get_template(template_path)
            html += template.render({'clas':class_})
            html +="<hr width='100%' size='2' color='black' noshade>"

        # End the PDF document
        html += "</body></html>"

        pisa_status = pisa.CreatePDF(html, dest=response)

        return response
    return redirect('main')