import subprocess


root_partition: str = "/"


def __get_disk_info() -> list:
    result = []
    df = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
    for line in df.stdout:
        split_line = line.decode().split()
        result.append(split_line)
    return result


def __get_disk_type(type: int) -> str:
    for item in __get_disk_info():
        if root_partition is item[5]:
            return item[type][:-1]


def get_full_disk() -> int:
    return float(__get_disk_type(1))


def get_percent_used() -> int:
    return int(__get_disk_type(4))


def get_disk_used() -> int:
    return float(__get_disk_type(2))


def alert(threshold: float) -> bool:
    if get_percent_used() >= threshold:
        return True
    else:
        return False
