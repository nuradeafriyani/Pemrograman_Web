from django.contrib import admin
from .models import Penulis, Buku, Peminjam, Peminjaman

class BukuAdmin(admin.ModelAdmin):
    list_display = ('judul', 'penulis', 'tahun_terbit')

class PenulisAdmin(admin.ModelAdmin):
    list_display = ('nama', 'alamat')

class PeminjamAdmin(admin.ModelAdmin):
    list_display = ('nama', 'alamat')

class PeminjamanAdmin(admin.ModelAdmin):
    list_display = ('buku', 'peminjam', 'tanggal_pinjam', 'tanggal_kembali')

admin.site.register(Buku, BukuAdmin)
admin.site.register(Penulis, PenulisAdmin)
admin.site.register(Peminjam, PeminjamAdmin)
admin.site.register(Peminjaman, PeminjamanAdmin)