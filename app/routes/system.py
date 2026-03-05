from fastapi import APIRouter, Depends
from typing import List
from security.auth import authenticate
from validators.param_validator import validate_params
from services.command_executor import execute_system_command

router = APIRouter()

@router.post("/system/execute")
async def execute_command(
    command_name: str,
    params: List[str] = [],
    user: str = Depends(authenticate)
):
    validate_params(params)

    result = execute_system_command(command_name, params)

    return {
        "command": command_name,
        "user_context": user,
        "exit_code": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip()
    }