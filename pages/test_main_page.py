import time
from client import Client


TOVAR_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class Test():

    def test_setup(self):
        page = Client().load_page(TOVAR_LINK)
        page.add_to_basket()
        time.sleep(2)
        page.solve_quiz_and_get_code()
        #time.sleep()


if __name__ == '__main__':
    t = Test()
    t.test_setup()