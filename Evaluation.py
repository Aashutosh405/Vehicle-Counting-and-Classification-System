# Ground truth (manually counted vehicles moving up and down)
true_vehicles = {
    "Up": 55,
    "Down": 43
}

# Predicted counts from the system
predicted_vehicles = {
    "Up": 39,  
    "Down": 26
}

# Total vehicle movements in ground truth
total_movements = sum(true_vehicles.values())

def calculate_metrics(true_count, predicted_count, total_movements):
    # True Positives (minimum of true and predicted counts)
    tp = min(true_count, predicted_count)
    
    # False Positives: Detected but not in the ground truth
    fp = max(0, predicted_count - true_count)
    
    # False Negatives: In the ground truth but missed by the system
    fn = max(0, true_count - predicted_count)
    
    # True Negatives: Total possible events minus all detections (TP, FP, FN)
    tn = total_movements - (tp + fp + fn)
    
    # Precision and Accuracy
    precision = tp / (tp + fn) if (tp + fn) > 0 else 0
    accuracy = (tp + tn) / total_movements if total_movements > 0 else 0
    
    return {
        "Recall": precision,
        "Accuracy": accuracy
    }

for vehicle_direction in true_vehicles.keys():
    print(f"Metrics for vehicles moving {vehicle_direction}:")
    metrics = calculate_metrics(true_vehicles[vehicle_direction], predicted_vehicles[vehicle_direction], total_movements)
    print(f"Precision: {metrics['Recall']:.2f}")
    print(f"Accuracy: {metrics['Accuracy']:.2f}")
    print("\n")
