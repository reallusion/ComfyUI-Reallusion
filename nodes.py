import os
from typing import Dict, Any, Tuple
import folder_paths

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any = AnyType("*")

class Core:
    """
    Reallusion Core 節點用於處理 CC/iClone 相關的圖片檔案
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            "required": {
                "render_output_path": ("STRING", {
                    "default": "", 
                    "multiline": False
                }),
                "input_type": (["video", "image"],),
                "output_type": (["video", "image"],),
                "frame_rate": ("INT", {
                    "default": 12,
                    "min": 1,
                    "max": 120
                }),
                "positive_prompt": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                "negative_prompt": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                # New input for steps
                "steps": ("INT", {
                    "default": 8,
                    "min": 1,
                    "max": 10000
                }),
                # New input for cfg
                "cfg": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 100.0
                }),
                "seed": ("INT", {
                    "default": 0,
                    "min": 0,
                    "max": 0xffffffffffffffff
                }),

                "denoise": ("FLOAT", {
                    "default": 0.5,
                    "min": 0.0,
                    "max": 1.0
                }),

                "select_model": ("STRING", {
                    "default": ""
                }),

                "sampler_name": ("STRING", {
                    "default": "k_lms",
                    "multiline": False
                }),

                "scheduler": ("STRING", {
                    "default": "normal",
                    "multiline": False
                }),

                "audio_path": ("STRING", {
                    "default": "",
                    "multiline": False
                }),

                "vae_model": ("STRING", {
                    "default": ""
                })
            },
        }
    
    RETURN_TYPES = ("STRING", "INT", "STRING", "STRING",
                   "INT", "FLOAT", "INT", "FLOAT",
                   any, "STRING", "STRING", any, "STRING")
    RETURN_NAMES = ("render_output_path", "frame_rate", "positive_prompt", "negative_prompt",
                   "steps", "cfg", "seed", "denoise",
                   "select_model", "audio_path", "sampler_name", "vae_model", "scheduler")
    FUNCTION = "process"
    CATEGORY = "Reallusion"
    
    def __init__(self):
        input_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input")
        controlnet_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "controlnet")
        if not hasattr(folder_paths, "input_directory"):
            folder_paths.input_directory = input_dir
        if not hasattr(folder_paths, "controlnet_directory"):
            folder_paths.controlnet_directory = controlnet_dir
    
    def process(self, render_output_path: str, input_type: str, output_type: str, frame_rate: int,
               positive_prompt: str, negative_prompt: str,
               steps: int, cfg: float, seed: int, denoise: float,
               select_model: str, sampler_name: str, scheduler: str,
               audio_path: str, vae_model: str):
        """
        處理 Reallusion 相關圖片檔案
        """
        try:
            # 處理輸入圖片路徑
            full_path = os.path.join(folder_paths.input_directory, render_output_path)
            # 處理音訊檔案路徑
            audio_full_path = os.path.join(folder_paths.input_directory, audio_path)
            
            print(f"Input image path: {full_path}")
            print(f"Input audio path: {audio_full_path}")
            print(f"Sampler name: {sampler_name}")
            print(f"Denoise: {denoise}")

            print(folder_paths.input_directory)
            # 檢查必要檔案是否存在
            if not os.path.exists(full_path):
                raise FileNotFoundError(f"找不到輸入檔案: {full_path}")
            
            SELECT_MODELS = list()
            if select_model != "":
                values = select_model.split(',')
                SELECT_MODELS = values[0]

            VAE_MODELS = list()
            if vae_model != "":
                values = vae_model.split(',')
                VAE_MODELS = values[0]

            return (full_path, frame_rate, positive_prompt, negative_prompt,
                   steps, cfg, seed, denoise,
                   SELECT_MODELS, audio_full_path, sampler_name, VAE_MODELS, scheduler)
            
        except Exception as e:
            print(f"處理過程中發生錯誤: {str(e)}")
            raise e

class WorkflowInfo:
    """
    Reallusion Workflow Info 節點，用於提供工作流程的相關資訊
    """

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            "required": {
                "name": ("STRING", {
                    "default": "Image To Image",
                    "multiline": False
                }),
                "creator": ("STRING", {
                    "default": "Reallusion",
                    "multiline": False
                }),
                "tags": ("STRING", {
                    "default": "Image",
                    "multiline": False
                }),
                "special_tag": ("STRING", {
                    "default": "Image Workflow",
                    "multiline": False
                })
            }
        }

    RETURN_TYPES = ()  # 空元組，表示沒有輸出
    RETURN_NAMES = ()  # 空元組，表示沒有輸出名稱
    FUNCTION = "process"
    CATEGORY = "Reallusion"

    def process(self, name: str, creator: str, tags: str, special_tag: str) -> tuple:
        """
        處理工作流程資訊

        Args:
            name (str): 工作流程名稱
            creator (str): 創建者
            tags (str): 標籤（逗號分隔的字串）
            special_tag (str): 特殊標籤

        Returns:
            tuple: 空元組，因為這個節點不需要輸出
        """
        return ()

class ControlNet:
    """
    Reallusion ControlNet 節點，用於提供 ControlNet 的相關資訊
    """
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            "required": {
                "control_net_type": (["normal", "depth", "canny", "open_pose"],),
                "control_net_path": ("STRING", {
                    "default": ""
                }),
                "control_net_state": ("BOOLEAN", {
                    "default": False
                }),
                "control_net_strength": ("FLOAT", {
                    "default": 0.0,
                    "min": 0.0,
                    "max": 1.0
                }),
                "control_net_start_percent": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": 1000000
                }),
                "control_net_end_percent": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": 1000000
                }),
            }
        }

    RETURN_TYPES = (
        "STRING", "BOOLEAN", "FLOAT", "FLOAT", "FLOAT"
    )
    RETURN_NAMES = (
        "control_net_path", "control_net_state", "control_net_strength",
        "control_net_start_percent", "control_net_end_percent",
    )
    FUNCTION = "process"
    CATEGORY = "Reallusion"

    def process(self,
                control_net_type: str,
                control_net_path: str,
                control_net_state: bool,
                control_net_strength: float,
                control_net_start_percent: float,
                control_net_end_percent: float,
                ) -> tuple:
        """
        處理 ControlNet 的相關資訊，包含路徑、狀態、強度和幀範圍
        """
        input_path = os.path.join(folder_paths.input_directory, control_net_path)

        if control_net_strength > 0 and not os.path.exists(input_path):
            raise FileNotFoundError(f"找不到 Normal 輸入檔案: {input_path}")

        return (
            input_path, control_net_state, control_net_strength,
            control_net_start_percent, control_net_end_percent,
        )

class AdditionalImage:
    """
    Reallusion AdditionalImage 節點，用於處理額外的圖片輸入和其權重
    """
    WEIGHT_TYPES = ["linear", "ease in", "ease out", "ease in-out", "reverse in-out", 
                    "weak input", "weak output", "weak middle", "strong middle",
                    "style transfer", "composition", "strong style transfer",
                    "style and composition", "style transfer precise", "composition precise"]

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            "required": {
                "name": ("STRING", {
                    "default": "additional_image",
                    "multiline": False
                }),
                "image_path": ("STRING", {
                    "default": "",
                    "multiline": False
                }),
                "weight_type": (cls.WEIGHT_TYPES,),
                "weight": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 1.0
                }),
                "active": ("BOOLEAN", {
                    "default": True
                })
            }
        }

    RETURN_TYPES = ("STRING", WEIGHT_TYPES, "FLOAT")
    RETURN_NAMES = ("image_path", "weight_type", "weight")
    FUNCTION = "process"
    CATEGORY = "Reallusion"

    def process(self, name: str, image_path: str, weight_type: str, weight: float, active: bool) -> tuple:
        """
        處理額外的圖片路徑和其權重
        
        Args:
            name (str): 額外圖片的名稱（用於在 RenderData 中識別）
            image_path (str): 額外圖片的路徑
            weight_type (str): 權重類型
            weight (float): 圖片的權重值
            
        Returns:
            tuple: (圖片完整路徑, 權重類型, 權重值)
        """
        try:
            full_path = os.path.join(folder_paths.input_directory, image_path)
            
            if not os.path.exists(full_path):
                raise FileNotFoundError(f"找不到輸入檔案: {full_path}")
            
            # 驗證 weight_type 是否為有效的 WEIGHT_TYPES 值
            if weight_type not in self.WEIGHT_TYPES:
                raise ValueError(f"無效的 weight_type: {weight_type}. 必須是以下其中之一: {', '.join(self.WEIGHT_TYPES)}")
            
            if not active:
                # 如果沒啟用，回傳空路徑、預設 weight_type、權重 0
                weight = 0

            return (full_path, weight_type, weight)
            
        except Exception as e:
            print(f"處理過程中發生錯誤: {str(e)}")
            raise e

class UpscaleData:
    """
    Reallusion UpscaleData 節點，用於處理放大尺寸的設定
    """
    
    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            "required": {
                "width": ("INT", {
                    "default": 512,
                    "min": 64,
                    "max": 8192
                }),
                "height": ("INT", {
                    "default": 512,
                    "min": 64,
                    "max": 8192
                })
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "process"
    CATEGORY = "Reallusion"

    def process(self, width: int, height: int) -> Tuple[int, int]:
        """
        處理放大尺寸的設定
        
        Args:
            width (int): 目標寬度
            height (int): 目標高度
            
        Returns:
            tuple: (寬度, 高度)
        """
        return (width, height)
