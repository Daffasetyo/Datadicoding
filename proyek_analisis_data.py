import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and Description
st.title("Proyek Analisis Data")
st.markdown("""
### Analisis Data E-Commerce
""")

# Load Datasets
st.header("Load Datasets")

# Load customers dataset
customers_df = pd.read_csv('customers_dataset.csv')
st.subheader("Customers Dataset")
st.write(customers_df.head())

# Load sellers dataset
sellers_df = pd.read_csv('sellers_dataset.csv')
st.subheader("Sellers Dataset")
st.write(sellers_df.head())

# Load products dataset
products_df = pd.read_csv('products_dataset.csv')
st.subheader("Products Dataset")
st.write(products_df.head())

# Load orders dataset
orders_df = pd.read_csv('orders_dataset.csv')
st.subheader("Orders Dataset")
st.write(orders_df.head())

# Visualization: Number of Customers by State
st.header("Visualizations")

st.subheader("Jumlah Pembeli Berdasarkan State")
customer_city = customers_df.groupby(by="customer_state").customer_id.nunique().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(10, 5))
customer_city.plot(kind='bar', ax=ax)
ax.set_title('Jumlah Pembeli Berdasarkan State')
ax.set_xlabel('State')
ax.set_ylabel('Jumlah Pembeli')
ax.set_xticks(range(len(customer_city.index)))
ax.set_xticklabels(customer_city.index, rotation=90)
st.pyplot(fig)

# Display delivery statistics
st.subheader("Statistik Waktu Pengiriman")
average_delivery_time = orders_df['delivery_time_days'].mean()
fastest_delivery_time = orders_df['delivery_time_days'].min()
slowest_delivery_time = orders_df['delivery_time_days'].max()

st.write(f"**Rata-rata Waktu Pengiriman:** {average_delivery_time:.2f} hari")
st.write(f"**Waktu Pengiriman Tercepat:** {fastest_delivery_time} hari")
st.write(f"**Waktu Pengiriman Terlama:** {slowest_delivery_time} hari")
