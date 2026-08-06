from playwright.sync_api import sync_playwright, TimeoutError

from src.config.settings import (
    MOODLE_URL,
    MOODLE_USERNAME,
    MOODLE_PASSWORD,
    HEADLESS,
)


class MoodleClient:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=HEADLESS
        )

        self.page = self.browser.new_page()

    def login(self):

        # Abrir Moodle
        self.page.goto(MOODLE_URL)

        self.page.wait_for_load_state("networkidle")

        # Usuario
        self.page.locator('input[type="text"]').fill(MOODLE_USERNAME)

        # Contraseña
        self.page.locator('input[type="password"]').fill(MOODLE_PASSWORD)

        # Botón Acceder
        self.page.get_by_role(
            "button",
            name="Acceder"
        ).click()

        # Esperar redirección
        self.page.wait_for_load_state("networkidle")

        # Si aparece el botón "Continuar"
        try:
            self.page.get_by_role(
                "button",
                name="Continuar"
            ).click(timeout=5000)

            self.page.wait_for_load_state("networkidle")

        except TimeoutError:
            pass

    def is_logged(self):
        self.page.wait_for_load_state("networkidle")
        return "/my" in self.page.url

    def close(self):
        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()