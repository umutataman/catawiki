import os
import pytest
from pathlib import Path
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

HEADLESS = os.getenv("HEADLESS", "true").lower() in ("true", "1", "yes")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    launch_args = [
        "--disable-blink-features=AutomationControlled",
        "--no-sandbox",
        "--disable-dev-shm-usage",
    ]
    if HEADLESS:
        launch_args.append("--headless=new")

    instance = playwright_instance.chromium.launch(
        headless=False,
        channel="chrome",
        args=launch_args,
    )
    yield instance
    instance.close()


@pytest.fixture(scope="function")
def context(browser, request):
    ctx = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        ),
        viewport={"width": 1440, "height": 900},
        locale="en-US",
    )
    ctx.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield ctx

    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        trace_dir = Path("test-results") / request.node.name
        trace_dir.mkdir(parents=True, exist_ok=True)
        ctx.tracing.stop(path=str(trace_dir / "trace.zip"))
    else:
        ctx.tracing.stop()
    ctx.close()


@pytest.fixture(scope="function")
def page(context):
    p = context.new_page()
    p.add_init_script(
        'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    )
    yield p
    p.close()
