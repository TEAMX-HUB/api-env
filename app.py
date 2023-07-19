from fastapi import FastAPI

from routes.admin import admin
from routes.auth import auth
from routes.building import building
from routes.classroom import classroom
from routes.laboratory import lab
from routes.office import office
from routes.ratings import ratings
from routes.schedule import schedule
from routes.user import user

app = FastAPI(
    title="Compax Api Backend",
    docs_url="/api/bare/docs",
    version="0.1.0",
    description="Software Engineering Project",
)


@app.get("/")
async def root():
    return {"Status": 200}


app.include_router(user)
app.include_router(admin)
app.include_router(auth)
app.include_router(classroom)
app.include_router(building)
app.include_router(lab)
app.include_router(office)
app.include_router(schedule)
app.include_router(ratings)
