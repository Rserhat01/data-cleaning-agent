# 🧹 AI-Powered CSV Cleaner

A lightweight Flask web application that leverages OpenAI's GPT to suggest and apply basic data cleaning operations on CSV files.

## ✨ Features

- 📁 Upload your own CSV dataset  
- 🧠 Get AI-generated cleaning suggestions (missing values, outliers, etc.)  
- 🧼 Apply basic cleaning: fill missing numeric values with column mean  
- ⬇️ Download the cleaned dataset  

## 🚀 How It Works

1. Upload a CSV file
2. Click **"Get Cleaning Suggestions"** to receive AI-based insights
3. Click **"Clean Based on Suggestion"** to apply simple fixes
4. Download the cleaned CSV file

## 📦 Tech Stack

- Python 3.9+
- Flask
- Pandas
- OpenAI API (GPT-4o-mini)
- HTML + Bootstrap (for UI)

## 🔐 Environment Variables

Create a `.env` file in the project root with your OpenAI API key:

```env
OPENAI_API_KEY=your-api-key-here


