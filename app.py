import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Coffee Roasting Simulator", layout="wide")

# Header
st.title("☕ Coffee Roasting Simulator")
st.image("assets/coffee.png", width=150)

# Sidebar: Input
st.sidebar.header("Roasting Controls")
bean_type = st.sidebar.selectbox("Select Coffee Bean Type", ["Arabica", "Robusta", "Liberica"])
temp = st.sidebar.slider("Roasting Temperature (°C)", min_value=150, max_value=250, value=200, step=5)
simulate_btn = st.sidebar.button("Start Roasting Simulation")

# Main Area
st.subheader(f"Roasting Profile for {bean_type} Beans at {temp}°C")

# Event-driven simulation
if simulate_btn:
    st.success("Simulation Started...")
    roasting_phases = ["Drying", "Browning", "Development"]
    phase_times = [0.4, 0.35, 0.25]  # normalized duration

    total_time = 60  # seconds
    phase_durations = [int(p * total_time) for p in phase_times]
    time_values = []
    temp_values = []

    progress_bar = st.progress(0)
    chart_area = st.empty()
    phase_display = st.empty()

    for phase, duration in zip(roasting_phases, phase_durations):
        phase_display.markdown(f"### 🔥 Current Phase: {phase}")
        for t in range(duration):
            elapsed = sum(phase_durations[:roasting_phases.index(phase)]) + t
            temp_point = temp + np.random.normal(0, 1)  # simulate variation
            time_values.append(elapsed)
            temp_values.append(temp_point)

            # Plotting real-time
            fig, ax = plt.subplots()
            ax.plot(time_values, temp_values, color="brown")
            ax.set_xlabel("Time (s)")
            ax.set_ylabel("Temperature (°C)")
            ax.set_title("Roasting Curve")
            chart_area.pyplot(fig)

            progress = int((elapsed / total_time) * 100)
            progress_bar.progress(min(progress, 100))
            time.sleep(0.1)

    phase_display.markdown("### ✅ Roasting Complete! Enjoy your coffee ☕")

else:
    st.info("Adjust the controls on the sidebar and click 'Start Roasting Simulation' to begin.")

