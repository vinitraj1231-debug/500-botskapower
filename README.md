# 🚀 Highly Advanced Multi-Functional Telegram Bot

This bot is a powerhouse with 500+ features, including an advanced music player, bot cloning system, group management, and 50+ interactive games.

## ✨ Key Features

- 🎵 **Advanced Music Bot:** Play songs on Voice Chat (VC) with high quality and no lag.
- 🤖 **Cloning Feature:** Users can create their own child bots using a bot token.
- 🎮 **50+ Games:** Dice, Slots, Darts, Football, Quizzes, Guessing games, and more.
- 🛡️ **Group Management:** Welcome messages, Anti-link, Rules, Ban, Kick, Mute.
- 🛠️ **Modular Plugin System:** Easily add or remove features.
- ⚡ **Highly Optimized:** Completely asynchronous for maximum speed and zero lag.

---

## 🚀 Deployment Guide

### 1. VPS / Dedicated Server (Recommended)
1. **Update System:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```
2. **Install Dependencies:**
   ```bash
   sudo apt install python3-pip ffmpeg -y
   ```
3. **Clone Repo:**
   ```bash
   git clone https://github.com/yourusername/advanced-bot.git
   cd advanced-bot
   ```
4. **Install Requirements:**
   ```bash
   pip3 install -r requirements.txt
   ```
5. **Configure Environment:**
   Create a `.env` file:
   ```env
   API_ID=your_api_id
   API_HASH=your_api_hash
   BOT_TOKEN=your_bot_token
   MONGO_URL=your_mongodb_url (optional)
   OWNER_ID=your_id
   ```
6. **Run the Bot:**
   ```bash
   python3 main.py
   ```

### 2. Docker Deployment
1. **Build Image:**
   ```bash
   docker build -t advanced-bot .
   ```
2. **Run Container:**
   ```bash
   docker run -d --env-file .env advanced-bot
   ```

### 3. Heroku
1. Click the **Deploy to Heroku** button (if available) or use Heroku CLI.
2. Add `ffmpeg` buildpack.
3. Set all `Config Vars` in Heroku Dashboard.

---

## 🛠️ Commands List

- `/start` - Start the bot
- `/help` - Show all categories
- `/play <song>` - Play music on VC
- `/clone <token>` - Create a child bot
- `/dice` - Roll a dice
- `/quiz` - Start a quiz
- `/ban` - Ban a user (Reply)

---

## 🤝 Support
Contact the owner for any issues.
