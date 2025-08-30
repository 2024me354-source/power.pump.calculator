import streamlit as st

# Constants
g = 9.81  # gravity (m/s²)

st.set_page_config(page_title="Power Pump Calculator", page_icon="💧", layout="centered")

st.title("💧 Power Pump Calculator")
st.markdown("This tool calculates **pump shaft power** for mechanical & civil engineering applications.")

# User Inputs
fluid_density = st.number_input("Fluid Density (kg/m³)", value=1000.0, min_value=1.0)
flow_rate_m3h = st.number_input("Flow Rate (m³/h)", value=50.0, min_value=0.0)
head = st.number_input("Pump Head (m)", value=20.0, min_value=0.0)
efficiency = st.slider("Pump Efficiency (%)", min_value=1, max_value=100, value=70)

# Convert flow rate from m³/h → m³/s
flow_rate_m3s = flow_rate_m3h / 3600.0
eta = efficiency / 100.0

# Power Calculation
if flow_rate_m3s > 0 and head > 0 and eta > 0:
    power_watts = (fluid_density * g * flow_rate_m3s * head) / eta
    power_kw = power_watts / 1000
    st.success(f"🔹 Required Pump Power: **{power_kw:.2f} kW**")
else:
    st.warning("Please enter valid input values to calculate pump power.")

# Extra info
with st.expander("ℹ️ Formula Used"):
    st.latex(r"P = \frac{\rho \cdot g \cdot Q \cdot H}{\eta}")
    st.write("""
    - ρ = Fluid density (kg/m³)  
    - g = Gravity (9.81 m/s²)  
    - Q = Flow rate (m³/s)  
    - H = Pump head (m)  
    - η = Pump efficiency (decimal)  
    """)

