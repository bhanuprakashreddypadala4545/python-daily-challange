import random
import math
import pandas as pd
import numpy as np

def generate_data(n):
    records = []
    i = 1
    while i <= n:
        m = random.randint(0, 100)
        a = random.randint(0, 100)
        ass = random.randint(0, 50)
        pi = (m * 0.6 + ass * 0.4) * math.log(a + 1)
        records.append((i, m, a, ass, pi))
        i += 1
    return records
def classify_students(data):
    d = {}
    for x in data:
        sid, m, a, ass, pi = x
        if m < 40 or a < 50:
            d[sid] = "At Risk"
        elif m > 90 and a > 80:
            d[sid] = "Top Performer"
        elif m >= 71:
            d[sid] = "Good"
        else:
            d[sid] = "Average"
    return d

def analyze_data(data, cat):
    df = pd.DataFrame(data, columns=["ID", "Marks", "Attendance", "Assign", "PI"])
    marks = df["Marks"].values
    total = 0
    for v in marks:
        total += v
    mean = total / len(marks)
    med = np.median(marks)
    sd = np.std(marks)
    c = np.corrcoef(df["Marks"], df["Attendance"])[0][1]
    mn = np.min(marks)
    mx = np.max(marks)
    df["Norm"] = [(x - mn) / (mx - mn) if mx != mn else 0 for x in marks]
    s = set(cat.values())
    low_att = 0
    for v in df["Attendance"]:
        if v < 50:
            low_att += 1
    high = 0
    for v in df["Marks"]:
        if v > 90:
            high += 1
    cons = sd < 15
    if cons and low_att <= 3:
        res = "Stable Academic System"
    elif high >= 2:
        res = "Moderate Performance"
    else:
        res = "Critical Attention Required"
    t = (mean, sd, mx)
    return df, med, c, t, res, s


n = 6
data = generate_data(n)
cat = classify_students(data)
df, med, corr, tup, ins, st = analyze_data(data, cat)
print(df)
print(cat)
print(st)
print(med)
print(corr)
print(tup)
print(ins)