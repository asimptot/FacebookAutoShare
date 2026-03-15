# AI Configuration
import g4f
import g4f.models
from g4f.Provider import RetryProvider
from g4f.client import Client
import sys
import asyncio

# Event loop policy for Windows
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# AI Providers (Single reliable provider)
# Format: (Provider_Name, Model_Name)
DEFAULT_PROVIDERS = [
    ("Yqcloud", "gpt-4"),  # Single reliable provider
]

def get_providers():
    """Load AI providers"""
    providers = []
    for provider_name, model_name in DEFAULT_PROVIDERS:
        try:
            ProviderClass = getattr(g4f.Provider, provider_name)
            providers.append(ProviderClass)
            print(f"✅ Provider loaded: {provider_name} (model: {model_name})")
        except AttributeError:
            print(f"⚠️ Provider not found: {provider_name}")
    return providers

def get_ai_client():
    """Create AI client"""
    providers = get_providers()
    if not providers:
        print("⚠️ No providers loaded, using default client")
        return Client()
    # Single provider, no retry needed
    return Client(provider=providers[0])

# AI Model - Use first available provider's model
AI_MODEL = DEFAULT_PROVIDERS[0][1] if DEFAULT_PROVIDERS else "gpt-4"

# Browser Settings
BROWSER_OPTIONS = {
    'headless': False,
    'window_position': '--window-position=-2400,-2400',
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'chrome_version': 137,
    'scale_factor': '0.75'
}

# Wait times (seconds)
WAIT_TIMES = {
    'page_load': 5,
    'after_login': 30,  # Increased to 30 seconds for manual bot verification
    'after_click': 2,
    'image_upload': 10,
    'after_post': 10,
    'between_groups': (120, 240),  # random range (min, max)
}

# Facebook element classes (spaces will be replaced with dots)
FB_ELEMENTS = {
    'cookies_button': 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen x1s688f xtk6v10',
    'post_button': 'x1i10hfl x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou'
}
