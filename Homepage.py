from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="BBPP Lembang",
    page_icon= "-", layout="wide"
)
#st.sidebar.success("Silahkan pilih halaman diatas")
def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json ()
lottie_coding1 =  load_lottieur("https://assets6.lottiefiles.com/packages/lf20_M9p23l.json")
lottie_coding2 = load_lottieur("https://assets9.lottiefiles.com/packages/lf20_UW8DlCRljO.json")
lottie_coding3 = load_lottieur("https://assets7.lottiefiles.com/packages/lf20_ggy3umlc.json")
lottie_coding4 = load_lottieur("https://assets6.lottiefiles.com/private_files/lf30_ysjb4sex.json")

st.title("HOME")

st.snow()
with st.container():
    st.write("------")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Selamat datang di Aplikasi Sistem Informasi Pelatihan Pertanian Terpadu")
        st.write("##")
        st.write( 
            """
            Aplikasi ini dibuat untuk memudahkan dalam berbagai hal antara lain :
            - Sebagai sarana untuk mendaftar peserta pelatihan 
            - Sebagai database bagi peserta pelatihan yang sudah dilatih di BBPP Lembang
            - Sebagai media monitoring bagi para stakeholder dalam kegiatan pelatihan yang diselenggarakan oleh BBPP Lembang
            """ )

    with right_column:
        st.lottie(lottie_coding1, height=500, key="coding" )
        
#Isi Kontainer-----
with st.container():
    st.write("------")
    st.header("TAHAPAN YANG PERLU DIKETAHUI OLEH CALON PESERTA ")
    st.write("##")
    image_column, text_column = st.columns ((1, 2))

    with image_column:
         # insert image 2 ya...--------
         
        st.lottie(lottie_coding2, height=300, key="registrasi" )
        with text_column :
         st.subheader("Biodata Peserta")
         st.write(
            """
            Masukan data diri anda sesuai dengan isian yang telah disediakan jika sebagai :
              1. APARATUR : calon peserta yang berasal dari lembaga/instansi pemerintah baik pusat maupun daerah
              2. NON APARATUR : calon peserta yang berasal dari petani/pelaku usaha di bidang pertanian
              3. PKL : calon peserta yang berasal dari sekolah kejuruan baik swasta maupun negeri
              4. MAGANG : calon peserta yang berasal dari unsur perguruan tinggi/badan/lembaga
            """
            )

        # insert image 3 ya...--------

        st.lottie(lottie_coding3, height=200, key="asrama" )
        with text_column :
         st.subheader("Asrama")
         st.write(
            """
            BBPP Lembang menyediakan asrama bagi peserta pelatihan dengan ketentuan :
              1. Pelatihan yang diselenggarakan lebih dari satu hari 
              2. Pelatihan yang diselenggarakan di dalam kampus BBPP Lembang
              3. Peserta pelatihan diwajibkan mematuhi peraturan di lingkungan BBPP Lembang
              4. Peserta pelatihan diwajibkan menjaga ketertiban dan fasilitas selama di asrama
              5. Untuk keluhan terkait di asrama dapat menghubungi contact center
            """
            )

        
        # insert image 4 ya..--------
        st.lottie(lottie_coding4, height=230, key="magang" )
        with text_column :
         st.subheader("Praktik Kerja Lapangan dan Magang")
         st.write(
            """
            Peserta Praktik Kerja Lapangan (PKL) dan magang wajib mematuhi ketentuan sebagai berikut :
              1. Mengisi daftar registrasi sesuai form yang telah disediakan
              2. Mematuhi peraturan yang telah ditentukan oleh BBPP Lembang melalui pembimbing lapangan masing-masing
              3. Melaksanakan kegiatan praktik kerja lapangan atau magang dari senin sampai hari sabtu 
              4. Jika mengalami kendala selama praktik kerja lapangan atau magang dapat memberitahukan kepada pembimbing yang telah ditentukan
            """
            )
