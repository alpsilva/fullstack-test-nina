from back.schemas.complaints import ComplaintSchema, ComplaintList, ComplaintUserSchema, ComplaintUserList
from fastapi import APIRouter, HTTPException
from back.database.database import client
from http import HTTPStatus

router = APIRouter(prefix='/complaints', tags=['complaints'])

@router.get('/', response_model=ComplaintUserList)
def get_complaints():
    complaints = client.get_complaints()
    complaints.sort(key=lambda x: x['id'])
    return {'complaints': complaints}

@router.get('/group/types')
def get_complaints_group_by_types():
    return {'types': client.group_by('type')}

@router.get('/group/genders')
def get_complaints_group_by_genders():
    return {'genders': client.group_by('user_gender')}

@router.get('/group/age_group')
def get_complaints_group_by_age_group():
    return {'age_groups': client.group_by_age_group()}

@router.get('/group/moment')
def get_complaints_group_by_moment():
    return {'at_moment': client.group_by('at_moment')}

@router.get('/group/months')
def get_complaints_group_by_months():
    return {'months': client.group_by_month()}

@router.get('/group/neighborhoods')
def get_complaints_group_by_neighborhoods():
    return {'neighborhoods': client.group_by('neighborhood')}

@router.get('/{complaint_id}', response_model=ComplaintSchema)
def get_complaint(complaint_id: str):
    complaint = client.get_complaint(complaint_id)
    
    if complaint is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Complaint not found.")

    return complaint

# @router.get('/user/{user_id}', response_model=ComplaintList)
# def get_complaints_from_user(user_id: str):
#     # Implement your function here!
