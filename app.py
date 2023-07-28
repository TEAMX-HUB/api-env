from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

prefix = "/api/v1"


@app.get("/")
async def root():
    return {"Status": 200}


app.include_router(user, prefix=prefix)
app.include_router(admin, prefix=prefix)
app.include_router(auth, prefix=prefix)
app.include_router(classroom, prefix=prefix)
app.include_router(building, prefix=prefix)
app.include_router(lab, prefix=prefix)
app.include_router(office, prefix=prefix)
app.include_router(schedule, prefix=prefix)
app.include_router(ratings, prefix=prefix)
