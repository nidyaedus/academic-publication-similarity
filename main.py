import streamlit as st 
import requests 
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer   
from sklearn.metrics.pairwise import cosine_similarity        

st.title("📚 Akademik Yayın Öneri Sistemi (OpenAlex) ")

# arama metni, kaç makale çekileceği, kaç makale önerisi gösterileceği ve makale indexi
defaults = {
    "query": "artificial intelligence",
    "per_page": 10,
    "top_n": 5,
    "paper_index": 0
}
#kullanıcı seçimlerini kaydedebilmek için for döngüsü  
#Eğer anahtarlar session state içinde varsa, onları değiştirmez.yoksa onları ilk kez varsayılan değerle oluşturur.
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# Bu fonksiyon, OpenAlex API’sinden belirli bir konuyla ilgili akademik makaleleri çekip her biri için makale kimliği, başlığı ve özetini döndürür.
#Tüm makaleler işlendiğinde sonuçlar bir pandas.DataFrame içinde döndürülür.
def get_openalex_papers(query="machine learning", per_page=10):
    url = f"https://api.openalex.org/works?filter=title.search:{query}&per-page={per_page}"
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    data = r.json()
    results = []
    for work in data.get("results", []):
        title = work.get("title", "")
        abstract = ""
        if work.get("abstract_inverted_index"):
            inverted = work["abstract_inverted_index"]
            positions = [p for v in inverted.values() for p in v]
            if positions:
                max_pos = max(positions)
                abstract_list = [""] * (max_pos + 1)
                for word, pos_list in inverted.items():
                    for pos in pos_list:
                        abstract_list[pos] = word
                abstract = " ".join(abstract_list)
        results.append({"id": work.get("id"), "title": title, "abstract": abstract})
    return pd.DataFrame(results)

#Bu iki fonksiyon, metin benzerliği hesaplayarak seçilen bir makaleye içerik olarak en yakın diğer makaleleri önermek için birlikte çalışır.
# fonksiyonun amacı, Makale başlıkları ve özetlerini kullanarak tüm makaleler arasında TF-IDF tabanlı metin benzerliği hesaplamak. 
def compute_similarity(df):
    texts = (df["title"].fillna("") + " " + df["abstract"].fillna("")).tolist()
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(texts)
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

#Kullanıcının seçtiği bir makaleye (paper_index) en çok benzeyen top_n makaleyi bulmak.
def recommend_papers(df, sim_matrix, paper_index, top_n=5):
    sim_scores = list(enumerate(sim_matrix[paper_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    return [
        {"id": df.iloc[idx]["id"], "title": df.iloc[idx]["title"], "similarity": round(score, 3)}
        for idx, score in sim_scores
    ]

# ---------- Giriş kontrolleri (widgetlarda value/index yok) ----------
query = st.text_input("Araştırma konusu giriniz:", key="query")
per_page = st.slider("Kaç makale çekilsin?", 5, 30, key="per_page")

# Veriyi çek / sakla
if st.button("Verileri Getir", type="primary"):
    df = get_openalex_papers(st.session_state.query, st.session_state.per_page)
    if df.empty:
        st.warning("Hiç sonuç bulunamadı.")
        st.session_state.pop("df", None)
        st.session_state.pop("sim_matrix", None)
    else:
        st.session_state.df = df
        st.session_state.sim_matrix = compute_similarity(df)
        # Güvenli varsayılanlar / kırpma
        st.session_state.paper_index = 0
        # top_n en az 1, en fazla len(df)-1
        max_top = max(1, len(df) - 1)
        st.session_state.top_n = min(st.session_state.get("top_n", 5), max_top)

# ---------- Sonuçlar (state varsa) ----------
if "df" in st.session_state and "sim_matrix" in st.session_state:
    df = st.session_state.df
    sim_matrix = st.session_state.sim_matrix

    st.subheader("Çekilen Makaleler")
    st.dataframe(df[["id", "title"]], use_container_width=True)

    st.markdown("### Öneri Ayarları")

    if len(df) < 2:
        st.info("Yeterli makale yok. Daha fazla sonuç için çekilecek makale sayısını arttırın.")
    else:
        # paper_index'in geçerli aralıkta olduğundan emin ol
        if st.session_state.paper_index >= len(df) or st.session_state.paper_index < 0:
            st.session_state.paper_index = 0

        st.selectbox(
            "Bir makale seçin:",
            range(len(df)),
            format_func=lambda i: df.iloc[i]["title"],
            key="paper_index"
        )

        st.slider(
            "Kaç öneri gösterilsin?",
            1,
            len(df) - 1,
            key="top_n"
        )

        recs = recommend_papers(df, sim_matrix, st.session_state.paper_index, st.session_state.top_n)

        st.subheader("Benzer Makale Önerileri")
        for r in recs:
            st.write(f"- *{r['title']}* (Benzerlik: {r['similarity']})")

            