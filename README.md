# 🌦️ Weather Automation Script

A simple Python script that fetches live weather data for any city using the [wttr.in](https://wttr.in) API. Built with Python and Docker, this project demonstrates basic DevOps principles like scripting, containerization, and automation.

## 🚀 Features

- 📍 Dynamic city input via CLI
- 🐳 Dockerized and portable
- 📝 Saves reports to file
- ☁️ Deployable with GitHub Actions

## 🔧 How to Run

```bash
# Without Docker
python scripts/weather_report.py Lagos

# With Docker
docker run --rm weatherbot Lagos
