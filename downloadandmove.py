import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSysytemEventHandler

# Event handler Class
class FileMovementHandler(FileSystemEventHandler):
     def on_created(self, event):
        print(event)


# Initialize event handler class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()


while True:
        time.sleep(2)
        print("running...")