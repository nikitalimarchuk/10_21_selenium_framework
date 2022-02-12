import pytest


@pytest.mark.smoke
@pytest.mark.c_sharp_cource
def test_check_title_after_click_on_c_sharp_card(dashboard_page):
    c_sharp_course_page = dashboard_page.select_c_sharp_course()

    assert "C#" not in c_sharp_course_page.get_title()
