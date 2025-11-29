from fastapi import APIRouter, HTTPException
import secrets
import string

from schemas import PasswordGenerateRequest


router = APIRouter(prefix="/api/password", tags=["password"])


@router.post("/generate")
async def generate_password(request: PasswordGenerateRequest):
    """生成安全密码"""
    chars = ""
    if request.include_lowercase:
        chars += string.ascii_lowercase
    if request.include_uppercase:
        chars += string.ascii_uppercase
    if request.include_numbers:
        chars += string.digits
    if request.include_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if not chars:
        raise HTTPException(status_code=400, detail="至少需要选择一种字符类型")

    password = ''.join(secrets.choice(chars) for _ in range(request.length))

    return {
        "password": password,
        "length": request.length,
        "character_types": {
            "lowercase": request.include_lowercase,
            "uppercase": request.include_uppercase,
            "numbers": request.include_numbers,
            "symbols": request.include_symbols
        }
    }


