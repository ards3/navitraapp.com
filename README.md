# Navitra Website - Deployment Guide

## 📁 File Structure

```
navitra-website/
├── index.html      # Landing page
├── privacy.html    # Privacy Policy
├── terms.html      # Terms of Service
├── support.html    # Support/FAQ page
├── images/         # Create this folder
│   ├── favicon.png
│   ├── hero-phone.png (app screenshot)
│   └── og-image.png (social share image)
└── README.md
```

## 🚀 Deployment Options

### Option 1: GitHub Pages (Free - Recommended)

1. **Create GitHub Repository**
   ```bash
   # Create new repo named "navitraapp.com" on GitHub
   git init
   git add .
   git commit -m "Initial website"
   git remote add origin https://github.com/YOUR_USERNAME/navitraapp.com.git
   git push -u origin main
   ```

2. **Enable GitHub Pages**
   - Go to repo Settings → Pages
   - Source: Deploy from branch
   - Branch: main, / (root)
   - Save

3. **Configure Custom Domain**
   - In GitHub Pages settings, add: `navitraapp.com`
   - Create a file named `CNAME` with content: `navitraapp.com`

4. **DNS Settings (Google Domains)**
   ```
   Type: A
   Host: @
   Value: 185.199.108.153
          185.199.109.153
          185.199.110.153
          185.199.111.153

   Type: CNAME
   Host: www
   Value: YOUR_USERNAME.github.io
   ```

### Option 2: Vercel (Free)

1. **Deploy**
   - Go to vercel.com
   - Import from GitHub or drag & drop folder
   - Click Deploy

2. **Custom Domain**
   - Project Settings → Domains
   - Add: navitraapp.com
   - Follow DNS instructions

### Option 3: Netlify (Free)

1. **Deploy**
   - Go to netlify.com
   - Drag & drop the website folder
   - Or connect to GitHub

2. **Custom Domain**
   - Domain settings → Add domain
   - Follow DNS instructions

---

## 🖼️ Required Images

### 1. favicon.png
- Size: 32x32 or 64x64
- Your Navitra logo icon

### 2. hero-phone.png
- Size: ~350px wide
- iPhone mockup with app screenshot
- Use: https://mockuphone.com or similar

### 3. og-image.png (Social Share)
- Size: 1200x630
- Text: "Navitra - AI Travel Planner"
- Used when sharing on social media

---

## 📝 Checklist Before Launch

- [ ] Update email addresses if different
- [ ] Add actual app screenshot to hero
- [ ] Create and add favicon
- [ ] Create og-image for social sharing
- [ ] Test all links work
- [ ] Test responsive design on mobile
- [ ] Update App Store link when available
- [ ] Set up SSL (automatic on GitHub Pages/Vercel/Netlify)

---

## 🔗 URLs for App Store Connect

After deployment, use these URLs:

| Field | URL |
|-------|-----|
| Marketing URL | https://navitraapp.com |
| Support URL | https://navitraapp.com/support.html |
| Privacy Policy URL | https://navitraapp.com/privacy.html |

---

## ✏️ Customization

### Update Branding
1. Replace logo SVG in `index.html` navigation
2. Update colors in `:root` CSS variables
3. Replace images in `images/` folder

### Update Content
1. Edit descriptions in HTML files
2. Update FAQ answers in `support.html`
3. Modify feature descriptions as needed

---

## 💡 Tips

1. **SSL Certificate**: All platforms above provide free SSL
2. **Caching**: Static sites load very fast
3. **Updates**: Just push to GitHub, auto-deploys
4. **Analytics**: Add Google Analytics later if needed

---

Good luck with your launch! 🚀
