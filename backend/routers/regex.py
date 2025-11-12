from fastapi import APIRouter
import re

from backend.schemas import RegexTestRequest


router = APIRouter(prefix="/api/regex", tags=["regex"])


@router.post("/test")
async def test_regex(request: RegexTestRequest):
    """测试正则表达式"""
    try:
        pattern = re.compile(request.pattern)
        matches = pattern.findall(request.text)
        match_objects = []

        for match in pattern.finditer(request.text):
            match_objects.append({
                "match": match.group(),
                "start": match.start(),
                "end": match.end(),
                "groups": match.groups()
            })

        return {
            "matches": matches,
            "match_details": match_objects,
            "success": True
        }

    except re.error as e:
        return {"error": str(e), "success": False}


