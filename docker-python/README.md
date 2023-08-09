# docker-python
---

- Kaggle Notebooks allow users to run a Python Notebook in the cloud against our competitions and datasets without having to
  download data or set up their environment.
- This repository includes the Dockerfile for building the CPU-only and GPU image that runs Python Notebooks on Kaggle.
> - Dockerfile: It is a text file that contains instructions to build a Docker container image.  
> - Docker container image: It is a lightweight, standalone, and executable software package that includes everything needed to
> run a piece of software, including the code, runtime (Python Runtime: interpreter), libraries, system tools, and settings.  
> - CPU-only Image: This Docker image is designed to run on systems with only a central processing unit (CPU).  
> - GPU Image: This Docker image is optimized to run on systems equipped with a GPU. It includes additional software and libraries
> that leverage the GPU's parallel processing capabilities for computationally intensive tasks, such as training deep learning  
 models. 
- Our Python Docker images are stored on the Google Container Registry
