from aiogram import Router
from .basic import router as basic_router

router = Router()
router.include_router(basic_router)