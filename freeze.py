from py2exe import freeze

freeze(console=['main.py', "fetch_system.py"], options={"includes": ["uvicorn", "fastapi", "psutil", "json", "datetime"]})