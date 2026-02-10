# AI TikTok Automation Project

This project generates Tech/AI educational videos automatically using AI tools and uploads them to TikTok.

## Features
- AI script generation
- AI voice narration
- AI video creation
- Automated upload workflow

## Tech Stack
- Python
- GitHub
- AI APIs

# AI TikTok Automation

# 📚 AI TikTok Automation Documentation (Learning Note)

ဒီကို README.md ထဲတင်လို့ရတယ်။

---

## 🎬 Project Name

AI TikTok Automation (Faceless Tech Channel)

---

## 🎯 Goal

Fully automated viral TikTok content system

Pipeline:

```
Topic → AI Script → AI Voice → Auto VisualVideo → TikTok Upload (future)
```

---

## 🧠 APIs Used

### 1️⃣ Groq API

Used for:

- Script generation

Model:

```
llama-3.3-70b-versatile
```

---

### 2️⃣ Pexels API

Used for:

- Stock tech images / videos
- Visual slideshow generation

---

### 3️⃣ TTS Engine

Used for:

- Female narration voice
- Script → Voice conversion

---

## ⚙️ Environment Configuration

`.env`

```
GROQ_API_KEY=your_key_herePEXELS_API_KEY=your_key_hereGROQ_MODEL=llama-3.3-70b-versatile
```

---

## 📁 Project Structure

```
src/
 ├──main.py
 ├── generate_script.py
 ├── tts_generator.py
 ├── video_generator.py
 └── fetch_pexels.py

assets/
 ├── images/
 ├── gifs/
 └──audio/

output/
 └── final videos
```

---

## 🔄 Automation Flow

### Step 1 — Script Generation

File:

```
generate_script.py
```

Function:

```
generate_script(topic)
```

Uses Groq AI to create viral TikTok narration.

---

### Step 2 — Voice Generation

File:

```
tts_generator.py
```

Function:

```
generate_voice(script)
```

Output:

```
voice.mp3
```

---

### Step 3 — Visual Fetching

File:

```
fetch_pexels.py
```

Function:

```
fetch_tech_visuals(topic)
```

Downloads tech-related visuals.

---

### Step 4 — Video Generation

File:

```
video_generator.py
```

Function:

```
generate_video(voice_file)
```

Responsibilities:

- Sync visuals with narration
- Add slideshow transitions
- Combine audio + video

---

### Step 5 — Main Controller

File:

```
main.py
```

Pipeline runner.

```
Topicinput
→ Script
→ Voice
→Video output
```

---

## 🐞 Issues Fixed During Development

### ❌ Old OpenAI API removed

✔ Migrated to Groq

---

### ❌ MoviePy import error

✔ Correct import path fixed

---

### ❌ GIF loop / black screen issue

✔ Video clip duration synced with audio

---

### ❌ Groq model decommission

✔ Updated to:

```
llama-3.3-70b-versatile
```

---

## 🔮 Future Upgrades

- Auto subtitle generation
- Smart scene detection
- TikTok auto uploader
- Viral editing effects
- Multi-language narration
- Background music AI selection

---

## 💰 Monetization Plan

- TikTok Creator Program
- Affiliate tech reviews
- AI tool promotions
- Sponsored content

---

# ⭐ Current Version Status

```
Version:v1PrototypeStatus:StableAutomation Level:70%
```

---

# 🧩 Learning Outcome

- Groq AI integration
- API environment management
- MoviePy automation editing
- AI content pipeline design
- DevOps style automation mindset
