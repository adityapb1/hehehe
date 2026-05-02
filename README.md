# 💖 For Priyanka — A Special Little App

A personal, password-protected Streamlit app made with love.

---

## 📁 Files to Upload on GitHub

Upload these **exact files** to your GitHub repo:

```
your-repo/
├── app.py               ← main app
├── data.json            ← all your content (auto-saves edits)
├── requirements.txt     ← dependencies
└── .streamlit/
    └── config.toml      ← pink theme settings
```

> ⚠️ Make sure the `.streamlit/` folder is included — GitHub sometimes hides dot-folders. Enable "Show hidden files" if needed.

---

## 🚀 How to Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click **"New app"**
4. Select your repo, branch (`main`), and set **Main file path** to `app.py`
5. Click **Deploy** 🎉

Your app will be live at:
`https://your-username-your-repo-name.streamlit.app`

---

## 🔑 Passwords

| Who         | Password   | What they see              |
|-------------|------------|----------------------------|
| Priyanka    | `im@motu`  | Full app — home, quiz, etc |
| Adi (you)   | `im@adi`   | Admin panel to edit everything |

---

## ✏️ How to Edit Content (as Adi)

1. Open the app
2. Enter password: `im@adi`
3. You'll see the **Admin Panel** with tabs:
   - 🔑 Passwords — change Priyanka's password
   - 🌸 Timeline — add/edit/remove story events (wedding etc.)
   - 💌 Message — edit the heartfelt letter
   - 🧠 Quiz — edit questions, answers, pass score & messages
   - 💆 Mood — edit sad/angry/stress responses
   - 🎁 Surprise — edit the surprise message
   - 📝 General — name, subtitle, footer

> **Note:** On Streamlit Cloud, edits to `data.json` won't persist between app restarts (cloud storage resets). For permanent edits, update `data.json` in your GitHub repo directly, or use the admin panel + commit the updated file.

---

## 🌟 Features

- 🔒 Password-protected entry with pink animated screen
- 💖 Pink heart animated background throughout
- 🧭 Beautiful nav bar — Home, Our Story, Letter, Mood, Quiz, Surprise, Dev
- 🌸 **Timeline** with wedding entry (gold glowing dot for future events!)
- 💌 **Heartfelt letter** — full editable message
- 💆 **Mood booster** — sad / angry / study stress responses
- 🧠 **Quiz** — 10 questions, custom pass score, encouraging low-score message
- 🎁 **Surprise** page with balloons
- 🫣 **Dev/Admin page** (Adi only) — edit everything page by page
- 📱 Mobile friendly
- 🎨 Playfair Display + Nunito fonts, deep pink palette

---

## 💡 Tips

- To add a **wedding** event with gold glow: make sure the date says "Coming Soon" or the title has 💍
- Quiz low score message now says **"Ik u know me — try again!"** with a retry button
- Pass screen is **pink and animated** with hearts when Priyanka logs in

---

Made with 💖 by Adi — sirf Priyanka ke liye 🌸
