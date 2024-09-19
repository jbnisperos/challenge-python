# delete_all_page.py

from playwright.sync_api import expect

class DeleteAllPage:

    def __init__(self, page):
        self.page = page
        self.edit_experience_and_skills = page.locator('[href="/profile/experience-and-skills"]')
        self.edit_qualifications = page.locator('[href="/profile/qualifications"]')
        self.delete_buttons = page.get_by_role('button', name='Delete this item')  # Correct locator, no .first() yet
        self.back_to_profile = page.locator('a:has-text("Back to profile")')
        self.delete_cv = page.get_by_test_id('upload-status-trash-icon').locator('path')
        self.deleting_in_progress = page.locator("text=Deleting...")
        self.count_list = page.get_by_text('NEEDS REVIEW')

    def delete_edit_experience_and_skills(self):
        # Click to navigate to the experience and skills section
        self.edit_experience_and_skills.click()
        self.page.wait_for_load_state('networkidle')  # Wait until the page fully loads

        # Adjusting the regex pattern to match the full URL
        expect(self.page).to_have_url(r'.*/profile/experience-and-skills')

        # Wait before performing any further actions
        self.page.wait_for_timeout(2000)

        count = self.count_list.count()
        for _ in range(count):
            # Click the first delete button at the time of execution
            self.delete_buttons.first.click()
            self.page.wait_for_timeout(2000)

        # Navigate back to the profile page
        self.back_to_profile.click()
        expect(self.page).to_have_url(r'.*/profile')
        self.page.wait_for_load_state('networkidle')

    def delete_edit_qualifications(self):
        # Click to navigate to the qualifications section
        self.edit_qualifications.click()
        self.page.wait_for_load_state('networkidle')  # Wait until the page fully loads

        # Adjusting the regex pattern to match the full URL
        expect(self.page).to_have_url(r'.*/profile/qualifications')

        self.page.wait_for_timeout(2000)

        count = self.count_list.count()
        for _ in range(count):
            # Click the first delete button at the time of execution
            self.delete_buttons.first.click()
            self.page.wait_for_timeout(2000)

        # Navigate back to the profile page
        self.back_to_profile.click()
        expect(self.page).to_have_url(r'.*/profile')
        self.page.wait_for_load_state('networkidle')

    def delete_uploaded_cv(self):
        self.page.wait_for_timeout(2000)
        if self.delete_cv.is_visible():
            self.delete_cv.click()
            self.page.wait_for_timeout(2000)
