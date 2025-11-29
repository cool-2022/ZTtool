from fastapi import APIRouter, HTTPException

from schemas import TextCompareRequest

router = APIRouter(prefix="/api/diff", tags=["diff"])

@router.post("/compare")
async def compare_files(request: TextCompareRequest):
    '''比较两个文本文件的不同'''
    try:
        # 分割成行
        lines_a = request.text1.split('\n')
        lines_b = request.text2.split('\n')
        
        only_in_a = []
        only_in_b = []
        
        # 简单的逐行比对算法
        max_lines = max(len(lines_a), len(lines_b))
        
        for i in range(max_lines):
            line_a = lines_a[i] if i < len(lines_a) else None
            line_b = lines_b[i] if i < len(lines_b) else None
            
            if line_a is not None and line_b is not None:
                if line_a != line_b:
                    # 行内容不同
                    if line_a not in lines_b:
                        only_in_a.append({
                            "lineNumber": i + 1,
                            "content": line_a
                        })
                    if line_b not in lines_a:
                        only_in_b.append({
                            "lineNumber": i + 1,
                            "content": line_b
                        })
            elif line_a is not None:
                # 只存在于A
                only_in_a.append({
                    "lineNumber": i + 1,
                    "content": line_a
                })
            elif line_b is not None:
                # 只存在于B
                only_in_b.append({
                    "lineNumber": i + 1,
                    "content": line_b
                })
        
        return {
            "onlyInA": only_in_a,
            "onlyInB": only_in_b,
            "success": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

