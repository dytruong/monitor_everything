import subprocess


def __run_cmd(cmd: str) -> str:
    return subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode(
        "utf-8"
    )


def get_host_name() -> str:
    return __run_cmd("hostname")


def get_public_ip() -> str:
    return __run_cmd("curl http://checkip.amazonaws.com")


def get_timestamp() -> str:
    return __run_cmd("date")


def get_region() -> str:
    return __run_cmd(
        "curl -s http://169.254.169.254/latest/dynamic/instance-identity/document | jq -r .region"
    )


def get_account_id() -> str:
    return __run_cmd(
        "curl -s http://169.254.169.254/latest/dynamic/instance-identity/document | jq -r .accountId"
    )
