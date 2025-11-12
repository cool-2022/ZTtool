from fastapi import APIRouter


router = APIRouter(tags=["misc"])


@router.get("/api/categories")
async def get_categories():
    """获取工具分类列表"""
    categories = [
        {
            "id": 1,
            "name": "文本工具",
            "description": "处理文本相关的实用工具",
            "tools": [
                {"id": 1, "name": "JSON格式化", "icon": "{}", "description": "格式化JSON数据"},
                {"id": 2, "name": "Base64编码", "icon": "64", "description": "Base64编码解码"},
                {"id": 3, "name": "URL编码", "icon": "%", "description": "URL编码解码"},
                {"id": 4, "name": "文本对比", "icon": "≈", "description": "对比两个文本的差异"}
            ]
        },
        {
            "id": 2,
            "name": "图片工具",
            "description": "图片处理和转换工具",
            "tools": [
                {"id": 5, "name": "图片压缩", "icon": "📷", "description": "压缩图片文件大小"},
                {"id": 6, "name": "格式转换", "icon": "🔄", "description": "转换图片格式"},
                {"id": 7, "name": "二维码生成", "icon": "📱", "description": "生成二维码"},
                {"id": 8, "name": "图片水印", "icon": "💧", "description": "添加图片水印"}
            ]
        },
        {
            "id": 3,
            "name": "开发工具",
            "description": "开发者常用工具",
            "tools": [
                {"id": 9, "name": "正则测试", "icon": ".*", "description": "测试正则表达式"},
                {"id": 10, "name": "颜色选择器", "icon": "🎨", "description": "选择颜色代码"},
                {"id": 11, "name": "时间戳转换", "icon": "⏰", "description": "时间戳转换工具"},
                {"id": 12, "name": "密码生成器", "icon": "🔐", "description": "生成安全密码"}
            ]
        }
    ]
    return {"categories": categories}


@router.get("/api/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy", "message": "ZYTool API is running"}


