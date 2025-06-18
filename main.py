
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import random

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/api/support/cases")
def get_support_cases(tenant_id: str = Query(...)):
    return [
        {
            "title": "Can't log in",
            "status": "Open",
            "submitted_on": "2025-06-15"
        },
        {
            "title": "Add dark mode",
            "status": "In Progress",
            "submitted_on": "2025-06-14"
        },
        {
            "title": "Bug in password reset flow",
            "status": "Resolved",
            "submitted_on": "2025-06-10"
        }
    ]

@app.get("/api/devices/status")
def get_device_status(tenant_id: str = Query(...)):
    return {
        "observers": [
            {"device_name": "Observer-01", "status": "active", "last_seen": "2025-06-18 14:02"},
            {"device_name": "Observer-02", "status": "offline", "last_seen": "2025-06-17 22:45"}
        ],
        "arty_devices": [
            {"device_name": "Arty-Main", "status": "live", "confidence": 94},
            {"device_name": "Arty-Backup", "status": "idle", "confidence": 88}
        ]
    }
