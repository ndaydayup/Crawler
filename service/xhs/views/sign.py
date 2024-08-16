import json

from utils.error_code import ErrorCode
from utils.reply import reply
from lib.logger import logger
from pydantic import BaseModel
from typing import Dict, Any
import execjs


with open('lib/js/xhs.js', encoding='utf-8') as f:
    xhs_sign_obj = execjs.compile(f.read())

class Param(BaseModel):
    api: str
    cookie: str
    data: dict = None

async def sign(param: Param):
    '''
    生成xs xt xc xbt
    '''

    if param.api == '' or param.cookie == '':
        logger.error(f'api or cookie is empty, api: {param.api}, cookie: {param.cookie}')
        return reply(ErrorCode.PARAMETER_ERROR, "api and cookie is required")

    # data = {i: param.data[i] for i in param.data}
    res = xhs_sign_obj.call('sign', param.api, param.data, param.cookie)
    return reply(ErrorCode.OK, '成功' , res)