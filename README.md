# Facebook Product Sales Automation

Python script for automatic product posting in Facebook groups. Developed with **modular and clean code structure**.

## ✨ Features

- 🤖 AI-generated unique post texts
- 🔄 Multiple products and groups support
- 🔒 Secure credential management (not committed to Git)
- 📊 Detailed progress tracking and statistics
- 🧩 Modular code structure (easy development)

## 🏗️ Modular Structure

```
Facebook/
├── config.py              # 🔧 All settings (AI, browser, wait times)
├── credentials.py         # 🔐 SECRET - Facebook login credentials
├── products.py            # 🛍️ Product and group configuration
├── ai_generator.py        # 🤖 AI text generation
├── facebook_bot.py        # 🌐 Facebook automation operations
├── run.py                 # ▶️ Main execution file
├── .gitignore            # 🚫 Files to be ignored by Git
└── har_and_cookies/      # 🍪 Cookie information (ignored)
```

### Modules

**config.py** - Central Configuration
- AI provider settings (OperaAria, Mintlify, AnyProvider, Yqcloud)
- Browser settings
- Wait times
- Facebook element classes

**ai_generator.py** - AI Text Generator
- Creates unique posts from product descriptions
- Custom prompt support
- Safe operation with error handling

**facebook_bot.py** - Facebook Bot
- Browser management
- Facebook login operations
- Post sharing in groups
- Image upload

**run.py** - Main Program
- Product posting manager
- Statistics tracking
- Error handling

## 🔒 Security (IMPORTANT!)

This project protects your credentials. **credentials.py**, **products.py** and product images are not committed.

## 📦 Installation

### 1. Install Dependencies

```bash
pip install undetected-chromedriver selenium g4f
```

### 2. Create Credentials File

Copy `credentials.example.py` to `credentials.py` and enter your information:

```python
FACEBOOK_EMAIL = "email@example.com"
FACEBOOK_PASSWORD = "your_password"
```

### 3. Configure Product Information

Copy `products.example.py` to `products.py` and add your products:

```python
PRODUCTS = [
    {
        "name": "Hanglamp",
        "image": "lamp.jpg",
        "description": "Een stijlvolle hanglamp..."
    },
]

FACEBOOK_GROUPS = ["group_id_1", "group_id_2", ...]
```

### 4. Add Images

Put your product images in the project folder (e.g., `lamp.jpg`)

## ⚙️ Configuration

### AI Provider Settings

You can change providers in [config.py](config.py):

```python
PROVIDER_NAMES = [
    "OperaAria",
    "Mintlify",
    "AnyProvider",
    "Yqcloud",
]
```

### Adjust Wait Times

In [config.py](config.py):

```python
WAIT_TIMES = {
    'page_load': 5,
    'after_login': 5,
    'between_groups': (120, 240),  # min-max
}
```

## ▶️ Running

```bash
python run.py
```

### Output Example

```
🚀 Starting Facebook Product Posting Bot...

🌐 Starting browser...
✅ Browser ready
✅ Provider loaded: OperaAria
✅ Provider loaded: Mintlify
🤖 AI client ready
🔐 Logging in to Facebook...
✅ Login successful

============================================================
📦 2 products to be posted in 65 groups
============================================================

============================================================
🛍️  [1/2] Hanglamp
============================================================
  [1/65] Group: marktplaatsnlenbe
  ✅ Success!
  ...

📊 SUMMARY
============================================================
Total posting attempts: 130
✅ Successful: 125
❌ Failed: 5
📈 Success rate: 96.2%
```

## 🎨 Adding and Editing Products

### Add Single Product

In [products.py](products.py):

```python
PRODUCTS = [
    {
        "name": "Hanglamp",
        "image": "lamp.jpg",  # Image filename
        "description": "Een stijlvolle hanglamp in goede staat"
    },
]
```

### Multiple Products

```python
PRODUCTS = [
    {
        "name": "Hanglamp",
        "image": "lamp.jpg",
        "description": "Een stijlvolle hanglamp..."
    },
    {
        "name": "Bank",
        "image": "bank.jpg",
        "description": "Comfortabele tweedehands bank..."
    },
    {
        "name": "Tafel",
        "image": "tafel.jpg",
        "description": "Mooie houten tafel..."
    },
]
```

## 🔧 Advanced Settings

### Disable Headless Mode (To See Browser)

In [config.py](config.py):

```python
BROWSER_OPTIONS = {
    'headless': False,  # Change True to False
    ...
}
```

### Decrease/Increase Wait Times

```python
WAIT_TIMES = {
    'between_groups': (60, 120),  # Faster (default: 120-240)
}
```

## 🐛 Troubleshooting

### Error: "Provider not found"

Some providers may change over time. Try different providers in [config.py](config.py).

### Error: "Element not found"

Facebook interface may have changed. You may need to update XPATHs in [facebook_bot.py](facebook_bot.py).

### Images Not Uploading

- Ensure images are in the project folder
- Ensure filenames are correct (case-sensitive)

## 🚀 Development

### Adding New Module

With modular structure, you can easily add new features:

```python
# new_module.py
from config import get_ai_client

def new_feature():
    # Your code...
    pass
```

### Customizing AI Prompt

Edit the `generate_post_text` method in [ai_generator.py](ai_generator.py):

```python
prompt = f"Your custom prompt: {product_description}"
```

## ⚠️ Important Notes

- 🚫 Wait between groups to avoid being flagged as spam
- 🔐 NEVER share your credentials file
- 📸 Use high-quality images for each product  
- ⏰ Be aware of Facebook's rate limits
- 📝 Write clear and honest product descriptions

## 🔐 Git Commit Security

Thanks to the `.gitignore` file, your sensitive information is not committed:

| File/Folder | Status |
|--------------|-------|
| credentials.py | ❌ Not committed |
| products.py | ❌ Not committed |
| *.jpg, *.png | ❌ Not committed |
| har_and_cookies/ | ❌ Not committed |
| config.py | ✅ Committed (no sensitive info) |
| facebook_bot.py | ✅ Committed |
| ai_generator.py | ✅ Committed |
| run.py | ✅ Committed |

You can safely use `git add .` and `git commit`!

## 📜 License

This project should be used at your own responsibility. Make sure you comply with Facebook's terms of use.

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/newFeature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/newFeature`)
5. Open a Pull Request

---

**Note:** The `init.py` file is legacy and no longer used. All functionality has been moved to modular files.
