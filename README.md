<a href="https://www.buymeacoffee.com/ajayagrawal" title="Buy me a Coffee"> ![Banner](https://user-images.githubusercontent.com/94609372/232104964-3c0991c9-d50b-4e79-8b1a-8273212ad134.jpg) </a>

<h1 align="center">🌟 Convert-My-Images 🌟</h1> <p align="center"><b>👑 An Open Source Project 👑 Built with Python 🐍</b></p> <br><br>
<p align="center"><repo-desc></p>

<p align="center">
<a href="https://github.com/ajayagrawalgit/Convert-My-Images/blob/master/LICENSE" title="License">
<img src="https://img.shields.io/github/license/ajayagrawalgit/Convert-My-Images?label=License&logo=Github&style=flat-square" alt="Convert-My-Images License"/>
</a>
<a href="https://github.com/ajayagrawalgit/Convert-My-Images/fork" title="Forks">
<img src="https://img.shields.io/github/forks/ajayagrawalgit/Convert-My-Images?label=Forks&logo=Github&style=flat-square" alt="Convert-My-Images Forks"/>
</a>
<a href="https://github.com/ajayagrawalgit/Convert-My-Images/stargazers" title="Stars">
<img src="https://img.shields.io/github/stars/ajayagrawalgit/Convert-My-Images?label=Stars&logo=Github&style=flat-square" alt="Convert-My-Images Stars"/>
</a>
<a href="https://github.com/ajayagrawalgit/Convert-My-Images/issues" title="Issues">
<img src="https://img.shields.io/github/issues/ajayagrawalgit/Convert-My-Images?label=Issues&logo=Github&style=flat-square" alt="Convert-My-Images Issues"/>
</a>
<a href="https://github.com/ajayagrawalgit/Convert-My-Images/pulls" title="Pull Requests">
<img src="https://img.shields.io/github/issues-pr/ajayagrawalgit/Convert-My-Images?label=Pull%20Requests&logo=Github&style=flat-square" alt="Convert-My-Images Pull Requests"/>
</a>
<a href="https://github.com/ajayagrawalgit/Convert-My-Images" title="Repo Size">
<img src="https://img.shields.io/github/repo-size/ajayagrawalgit/Convert-My-Images?label=Repo%20Size&logo=Github&style=flat-square" alt="Convert-My-Images Repo Size"/>
</a>


<h3 align="center">💻 Compatible with all the Linux Distros and MacOS 💻<h3>
<p align="center"><b>Specifically Tested on MacOS, RHEL and Ubuntu</b></p>


<br><br>




## 🛰️ Description / How the tool works ?
Language: `Python` <br>
Libraries Used: `PILLOW`, `os`, `sys`<br>

<br>

**FAQs:**
1. Can I use this tool to convert a Single Image  ?  <br>
_Yes you can ! But as this tool is made specifically for **Bulk Image Conversions**, you need to create a Directory/Folder in which you store that one single image to convert and give the paths accordingly._

2. How is it different from any other Image Converters which are Popular in Market ?  <br>
 _Offcourse ! Softwares like XnConvert, Adapter & Pixillion Image Converter Software, etc have a different place all together that cannot be denied and this tool is not at all a competition to those in any way. Consider this tool as a utility which you can may be configure in your linux/windows "servers" to automate the Image Conversion tasks/jobs if you have any of such requirements. As this is made using one of the most robust languages "Python", it can easily handle bulk conversions. Also, Cherry on the cake, it's an Open Source Software_ 😊

 <br>
 
**For Better Understanding, Here's a Quick Description for Convert-My-Images:**

The tool accepts 4 parameters: <source_path> <destination_path> <initial_format> <final_format>
Source Path: The path where all the Images you want to convert as stored.
Destination Path: The path where you want to store your Converted Images.
Initial Format: Now, the source Path can have multiple images having formats of more than one type. Here you need to specify the type "you" need the conversion for.
Final Format: This is the format you want the Images to be converted.

> Note: Please make sure you don't give the format names with a dot (.). For example, if you want to convert all the jpg images to png. the command should be like `convertmyimages /path/to/source/ /path/to/destination/ jpg png`

<br>

I hope you find the Description useful. If you have any further questions, Please feel free to reach out and details for that are in _Know Me More_ section below.

Have a great day ahead 🥂 


<br><br>


## 🛠️ Installation Steps (All Linux Distros and MacOS)

#### 1. Clone the Repository

```Bash
git clone https://github.com/ajayagrawalgit/Convert-My-Images.git
```

<br>

#### 2. Go Inside the Cloned Repository and Change some Permissions (Changing permissions are required for some OS Types)

```Bash
cd Convert-My-Images
chmod 755 *
```

<br>


#### 3. Just run the Install Script

```Bash
./install.sh
```

<br>


<br>

<br>



## 🛠️ Installation Steps (Windows)
> Note: Make sure that GIT Works and you have Python 3 installed on your machine. If not, please download and install git from <a href="https://git-scm.com/download/win">here</a> and Python from <a href="https://www.python.org/downloads/windows/">here</a>. Once downloaded and Installed, Please follow the steps below:

#### 1. Clone the Repository

```Bash
git clone https://github.com/ajayagrawalgit/Convert-My-Images.git
```

<br>

#### 2. Go Inside the Cloned Repository and Run the Python File directly using the command below:

```Bash
cd /d Convert-My-Images/src
python3 main.py
```
> Above Command will display how to use the tool.

<br>

As we're running the Python file directly here. We don't need to actually Install the tool on our machine. If you need step by step instructions how to set up python on your windows machine. I found this website quite good. You can definitely refer to <a href="https://www.tutorialspoint.com/how-to-install-python-in-windows">this link</a>.

Also, if you don't want to install Git as well on your Machine, you can also consider downloading the package as a zip file directly from the GitHub itself. Refer the instructions for the same from <a href="https://sites.northwestern.edu/researchcomputing/resources/downloading-from-github/#:~:text=Without%20Git&text=To%20do%20this%2C%20go%20to,likely%20in%20your%20Downloads%20folder.">here</a>.




<br><br>






<br><br>

## ❗ How to Use ? 🦾
 
> Using the tool is pretty easy to be honest 💫 Please read the instructions below according to your OS:️

### For all Linux Distros and MacOS:
**For help:**
```Bash
convertmyimages -h
OR 
convertmyimages --help
```
<br>

**Tool Syntax:**
```Bash
convertmyimages <source_path> <destination_path> <initial_format> <final_format>
```
<br>

**Examples:**
```Bash
$> convertmyimages /Users/ajay.agrawal/Downloads /Users/ajay.agrawal/Documents jpg png
$> convertmyimages /Users/ajay.agrawal/Downloads ConvertedImages png gif
```

_Example No. 1_ is pretty self-explanatory. It will convert all the Images of the extension `.jpg` stored in `/Users/ajay.agrawal/Downloads` and save the converted Images to `/Users/ajay.agrawal/Documents`

_Example No. 2_ is a little different. Here you can see that, The destination path is just a Name. Which may or may not be there on your present working directory. If it is present there, Offcourse the script will choose that as a destination path and even if it is not, the tool will create a directory of the name `ConvertedImages` and save the Converted Images of `/Users/ajay.agrawal/Downloads` to `ConvertedImages`.

Don't worry ! Whatever is the case. Once you run the tool. You don't have to search for the location where the tool is saving the files as it'll provide you the path what it chooses to save the files.

<br><br>

### For Windows:
**Move to the `src` folder and execute `main.py` like stated below:**
**For help:**
```cmd
cd /d Convert-My-Images/src
```
```Bash
python3 main.py -h
OR
python3 main.py --help
```
<br>

**Tool Syntax (Remains the same):**
```Bash
convertmyimages <source_path> <destination_path> <initial_format> <final_format>
```
<br>

**Examples:**
```cmd
\Convert-My-Images\src>   python3 main.py D:\MyImages D:\MyImages_Converted
\Convert-My-Images\src>   python3 main.py D:\MyImages MyConvertedImages
```

<br><br>

 
 
<br><br>
## 🧶 Supported Image Formats
#### Converts Images from and to below formats:
- PNG
- JPEG
- PPM
- GIF
- TIFF
- BMP

<br>

<br>

## 🎊 Future Updates

- [ ] Add support for more Image Formats.
- [ ] Better Path Handling according to the OS Type.
- [ ] Beautify the text displayed on the terminal.
 
 <br>
 <br>
 
 
 ## 🧑🏻 Know Me More
Developer - <b> Ajay Agrawal </b>
<br>
- 🌌 [Profile](https://github.com/ajayagrawalgit "Ajay Agrawal")
- 🏮 [Email](mailto:ajayagrawalhere@gmail.com?subject=Hi%20from%20<repo-email> "Hi!")
- 🐦 [Twitter Bot (@mickbotsays)](https://twitter.com/mickbotsays)

<br>
<br>
<h2 align="center"> 🤝 Support Me 🤝 <h2>
<p align="center">
<a href="https://www.buymeacoffee.com/ajayagrawal" title="Buy me a Coffee"><img src="https://user-images.githubusercontent.com/94609372/232127833-d03502af-baf2-46e3-a045-0f7c84531a61.png" alt="Buy me a Coffee"/></a>
</p>
<br><br>
<h4>
<p align="center"> Made with ♥️ in India </p>
<br>
<h4>


