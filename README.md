## Download Model Weights

This repository requires a large model file that cannot be stored on GitHub.

1. Download `pytorch_model.bin` from [Google Drive link here](https://drive.google.com/file/d/1gYF0sLhNv7_9P4hpzPPli0tANkmmQl9I/view?usp=sharing).
2. Place it in the folder: `models/facebook/nllb-200-distilled-600M/`

---

### Optional: Download Automatically with gdown

If you have [gdown](https://github.com/wkentaro/gdown) installed, you can run this command in your terminal:

```sh
gdown --id 1gYF0sLhNv7_9P4hpzPPli0tANkmmQl9I -O models/facebook/nllb-200-distilled-600M/pytorch_model.bin
```

If you don't have gdown, install it with:

```sh
pip install gdown
```

---

**Note:** Ensure `models/facebook/nllb-200-distilled-600M/pytorch_model.bin` is listed in your `.gitignore` so it is not tracked by git.