from fastapi import APIRouter, HTTPException
from datetime import datetime

from schemas import TimestampConvertRequest


router = APIRouter(prefix="/api/timestamp", tags=["timestamp"])


@router.post("/convert")
async def convert_timestamp(request: TimestampConvertRequest):
    """时间戳转换"""
    try:
        if request.action == "to_datetime":
            dt = datetime.fromtimestamp(request.timestamp)
            return {
                "datetime": dt.strftime("%Y-%m-%d %H:%M:%S"),
                "timestamp": request.timestamp,
                "action": request.action
            }

        elif request.action == "to_timestamp":
            return {
                "datetime": request.timestamp,
                "timestamp": int(request.timestamp),
                "action": request.action
            }

        else:
            raise HTTPException(status_code=400, detail="不支持的操作类型")

    except Exception as e:
        return {"error": str(e), "success": False}


