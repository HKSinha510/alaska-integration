import logging
import sys
import uvicorn
from uvicorn import Config, Server
from main import app  # Replace with the import for your FastAPI app instance

# Create a custom logging handler that writes to the log file
class LogToFileHandler(logging.StreamHandler):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def emit(self, record):
        with open(self.filename, 'a') as file:
            file.write(self.format(record) + '\n')

# Configure custom logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

# Create a custom logger and add the file handler
logger = logging.getLogger('custom_logger')
log_file_handler = LogToFileHandler('my_app.log')
logger.addHandler(log_file_handler)

# Create a Uvicorn configuration
config = Config(
    app=app,
    host="0.0.0.0",
    port=8801,
)

# Capture Uvicorn's logs in the custom logger
config.logger = logger

# Create a Uvicorn server with the custom logger
server = Server(config=config)

if __name__ == "__main__":
    server.run()
