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
    kcm = st.text_input('Kadar CK-MB(unit/liter)')
with col2:
    gender = st.text_input('Jenis Kelamin (Masukkan 1 jika laki-laki, 0 jika perempuan)')
    pressurehight = st.text_input('Tekanan Darah Sistolik(mmHG)')
    glucose = st.text_input('Gula Darah(mg/dL)')
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
        heart_diagnosis = st.warning('Pasien Terindikasi Penyakit Jantung')
    else:
        heart_diagnosis = st.success('Pasien Tidak Terindikasi Penyakit Jantung')

# Tampilkan ringkasan input yang dimasukkan oleh pengguna
st.subheader('Ringkasan Input:')
st.write('Umur:', age, 'tahun')
gender_text = 'Laki-laki' if gender == '1' else 'Perempuan' if gender == '0' else 'Tidak diketahui'
st.write('Jenis Kelamin:', gender_text)
st.write('Detak Jantung:', impulse, 'bpm')
st.write('Tekanan Darah Sistolik:', pressurehight, 'mmHG')
st.write('Tekanan Darah Diastolik:', pressurelow, 'mmHG')
st.write('Gula Darah:', glucose, 'mg/dL')
st.write('Kadar CK-MB:', kcm, 'unit/Liter darah')
st.write('Troponin:', troponin, 'ng/mL')