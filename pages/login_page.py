from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email = page.locator('[placeholder="yours\\@example\\.com"]')
        self.password = page.locator('[placeholder="your password"]')
        self.login_button = page.locator('[aria-label="Log In"]')

    def go_to(self):
        # Go to the login page and wait for the page to load fully
        with self.page.expect_navigation():
            self.page.goto("https://candidate-qa-test.dev.platform.compono.dev/")
        self.page.wait_for_load_state('networkidle')

    def login(self, email, password):
        # Fill in email and password and click login
        self.email.fill(email)
        self.password.fill(password)
        with self.page.expect_navigation():
            self.login_button.click()
        self.page.wait_for_load_state('networkidle')
