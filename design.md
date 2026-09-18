# System Design for Smart Bus Optimization

## 1. Overview
The Smart Bus Optimization system is designed to dynamically adjust bus schedules based on real-time data and demand predictions. The system consists of several interconnected modules that process historical and real-time data, predict demand, optimize schedules, and provide a dashboard for visualization and monitoring.

## 2. Architecture
The system follows a modular architecture with the following core components:
- **Data Ingestion Layer**: Handles loading and cleaning of historical data (ticket sales, passenger counts, GPS logs).
- **Simulation Layer**: Generates real-time bus movements and passenger boarding/alighting events.
- **Prediction Layer**: Forecasts short-term passenger demand for each route and time window.
- **Optimization Layer**: Adjusts bus schedules to prevent bunching, minimize wait times, and maximize occupancy.
- **Dashboard Layer**: Provides a user interface to visualize original vs. optimized schedules, forecasted vs. actual ridership, and alerts.
- **Storage Layer**: Uses CSV files for storing historical data, cleaned data, model outputs, and simulation states.

## 3. Components

### 3.1 Data Ingestion Module
- **Purpose**: Load raw data from multiple sources, clean and preprocess it.
- **Inputs**: Raw CSV files (ticket_sales.csv, passenger_counts.csv, gps_logs.csv).
- **Outputs**: Cleaned dataset (cleaned_data.csv) with features like timestamp, route_id, stop_id, passenger_count, latitude, longitude, etc.
- **Processes**:
  - Timestamp parsing and normalization.
  - Missing value imputation (using forward fill or interpolation for time series).
  - Outlier removal (e.g., GPS coordinates outside city bounds, negative passenger counts).
  - Feature engineering: hour_of_day, day_of_week, is_weekend, etc.

### 3.2 Simulation Module
- **Purpose**: Simulate real-time bus movements and passenger dynamics.
- **Inputs**: Cleaned historical data (for route patterns), optimized schedule (from Optimization Layer), initial bus positions.
- **Outputs**: Real-time feed of bus locations and occupancy (updated every simulation tick).
- **Processes**:
  - For each bus, simulate movement along a predefined route using GPS waypoints.
  - At each stop, simulate boarding and alighting based on predicted demand and current occupancy.
  - Update bus location and occupancy in a shared data structure (e.g., a CSV file or in-memory queue) that the Dashboard can read.

### 3.3 Prediction Module
- **Purpose**: Forecast passenger demand for the next few hours for each route.
- **Inputs**: Cleaned historical data (aggregated by route and hour).
- **Outputs**: Demand forecast (forecasted_demand.csv) with columns: route_id, timestamp, predicted_passenger_count.
- **Processes**:
  - Aggregate historical data by route and hour to create time series.
  - Train a model (e.g., ARIMA, Prophet, or simple exponential smoothing) on historical data.
  - Generate forecasts for the next 3-6 hours.
  - Save forecasts to a file for the Optimization and Simulation layers to consume.

### 3.4 Optimization Module
- **Purpose**: Adjust bus schedules to improve service quality.
- **Inputs**: Current bus locations (from Simulation), demand forecast (from Prediction), current schedule.
- **Outputs**: Optimized schedule (optimized_schedule.csv) with adjusted departure times for each bus at each stop.
- **Processes**:
  - Detect bus bunching: if two buses on the same route are within a threshold distance (or time), hold the following bus.
  - Adjust frequency: increase departures during high predicted demand, decrease during low demand to avoid empty runs.
  - Ensure that adjustments do not cause excessive delays or violate minimum headway constraints.
  - Output a new schedule that the Simulation Layer uses for the next update cycle.

### 3.5 Dashboard Module
- **Purpose**: Visualize system performance and provide alerts.
- **Inputs**: Original schedule, optimized schedule, demand forecast, simulation output (bus locations, occupancy), alerts.
- **Outputs**: Web-based interface showing:
  - Side-by-side comparison of original vs. optimized schedules (Gantt chart or table).
  - Line chart of forecasted vs. actual ridership (actual from simulation).
  - Map view (bonus) showing real-time bus locations with updated ETAs.
  - Alert panel for events like "Route 5 delayed – rescheduling now..." or "Bus bunching detected on Route 10".
- **Technology**: Streamlit for rapid prototyping, with optional use of folium for interactive maps.

### 3.6 Storage Layer
- **Purpose**: Persist data for reproducibility and debugging.
- **Files**:
  - `data/raw/`: Original data sources.
  - `data/cleaned/`: Cleaned datasets.
  - `data/predictions/`: Demand forecast outputs.
  - `data/schedules/`: Original and optimized schedules.
  - `data/simulation/`: Real-time simulation outputs (bus states).
  - `models/`: Saved prediction models (if any).

## 4. Data Flow
1. Historical data is loaded and cleaned by the Data Ingestion module.
2. Cleaned data is used to train the Prediction module, which generates demand forecasts.
3. The Simulation module initializes buses using historical routes and starts simulating movement.
4. At each simulation tick:
   - The Simulation module updates bus locations and occupancy.
   - The Prediction module may be retried periodically (e.g., every hour) with new data.
   - The Optimization module receives current bus states and demand forecasts to produce an adjusted schedule.
   - The Dashboard reads the latest data (schedules, bus locations, forecasts) and updates the display.
5. Alerts are generated based on simulation events (e.g., bunching, delays) and shown in the Dashboard.

## 5. Algorithms and Models
- **Data Cleaning**: Simple imputation and rule-based outlier detection.
- **Demand Prediction**: 
  - Baseline: Historical average for the same hour of day and day of week.
  - Enhanced: ARIMA or exponential smoothing (if time permits).
- **Optimization**: Rule-based heuristic:
  - If time between consecutive buses < threshold → increase headway (hold the latter bus).
  - If predicted demand for next hour > current occupancy + threshold → decrease headway (add a bus if possible).
  - If predicted demand for next hour < current occupancy - threshold → increase headway (remove a bus if possible).
  - Constraints: minimum and maximum headway, maximum delay allowed.

## 6. Interface Specifications
- **Between Modules**: Communication via file system (CSV files) for simplicity in prototype.
  - Example: Prediction module writes to `data/predictions/forecast.csv`; Optimization and Simulation modules read from it.
- **Dashboard**: Reads the latest CSV files to update visualizations every few seconds.

## 7. Deployment (Prototype)
- **Local Deployment**: 
  - Install dependencies from `requirements.txt`.
  - Run data cleaning script to prepare data.
  - Start the simulation and optimization loops (can be run as separate background processes or integrated into the Streamlit app with threading).
  - Launch the dashboard: `streamlit run dashboard.py`.
- **Notes**: For the 36-hour prototype, we aim for a single-container (local machine) setup. All components run on the same machine.

## 8. Future Enhancements
- Replace file-based communication with a message queue (e.g., Redis) or WebSocket for real-time updates.
- Use a lightweight database (SQLite) for better data management.
- Implement more advanced optimization techniques (e.g., reinforcement learning).
- Deploy to cloud for scalability.

---
*This design document outlines the planned architecture for the Smart Bus Optimization prototype. It is subject to change based on evolving requirements and time constraints.*