from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📝EFendi haqida malumot", callback_data="alert")], # noqa
    [InlineKeyboardButton(text="📖Menu korish", callback_data="korish"), InlineKeyboardButton(text="📜Oldindan xona band qilish", callback_data="zakaz")], # noqa
    [InlineKeyboardButton(text="👀Band qilingan joylarni korish", callback_data="bo'sh"), InlineKeyboardButton(text="👨‍💻Adminga yozish", callback_data="adminga_yozish", url="https://t.me/Rahimov_MR")]
]) # noqa


department = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="1-Bolim", callback_data="bolim1"), InlineKeyboardButton(text="2-Bolim", callback_data="bolim2")], # noqa
    [InlineKeyboardButton(text="3-Bolim", callback_data="bolim3"), InlineKeyboardButton(text="4-Bolim", callback_data="bolim4")], # noqa
    [InlineKeyboardButton(text="🔙Orqaga qaytish")] # noqa
]) # noqa


yes_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="HA", callback_data="yes"), InlineKeyboardButton(text="Boshqasi", callback_data="no")],
    [InlineKeyboardButton(text="Xona haqida malumot olish", callback_data="room_data")]
])
delete_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Malumotni ochirib yuborish", callback_data="delete")],
])