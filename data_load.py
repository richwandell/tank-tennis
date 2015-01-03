import json
level = [{
    "ConcreteSlabDarkTop": {
        "speed": 0.8,
        "coords": []
    },
    "ConcreteSlab": {
        "speed": 0.8,
        "coords": []
    },
    "ConcreteSlab2": {
        "speed": 0.8,
        "coords": []
    }
}]

for x in range(1000):
    if x > 10 and x < 15:
        level[0]["ConcreteSlab"]["coords"].append([1 + x*.05, 0.85])
        
    if x >= 15 and x < 20:
        level[0]["ConcreteSlab"]["coords"].append([1 + x*.05, 0.90])
        
    if x > 22 and x < 30:
        level[0]["ConcreteSlab"]["coords"].append([1 + x*.05, 0.90])
        
    if x > 25 and x < 30:
        level[0]["ConcreteSlab"]["coords"].append([1 + x*.05, 0.85])
        level[0]["ConcreteSlab2"]["coords"].append([1 + x*.05, 0.80])
    
    if x > 32 and x < 35:
        level[0]["ConcreteSlab2"]["coords"].append([1 + x*.05, 0.80])
    
    if x <= 30:
        level[0]["ConcreteSlab"]["coords"].append([x*.05, 0.99])
    
    if (x > 30 and x < 50) or (x > 55 and x < 75) or (x > 77 and x < 95):
        level[0]["ConcreteSlabDarkTop"]["coords"].append([x*.05, 0.99])
    
    level[0]["ConcreteSlab"]["coords"].append([x*.05, 0.01])
    
open("levels/level1.json", "w").writelines(json.dumps(level))