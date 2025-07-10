## Reallusion ComfyUI Custom Nodes

This repository contains custom nodes for ComfyUI designed specifically for handling Reallusion-related assets such as Character Creator and iClone image and video files. 
These nodes are intended to be used as backend components that communicate and operate through the AI Render Plugin interface of iClone or Character Creator, 
enabling a seamless integration between ComfyUI's powerful image/video generation capabilities and Reallusion’s animation tools.
By bridging ComfyUI with iClone/Character Creator’s AI Render Plugin, these nodes facilitate workflows where AI-assisted content generation can be controlled, 
customized, and rendered directly from within Reallusion software environments.

## Features

AI Render UI Core Node
 Handles Reallusion output image or video files with options for frame rate, positive and negative prompts, sampling steps, CFG scale, seed, denoising strength, model selection, and audio path. 
It processes inputs and parameters passed via the AI Render Plugin interface, enabling direct control from iClone or Character Creator.


ControlNet Node
  Provides settings for ControlNet model type, input path, activation state, strength, and effect range. 
ControlNet configurations are managed in coordination with Reallusion’s plugin workflow to enhance pose, depth, normal, 
or edge (Canny) guidance during rendering. Currently, it supports four ControlNet types: Pose, Depth, Normal, and Canny.


Additional Image Node
  Additional Image Node supports various extra image inputs with different weight types (like style transfer or linear blending). 
It works well for overlay styles such as IPAdapter and can also be used to input multiple reference images at once in the same workflow, allowing flexible guidance in rendering.


Upscale Data Node
  Allows configuration of output upscale width and height, reflecting scaling options set from within the Reallusion AI Render Plugin interface.


## Installation

Copy ComfyUI-Reallusion folder into your ComfyUI custom nodes directory (usually ComfyUI/custom_nodes/).


Launch ComfyUI; the nodes will appear under the category Reallusion.


##Usage


These nodes are designed to be controlled primarily through the AI Render Plugin of iClone or Character Creator, which sends parameters and file paths to ComfyUI via these nodes.


All media paths are relative to the input directory, matching the structure expected by the AI Render Plugin.