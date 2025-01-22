import shutil
import os

folders = ["../veri_setleri/orijinal_halleri/train", 
           "../veri_setleri/orijinal_halleri/valid", 
           "../veri_setleri/orijinal_halleri/test"]

combined_folder = "./veri_setleri/birlestirilmis_hali"  # Tüm verilerin birleştirileceği klasör

# Hedef klasör oluştur
os.makedirs(combined_folder, exist_ok=True)

# Mevcut verileri birleştir
for folder in folders:
    for class_name in os.listdir(folder):
        class_path = os.path.join(folder, class_name)
        combined_class_path = os.path.join(combined_folder, class_name)
        os.makedirs(combined_class_path, exist_ok=True)
        for img in os.listdir(class_path):
            shutil.copy(os.path.join(class_path, img), combined_class_path)

print("Veriler başarıyla birleştirildi!")
