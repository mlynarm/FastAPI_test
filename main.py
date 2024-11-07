from fastapi import FastAPI

# Inicializace FastAPI instance
app = FastAPI()

# Definování GET endpointu
@app.get("/test")
async def test_success():
    return "Working properly..."
