try:
    score = int(input("Masukkan nilai score: "))
    
    if score < 0 or score > 100:
        print("Nilai score harus berada di antara 0 dan 100.")
    elif score >= 90:
        print("Selamat! Anda mendapatkan nilai A.")
    elif score >= 80:
        print("Anda mendapatkan nilai B.")
    elif score >= 70:
        print("Anda mendapatkan nilai C.")
    elif score >= 60:
        print("Anda mendapatkan nilai D.")
    else:
        print("Anda mendapatkan nilai E.")
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")