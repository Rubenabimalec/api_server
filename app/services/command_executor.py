import subprocess
from fastapi import HTTPException
from config.settings import ALLOWED_COMMANDS

def execute_system_command(command, params):

    if command not in ALLOWED_COMMANDS:
        raise HTTPException(
            status_code=403,
            detail="Comando no autorizado"
        )

    binary_path = ALLOWED_COMMANDS[command]

    result = subprocess.run(
        [binary_path] + params,
        capture_output=True,
        text=True,
        shell=False,
        timeout=5
    )

    return result