# Deploy to Render - Quick Guide

## Step 1: Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit for Render deployment"

# Add your GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

## Step 2: Deploy on Render

1. **Go to [render.com](https://render.com)**
2. **Sign up/Login** with your GitHub account
3. **Click "New +"** → **"Web Service"**
4. **Connect your GitHub repository**
5. **Configure the service:**

### Basic Settings:
- **Name**: `crypto-news-app` (or your preferred name)
- **Environment**: `Python 3`
- **Region**: Choose closest to your users
- **Branch**: `main`

### Build & Deploy Settings:
- **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- **Start Command**: `gunicorn news.wsgi:application`
- **Plan**: Free

## Step 3: Set Environment Variables

In Render dashboard → Your Service → Environment → Add these variables:

```
DEBUG=False
SECRET_KEY=your-generated-secret-key-here
ALLOWED_HOSTS=your-app-name.onrender.com
CHAINECHO_API_KEY=your-chainecho-api-key
```

### Generate Secret Key:
```python
import secrets
print(secrets.token_urlsafe(50))
```

## Step 4: Deploy

Click **"Create Web Service"** and wait for deployment (usually 2-5 minutes).

## Step 5: Your App is Live!

Your app will be available at: `https://your-app-name.onrender.com`

## Troubleshooting

### If deployment fails:
1. Check the build logs in Render dashboard
2. Verify all environment variables are set
3. Make sure `requirements.txt` is in the root directory
4. Ensure `Procfile` is present and correct

### If app doesn't load:
1. Check the logs in Render dashboard
2. Verify `ALLOWED_HOSTS` includes your Render domain
3. Make sure `DEBUG=False` in production

## Features You'll Have Live:

✅ Real-time crypto price ticker  
✅ News articles in 3-column grid  
✅ Responsive design  
✅ API endpoints for news and prices  
✅ Professional styling like CoinDesk  

## Next Steps After Deployment:

1. **Test all features** on your live site
2. **Set up monitoring** (optional)
3. **Configure custom domain** (optional)
4. **Set up automatic deployments** from GitHub

Your crypto news app will be live and accessible worldwide! 🎉 