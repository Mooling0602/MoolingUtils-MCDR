## This module need MCDR plugin env.
from . import *
from typing import Optional


psi = ServerInterface.psi()

def tr(tr_key: str, return_str: Optional[bool] = True):
    '''
    [zh_CN]
    对`PluginServerInterface.rtr()`进行优化，提高翻译效率。

    参数:
        tr_key (str): 原始或简化后的翻译键，使用#做前缀以指定原始的翻译键
        return_str (可选[bool]): 是否尝试转换成字符串减少出错

    返回:
        translation: RTextMCDRTranslation组件
        或tr_to_str: 字符串
    '''
    # [zh_CN]
    # 动态获取插件元数据信息，避免解析错误
    # 注意：语言文件的翻译键必须以插件id开头，否则请参考参数`tr_key`的前缀用法
    plgSelf = psi.get_self_metadata()
    if tr_key.startswith(f"{plgSelf.id}"):
        translation = psi.rtr(f"{tr_key}")
    else:
        # [zh_CN]
        # 使用此前缀代表非本插件的翻译键，则翻译时不会附加本插件的ID，避免错误
        # 尚不支持自定义前缀
        if tr_key.startswith("#"):
            translation = psi.rtr(tr_key.replace("#", ""))
        else:
            translation = psi.rtr(f"{plgSelf.id}.{tr_key}")
    if return_str:
        tr_to_str: str = str(translation)
        return tr_to_str
    else:
        return translation
    
__all__ = ["tr"]
import sys
sys.modules[__name__] = tr