from django.db import models


class Profil(models.Model):
    ism=models.CharField(max_length=200)
    yosh=models.PositiveSmallIntegerField()
    sana=models.DateField(auto_now=True)

    def __str__(self):
        return self.ism

class Kurs(models.Model):
    nom=models.CharField(max_length=255)
    daraja=models.CharField(max_length=50)
    ustoz=models.CharField(max_length=255)
    narx=models.PositiveSmallIntegerField()
    chegirma=models.CharField(max_length=20,default=0)

    def __str__(self):
        return self.nom

class Izoh(models.Model):
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    kurs=models.ForeignKey(Kurs, on_delete=models.CASCADE)
    matn=models.CharField(max_length=255)
    sana=models.DateField(auto_now=True)
    baho=models.CharField(max_length=400)
    def __str__(self):
        return f"{self.profil}:{self.kurs}"


class Tanlangan(models.Model):
    kurs=models.ForeignKey(Kurs,on_delete=models.CASCADE)
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.profil}:{self.kurs}"

class Xarid(models.Model):
    kurs=models.ForeignKey(Kurs, on_delete=models.CASCADE)
    progil=models.ForeignKey(Profil, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.progil}:{self.kurs}"


