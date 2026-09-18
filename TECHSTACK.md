# Technology Stack for Smart Bus Optimization

## Overview
This document outlines the chosen technologies for the Smart Bus Optimization prototype. The stack is selected for ease of development, suitability for data processing and visualization, and ability to meet the 36-hour prototype constraint.

## Backend
- **Language**: Python 3.8+
  - Reason: Extensive libraries for data science, machine learning, and scripting; cross-platform.
- **Data Processing**:
  - pandas: For data cleaning, manipulation, and analysis.
  - numpy: For numerical operations.
- **Machine Learning / Forecasting**:
  - scikit-learn: For simple regression models (if needed).
  - statsmodels: For time-series models like ARIMA (optional).
  - Alternative: Use a simple moving average or exponential smoothing for quick implementation.
- **Simulation**:
  - Custom simulation loop using Python's `time` module to control update frequency.
  - For more complex simulation (optional): `simpy` (discrete event simulation).
- **Data Storage (Prototype)**:
  - CSV files: For simplicity and zero setup. Historical data and simulated outputs stored as CSV.
  - Alternative (if needed): SQLite for lightweight relational storage without a server.
- **Real-time Updates**:
  - Approach: Backend simulation loop updates CSV files or in-memory data structures; frontend polls for updates.
  - For bonus real-time map: Use WebSocket via `flask-socketio` or `fastapi` if using a custom frontend, but we aim to keep it simple.

## Frontend / Dashboard
- **Primary Choice**: Streamlit
  - Reason: Enables rapid creation of data-driven web apps with pure Python. Handles reactivity, layout, and basic interactivity.
  - Features: Easy integration with pandas, matplotlib, and built-in map elements.
  - Alternative: Dash or Flask with HTML/Bootstrap if more customization is needed, but Streamlit fits the timeline.
- **Map View (Bonus)**:
  - Streamlit's `st.map` (using Deck.gl) for simple point maps.
  - For more control: `folium` + `streamlit-folium` to embed interactive Leaflet maps.
- **Charts**:
  - Streamlit's built-in charting (st.line_chart, st.bar_chart) or matplotlib/seaborn for custom plots.
  - Alternative: Plotly for interactive charts (if time permits).

## Development & Deployment
- **Version Control**: Git (already initialized).
- **Dependency Management**: 
  - requirements.txt: To list Python packages.
  - Optional: Use a virtual environment (venv or conda).
- **Deployment**:
  - For local prototype: Run via `streamlit run dashboard.py`.
  - For sharing: Could be deployed to Streamlit Community Cloud, Heroku, or similar (but not required for prototype).

## Chosen Stack Summary
- **Backend**: Python with pandas, numpy, and scikit-learn/statsmodels.
- **Frontend**: Streamlit for dashboard and optional map view.
- **Data**: CSV files for storage.
- **Simulation**: Python loop with time delays to simulate real-time updates.
- **Map (Bonus)**: Streamlit's built-in map or folium.

## Installation
```bash
# Clone the repository
git clone <repository-url>
cd Smart-Bus-Optimization

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Files
- `requirements.txt`: Lists required Python packages.
- `dashboard.py`: Main Streamlit application (to be created).
- Data cleaning, prediction, simulation, and scheduling scripts (to be created).

## Notes
- The stack is intentionally kept simple to focus on core functionality within the time limit.
- If time permits, we can enhance with more advanced models or real-time WebSocket updates.