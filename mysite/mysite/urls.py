from django.contrib import admin
from django.urls import path, include

# Importing views dari aplikasi mysite
from mysite.views import about, contact, home, detail_artikel
from mysite.authentikasi import akun_login, akun_registrasi, akun_logout

# Definisikan pola URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('artikel/<slug:slug>/', detail_artikel, name="detail_artikel"),
    
    # Include URLs dari aplikasi berita untuk dashboard
    path('dashboard/', include('berita.urls')),
    
    # Jalur otentikasi
    path('authentikasi/login/', akun_login, name="akun_login"),
    path('authentikasi/registrasi/', akun_registrasi, name="akun_registrasi"),
    path('authentikasi/logout/', akun_logout, name="akun_logout"),
]

# Menampilkan file media selama pengembangan
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
