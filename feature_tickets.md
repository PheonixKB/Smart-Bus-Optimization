# Feature Tickets

## Phase 1: Data Pipeline Setup

- [ ] **Ticket 1.1**: Set up data directory structure (raw, cleaned, predictions, schedules, simulation)
- [ ] **Ticket 1.2**: Ingest raw CSV files (bmtc_route_stop_sequence.csv, bmtc_routes_clean.csv, bmtc_stops_clean.csv)
- [ ] **Ticket 1.3**: Clean and preprocess data (handle missing values, normalize columns)
- [ ] **Ticket 1.4**: Store cleaned data in data/cleaned/ directory

## Phase 2: Demand Prediction Model

- [ ] **Ticket 2.1**: Explore and visualize historical demand patterns
- [ ] **Ticket 2.2**: Feature engineering (time of day, day of week, route popularity, etc.)
- [ ] **Ticket 2.3**: Train baseline model (Linear Regression) for demand prediction
- [ ] **Ticket 2.4**: Train advanced model (Random Forest / LSTM) for demand prediction
- [ ] **Ticket 2.5**: Evaluate model performance (MAE, RMSE)
- [ ] **Ticket 2.6**: Save trained model to models/ directory
- [ ] **Ticket 2.7**: Create prediction service API endpoint

## Phase 3: Route Optimization Engine

- [ ] **Ticket 3.1**: Define optimization objective (minimize wait time, maximize coverage, reduce operational cost)
- [ ] **Ticket 3.2**: Formulate constraints (bus capacity, route length, time windows)
- [ ] **Ticket 3.3**: Implement optimization algorithm using OR-Tools
- [ ] **Ticket 3.4**: Integrate demand predictions as input to optimizer
- [ ] **Ticket 3.5**: Generate optimized bus schedules
- [ ] **Ticket 3.6**: Save schedules to data/schedules/ directory

## Phase 4: Visualization Dashboard

- [ ] **Ticket 4.1**: Set up FastAPI backend for serving data and predictions
- [ ] **Ticket 4.2**: Create React frontend for dashboard
- [ ] **Ticket 4.3**: Display bus routes and stops on interactive map (Folium/Leaflet)
- [ ] **Ticket 4.4**: Show demand heatmaps and prediction visualizations
- [ ] **Ticket 4.5**: Display optimized schedules and comparisons with current schedules
- [ ] **Ticket 4.6**: Implement user controls for adjusting parameters (time of day, date, etc.)

## Phase 5: Simulation and Evaluation

- [ ] **Ticket 5.1**: Build simulation environment to test optimized schedules
- [ ] **Ticket 5.2**: Define metrics for evaluation (average wait time, bus utilization, coverage)
- [ ] **Ticket 5.3**: Run simulation with current vs optimized schedules
- [ ] **Ticket 5.4**: Generate performance reports
- [ ] **Ticket 5.5**: Store simulation results in data/simulation/ directory

## Phase 6: Deployment and Documentation

- [ ] **Ticket 6.1**: Write Dockerfile for containerization
- [ ] **Ticket 6.2**: Set up CI/CD pipeline (GitHub Actions)
- [ ] **Ticket 6.3**: Create user documentation (how to run, configure, extend)
- [ ] **Ticket 6.4**: Create developer documentation (architecture, APIs, contribution guidelines)
- [ ] **Ticket 6.5**: Deploy to staging environment for testing
- [ ] **Ticket 6.6**: Prepare for production deployment

## Non-Functional Tickets

- [ ] **Ticket NF-1**: Implement logging throughout the application
- [ ] **Ticket NF-2**: Add error handling and recovery mechanisms
- [ ] **Ticket NF-3**: Write unit tests for critical functions (target >80% coverage)
- [ ] **Ticket NF-4**: Write integration tests for API endpoints
- [ ] **Ticket NF-5**: Perform security audit and fix vulnerabilities
- [ ] **Ticket NF-6**: Optimize performance (caching, database indexing, etc.)