import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.upload_resume_page import UploadResumePage
from pages.delete_all_page import DeleteAllPage
import sys
import os

# Add parent directory to Python path to ensure imports work correctly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture(scope="session")
def browser_context(playwright):
    # Set up a browser and login context once for all tests
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Login before all tests
    email = "tomlaurence.2000@gmail.com"
    password = "Password!"
    login_page = LoginPage(page)
    login_page.go_to()
    login_page.login(email, password)
    
    # Save storage state for reuse
    context.storage_state(path="state.json")
    
    # Check for upload dialog box and delete items if not visible
    upload_resume_page = UploadResumePage(page)
    
    if not upload_resume_page.upload_dialog_box.is_visible():
        # Perform the delete actions if the upload dialog is not present
        delete_all_page = DeleteAllPage(page)
        
        login_page.go_to()

        # Handle any dialogs
        page.on("dialog", lambda dialog: dialog.accept())
        
        # Perform delete actions
        delete_all_page.delete_edit_experience_and_skills()
        delete_all_page.delete_edit_qualifications()
        delete_all_page.delete_uploaded_cv()
    else:
        print("Upload CV element is already present.")

    yield context
    browser.close()

@pytest.fixture
def new_page(browser_context):
    # Create a new page using the session-scoped context
    page = browser_context.new_page()
    yield page
    # This is where the teardown/afterEach behavior happens
    login_page = LoginPage(page)
    delete_all_page = DeleteAllPage(page)

    login_page.go_to()
    
    # Handle dialogs before performing delete operations
    page.on("dialog", lambda dialog: dialog.accept())

    # Perform delete actions after the test is complete
    delete_all_page.delete_edit_experience_and_skills()
    delete_all_page.delete_edit_qualifications()
    delete_all_page.delete_uploaded_cv()
    
    page.close()

@pytest.mark.usefixtures("new_page")
class TestUploadResume:

    def test_upload_resume_cv1(self, new_page):
        login_page = LoginPage(new_page)
        upload_resume_page = UploadResumePage(new_page)

        file_path = os.path.abspath('./fixtures/CV1.docx')  # Ensure absolute path
        login_page.go_to()
        upload_resume_page.upload_cv_file(file_path)

    def test_upload_resume_cv2(self, new_page):
        login_page = LoginPage(new_page)
        upload_resume_page = UploadResumePage(new_page)

        file_path = os.path.abspath('./fixtures/CV2.doc')  # Ensure absolute path
        login_page.go_to()
        upload_resume_page.upload_cv_file(file_path)

    def test_upload_resume_cv3(self, new_page):
        login_page = LoginPage(new_page)
        upload_resume_page = UploadResumePage(new_page)

        file_path = os.path.abspath('./fixtures/CV3.txt')  # Ensure absolute path
        login_page.go_to()
        upload_resume_page.upload_cv_file(file_path)

    def test_upload_resume_cv4(self, new_page):
        login_page = LoginPage(new_page)
        upload_resume_page = UploadResumePage(new_page)

        file_path = os.path.abspath('./fixtures/CV4.pdf')  # Ensure absolute path
        login_page.go_to()
        upload_resume_page.upload_cv_file(file_path)

    def test_upload_resume_cv5(self, new_page):
        login_page = LoginPage(new_page)
        upload_resume_page = UploadResumePage(new_page)

        file_path = os.path.abspath('./fixtures/CV5.rtf')  # Ensure absolute path
        login_page.go_to()
        upload_resume_page.upload_cv_file(file_path)
