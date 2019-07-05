from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password, check_password
from miscFiles.functions import generate_string, link_send
from front_panel.models import RoleDetails, UserRole
from front_panel.forms import RoleDetailsForm


def registration(request):
    if request.method == "POST":
        form = RoleDetailsForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.role_id = request.POST['role']
            f.name = request.POST['name']
            f.email = request.POST['email']
            f.gender = request.POST['gender']
            f.active = 0
            string = generate_string()
            password = string
            link = make_password(password)
            link = link.replace("+", "")
            f.password = link
            f.verify_link = link
            f.save()
            f_link = "127.0.0.1:8000/verify_link/?link=" + link
            request.session['email'] = f.email
            link_send(f.email, f_link, password)
            return render(request, "index.html", {'confirm': True})
    return render(request, 'index.html')


def login(request):
    data = UserRole.objects.all()
    if request.method == "POST":
        get_email = request.POST['email']
        get_password = request.POST['password']

        data = RoleDetails.objects.get(email=get_email)
        db_password = data.password
        db_active = data.active
        db_verify_link = data.verify_link
        role = data.role_id
        if check_password(get_password, db_password):

            if db_active == 0 and db_verify_link != "":
                return HttpResponse("Please verify your email")
            elif db_active == 1:
                request.session['email'] = get_email
                request.session['name'] = data.name
                request.session['role'] = role
                if role == 1:
                    return render(request, "adminindex.html")
                elif role == 2:
                    pass
        else:
            return HttpResponse("Password not valid")
    return render(request, "index.html", {'role': data})


def verify_link(request):
    get_link = request.GET['link']
    session_mail = request.session['email']
    data = RoleDetails.objects.get(email=session_mail)
    db_verify = data.verify_link
    if get_link == db_verify:
        update = RoleDetails(email=session_mail, active=1, verify_link="")
        update.save(update_fields=['active', 'verify_link'])
        return render(request, "index.html")
