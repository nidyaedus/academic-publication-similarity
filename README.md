# 📚 OpenAlex Tabanlı İçerik Bazlı Akademik Yayın Benzerlik Sistemi  
# 📚 OpenAlex-Based Content Similarity System for Academic Publications  

---

## 🇹🇷 Türkçe

### 📌 Proje Hakkında

Bu proje, **Veri Madenciliği dersi kapsamında** gerçekleştirilmiştir.  
Çalışmanın temel amacı, OpenAlex API kullanılarak akademik yayınlar arasında içerik bazlı benzerlik analizi yapabilen bir sistem geliştirmek ve ders kapsamında öğrenilen teorik bilgileri uygulamaya dönüştürmektir.

Bu doğrultuda, veri toplama, veri ön işleme, metin vektörleştirme ve benzerlik hesaplama adımları uçtan uca uygulanmıştır.

---

### 🎯 Projenin Amacı

- OpenAlex API üzerinden veri çekme sürecinin uygulamalı olarak öğrenilmesi  
- Ham metin verisinin temizlenmesi ve dönüştürülmesi süreçlerinin uygulanması  
- TF-IDF ve transformer tabanlı embedding yöntemlerinin karşılaştırmalı olarak incelenmesi  
- Cosine similarity ile içerik tabanlı benzerlik hesaplama yönteminin uygulanması  
- Yakın komşu arama algoritmalarının çalışma mantığının kavranması  
- Basit bir arayüz aracılığıyla sistem çıktılarının gözlemlenmesi  

Bu çalışma ile veri madenciliği dersinde öğrenilen kavramların pratiğe aktarılması hedeflenmiştir.

---

### 🛠 Kullanılan Teknolojiler

- Python  
- OpenAlex API  
- Pandas  
- Scikit-learn  
- Sentence-Transformers (SBERT)  
- FAISS / Nearest Neighbor algoritmaları  
- Streamlit  

---

### 🏗 Sistem Akışı

1. **Veri Toplama**  
   OpenAlex API üzerinden makale verileri elde edilmiş, başlık ve özet alanları analiz için kullanılmıştır.

2. **Veri Ön İşleme**  
   - Küçük harfe dönüştürme  
   - Noktalama işaretlerinin temizlenmesi  
   - Stop-word çıkarımı  
   - Lemmatization işlemi  

3. **Özellik Çıkarma**  
   - TF-IDF yöntemi ile metinlerin sayısal temsili oluşturulmuştur.  
   - Sentence-BERT modeli ile semantik embedding üretimi gerçekleştirilmiştir.  

4. **Benzerlik Hesaplama**  
   - Cosine similarity kullanılarak yayınlar arası benzerlik hesaplanmıştır.  
   - En yakın komşu arama algoritmaları uygulanmıştır.  

5. **Arayüz**  
   Kullanıcı tarafından girilen metin doğrultusunda en benzer yayınlar listelenmiştir.

---

### 📈 Öğrenim Sürecine Katkıları

Bu proje kapsamında:

- Veri madenciliği dersinde öğrenilen teorik bilgiler uygulamaya dönüştürülmüştür.  
- REST API kullanım süreci deneyimlenmiştir.  
- JSON formatındaki verilerin işlenmesi pratiğe aktarılmıştır.  
- Metin madenciliği ve doğal dil işleme adımları uygulamalı olarak gerçekleştirilmiştir.  
- Vektör uzayı modeli ve benzerlik ölçütlerinin çalışma prensibi kavranmıştır.  
- Embedding tabanlı semantik temsil ile geleneksel TF-IDF yaklaşımı karşılaştırılmıştır.  
- Büyük veri üzerinde benzerlik aramalarında indeksleme yöntemlerinin gerekliliği gözlemlenmiştir.  
- Modüler ve sürdürülebilir bir proje yapısı oluşturma pratiği kazanılmıştır.  

---

### 🚀 Akademik ve Teknik Gelişim

Bu çalışma ile:

- İçerik tabanlı öneri sistemlerinin temel mimarisi uygulanmıştır.  
- Teorik kavramlar ile pratik uygulama arasında bağlantı kurulmuştur.  
- NLP alanında teknik uygulama deneyimi kazanılmıştır.  
- Model çıktılarının karşılaştırılması ve yorumlanması becerisi geliştirilmiştir.  

---

### ⚠️ Sınırlamalar

- Sistem büyük ölçekli üretim ortamları için optimize edilmemiştir.  
- Performans değerlendirmesi kapsamlı metrik analizleri içermemektedir.  
- Çalışma öğrenim odaklıdır ve araştırma yayını niteliği taşımamaktadır.  

---

## 🇬🇧 English

### 📌 About the Project

This project was conducted as part of a **Data Mining course**.  
The primary objective is to develop a content-based similarity system for academic publications using the OpenAlex API and to transform theoretical knowledge gained in the course into practical implementation.

The full pipeline, including data collection, preprocessing, vectorization, and similarity computation, was implemented end-to-end.

---

### 🎯 Objectives

- Practically apply data retrieval from the OpenAlex API  
- Implement text preprocessing techniques  
- Compare TF-IDF and transformer-based embedding approaches  
- Compute similarity using cosine similarity  
- Understand nearest neighbor search algorithms  
- Observe system outputs through a simple user interface  

The project aims to operationalize theoretical data mining concepts through implementation.

---

### 🛠 Technologies Used

- Python  
- OpenAlex API  
- Pandas  
- Scikit-learn  
- Sentence-Transformers (SBERT)  
- FAISS / Nearest Neighbor Search  
- Streamlit  

---

### 🏗 System Workflow

1. **Data Collection**  
   Publication data were retrieved from the OpenAlex API. Title and abstract fields were used for analysis.

2. **Preprocessing**  
   - Lowercasing  
   - Punctuation removal  
   - Stop-word removal  
   - Lemmatization  

3. **Feature Extraction**  
   - TF-IDF representation  
   - Sentence-BERT semantic embeddings  

4. **Similarity Computation**  
   - Cosine similarity  
   - Nearest neighbor search  

5. **Interface**  
   The system returns the most similar publications based on user input text.

---

### 📈 Learning Outcomes

Through this project:

- Theoretical knowledge from the Data Mining course was translated into practice.  
- REST API usage was experienced in a real implementation.  
- JSON data processing was applied.  
- Practical text mining and NLP workflows were implemented.  
- The principles of vector space models and similarity metrics were understood.  
- Traditional TF-IDF and semantic embedding approaches were comparatively analyzed.  
- The importance of indexing techniques in similarity search was observed.  

---

### 🚀 Academic and Technical Development

- A complete content-based recommendation pipeline was implemented.  
- The relationship between theoretical concepts and practical applications was established.  
- Technical proficiency in NLP methods was improved.  
- Analytical interpretation of model outputs was developed.  

---

### ⚠️ Limitations

- The system is not optimized for large-scale production environments.  
- Comprehensive performance evaluation metrics are not included.  
- The project is learning-oriented rather than research-focused.  

---

This project was developed for educational purposes.