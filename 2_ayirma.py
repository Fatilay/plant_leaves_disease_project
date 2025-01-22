import splitfolders 

# Birleştirilen veri kümesinin yolu
input_folder = "./veri_setleri/birlestirilmis_hali"
output_folder = "./veri_setleri/tekrardan_bolunmus_hali"

# %70 Eğitim, %10 Doğrulama, %20 Test oranlarına göre bölme işlemi
splitfolders.ratio(
    input_folder, 
    output=output_folder, 
    seed=42,  # Rastgelelik için sabit bir değer
    ratio=(0.7, 0.1, 0.2)  # Eğitim, Doğrulama, Test oranları
)

print("Veri başarıyla %70-%10-%20 oranlarında bölündü!")