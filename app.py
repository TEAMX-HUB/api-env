from fastapi import FastAPI

from routes.admin import adminpoint
from routes.auth import auth
from routes.building import buildingpoint
from routes.classroom import classroompoint
from routes.laboratory import labpoint
from routes.office import officepoint
from routes.ratings import ratingspoint
from routes.schedule import schedule
from routes.user import userpoint

app = FastAPI(
    title="Compax Api Backend",
    docs_url="/api/bare/docs",
    version="0.1.0",
    description="Software Engineering Project",
)


@app.get("/")
async def root():
    return {"Status": 200}


app.include_router(userpoint)
app.include_router(adminpoint)
app.include_router(auth)
app.include_router(classroompoint)
app.include_router(buildingpoint)
app.include_router(labpoint)
app.include_router(officepoint)
app.include_router(schedule)
app.include_router(ratingspoint)
