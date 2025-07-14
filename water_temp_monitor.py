import streamlit as st
import random
import time
import matplotlib.pyplot as plt

# Simulate reading water temperature
def read_temperature():
    return round(random.uniform(20.0, 60.0), 2)  # °C

# Streamlit config
st.set_page_config(page_title="Water Temperature Monitor", layout="centered")
st.title("💧 Smart Water Temperature Monitor")

threshold = st.slider("Set Temperature Threshold (°C)", min_value=25, max_value=55, value=40)
monitor_time = st.slider("Monitor for how many seconds?", 5, 60, 30)

start = st.button("🚀 Start Monitoring")

if start:
    st.success("Monitoring Started! Live readings below...")
    temp_data = []
    time_data = []

    chart_area = st.empty()
    status_box = st.empty()

    for i in range(monitor_time):
        temp = read_temperature()
        temp_data.append(temp)
        time_data.append(i)

        # Plotting live graph
        fig, ax = plt.subplots()
        ax.plot(time_data, temp_data, color='blue', marker='o')
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Temperature (°C)")
        ax.set_title("Real-time Water Temperature")
        chart_area.pyplot(fig)

        # Show status with color
        if temp > threshold:
            status_box.error(f"🔥 {temp} °C - High Temperature!")
        elif threshold - 3 <= temp <= threshold:
            status_box.warning(f"⚠️ {temp} °C - Approaching Limit")
        else:
            status_box.success(f"✅ {temp} °C - Safe")

        time.sleep(1)

    st.balloons()
    st.info("🎉 Monitoring Complete.")
