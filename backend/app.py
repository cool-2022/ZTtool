from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers.text import router as text_router
from backend.routers.regex import router as regex_router
from backend.routers.password import router as password_router
from backend.routers.timestamp import router as timestamp_router
from backend.routers.misc import router as misc_router


app = FastAPI(title="ZYTool API", version="1.0.0")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vue开发服务器端口
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由模块
app.include_router(text_router)
app.include_router(regex_router)
app.include_router(password_router)
app.include_router(timestamp_router)
app.include_router(misc_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
