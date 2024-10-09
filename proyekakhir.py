import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV files
gucheng = pd.read_csv('gucheng_cleaned.csv') 
dingling = pd.read_csv('dingling_cleaned.csv')
dongsi = pd.read_csv('dongsi_cleaned.csv')
guanyuan = pd.read_csv('guanyuan_cleaned.csv')

station = st.sidebar.selectbox('Pilih Stasiun', ['Gucheng', 'Dingling', 'Dongsi', 'Guanyuan'])

if station == 'Gucheng':
    # Visualisasi untuk Gucheng
    st.title('KADAR POLUTAN DI Gucheng')
    st.write('Menurut data yang diambil distasiun gucheng dapat disimpulkan bahwa kualitas udara di kota gucheng sangat tidak sehat.')  # Tambahkan deskripsi
    plt.bar(gucheng['hour'], gucheng['CO'], label='CO', width=0.6)  # Plot CO
    plt.bar(gucheng['hour'], gucheng['O3'], bottom=gucheng['CO'], label='O3', width=0.7)  # Plot O3 di atas CO
    plt.xlabel('jam')
    plt.ylabel('kadar polutan CO dan O3')
    plt.title('KADAR POLUTAN DI Gucheng')
    plt.xticks(gucheng['hour']) 
    plt.legend() 
    plt.tight_layout()
    st.pyplot(plt)

elif station == 'Dingling':
    # Visualisasi untuk Dingling
    st.title('KADAR POLUTAN DI Dingling')
    st.write('Menurut data yang diambil distasiun dingling dapat disimpulkan bahwa kualitas udara di kota dingling sehat.')  # Tambahkan deskripsi
    plt.bar(dingling['hour'], dingling['CO'], label='CO', width=0.6)  # Plot CO
    plt.bar(dingling['hour'], dingling['O3'], bottom=dingling['CO'], label='O3', width=0.7)  # Plot O3 di atas CO
    plt.xlabel('jam')
    plt.ylabel('kadar polutan CO dan O3')
    plt.title('KADAR POLUTAN DI Dingling')
    plt.xticks(dingling['hour']) 
    plt.legend() 
    plt.tight_layout()
    st.pyplot(plt)

elif station == 'Dongsi':
    # Visualisasi untuk Dongsi
    st.title('KADAR POLUTAN DI Dongsi')
    st.write('Menurut data yang diambil distasiun dongsi dapat disimpulkan bahwa kualitas udara di kota kurang sehat.')  # Tambahkan deskripsi
    plt.bar(dongsi['hour'], dongsi['CO'], label='CO', width=0.6)  # Plot CO
    plt.bar(dongsi['hour'], dongsi['O3'], bottom=dongsi['CO'], label='O3', width=0.7)  # Plot O3 di atas CO
    plt.xlabel('jam')
    plt.ylabel('kadar polutan CO dan O3')
    plt.title('KADAR POLUTAN DI Dongsi')
    plt.xticks(dongsi['hour']) 
    plt.legend() 
    plt.tight_layout()
    st.pyplot(plt)

elif station == 'Guanyuan':
    # Visualisasi untuk Guanyuan
    st.title('KADAR POLUTAN DI Guanyuan')
    st.write('Menurut data yang diambil distasiun guanyuan dapat disimpulkan bahwa kualitas udara di kota guanyuan kurang sehat.')  # Tambahkan deskripsi
    plt.bar(guanyuan['hour'], guanyuan['CO'], label='CO', width=0.6)  # Plot CO
    plt.bar(guanyuan['hour'], guanyuan['O3'], bottom=guanyuan['CO'], label='O3', width=0.7)  # Plot O3 di atas CO
    plt.xlabel('jam')
    plt.ylabel('kadar polutan CO dan O3')
    plt.title('KADAR POLUTAN DI Guanyuan')
    plt.xticks(guanyuan['hour']) 
    plt.legend() 
    plt.tight_layout()
    st.pyplot(plt)