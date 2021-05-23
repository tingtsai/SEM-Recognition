# SEM-Recognition

[Projec description video](https://www.youtube.com/watch?v=BiHHvy-QbIQ)
[Project paper](http://cs230.stanford.edu/projects_spring_2020/reports/38856594.pdf)

Scanning Electron Microscopy (SEM) has become a powerful tool in nanoscience. Its images provide valuable morphology information and extracting contours from the images is useful for labs or semiconductor companies to evaluate their patterning capabilities. However, there is a lack of suitable tool to efficiently identify the contour of nanostructures. Previous approaches mainly applied edge detection and filtering algorithm and results are highly dependent on the quality of the images.

SEM images are usually noisy and under-resolved, though it is distinguishable to human, the contour of nanostructures extracted by the conventional numerical method are usually inaccurate and biased. (Figure 1b) Also, creating labels for given SEM images can be time-consuming and labor-intensive.

Here, we launch a label-free SEM image recognition project based on the Cycle-consistent Generative Adversarial Networks’ (Cycle GAN) network. Inspired by its ability to process unpaired training data, we will use lithography design to train the discriminator instead of using labeled data generated manually.

We propose to solve this problem with both supervised learning and unsupervised learning methods:
For the supervised learning method, we trained a CNN with labeled data (paired SEM images and labeled generated from ilastik tool) and use this network as the benchmark of our project. For the unsupervised learning method, we trained a CycleGAN with unpaired training data (SEM images and contours generated from the PhiDL packages) and compare the results with the first method. The authors of CycleGAN provide the implementation in PyTorch. The application was can be also applied to our problem the contour image can be considered as a different “style” of the polygon. We modified the data pipeline to train the network with our data, then tune the hyper-parameters and introduce new functional modules as the project proceeds.

![](/figures/detection.png)

