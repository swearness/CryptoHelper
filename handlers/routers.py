from aiogram import Router

from . import navigation, profile, start

main_router = Router()


main_router.include_routers(start.router, profile.router, navigation.router)
