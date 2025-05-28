from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        # Go to the Audi PDF viewer
        page.goto("https://stock.audi.bg/pdf/offer/A-2024-0234633-BG")
        page.wait_for_timeout(5000)

        # Click the download button
        with page.expect_download() as download_info:
            page.click("#download")
        download = download_info.value

        file_path = os.path.join(os.getcwd(), download.suggested_filename)
        download.save_as(file_path)
        print(f"✅ File downloaded: {file_path}")

        browser.close()

if __name__ == "__main__":
    run()
