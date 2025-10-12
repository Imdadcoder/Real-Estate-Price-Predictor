# Bangalore Home Prices Prediction

A Flask web application that predicts home prices in Bangalore based on location, square footage, BHK, and bathrooms.

## Project Structure

```
BHP/
├── Client/           # Frontend files (HTML, CSS, JS)
├── Server/           # Backend Flask application
│   ├── artifacts/    # Model files for deployment
│   ├── server.py     # Main Flask app
│   └── util.py       # Utility functions
├── Model/            # Original model files
├── requirements.txt  # Python dependencies
├── render.yaml       # Render deployment config
├── Procfile          # Alternative deployment config
└── start_server.py   # Debug startup script
```

## Deployment on Render

### Method 1: Using render.yaml (Recommended)

1. Push your code to GitHub
2. Connect your GitHub repository to Render
3. Render will automatically detect the `render.yaml` file
4. The service will be deployed with the configuration specified

### Method 2: Manual Configuration

If you prefer manual setup:

1. **Service Type**: Web Service
2. **Environment**: Python 3
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `cd Server && gunicorn --bind 0.0.0.0:$PORT server:app`
5. **Python Version**: 3.11.0

### Important Notes for Deployment

- The model files are located in `Server/artifacts/` directory
- The application automatically detects the correct path for model files
- CORS is enabled for cross-origin requests
- The app runs on the port provided by Render's environment variable
- **Fixed Import Issue**: The server now properly handles imports on Render deployment

### Troubleshooting

If the backend is not accessible:

1. Check the Render logs for any error messages
2. Ensure all model files are present in `Server/artifacts/`
3. Verify that the Python version is compatible
4. Check that all dependencies are installed correctly

### Local Development

To run locally:

```bash
cd Server
python server.py
```

The application will be available at `http://localhost:5000`

## API Endpoints

- `GET /` - Serves the main HTML page
- `GET /get_location_names` - Returns list of available locations
- `POST /predict_home_price` - Predicts home price based on input parameters
