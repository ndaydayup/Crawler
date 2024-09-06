from . import views
from fastapi import APIRouter

router = APIRouter(prefix='/xhs')

router.add_api_route('/sign', views.sign, methods=['POST'])