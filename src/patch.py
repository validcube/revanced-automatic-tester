import os
# import sys
from time import time
# import multiprocessing
# import subprocess
import re

from src.actionToTake import actionToTake as aTT

try:
    from alive_progress import alive_bar
    import tabulate
except ImportError:
    print("Please install alive_progress using 'pip install alive-progress'")
    print("Please install tabulate using 'pip install tabulate'")


path = f"{os.getcwd()}/src/"

rvcli = path + "revanced-cli-2.20.1-dev.1-all.jar"
rvpatches = path + "revanced-patches-2.165.0-dev.9.jar"
rvintegration = path+"revanced-integrations-0.100.0-dev.7.apk"
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
if experimental == True:
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

                # apk_name = file.split("_")[0]
                # version = re.search(r"_([\d.]+)-\d+_minAPI", file).group(1)
                actionToTake = aTT[1]
                patching_status = "✅ Patching successful"

                apk_info.append(
                    (apk_name, version, patching_status, actionToTake))
                print(f'Took {time()-ds} seconds to finish patching {file}')
            except OSError or Exception as e:
                print(e)
                print(
                    f'Error: Took {time()-ds} seconds to finish patching {file}')
                patching_status = f"❎ Patching failed | {e}"
                actionToTake = aTT[4]
                apk_info.append(
                    (apk_name, version, patching_status, actionToTake))

    return apk_info


def validate():
    for file in os.listdir(input):
        with alive_bar(1, title=f"Validating file {file}") as bar:
            if file.endswith(".apk") or file.endswith(".keystore"):
                bar()

    print(f"✅ Operation done! Every file is valid!")


def format_output(apk_info, style="github"):
    # apk_info = []

    # for file in os.listdir(output_directory):
    #    if file.endswith(".apk"):
    #        version = re.search(r"_([\d.]+)-\d+_minAPI", file).group(1)
    #        apk_name = file.split("_")[0]
    #        actionToTake = "✋ Require manual testing of the APK to ensure all patches are applied correctly"
    #        patching_status = "✅ Patching successful"
    #        apk_info.append((apk_name, version, patching_status, actionToTake))
    print(tabulate.tabulate(apk_info, headers=[
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

# run patching in parallel using 4 processes
# if __name__ == '__main__':
#    processes = [multiprocessing.Process(target=patch, args=(file,)) for file in os.listdir(input)]
#    # start all processes
#    for process in processes:
#        process.start()
#        sleep(2.5)
#    # wait for all processes to complete
#    print('Waiting for the process...')
#    for process in processes:
#        process.join()

# TODO
# - Add support for human readable format
# - Add support for GitHub MarkDown table format
