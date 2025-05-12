import logging
import os
from datetime import datetime

# Step 1: Set up a logs directory (only once)
logs_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_dir, exist_ok=True)

# Step 2: Create a time-stamped log file inside the logs directory
log_file = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
log_file_path = os.path.join(logs_dir, log_file)

# Step 3: Set up logging config
logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Step 4: Test logging
if __name__ == '__main__':
    logging.info('Logging has started !!!')
