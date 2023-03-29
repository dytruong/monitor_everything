import datetime
import subprocess


log_dir: str = "/var/log/g4b-monitor/"
log_file: str = "monitor_disk.log"
log_path: str = f"{log_dir}/{log_file}"


def set_up(self) -> None:
    folder_path = Path(self.log_dir)
    folder_path.mkdir(parents=True, exist_ok=True)
    file_path = Path(self.log_path)
    file_path.touch(exist_ok=True)


@staticmethod
def get_log(log_info) -> None:
    date_time = datetime.datetime.utcnow().strftime("%m/%d/%Y-%H:%M:%S")
    subprocess.run(
        f"echo '[{date_time} UTC +0] - {log_info}' >> {Log.log_path}", shell=True
    )
