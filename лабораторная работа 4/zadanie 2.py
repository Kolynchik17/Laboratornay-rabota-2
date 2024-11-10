# TODO решите задачу
def task() -> float:
    sum =0
    import json
    with open('input.json') as f:
        sl = json.load(f)
        for i in range (len(sl)):
            sum=sum+sl[i]['score']*sl[i]['weight']
    return round(sum, 3)

print(task())
