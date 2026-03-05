import subprocess
from fastapi import HTTPException
from config.settings import ALLOWED_COMMANDS

def execute_system_command(command_name, params):

    if command_name not in ALLOWED_COMMANDS:
        raise HTTPException(status_code=403, detail="Comando no autorizado")

    binary_path = ALLOWED_COMMANDS[command_name]

    try:
        result = subprocess.run(
            [binary_path] + params,
            capture_output=True,
            text=True,
            shell=False,
            timeout=5
        )

        return result

    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="Tiempo límite excedido")