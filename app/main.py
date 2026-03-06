from fastapi import FastAPI
from routes.system import router as system_router

app = FastAPI(title="Linux Command Executor API")

app.include_router(system_router)

##EJECUTA EL SIGUIENTE COMANDO DESDE OTRA CONSOLA:
# CADA QUE MODIFICAS CODIGO RECARGAR EL SERVER: uvicorn main:app --reload
##FORMA CORRECTA DE EJECUTAR COMOANDO DESDE OTRA CONSOLA:
#curl -X POST "http://127.0.0.1:8000/system/execute?command_name=uptime"   -u "caballero:4220"   -H "Content-Type: application/json"   -d '[]'
