import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from optimizer import optimize_risol

st.set_page_config(page_title="Optimasi Produksi Risol", layout="centered")
st.title("📈 Aplikasi Optimasi Produksi Risol")

st.subheader("Masukkan Data Produksi")

# Input keuntungan
profit_mayo = st.number_input("Keuntungan per Risol Mayo", min_value=1.0, value=5000.0)
profit_sayur = st.number_input("Keuntungan per Risol Sayur", min_value=1.0, value=3000.0)

st.markdown("### Batasan (Kendala Produksi)")

A = []
b = []

col1, col2 = st.columns(2)
with col1:
    a1 = st.number_input("Bahan baku per Risol Mayo", value=2.0)
    a2 = st.number_input("Bahan baku per Risol Sayur", value=1.0)
    b1 = st.number_input("Total bahan baku tersedia", value=100.0)

with col2:
    a3 = st.number_input("Jam kerja per Risol Mayo", value=1.0)
    a4 = st.number_input("Jam kerja per Risol Sayur", value=2.0)
    b2 = st.number_input("Total jam kerja tersedia", value=80.0)

# Matriks kendala
A = [
    [a1, a2],  # Bahan baku
    [a3, a4]   # Jam kerja
]
b = [b1, b2]

if st.button("🔍 Hitung Solusi Optimal"):
    x_opt, y_opt, total_profit = optimize_risol(profit_mayo, profit_sayur, A, b)

    if x_opt is not None:
        st.success(f"Produksi Optimal:\n- Risol Mayo: {x_opt:.2f}\n- Risol Sayur: {y_opt:.2f}")
        st.success(f"Total Keuntungan Maksimal: Rp {total_profit:,.2f}")

        # GRAFIK
        x = np.linspace(0, 100, 400)
        y1 = (b[0] - A[0][0]*x) / A[0][1]
        y2 = (b[1] - A[1][0]*x) / A[1][1]

        plt.figure(figsize=(8, 6))
        plt.plot(x, y1, label="Bahan Baku", color="blue")
        plt.plot(x, y2, label="Jam Kerja", color="green")
        plt.fill_between(x, 0, np.minimum(y1, y2), where=(y1>=0) & (y2>=0), color="skyblue", alpha=0.5)
        plt.plot(x_opt, y_opt, 'ro', label="Solusi Optimal")
        plt.xlabel("Risol Mayo")
        plt.ylabel("Risol Sayur")
        plt.title("Visualisasi Area Feasible dan Solusi Optimal")
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)
    else:
        st.error("Tidak ditemukan solusi yang feasible.")
