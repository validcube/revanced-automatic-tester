"""Module that patch the APKs... in the future"""

import os

from time import time
import re

try:
    from status_message import status_message
except ImportError:
    from status_message import status_message
    print("Using workaround to import status_message module")

try:
    # from alive_progress import alive_bar
    import tabulate
except ImportError:
    print("Please install alive_progress using 'pip install alive-progress'")
    print("Please install tabulate using 'pip install tabulate'")


path = f"{os.getcwd()}/src/"

rvcli = path + "revanced-cli-2.20.1-all.jar"
rvpatches = path + "revanced-patches-2.167.0.jar"
rvintegration = path + "revanced-integrations-0.102.0-dev.1.apk"
APK = "D:/HS-Storage/Project/revanced-automatic-tester/APK"
input_location = "D:/HS-Storage/Project/revanced-automatic-tester/APK/Input"
output_location = "D:/HS-Storage/Project/revanced-automatic-tester/APK/Output"
arguments = ""
file = ""

verbose = True
version = "0.0.11"
variant = "dev_python_aapt2"
emoji = "🤖"

rvcli_info = re.search(r"cli-(\d+\.\d+\.\d+)", rvcli)
rvpatches_info = re.search(r"patches-(\d+\.\d+\.\d+)", rvpatches)
rvintegration_info = re.search(
    r"integrations-(\d+\.\d+\.\d+)", rvintegration)

experimental = True
if experimental is True:
    arguments = "--experimental"


def patch(input_directory):
    apk_info = []

    for file in os.listdir(input_directory):
        if file.endswith(".apk"):
            apk_name = file.split("_")[0]
            version = re.search(r"_([\d.]+)-\d+_minAPI", file).group(1)
            ds = time()
            try:
                action_to_take = status_message[1]
                patching_status = status_message[7]

                cmd = f"java -jar {rvcli} -a \"{input_location}/{file}\" -o \"{output_location}/{file}\" -b \"{rvpatches}\" -m \"{rvintegration}\" {arguments} -c"
                os.system(cmd)

                print("\n")

                apk_info.append(
                    (apk_name, version, patching_status, action_to_take))

                print(f'Took {time()-ds} seconds to finish patching {file}')
                print("\n")
            except Exception as error:
                print(error)
                print(
                    f'Error: Took {time()-ds} seconds to finish patching {file}')
                patching_status = f"{status_message[8]} | {error}"
                action_to_take = status_message[4]
                apk_info.append(
                    (apk_name, version, patching_status, action_to_take))

    return apk_info


def format_output(apks, style="github"):

    # Print APK status
    print(tabulate.tabulate(apks, headers=[
          "APK name", "Version", "Status", "Action"], tablefmt=style))
    
    # Print ReVanced tools version
    print(tabulate.tabulate([["💻 ReVanced CLI", rvcli_info.group(1)], ["🧩 ReVanced Patches", rvpatches_info.group(1)], [
          "🔩 ReVanced Integrations", rvintegration_info.group(1)], [f"{emoji} (unofficial) ReVanced Automatic Patcher", f'{version}-{variant}']], headers=["Tool", "Version"], tablefmt=style))


ts = time()
apk_info = patch(input_location)
format_output(apk_info, "github")

# with alive_bar(0, title="Patching") as bar:
#    for file in os.listdir(input_location):
#        bar()
#        patch(file)


print(f'Took {time()-ts} seconds to finish patching all files & formatting output into a table')
