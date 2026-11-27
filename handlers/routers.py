from aiogram import Router

from . import profile, start

main_router = Router()


main_router.include_routers(start.router, profile.router)
