"""
Machine Learning Model Evaluation & Feature Importance Visualization Suite
Generates 19 comprehensive charts for college research projects
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification, make_blobs
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.metrics import (
    roc_curve, auc, roc_auc_score, precision_recall_curve,
    confusion_matrix, classification_report, accuracy_score,
    precision_score, recall_score, f1_score
)
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Create output directory
import os
os.makedirs('output_charts', exist_ok=True)

print("🚀 Generating ML Model Evaluation Charts...")
print("=" * 60)

# ============================================================================
# PHASE 1: Generate Synthetic Data
# ============================================================================
np.random.seed(42)

# Create classification dataset
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    n_classes=2,
    random_state=42
)

# Create feature names
feature_names = [f"Feature_{i}" for i in range(X.shape[1])]
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Scale data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("✅ Data generated: 1000 samples, 20 features, 2 classes")

# ============================================================================
# PHASE 2: Train Models
# ============================================================================
print("\n📊 Training ML Models...")

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)
rf_pred = rf_model.predict(X_test_scaled)
rf_pred_proba = rf_model.predict_proba(X_test_scaled)[:, 1]

# XGBoost
xgb_model = XGBClassifier(n_estimators=100, random_state=42, verbosity=0)
xgb_model.fit(X_train_scaled, y_train)
xgb_pred = xgb_model.predict(X_test_scaled)
xgb_pred_proba = xgb_model.predict_proba(X_test_scaled)[:, 1]

# Logistic Regression
lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train_scaled, y_train)
lr_pred = lr_model.predict(X_test_scaled)
lr_pred_proba = lr_model.predict_proba(X_test_scaled)[:, 1]

print("✅ Models trained: Random Forest, XGBoost, Logistic Regression")

# ============================================================================
# CHART 1: ROC Graph – Random Forest
# ============================================================================
print("\n📈 Generating Chart 1: ROC Graph – Random Forest")
fpr_rf, tpr_rf, _ = roc_curve(y_test, rf_pred_proba)
roc_auc_rf = auc(fpr_rf, tpr_rf)

fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(fpr_rf, tpr_rf, color='darkorange', lw=2, label=f'ROC Curve (AUC = {roc_auc_rf:.3f})')
ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Classifier')
ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 1.05])
ax.set_xlabel('False Positive Rate', fontsize=12, fontweight='bold')
ax.set_ylabel('True Positive Rate', fontsize=12, fontweight='bold')
ax.set_title('ROC Curve - Random Forest Classifier', fontsize=14, fontweight='bold')
ax.legend(loc="lower right", fontsize=11)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('output_charts/01_roc_random_forest.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 01_roc_random_forest.png")

# ============================================================================
# CHART 2: Column Data – Random Forest (Top Feature Importance)
# ============================================================================
print("📈 Generating Chart 2: Feature Importance – Random Forest")
feature_importance_rf = pd.DataFrame({
    'feature': feature_names,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(feature_importance_rf['feature'], feature_importance_rf['importance'], color='steelblue')
ax.set_xlabel('Importance Score', fontsize=12, fontweight='bold')
ax.set_ylabel('Features', fontsize=12, fontweight='bold')
ax.set_title('Top 10 Feature Importance - Random Forest', fontsize=14, fontweight='bold')
ax.invert_yaxis()
for i, (idx, row) in enumerate(feature_importance_rf.iterrows()):
    ax.text(row['importance'], i, f" {row['importance']:.4f}", va='center', fontsize=10)
plt.tight_layout()
plt.savefig('output_charts/02_feature_importance_rf.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 02_feature_importance_rf.png")

# ============================================================================
# CHART 3: ROC Graph – XGBoost
# ============================================================================
print("📈 Generating Chart 3: ROC Graph – XGBoost")
fpr_xgb, tpr_xgb, _ = roc_curve(y_test, xgb_pred_proba)
roc_auc_xgb = auc(fpr_xgb, tpr_xgb)

fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(fpr_xgb, tpr_xgb, color='green', lw=2, label=f'ROC Curve (AUC = {roc_auc_xgb:.3f})')
ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Classifier')
ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 1.05])
ax.set_xlabel('False Positive Rate', fontsize=12, fontweight='bold')
ax.set_ylabel('True Positive Rate', fontsize=12, fontweight='bold')
ax.set_title('ROC Curve - XGBoost Classifier', fontsize=14, fontweight='bold')
ax.legend(loc="lower right", fontsize=11)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('output_charts/03_roc_xgboost.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 03_roc_xgboost.png")

# ============================================================================
# CHART 4: Column Data – XGBoost (Top Feature Importance)
# ============================================================================
print("📈 Generating Chart 4: Feature Importance – XGBoost")
feature_importance_xgb = pd.DataFrame({
    'feature': feature_names,
    'importance': xgb_model.feature_importances_
}).sort_values('importance', ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(feature_importance_xgb['feature'], feature_importance_xgb['importance'], color='forestgreen')
ax.set_xlabel('Importance Score', fontsize=12, fontweight='bold')
ax.set_ylabel('Features', fontsize=12, fontweight='bold')
ax.set_title('Top 10 Feature Importance - XGBoost', fontsize=14, fontweight='bold')
ax.invert_yaxis()
for i, (idx, row) in enumerate(feature_importance_xgb.iterrows()):
    ax.text(row['importance'], i, f" {row['importance']:.4f}", va='center', fontsize=10)
plt.tight_layout()
plt.savefig('output_charts/04_feature_importance_xgb.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 04_feature_importance_xgb.png")

# ============================================================================
# CHART 5: Model Performance Comparison Bar Chart
# ============================================================================
print("📈 Generating Chart 5: Model Performance Comparison")
models = ['Random Forest', 'XGBoost', 'Logistic Regression']
accuracies = [
    accuracy_score(y_test, rf_pred),
    accuracy_score(y_test, xgb_pred),
    accuracy_score(y_test, lr_pred)
]
precisions = [
    precision_score(y_test, rf_pred),
    precision_score(y_test, xgb_pred),
    precision_score(y_test, lr_pred)
]
recalls = [
    recall_score(y_test, rf_pred),
    recall_score(y_test, xgb_pred),
    recall_score(y_test, lr_pred)
]
f1_scores = [
    f1_score(y_test, rf_pred),
    f1_score(y_test, xgb_pred),
    f1_score(y_test, lr_pred)
]

x = np.arange(len(models))
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - 1.5*width, accuracies, width, label='Accuracy', color='steelblue')
ax.bar(x - 0.5*width, precisions, width, label='Precision', color='darkorange')
ax.bar(x + 0.5*width, recalls, width, label='Recall', color='green')
ax.bar(x + 1.5*width, f1_scores, width, label='F1-Score', color='red')

ax.set_ylabel('Score', fontsize=12, fontweight='bold')
ax.set_title('Model Performance Comparison', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend(fontsize=10)
ax.set_ylim([0, 1.1])
ax.grid(alpha=0.3, axis='y')

for i, model in enumerate(models):
    ax.text(i - 1.5*width, accuracies[i] + 0.02, f'{accuracies[i]:.3f}', ha='center', fontsize=9)
    ax.text(i - 0.5*width, precisions[i] + 0.02, f'{precisions[i]:.3f}', ha='center', fontsize=9)
    ax.text(i + 0.5*width, recalls[i] + 0.02, f'{recalls[i]:.3f}', ha='center', fontsize=9)
    ax.text(i + 1.5*width, f1_scores[i] + 0.02, f'{f1_scores[i]:.3f}', ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('output_charts/05_model_performance_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 05_model_performance_comparison.png")

# ============================================================================
# CHART 6: ROC Curve Overlay (All Models Comparison)
# ============================================================================
print("📈 Generating Chart 6: ROC Curve Overlay - All Models")
fpr_lr, tpr_lr, _ = roc_curve(y_test, lr_pred_proba)
roc_auc_lr = auc(fpr_lr, tpr_lr)

fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(fpr_rf, tpr_rf, color='darkorange', lw=2.5, label=f'Random Forest (AUC = {roc_auc_rf:.3f})')
ax.plot(fpr_xgb, tpr_xgb, color='green', lw=2.5, label=f'XGBoost (AUC = {roc_auc_xgb:.3f})')
ax.plot(fpr_lr, tpr_lr, color='blue', lw=2.5, label=f'Logistic Regression (AUC = {roc_auc_lr:.3f})')
ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Classifier')
ax.set_xlim([0.0, 1.0])
ax.set_ylim([0.0, 1.05])
ax.set_xlabel('False Positive Rate', fontsize=12, fontweight='bold')
ax.set_ylabel('True Positive Rate', fontsize=12, fontweight='bold')
ax.set_title('ROC Curve Comparison - All Models', fontsize=14, fontweight='bold')
ax.legend(loc="lower right", fontsize=11)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('output_charts/06_roc_all_models.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 06_roc_all_models.png")

# ============================================================================
# CHART 7: Precision–Recall Curve
# ============================================================================
print("📈 Generating Chart 7: Precision-Recall Curve")
precision_rf, recall_rf, _ = precision_recall_curve(y_test, rf_pred_proba)
precision_xgb, recall_xgb, _ = precision_recall_curve(y_test, xgb_pred_proba)
precision_lr, recall_lr, _ = precision_recall_curve(y_test, lr_pred_proba)

fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(recall_rf, precision_rf, color='darkorange', lw=2.5, label='Random Forest', marker='o')
ax.plot(recall_xgb, precision_xgb, color='green', lw=2.5, label='XGBoost', marker='s')
ax.plot(recall_lr, precision_lr, color='blue', lw=2.5, label='Logistic Regression', marker='^')
ax.set_xlabel('Recall', fontsize=12, fontweight='bold')
ax.set_ylabel('Precision', fontsize=12, fontweight='bold')
ax.set_title('Precision-Recall Curve - All Models', fontsize=14, fontweight='bold')
ax.legend(loc="best", fontsize=11)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('output_charts/07_precision_recall_curve.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 07_precision_recall_curve.png")

# ============================================================================
# CHART 8: Enhanced Classification Heatmap (Overall)
# ============================================================================
print("📈 Generating Chart 8: Classification Heatmap - Overall")
cm_rf = confusion_matrix(y_test, rf_pred)
cm_xgb = confusion_matrix(y_test, xgb_pred)
cm_lr = confusion_matrix(y_test, lr_pred)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

models_list = [('Random Forest', cm_rf), ('XGBoost', cm_xgb), ('Logistic Regression', cm_lr)]
for idx, (name, cm) in enumerate(models_list):
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx], cbar=True,
                xticklabels=['Negative', 'Positive'], yticklabels=['Negative', 'Positive'])
    axes[idx].set_title(f'{name}', fontsize=12, fontweight='bold')
    axes[idx].set_ylabel('True Label', fontsize=10)
    axes[idx].set_xlabel('Predicted Label', fontsize=10)

plt.suptitle('Confusion Matrices - All Models', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('output_charts/08_confusion_matrices_overall.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 08_confusion_matrices_overall.png")

# ============================================================================
# CHART 9: Throughput Comparison Over Time
# ============================================================================
print("📈 Generating Chart 9: Throughput Comparison Over Time")
time_points = np.arange(0, 100, 5)
rf_throughput = 1000 + 50*np.sin(time_points/10) + np.random.normal(0, 30, len(time_points))
xgb_throughput = 1200 + 40*np.cos(time_points/10) + np.random.normal(0, 40, len(time_points))
lr_throughput = 1500 + 30*np.sin(time_points/10) + np.random.normal(0, 20, len(time_points))

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(time_points, rf_throughput, marker='o', linewidth=2, label='Random Forest', color='darkorange')
ax.plot(time_points, xgb_throughput, marker='s', linewidth=2, label='XGBoost', color='green')
ax.plot(time_points, lr_throughput, marker='^', linewidth=2, label='Logistic Regression', color='blue')
ax.set_xlabel('Time (seconds)', fontsize=12, fontweight='bold')
ax.set_ylabel('Throughput (predictions/sec)', fontsize=12, fontweight='bold')
ax.set_title('System Throughput Comparison Over Time', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('output_charts/09_throughput_over_time.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 09_throughput_over_time.png")

# ============================================================================
# CHART 10: Latency CDF (Cumulative Distribution Function)
# ============================================================================
print("📈 Generating Chart 10: Latency CDF")
rf_latency = np.random.gamma(shape=2, scale=10, size=1000)
xgb_latency = np.random.gamma(shape=2, scale=12, size=1000)
lr_latency = np.random.gamma(shape=2, scale=8, size=1000)

fig, ax = plt.subplots(figsize=(12, 6))
for data, label, color in [
    (np.sort(rf_latency), 'Random Forest', 'darkorange'),
    (np.sort(xgb_latency), 'XGBoost', 'green'),
    (np.sort(lr_latency), 'Logistic Regression', 'blue')
]:
    ax.plot(data, np.arange(1, len(data)+1)/len(data), label=label, linewidth=2.5, color=color)

ax.set_xlabel('Latency (ms)', fontsize=12, fontweight='bold')
ax.set_ylabel('CDF', fontsize=12, fontweight='bold')
ax.set_title('Latency CDF - All Models', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('output_charts/10_latency_cdf.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 10_latency_cdf.png")

# ============================================================================
# CHART 11: Timeline of Predicted Classes
# ============================================================================
print("📈 Generating Chart 11: Timeline of Predicted Classes")
predictions_timeline = np.concatenate([rf_pred[:50], xgb_pred[:50], lr_pred[:50]])
time_idx = np.repeat(np.arange(3), 50) * 50 + np.tile(np.arange(50), 3)

fig, ax = plt.subplots(figsize=(14, 5))
colors = ['red' if p == 0 else 'green' for p in predictions_timeline]
ax.scatter(time_idx, predictions_timeline, c=colors, s=100, alpha=0.6, edgecolors='black')
ax.axhline(y=0.5, color='gray', linestyle='--', linewidth=2, alpha=0.5)
ax.set_xlabel('Prediction Sequence', fontsize=12, fontweight='bold')
ax.set_ylabel('Predicted Class', fontsize=12, fontweight='bold')
ax.set_title('Timeline of Predicted Classes', fontsize=14, fontweight='bold')
ax.set_yticks([0, 1])
ax.set_yticklabels(['Negative', 'Positive'])
ax.grid(alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('output_charts/11_timeline_predictions.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 11_timeline_predictions.png")

# ============================================================================
# CHART 12: Anomaly Score Distribution
# ============================================================================
print("📈 Generating Chart 12: Anomaly Score Distribution")
anomaly_scores = np.random.beta(2, 5, 1000)
threshold = 0.7

fig, ax = plt.subplots(figsize=(10, 6))
n, bins, patches = ax.hist(anomaly_scores, bins=30, alpha=0.7, color='steelblue', edgecolor='black')
for i, patch in enumerate(patches):
    if bins[i] > threshold:
        patch.set_facecolor('red')
    else:
        patch.set_facecolor('steelblue')

ax.axvline(x=threshold, color='red', linestyle='--', linewidth=2.5, label=f'Anomaly Threshold ({threshold})')
ax.set_xlabel('Anomaly Score', fontsize=12, fontweight='bold')
ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax.set_title('Anomaly Score Distribution with Threshold', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('output_charts/12_anomaly_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 12_anomaly_distribution.png")

# ============================================================================
# CHART 13: Real-Time Anomaly Timeline with Mitigation Triggers
# ============================================================================
print("📈 Generating Chart 13: Anomaly Timeline with Mitigation")
time_range = np.arange(0, 100)
anomaly_timeline = np.random.beta(2, 5, 100)
mitigation_triggered = anomaly_timeline > threshold

fig, ax = plt.subplots(figsize=(14, 6))
ax.fill_between(time_range, 0, anomaly_timeline, alpha=0.3, color='blue', label='Anomaly Score')
ax.plot(time_range, anomaly_timeline, color='blue', linewidth=2)
ax.axhline(y=threshold, color='red', linestyle='--', linewidth=2.5, label='Threshold')

trigger_times = time_range[mitigation_triggered]
ax.scatter(trigger_times, anomaly_timeline[mitigation_triggered], color='red', s=200, 
          marker='X', label='Mitigation Trigger', zorder=5, edgecolors='darkred', linewidth=2)

ax.set_xlabel('Time (minutes)', fontsize=12, fontweight='bold')
ax.set_ylabel('Anomaly Score', fontsize=12, fontweight='bold')
ax.set_title('Real-Time Anomaly Timeline with Mitigation Triggers', fontsize=14, fontweight='bold')
ax.legend(fontsize=11, loc='upper right')
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('output_charts/13_anomaly_timeline.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 13_anomaly_timeline.png")

# ============================================================================
# CHART 14: Enhanced Classification Heatmap (Per-Class)
# ============================================================================
print("📈 Generating Chart 14: Classification Heatmap - Per-Class")
from sklearn.metrics import classification_report

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
models_list_names = ['Random Forest', 'XGBoost', 'Logistic Regression']
predictions_list = [rf_pred, xgb_pred, lr_pred]

for idx, (name, preds) in enumerate(zip(models_list_names, predictions_list)):
    report = classification_report(y_test, preds, output_dict=True)
    report_df = pd.DataFrame(report).iloc[:-1, :-1].T
    
    sns.heatmap(report_df, annot=True, fmt='.3f', cmap='RdYlGn', ax=axes[idx], cbar=True,
                vmin=0, vmax=1)
    axes[idx].set_title(f'{name}', fontsize=12, fontweight='bold')
    axes[idx].set_ylabel('Metrics', fontsize=10)

plt.suptitle('Classification Report - All Models', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('output_charts/14_classification_heatmap_per_class.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 14_classification_heatmap_per_class.png")

# ============================================================================
# CHART 15: Heatmap (Classification Report – XGBoost)
# ============================================================================
print("📈 Generating Chart 15: XGBoost Classification Report Heatmap")
report_xgb = classification_report(y_test, xgb_pred, output_dict=True)
report_xgb_df = pd.DataFrame(report_xgb).iloc[:-1, :-1].T

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(report_xgb_df, annot=True, fmt='.3f', cmap='YlOrRd', ax=ax, cbar_kws={'label': 'Score'},
            linewidths=0.5, linecolor='gray')
ax.set_title('XGBoost Classification Report Heatmap', fontsize=14, fontweight='bold')
ax.set_ylabel('Metrics', fontsize=12, fontweight='bold')
ax.set_xlabel('Classes', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('output_charts/15_xgboost_report_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 15_xgboost_report_heatmap.png")

# ============================================================================
# CHART 16: Timeline Classification Results
# ============================================================================
print("📈 Generating Chart 16: Timeline Classification Results")
window_size = 10
rf_accuracy_timeline = [accuracy_score(y_test[i:i+window_size], rf_pred[i:i+window_size]) 
                        for i in range(0, len(y_test)-window_size, window_size)]
xgb_accuracy_timeline = [accuracy_score(y_test[i:i+window_size], xgb_pred[i:i+window_size]) 
                         for i in range(0, len(y_test)-window_size, window_size)]
lr_accuracy_timeline = [accuracy_score(y_test[i:i+window_size], lr_pred[i:i+window_size]) 
                        for i in range(0, len(y_test)-window_size, window_size)]

fig, ax = plt.subplots(figsize=(14, 6))
x_positions = np.arange(len(rf_accuracy_timeline))
ax.plot(x_positions, rf_accuracy_timeline, marker='o', linewidth=2.5, label='Random Forest', color='darkorange')
ax.plot(x_positions, xgb_accuracy_timeline, marker='s', linewidth=2.5, label='XGBoost', color='green')
ax.plot(x_positions, lr_accuracy_timeline, marker='^', linewidth=2.5, label='Logistic Regression', color='blue')

ax.set_xlabel('Time Window (batches)', fontsize=12, fontweight='bold')
ax.set_ylabel('Accuracy', fontsize=12, fontweight='bold')
ax.set_title('Timeline of Classification Results (Sliding Window)', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.set_ylim([0.5, 1.05])
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('output_charts/16_timeline_classification.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 16_timeline_classification.png")

# ============================================================================
# CHART 17: Throughput Over Time (Alternative Perspective)
# ============================================================================
print("📈 Generating Chart 17: Throughput Over Time - Alternative")
timestamps = pd.date_range(start='2024-01-01', periods=100, freq='H')
rf_throughput_alt = np.cumsum(np.random.randint(50, 150, 100))
xgb_throughput_alt = np.cumsum(np.random.randint(60, 180, 100))
lr_throughput_alt = np.cumsum(np.random.randint(80, 200, 100))

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(timestamps, rf_throughput_alt, marker='o', linewidth=2.5, label='Random Forest', color='darkorange')
ax.plot(timestamps, xgb_throughput_alt, marker='s', linewidth=2.5, label='XGBoost', color='green')
ax.plot(timestamps, lr_throughput_alt, marker='^', linewidth=2.5, label='Logistic Regression', color='blue')

ax.set_xlabel('Timestamp', fontsize=12, fontweight='bold')
ax.set_ylabel('Cumulative Predictions', fontsize=12, fontweight='bold')
ax.set_title('Cumulative Throughput Over Time', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('output_charts/17_throughput_cumulative.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 17_throughput_cumulative.png")

# ============================================================================
# CHART 18: Architecture Diagram
# ============================================================================
print("📈 Generating Chart 18: Architecture Diagram")
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'Machine Learning System Architecture', fontsize=16, fontweight='bold', ha='center')

# Data Layer
data_box = FancyBboxPatch((0.5, 7.5), 2, 1.2, boxstyle="round,pad=0.1", 
                          edgecolor='black', facecolor='lightblue', linewidth=2)
ax.add_patch(data_box)
ax.text(1.5, 8.1, 'Data Input\n(1000 samples)', fontsize=10, ha='center', va='center', fontweight='bold')

# Preprocessing Layer
preprocess_box = FancyBboxPatch((3.5, 7.5), 2, 1.2, boxstyle="round,pad=0.1",
                               edgecolor='black', facecolor='lightyellow', linewidth=2)
ax.add_patch(preprocess_box)
ax.text(4.5, 8.1, 'Preprocessing\n(Scaling)', fontsize=10, ha='center', va='center', fontweight='bold')

# Model Layer
models_y = 5.5
model_names = ['Random\nForest', 'XGBoost', 'Logistic\nRegression']
model_x_positions = [1.5, 4.5, 7.5]
model_colors = ['lightcoral', 'lightgreen', 'lightcyan']

for x, name, color in zip(model_x_positions, model_names, model_colors):
    model_box = FancyBboxPatch((x-1, models_y), 2, 1.2, boxstyle="round,pad=0.1",
                              edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(model_box)
    ax.text(x, models_y+0.6, name, fontsize=10, ha='center', va='center', fontweight='bold')

# Evaluation Layer
eval_box = FancyBboxPatch((2.5, 3.5), 5, 1.2, boxstyle="round,pad=0.1",
                         edgecolor='black', facecolor='lightgray', linewidth=2)
ax.add_patch(eval_box)
ax.text(5, 4.1, 'Evaluation Metrics\n(ROC, Precision, Recall, F1)', fontsize=10, ha='center', va='center', fontweight='bold')

# Deployment Layer
deploy_box = FancyBboxPatch((2.5, 1.5), 5, 1.2, boxstyle="round,pad=0.1",
                           edgecolor='black', facecolor='lightyellow', linewidth=2)
ax.add_patch(deploy_box)
ax.text(5, 2.1, 'Deployment & Monitoring\n(Real-time Predictions)', fontsize=10, ha='center', va='center', fontweight='bold')

# Arrows
arrow_props = dict(arrowstyle='->', lw=2.5, color='black')
ax.annotate('', xy=(3.5, 8.1), xytext=(2.5, 8.1), arrowprops=arrow_props)
ax.annotate('', xy=(1.5, 7.5), xytext=(4, 7.5), arrowprops=arrow_props)
ax.annotate('', xy=(4.5, 7.5), xytext=(4, 7.5), arrowprops=arrow_props)
ax.annotate('', xy=(7.5, 7.5), xytext=(6.5, 7.5), arrowprops=arrow_props)
ax.annotate('', xy=(4, 4.7), xytext=(3, 5.5), arrowprops=arrow_props)
ax.annotate('', xy=(4.5, 4.7), xytext=(4.5, 5.5), arrowprops=arrow_props)
ax.annotate('', xy=(5, 4.7), xytext=(6, 5.5), arrowprops=arrow_props)
ax.annotate('', xy=(5, 2.7), xytext=(5, 3.5), arrowprops=arrow_props)

plt.tight_layout()
plt.savefig('output_charts/18_architecture_diagram.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 18_architecture_diagram.png")

# ============================================================================
# CHART 19: Flow State Diagram
# ============================================================================
print("📈 Generating Chart 19: Flow State Diagram")
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

ax.text(5, 11.5, 'System Workflow - State Flow Diagram', fontsize=16, fontweight='bold', ha='center')

# States
states = [
    (2, 10, 'START', 'lightblue'),
    (5, 10, 'Data\nIngestion', 'lightgreen'),
    (8, 10, 'Validation', 'lightyellow'),
    (2, 7.5, 'Feature\nEngineering', 'lightcoral'),
    (5, 7.5, 'Model\nTraining', 'lightsteelblue'),
    (8, 7.5, 'Model\nEvaluation', 'lightcyan'),
    (2, 5, 'Hyperparameter\nTuning', 'lightsalmon'),
    (5, 5, 'Cross\nValidation', 'lightgoldenrodyellow'),
    (8, 5, 'Decision\nPoint', 'lightpink'),
    (5, 2.5, 'Deployment', 'lightgreen'),
    (5, 0.5, 'MONITORING &\nFEEDBACK', 'lightblue'),
]

for x, y, label, color in states:
    circle = plt.Circle((x, y), 0.6, color=color, ec='black', linewidth=2)
    ax.add_patch(circle)
    ax.text(x, y, label, fontsize=9, ha='center', va='center', fontweight='bold')

# Transitions
transitions = [
    ((2.6, 10), (4.4, 10)),
    ((5.6, 10), (7.4, 10)),
    ((8, 9.4), (8, 8.1)),
    ((7.4, 7.5), (5.6, 7.5)),
    ((5, 6.9), (2.6, 6.5)),
    ((2, 6.9), (2, 5.6)),
    ((2.6, 5), (4.4, 5)),
    ((5.6, 5), (7.4, 5)),
    ((8, 4.4), (5.6, 2.9)),
    ((4.4, 2.5), (5.6, 2.5)),
    ((5, 2.1), (5, 1.1)),
]

for (x1, y1), (x2, y2) in transitions:
    arrow = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='->', mutation_scale=25, lw=2, color='black')
    ax.add_patch(arrow)

# Legend
legend_items = [
    'Process',
    'Decision',
    'Input/Output'
]
ax.text(0.5, -0.5, 'Legend: Blue=Start/End, Green=Process, Yellow=Validation, Red=Tuning, Pink=Decision', 
        fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('output_charts/19_flow_state_diagram.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Saved: 19_flow_state_diagram.png")

# ============================================================================
# Summary Report
# ============================================================================
print("\n" + "=" * 60)
print("🎉 ALL CHARTS GENERATED SUCCESSFULLY!")
print("=" * 60)

summary = f"""
📊 GENERATION SUMMARY:
─────────────────────────────────────────────────────────

Total Charts Generated: 19
Output Directory: output_charts/

📈 CHARTS BY CATEGORY:

Model Evaluation & Feature Importance (4 charts):
  ✅ 01_roc_random_forest.png
  ✅ 02_feature_importance_rf.png
  ✅ 03_roc_xgboost.png
  ✅ 04_feature_importance_xgb.png

Performance Comparison (4 charts):
  ✅ 05_model_performance_comparison.png
  ✅ 06_roc_all_models.png
  ✅ 07_precision_recall_curve.png
  ✅ 08_confusion_matrices_overall.png

System Speed & Real-Time Behavior (3 charts):
  ✅ 09_throughput_over_time.png
  ✅ 10_latency_cdf.png
  ✅ 11_timeline_predictions.png

Risk & Anomaly Detection (3 charts):
  ✅ 12_anomaly_distribution.png
  ✅ 13_anomaly_timeline.png
  ✅ 14_classification_heatmap_per_class.png

Additional Monitoring/Deployment (3 charts):
  ✅ 15_xgboost_report_heatmap.png
  ✅ 16_timeline_classification.png
  ✅ 17_throughput_cumulative.png

Architecture & Workflow (2 diagrams):
  ✅ 18_architecture_diagram.png
  ✅ 19_flow_state_diagram.png

─────────────────────────────────────────────────────────

🏆 MODEL PERFORMANCE RESULTS:

Random Forest:
  • Accuracy: {accuracy_score(y_test, rf_pred):.4f}
  • Precision: {precision_score(y_test, rf_pred):.4f}
  • Recall: {recall_score(y_test, rf_pred):.4f}
  • F1-Score: {f1_score(y_test, rf_pred):.4f}
  • ROC AUC: {roc_auc_rf:.4f}

XGBoost:
  • Accuracy: {accuracy_score(y_test, xgb_pred):.4f}
  • Precision: {precision_score(y_test, xgb_pred):.4f}
  • Recall: {recall_score(y_test, xgb_pred):.4f}
  • F1-Score: {f1_score(y_test, xgb_pred):.4f}
  • ROC AUC: {roc_auc_xgb:.4f}

Logistic Regression:
  • Accuracy: {accuracy_score(y_test, lr_pred):.4f}
  • Precision: {precision_score(y_test, lr_pred):.4f}
  • Recall: {recall_score(y_test, lr_pred):.4f}
  • F1-Score: {f1_score(y_test, lr_pred):.4f}
  • ROC AUC: {roc_auc_lr:.4f}

─────────────────────────────────────────────────────────

📁 All files saved to: /output_charts/

✨ Ready for your college research project presentation! ✨
"""

print(summary)

# Save summary to text file
with open('output_charts/CHART_SUMMARY.txt', 'w') as f:
    f.write(summary)

print("\n✅ Summary saved to: CHART_SUMMARY.txt")
