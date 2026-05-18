# Python Selenium Automation 🚀

A collection of Python Selenium automation scripts and practice projects for learning and implementing web automation, browser interaction, and testing workflows using Selenium WebDriver.

This repository contains real-world automation examples such as:
- Web form handling
- Dynamic dropdown interaction
- Browser navigation
- Web scraping basics
- Selenium waits and locators
- Automation testing practice scripts

---

## Features ✨
- Beginner-friendly Selenium examples
- Practical browser automation scripts
- Chrome WebDriver integration
- XPath, CSS Selector, and ID locators
- Dynamic element handling
- Automation practice for interviews and learning

---

## Tech Stack 🛠️
- Python
- Selenium WebDriver
- ChromeDriver
- PyCharm / VS Code

---

## Installation ⚙️

Clone the repository:

```bash
git clone https://github.com/SpRajib/python-Selenium.git
cd python-Selenium
```

Install required packages:

```bash
pip install selenium
```

Download ChromeDriver compatible with your Chrome browser version and add it to your system PATH.

---

## Project Structure 📂

```bash
python-Selenium/
│
├── Test_codes/
├── Practice_scripts/
├── Selenium_examples/
├── README.md
└── requirements.txt
```

---

## Sample Code ▶️

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search = driver.find_element(By.NAME, "q")
search.send_keys("Python Selenium")
search.submit()
```

---

## Learning Topics Covered 📘
- Selenium WebDriver basics
- Locators in Selenium
- Handling alerts and popups
- Dropdown handling
- Waits in Selenium
- Window and tab handling
- Web scraping with Selenium
- Form automation
- Automation testing concepts

---

## Requirements ✅
- Python 3.x
- Google Chrome
- ChromeDriver
- Selenium Library

---

## Author 👨‍💻
**Rajib Sahoo**

GitHub: https://github.com/SpRajib

---

## Repository 🔗
https://github.com/SpRajib/python-Selenium

---

## Future Improvements 🚀
- Add PyTest framework integration
- Implement Page Object Model (POM)
- Add CI/CD with GitHub Actions
- Cross-browser testing support
- Headless browser automation

---

## Contributing 🤝
Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## License 📄
This project is open-source and available under the MIT License.
