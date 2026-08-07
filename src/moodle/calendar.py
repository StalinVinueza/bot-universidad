from playwright.sync_api import Page


class Calendar:

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        """
        Abre la página del calendario.
        """
        self.page.goto(
            "https://evea-nivelacion.ueb.edu.ec/calendar/view.php"
        )

        self.page.wait_for_load_state("networkidle")