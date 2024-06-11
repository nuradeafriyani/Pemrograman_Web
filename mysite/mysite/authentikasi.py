from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group

def akun_login(request):
    # jika user sudah login maka tidak boleh akses fungsi ini lagi
    if request.user.is_authenticated:
        return redirect('/')

    template_name = "halaman/login.html"
    pesan = ''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            pesan = "Gagal Login"
    context = {
        'pesan' : pesan
    }
    return render(request, template_name, context)

def akun_registrasi(request):
    # jika user sudah login maka tidak boleh akses fungsi ini lagi
    if request.user.is_authenticated:
        return redirect('/')
    
    pesan = ''
    template_name = "halaman/registrasi.html"
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        print(username, first_name, last_name, email, password1, password2)
    
        if password1 == password2:
            check_user = User.objects.filter(username=username)
            if check_user.count() == 0:
                user_simpan = User.objects.create(
                    username = username,
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    # password = password1,
                    is_active = True
                )
                user_simpan.set_password(password1)
                user_simpan.save()

                return redirect('/')
            else:
                pesan = "Username sudah digunakan"

        else:
            pesan ="password tidak sama"

        
    context = {
        'pesan':pesan
    }
    return render(request, template_name, context)

def akun_logout(request):
    logout(request)
    return redirect('/')