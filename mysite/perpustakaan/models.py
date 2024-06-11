from django.db import models

class Penulis(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "1. Penulis"

class Buku(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.OneToOneField(Penulis, on_delete=models.CASCADE)
    tahun_terbit = models.PositiveIntegerField()

    def __str__(self):
        return self.judul
    
    class Meta:
        verbose_name_plural = "2. Buku"

class Peminjam(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "3. Peminjam"

class Peminjaman(models.Model):
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    peminjam = models.ForeignKey(Peminjam, on_delete=models.CASCADE)
    tanggal_pinjam = models.DateField()
    tanggal_kembali = models.DateField()

    def __str__(self):
        return f"{self.buku} dipinjam oleh {self.peminjam}"
    
    class Meta:
        verbose_name_plural = "4. Peminjaman"