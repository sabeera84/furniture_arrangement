import random
import json
import numpy as np
import matplotlib.pyplot as plt

def generate_room_data(num_samples=10, room_size=(10, 10)):
    furniture_types = [
        {"name": "Bed", "width": 3, "height": 2, "constraint": "Against Wall"},
        {"name": "Table", "width": 2, "height": 2, "constraint": "Not near Bed"},
        {"name": "Chair", "width": 1, "height": 1, "constraint": "Near Table"},
        {"name": "Sofa", "width": 3, "height": 1, "constraint": "Against Wall"},
        {"name": "Shelf", "width": 2, "height": 1, "constraint": "Anywhere"}
    ]
    
    dataset = []
    for _ in range(num_samples):
        room = {"width": room_size[0], "height": room_size[1], "furniture": []}
        num_furniture = random.randint(2, 5)
        selected_furniture = random.sample(furniture_types, num_furniture)
        
        for item in selected_furniture:
            x = random.randint(0, room_size[0] - item["width"])
            y = random.randint(0, room_size[1] - item["height"])
            room["furniture"].append({"name": item["name"], "x": x, "y": y, "width": item["width"], "height": item["height"], "constraint": item["constraint"]})
        
        dataset.append(room)
    
    return dataset

def fitness(layout, room_size):
    score = 0
    occupied = np.zeros(room_size)
    
    for item in layout["furniture"]:
        x, y, w, h = item["x"], item["y"], item["width"], item["height"]
        
        if x + w > room_size[0] or y + h > room_size[1]:
            score -= 10
        
        for i in range(w):
            for j in range(h):
                if occupied[x + i][y + j] == 1:
                    score -= 5
                occupied[x + i][y + j] = 1
        
        if "constraint" in item and item["constraint"] == "Against Wall":
            if x > 0 and x + w < room_size[0]:
                score -= 3
        
    return score

def create_population(size, room_size, num_furniture):
    furniture_types = [
        {"name": "Bed", "width": 3, "height": 2, "constraint": "Against Wall"},
        {"name": "Table", "width": 2, "height": 2, "constraint": "Not near Bed"},
        {"name": "Chair", "width": 1, "height": 1, "constraint": "Near Table"},
    ]
    
    population = []
    for _ in range(size):
        layout = {"width": room_size[0], "height": room_size[1], "furniture": []}
        for _ in range(num_furniture):
            furniture = random.choice(furniture_types)
            x = random.randint(0, room_size[0] - furniture["width"])
            y = random.randint(0, room_size[1] - furniture["height"])
            layout["furniture"].append({
                "name": furniture["name"],
                "x": x,
                "y": y,
                "width": furniture["width"],
                "height": furniture["height"],
                "constraint": furniture["constraint"]
            })
        population.append(layout)
    return population

def crossover(parent1, parent2):
    child = {"width": parent1["width"], "height": parent1["height"], "furniture": []}
    for i in range(len(parent1["furniture"])):
        if random.random() > 0.5:
            child["furniture"].append(parent1["furniture"][i])
        else:
            child["furniture"].append(parent2["furniture"][i])
    return child

def mutate(layout, mutation_rate=0.1):
    for item in layout["furniture"]:
        if random.random() < mutation_rate:
            item["x"] = random.randint(0, layout["width"] - item["width"])
            item["y"] = random.randint(0, layout["height"] - item["height"])
    return layout

def genetic_algorithm(room_size, num_furniture, generations=100, population_size=10):
    population = create_population(population_size, room_size, num_furniture)
    for _ in range(generations):
        population = sorted(population, key=lambda x: fitness(x, room_size), reverse=True)
        new_population = population[:2]
        for _ in range(population_size - 2):
            p1, p2 = random.sample(population[:5], 2)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
    return population[0]

def visualize_layout(layout):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, layout["width"])
    ax.set_ylim(0, layout["height"])
    ax.set_xticks(range(layout["width"] + 1))
    ax.set_yticks(range(layout["height"] + 1))
    ax.grid(True)
    
    for item in layout["furniture"]:
        rect = plt.Rectangle((item["x"], item["y"]), item["width"], item["height"], color='lightblue', edgecolor='black')
        ax.add_patch(rect)
        ax.text(item["x"] + item["width"] / 2, item["y"] + item["height"] / 2, item["name"], ha='center', va='center', fontsize=8, color='black')
    
    plt.title("Optimized Furniture Layout")
    plt.show()

best_layout = genetic_algorithm(room_size=(10, 10), num_furniture=3)
print("Optimized Layout:", json.dumps(best_layout, indent=4))
visualize_layout(best_layout)
