from pydantic import BaseModel


class TextProcessRequest(BaseModel):
    text: str
    action: str  # "json_format", "base64_encode", "base64_decode", "url_encode", "url_decode"


class TextCompareRequest(BaseModel):
    text1: str
    text2: str


class PasswordGenerateRequest(BaseModel):
    length: int = 12
    include_symbols: bool = True
    include_numbers: bool = True
    include_uppercase: bool = True
    include_lowercase: bool = True


class RegexTestRequest(BaseModel):
    pattern: str
    text: str


class TimestampConvertRequest(BaseModel):
    timestamp: int
    action: str  # "to_datetime" or "to_timestamp"


