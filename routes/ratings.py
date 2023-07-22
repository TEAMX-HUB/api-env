from fastapi import APIRouter

ratings = APIRouter()

# GET /ratings/classrooms/{id}: Retrieves ratings and reviews for a specific classroom.
# GET /ratings/laboratories/{id}: Retrieves ratings and reviews for a specific laboratory
# POST /ratings/classrooms/{id}: Adds a new rating and review for a specific classroom.
# POST /ratings/laboratories/{id}: Adds a new rating and review for a specific laboratory.
