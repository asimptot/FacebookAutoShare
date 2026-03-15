# 🚀 Quick Start Guide

Get started in 5 minutes!

## 1️⃣ Installation (2 min)

```bash
# Install dependencies
pip install -r requirements.txt
```

## 2️⃣ Configuration (2 min)

### a) Create Credentials

Copy `credentials.example.py` → `credentials.py` and edit:

```python
FACEBOOK_EMAIL = "your@email.com"
FACEBOOK_PASSWORD = "your_password"
```

### b) Add Products

Copy `products.example.py` → `products.py` and edit:

```python
PRODUCTS = [
    {
        "name": "Hanglamp",
        "image": "lamp.jpg",
        "description": "Een stijlvolle hanglamp in goede staat"
    },
]

FACEBOOK_GROUPS = [
    "marktplaatsnlenbe",
    "1149152901844716",
    # Add group IDs here
]
```

### c) Add Images

Put product images in the project folder (`lamp.jpg` etc.)

## 3️⃣ Run (1 min)

```bash
python run.py
```

## ✅ Success!

The bot will automatically:
- ✅ Login to Facebook
- ✅ Post each product to each group
- ✅ Generate unique descriptions with AI
- ✅ Show statistics

## 🎯 Next Steps

- Add more products → [products.py](products.py)
- Customize settings → [config.py](config.py)
- Detailed documentation → [README.md](README.md)

## ⚠️ Important

- NEVER share credentials
- See browser on first run: `config.py` → `headless: False`
- If hitting rate limit: increase `WAIT_TIMES['between_groups']`

---

**Having issues?** Check the "Troubleshooting" section in README.md!
