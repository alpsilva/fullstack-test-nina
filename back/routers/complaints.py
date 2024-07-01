from back.schemas.complaints import ComplaintSchema, ComplaintList
from fastapi import APIRouter, HTTPException
from back.database.database import client
from http import HTTPStatus

router = APIRouter(prefix='/complaints', tags=['complaints'])

@router.get('/', response_model=ComplaintList)
def get_complaints():
    complaints = client.get_complaints()
    complaints.sort(key=lambda x: x['id'])
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
