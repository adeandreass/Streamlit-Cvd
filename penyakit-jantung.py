import pickle
import numpy as np
import streamlit as st


# Load saved model
model = pickle.load(open('penyakit_jantung.sav', 'rb'))

# Web title
st.title('Prediksi Penyakit Jantung')

# Input fields
st.subheader('Masukkan Data Pasien:')
col1, col2= st.columns(2)
with col1:
    age = st.text_input('Umur')
    impulse = st.text_input('Detak Jantung(bpm)')
    pressurelow = st.text_input('Tekanan Darah Diastolik(mmHG)')
    glucose = st.text_input('Gula Darah(mg/dL)')
with col2:
    gender = st.text_input('Jenis Kelamin (Masukkan 1 jika laki-laki, 0 jika perempuan)')
    pressurehight = st.text_input('Tekanan Darah Sistolik(mmHG)')
    kcm = st.text_input('Kadar CK-MB(unit/liter)')
    troponin = st.text_input('Kadar Troponin(ng/mL)')

# Code for prediction
heart_diagnosis = ''

# Make prediction when button is clicked
if st.button('Prediksi Penyakit Jantung'):

    # Convert input values to numeric
    inputs = np.array([[float(age), float(gender), float(impulse), float(pressurehight), float(pressurelow), float(glucose), float(kcm),
                        float(troponin)]])
    
    # Predict using the model
    heart_prediction = model.predict(inputs)

    # Tampilkan hasil prediksi dengan probabilitas
    if heart_prediction[0] == 1:
        heart_diagnosis = 'Pasien Terindikasi Penyakit Jantung'
    else:
        heart_diagnosis = 'Pasien Tidak Terindikasi Penyakit Jantung'

# Tampilkan ringkasan input yang dimasukkan oleh pengguna
st.subheader('Ringkasan Input:')
st.write('Umur:', age, 'tahun')
gender_text = 'Laki-laki' if gender == '1' else 'Perempuan' if gender == '0' else 'Tidak diketahui'
st.write('Jenis Kelamin:', gender_text)
st.write('Detak Jantung:', impulse, 'bpm')
st.write('Tekanan Darah Sistolik:', pressurehight, 'mmHG')
st.write('Tekanan Darah Diastolik:', pressurelow, 'mmHG')
st.write('Kadar CK-MB:', kcm, 'unit/Liter darah')
st.write('Gula Darah:', glucose, 'mg/dL')
st.write('Troponin:', troponin, 'ng/mL')

# Tampilkan hasil diagnosis
if heart_diagnosis:
    st.success(heart_diagnosis)


st.subheader('Tentang Model:')
st.write('Model ini dibuat dengan algoritma C4.5.')

#Classification Report
st.write('Model ini memiliki tingkat akurasi 98%. Seperti yang bisa dilihat dalam classification report:')
image_path = 'class.png'
st.image(image_path, caption='Classification Report', use_column_width=True)

#Pohon Keputusan
st.write('Berikut adalah pohon keputusan dari model ini:')
image_path = 'pohon_keputusan.png'
st.image(image_path, caption='Pohon Keputusan', use_column_width=True)