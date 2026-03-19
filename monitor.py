import hashlib
import json
import os
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from plyer import notification

HASH_FILE = "hashes.json"
LOG_FILE = "logs.txt"
MONITOR_FOLDER = "monitored_folder"


def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:

        while chunk := f.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def load_hashes():

    if os.path.exists(HASH_FILE):

        with open(HASH_FILE, "r") as f:
            return json.load(f)

    return {}


def save_hashes(data):

    with open(HASH_FILE, "w") as f:
        json.dump(data, f, indent=4)


def write_log(message):

    time = datetime.datetime.now()

    with open(LOG_FILE, "a") as f:
        f.write(f"{time} - {message}\n")


def send_alert(message):

    notification.notify(
        title="Security Alert",
        message=message,
        timeout=5
    )


class MonitorHandler(FileSystemEventHandler):

    def on_modified(self, event):

        if event.is_directory:
            return

        file_path = event.src_path

        hashes = load_hashes()

        current_hash = calculate_hash(file_path)

        if file_path in hashes:

            if hashes[file_path] != current_hash:

                message = f"File modified: {file_path}"

                print("WARNING:", message)

                write_log(message)

                send_alert(message)

        hashes[file_path] = current_hash

        save_hashes(hashes)


    def on_created(self, event):

        if event.is_directory:
            return

        file_path = event.src_path

        file_hash = calculate_hash(file_path)

        hashes = load_hashes()

        hashes[file_path] = file_hash

        save_hashes(hashes)

        message = f"New file created: {file_path}"

        print(message)

        write_log(message)


    def on_deleted(self, event):

        file_path = event.src_path

        message = f"File deleted: {file_path}"

        print(message)

        write_log(message)

        send_alert(message)


if __name__ == "__main__":

    print("Starting Smart File Integrity Monitor...")

    event_handler = MonitorHandler()

    observer = Observer()

    observer.schedule(event_handler, MONITOR_FOLDER, recursive=True)

    observer.start()

    try:

        while True:
            pass

    except KeyboardInterrupt:

        observer.stop()

    observer.join()