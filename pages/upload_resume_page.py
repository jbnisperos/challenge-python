# upload_resume_page.py

from playwright.sync_api import expect

class UploadResumePage:
    
    def __init__(self, page):
        self.page = page
        self.upload_cv = page.get_by_test_id('upload-cv-input')
        self.uploading_in_progress = page.locator("text=Uploading...")
        self.dialog_box_close_button = page.locator('.CloseIconButton-sc-19wgu2s-0')
        self.upload_dialog_box = page.get_by_test_id('upload-dialog').get_by_test_id('upload-cv-button')

    def upload_cv_file(self, file_path):
        # Upload the file to the CV input
        self.upload_cv.set_input_files(file_path)
        
        # Check if the upload is in progress
        expect(self.uploading_in_progress).to_be_visible()
        expect(self.uploading_in_progress).to_be_hidden()
        
        # Close the upload dialog
        self.dialog_box_close_button.click()
