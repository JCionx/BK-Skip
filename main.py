from typing import Optional
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware
from playwright.async_api import async_playwright, Playwright
import asyncio
import json
import os
from nicegui import Client, app, ui

passwords = {'admin': 'admin'}

if not os.path.exists('/app/creds.json'):
    default_passwords = {'admin': 'admin'}
    with open('/app/creds.json', 'w') as f:
        json.dump(default_passwords, f, indent=4)

with open('/app/creds.json', 'r') as f:
    passwords = json.load(f)

unrestricted_page_routes = {'/login'}

class AuthMiddleware(BaseHTTPMiddleware):
    """This middleware restricts access to all NiceGUI pages.

    It redirects the user to the login page if they are not authenticated.
    """

    async def dispatch(self, request: Request, call_next):
        if not app.storage.user.get('authenticated', False):
            if request.url.path in Client.page_routes.values() and request.url.path not in unrestricted_page_routes:
                app.storage.user['referrer_path'] = request.url.path  # remember where the user wanted to go
                return RedirectResponse('/login')
        return await call_next(request)


app.add_middleware(AuthMiddleware)


@ui.page('/')
def main_page() -> None:
    steps = 24
    async def run(playwright: Playwright):
        ui.notify("Generating code...")
        progressbar.set_visibility(True)
        generate_button.set_visibility(False)

        chromium = playwright.chromium
        browser = await chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://rbixm.qualtrics.com/jfe/form/SV_9MHgHFvPm0OEHr0?CountryCode=PRT&Q_Language=PT&PT=1")  # Replace with the actual URL

        # Burger King number
        progressbar.value = 1 / steps
        await (await page.wait_for_selector(".QR-QID4")).fill("15130")
        await asyncio.sleep(1.5)
        await (await page.wait_for_selector("#NextButton")).click()

        # Date and time of visit
        progressbar.value = 2 / steps
        await (await page.wait_for_selector(".QR-QID118-2")).click()
        await asyncio.sleep(0.1)
        await (await page.wait_for_selector(".ui-datepicker-today")).click()
        await (await page.wait_for_selector('[name="QR~QID8#1~1"]')).select_option("8")
        await (await page.wait_for_selector('[name="QR~QID8#2~1"]')).select_option("4")
        await (await page.wait_for_selector('[name="QR~QID8#3~1"]')).select_option("1")
        await asyncio.sleep(0.4)
        await (await page.wait_for_selector("#NextButton")).click()

        # Order type
        progressbar.value = 3 / steps
        await (await page.wait_for_selector("#QID12-1-label")).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # Order receiving method
        progressbar.value = 4 / steps
        await (await page.wait_for_selector("#QID14-2-label")).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # How satisfied were you with the visit
        progressbar.value = 5 / steps
        await (await page.wait_for_selector("#QID18-17-label")).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # Tell us in three sentences what you liked the most about your visit
        progressbar.value = 6 / steps
        await (await page.wait_for_selector(".QR-QID117")).fill("...")
        await (await page.wait_for_selector("#NextButton")).click()

        # Classify your satisfaction with the service
        progressbar.value = 7 / steps
        await (await page.wait_for_selector('[for="QR~QID121~4~12"]')).click()
        await (await page.wait_for_selector('[for="QR~QID121~5~12"]')).click()
        await (await page.wait_for_selector('[for="QR~QID121~10~12"]')).click()
        await (await page.wait_for_selector('[for="QR~QID121~11~12"]')).click()
        await (await page.wait_for_selector('[for="QR~QID121~13~12"]')).click()
        await (await page.wait_for_selector('[for="QR~QID121~16~12"]')).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # Classify the restaurant hygiene
        progressbar.value = 8 / steps
        await (await page.wait_for_selector('[for="QR~QID123~7~12"]')).click()
        await (await page.wait_for_selector('[for="QR~QID123~9~12"]')).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # Classify the satisfaction with the advanced hygiene measures
        progressbar.value = 9 / steps
        await (await page.wait_for_selector('#QID122-8-label')).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # Classify the satisfaction with the food
        progressbar.value = 10 / steps
        await (await page.wait_for_selector('[for="QR~QID21~1~12"]')).click()
        await (await page.wait_for_selector('[for="QR~QID21~2~12"]')).click()
        await (await page.wait_for_selector('[for="QR~QID21~3~12"]')).click()
        await (await page.wait_for_selector('[for="QR~QID21~20~12"]')).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # Classify the satisfaction with the item
        progressbar.value = 11 / steps
        await (await page.wait_for_selector('[for="QR~QID22~1~8"]')).click()
        await (await page.wait_for_selector('[for="QR~QID22~2~13"]')).click()
        await (await page.wait_for_selector('[for="QR~QID22~3~13"]')).click()
        await (await page.wait_for_selector('[for="QR~QID22~4~13"]')).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # Did any problem occur during the visit?
        progressbar.value = 12 / steps
        await (await page.wait_for_selector("#QID38-2-label")).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # Based on your experience, how likely are you to recommend Burger King to a friend or family member?
        progressbar.value = 13 / steps
        await (await page.wait_for_selector('[for="QR~QID41~1~6"]')).click()
        await (await page.wait_for_selector('[for="QR~QID41~2~6"]')).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # What main item did you order?
        progressbar.value = 14 / steps
        await (await page.wait_for_selector('#QID46-312-label')).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # What extras or desserts did you order?
        progressbar.value = 15 / steps
        await (await page.wait_for_selector('#QID47-128-label')).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # How many people were in your group?
        progressbar.value = 16 / steps
        await (await page.wait_for_selector('#QID55-1-label')).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # Did you ask for a custom order?
        progressbar.value = 17 / steps
        await (await page.wait_for_selector("#QID57-2-label")).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # How many times have you visited a Burger King in the last month?
        progressbar.value = 18 / steps
        await (await page.wait_for_selector("#QID60-1-label")).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # How many times have you visited a fast food restaurant in the last month?
        progressbar.value = 19 / steps
        await (await page.wait_for_selector("#QID61-1-label")).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # Why did you visit Burger King today?
        progressbar.value = 20 / steps
        await (await page.wait_for_selector("#QID62-3-label")).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # Would you like to shout out to any employee?
        progressbar.value = 21 / steps
        await (await page.wait_for_selector("#QID78-2-label")).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # What's your gender?
        progressbar.value = 22 / steps
        await (await page.wait_for_selector("#QID65-5-label")).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # What's your age?
        progressbar.value = 23 / steps
        await (await page.wait_for_selector("#QID66-6-label")).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # What's your household income?
        progressbar.value = 24 / steps
        await (await page.wait_for_selector("#QID108-175-label")).click()
        await (await page.wait_for_selector("#NextButton")).click()

        # Show the validation code
        progressbar.set_visibility(False)
        progressbar.value = 0
        generate_button.set_visibility(True)

        result = await (await page.wait_for_selector("#EndOfSurvey")).inner_text()
        survey_code = result.split("Código de validação: ")[1][:7]
        ui.notify("Completed")
        code_dialog.open()
        code_label.set_text(survey_code)

        await browser.close()

    async def main():
        async with async_playwright() as playwright:
            await run(playwright)

    ui.page_title("BK Skip")

    with ui.card().classes('fixed-center'):
        ui.label('BK Skip').style("font-size: 180%; width: 100%; text-align: center;")
        progressbar = ui.linear_progress(value=0, show_value=False)
        progressbar.set_visibility(False)
        generate_button = ui.button('Generate code', on_click=lambda: main())

        with ui.dialog() as code_dialog, ui.card():
            ui.label('The code is:').style("margin: 0 80px; text-align: center;")
            code_label = ui.label('FFFFFFF').style("width: 100%; text-align: center; font-weight: bold; font-size: large;")
            ui.button('Close', on_click=code_dialog.close).style("width: 100%;")
    ui.button(on_click=lambda: (app.storage.user.clear(), ui.navigate.to('/login')), icon='logout').props('outline round')

@ui.page('/login')
def login() -> Optional[RedirectResponse]:
    ui.page_title("BK Skip - Login")

    def try_login() -> None:  # local function to avoid passing username and password as arguments
        if passwords.get(username.value) == password.value:
            app.storage.user.update({'username': username.value, 'authenticated': True})
            ui.navigate.to(app.storage.user.get('referrer_path', '/'))  # go back to where the user wanted to go
        else:
            ui.notify('Wrong username or password', color='negative')

    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/')
    with ui.card().classes('absolute-center'):
        ui.label('BK Skip').style("font-size: 180%; width: 100%; text-align: center;")
        username = ui.input('Username').on('keydown.enter', try_login)
        password = ui.input('Password', password=True, password_toggle_button=True).on('keydown.enter', try_login)
        ui.button('Log in', on_click=try_login).style("width: 100%;")
    return None

ui.run(storage_secret='0fcbe8045a2f126b7cb320e1dbcf6846ad7cfc6a78fbca8d6a08263cebb60462', favicon="/opt/app/icon.png")
