from fastapi import APIRouter, HTTPException

from backend.schemas import TextProcessRequest, TextCompareRequest

router = APIRouter(prefix="/api/diff", tags=["diff"])

@router.post("/diff")
async def process_text(request: TextProcessRequest):
    '''比较两个文件夹的不同'''
    try:
        return {"result": "功能开发中...", "success": True}
    except Exception as e:
        return {"result": str(e), "success": False}

