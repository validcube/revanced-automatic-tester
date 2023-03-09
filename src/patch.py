import os

from time import time
import re

from action_to_take import action_to_take as aTT

try:
    from alive_progress import alive_bar
    import tabulate
except ImportError:
    print("Please install alive_progress using 'pip install alive-progress'")
    print("Please install tabulate using 'pip install tabulate'")


path = f"{os.getcwd()}/src/"

rvcli = path + "revanced-cli-2.20.1-dev.1-all.jar"
rvpatches = path + "revanced-patches-2.165.0-dev.9.jar"
rvintegration = path + "revanced-integrations-0.100.0-dev.7.apk"
APK = "D:/HS-Storage/Project/revanced-automatic-tester/APK"
input = "D:/HS-Storage/Project/revanced-automatic-tester/APK/Input"
output = "D:/HS-Storage/Project/revanced-automatic-tester/APK/Output"
arguments = ""
file = ""

verbose = True

rvcli_info = re.search(r"cli-(\d+\.\d+\.\d+-\w+\.\d+)", rvcli)
rvpatches_info = re.search(r"patches-(\d+\.\d+\.\d+-\w+\.\d+)", rvpatches)
rvintegration_info = re.search(
    r"integrations-(\d+\.\d+\.\d+-\w+\.\d+)", rvintegration)

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

                cmd = f"java -jar {rvcli} -a \"{input}/{file}\" -o \"{output}/{file}\" -b \"{rvpatches}\" -m \"{rvintegration}\" {arguments} -c"
                os.system(cmd)

                print("\n")

                actionToTake = aTT[1]
                patching_status = "✅ Patching successful"

                apk_info.append(
                    (apk_name, version, patching_status, actionToTake))
                
                print(f'Took {time()-ds} seconds to finish patching {file}')
            except OSError or Exception as error:
                print(error)
                print(
                    f'Error: Took {time()-ds} seconds to finish patching {file}')
                patching_status = f"❎ Patching failed | {error}"
                action_to_take = aTT[4]
                apk_info.append(
                    (apk_name, version, patching_status, action_to_take))

    return apk_info


def format_output(apks, style="github"):
    print(tabulate.tabulate(apks, headers=[
          "APK name", "Version", "Status", "Action"], tablefmt=style))
    print(tabulate.tabulate([["ReVanced CLI", rvcli_info.group(1)], ["ReVanced Patches", rvpatches_info.group(1)], [
          "ReVanced Integrations", rvintegration_info.group(1)]], headers=["Tool", "Version"], tablefmt="github"))


ts = time()
apk_info = patch(input)
format_output(apk_info, "github")

# with alive_bar(0, title="Patching") as bar:
#    for file in os.listdir(input):
#        bar()
#        patch(file)


print(f'Took {time()-ts} seconds to finish patching all files & formatting output into a table')
