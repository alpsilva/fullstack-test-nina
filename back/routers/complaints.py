from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from back.database.database import client
from back.schemas.complaints import ComplaintSchema, ComplaintList

router = APIRouter(prefix='/complaints', tags=['complaints'])

@router.get('/', response_model=ComplaintList)
def get_complaints():
    complaints = client.get_complaints()
    return {'complaints': complaints}

@router.get('/{complaint_id}', response_model=ComplaintSchema)
def get_complaint(complaint_id: str):
    complaint = client.get_complaint(complaint_id)
    if complaint is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Complaint not found.")

    return complaint

# @router.get('/user/{user_id}', response_model=ComplaintList)
# def get_complaints_from_user(user_id: str):
#     # Implement your function here!
