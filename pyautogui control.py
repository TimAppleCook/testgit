import pyautogui

pyautogui.PAUSE = 1

#启用自动防故障功能：将鼠标移动到屏幕的左上角来触发异常来终止脚本
pyautogui.FAILSAFE = True


width, height = pyautogui.size()
print(f"屏幕尺寸：宽度={width}，高度={height}")


x, y = pyautogui.position()
print(f"鼠标当前位置：({x}, {y})")


pyautogui.click(30, 30, button='left') 
# 在坐标(30, 30)处左键点击来打开macOS菜单


pyautogui.doubleClick(30, 30) 
# 在macOS菜单处双击左键

#鼠标右键点击
pyautogui.rightClick(30, 30)


pyautogui.dragTo(100, 100, button='left') 
#将鼠标拖拽到坐标(100, 100)处，打开sublime text的changelog选项
 
screenshot = pyautogui.screenshot()
screenshot.save("screen.png")

print("演示完成。")
