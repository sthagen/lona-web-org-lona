async def test_rendering(lona_project_context):
    import os

    from playwright.async_api import async_playwright

    from lona.html import HTML

    TEST_PROJECT_PATH = os.path.join(__file__, '../../test_project')

    context = await lona_project_context(
        project_root=TEST_PROJECT_PATH,
        settings=['settings.py'],
    )

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        browser_context = await browser.new_context()
        page = await browser_context.new_page()

        # start rendering test view
        await page.goto(context.make_url('/frontend/rendering/'))
        await page.wait_for_selector('#lona>div>h2:has-text("Rendering Test")')

        rendering_root_element = page.locator('#lona #rendering-root')

        # get total rendering steps
        total_steps_element = page.locator('#lona #step-label #total')
        total_steps = int(await total_steps_element.inner_text())

        for step in range(1, total_steps):

            # start next step
            await page.locator('#lona #next-step').click()
            await page.wait_for_selector(f'#lona #step-label>#current:has-text("{step}")')

            # get rendered html
            html_string = await rendering_root_element.inner_html()

            # parse and compare html
            html = HTML(f'<div id="rendering-root">{html_string}</div>')

            assert html == context.server.state['rendering-root']
