#!/usr/bin/env python3
"""
ML Research Visualizations Generator
Generates 19 professional charts for machine learning model evaluation and analysis
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc, precision_recall_curve
from sklearn.preprocessing import StandardScaler
import warnings
import os

warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

# Create output directory
output_dir = os.path.dirname(os.path.abspath(__file__))

# Generate synthetic data for demonstrations
np.random.seed(42)

print("Starting ML Research Visualizations Generation...")
print("=" * 60)

# ========================
# 1. MODEL EVALUATION CHARTS (4)
# ========================

# Chart 1: ROC Curve (Multi-class)
print("Generating Chart 1: ROC Curve (Multi-class)...")
n_classes = 3
y_true = np.random.randint(0, n_classes, 200)
y_scores = np.random.rand(200, n_classes)

fig, ax = plt.subplots(figsize=(10, 8))
colors = ['blue', 'red', 'green']
for i, color in enumerate(colors):
    fpr, tpr, _ = roc_curve((y_true == i).astype(int), y_scores[:, i])
    roc_auc = auc(fpr, tpr)
    ax.plot(fpr, tpr, color=color, lw=2.5, label=f'Class {i} (AUC = {roc_auc:.3f})')
ax.plot([0, 1], [0, 1], 'k--', lw=2)
ax.set_xlabel('False Positive Rate', fontsize=12, fontweight='bold')
ax.set_ylabel('True Positive Rate', fontsize=12, fontweight='bold')
ax.set_title('ROC Curve - Multi-class Classification', fontsize=14, fontweight='bold')
ax.legend(loc='lower right', fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '01_roc_curve_multiclass.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 1 saved: 01_roc_curve_multiclass.png")

# Chart 2: Confusion Matrix Heatmap
print("Generating Chart 2: Confusion Matrix Heatmap...")
y_true_multi = np.random.randint(0, 4, 200)
y_pred_multi = np.random.randint(0, 4, 200)
cm = confusion_matrix(y_true_multi, y_pred_multi)

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar_kws={'label': 'Count'}, ax=ax)
ax.set_xlabel('Predicted Label', fontsize=12, fontweight='bold')
ax.set_ylabel('True Label', fontsize=12, fontweight='bold')
ax.set_title('Confusion Matrix - Multi-class Classifier', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '02_confusion_matrix.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 2 saved: 02_confusion_matrix.png")

# Chart 3: Feature Importance (Top 15)
print("Generating Chart 3: Feature Importance (Top 15)...")
feature_names = [f'Feature_{i}' for i in range(1, 31)]
importances = np.abs(np.random.randn(30))
importances = importances / importances.sum()
top_indices = np.argsort(importances)[-15:]
top_features = [feature_names[i] for i in top_indices]
top_importances = importances[top_indices]

fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.barh(range(len(top_features)), top_importances, color=plt.cm.viridis(np.linspace(0, 1, len(top_features))))
ax.set_yticks(range(len(top_features)))
ax.set_yticklabels(top_features, fontsize=10)
ax.set_xlabel('Importance Score', fontsize=12, fontweight='bold')
ax.set_title('Feature Importance - Top 15 Features', fontsize=14, fontweight='bold')
for i, (bar, importance) in enumerate(zip(bars, top_importances)):
    ax.text(importance, i, f' {importance:.4f}', va='center', fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '03_feature_importance.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 3 saved: 03_feature_importance.png")

# Chart 4: Precision-Recall Curve
print("Generating Chart 4: Precision-Recall Curve...")
y_true_binary = np.random.randint(0, 2, 200)
y_scores_binary = np.random.rand(200)

fig, ax = plt.subplots(figsize=(10, 8))
for i in range(3):
    precision, recall, _ = precision_recall_curve(y_true_binary, np.random.rand(200))
    avg_precision = np.mean(precision)
    ax.plot(recall, precision, linewidth=2.5, label=f'Model {i+1} (AP = {avg_precision:.3f})')
ax.set_xlabel('Recall', fontsize=12, fontweight='bold')
ax.set_ylabel('Precision', fontsize=12, fontweight='bold')
ax.set_title('Precision-Recall Curve - Binary Classification', fontsize=14, fontweight='bold')
ax.legend(loc='best', fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '04_precision_recall_curve.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 4 saved: 04_precision_recall_curve.png")

# ========================
# 2. PERFORMANCE COMPARISON CHARTS (4)
# ========================

# Chart 5: Model Performance Comparison (Bar Chart)
print("Generating Chart 5: Model Performance Comparison...")
models = ['Model A', 'Model B', 'Model C', 'Model D', 'Model E']
accuracy = [0.92, 0.88, 0.95, 0.87, 0.91]
precision = [0.90, 0.86, 0.93, 0.85, 0.89]
recall = [0.89, 0.87, 0.96, 0.88, 0.92]

fig, ax = plt.subplots(figsize=(12, 7))
x = np.arange(len(models))
width = 0.25
bars1 = ax.bar(x - width, accuracy, width, label='Accuracy', color='#2E86AB')
bars2 = ax.bar(x, precision, width, label='Precision', color='#A23B72')
bars3 = ax.bar(x + width, recall, width, label='Recall', color='#F18F01')

ax.set_ylabel('Score', fontsize=12, fontweight='bold')
ax.set_xlabel('Models', fontsize=12, fontweight='bold')
ax.set_title('Model Performance Comparison', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend(fontsize=11)
ax.set_ylim([0.8, 1.0])

# Add value labels
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, '05_model_performance_comparison.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 5 saved: 05_model_performance_comparison.png")

# Chart 6: Training vs Validation Loss
print("Generating Chart 6: Training vs Validation Loss...")
epochs = np.arange(1, 101)
train_loss = 0.5 * np.exp(-epochs/20) + 0.05 * np.random.rand(100)
val_loss = 0.5 * np.exp(-epochs/20) + 0.08 * np.random.rand(100)

fig, ax = plt.subplots(figsize=(12, 7))
ax.plot(epochs, train_loss, linewidth=2.5, label='Training Loss', color='#2E86AB', marker='o', markersize=4, markevery=10)
ax.plot(epochs, val_loss, linewidth=2.5, label='Validation Loss', color='#F18F01', marker='s', markersize=4, markevery=10)
ax.set_xlabel('Epoch', fontsize=12, fontweight='bold')
ax.set_ylabel('Loss', fontsize=12, fontweight='bold')
ax.set_title('Training vs Validation Loss Over Epochs', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '06_training_validation_loss.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 6 saved: 06_training_validation_loss.png")

# Chart 7: F1-Score Across Thresholds
print("Generating Chart 7: F1-Score Across Thresholds...")
thresholds = np.linspace(0, 1, 50)
f1_scores = []
for threshold in thresholds:
    tp = np.sum((y_scores_binary >= threshold) & (y_true_binary == 1))
    fp = np.sum((y_scores_binary >= threshold) & (y_true_binary == 0))
    fn = np.sum((y_scores_binary < threshold) & (y_true_binary == 1))
    if tp + fp + fn > 0:
        precision_t = tp / (tp + fp) if tp + fp > 0 else 0
        recall_t = tp / (tp + fn) if tp + fn > 0 else 0
        f1 = 2 * (precision_t * recall_t) / (precision_t + recall_t) if precision_t + recall_t > 0 else 0
        f1_scores.append(f1)
    else:
        f1_scores.append(0)

fig, ax = plt.subplots(figsize=(12, 7))
ax.plot(thresholds, f1_scores, linewidth=2.5, color='#2E86AB', marker='o', markersize=5, markevery=5)
optimal_idx = np.argmax(f1_scores)
ax.scatter([thresholds[optimal_idx]], [f1_scores[optimal_idx]], color='red', s=200, zorder=5, label=f'Optimal (Threshold={thresholds[optimal_idx]:.3f})')
ax.set_xlabel('Decision Threshold', fontsize=12, fontweight='bold')
ax.set_ylabel('F1-Score', fontsize=12, fontweight='bold')
ax.set_title('F1-Score vs Decision Threshold', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '07_f1_score_threshold.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 7 saved: 07_f1_score_threshold.png")

# Chart 8: Fairness Across Demographics
print("Generating Chart 8: Fairness Across Demographics...")
demographics = ['Group A', 'Group B', 'Group C', 'Group D']
fairness_scores = [0.85, 0.82, 0.88, 0.80]
disparate_impact = [1.2, 0.95, 1.1, 0.98]

fig, ax1 = plt.subplots(figsize=(12, 7))
color1 = '#2E86AB'
ax1.bar(demographics, fairness_scores, color=color1, alpha=0.7, label='Fairness Score')
ax1.set_ylabel('Fairness Score', fontsize=12, fontweight='bold', color=color1)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_ylim([0.7, 1.0])

ax2 = ax1.twinx()
color2 = '#F18F01'
ax2.plot(demographics, disparate_impact, color=color2, marker='o', markersize=10, linewidth=2.5, label='Disparate Impact')
ax2.set_ylabel('Disparate Impact Ratio', fontsize=12, fontweight='bold', color=color2)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.axhline(y=1.0, color='red', linestyle='--', linewidth=2, alpha=0.5, label='Parity Line')

fig.suptitle('Fairness Analysis Across Demographics', fontsize=14, fontweight='bold')
fig.tight_layout()
plt.savefig(os.path.join(output_dir, '08_fairness_demographics.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 8 saved: 08_fairness_demographics.png")

# ========================
# 3. SYSTEM PERFORMANCE CHARTS (3)
# ========================

# Chart 9: Inference Latency Distribution
print("Generating Chart 9: Inference Latency Distribution...")
latencies = np.random.gamma(shape=2, scale=10, size=1000)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
ax1.hist(latencies, bins=40, color='#2E86AB', edgecolor='black', alpha=0.7)
ax1.axvline(np.mean(latencies), color='red', linestyle='--', linewidth=2, label=f'Mean: {np.mean(latencies):.2f}ms')
ax1.axvline(np.median(latencies), color='green', linestyle='--', linewidth=2, label=f'Median: {np.median(latencies):.2f}ms')
ax1.set_xlabel('Latency (ms)', fontsize=11, fontweight='bold')
ax1.set_ylabel('Frequency', fontsize=11, fontweight='bold')
ax1.set_title('Histogram of Inference Latencies', fontsize=12, fontweight='bold')
ax1.legend()

ax2.boxplot(latencies, vert=True)
ax2.set_ylabel('Latency (ms)', fontsize=11, fontweight='bold')
ax2.set_title('Box Plot of Inference Latencies', fontsize=12, fontweight='bold')

fig.suptitle('Inference Latency Distribution Analysis', fontsize=14, fontweight='bold')
fig.tight_layout()
plt.savefig(os.path.join(output_dir, '09_latency_distribution.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 9 saved: 09_latency_distribution.png")

# Chart 10: Memory Usage Over Time
print("Generating Chart 10: Memory Usage Over Time...")
time_steps = np.arange(0, 300, 5)
memory_cpu = 1024 + 50 * np.sin(time_steps/50) + 20 * np.random.rand(len(time_steps))
memory_gpu = 4096 + 200 * np.sin(time_steps/60) + 100 * np.random.rand(len(time_steps))

fig, ax = plt.subplots(figsize=(12, 7))
ax.fill_between(time_steps, memory_cpu, alpha=0.5, color='#2E86AB', label='CPU Memory')
ax.fill_between(time_steps, memory_gpu, alpha=0.5, color='#F18F01', label='GPU Memory')
ax.plot(time_steps, memory_cpu, color='#2E86AB', linewidth=2.5)
ax.plot(time_steps, memory_gpu, color='#F18F01', linewidth=2.5)
ax.set_xlabel('Time (seconds)', fontsize=12, fontweight='bold')
ax.set_ylabel('Memory Usage (MB)', fontsize=12, fontweight='bold')
ax.set_title('Memory Usage Over Inference Time', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '10_memory_usage.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 10 saved: 10_memory_usage.png")

# Chart 11: GPU Utilization Heatmap
print("Generating Chart 11: GPU Utilization Heatmap...")
hours = np.arange(24)
gpu_cores = np.arange(8)
utilization = np.random.rand(8, 24) * 100

fig, ax = plt.subplots(figsize=(14, 6))
im = ax.imshow(utilization, cmap='RdYlGn', aspect='auto')
ax.set_xlabel('Hour of Day', fontsize=11, fontweight='bold')
ax.set_ylabel('GPU Core', fontsize=11, fontweight='bold')
ax.set_xticks(hours)
ax.set_yticks(gpu_cores)
ax.set_title('GPU Core Utilization Heatmap (24-hour Period)', fontsize=14, fontweight='bold')
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Utilization (%)', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '11_gpu_utilization_heatmap.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 11 saved: 11_gpu_utilization_heatmap.png")

# ========================
# 4. ANOMALY DETECTION CHARTS (3)
# ========================

# Chart 12: Anomaly Detection - Isolation Forest Results
print("Generating Chart 12: Anomaly Detection Scatter Plot...")
normal_data = np.random.randn(150, 2) * 2
anomaly_data = np.random.randn(10, 2) * 5 + 8
data = np.vstack([normal_data, anomaly_data])
labels = np.hstack([np.zeros(150), np.ones(10)])

fig, ax = plt.subplots(figsize=(11, 9))
scatter1 = ax.scatter(data[labels == 0, 0], data[labels == 0, 1], c='#2E86AB', s=50, alpha=0.6, label='Normal', edgecolors='navy')
scatter2 = ax.scatter(data[labels == 1, 0], data[labels == 1, 1], c='#F18F01', s=200, alpha=0.8, marker='X', label='Anomaly', edgecolors='red')
ax.set_xlabel('Feature 1', fontsize=12, fontweight='bold')
ax.set_ylabel('Feature 2', fontsize=12, fontweight='bold')
ax.set_title('Anomaly Detection - Isolation Forest Results', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '12_anomaly_detection_scatter.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 12 saved: 12_anomaly_detection_scatter.png")

# Chart 13: Anomaly Score Distribution
print("Generating Chart 13: Anomaly Score Distribution...")
anomaly_scores = np.hstack([np.random.rand(150) * 0.4, np.random.rand(10) * 0.3 + 0.7])
threshold = 0.6

fig, ax = plt.subplots(figsize=(12, 7))
colors_dist = ['#2E86AB' if score < threshold else '#F18F01' for score in anomaly_scores]
ax.hist(anomaly_scores[anomaly_scores < threshold], bins=30, color='#2E86AB', alpha=0.7, label='Normal', edgecolor='black')
ax.hist(anomaly_scores[anomaly_scores >= threshold], bins=10, color='#F18F01', alpha=0.7, label='Anomaly', edgecolor='red')
ax.axvline(threshold, color='red', linestyle='--', linewidth=2.5, label=f'Threshold: {threshold}')
ax.set_xlabel('Anomaly Score', fontsize=12, fontweight='bold')
ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax.set_title('Distribution of Anomaly Scores', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '13_anomaly_score_distribution.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 13 saved: 13_anomaly_score_distribution.png")

# Chart 14: Time Series Anomaly Detection
print("Generating Chart 14: Time Series Anomaly Detection...")
t = np.arange(0, 200, 0.5)
signal = 10 * np.sin(t/20) + 2 * np.random.randn(len(t))
anomaly_indices = [100, 150, 250, 300]
anomaly_signal = np.zeros_like(signal)
for idx in anomaly_indices:
    if idx < len(signal):
        anomaly_signal[idx] = signal[idx] + 15

fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(t, signal, color='#2E86AB', linewidth=2, label='Time Series', alpha=0.7)
ax.scatter([t[idx] for idx in anomaly_indices if idx < len(t)], 
           [signal[idx] + 15 for idx in anomaly_indices if idx < len(t)],
           color='#F18F01', s=200, marker='X', label='Anomalies', edgecolors='red', zorder=5)
ax.set_xlabel('Time', fontsize=12, fontweight='bold')
ax.set_ylabel('Value', fontsize=12, fontweight='bold')
ax.set_title('Time Series with Detected Anomalies', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '14_timeseries_anomaly.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 14 saved: 14_timeseries_anomaly.png")

# ========================
# 5. MONITORING & DEPLOYMENT CHARTS (3)
# ========================

# Chart 15: Model Drift Detection
print("Generating Chart 15: Model Drift Detection...")
days = np.arange(30)
baseline_accuracy = 0.92
drift_signal = 0.92 - 0.015 * (days / 30) + 0.02 * np.sin(days / 10)

fig, ax = plt.subplots(figsize=(12, 7))
ax.plot(days, drift_signal, color='#2E86AB', linewidth=2.5, marker='o', markersize=6)
ax.axhline(y=baseline_accuracy * 0.95, color='orange', linestyle='--', linewidth=2, label='Warning Threshold (95%)')
ax.fill_between(days, baseline_accuracy * 0.95, 1.0, alpha=0.2, color='green', label='Acceptable Range')
ax.fill_between(days, 0.8, baseline_accuracy * 0.95, alpha=0.2, color='red', label='Alert Range')
ax.set_xlabel('Days', fontsize=12, fontweight='bold')
ax.set_ylabel('Model Accuracy', fontsize=12, fontweight='bold')
ax.set_title('Model Drift Detection Over 30 Days', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_ylim([0.85, 0.95])
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '15_model_drift.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 15 saved: 15_model_drift.png")

# Chart 16: Model Retraining Schedule
print("Generating Chart 16: Model Retraining Schedule...")
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
versions = [1, 2, 3, 4, 5, 6]
accuracy_progression = [0.85, 0.87, 0.89, 0.88, 0.91, 0.93]
training_time = [120, 135, 140, 125, 150, 145]

fig, ax1 = plt.subplots(figsize=(12, 7))
color1 = '#2E86AB'
ax1.plot(months, accuracy_progression, color=color1, marker='o', markersize=10, linewidth=2.5, label='Model Accuracy')
ax1.set_ylabel('Accuracy', fontsize=12, fontweight='bold', color=color1)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_ylim([0.8, 0.95])

ax2 = ax1.twinx()
color2 = '#F18F01'
ax2.bar(months, training_time, alpha=0.5, color=color2, label='Training Time')
ax2.set_ylabel('Training Time (minutes)', fontsize=12, fontweight='bold', color=color2)
ax2.tick_params(axis='y', labelcolor=color2)

fig.suptitle('Model Retraining Schedule and Performance', fontsize=14, fontweight='bold')
fig.tight_layout()
plt.savefig(os.path.join(output_dir, '16_retraining_schedule.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 16 saved: 16_retraining_schedule.png")

# Chart 17: Inference Cost vs Performance
print("Generating Chart 17: Inference Cost vs Performance...")
model_names = ['Lightweight', 'Standard', 'Advanced', 'Premium', 'Enterprise']
cost_per_1k = [0.01, 0.05, 0.15, 0.30, 0.50]
performance = [0.82, 0.88, 0.93, 0.96, 0.98]

fig, ax = plt.subplots(figsize=(11, 8))
scatter = ax.scatter(cost_per_1k, performance, s=500, alpha=0.6, c=range(len(model_names)), 
                    cmap='viridis', edgecolors='black', linewidth=2)
for i, name in enumerate(model_names):
    ax.annotate(name, (cost_per_1k[i], performance[i]), 
               xytext=(5, 5), textcoords='offset points', fontsize=10, fontweight='bold')
ax.set_xlabel('Cost per 1K Inferences ($)', fontsize=12, fontweight='bold')
ax.set_ylabel('Model Performance (F1-Score)', fontsize=12, fontweight='bold')
ax.set_title('Inference Cost vs Performance Trade-off', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '17_cost_performance_tradeoff.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 17 saved: 17_cost_performance_tradeoff.png")

# ========================
# 6. ARCHITECTURE DIAGRAMS (2)
# ========================

# Chart 18: Model Architecture Diagram
print("Generating Chart 18: Model Architecture Flow...")
fig, ax = plt.subplots(figsize=(13, 8))
ax.axis('off')

layers = ['Input\n(Feature Vector)', 'Dense\n(128 units)', 'Dense\n(64 units)', 
          'Dense\n(32 units)', 'Output\n(Classification)']
activations = ['None', 'ReLU', 'ReLU', 'ReLU', 'Softmax']
y_positions = np.linspace(0.9, 0.1, len(layers))

for i, (layer, activation, y) in enumerate(zip(layers, activations, y_positions)):
    # Draw box
    box = plt.Rectangle((0.1 + i*0.17, y - 0.05), 0.12, 0.1, 
                        fill=True, facecolor='#2E86AB', edgecolor='black', linewidth=2)
    ax.add_patch(box)
    ax.text(0.16 + i*0.17, y, layer, ha='center', va='center', 
           fontsize=9, fontweight='bold', color='white')
    ax.text(0.16 + i*0.17, y - 0.08, activation, ha='center', va='top', 
           fontsize=8, style='italic', color='gray')
    
    # Draw arrow
    if i < len(layers) - 1:
        ax.arrow(0.22 + i*0.17, y, 0.08, 0, head_width=0.02, head_length=0.02, 
                fc='black', ec='black', linewidth=2)

ax.text(0.5, 0.98, 'Neural Network Architecture', ha='center', fontsize=14, fontweight='bold')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '18_model_architecture.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 18 saved: 18_model_architecture.png")

# Chart 19: ML Pipeline Workflow
print("Generating Chart 19: ML Pipeline Workflow...")
fig, ax = plt.subplots(figsize=(14, 8))
ax.axis('off')

stages = [
    {'name': 'Data\nIngestion', 'color': '#2E86AB'},
    {'name': 'Data\nPreprocessing', 'color': '#A23B72'},
    {'name': 'Feature\nEngineering', 'color': '#F18F01'},
    {'name': 'Model\nTraining', 'color': '#C73E1D'},
    {'name': 'Model\nValidation', 'color': '#6A994E'},
    {'name': 'Model\nDeployment', 'color': '#BC4749'}
]

y_pos = 0.5
x_positions = np.linspace(0.08, 0.92, len(stages))

for i, (stage, x) in enumerate(zip(stages, x_positions)):
    # Draw stage box
    box = plt.Rectangle((x - 0.06, y_pos - 0.08), 0.12, 0.16, 
                        fill=True, facecolor=stage['color'], edgecolor='black', linewidth=2)
    ax.add_patch(box)
    ax.text(x, y_pos, stage['name'], ha='center', va='center', 
           fontsize=10, fontweight='bold', color='white')
    
    # Draw arrow to next stage
    if i < len(stages) - 1:
        ax.arrow(x + 0.06, y_pos, 0.08, 0, head_width=0.04, head_length=0.02, 
                fc='black', ec='black', linewidth=2.5)

# Add feedback loop
ax.annotate('', xy=(x_positions[0], y_pos - 0.18), xytext=(x_positions[-1], y_pos - 0.18),
            arrowprops=dict(arrowstyle='<-', lw=2.5, color='red'))
ax.text(0.5, y_pos - 0.22, 'Feedback Loop (Model Improvement)', ha='center', 
       fontsize=10, style='italic', color='red', fontweight='bold')

ax.text(0.5, 0.95, 'End-to-End ML Pipeline Workflow', ha='center', fontsize=14, fontweight='bold')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, '19_ml_pipeline_workflow.png'), dpi=300, bbox_inches='tight')
plt.close()
print("✓ Chart 19 saved: 19_ml_pipeline_workflow.png")

print("\n" + "=" * 60)
print("✓ All 19 charts generated successfully!")
print("=" * 60)
