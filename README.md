# 🇻🇳 Hệ thống Multi-Agent Viet Nam Stock

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![Gemini](https://img.shields.io/badge/Google-Gemini-orange.svg)](https://ai.google.dev)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.117+-purple.svg)](https://crewai.com)

> **Hệ thống phân tích đầu tư chứng khoán thông minh với 6 AI Agents + Gemini AI + CrewAI + LSTM Neural Network**

---

**👤 Thành viên chính:**  
- **Nguyễn Minh Dương**  
- **Mã sinh viên:** 23010441  
- **Lớp:** Phân tích và thiết kế phần mềm (N05)  
- **Nhóm:** 11

---

## 🎯 Tổng quan

**Hệ thống Multi-Agent Viet Nam Stock** là hệ thống phân tích đầu tư chứng khoán hoàn chỉnh, tích hợp 6 AI Agents chuyên nghiệp, Gemini AI, và mạng neural LSTM để cung cấp phân tích toàn diện cho thị trường chứng khoán Việt Nam và quốc tế.

### ✨ Tính năng nổi bật

- 🤖 **6 AI Agents chuyên nghiệp** với phân tích cá nhân hóa
- 🧠 **Gemini AI Chatbot** với khả năng offline fallback
- 🔮 **LSTM Neural Network** cho dự đoán giá nâng cao
- 📊 **Dữ liệu real-time** từ VNStock API và CrewAI
- 🚀 **FastAPI Backend** + **Streamlit Frontend** với 6 tabs chuyên nghiệp
- 📈 **Phân tích kỹ thuật & cơ bản** với số liệu chính xác
- ⚙️ **Cài đặt đầu tư cá nhân** (thời gian + mức độ rủi ro)
- 🎨 **Giao diện đẹp mắt** với Bootstrap integration

## 🤖 Đội ngũ 6 AI Agents

| Agent | Chức năng | Mô tả | Tính năng đặc biệt |
|-------|-----------|-------|-------------------|
| 📈 **PricePredictor** | Dự đoán giá | LSTM + Technical Analysis cho dự báo giá | LSTM Neural Network, Multi-timeframe |
| 💼 **InvestmentExpert** | Chuyên gia đầu tư | Phân tích cơ bản và khuyến nghị BUY/SELL/HOLD | Real financial ratios, AI-enhanced |
| ⚠️ **RiskExpert** | Quản lý rủi ro | Đánh giá rủi ro với VaR, Beta, Sharpe ratio | Advanced risk metrics, AI advice |
| 📰 **TickerNews** | Tin tức cổ phiếu | Crawl tin tức từ CafeF, VietStock | Multi-source crawling, Sentiment analysis |
| 🌍 **MarketNews** | Tin tức thị trường | Risk-based news filtering | Underground news, Risk-adjusted content |
| 🏢 **StockInfo** | Thông tin chi tiết | Hiển thị metrics và charts chuyên nghiệp | Real-time data, Interactive charts |

## 🏗️ Kiến trúc hệ thống

```
agentvnstock/
├── agents/
│   ├── price_predictor.py
│   ├── lstm_price_predictor.py
│   ├── investment_expert.py
│   ├── risk_expert.py
│   ├── ticker_news.py
│   ├── market_news.py
│   ├── stock_info.py
│   └── risk_based_news.py
├── src/
│   ├── data/
│   │   ├── vn_stock_api.py
│   │   ├── crewai_collector.py
│   │   └── company_search_api.py
│   ├── ui/
│   │   ├── styles.py
│   │   └── components.py
│   └── utils/
│       ├── error_handler.py
│       ├── market_schedule.py
│       ├── performance_monitor.py
│       └── security_manager.py
├── deep-learning/
│   ├── 1.lstm.ipynb
│   ├── 16.attention-is-all-you-need.ipynb
│   └── [18 Jupyter notebooks]
├── static/
│   ├── index.html
│   ├── script.js
│   └── styles.css
├── gemini_agent.py
├── main_agent.py
├── api.py
└── app.py
```

## 📱 Giao diện 6 Tabs chuyên nghiệp

- **Phân tích cổ phiếu:** 6 agents + LSTM, dự đoán giá, phân tích đầu tư, đánh giá rủi ro
- **AI Chatbot:** Gemini AI, offline fallback, gợi ý câu hỏi, phản hồi thông minh
- **Thị trường VN:** VN-Index real-time, top movers, 37+ cổ phiếu, market overview
- **Tin tức cổ phiếu:** Multi-source crawling, AI sentiment analysis, priority highlighting
- **Thông tin công ty:** Company overview, financial metrics, interactive charts
- **Tin tức thị trường:** Risk-based filtering, underground news, official news, smart categorization

## 🧠 LSTM Neural Network

- 18 mô hình ML: LSTM, GRU, Transformer, CNN...
- Multi-timeframe prediction: 1 ngày đến 1 năm
- Confidence scoring, AI enhancement, real-time training

## 📊 Cổ phiếu được hỗ trợ

### 🏦 Ngân hàng (7 mã)
**VCB** • **BID** • **CTG** • **TCB** • **ACB** • **MBB** • **VPB**

### 🏢 Bất động sản (5 mã)
**VIC** • **VHM** • **VRE** • **DXG** • **NVL**

### 🛒 Tiêu dùng (5 mã)
**MSN** • **MWG** • **VNM** • **SAB** • **PNJ**

### 🏭 Công nghiệp (3 mã)
**HPG** • **HSG** • **NKG**

### ⚡ Tiện ích (3 mã)
**GAS** • **PLX** • **POW**

### 💻 Công nghệ (2 mã)
**FPT** • **CMG**

### 🚁 Vận tải (2 mã)
**VJC** • **HVN**

### 💊 Y tế (2 mã)
**DHG** • **IMP**

**Tổng cộng: 37+ cổ phiếu VN**