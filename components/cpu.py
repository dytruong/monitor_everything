from dataclasses import dataclass, field
import psutil


def get_cpu_percent() -> float:
    return psutil.cpu_percent(interval=0.4)


def alert_cpu(threshold: float = 80) -> bool:
    if get_cpu_percent() >= threshold:
        return True
    else:
        return False
