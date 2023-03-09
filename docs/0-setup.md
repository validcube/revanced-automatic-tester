# 🤖 ReVanced Automatic Patcher
Determine if you can successfully patch a APK(s)

## Setup


### 0.1 Python
First, let start off by installing Python, this program recommends at least [Python 3.10 or higher](https://www.python.org/downloads/). Once you're in the installation, don't forget to check "Add python.exe to PATH"

![](docs\assets\addToPath.png "Add Python to Path")

> **Warning** <br>
> If you forget to check "Add python.exe to PATH", See "Troubleshooting"

<details>
<summary>Troubleshooting</summary>
If you've forgot to check "Add python.exe to PATH", open the installation that you used to install Python and click on "Customise Installation" then check "Add Python to enviroment variables"

![](docs\assets\customisedInstallation.png "1. Customise Installation")
![](docs\assets\addToEnviroment.png "2. Add Python to enviroment variables")

You're good to go!
</details>

### 0.2 Java Development Kit 
Now, let install Open Java Development Kit, also known as OpenJDK! The ReVanced CLI recommends [Zulu OpenJDK 17](https://www.azul.com/downloads/?package=jdk#download-openjdk), equivalent (e.g. [Eclipse Temurin™ OpenJDK 17](https://adoptium.net/temurin/releases/)) or higher.

#### 0.3 Python Dependencies
Let's install the required dependencies to run RVAP. Open up Terminal of your choice and run `pip install -r requirements.txt` in the same directory that `requirements.txt` exist.

#### Documentation
Continue: [Using the RVAP](1-using_RVAP.md)