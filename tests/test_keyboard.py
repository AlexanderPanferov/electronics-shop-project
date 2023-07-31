from src.keyboard import Keyboard


def test_init():
    keyboard = Keyboard("Keyboard", 2000, 31)

    assert keyboard.name == "Keyboard"
    assert keyboard.price == 2000
    assert keyboard.quantity == 31


def test_change_lang():
    keyboard = Keyboard("Keyboard", 2000, 31)

    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang().change_lang()
    assert keyboard.language == 'RU'
