# 🤖 ReVanced Automatic Patcher
Determine if you can successfully patch an APK(s)

## Setup


### 0.1 Python
First, let's start by installing Python, this program recommends at least [Python 3.9 or higher](https://www.python.org/downloads/). Once you're in the installation, don't forget to check "Add python.exe to PATH".

[![Add Python to Path](assets/addToPath.png "Add Python to Path")](#01-Python)

> **Warning** <br>
> If you forget to check "Add python.exe to PATH", See "Troubleshooting".

<details>
<summary>Troubleshooting</summary>
If you've forgotten to check "Add python.exe to PATH", open the installation that you used to install Python and click on "Customise Installation" then check "Add Python to environment variables".

[![1. Customise Installation](assets/customisedInstallation.png "1. Customise Installation")](#01-Python)
[![2. Add Python to environment variables](assets/addToEnviroment.png "2. Add Python to environment variables")](#01-Python)

You're good to go!
</details>

### 0.2 Java Development Kit 
Now, let's install Open Java Development Kit, also known as OpenJDK! The ReVanced CLI recommends [Azul Zulu™ OpenJDK 17](https://www.azul.com/downloads/?package=jdk#download-openjdk), equivalent (e.g. [Eclipse Temurin™ OpenJDK 17](https://adoptium.net/temurin/releases/)) or higher.

### 0.3 Python Dependencies
Let's install the required dependencies to run RVAP. Open up the Terminal of your choice and run `pip install -r requirements.txt` in the same directory where `requirements.txt` exist.

#### Documentation
Continue: [Using the RVAP](1-using_RVAP.md)
