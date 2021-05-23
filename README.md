# Label-free SEM Content Recognition with CycleGAN

[Description video](https://www.youtube.com/watch?v=BiHHvy-QbIQ) <br>
[Paper](http://cs230.stanford.edu/projects_spring_2020/reports/38856594.pdf) <br>

Scanning Electron Microscopy (SEM) has become a powerful tool in nanoscience. Its images provide valuable morphology information, and extracting contours from the images is helpful for labs or semiconductor companies to evaluate their patterning capabilities. However, there is a lack of a suitable tool to identify the contour of nanostructures efficiently. Previous approaches mainly applied edge detection and filtering algorithm, and results are highly dependent on the quality of the images.
SEM images are usually noisy and under-resolved. Though they are distinguishable to humans, the contour of nanostructures extracted by the conventional numerical method is generally inaccurate and biased. (Figure 1b) Also, creating labels for given SEM images can be time-consuming and labor-intensive.
Here, we launch a label-free SEM image recognition project based on the Cycle-consistent Generative Adversarial Networks’ (Cycle GAN) network. Inspired by its ability to process unpaired training data, we used lithography design to train the discriminator instead of using labeled data generated manually.
We proposed to solve this problem with supervised learning and unsupervised learning methods: For the supervised learning method, we trained a CNN with labeled data (paired SEM images and labeled generated from ilastik tool) and used this network as the benchmark for our project. We introduced a CycleGAN with unpaired training data (SEM images and contours generated from the PhiDL packages) and compared the results with the first method for the unsupervised learning method. The contour image can be considered a different “style” of the polygon. We modified the data pipeline to train the network with our data, tuned the hyper-parameters, and demonstrated the network capabilities for label-free nanostructure detection.

![](/figures/detection.png)

![](/figures/CycleGAN.png)
