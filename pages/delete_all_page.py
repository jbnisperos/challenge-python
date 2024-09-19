from playwright.sync_api import expect

class DeleteAllPage:

    def __init__(self, page):
        self.page = page
        self.edit_experience_and_skills = page.locator('[href="/profile/experience-and-skills"]')
        self.edit_qualifications = page.locator('[href="/profile/qualifications"]')
        self.delete_buttons = page.get_by_role('button', name='Delete this item')
        self.back_to_profile = page.locator('a:has-text("Back to profile")')
        self.delete_cv = page.get_by_test_id('upload-status-trash-icon').locator('path')
        self.deleting_in_progress = page.locator("text=Deleting...")
        self.count_list = page.get_by_text('NEEDS REVIEW')

    def delete_edit_experience_and_skills(self):
        # Navigate to the experience and skills section
        self.edit_experience_and_skills.click()
        self.page.wait_for_load_state('networkidle')  # Wait until the page fully loads

        # Match the full URL for experience and skills page
        expect(self.page).to_have_url("https://candidate-qa-test.dev.platform.compono.dev/profile/experience-and-skills")

        # Perform delete actions
        self.page.wait_for_timeout(2000)
        count = self.count_list.count()
        for _ in range(count):
            self.delete_buttons.first.click()
            self.page.wait_for_timeout(2000)
        
        # Navigate back to profile
        self.back_to_profile.click()
        expect(self.page).to_have_url("https://candidate-qa-test.dev.platform.compono.dev/profile")
        self.page.wait_for_load_state('networkidle')

    def delete_edit_qualifications(self):
        # Navigate to the qualifications section
        self.edit_qualifications.click()
        self.page.wait_for_load_state('networkidle')  # Wait until the page fully loads

        # Match the full URL for qualifications page
        expect(self.page).to_have_url("https://candidate-qa-test.dev.platform.compono.dev/profile/qualifications")

        # Perform delete actions
        self.page.wait_for_timeout(2000)
        count = self.count_list.count()
        for _ in range(count):
            self.delete_buttons.first.click()
            self.page.wait_for_timeout(2000)
        
        # Navigate back to profile
        self.back_to_profile.click()
        expect(self.page).to_have_url("https://candidate-qa-test.dev.platform.compono.dev/profile")
        self.page.wait_for_load_state('networkidle')

    def delete_uploaded_cv(self):
        # Wait until the page fully loads and check if the delete CV button is visible
        self.page.wait_for_timeout(2000)
        if self.delete_cv.is_visible():
            self.delete_cv.click()
            self.page.wait_for_timeout(2000)
        else:
            print("Delete CV button not found.")