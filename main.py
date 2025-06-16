
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import random

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with Lovable URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy tenant-aware stats
@app.get("/api/dashboard/stats")
def get_dashboard_stats(tenant_id: str = Query(...)):
    return {
        "tickets": random.randint(80, 150),
        "confidence": random.randint(85, 99),
        "readiness": random.randint(70, 100)
    }

@app.get("/api/dashboard/chart-data")
def get_chart_data(tenant_id: str = Query(...)):
    return {
        "labels": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "data": [random.randint(10, 30) for _ in range(5)]
    }

@app.get("/api/tickets/flagged")
def get_flagged_tickets(tenant_id: str = Query(...)):
    return [
        {"title": "Reset failed", "confidence": 87},
        {"title": "Login issue", "confidence": 90},
        {"title": "Email error", "confidence": 89}
    ]

@app.get("/api/arty/status")
def get_arty_status(tenant_id: str = Query(...)):
    return { "readiness": random.randint(70, 100) }

@app.get("/api/analytics/summary")
def get_analytics_summary(tenant_id: str = Query(...)):
    return {
        "weekly_accuracy": "93%",
        "avg_task_time": "14s",
        "most_common_task": "Password Reset"
    }
