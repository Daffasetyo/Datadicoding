# Create a Streamlit dashboard file named 'delivery_time_dashboard.py'

streamlit_code = """
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'orders_dataset.csv'  # Adjust this if necessary
orders_df = pd.read_csv(file_path)

# Convert the date columns to datetime format
orders_df['order_purchase_timestamp'] = pd.to_datetime(orders_df['order_purchase_timestamp'])
orders_df['order_delivered_customer_date'] = pd.to_datetime(orders_df['order_delivered_customer_date'])

# Calculate the delivery time in days
orders_df['delivery_time'] = (orders_df['order_delivered_customer_date'] - orders_df['order_purchase_timestamp']).dt.days

# Filter out negative delivery times
orders_df = orders_df[orders_df['delivery_time'] >= 0]

# Calculate average, fastest, and slowest delivery times
average_delivery_time = orders_df['delivery_time'].mean()
fastest_delivery_time = orders_df['delivery_time'].min()
slowest_delivery_time = orders_df['delivery_time'].max()

# Streamlit App
st.title("Delivery Time Analysis Dashboard")

# Display Metrics
st.metric("Average Delivery Time (Days)", f"{average_delivery_time:.2f}")
st.metric("Fastest Delivery Time (Days)", fastest_delivery_time)
st.metric("Slowest Delivery Time (Days)", slowest_delivery_time)

# Bar chart visualization
st.subheader("Delivery Time Comparison")
delivery_time_df = pd.DataFrame({
    'Delivery Time': ['Average', 'Fastest', 'Slowest'],
    'Days': [average_delivery_time, fastest_delivery_time, slowest_delivery_time]
})

# Plot the chart
plt.figure(figsize=(10, 5))
sns.barplot(x='Delivery Time', y='Days', data=delivery_time_df)
plt.title('Waktu Pengiriman')
plt.xlabel('Jenis Waktu Pengiriman')
plt.ylabel('Hari')

# Show the plot in Streamlit
st.pyplot(plt)

# Show the raw data
st.subheader("Raw Data")
st.dataframe(orders_df)
"""

