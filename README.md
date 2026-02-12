# 🧠 AI-Driven System Resource Monitoring Dashboard

## 📌 Project Description

This project is a containerized DevOps monitoring system that collects real-time system metrics from Docker containers and enhances them with an AI-based insight layer.

The system monitors CPU usage, memory usage, and network activity of running containers, stores the metrics using Prometheus, visualizes them using Grafana, and exposes intelligent REST APIs through a Flask backend. A custom frontend dashboard displays live statistics along with AI-generated system health insights.

The goal of this project is to demonstrate how modern DevOps monitoring tools can be integrated with AI logic to convert raw infrastructure data into meaningful, human-readable insights.

---

## 🏗️ System Architecture Overview

The architecture follows a layered monitoring pipeline:

**Docker Containers**  
⬇  
**cAdvisor** – Collects container metrics (CPU, Memory, Network)  
⬇  
**Prometheus** – Scrapes and stores time-series data  
⬇  
**Flask APIs** – Queries Prometheus and adds AI logic  
⬇  
**Frontend Dashboard & Grafana** – Visualizes metrics and insights  

---

### 🔁 Data Flow Explanation

- Docker runs application containers.
- cAdvisor gathers container-level metrics.
- Prometheus pulls metrics from cAdvisor.
- Flask queries Prometheus and processes the data.
- Grafana and the custom frontend display the results.

---

## ⚙️ Technologies Used

### 🐳 Docker & Docker Compose
- Containerized the entire application stack
- Managed multi-service architecture
- Ensured portability and isolation

### 📊 cAdvisor
- Collected real-time container metrics
- Monitored CPU, memory, and network usage
- Exposed metrics for Prometheus scraping

### 📈 Prometheus
- Scraped metrics from cAdvisor and Flask
- Stored time-series data
- Used PromQL queries to retrieve metrics

### 📊 Grafana
- Connected to Prometheus as a data source
- Created professional monitoring dashboards
- Visualized CPU, memory, and network metrics

### 🐍 Flask (Python Backend)
- Built custom REST APIs:
  - `/api/cpu`
  - `/api/memory`
  - `/api/network`
  - `/api/ai`
- Queried Prometheus using HTTP API
- Converted raw metrics into readable values
- Implemented AI rule-based insight logic

### 🎨 Frontend (HTML, CSS, JavaScript, Chart.js)
- Built custom monitoring dashboard
- Fetched live data from Flask APIs
- Displayed:
  - CPU usage
  - Memory usage
  - Network RX/TX
  - AI-generated system insights
- Implemented auto-refresh for real-time updates

---

## 🤖 AI Insight Layer

The AI module analyzes system metrics and provides intelligent recommendations.

**Examples:**
- High CPU → Suggest scaling containers
- High Memory → Warn about possible memory leak
- Normal usage → System stable

Although currently rule-based, the system is designed to be extended with:
- Machine Learning anomaly detection
- Predictive resource usage modeling
- Auto-scaling logic

---

## 🔥 Key Features

- Real-time container monitoring
- Fully Dockerized multi-service architecture
- Prometheus time-series metric storage
- Grafana visualization dashboard
- Custom REST API integration
- AI-based system health interpretation
- Clean and responsive frontend dashboard

---

## 🎯 Project Highlights

- Industry-standard DevOps toolchain
- Clear separation of monitoring, storage, processing, and visualization layers
- Intelligent monitoring beyond simple graphs
- Scalable and extendable architecture
- Resume-ready, production-style project

---

## 🚀 Future Enhancements

- ML-based anomaly detection
- Alert system (Email / Slack integration)
- Kubernetes monitoring support
- Predictive system scaling
- Role-based authentication
