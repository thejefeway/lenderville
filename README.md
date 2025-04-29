
# Lenderville Demo

Demo project for Lenderville refinance quotes.

## How to Deploy

### Backend (API)
- Sign up at Railway.app
- Create new project -> Deploy from GitHub -> select `/backend/`
- Railway will auto deploy FastAPI and give you a public API URL

### Frontend (Website)
- Sign up at Vercel.com
- Create new project -> Import GitHub -> select `/frontend/`
- Change the fetch URL in `index.html` to your new Railway URL + `/get-quote`
- Deploy site

Then your full system is live!

