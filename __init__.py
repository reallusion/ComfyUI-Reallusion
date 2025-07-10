from .nodes import *

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "core": Core,
    "control_net": ControlNet,
    "additional_image": AdditionalImage,
    "upscale_data": UpscaleData,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "core": "RL AI Render UI Core",
    "control_net": "RL Set ControlNet",
    "additional_image": "RL Set Reference Image",
    "upscale_data": "RL Set Upscale Data",
}