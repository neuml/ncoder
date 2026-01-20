#!/bin/bash

# Start opencode in background
nohup /app/opencode serve &

# Start uvicorn server
uvicorn --host 0.0.0.0 txtai.api:app
