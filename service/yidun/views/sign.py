from utils.error_code import ErrorCode
from utils.reply import reply
from pydantic import BaseModel
import execjs


with open('lib/js/yidun.js', encoding='utf-8') as f:
    yidun_sign_obj = execjs.compile(f.read())

class Param(BaseModel):
    id: str


async def sign(param: Param):
    '''
    生成fp  cb
    '''

    if param.id == 'fp':

        # data = {i: param.data[i] for i in param.data}
        res = yidun_sign_obj.call('get_fp')
        return reply(ErrorCode.OK, '成功' , res)

    else:
        res = yidun_sign_obj.call('get_cb')
        return reply(ErrorCode.OK, '成功' , res)