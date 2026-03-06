from fastapi import APIRouter, Depends
from security.auth import authenticate
from validators.param_validator import validate_params
from services.command_executor import execute_system_command
from schemas.command import CommandRequest

router = APIRouter()

@router.post("/system/execute")
async def execute_command(
    request: CommandRequest,
    user: str = Depends(authenticate)
):
    
    validate_params(request.params)

    result = execute_system_command(
        request.command,
        request.params
    )

    return {
        "command": request.command,
        "user_context": user,
        "exit_code": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip()
    }