from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from typing import Callable

class ExerciseEventHandler(FileSystemEventHandler):
    def __init__(self, callback: Callable):
        self.callback = callback

    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".py"):
            self.callback(event.src_path)

class Watcher:
    def __init__(self, path: str, callback: Callable):
        self.path = path
        self.callback = callback
        self.observer = Observer()

    def start(self):
        event_handler = ExerciseEventHandler(self.callback)
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()
