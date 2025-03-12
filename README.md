# 🏠 AI-Powered Furniture Layout Optimization  

This project uses **Genetic Algorithms (GA)** to optimize furniture arrangement within a given room space. The goal is to generate an **optimal layout** based on constraints such as wall placement, distance rules, and object collisions.  

## 🚀 Features  
- **FastAPI Backend** to generate optimized layouts  
- **Genetic Algorithm (GA)** for layout optimization  
- **Matplotlib Visualization** for layout display  
- **UI Component** (WIP) for user interaction  

## 📁 Project Structure  
```
📂 Project Root
 ├── app.py                 # FastAPI backend
 ├── dataset_GA_visual.py   # GA-based dataset generation & visualization
 ├── ui.py                  # UI logic (if applicable)
 ├── README.md              # Project documentation
```

## 🛠 Installation & Usage  
1️⃣ **Clone the repository:**  
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```
  
2️⃣ **Install dependencies:**  
```bash
pip install fastapi uvicorn numpy matplotlib
```
  
3️⃣ **Run the API server:**  
```bash
uvicorn app:app --reload
```
  
4️⃣ **Test the API:**  
Open **Postman** or use **cURL**:  
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/optimize' \
  -H 'Content-Type: application/json' \
  -d '{"width": 10, "height": 10, "num_furniture": 3}'
```

## 📊 Visualization  
The optimized layout is displayed using **Matplotlib**. It shows room dimensions and furniture placements based on the GA-generated best configuration.

## 🎯 Next Steps  
✅ Improve UI for interactive input  
✅ Enhance GA scoring for better furniture placement  
✅ Integrate real-world datasets  

