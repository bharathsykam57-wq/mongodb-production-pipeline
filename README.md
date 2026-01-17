# MongoDB Atlas Production Data Pipeline (Python)

## Project Overview

This project demonstrates a production-style MongoDB Atlas integration using Python.
It follows industry best practices such as secure credential management, modular project
structure, and environment isolation.

The pipeline connects to a cloud MongoDB database, inserts records, and retrieves data
using a reusable service architecture.

---

## Tech Stack

- Python 3.10
- MongoDB Atlas (Cloud Database)
- PyMongo
- python-dotenv
- Virtual Environment (venv)

---

## Project Architecture

MongoDB Atlas (Cloud)
        ↓
Environment Variables (.env)
        ↓
MongoDB Client Layer
        ↓
Service Layer (Business Logic)
        ↓
Main Application Runner

---

## Folder Structure
```
mongodb-production-pipeline
├── mongo_production_app
│   ├── app
│   │   └── main.py
│   ├── db
│   │   └── mongo_client.py
│   └── services
│       └── user_service.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

```
---

## Setup Instructions

### 1. Clone Repository

git clone <your-repository-url>
cd mongo_production_app

---

### 2. Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

---

### 3. Install Dependencies

pip install -r requirements.txt

---

### 4. Configure Environment Variables

Create .env file:

cp .env.example .env

Update with your MongoDB Atlas credentials:

MONGO_URI=your_connection_string
DATABASE_NAME=learning_mongodb

---

### 5. Run Application

python -m app.main

---

## Output Example

Starting MongoDB Production App...
Inserted User ID: ...
Fetching all users from database:
...

---

## Key Learning Outcomes

- Cloud database integration using MongoDB Atlas
- Secure credential handling using environment variables
- Production-grade Python project structure
- Modular service architecture
- Real-world data ingestion pipeline design

---

## Future Extensions

- MongoDB to Pandas ML pipeline
- Feature engineering layer
- Machine learning model integration
- Logging and monitoring
- Deployment automation
