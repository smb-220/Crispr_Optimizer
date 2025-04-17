#!/bin/bash

echo "🚀 Starting CRISPR gRNA Optimizer..."

# Step 1: Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Step 2: Activate it
source venv/bin/activate

# Step 3: Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Step 4: Train model if not exists
if [ ! -f "ai_model/model_weights.pt" ]; then
    echo "🧠 Training model..."
    python ai_model/train.py
else
    echo "✅ Model already trained."
fi

# Step 5: Run the web app
echo "🌐 Launching Web App..."
cd webapp
export PYTHONPATH=$PYTHONPATH:/crispr-optimizer/ai-model/gnn_model.py
streamlit run app.py
