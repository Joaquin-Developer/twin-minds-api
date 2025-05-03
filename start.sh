#!/bin/bash

export ENVIRONMENT="production"
source venv/bin/activate
uvicorn app.main:app --port 8069