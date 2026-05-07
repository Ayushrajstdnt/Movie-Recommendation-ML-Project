import pickle
import streamlit as st

st.set_page_config(page_title="Movie Recommender System", page_icon="🎬", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@700;900&display=swap');

    .stApp {
        background-color: #0f0f0f;
        background-image: radial-gradient(ellipse at top, #1a1a2e 0%, #0f0f0f 100%);
    }

    * { font-family: 'Montserrat', sans-serif !important; font-weight: 700 !important; }

    h1 {
        color: #e50914 !important;
        font-family: 'Bebas Neue', cursive !important;
        font-size: 4.5rem !important;
        text-align: center !important;
        letter-spacing: 8px !important;
        text-shadow: 0 0 30px rgba(229, 9, 20, 0.6);
        padding: 30px 0 10px 0 !important;
    }

    .subtitle {
        text-align: center;
        color: #888888;
        font-size: 0.85rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 40px;
    }

    .red-divider {
        height: 3px;
        background: linear-gradient(to right, transparent, #e50914, transparent);
        margin: 10px auto 40px auto;
        width: 60%;
        border-radius: 2px;
    }

    label {
        color: #ffffff !important;
        font-size: 0.9rem !important;
        letter-spacing: 3px !important;
        text-transform: uppercase !important;
    }

    .stSelectbox > div > div {
        background-color: #1a1a1a !important;
        color: white !important;
        border: 2px solid #333 !important;
        border-radius: 10px !important;
        font-size: 1rem !important;
        padding: 4px !important;
    }

    .stSelectbox > div > div:hover { border: 2px solid #e50914 !important; }

    .stButton > button {
        background: linear-gradient(135deg, #e50914, #b20710) !important;
        color: white !important;
        font-size: 1rem !important;
        font-weight: 900 !important;
        letter-spacing: 4px !important;
        text-transform: uppercase !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 14px 30px !important;
        width: 100% !important;
        margin-top: 10px !important;
        box-shadow: 0 4px 15px rgba(229, 9, 20, 0.3) !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(229, 9, 20, 0.6) !important;
    }

    .movie-card {
        background: linear-gradient(145deg, #1a1a1a, #111111);
        border-radius: 14px;
        padding: 28px 16px;
        border: 1px solid #222;
        transition: all 0.3s ease;
        text-align: center;
        margin: 8px 0;
    }

    .movie-card:hover {
        border-color: #e50914;
        box-shadow: 0 0 25px rgba(229, 9, 20, 0.3);
        transform: translateY(-4px);
    }

    .movie-number {
        color: #e50914;
        font-size: 2rem;
        font-family: 'Bebas Neue', cursive;
        letter-spacing: 3px;
        margin-bottom: 10px;
    }

    .movie-title {
        color: #ffffff;
        font-size: 0.95rem;
        font-weight: 800;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        line-height: 1.5;
    }

    .rec-label {
        text-align: center;
        color: #888;
        font-size: 0.75rem;
        letter-spacing: 5px;
        text-transform: uppercase;
        margin: 30px 0 10px 0;
    }

    .rec-title {
        text-align: center;
        color: #ffffff;
        font-family: 'Bebas Neue', cursive;
        font-size: 2rem;
        letter-spacing: 6px;
        margin-bottom: 30px;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #111; }
    ::-webkit-scrollbar-thumb { background: #e50914; border-radius: 3px; }
    </style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    movies = pickle.load(open('movie_list.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity


def recommend(movie, movies, similarity):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    names = []
    for i in distances[1:6]:
        names.append(movies.iloc[i[0]].title)
    return names


# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown("<h1>🎬 MOVIE RECOMMENDER</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">Discover Your Next Favourite Film</p>', unsafe_allow_html=True)
st.markdown('<div class="red-divider"></div>', unsafe_allow_html=True)

with st.spinner('Loading...'):
    movies, similarity = load_data()

col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    selected_movie = st.selectbox("🎥  Type or select a movie", movies['title'].values)
    show_btn = st.button('🔍  SHOW RECOMMENDATIONS')

if show_btn:
    names = recommend(selected_movie, movies, similarity)

    st.markdown('<p class="rec-label">Based on your selection</p>', unsafe_allow_html=True)
    st.markdown('<p class="rec-title">RECOMMENDED FOR YOU</p>', unsafe_allow_html=True)

    cols = st.columns(5)
    for i, (col, name) in enumerate(zip(cols, names), 1):
        with col:
            st.markdown(f'''
                <div class="movie-card">
                    <div class="movie-number">#{i}</div>
                    <div class="movie-title">{name}</div>
                </div>
            ''', unsafe_allow_html=True)

    st.markdown('<div class="red-divider" style="margin-top:40px;"></div>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Powered by TMDB • Built with Streamlit</p>', unsafe_allow_html=True)