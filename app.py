from fastapi import FastAPI

app = FastAPI(
    title="Compax Api Backend",
    docs_url="/api/bare/docs",
    version="0.1.0",
    description="Software Engineering Project",
)


@app.get("/")
async def root():
    return {"Status": 200}
