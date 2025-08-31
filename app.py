import streamlit as st
import plotly.graph_objects as go

# ---------------------------
# Constants
# ---------------------------
g = 9.81  # gravity (m/s²)

# Page setup
st.set_page_config(page_title="Power Pump Calculator", page_icon="💧", layout="centered")

# ---------------------------
# Custom CSS for unique frontend
# ---------------------------
st.markdown(
    """
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
        font-family: 'Poppins', sans-serif;
    }

    /* Title */
    h1 {
        text-align: center;
        color: #56ccf2;
        font-size: 2.2rem;
        margin-bottom: 20px;
    }

    /* Input labels */
    label, .stSlider label {
        color: #fff !important;
        font-weight: 500;
    }

    /* Number input boxes */
    input {
        border-radius: 10px !important;
        padding: 8px !important;
    }

    /* Success box */
    .stSuccess {
        background: rgba(86,204,242,0.15);
        border: 1px solid #56ccf2;
        border-radius: 15px;
        padding: 15px;
        color: #fff;
    }

    /* Expander style */
    .streamlit-expanderHeader {
        font-weight: bold;
        color: #56ccf2 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# App UI
# ---------------------------
st.title("💧 Power Pump Calculator")
st.markdown("This tool calculates **pump shaft power** for mechanical & civil engineering applications.")

# Input layout in two columns
col1, col2 = st.columns(2)

with col1:
    fluid_density = st.number_input("Fluid Density (kg/m³)", value=1000.0, min_value=1.0)
    head = st.number_input("Pump Head (m)", value=20.0, min_value=0.0)

with col2:
    flow_rate_m3h = st.number_input("Flow Rate (m³/h)", value=50.0, min_value=0.0)
    efficiency = st.slider("Pump Efficiency (%)", min_value=1, max_value=100, value=70)

# Convert flow rate from m³/h → m³/s
flow_rate_m3s = flow_rate_m3h / 3600.0
eta = efficiency / 100.0

# ---------------------------
# Calculation & Results
# ---------------------------
if flow_rate_m3s > 0 and head > 0 and eta > 0:
    power_watts = (fluid_density * g * flow_rate_m3s * head) / eta
    power_kw = power_watts / 1000

    st.success(f"🔹 Required Pump Power: **{power_kw:.2f} kW**")

    # Gauge chart for visualization
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=power_kw,
        title={"text": "Pump Power (kW)", "font": {"color": "white"}},
        gauge={
            "axis": {"range": [0, max(1, power_kw * 1.5)], "tickcolor": "white"},
            "bar": {"color": "#56ccf2"},
            "bgcolor": "rgba(255,255,255,0.1)",
            "borderwidth": 2,
            "bordercolor": "white",
            "steps": [
                {"range": [0, power_kw * 0.5], "color": "rgba(86,204,242,0.2)"},
                {"range": [power_kw * 0.5, power_kw], "color": "rgba(86,204,242,0.4)"}
            ],
        }
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font={"color": "white"}
    )
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Please enter valid input values to calculate pump power.")

# ---------------------------
# Formula Info
# ---------------------------
with st.expander("ℹ️ Formula Used"):
    st.latex(r"P = \frac{\rho \cdot g \cdot Q \cdot H}{\eta}")
    st.write("""
    - ρ = Fluid density (kg/m³)  
    - g = Gravity (9.81 m/s²)  
    - Q = Flow rate (m³/s)  
    - H = Pump head (m)  
    - η = Pump efficiency (decimal)  
    """)


