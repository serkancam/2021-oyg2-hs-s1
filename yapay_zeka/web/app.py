from flask import Flask,render_template,request
import csv
import os
from datetime import datetime
app = Flask(__name__)

@app.route("/")#www.serkancam.com gibi bir ana site adı yazıldığında ne görüntülencek
#127.0.0.1:5000
def index():
    #çerez işlemleri
    """
        eğer çerez varsa göster
        yoksa oluştur
    """
    #çerez işlemleri
    deger=request.args.get("isim","")
    return render_template("index.html",ad=deger)

@app.route("/kayit_formu")
def kayit_formu():
    return render_template("kayit_formu.html")

@app.route("/liste")
def liste():
    dosya=""
    sil=request.args.get("sil")
    if sil:
        print(f"{sil} isimli öğrenci silind.")

    try:
        yol = os.path.join(os.getcwd(),"ogrenciler.csv")
        dosya=open(yol,"r",encoding="utf-8")
        okuyucu=csv.reader(dosya)
        ogrenciler=list(okuyucu)
    except:
        pass
    finally:
        if dosya:
            dosya.close()

    return render_template("liste.html",ogrenciler=ogrenciler)

@app.route("/kayit",methods=["POST","GET"])
def kayit():
    ad=request.form.get("ad")
    soyad=request.form.get("soyad")
    program=request.form.get("program")
    yol=os.getcwd()
    if not(ad and soyad and program):
        return render_template("kayit_formu.html",hata="Bilgiler eksik.")
    else:
        dosya=""
        try:
            yol = os.path.join(yol,"ogrenciler.csv")
            dosya=open(yol,"a",encoding="utf-8")
            yazici=csv.writer(dosya)
            yazici.writerow([ad,soyad,program])
        except:
            return render_template("kayit_formu.html",hata="Veri kaydedilemedi."+yol)
        finally:               
            if dosya:
                dosya.close()

        return render_template("kayit_formu.html",hata="Kayıt işlemi tamam")
