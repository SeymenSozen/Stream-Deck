#Stream Deck 
Profesyonel olmasamda yayıncılık ile uğraştığım için geliştirdiğim bir proje hemde streamdeck fiyatları bukadar arttıktan sonra 🙂;
    eski bir telefonu veya tableti stream deck e dönüştürmenizi sağlar 
    Python/Flask tabanlı bir web uygulamasıdır
    **⚠️ Not:** Bu proje şu anda geliştirme aşamasındadır, yeni özellikler ve optimizasyonlar eklenmeye devam edecektir.Özellikle OBS WebSocket desteği,direkt obs ile bütün bir şekilde çalışmasını sağlayacaktır;
## ✨ Özellikler ( Şuanlık )
-- **12 x5 Kordinat Sistemi** Butonları ekranda sadece sıralamak yerine istediğiniz kordinata (`pos: (satır, sütun)`) koymanızı sağlıyor;
-- **Dinamik Izgara** Python tarafında tanımlanan butonlar,html tarafında otomatik olarak istenen pozisyonlara yerleştirilir
-- **Web Tabanlı Arayüz** Herhangi bir uygulama yüklemeden, tarayıcı üzerinden kontrol imkanı
-- **Kısa Tepkime Süresi** Flask backend sayesinde düşük gecikmeli komut gönderimi

## 🛠️ Kurulum
1. Projeyi bilgisayarınıza indirin:
\`\`\`bash
git clone https://github.com/seymensozen/strem-mdeck.git
\`\`\`
2. Gerekli kütüphaneleri yükleyin:
\`\`\`bash
pip install flask
\`\`\`
3.uygulamayı başlatın:
\`\`\`bash
python app.py
\`\`\`
4.Telefonunuzun tarayıcısından bilgisayarınızın yerel IP adresine gidin: http://bilgisayar-ip-adresiniz:33333

🚀 Yol Haritası (Gelecek Özellikler)
[ ] OBS WebSocket Entegrasyonu: Sahneler arası geçiş ve yayın kontrolü.
[ ] Haptic Feedback: Butona basıldığında telefonda titreşim hissi.
[ ] Profesyonel Animasyonlar: Butona basıldığında gelicek animasyonlar daha keskin hale gelicek.
[ ] Dinamik İkonlar: OBS durumuna göre (Örn: Mikrofon sessizdeyse ikonun değişmesi) gerçek zamanlı güncellemeler.
[ ] Config Dosyası: Butonları kodun içinden değil, bir JSON veya YAML dosyasından yönetme.

# Test
