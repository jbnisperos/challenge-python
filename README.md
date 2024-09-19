# Playwright Automation with Python

This project demonstrates how to run automated tests using Playwright in Python. It includes tests for uploading resumes and cleaning up user profiles through actions like deleting experience, qualifications, and uploaded CVs.

## Project Structure

Sure! Below is an example of a README.md file that includes setup instructions for your Playwright tests, including the step to set the PYTHONPATH.
README.md

markdown

# Playwright Automation with Python

This project demonstrates how to run automated tests using Playwright in Python. It includes tests for uploading resumes and cleaning up user profiles through actions like deleting experience, qualifications, and uploaded CVs.

## Project Structure

/challenge-python ├── /pages │ ├── login_page.py # Handles login functionality │ ├── upload_resume_page.py # Handles resume upload functionality │ └── delete_all_page.py # Handles deletion of user experience, qualifications, and uploaded CVs ├── /tests │ └── test_upload_resume.py # Test file for uploading resumes and cleanup └── README.md # Project setup and instructions (this file)


## Prerequisites

Ensure the following are installed:


## Prerequisites

Ensure the following are installed:

1. **Python 3.10+**: Check [Python's website](https://www.python.org/downloads/) for installation instructions.
2. **Playwright for Python**: Playwright is used for browser automation. Install Playwright by following these steps:
   ```bash
   pip install pytest-playwright
   playwright install
    

3. **pytest:** This project uses pytest to run tests. You can install it via:

```bash
pip install pytest
```

## Setup Instructions

1. **Clone the repository**

Clone this repository to your local machine:

```bash
git clone https://github.com/your-repo/challenge-python.git
```

2. **Navigate to the project directory**

```bash
cd challenge-python
```

3. **Install dependencies**

Ensure that all required Python packages and Playwright are installed by running:

```bash
pip install -r requirements.txt
playwright install
```

4. **Export PYTHONPATH**

For macOS/Linux:

```bash 
export PYTHONPATH=$PYTHONPATH:/[project root directory]/challenge-python
```

For Windows (Command Prompt):


set PYTHONPATH=%PYTHONPATH%;C:\[project root directory]\challenge-python


For Windows (PowerShell):

```powershell
$env:PYTHONPATH += ";C:\[project root directory]\challenge-python"
```

Note: Replace the path with the correct absolute path to your project on your machine.

Alternatively, you can modify the test_upload_resume.py file to add the project root directory to sys.path programmatically, as shown below:

python

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

5. **Run the Tests**

To run the tests using pytest, use the following command:

```bash
pytest tests/test_upload_resume.py
```