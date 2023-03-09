# 🤖 ReVanced Automatic Patcher
Determine if you can successfully patch a APK(s)

## How does it work?
`RVAP -------> Get App's version -------> Download APK -------> Error checking -------> Await test from Human`
We'll refer to ReVanced Automatic Patcher as RVAP. When RVAP runs, it will grab the latest version of the app and download the APK. Then, it will patch the APK with recommended settings, which can be customized to your preferences. RVAP will check for errors; if any are found, the app will repeat the process but downgrade the version until it finds a working one. Once this is done, the outputted APK will be located under `/output/*.apk`, awaiting testing by a human to validate if the patches are working as intended.

## About repository
This repository is listed under **Pun Experiments**, label `autoPatcher` on `reVanced` category. Please use `reVanced-autoPatcher` for querying internal information.

###### Ignore that