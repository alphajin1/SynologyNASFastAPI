#!/usr/bin/env bash
nohup uvicorn main:app --reload --host=0.0.0.0 --port=9010 &