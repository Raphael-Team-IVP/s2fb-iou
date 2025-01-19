# S2FB IoU: Improving Boundary-based Object-Centric Image Segmentation Quality Evaluation

[![DOI](https://img.shields.io/badge/DOI-10.1145/3696409.3700238-blue)](https://dl.acm.org/doi/10.1145/3696409.3700238)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-blue)](https://www.python.org/)

---


# Table of Contents
- [Overview](#overview)
- [Abstract](#abstract)
- [SegAtlas: Object Segmentation Quality Evaluation Tool](#segatlas-object-segmentation-quality-evaluation-tool)
- [Citation](#citation)
- [License](#license)
- [Contact](#contact)

---

## Overview

This repository contains the official implementation and supplementary resources for the paper:

**"S2FB IoU: Improving Boundary-based Object-Centric Image Segmentation Quality Evaluation"**

Published in *ACM Digital Library*.

**[Link to the paper](https://dl.acm.org/doi/10.1145/3696409.3700238)**

---

## Abstract

Existing segmentation quality evaluation measures often fail to adequately assess boundary variations and shape consistency. To address these issues, we propose **Shape Solidity based Full Band Intersection-over-Union (S2FB IoU)**, a novel boundary-based object-centric segmentation quality evaluation measure. This approach extends beyond pixel-wise comparison by:

- Integrating intricate boundary details.
- Effectively evaluates the boundary variations.
- Maintaining the shape solidity of the boundary bands.

We also introduce **S2FB Average Precision (S2FB AP)**, an extension of S2FB IoU for instance segmentation tasks and validate its performance on various datasets.

---

## SegAtlas: Object Segmentation Quality Evaluation Tool

Evaluating the quality of segmentation results can often be an intricate task, requiring a deep understanding of various metrics and methodologies. Traditional evaluation methods often involve cumbersome command-line interfaces and manual inspection of results through terminal outputs.

**SegAtlas** is an object segmentation quality evaluation tool that streamlines the evaluation process by eliminating the need for manual commands and terminal-based analysis.

### Features

- **Object Segmentation Quality Assessment**: Compare one or multiple ground truth and segmentation result images using the supported metrics (Mask IoU, Boundary IoU, and S2FB IoU) and conduct error analysis. This feature is labeled as "Image Evaluation" in the SegAtlas app.
- **Comprehensive Instance Segmentation Quality Assessment**: Assess quality based on entire COCO datasets or specific subsets of any segmentation method using the supported metrics. This feature is labeled as "Dataset Evaluation" in the SegAtlas app.
- **Solidity Assessment**: Dive deeper into the comparison of ground truth and segmentation result masks by analyzing solidity ratios and visualizing convex hulls.

### How to Use

SegAtlas supports three metrics: Mask IoU, Boundary IoU, and S2FB IoU. Users can find the app (in `.exe` format) in the **Releases** section of this repository. To get started:

1. Download and install the SegAtlas application from the [Releases](https://github.com/Raphael-Team-IVP/s2fb-iou/releases) section.
2. Launch the application.
3. Refer to the "User Guide" provided within the app for detailed instructions on usage.

---

## Citation

If you find **S2FB IoU** or **SegAtlas** helpful in your research or wish to reference the results presented in our work, please use the following BibTeX entry:

```bibtex
@inproceedings{10.1145/3696409.3700238,
  author = {El Filali, Rim and Jdaba, Soufiane and Xie, Ronghui and Shi, Ran and Qiao, Tong and Qiaodong, Pan and Wu, Ting},
  title = {S2FB IoU: Improving Boundary-based Object-Centric Image Segmentation Quality Evaluation},
  year = {2024},
  isbn = {9798400712739},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  url = {https://doi.org/10.1145/3696409.3700238},
  doi = {10.1145/3696409.3700238},
  booktitle = {Proceedings of the 6th ACM International Conference on Multimedia in Asia},
  articleno = {77},
  numpages = {7},
  series = {MMAsia '24}
}
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

---

## Contact

For questions or collaborations, please contact:

- **Rim EL FILALI**: [rim.elfilali@outlook.com](rim.elfilali@outlook.com), [@Rima119](https://github.com/Rima119)
