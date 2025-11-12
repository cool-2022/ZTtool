from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
import json
import base64
import urllib.parse

from backend.schemas import TextProcessRequest, TextCompareRequest


router = APIRouter(prefix="/api/text", tags=["text"])


@router.post("/process")
async def process_text(request: TextProcessRequest):
    """处理文本（JSON格式化、Base64编码解码、URL编码解码）"""
    try:
        if request.action == "json_format":
            parsed = json.loads(request.text)
            formatted = json.dumps(parsed, indent=2, ensure_ascii=False)
            return {"result": formatted, "success": True}

        elif request.action == "base64_encode":
            encoded = base64.b64encode(request.text.encode('utf-8')).decode('utf-8')
            return {"result": encoded, "success": True}

        elif request.action == "base64_decode":
            decoded = base64.b64decode(request.text).decode('utf-8')
            return {"result": decoded, "success": True}

        elif request.action == "url_encode":
            encoded = urllib.parse.quote(request.text)
            return {"result": encoded, "success": True}

        elif request.action == "url_decode":
            decoded = urllib.parse.unquote(request.text)
            return {"result": decoded, "success": True}

        else:
            raise HTTPException(status_code=400, detail="不支持的操作类型")

    except Exception as e:
        return {"result": str(e), "success": False}


@router.post("/compare")
async def compare_text(request: TextCompareRequest):
    """对比两个文本的差异"""
    text1_lines = request.text1.splitlines()
    text2_lines = request.text2.splitlines()

    differences = []
    max_lines = max(len(text1_lines), len(text2_lines))

    for i in range(max_lines):
        line1 = text1_lines[i] if i < len(text1_lines) else ""
        line2 = text2_lines[i] if i < len(text2_lines) else ""

        if line1 != line2:
            differences.append({
                "line": i + 1,
                "text1": line1,
                "text2": line2,
                "type": "modified" if line1 and line2 else ("added" if line2 else "removed")
            })

    return {
        "differences": differences,
        "summary": {
            "total_lines": max_lines,
            "different_lines": len(differences),
            "identical": len(differences) == 0
        }
    }


