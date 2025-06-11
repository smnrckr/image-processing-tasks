Tabii! Aşağıda, verdiğin tüm içeriği düzgün markdown biçiminde, tek bir `README.md` dosyası olarak hazırladım. Hem kod blokları hem emoji ve başlıklar uyumlu:

````markdown
# 🧠 Görüntü İşleme Uygulamaları

Bu repoda Python ve NumPy kullanılarak geliştirilen **dört farklı görüntü işleme projesi** bulunmaktadır. Her proje, görüntüler üzerinde farklı analiz ve dönüşüm teknikleri ile çalışır.

---

## 📁 Projeler

| Proje No | Proje Adı                                | Açıklama                                          |
|----------|------------------------------------------|--------------------------------------------------|
| 1        | Para Tanıma ve Toplam Değer Hesaplama    | Görüntüdeki Türk paralarını algılar ve sınıflandırır. |
| 2        | Prewitt ve Roberts ile Kenar Algılama    | Prewitt ve Roberts operatörleriyle kenar tespiti yapar. |
| 3        | 3D Küp Dönüşümleri                       | 3D bir küpe dönüşüm (ölçekleme, döndürme, öteleme) uygular. |
| 4        | Histogram Eşitleme ve Germe              | Kontrast artırımı için iki yöntem uygular.       |

---

## 🛠 Gereksinimler

Tüm projeler için aşağıdaki Python kütüphaneleri gereklidir:

```bash
pip install numpy opencv-python matplotlib Pillow
````

---

## 1️⃣ Para Tanıma ve Toplam Değer Hesaplama (`coin_detector.py`)

### 🎯 Amaç

* Görüntüdeki dairesel şekilli paraları tespit eder.
* Çaplarına göre 5 TL, 1 TL ve 50 kuruş olarak sınıflandırır.
* Toplam para değerini hesaplayıp görselleştirir.

### 📂 Gerekli Dosya

* `paralar.jpg`: Paraların bulunduğu bir görsel (renkli)

### 🚀 Çalıştırma

```bash
python coin_detector.py
```

### 🧪 Kullanılan Teknikler

* CLAHE: Kontrast artırımı
* Canny: Kenar tespiti
* Hough Dönüşümü: Daire tespiti
* NMS (Non-Maximum Suppression): Aynı objeleri filtreleme
* Yarıçap tabanlı sınıflandırma

---

## 2️⃣ Prewitt ve Roberts ile Kenar Algılama (`edge_detection.py`)

### 🎯 Amaç

* Görüntüdeki kenarları tespit etmek için iki klasik kenar tespit filtresi kullanılır.

### 📂 Gerekli Dosya

* `bina.jpg`: Gri seviye (siyah-beyaz) bina görseli

### 🚀 Çalıştırma

```bash
python edge_detection.py
```

### 🧪 Kullanılan Teknikler

* Prewitt Operatörü: 3x3 kenar filtreleri
* Roberts Operatörü: 2x2 kenar filtreleri
* Matplotlib ile görselleştirme

---

## 3️⃣ 3D Küp Dönüşümleri (`transform_3d_cube.py`)

### 🎯 Amaç

* Sanal 3D küpe dönüşüm matrisleri uygulanır.
* Her adımda ayrı bir küp çıktısı görselleştirilir.

### 🚀 Çalıştırma

```bash
python transform_3d_cube.py
```

### 🔧 Uygulanan Dönüşümler

* Ölçekleme
* Dönme (X, Y, Z ekseni)
* Öteleme
* Affine kombinasyonları

### 🎨 Görselleştirme

* Matplotlib’in 3D plot modülü kullanılarak çizilir.

---

## 4️⃣ Histogram Eşitleme ve Germe (`histogram_processing.py`)

### 🎯 Amaç

* Gri seviye bir görüntünün kontrastını artırmak.
* Görüntünün histogramını eşitleme ve genişletme yöntemleriyle düzenlemek.

### 📂 Gerekli Dosya

* `tree.jpeg`: Gri seviye bir doğal manzara ya da ağaç görseli

### 🚀 Çalıştırma

```bash
python histogram_processing.py
```

### 🧪 Uygulanan İşlemler

* Histogram Hesaplama
* Kümülatif Histogram
* Histogram Eşitleme
* Histogram Germe

### 📊 Görselleştirilenler

* Orijinal, eşitlenmiş ve genişletilmiş görüntüler
* Her görüntünün histogramı


## 📎 Proje Yapısı

```
proje-klasoru/
├── coin_detector.py
├── edge_detection.py
├── transform_3d_cube.py
├── histogram_processing.py
├── paralar.jpg
├── bina.jpg
├── tree.jpeg
└── README.md
```
