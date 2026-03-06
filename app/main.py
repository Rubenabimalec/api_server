from fastapi import FastAPI
from routes.system import router as system_router

app = FastAPI()

app.include_router(system_router)

##EJECUTA EL SIGUIENTE COMANDO DESDE OTRA CONSOLA:
# CADA QUE MODIFICAS CODIGO RECARGAR EL SERVER: uvicorn main:app --reload
##FORMA CORRECTA DE EJECUTAR COMOANDO DESDE OTRA CONSOLA:
#curl -X POST http://localhost:8000/system/execute \                                                   
#-u caballero:Password \
#-H "Content-Type: application/json" \
#-d '{
#  "command": "df",
#  "params": ["-h"]
# }'
