from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# ——— 1. LOAD & PARSE YOUR DATAFILE ———
df = pd.read_csv(
    'Measurment.txt',
    sep='\t',
    engine='python',
    encoding='latin1',
    on_bad_lines='warn'
)
df.columns = [c.strip() for c in df.columns]

# The seven channels (which may be strings like "12.34dB,°")
raw_cols = [
    'V(curr_measur_1)',
    'V(curr_measur_2)',
    'V(curr_measur_3)',
    'V(volt_measur_1)',
    'V(volt_measur_2)',
    'V(volt_measur_3)',
    'V(volt_measur_4)',
]

# ——— 2. CLEAN & CONVERT TO FLOAT ———
# Extract the first signed decimal number from each string; coerce errors to NaN.
for col in raw_cols:
    df[col] = (
        df[col]
          .astype(str)
          .str.extract(r'([-+]?\d*\.?\d+)')[0]
          .astype(float)
    )

# ——— 3. COMPUTE IMPEDANCE ———
# R = V(volt_measur_4) / V(curr_measur_3) / 100
df['Impedance'] = df['V(volt_measur_4)'] / df['V(curr_measur_3)'] / 100

# ——— 4. FLASK ROUTES ———
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    payload = {'idx': df.index.tolist()}
    # seven cleaned channels
    for i, col in enumerate(raw_cols, start=1):
        payload[f'chan{i}'] = df[col].tolist()
    # impedance as the 8th series
    payload['chan8'] = df['Impedance'].tolist()
    return jsonify(payload)

if __name__ == '__main__':
    app.run(debug=True)
