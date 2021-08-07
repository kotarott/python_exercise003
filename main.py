import eel
import numpy as np

eel.init("web")
# jsの結果をpythonで受け取る①　処理後
eel.js_function()(lambda val: print(val + " from JavaScript"))

eel.start("main.html")

# jsの結果をpythonで受け取る②　同期
# test = eel.js_function()()
