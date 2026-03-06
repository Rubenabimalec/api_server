import pam
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    p = pam.pam()

    if p.authenticate(credentials.username, credentials.password):
        return credentials.username

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Usuario o contraseña inválidos",
        headers={"WWW-Authenticate": "Basic"},
    )