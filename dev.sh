#!/bin/bash

export ENVIRONMENT="development"
source venv/bin/activate
uvicorn app.main:app --port 8069 --reload