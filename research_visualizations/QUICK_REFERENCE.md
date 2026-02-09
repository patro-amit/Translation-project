# Quick Reference Guide

## Execution Steps

### Step 1: Navigate to Directory
```bash
cd research_visualizations
```

### Step 2: Verify Dependencies
```bash
pip list | grep -E 'numpy|matplotlib|seaborn|scikit-learn'
```

### Step 3: Run Generator
```bash
python generate_charts.py
```

### Step 4: Check Output
```bash
ls -lh *.png
```

---

## Chart Categories & Files

### 🎯 MODEL EVALUATION (4 charts)
| # | File | Purpose |
|---|------|---------|
| 1 | `01_roc_curve_multiclass.png` | Multi-class ROC Analysis |
| 2 | `02_confusion_matrix.png` | Classification Results Heatmap |
| 3 | `03_feature_importance.png` | Top 15 Feature Rankings |
| 4 | `04_precision_recall_curve.png` | Classifier Trade-offs |

### 📊 PERFORMANCE COMPARISON (4 charts)
| # | File | Purpose |
|---|------|---------|
| 5 | `05_model_performance_comparison.png` | Multi-Model Benchmark |
| 6 | `06_training_validation_loss.png` | Learning Curves (100 epochs) |
| 7 | `07_f1_score_threshold.png` | Optimal Threshold Selection |
| 8 | `08_fairness_demographics.png` | Bias & Disparate Impact |

### ⚡ SYSTEM PERFORMANCE (3 charts)
| # | File | Purpose |
|---|------|---------|
| 9 | `09_latency_distribution.png` | Inference Speed Analysis |
| 10 | `10_memory_usage.png` | CPU/GPU Memory Trends |
| 11 | `11_gpu_utilization_heatmap.png` | 24-Hour Core Usage |

### 🚨 ANOMALY DETECTION (3 charts)
| # | File | Purpose |
|---|------|---------|
| 12 | `12_anomaly_detection_scatter.png` | 2D Anomaly Visualization |
| 13 | `13_anomaly_score_distribution.png` | Threshold Analysis |
| 14 | `14_timeseries_anomaly.png` | Temporal Anomalies |

### 📈 MONITORING & DEPLOYMENT (3 charts)
| # | File | Purpose |
|---|------|---------|
| 15 | `15_model_drift.png` | Performance Degradation Tracking |
| 16 | `16_retraining_schedule.png` | Version & Training Progress |
| 17 | `17_cost_performance_tradeoff.png` | Business Economics |

### 🏗️ ARCHITECTURE (2 charts)
| # | File | Purpose |
|---|------|---------|
| 18 | `18_model_architecture.png` | Neural Network Layers |
| 19 | `19_ml_pipeline_workflow.png` | End-to-End Pipeline |

---

## Common Commands

### View Single Chart
```bash
open 01_roc_curve_multiclass.png    # macOS
xdg-open 01_roc_curve_multiclass.png # Linux
```

### Count Generated Charts
```bash
ls -1 *.png | wc -l
```

### Check File Sizes
```bash
du -sh *.png
```

### Batch Convert to PDF
```bash
for f in *.png; do convert "$f" "${f%.png}.pdf"; done
```

### Create Archive
```bash
zip -r ml_charts.zip *.png
```

---

## Customization Tips

### Change Output Resolution
Edit line in `generate_charts.py`:
```python
# From:
plt.savefig(..., dpi=300, ...)
# To:
plt.savefig(..., dpi=150, ...)  # Lower resolution
```

### Modify Color Scheme
Edit color definitions:
```python
color1 = '#2E86AB'  # Change to your hex color
color2 = '#F18F01'
```

### Adjust Figure Size
```python
plt.rcParams['figure.figsize'] = (12, 8)  # width, height in inches
```

### Change Font Sizes
```python
plt.rcParams['font.size'] = 10  # Default font size
```

---

## Troubleshooting

### Missing Dependencies
```bash
pip install -r ../requirements.txt
# Or manually:
pip install numpy matplotlib seaborn scikit-learn
```

### Permission Denied
```bash
chmod +x generate_charts.py
python generate_charts.py
```

### Out of Memory
- Run on machine with 4GB+ RAM
- Reduce `figsize` in script
- Generate individual charts instead

### Charts Not Displaying
- Check if file exists: `ls *.png`
- Verify DPI: `file *.png`
- Try different viewer application

---

## Performance Notes

| Metric | Value |
|--------|-------|
| Execution Time | ~30-45 seconds |
| Total Output Size | ~15-20 MB |
| DPI Resolution | 300 (publication quality) |
| Memory Required | ~500 MB |
| Disk Space | ~20 MB after generation |

---

## File Organization

```
research_visualizations/
├── generate_charts.py          # Main script
├── README.md                   # Full documentation
├── QUICK_REFERENCE.md          # This file
├── INSTALLATION_GUIDE.txt      # Setup instructions
├── 01_roc_curve_multiclass.png
├── 02_confusion_matrix.png
├── ... (17 more PNG files)
└── 19_ml_pipeline_workflow.png
```

---

## Quick Links

- **Generate Charts**: `python generate_charts.py`
- **View Results**: `ls -lh *.png`
- **Archive Output**: `zip -r charts.zip *.png`
- **Full Docs**: See `README.md`

---

*Last Updated: 2026*
