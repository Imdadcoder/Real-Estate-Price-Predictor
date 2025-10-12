#!/usr/bin/env python3
"""
Startup script for Bangalore Home Prices prediction service
"""
import os
import sys
from Server.server import app

if __name__ == "__main__":
    print("🏠 Starting Bangalore Home Prices Prediction Service...")
    print(f"Python version: {sys.version}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Files in current directory: {os.listdir('.')}")
    
    # Check if Server directory exists
    if os.path.exists('Server'):
        print("✅ Server directory found")
        print(f"Files in Server directory: {os.listdir('Server')}")
        
        # Check if artifacts exist
        artifacts_path = os.path.join('Server', 'artifacts')
        if os.path.exists(artifacts_path):
            print("✅ Artifacts directory found")
            print(f"Files in artifacts: {os.listdir(artifacts_path)}")
        else:
            print("❌ Artifacts directory not found")
    else:
        print("❌ Server directory not found")
    
    # Get port from environment
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting server on port: {port}")
    
    app.run(host='0.0.0.0', port=port, debug=False)
