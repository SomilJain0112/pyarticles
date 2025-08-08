# Deployment Guide for Crypto News App

This guide will help you deploy your Django crypto news application to various hosting platforms.

## Prerequisites

1. **GitHub Account**: You'll need to push your code to GitHub
2. **Environment Variables**: Set up your API keys and secrets
3. **Domain Name** (optional): For custom domain

## Option 1: Render (Recommended for Beginners)

### Step 1: Prepare Your Code
1. Push your code to GitHub
2. Make sure all files are committed

### Step 2: Deploy on Render
1. Go to [render.com](https://render.com)
2. Sign up/Login with your GitHub account
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure the service:
   - **Name**: `crypto-news-app`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn news.wsgi:application`
   - **Plan**: Free

### Step 3: Set Environment Variables
In Render dashboard, go to your service → Environment → Add:
```
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=your-app-name.onrender.com
CHAINECHO_API_KEY=your-chainecho-api-key
```

### Step 4: Deploy
Click "Create Web Service" and wait for deployment.

## Option 2: Railway

### Step 1: Deploy on Railway
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway will auto-detect Django and deploy

### Step 2: Set Environment Variables
In Railway dashboard → Variables:
```
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=your-app-name.railway.app
CHAINECHO_API_KEY=your-chainecho-api-key
```

## Option 3: Heroku

### Step 1: Install Heroku CLI
```bash
# Windows
# Download from https://devcenter.heroku.com/articles/heroku-cli

# macOS
brew tap heroku/brew && brew install heroku
```

### Step 2: Deploy
```bash
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key-here
heroku config:set CHAINECHO_API_KEY=your-chainecho-api-key

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate
```

## Option 4: DigitalOcean App Platform

### Step 1: Deploy
1. Go to [DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform)
2. Connect your GitHub account
3. Select your repository
4. Configure:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Run Command**: `gunicorn news.wsgi:application`

### Step 2: Set Environment Variables
In the App Platform dashboard → Settings → Environment Variables:
```
DEBUG=False
SECRET_KEY=your-secret-key-here
CHAINECHO_API_KEY=your-chainecho-api-key
```

## Environment Variables Setup

### Generate Secret Key
```python
import secrets
print(secrets.token_urlsafe(50))
```

### Required Environment Variables
```
DEBUG=False
SECRET_KEY=your-generated-secret-key
ALLOWED_HOSTS=your-domain.com,your-app-name.onrender.com
CHAINECHO_API_KEY=your-chainecho-api-key
```

## Local Testing Before Deployment

### Step 1: Test Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export DEBUG=False
export SECRET_KEY=your-secret-key
export CHAINECHO_API_KEY=your-api-key

# Collect static files
python manage.py collectstatic --noinput

# Run with gunicorn
gunicorn news.wsgi:application
```

### Step 2: Test Production Settings
```bash
# Set production environment
export DEBUG=False
python manage.py check --deploy
```

## Post-Deployment Checklist

1. ✅ **SSL Certificate**: Ensure HTTPS is working
2. ✅ **Static Files**: Verify CSS/JS are loading
3. ✅ **API Endpoints**: Test `/api/news/` and `/api/crypto-prices/`
4. ✅ **Database**: Check if migrations ran successfully
5. ✅ **Environment Variables**: Verify all are set correctly
6. ✅ **Performance**: Test page load times

## Troubleshooting

### Common Issues:

1. **Static Files Not Loading**
   - Ensure `whitenoise` is in MIDDLEWARE
   - Run `python manage.py collectstatic`

2. **500 Server Error**
   - Check logs in your hosting platform
   - Verify environment variables are set

3. **API Not Working**
   - Check if `CHAINECHO_API_KEY` is set
   - Verify API endpoint URLs

4. **Database Issues**
   - Run `python manage.py migrate`
   - Check database configuration

## Monitoring and Maintenance

1. **Set up monitoring** (optional):
   - Uptime monitoring
   - Error tracking (Sentry)
   - Performance monitoring

2. **Regular updates**:
   - Keep dependencies updated
   - Monitor security patches
   - Backup database regularly

## Cost Comparison

| Platform | Free Tier | Paid Plans | Ease of Use |
|----------|-----------|------------|-------------|
| Render   | ✅ Yes    | $7/month   | ⭐⭐⭐⭐⭐    |
| Railway  | ✅ Yes    | $5/month   | ⭐⭐⭐⭐     |
| Heroku   | ❌ No     | $7/month   | ⭐⭐⭐⭐⭐    |
| DigitalOcean | ❌ No  | $5/month   | ⭐⭐⭐       |

## Recommended: Render

For beginners, I recommend **Render** because:
- Free tier available
- Easy deployment from GitHub
- Automatic SSL certificates
- Good documentation
- Reliable performance

Your app will be live at: `https://your-app-name.onrender.com` 