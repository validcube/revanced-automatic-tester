"""Module that display the recommended action to take after the patching and validation process"""

status_message = []
status_message.append("✅ Successful patching & validation")
status_message.append("✋ Require manual testing of the APK to ensure all patches are applied correctly")
status_message.append("✋ Skipped")
status_message.append("❎ Unknown error")
status_message.append("❎ Require restart")
status_message.append("🙅 Validation failed")
status_message.append("🙅 Validation failed, some patches applied correctly")
