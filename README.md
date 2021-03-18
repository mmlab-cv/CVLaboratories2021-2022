# Computer Vision Laboratories
Welcome to the Computer Vision 2021 laboratories GitHub repository. Here you will find all the information and the material needed for the laboratories lectures that will come.
The repository will be updated periodically with the material for the current lab. 
Please arrive at the lectures with the repository up-to-date on your machine, so that lectures can flow smoothly.

## Requirements
The laboratory exercises will all be written in Python (v3.6 or higher, with VisualStudioCode as IDE) and the following packages will be required:
	- OpenCV with contrib
	- Numpy (should be already installed as OpenCV dependency)
	- Open3D for the PointCloud/Mesh section

In order to install a Python package, you need to use the `pip` package manager (`pip3` if you are using the `python3` command) with this command: `pip install *package_name*`. The names of the required packages are:
- `opencv-python`
- `opencv-contrib`
- `numpy`
- `open3d`

## Material

The required material for the laboratories is contained in the `material` folder on the root of this repository. Inside, you will find:
- `video.mp4`: test video
- `google.jpg`: test image
- `00001640.ply`: a PointCloud of the Panoptic dataset
- `bunny`: folder containing the Bunny mesh of the Standford 3D Scanning Repository

## Virtual Machine
In addition, a virtual machine with all the requirements installed and tested as well as with this repository already cloned has been created. It can be downloaded at the following link:

[Virtual Machine with Ubuntu 18.04 LTS (Bionic Beaver)]()

VM credentials:
- **USER**: mmlab
- **PWD**: mmlab


### Extra

Inside the Virtual Machine there will also be a compiled and working version of OpenCV C++ if any of you is curious and want to try it out!

#
> **NOTE1:** For those of you who are not familiar with GitHub, be careful when performing the `pull` action from the repository! Before  doing it, move the code you wrote to another folder or you will lose its content. The `pull` action will overwrite everything there is inside it.

> **NOTE2:** If you experience any kind of trouble running the VirtualMachine do the following steps:
> *1*: https://lmgtfy.app/?q=how+to+run+a+virtual+machine
> *2*: Google it again, maybe with a smarter choice of words. 
> *3*: Maybe you should check this [link](https://support.google.com/websearch/answer/134479?hl=en) out! Or maybe [this](https://www.pcmag.com/how-to/23-google-search-tips-youll-want-to-learn) one!
> *4*: Ask a colleague for help, teamwork always wins 
> *5*: Beg a colleague for help, he/she does not bite, at most you will be asked money
> *6*: Google it one last time, it never hurts
> *7*: Ask the TA for help, show that you tried and help will be provided

> **NOTE3** If you feel confident with coding/git/computer science in general you can avoid using the VM and setup the environment on your local machine, following the above explained steps. Please note that very little help will be provided by the TA in this case

