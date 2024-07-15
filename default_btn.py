from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Share Contact",request_contact=True)
        ]
    ],resize_keyboard=True
)

courses = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Python"),
            KeyboardButton("HTML"),
        ],
        [
            KeyboardButton("CSS"),
            KeyboardButton("JavaScript"),
        ],
    ],resize_keyboard=True
)