## [zh_CN]
## 将含有Minecraft格式化代码的文本在终端环境使用ANSI转义符正确渲染上文本颜色
## 需要MCDReforged的文本组件，但不需要运行在插件中也能使用
import re

from mcdreforged.minecraft.rtext.style import *


pattern = re.compile(r'(§[0-9a-fklmnor])')

def mc_to_ansi(text: str) -> str:

    mc_to_console_map = {
        color.mc_code: color.console_code
        for color in RColor
        if isinstance(color, RColorClassic)
    }
    mc_to_console_map.update({
        style.mc_code: style.console_code
        for style in RStyle
        if isinstance(style, RStyleClassic)
    })
    mc_to_console_map['§r'] = Style.RESET_ALL

    def replace_code(match):
        code = match.group(1)
        return mc_to_console_map.get(code, '')

    return pattern.sub(replace_code, text)