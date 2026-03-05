import re
from fastapi import HTTPException

PARAM_VALIDATOR = re.compile(r"^[a-zA-Z0-9\-\. ]*$")

def validate_params(params):
    for param in params:
        if not PARAM_VALIDATOR.match(param):
            raise HTTPException(
                status_code=400,
                detail=f"Parámetro inválido: {param}"
            )