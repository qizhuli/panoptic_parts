# Panoptic Parts datasets for Holistic Scene Understanding

[![Documentation Status](https://readthedocs.org/projects/panoptic-parts/badge/?version=latest)](https://panoptic-parts.readthedocs.io/en/latest/?badge=latest)

This repository contains code and tools for reading, processing, and visualizing *Cityscapes-Panoptic-Parts* and *PASCAL-Panoptic-Parts* datasets. We created these datasets by extending two established datasets for image scene understanding, namely [Cityscapes](https://github.com/mcordts/cityscapesScripts "Cityscapes") and [PASCAL](http://host.robots.ox.ac.uk/pascal/VOC/voc2010/ "PASCAL") datasets.

Detailed description of the datasets and various statistics are presented in our technical report in [arxiv](https://arxiv.org/abs/2004.07944 "arxiv.org"). Please cite us if you find our work useful and you use it for your research:

```bibtex
@article{meletis2020panopticparts,
    title = {Cityscapes-Panoptic-Parts and PASCAL-Panoptic-Parts datasets for Scene Understanding},
    author = {Panagiotis Meletis and Xiaoxiao Wen and Chenyang Lu and Daan de Geus and Gijs Dubbelman},
    type = {Technical report},
    institution = {Eindhoven University of Technology},
    date = {16/04/2020},
    url = {https://github.com/tue-mps/panoptic_parts},
    eprint={2004.07944},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```

<a href="https://www.tue.nl/en/research/research-groups/signal-processing-systems/mobile-perception-systems-lab"><img src="readme/mps_logo.png" height="100" alt="MPS"></a> &emsp; <a href="https://www.tue.nl"><img src="readme/tue_logo.jpg" height="100" alt="TU/e"></a>

## Cityscapes-Panoptic-Parts

![Image](readme/aachen_000012_000019_leftImg8bit.jpg "Image") | ![Image](readme/aachen_000012_000019_uids_pids_colored.png "Image")
---- | ----
![Image](readme/frankfurt_000001_011835_leftImg8bit.jpg "Image") | ![Image](readme/frankfurt_000001_011835_uids_pids_colored.png "Image")

## PASCAL-Panoptic-Parts

![Image](readme/2008_000393.jpg "Image") | ![Image](readme/2008_000393_colored.png "Image") | ![Image](readme/2008_000716.jpg "Image") | ![Image](readme/2008_000716_colored.png "Image")
---- | ---- | ---- | ----
![Image](readme/2008_007456.jpg "Image") | ![Image](readme/2008_007456_colored_repainted.png "Image") | ![Image](readme/2010_002356.jpg "Image") | ![Image](readme/2010_002356_colored.png "Image")

## Code usage

We provide a public, backwards compatible API, which allows easier bug fixes and functionality updates. We suggest that the users update their local clone of this repository frequently by pulling the master branch. The list can be found here: [Public API](API.md).

All functions and arguments named with the preffix 'experimental_' or with an '_' do not
belong to the stable API and may change.

## Hierarchical format and labels encoding

We encode three levels of labels: semantic, instance, and parts in a single image-like file. The hierarchical panoptic encoding of the labels is explained here: [Label format](LABEL_FORMAT.md). Labels for both datasets follow this format.

## Ground Truth usage cases

We provide for each image a single (image-like) ground truth file encoding semantic-, instance-, and parts- levels annotations. Our compact [label format](LABEL_FORMAT.md) together with [_decode_uids_](utils/format.py) function enable easy decoding of the labels for various image understanding tasks including:

```Python
# labels: Python int, or np.ndarray, or tf.Tensor, or torch.tensor

# Semantic Segmentation
semantic_ids, _, _ = decode_uids(labels)

# Instance Segmentation
semantic_ids, instance_ids, _ = decode_uids(labels)

# Panoptic Segmentation
_, _, _, semantic_instance_ids = decode_uids(labels, return_sids_iids=True)

# Parts Segmentation / Parts Parsing
_, _, _, semantic_parts_ids = decode_uids(labels, return_sids_pids=True)

# Instance-level Parts Parsing
semantic_ids, instance_ids, parts_ids = decode_uids(labels)

# Parts-level Panoptic Segmentation
_, _, _, semantic_instance_ids, semantic_parts_ids = decode_uids(labels, return_sids_iids=True, return_sids_pids=True)

```

## Requirements

Tested with the following configuration (Linux system):

* Required
  * Python >= 3.6
  * Numpy >= 1.19.4
  * Pillow >= 8.0.1
  * SciPy >= 1.5.4
  * PyYAML >= 5.3.1

* Optional
  * Tensorflow >= 2.4.0 (for label format handling)
  * Pytorch >= 1.7.0 (for label format handling)
  * Matplotlib >= 3.3.0 (for visualization scripts)
  * panopticapi (for PASCAL visualization script)

## Contact

Please feel free to contact us for any suggestions or questions:

* Panagiotis Meletis: **p**[DOT]**c**[DOT]**meletis**[AT]**tue.nl**
* Xiaoxiao (Vincent) Wen: **wenxx10**[AT]**gmail.com**
