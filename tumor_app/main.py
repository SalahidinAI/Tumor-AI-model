from fastapi import FastAPI
import uvicorn
from tumor_app.api import tumor


tumor_app = FastAPI(title='Tumor')
tumor_app.include_router(tumor.tumor_router)


if __name__ == '__main__':
    uvicorn.run(tumor_app, host='127.0.0.1', port=8000)
