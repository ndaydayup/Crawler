from .common import mobile_common_request
import asyncio

async def request_repost(id: str, cookie: str, offset: int = 0, limit: int = 20) -> dict:
    """
    请求微博获取转发信息
    """
    results = []
    total = 0
    page_size = 20
    start_page = int( offset / page_size ) + 1
    end_page = int((offset + limit - 1) / page_size) + 1
    tasks = [request_page(page, id, cookie) for page in range(start_page, end_page + 1)]
    pages = await asyncio.gather(*tasks)
    for data in pages:
        total = data.get('total_number') if data.get('total_number') else total
        results.extend(data.get('data', []))

    ret = {'total': total, 'results': results[(offset % page_size):(offset % page_size + limit)]}
    return ret

async def request_page(page: int, id: str, cookie: str) -> dict:
    headers = {"Cookie": cookie}
    params = {
        "id": id,
        "page": page,
        "moduleID": "feed",
        "count": "20"
    }
    resp, succ = await mobile_common_request('/ajax/statuses/repostTimeline', params, headers)
    if not succ:
        return {}
    return resp.get('data', {})