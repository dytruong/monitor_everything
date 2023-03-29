import psutil


def get_memory_percent() -> float:
    return psutil.virtual_memory().percent


def alert_memory(threshold: float = 80) -> bool:
    if get_memory_percent() >= threshold:
        return True
    else:
        return False
