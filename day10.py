import random, math, numpy as np, pandas as pd, copy
r = 24110011661 % 3
def gen(n=10):
    return [{"id":i+1,
             "marks":random.randint(40,100),
             "attendance":random.randint(60,100),
             "scores":[random.randint(10,30),random.randint(10,30)]}
            for i in range(n)]
def mutate(d):
    for i in range(len(d)):
        if i % r == 0:
            d[i]["marks"] += math.sqrt(d[i]["marks"])
            d[i]["attendance"] += 5
            d[i]["scores"][0] += 1
    return d
def manual_mean(d):
    return sum(x["marks"] for x in d)/len(d)
def analyze(o, m):
    om = np.array([x["marks"] for x in o])
    mm = np.array([x["marks"] for x in m])
    drift = abs(np.mean(om) - np.mean(mm))
    std = np.std(mm)
    norm = (mm - mm.min())/(mm.max()-mm.min())
    return np.mean(mm), drift, std, norm
def detect(o, d, drift, t=5):
    if any(o[i]["scores"] != d[i]["scores"] for i in range(len(o))):
        return "Copy Failure Detected"
    if drift > t: return "Critical Drift"
    if drift > 0: return "Minor Drift"
    return "Stable Data"
data = gen()
s = copy.copy(data)
d = copy.deepcopy(data)
mutate(s)
mutate(d)
odf = pd.DataFrame(data)
sdf = pd.DataFrame(s)
ddf = pd.DataFrame(d)
mean, drift, std, norm = analyze(data, d)
print(odf)
print(sdf)
print(ddf)
print("Drift:", drift)
print("Tuple:", (mean, drift, std))
print("Manual Mean:", manual_mean(data))
print("Result:", detect(data, d, drift))