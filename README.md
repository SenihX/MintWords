# MintWords
 MintWords: MintWords is a powerful tool that allows users to create personalized and effective wordlists. It allows users to create custom wordlists that fit their needs, especially for use in cybersecurity, password testing, and security testing.
 Haklısınız, dediğiniz gibi kodları **normal metin** formatında yazacağım. İşte güncellenmiş hali: 

---

# MintWords Kurulum ve Çalıştırma Rehberi

Bu rehber, MintWords projesini Termux ve Kali Linux üzerinde nasıl kurup çalıştırabileceğinizi adım adım açıklar.

## Termux Üzerinde MintWords Nasıl Çalıştırılır?

1. Termux’u güncelleyin ve gerekli paketleri kurun:  
pkg update && pkg upgrade  
pkg install git python  

2. Depoyu klonlayın:  
git clone https://github.com/SenihX/MintWords.git  

3. Proje dizini içine girin:  
cd MintWords  

4. Gerekli Python kütüphanelerini yükleyin:  
pip install -r requirements.txt  

5. MintWords’u çalıştırın:  
python mintwords.py  

---

## Kali Linux Üzerinde MintWords Nasıl Çalıştırılır?

1. Sistem paketlerini güncelleyin ve gerekli bağımlılıkları yükleyin:  
sudo apt update && sudo apt upgrade  
sudo apt install git python3 python3-pip  

2. Depoyu klonlayın:  
git clone https://github.com/SenihX/MintWords.git  

3. Proje dizinine gidin:  
cd MintWords  

4. Gerekli Python kütüphanelerini yükleyin:  
pip3 install -r requirements.txt  

5. MintWords’u çalıştırın:  
python3 mintwords.py  

---

Umarım bu haliyle açıklamalar daha net olmuştur! 😊
