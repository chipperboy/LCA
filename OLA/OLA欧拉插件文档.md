# OLA欧拉插件文档 (beta65)

> 当前仓库附带的新版文档文件为 `欧拉插件文档_beta65.chm`
>
> 本 Markdown 说明基于仓库当前同步的欧拉文档整理维护

---

## 目录

- **Config相关**
  - 添加数据库配置项 - SetDbConfig
  - 添加数据库配置项 - SetDbConfigEx
  - 移除数据库配置项 - RemoveDbConfig
  - 移除数据库配置项 - RemoveDbConfigEx
  - 读取数据库配置项 - GetDbConfig
  - 读取数据库配置项 - GetDbConfigEx
- **JSON**
  - 创建空的JSON对象 - JsonCreateObject
  - 创建空的JSON数组 - JsonCreateArray
  - 删除JSON对象中的键 - JsonDeleteKey
  - 向JSON数组添加元素 - JsonArrayAppend
  - 将JSON对象序列化为字符串 - JsonStringify
  - 清空JSON对象或数组 - JsonClear
  - 获取JSON对象中的值 - JsonGetValue
  - 获取JSON对象中的字符串值 - JsonGetString
  - 获取JSON对象中的布尔值 - JsonGetBool
  - 获取JSON对象中的数值 - JsonGetNumber
  - 获取JSON对象或数组的大小 - JsonGetSize
  - 获取JSON数组中的元素 - JsonGetArrayItem
  - 获取匹配图像JSON数量 - GetMatchImageAllCount
  - 解析JSON字符串 - JsonParse
  - 解析匹配图像JSON - ParseMatchImageJson
  - 解析匹配图像多结果JSON - ParseMatchImageAllJson
  - 设置JSON对象中的值 - JsonSetValue
  - 设置JSON对象中的字符串值 - JsonSetString
  - 设置JSON对象中的布尔值 - JsonSetBool
  - 设置JSON对象中的数值 - JsonSetNumber
  - 释放JSON对象 - JsonFree
- **YOLO**
  - YOLO
- **其他**
  - 从内存地址读取字符串 - GetStringFromPtr
  - 创建OLA-COM对象
  - 创建OLA对象
  - 执行cmd指令 - ExecuteCmd
  - 注册到后台 - Reg
  - 解析返回结果数量 - GetResultCount
  - 读取字符串大小 - GetStringSize
  - 释放OLA对象 - DestroyCOLAPlugInterFace
  - 释放字符串内存 - FreeStringPtr
  - 释放字节流内存 - FreeMemoryPtr
- **内存**
  - 32位整数转64位整数 - Int32ToInt64
  - 64位整数转32位整数 - Int64ToInt32
  - 写入指定地址的单精度浮点数 - WriteFloat
  - 写入指定地址的单精度浮点数 - WriteFloatAddr
  - 写入指定地址的双精度浮点数 - WriteDouble
  - 写入指定地址的双精度浮点数 - WriteDoubleAddr
  - 写入指定地址的字符串 - WriteString
  - 写入指定地址的字符串 - WriteStringAddr
  - 写入指定地址的数据 - WriteData
  - 写入指定地址的数据 - WriteDataAddr
  - 写入指定地址的数据 - WriteDataAddrFromBin
  - 写入指定地址的数据 - WriteDataFromBin
  - 写入指定地址的整数 - WriteInt
  - 写入指定地址的整数 - WriteIntAddr
  - 单精度浮点数转二进制 - FloatToData
  - 双精度浮点数转二进制 - DoubleToData
  - 字符串转二进制 - StringToData
  - 指定窗口修改内存保护属性 - VirtualProtectEx
  - 指定窗口分配内存 - VirtualAllocEx
  - 指定窗口查询内存信息 - VirtualQueryEx
  - 指定窗口释放内存 - VirtualFreeEx
  - 搜索二进制数据 - FindData
  - 搜索二进制数据 - FindDataEx
  - 搜索单精度浮点数 - FindFloat
  - 搜索单精度浮点数 - FindFloatEx
  - 搜索双精度浮点数 - FindDouble
  - 搜索双精度浮点数 - FindDoubleEx
  - 搜索字符串 - FindString
  - 搜索字符串 - FindStringEx
  - 搜索长整型数 - FindInt
  - 搜索长整型数 - FindIntEx
  - 获取模块基地址 - GetModuleBaseAddr
  - 获取模块大小 - GetModuleSize
  - 获取远程API地址 - GetRemoteApiAddress
  - 设置是否把所有内存接口函数中的窗口句柄当作进程ID - SetMemoryHwndAsProcessId
  - 读取指定地址的单精度浮点数 - ReadFloat
  - 读取指定地址的单精度浮点数 - ReadFloatAddr
  - 读取指定地址的双精度浮点数 - ReadDouble
  - 读取指定地址的双精度浮点数 - ReadDoubleAddr
  - 读取指定地址的字符串 - ReadString
  - 读取指定地址的字符串 - ReadStringAddr
  - 读取指定地址的数据 - ReadData
  - 读取指定地址的数据 - ReadDataAddr
  - 读取指定地址的数据 - ReadDataAddrToBin
  - 读取指定地址的数据 - ReadDataToBin
  - 读取指定地址的长整型数 - ReadInt
  - 读取指定地址的长整型数 - ReadIntAddr
  - 释放进程内存 - FreeProcessMemory
- **加密**
  - AES加密 - AESEncryptEx
  - AES加密简化版本 - AESEncrypt
  - AES解密 - AESDecryptEx
  - AES解密简化版本 - AESDecrypt
  - Base64编码 - Base64Encode
  - Base64解码 - Base64Decode
  - HMAC消息认证码 - HMAC
  - MD5加密 - MD5Encrypt
  - PBKDF2密钥派生函数 - PBKDF2
  - SHA系列哈希算法 - SHAHash
  - 使用RSA公钥加密 - EncryptWithRsa
  - 使用RSA公钥验证签名 - VerifySignWithRsa
  - 使用RSA私钥签名 - SignWithRsa
  - 使用RSA私钥解密 - DecryptWithRsa
  - 生成GUID - GenerateGuid
  - 生成RSA密钥 - GenerateRSAKey
  - 生成随机字节 - GenerateRandomBytes
  - 计算文件MD5哈希值 - MD5File
  - 计算文件SHA哈希值 - SHAFile
  - 转换RSA公钥 - ConvertRSAPublicKey
  - 转换RSA私钥 - ConvertRSAPrivateKey
- **图像处理**
  - 16进制格式颜色转为ARGB - Hex2ARGB
  - 16进制格式颜色转为RGB - Hex2RGB
  - ARGB颜色转为16进制格式 - ARGB2Hex
  - Canny边缘检测 - CannyEdge
  - RGB转HSV - RGB2HSV
  - RGB颜色转为16进制格式 - GetColorHex
  - RGB颜色转为16进制格式 - RGB2Hex
  - base64字符串转为图片 - Base64ToImage
  - 从路径拼接图片 - ImageStitchFromPath
  - 保存图片 - SaveImageFromPtr
  - 创建图片 - CreateImage
  - 创建拼接实例 - ImageStitchCreate
  - 加载图片 - LoadImage
  - 加载图片 - LoadImageFromRGBData
  - 加载文件夹下的所有图片 - LoadImagePath
  - 十六进制转HSV - Hex2HSV
  - 去除孤岛 - RemoveIslands
  - 取色 - GetColor
  - 图像锐化 - Sharpen
  - 图像阈值化 - Threshold
  - 图片转为base64字符串 - ImageToBase64
  - 对比颜色 - CmpColor
  - 对比颜色 - CmpColorEx
  - 对比颜色 - CmpColorHex
  - 对比颜色 - CmpColorHexEx
  - 对比颜色 - CmpColorPtr
  - 对比颜色 - CmpColorPtrEx
  - 弹窗显示图片 - ShowImage
  - 弹窗显示图片 - ShowImageFromFile
  - 形态学开运算 - MorphOpen
  - 形态学梯度 - MorphGradient
  - 形态学闭运算 - MorphClose
  - 形态学顶帽 - MorphTophat
  - 形态学黑帽 - MorphBlackhat
  - 快速ROI - FastROI
  - 截图GIF - CaptureGif
  - 截图并保存成文件 - Capture
  - 截图返回字节流 - GetScreenData
  - 截图返回字节流 - GetScreenDataBmp
  - 拷贝图片 - CopyImage
  - 拼接图片 - ConcatImage
  - 拼接图片追加 - ImageStitchAppend
  - 指定区域数据是否卡屏 - IsDisplayDead
  - 旋转图片 - RotateImage
  - 查找所有符合的颜色 - FindColorList
  - 查找所有符合的颜色 - FindColorListEx
  - 查找指定区域内的所有颜色块 - FindColorBlockList
  - 查找指定区域内的所有颜色块 - FindColorBlockListEx
  - 查找指定区域内的所有颜色块 - FindColorBlockListPtr
  - 查找指定区域内的所有颜色块 - FindColorBlockListPtrEx
  - 查找指定区域内的颜色块 - FindColorBlock
  - 查找指定区域内的颜色块 - FindColorBlockEx
  - 查找指定区域内的颜色块 - FindColorBlockPtr
  - 查找指定区域内的颜色块 - FindColorBlockPtrEx
  - 查找指定颜色范围坐标 - FindMultiColor
  - 查找指定颜色范围坐标 - FindMultiColorFromPtr
  - 查找指定颜色范围坐标 - FindMultiColorList
  - 查找指定颜色范围坐标 - FindMultiColorListFromPtr
  - 查找符合的颜色 - FindColor
  - 查找符合的颜色 - FindColorEx
  - 点阵颜色列表格式说明 - PointColorListFormat
  - 生成二维码 - CreateQRCode
  - 生成二维码 - CreateQRCodeEx
  - 移除图片差异部分 - RemoveImageDiff
  - 移除除指定颜色外的所有颜色 - RemoveOtherColors
  - 绘制圆形 - DrawCircle
  - 绘制多边形 - DrawFillPoly
  - 绘制矩形 - DrawRectangle
  - 翻转图像 - Flip
  - 腐蚀 - Erosion
  - 膨胀 - Dilation
  - 获取ROI区域 - GetROIRegion
  - 获取二值化图像 -GetThresholdImageFromMultiColorPtr
  - 获取像素颜色 - GetColorPtr
  - 获取前景点 - GetForegroundPoints
  - 获取图片大小 - GetImageSize
  - 获取拼接结果 - ImageStitchGetResult
  - 获取指定区域二值化图像 -GetThresholdImageFromMultiColor
  - 获取指定区域刷新率 - GetWindowsFps
  - 获取指定区域图象 - GetScreenDataPtr
  - 获取指定颜色数量 - GetColorNum
  - 获取指定颜色数量 - GetColorNumPtr
  - 获取连通域 - GetConnectedComponents
  - 裁剪图片 - Cropped
  - 覆盖图片 - CoverImage
  - 解析二维码 - DecodeQRCode
  - 设置图片指定坐标的颜色 - SetPixel
  - 设置图片指定坐标集的颜色 - SetPixelList
  - 设置指定颜色为新的颜色 - SetColorsToNewColor
  - 读取图片BMP字节流 - GetImageBmpData
  - 读取图片PNG字节流 - GetImagePngData
  - 读取图片大小 - GetImageSize
  - 读取图片字节流 - GetImageData
  - 调整图片大小 - ReSize
  - 调整图片大小 - ScalePixels
  - 转换颜色格式 - ConvertColor
  - 载入bmp图片 - LoadImageFromBmpData
  - 释放所有内存 - FreeImageAll
  - 释放拼接实例 - ImageStitchFree
  - 释放指定图片内存 - FreeImagePtr
  - 释放指定图片内存1 - FreeImageData
  - 释放路径下图片内存 - FreeImagePath
  - 颜色模型说明 - ColorModel
  - 骨架化 - Skeletonize
  - 高斯模糊 - GaussianBlur
- **图像数据库**
  - 初始化ola相关数据库 - InitOlaDatabase
  - 初始化图片数据库 - InitOlaImageFromDir
  - 导入ola图片数据 - ImportOlaImage
  - 导出指定目录下所有ola图片数据 - ExportOlaImageDir
  - 移除ola图片数据 - RemoveOlaImage
  - 移除指定文件夹下所有图片数据 - RemoveOlaImageFromDir
  - 读取ola图片数据 - GetOlaImage
- **图像识别**
  - 匹配动画窗口 - MatchAnimationFromPath
  - 匹配动画窗口1 - MatchAnimationFromPtr
  - 匹配图片 - MatchImageFromPathAll
  - 匹配图片1 - MatchImageFromPath
  - 匹配图片2 - MatchImageFromPtrAll
  - 匹配图片3 - MatchImageFromPtr
  - 匹配图片4 - MatchImagePtrFromPath
  - 匹配图片5 - MatchImagePtrFromPathAll
  - 匹配绑定窗口图片 - MatchWindowsFromPathAll
  - 匹配绑定窗口图片1 - MatchWindowsFromPtr
  - 匹配绑定窗口图片2 - MatchWindowsFromPtrAll
  - 匹配绑定窗口图片3 - MatchWindowsFromPath
  - 匹配绑定窗口图片4 - MatchWindowsThresholdFromPtr
  - 匹配绑定窗口图片5 - MatchWindowsThresholdFromPtrAll
  - 匹配绑定窗口图片6 - MatchWindowsThresholdFromPath
  - 匹配绑定窗口图片7 - MatchWindowsThresholdFromPathAll
  - 图片比较-均方误差 - CalculateMSE
  - 图片比较-完整比较 - IsSameImage
  - 图片比较-直方图比较 - CalculateHistograms
  - 图片比较-结构相似性指数 - CalculateSSIM
  - 是否显示匹配结果弹窗 - ShowMatchWindow
- **屏幕绘制**
  - 创建按钮 - DrawGuiButton
  - 创建窗口 - DrawGuiWindow
  - 创建面板 - DrawGuiPanel
  - 删除对象 - DrawGuiDeleteObject
  - 启用绘制 - DrawGuiSetGuiActive
  - 是否启用绘制 - DrawGuiIsGuiActive
  - 是否穿透点击 - DrawGuiIsGuiClickThrough
  - 清空所有对象 - DrawGuiClearAll
  - 点是否在对象内 - DrawGuiIsPointInObject
  - 绘制图片 - DrawGuiImage
  - 绘制图片指针 - DrawGuiImagePtr
  - 绘制圆形 - DrawGuiCircle
  - 绘制文本 - DrawGuiText
  - 绘制直线 - DrawGuiLine
  - 绘制矩形 - DrawGuiRectangle
  - 获取位置 - DrawGuiGetPosition
  - 获取对象类型 - DrawGuiGetDrawObjectType
  - 获取尺寸 - DrawGuiGetSize
  - 设置Z序 - DrawGuiSetZOrder
  - 设置位置 - DrawGuiSetPosition
  - 设置可见性 - DrawGuiSetVisible
  - 设置字体 - DrawGuiSetFont
  - 设置尺寸 - DrawGuiSetSize
  - 设置按钮回调 - DrawGuiSetButtonCallback
  - 设置文本内容 - DrawGuiSetText
  - 设置文本对齐 - DrawGuiSetTextAlign
  - 设置父子关系 - DrawGuiSetParent
  - 设置穿透点击 - DrawGuiSetGuiClickThrough
  - 设置窗口标题 - DrawGuiSetWindowTitle
  - 设置窗口样式 - DrawGuiSetWindowStyle
  - 设置窗口置顶 - DrawGuiSetWindowTopMost
  - 设置窗口透明度 - DrawGuiSetWindowTransparency
  - 设置线宽 - DrawGuiSetLineThickness
  - 设置绘制模式 - DrawGuiSetDrawMode
  - 设置透明度 - DrawGuiSetAlpha
  - 设置颜色 - DrawGuiSetColor
  - 设置鼠标回调 - DrawGuiSetMouseCallback
  - 释放绘制资源 - DrawGuiCleanup
- **快捷键**
  - 停止快捷键监听 - StopHotkeyHook
  - 卸载键盘快捷键 - UnregisterHotkey
  - 卸载鼠标拖动快捷键 - UnregisterMouseDrag
  - 卸载鼠标滚轮快捷键 - UnregisterMouseWheel
  - 卸载鼠标点击快捷键 - UnregisterMouseButton
  - 卸载鼠标移动快捷键 - UnregisterMouseMove
  - 启动快捷键监听 - StartHotkeyHook
  - 注册键盘快捷键 - RegisterHotkey
  - 注册鼠标拖动快捷键 - RegisterMouseDrag
  - 注册鼠标滚轮快捷键 - RegisterMouseWheel
  - 注册鼠标点击快捷键 - RegisterMouseButton
  - 注册鼠标移动快捷键 - RegisterMouseMove
- **数据库**
  - 关闭数据库 - CloseDatabase
  - 创建数据库 - CreateDatabase
  - 打开内存数据库 - OpenMemoryDatabase
  - 打开数据库 - OpenDatabase
  - 执行sql - ExecuteSql
  - 执行查询 - ExecuteScalar
  - 读取double数据 - GetDouble
  - 读取double数据 - GetDoubleByColumnName
  - 读取int32数据 - GetInt32
  - 读取int32数据 - GetInt32ByColumnName
  - 读取int64数据 - GetInt64
  - 读取int64数据 - GetInt64ByColumnName
  - 读取列名称 - GetColumnName
  - 读取列数量 - GetColumnCount
  - 读取列类型 - GetColumnType
  - 读取列索引 - GetColumnIndex
  - 读取字符串数据 - GetString
  - 读取字符串数据 - GetStringByColumnName
  - 读取所有表名 - GetAllTableNames
  - 读取查询结果的数量 - GetDataCount
  - 读取游标 - Read
  - 读取结果集 - ExecuteReader
  - 读取表结构信息 - GetTableInfo
  - 读取表结构详细信息 - GetTableInfoDetail
  - 读取错误信息 - GetDatabaseError
  - 销毁stmt对象 - Finalize
- **文件**
  - 写入字符串到文件 - WriteStringToFile
  - 写入字节到文件 - WriteBytesToFile
  - 创建文件 - CreateFile
  - 创建文件夹 - CreateFolder
  - 删除文件 - DeleteFile
  - 删除文件夹 - DeleteFolder
  - 判断文件夹是否存在 - IsDirectory
  - 判断文件或目录是否存在 - FileOrDirectoryExists
  - 判断文件是否存在 - IsFile
  - 复制文件 - CopyFile
  - 移动文件 - MoveFile
  - 获取文件列表 - GetFileList
  - 获取文件名 - GetFileName
  - 获取文件大小 - GetFileSize
  - 获取文件夹列表 - GetFolderList
  - 读取文件字符串 - ReadFileString
  - 读取文件字节 - ReadBytesFromFile
  - 转为相对路径 - ToRelativePath
  - 转为绝对路径 - ToAbsolutePath
  - 重命名文件 - RenameFile
- **文字识别**
  - 从字库中识别文字 - OcrFromDict
  - 从字库中识别文字 - OcrFromDictDetails
  - 从字库中识别文字 - OcrFromDictPtr
  - 从字库中识别文字 - OcrFromDictPtrDetails
  - 加载字库图片 - InitDictFromDir
  - 导出字库数据 - ExportDict
  - 快速识别数字 - FastNumberOcr
  - 快速识别数字 - FastNumberOcrFromPtr
  - 指定bmp图片识字 - OcrFromBmpData
  - 指定bmp图片详细信息 - OcrFromBmpDataDetails
  - 指定区域识字 - Ocr
  - 指定区域识字 - OcrV5
  - 指定区域详细信息- OcrDetails
  - 指定区域详细信息- OcrV5Details
  - 指定图片识字 - OcrFromPtr
  - 指定图片识字 - OcrV5FromPtr
  - 指定图片详细信息 - OcrFromPtrDetails
  - 指定图片详细信息 - OcrV5FromPtrDetails
  - 查找文字 - FindStr
  - 查找文字 - FindStrDetail
  - 查找文字 - FindStrFromPtr
  - 查找文字返回全部结果 - FindStrAll
  - 查找文字返回全部结果 - FindStrFromPtrAll
  - 添加字库数据 - ImportDictWord
  - 移除字库 - RemoveDict
  - 移除词典词条 - RemoveDictWord
  - 获取OCR配置 - GetOcrConfig
  - 设置OCR配置 - SetOcrConfig
  - 设置OCR配置键值 - SetOcrConfigByKey
  - 读取字库图片 - GetDictImage
- **汇编**
  - 执行汇编指令 - AsmCall
  - 机器码转汇编 - Disassemble
  - 汇编转机器码 - Assemble
- **注入**
  - 从URL注入DLL - InjectFromUrl
  - 从内存注入DLL - InjectFromBuffer
  - 注入DLL - Inject
- **注册表**
  - 从文件恢复注册表 - RegistryRestoreFromFile
  - 关闭注册表键 - RegistryCloseKey
  - 创建注册表键 - RegistryCreateKey
  - 删除注册表值 - RegistryDeleteValue
  - 删除注册表键 - RegistryDeleteKey
  - 判断注册表键是否存在 - RegistryKeyExists
  - 备份注册表到文件 - RegistryBackupToFile
  - 打开注册表键 - RegistryOpenKey
  - 搜索注册表键 - RegistrySearchKeys
  - 枚举值名称 - RegistryEnumValues
  - 枚举子键 - RegistryEnumSubKeys
  - 比较注册表键 - RegistryCompareKeys
  - 获取Windows版本信息 - RegistryGetWindowsVersion
  - 获取已安装软件列表 - RegistryGetInstalledSoftware
  - 获取环境变量 - RegistryGetEnvironmentVariable
  - 获取用户注册表路径 - RegistryGetUserRegistryPath
  - 获取系统注册表路径 - RegistryGetSystemRegistryPath
  - 设置32位整型值 - RegistrySetDword
  - 设置64位整型值 - RegistrySetQword
  - 设置字符串值 - RegistrySetString
  - 设置环境变量 - RegistrySetEnvironmentVariable
  - 读取32位整型值 - RegistryGetDword
  - 读取64位整型值 - RegistryGetQword
  - 读取字符串值 - RegistryGetString
- **窗口**
  - 发送剪贴板内容 - SendPaste
  - 发送字符串 - SendString
  - 发送字符串 - SendStringEx
  - 屏幕坐标转窗口坐标 - ScreenToClient
  - 强制卸载DLL - ReleaseWindowsDll
  - 拓展找窗口 - FindWindowEx
  - 枚举特殊窗口 - EnumWindowSuper
  - 枚举窗口 - EnumWindow
  - 枚举进程 - EnumProcess
  - 枚举进程窗口 - EnumWindowByProcess
  - 枚举进程窗口 - EnumWindowByProcessId
  - 查找特殊窗口 - FindWindowSuper
  - 查找窗口 - FindWindow
  - 查看绑定窗口 - GetBindWindow
  - 移动窗口 - MoveWindow
  - 窗口坐标转屏幕坐标 - ClientToScreen
  - 绑定窗口 - BindWindow
  - 绑定窗口高级 - BindWindowEx
  - 获取到客户区域 - GetClientRect
  - 获取剪贴板内容 - GetClipboard
  - 获取坐标所在窗口句柄 - GetPointWindow
  - 获取客户区大小 - GetClientSize
  - 获取焦点窗口 - GetForegroundFocus
  - 获取特殊窗口 - GetSpecialWindow
  - 获取窗口 - GetWindow
  - 获取窗口DPI感知比例 - GetWindowDpiAwarenessScale
  - 获取窗口区域 - GetWindowRect
  - 获取窗口所在路径 - GetWindowProcessPath
  - 获取窗口标题 - GetWindowTitle
  - 获取窗口状态 - GetWindowState
  - 获取窗口类名 - GetWindowClass
  - 获取线程ID - GetWindowThreadId
  - 获取绑定窗口缩放比例 - GetScaleFromWindows
  - 获取进程ID - GetWindowProcessId
  - 获取进程详细信息 - GetProcessInfo
  - 获取顶层窗口句柄 - GetForegroundWindow
  - 获取鼠标所在窗口句柄 - GetMousePointWindow
  - 解绑窗口 - UnBindWindow
  - 设置剪贴板 - SetClipboard
  - 设置客户区大小 - SetClientSize
  - 设置窗口大小 - SetWindowSize
  - 设置窗口标题 - SetWindowText
  - 设置窗口状态 - SetWindowState
  - 设置透明度 - SetWindowTransparent
  - 通过进程找窗口 - FindWindowByProcess
  - 通过进程找窗口 - FindWindowByProcessId
- **算法**
  - 创建图 - CreateGraph
  - 删除图 - DeleteGraph
  - 坐标点排序 - SortPosDistance
  - 查找最近坐标点 - FindNearestPos
  - 添加坐标节点 - AddCoordinateNode
  - 添加边 - AddEdge
  - 清空图 - ClearGraph
  - 获取图 - GetGraph
  - 获取密集矩形 - GetDenseRect
  - 获取最小生成树 - GetMinimumSpanningTree
  - 获取最短距离 - GetShortestDistance
  - 获取最短路径 - GetShortestPath
  - 获取最短路径到所有节点 - GetShortestPathToAllNodes
  - 获取有向图最小生成树 - GetMinimumArborescence
  - 获取有向路径到所有节点 - GetDirectedPathToAllNodes
  - 获取节点坐标 - GetNodeCoordinates
  - 获取节点数量 - GetNodeCount
  - 获取边数量 - GetEdgeCount
  - 获取连接状态 - GetNodeConnectionStatus
  - 获取随机整数 - GetRandomNumber
  - 获取随机浮点数 - GetRandomDouble
  - 设置节点连接 - SetNodeConnection
  - 识别图片排除指定区域 - ExcludePos
  - 通过坐标创建图 - CreateGraphFromCoordinates
- **系统**
  - 关闭内核对象 - CloseHandle
  - 创建子进程 - CreateChildProcess
  - 创建远程线程 - CreateRemoteThread
  - 启动安全守护 - StartSecurityGuard
  - 启用调试权限 - EnableDebugPrivilege
  - 延时指定毫秒 - Delay
  - 延时指定随机时间 - Delays
  - 拖动文件到窗口 - SendDropFiles
  - 控制窗口任务栏图标 - ShowTaskBarIcon
  - 检查字体平滑 - CheckFontSmooth
  - 检测UAC状态 - CheckUAC
  - 系统权限启动 - SystemStart
  - 终止进程 - TerminateProcess
  - 终止进程树 - TerminateProcessTree
  - 获取进程启动命令行 - GetCommandLine
  - 设置UAC状态 - SetUAC
  - 设置字体平滑 - SetFontSmooth
  - 运行指定程序 - RunApp
- **视频处理**
  - 从图片序列创建视频 - CreateVideoFromImages
  - 保存当前帧为图片文件 - SaveCurrentFrame
  - 保存指定帧为图片文件 - SaveFrameAtIndex
  - 关闭视频 - CloseVideo
  - 剪切视频片段 - TrimVideo
  - 将当前帧转换为Base64字符串 - FrameToBase64
  - 快速提取单帧 - ExtractSingleFrame
  - 快速提取视频第一帧 - ExtractThumbnail
  - 快速获取视频文件信息 - GetVideoInfoFromPath
  - 打开摄像头设备 - OpenCamera
  - 打开视频文件 - OpenVideo
  - 批量提取视频帧并保存为文件 - ExtractFramesToFiles
  - 按时间间隔提取帧并保存为文件 - ExtractFramesByInterval
  - 提取关键帧 - ExtractKeyFrames
  - 检查视频文件是否有效 - IsValidVideoFile
  - 检查视频是否已打开 - IsVideoOpened
  - 检测视频中的场景变化点 - DetectSceneChanges
  - 检测视频中的运动 - DetectMotion
  - 获取当前帧位置 - GetCurrentFrameIndex
  - 获取当前时间戳 - GetCurrentTimestamp
  - 获取视频基本信息 - GetVideoInfo
  - 获取视频宽度 - GetVideoWidth
  - 获取视频帧率 - GetVideoFPS
  - 获取视频总帧数 - GetVideoTotalFrames
  - 获取视频时长 - GetVideoDuration
  - 获取视频高度 - GetVideoHeight
  - 计算两帧之间的相似度 - CalculateFrameSimilarity
  - 计算视频平均亮度 - CalculateAverageBrightness
  - 读取下一帧 - ReadNextFrame
  - 读取当前帧 - ReadCurrentFrame
  - 读取指定时间戳的帧 - ReadFrameAtTime
  - 读取指定索引的帧 - ReadFrameAtIndex
  - 调整视频尺寸 - ResizeVideo
  - 跳转到指定帧 - SeekToFrame
  - 跳转到指定时间 - SeekToTime
  - 跳转到视频开头 - SeekToBeginning
  - 跳转到视频结尾 - SeekToEnd
  - 转换视频格式 - ConvertVideo
- **设置**
  - 修改用户自定义设置 - SetConfig
  - 修改用户自定义设置 - SetConfigByKey
  - 版本 - Ver
  - 获取全局路径 - GetPath
  - 获取插件路径 - GetBasePath
  - 获取机器码 - GetMachineCode
  - 设置全局路径 - SetPath
  - 设置默认编码 - SetDefaultEncode
  - 读取用户自定义设置 - GetConfig
- **键盘**
  - 按键 - KeyPress
  - 按键char - KeyPressChar
  - 按键str - KeyPressStr
  - 等待按键 - WaitKey
  - 键盘弹起 - KeyUp
  - 键盘弹起char - KeyUpChar
  - 键盘按住 - KeyDown
  - 键盘按住char - KeyDownChar
- **驱动内核**
  - 伪装进程 - FakeProcess
  - 保护窗口 - ProtectWindow
  - 保护进程 - ProtectProcess
  - 加载PDB - LoadPdb
  - 加载驱动 - LoadDriver
  - 卸载驱动 - UnloadDriver
  - 导出驱动 - ExportDriver
  - 打开线程句柄 - KeOpenThread
  - 打开进程句柄 - KeOpenProcess
  - 测试驱动 - DriverTest
  - 添加保护进程 - AddProtectPID
  - 添加白名单进程 - AddAllowPID
  - 移除保护进程 - RemoveProtectPID
  - 移除白名单进程 - RemoveAllowPID
  - 设置内存读写模式 - SetMemoryMode
  - 隐藏进程 - HideProcess
- **鼠标**
  - 中键上滚 - WheelUp
  - 中键下滚 - WheelDown
  - 中键双击 - MiddleDoubleClick
  - 中键弹起 - MiddleUp
  - 中键按下 - MiddleDown
  - 中键点击 - MiddleClick
  - 右键弹起 - RightUp
  - 右键按下 - RightDown
  - 右键点击 - RightClick
  - 左键双击 - LeftDoubleClick
  - 左键弹起 - LeftUp
  - 左键按下 - LeftDown
  - 左键点击 - LeftClick
  - 生成鼠标移动轨迹 - GenerateMouseTrajectory
  - 直接移动 - MoveToWithoutSimulator
  - 相对移动 - MoveR
  - 移动 - MoveTo
  - 范围鼠标移动 - MoveToEx
  - 获取鼠标位置 - GetCursorPos
  - 获取鼠标图标 - GetCursorImage
  - 获取鼠标特征码 - GetCursorShape
  - 设置系统鼠标精度 - EnableMouseAccuracy
  - 鼠标右键双击 - RightDoubleClick

---

## Config相关

# 设置数据库配置 - SetDbConfig

## 函数简介

保存用户自定义数据到数据库

## 函数原型

```
[](#cb1-1)int SetDbConfig(long ola, const long db, string key, string value);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db`: 数据库对象指针，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口返回。

- `key` (字符串): 配置项名，如”width”、“height”。

- `value`(字符串): 配置项值 如:100

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 设置数据库配置
[](#cb2-22)            string key = "cache_size";
[](#cb2-23)            string value = "1000";
[](#cb2-24)            int result = OLAServer.SetDbConfig(db, key, value);
[](#cb2-25)            if (result == 1)
[](#cb2-26)            {
[](#cb2-27)                Console.WriteLine("数据库配置设置成功。");
[](#cb2-28)            }
[](#cb2-29)            else
[](#cb2-30)            {
[](#cb2-31)                Console.WriteLine("数据库配置设置失败。");
[](#cb2-32)            }
[](#cb2-33)        }
[](#cb2-34)    }
[](#cb2-35)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 设置数据库配置
[](#cb3-14)key = "cache_size"
[](#cb3-15)value = "1000"
[](#cb3-16)result = OLAServer.SetDbConfig(db, key, value)
[](#cb3-17)if result == 1:
[](#cb3-18)    print("数据库配置设置成功。")
[](#cb3-19)else:
[](#cb3-20)    print("数据库配置设置失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 设置数据库配置
[](#cb4-33)key = "cache_size"
[](#cb4-34)value = "1000"
[](#cb4-35)olaplug_dll.SetDbConfig.argtypes = [c_void_p, c_void_p, c_char_p, c_char_p]
[](#cb4-36)olaplug_dll.SetDbConfig.restype = c_int32
[](#cb4-37)result = olaplug_dll.SetDbConfig(ola_obj, db, key.encode('utf-8'), value.encode('utf-8'))
[](#cb4-38)if result == 1:
[](#cb4-39)    print("数据库配置设置成功。")
[](#cb4-40)else:
[](#cb4-41)    print("数据库配置设置失败。")
```

## 注意事项

- 该函数用于设置用户自定义数据,如账号密码软件默认配置等信息。

---

# 设置数据库配置 -
SetDbConfigEx

## 函数简介

保存用户自定义数据到数据库 - 默认使用[SetConfig](/设置/修改用户自定义设置%20-%20SetConfig.html)
接口配置的数据库 - 如果未配置则返回失败

## 函数原型

```
[](#cb1-1)int SetDbConfigEx(long ola, string key, string value);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key` (字符串): 配置项名，如”width”、“height”。

- `value`(字符串): 配置项值 如:100

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

暂无

## 注意事项

- 该函数用于设置用户自定义数据,如账号密码软件默认配置等信息。

---

# 移除数据库配置项 -
RemoveDbConfig

## 函数简介

移除自定义的配置项

## 函数原型

```
[](#cb1-1)int RemoveDbConfig(long ola, const long db, string key);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db`: 数据库对象指针，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口返回。

- `key` (字符串): 配置项名，如”width”、“height”。

## 返回值

- 返回值：操作结果，返回 `1` 表示成功，返回 `0`
表示失败。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 设置数据库配置
[](#cb2-22)            string key = "cache_size";
[](#cb2-23)            string value = "1000";
[](#cb2-24)            int result = OLAServer.SetDbConfig(db, key, value);
[](#cb2-25)            if (result == 1)
[](#cb2-26)            {
[](#cb2-27)                Console.WriteLine("数据库配置设置成功。");
[](#cb2-28)            }
[](#cb2-29)            else
[](#cb2-30)            {
[](#cb2-31)                Console.WriteLine("数据库配置设置失败。");
[](#cb2-32)            }
[](#cb2-33)            var RemoveDbConfigResult = OLAServer.RemoveDbConfig(db, key);
[](#cb2-34)            Console.WriteLine($"RemoveDbConfig 返回:{RemoveDbConfigResult}");
[](#cb2-35)        }
[](#cb2-36)    }
[](#cb2-37)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 设置数据库配置
[](#cb3-14)key = "cache_size"
[](#cb3-15)value = "1000"
[](#cb3-16)result = OLAServer.SetDbConfig(db, key, value)
[](#cb3-17)if result == 1:
[](#cb3-18)    print("数据库配置设置成功。")
[](#cb3-19)else:
[](#cb3-20)    print("数据库配置设置失败。")
[](#cb3-21)RemoveDbConfigResult = OLAServer.RemoveDbConfig(db, key)
[](#cb3-22)print(f"RemoveDbConfig 返回:{RemoveDbConfigResult}")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 设置数据库配置
[](#cb4-33)key = "cache_size"
[](#cb4-34)value = "1000"
[](#cb4-35)olaplug_dll.SetDbConfig.argtypes = [c_void_p, c_void_p, c_char_p, c_char_p]
[](#cb4-36)olaplug_dll.SetDbConfig.restype = c_int32
[](#cb4-37)result = olaplug_dll.SetDbConfig(ola_obj, db, key.encode('utf-8'), value.encode('utf-8'))
[](#cb4-38)if result == 1:
[](#cb4-39)    print("数据库配置设置成功。")
[](#cb4-40)else:
[](#cb4-41)    print("数据库配置设置失败。")
[](#cb4-42)olaplug_dll.RemoveDbConfig.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-43)olaplug_dll.RemoveDbConfig.restype = c_char_p
[](#cb4-44)RemoveDbConfigResult = olaplug_dll.RemoveDbConfig(ola_obj, db, key.encode('utf-8'))
[](#cb4-45)print(f"RemoveDbConfig 返回:{RemoveDbConfigResult}")
```

---

# 移除数据库配置项 -
RemoveDbConfigEx

## 函数简介

移除自定义的配置项 - 默认使用[SetConfig](/设置/修改用户自定义设置%20-%20SetConfig.html)
接口配置的数据库 - 如果未配置则返回失败

## 函数原型

```
[](#cb1-1)int RemoveDbConfigEx(long ola, string key);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key` (字符串): 配置项名，如”width”、“height”。

## 返回值

- 返回值：操作结果，返回 `1` 表示成功，返回 `0`
表示失败。

## 示例

暂无

---

# 读取数据库配置项 -
GetDbConfig

## 函数简介

读取自定义的配置项

## 函数原型

```
[](#cb1-1)long GetDbConfig(long ola, const long db, string key);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db`: 数据库对象指针，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口返回。

- `key` (字符串): 配置项名，如”width”、“height”。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 设置数据库配置
[](#cb2-22)            string key = "cache_size";
[](#cb2-23)            string value = "1000";
[](#cb2-24)            int result = OLAServer.SetDbConfig(db, key, value);
[](#cb2-25)            if (result == 1)
[](#cb2-26)            {
[](#cb2-27)                Console.WriteLine("数据库配置设置成功。");
[](#cb2-28)            }
[](#cb2-29)            else
[](#cb2-30)            {
[](#cb2-31)                Console.WriteLine("数据库配置设置失败。");
[](#cb2-32)            }
[](#cb2-33)            var GetDbConfigResult = OLAServer.GetDbConfig(db, key);
[](#cb2-34)            Console.WriteLine($"GetDbConfig 返回:{GetDbConfigResult}");
[](#cb2-35)        }
[](#cb2-36)    }
[](#cb2-37)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 设置数据库配置
[](#cb3-14)key = "cache_size"
[](#cb3-15)value = "1000"
[](#cb3-16)result = OLAServer.SetDbConfig(db, key, value)
[](#cb3-17)if result == 1:
[](#cb3-18)    print("数据库配置设置成功。")
[](#cb3-19)else:
[](#cb3-20)    print("数据库配置设置失败。")
[](#cb3-21)GetDbConfigResult = OLAServer.GetDbConfig(db, key)
[](#cb3-22)print(f"GetDbConfig 返回:{GetDbConfigResult}")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 设置数据库配置
[](#cb4-33)key = "cache_size"
[](#cb4-34)value = "1000"
[](#cb4-35)olaplug_dll.SetDbConfig.argtypes = [c_void_p, c_void_p, c_char_p, c_char_p]
[](#cb4-36)olaplug_dll.SetDbConfig.restype = c_int32
[](#cb4-37)result = olaplug_dll.SetDbConfig(ola_obj, db, key.encode('utf-8'), value.encode('utf-8'))
[](#cb4-38)if result == 1:
[](#cb4-39)    print("数据库配置设置成功。")
[](#cb4-40)else:
[](#cb4-41)    print("数据库配置设置失败。")
[](#cb4-42)olaplug_dll.GetDbConfig.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-43)olaplug_dll.GetDbConfig.restype = c_char_p
[](#cb4-44)GetDbConfigResult = olaplug_dll.GetDbConfig(ola_obj, db, key.encode('utf-8'))
[](#cb4-45)print(f"GetDbConfig 返回:{GetDbConfigResult}")
```

## 返回值

字符串:

对应配置项的。

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

## 注意事项

- 该函数用于读取用户自定义数据,如账号密码软件默认配置等信息。

---

# 读取数据库配置项 -
GetDbConfigEx

## 函数简介

读取自定义的配置项 - 默认使用[SetConfig](/设置/修改用户自定义设置%20-%20SetConfig.html)
接口配置的数据库 - 如果未配置则返回失败

## 函数原型

```
[](#cb1-1)long GetDbConfigEx(long ola, string key);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key` (字符串): 配置项名，如”width”、“height”。

## 示例

## 返回值

字符串:

对应配置项的。

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

## 注意事项

- 该函数用于读取用户自定义数据,如账号密码软件默认配置等信息。

---

## JSON

# 创建空的JSON对象 -
JsonCreateObject

## 函数简介

创建一个空的JSON对象，用于构建JSON数据结构。

## 接口名称

```
JsonCreateObject
```

## DLL调用

```
long JsonCreateObject()
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
无参数 |
|
|
|

### 示例

```
[](#cb3-1)// 创建空的JSON对象
[](#cb3-2)long jsonObj = JsonCreateObject();
[](#cb3-3)if (jsonObj != 0) {
[](#cb3-4)    // 使用JSON对象
[](#cb3-5)    // ...
[](#cb3-6)    JsonFree(jsonObj); // 释放内存
[](#cb3-7)}
```

## 返回值

返回新创建的JSON对象句柄，失败时返回0

## 错误码说明

|
返回值 |
说明 |
|

|
非0值 |
操作成功，返回JSON对象句柄 |
|

|
0 |
创建失败，可能是内存不足 |
|

## 注意事项

- 返回的JSON对象句柄需要调用JsonFree释放内存

- 创建失败时返回0，需要检查返回值

---

# 创建空的JSON数组 -
JsonCreateArray

## 函数简介

创建一个空的JSON数组，用于构建JSON数组数据结构。

## 接口名称

```
JsonCreateArray
```

## DLL调用

```
long JsonCreateArray()
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
无参数 |
|
|
|

### 示例

```
[](#cb3-1)// 创建空的JSON数组
[](#cb3-2)long jsonArr = JsonCreateArray();
[](#cb3-3)if (jsonArr != 0) {
[](#cb3-4)    // 使用JSON数组
[](#cb3-5)    // ...
[](#cb3-6)    JsonFree(jsonArr); // 释放内存
[](#cb3-7)}
```

## 返回值

返回新创建的JSON数组句柄，失败时返回0

## 错误码说明

|
返回值 |
说明 |
|

|
非0值 |
操作成功，返回JSON数组句柄 |
|

|
0 |
创建失败，可能是内存不足 |
|

## 注意事项

- 返回的JSON数组句柄需要调用JsonFree释放内存

- 创建失败时返回0，需要检查返回值

---

# 删除JSON对象中的键 -
JsonDeleteKey

## 函数简介

删除JSON对象中指定的键及其对应的值。

## 接口名称

```
JsonDeleteKey
```

## DLL调用

```
int JsonDeleteKey(long obj, string key)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
obj |
长整数型 |
JSON对象句柄 |
|

|
key |
字符串 |
要删除的键名 |
|

### 示例

```
[](#cb3-1)// 删除JSON对象中的键
[](#cb3-2)long jsonObj = JsonParse("{\"name\":\"test\",\"age\":25,\"city\":\"beijing\"}", 0);
[](#cb3-3)
[](#cb3-4)// 删除指定键
[](#cb3-5)int result = JsonDeleteKey(jsonObj, "age");
[](#cb3-6)if (result == 0) {
[](#cb3-7)    printf("删除键成功\n");
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)// 查看删除后的结果
[](#cb3-11)int err = 0;
[](#cb3-12)const char* jsonStr = JsonStringify(jsonObj, 2, &err);
[](#cb3-13)if (jsonStr != 0 && err == 0) {
[](#cb3-14)    printf("删除后的JSON: %s\n", jsonStr);
[](#cb3-15)    FreeStringPtr(jsonStr);
[](#cb3-16)}
[](#cb3-17)
[](#cb3-18)JsonFree(jsonObj);
```

## 返回值

返回操作结果错误码，0表示成功

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 如果键不存在，操作仍然成功（无操作）

- 删除后，对应的值也会被释放

- 删除操作不可逆

---

# 向JSON数组添加元素 -
JsonArrayAppend

## 函数简介

向JSON数组末尾添加元素，支持添加任意类型的JSON值。

## 接口名称

```
JsonArrayAppend
```

## DLL调用

```
int JsonArrayAppend(long arr, long value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
arr |
长整数型 |
JSON数组句柄 |
|

|
value |
长整数型 |
要添加的元素句柄 |
|

### 示例

```
[](#cb3-1)// 向JSON数组添加元素
[](#cb3-2)long jsonArr = JsonCreateArray();
[](#cb3-3)
[](#cb3-4)// 添加字符串元素
[](#cb3-5)long strValue = JsonCreateObject(); // 创建字符串值
[](#cb3-6)JsonSetString(strValue, "", "hello");
[](#cb3-7)JsonArrayAppend(jsonArr, strValue);
[](#cb3-8)
[](#cb3-9)// 添加数字元素
[](#cb3-10)long numValue = JsonCreateObject(); // 创建数字值
[](#cb3-11)JsonSetNumber(numValue, "", 123);
[](#cb3-12)JsonArrayAppend(jsonArr, numValue);
[](#cb3-13)
[](#cb3-14)// 添加对象元素
[](#cb3-15)long objValue = JsonCreateObject();
[](#cb3-16)JsonSetString(objValue, "name", "test");
[](#cb3-17)JsonSetNumber(objValue, "age", 25);
[](#cb3-18)JsonArrayAppend(jsonArr, objValue);
[](#cb3-19)
[](#cb3-20)// 注意：所有value句柄的所有权都转移给arr，不需要单独释放
[](#cb3-21)JsonFree(jsonArr); // 释放数组（会同时释放所有元素）
```

## 返回值

返回操作结果错误码，0表示成功

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 添加成功后，value句柄的所有权转移给arr，不需要单独释放

- 元素会被添加到数组末尾

- 支持添加对象、数组、字符串、数字等任意JSON类型

---

# 将JSON对象序列化为字符串 -
JsonStringify

## 函数简介

将JSON对象序列化为字符串，支持格式化输出。

## 接口名称

```
JsonStringify
```

## DLL调用

```
long JsonStringify(long obj, int indent, int* err)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
obj |
长整数型 |
JSON对象句柄 |
|

|
indent |
整数型 |
缩进空格数，0表示不格式化 |
|

|
err |
整数型指针 |
错误码输出参数，可为0 |
|

### 示例

```
[](#cb3-1)// 将JSON对象序列化为字符串
[](#cb3-2)long jsonObj = JsonCreateObject();
[](#cb3-3)JsonSetString(jsonObj, "name", "test");
[](#cb3-4)JsonSetNumber(jsonObj, "age", 25);
[](#cb3-5)
[](#cb3-6)int err = 0;
[](#cb3-7)const char* jsonStr = JsonStringify(jsonObj, 2, &err);
[](#cb3-8)if (jsonStr != 0 && err == 0) {
[](#cb3-9)    printf("JSON字符串: %s\n", jsonStr);
[](#cb3-10)    FreeStringPtr(jsonStr); // 释放字符串内存
[](#cb3-11)}
[](#cb3-12)
[](#cb3-13)JsonFree(jsonObj); // 释放JSON对象
```

## 返回值

返回JSON字符串，需调用FreeStringPtr释放，失败时返回0

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 返回的字符串需要调用FreeStringPtr释放内存

- 序列化失败时返回0，错误码通过err参数返回

- indent参数控制格式化，0表示紧凑格式，大于0表示缩进空格数

---

# 清空JSON对象或数组 -
JsonClear

## 函数简介

清空JSON对象中的所有属性或JSON数组中的所有元素。

## 接口名称

```
JsonClear
```

## DLL调用

```
int JsonClear(long obj)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
obj |
长整数型 |
JSON对象或数组句柄 |
|

### 示例

```
[](#cb3-1)// 清空JSON对象
[](#cb3-2)long jsonObj = JsonParse("{\"name\":\"test\",\"age\":25,\"city\":\"beijing\"}", 0);
[](#cb3-3)
[](#cb3-4)// 清空对象
[](#cb3-5)int result = JsonClear(jsonObj);
[](#cb3-6)if (result == 0) {
[](#cb3-7)    printf("清空对象成功\n");
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)// 查看清空后的结果
[](#cb3-11)int err = 0;
[](#cb3-12)const char* jsonStr = JsonStringify(jsonObj, 2, &err);
[](#cb3-13)if (jsonStr != 0 && err == 0) {
[](#cb3-14)    printf("清空后的JSON: %s\n", jsonStr);
[](#cb3-15)    FreeStringPtr(jsonStr);
[](#cb3-16)}
[](#cb3-17)
[](#cb3-18)// 清空JSON数组
[](#cb3-19)long jsonArr = JsonParse("[1,2,3,4,5]", 0);
[](#cb3-20)JsonClear(jsonArr);
[](#cb3-21)
[](#cb3-22)JsonFree(jsonObj);
[](#cb3-23)JsonFree(jsonArr);
```

## 返回值

返回操作结果错误码，0表示成功

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 清空后，所有子元素都会被释放

- 清空操作不可逆

- 适用于对象和数组类型

---

# 获取JSON对象中的值 -
JsonGetValue

## 函数简介

获取JSON对象中指定键对应的值，返回JSON值句柄。

## 接口名称

```
JsonGetValue
```

## DLL调用

```
long JsonGetValue(long obj, string key, int* err)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
obj |
长整数型 |
JSON对象句柄 |
|

|
key |
字符串 |
键名 |
|

|
err |
整数型指针 |
错误码输出参数，可为0 |
|

### 示例

```
[](#cb3-1)// 获取JSON对象中的值
[](#cb3-2)long jsonObj = JsonParse("{\"name\":\"test\",\"age\":25}", 0);
[](#cb3-3)int err = 0;
[](#cb3-4)
[](#cb3-5)// 获取字符串值
[](#cb3-6)long nameValue = JsonGetValue(jsonObj, "name", &err);
[](#cb3-7)if (nameValue != 0 && err == 0) {
[](#cb3-8)    // 使用获取到的值
[](#cb3-9)    // ...
[](#cb3-10)    JsonFree(nameValue); // 释放值句柄
[](#cb3-11)}
[](#cb3-12)
[](#cb3-13)JsonFree(jsonObj); // 释放JSON对象
```

## 返回值

返回对应的JSON值句柄，失败时返回0

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 返回的值句柄需要调用JsonFree释放内存

- 如果键不存在或获取失败，返回0

- 错误码通过err参数返回

---

# 获取JSON对象中的字符串值 -
JsonGetString

## 函数简介

获取JSON对象中指定键对应的字符串值。

## 接口名称

```
JsonGetString
```

## DLL调用

```
long JsonGetString(long obj, string key, int* err)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
obj |
长整数型 |
JSON对象句柄 |
|

|
key |
字符串 |
键名 |
|

|
err |
整数型指针 |
错误码输出参数，可为0 |
|

### 示例

```
[](#cb3-1)// 获取JSON对象中的字符串值
[](#cb3-2)long jsonObj = JsonParse("{\"name\":\"test\",\"message\":\"hello world\"}", 0);
[](#cb3-3)int err = 0;
[](#cb3-4)
[](#cb3-5)const char* name = JsonGetString(jsonObj, "name", &err);
[](#cb3-6)if (name != 0 && err == 0) {
[](#cb3-7)    printf("name: %s\n", name);
[](#cb3-8)    FreeStringPtr(name); // 释放字符串内存
[](#cb3-9)}
[](#cb3-10)
[](#cb3-11)JsonFree(jsonObj); // 释放JSON对象
```

## 返回值

返回字符串值，需调用FreeStringPtr释放，失败时返回0

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 返回的字符串需要调用FreeStringPtr释放内存

- 如果键不存在或值不是字符串类型，返回0

- 错误码通过err参数返回

---

# 获取JSON对象中的布尔值 -
JsonGetBool

## 函数简介

获取JSON对象中指定键对应的布尔值。

## 接口名称

```
JsonGetBool
```

## DLL调用

```
int JsonGetBool(long obj, string key, int* err)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
obj |
长整数型 |
JSON对象句柄 |
|

|
key |
字符串 |
键名 |
|

|
err |
整数型指针 |
错误码输出参数，可为0 |
|

### 示例

```
[](#cb3-1)// 获取JSON对象中的字符串值
[](#cb3-2)long jsonObj = JsonParse("{\"state\":true,\"message\":\"hello world\"}", 0);
[](#cb3-3)int err = 0;
[](#cb3-4)
[](#cb3-5)int state = JsonGetBool(jsonObj, "state", &err);
[](#cb3-6)
[](#cb3-7)
[](#cb3-8)JsonFree(jsonObj); // 释放JSON对象
```

## 返回值

返回布尔值（0表示false，非0表示true）

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 错误码通过err参数返回

---

# 获取JSON对象中的数值 -
JsonGetNumber

## 函数简介

获取JSON对象中指定键对应的数值。

## 接口名称

```
JsonGetNumber
```

## DLL调用

```
double JsonGetNumber(long obj, string key, int* err)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
obj |
长整数型 |
JSON对象句柄 |
|

|
key |
字符串 |
键名 |
|

|
err |
整数型指针 |
错误码输出参数，可为0 |
|

### 示例

```
[](#cb3-1)// 获取JSON对象中的数值
[](#cb3-2)long jsonObj = JsonParse("{\"age\":25,\"score\":98.5,\"count\":100}", 0);
[](#cb3-3)int err = 0;
[](#cb3-4)
[](#cb3-5)double age = JsonGetNumber(jsonObj, "age", &err);
[](#cb3-6)if (err == 0) {
[](#cb3-7)    printf("age: %.0f\n", age);
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)double score = JsonGetNumber(jsonObj, "score", &err);
[](#cb3-11)if (err == 0) {
[](#cb3-12)    printf("score: %.1f\n", score);
[](#cb3-13)}
[](#cb3-14)
[](#cb3-15)JsonFree(jsonObj); // 释放JSON对象
```

## 返回值

返回数值，失败时返回0.0

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 如果键不存在或值不是数字类型，返回0.0

- 错误码通过err参数返回

- 支持整数和浮点数类型

---

# 获取JSON对象或数组的大小
- JsonGetSize

## 函数简介

获取JSON对象中属性的数量或JSON数组中元素的数量。

## 接口名称

```
JsonGetSize
```

## DLL调用

```
int JsonGetSize(long obj, int* err)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
obj |
长整数型 |
JSON对象或数组句柄 |
|

|
err |
整数型指针 |
错误码输出参数，可为0 |
|

### 示例

```
[](#cb3-1)// 获取JSON对象的大小
[](#cb3-2)long jsonObj = JsonParse("{\"name\":\"test\",\"age\":25,\"city\":\"beijing\"}", 0);
[](#cb3-3)int err = 0;
[](#cb3-4)int objSize = JsonGetSize(jsonObj, &err);
[](#cb3-5)if (err == 0) {
[](#cb3-6)    printf("对象属性数量: %d\n", objSize);
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 获取JSON数组的大小
[](#cb3-10)long jsonArr = JsonParse("[1,2,3,4,5]", 0);
[](#cb3-11)int arrSize = JsonGetSize(jsonArr, &err);
[](#cb3-12)if (err == 0) {
[](#cb3-13)    printf("数组元素数量: %d\n", arrSize);
[](#cb3-14)}
[](#cb3-15)
[](#cb3-16)JsonFree(jsonObj);
[](#cb3-17)JsonFree(jsonArr);
```

## 返回值

返回对象属性数量或数组长度，失败时返回0

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 对于JSON对象，返回属性的数量

- 对于JSON数组，返回元素的数量

- 如果参数不是对象或数组类型，返回0

- 错误码通过err参数返回

---

# 获取JSON数组中的元素 -
JsonGetArrayItem

## 函数简介

获取JSON数组中指定索引位置的元素，返回JSON值句柄。

## 接口名称

```
JsonGetArrayItem
```

## DLL调用

```
long JsonGetArrayItem(long arr, int index, int* err)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
arr |
长整数型 |
JSON数组句柄 |
|

|
index |
整数型 |
元素索引（从0开始） |
|

|
err |
整数型指针 |
错误码输出参数，可为0 |
|

### 示例

```
[](#cb3-1)// 获取JSON数组中的元素
[](#cb3-2)long jsonArr = JsonParse("[1,2,3,\"test\"]", 0);
[](#cb3-3)int err = 0;
[](#cb3-4)
[](#cb3-5)// 获取第一个元素
[](#cb3-6)long firstItem = JsonGetArrayItem(jsonArr, 0, &err);
[](#cb3-7)if (firstItem != 0 && err == 0) {
[](#cb3-8)    // 使用获取到的元素
[](#cb3-9)    // ...
[](#cb3-10)    JsonFree(firstItem); // 释放元素句柄
[](#cb3-11)}
[](#cb3-12)
[](#cb3-13)JsonFree(jsonArr); // 释放JSON数组
```

## 返回值

返回数组元素句柄，失败时返回0

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 返回的元素句柄需要调用JsonFree释放内存

- 如果索引超出范围或获取失败，返回0

- 错误码通过err参数返回

- 索引从0开始计数

---

# 获取匹配图像JSON数量 -
GetMatchImageAllCount

## 函数简介

获取匹配图像JSON数组中的匹配结果数量。

## 接口名称

```
GetMatchImageAllCount
```

## DLL调用

```
int GetMatchImageAllCount(string str)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
str |
字符串 |
匹配图像JSON字符串 |
|

### 示例

```
[](#cb3-1)// 获取匹配图像JSON数组的数量
[](#cb3-2)const char* jsonStr = "[{\"MatchVal\":0.85,\"MatchState\":1,\"Index\":0,\"Angle\":45.0,,\"X\":50,,\"Y\":120,\"Width\":100,\"Height\":100},{\"MatchVal\":0.92,\"MatchState\":1,\"Index\":0,\"Angle\":0.0,,\"X\":50,,\"Y\":120,\"Width\":100,\"Height\":100}]";
[](#cb3-3)
[](#cb3-4)int count = GetMatchImageAllCount(jsonStr);
[](#cb3-5)printf("匹配结果数量: %d\n", count);
[](#cb3-6)
[](#cb3-7)// 根据数量遍历所有匹配结果
[](#cb3-8)for (int i = 0; i < count; i++) {
[](#cb3-9)    // 使用 ParseMatchImageAllJson 解析每个结果
[](#cb3-10)    // ...
[](#cb3-11)}
```

## 返回值

返回匹配图像JSON数量，解析失败时返回0

## 注意事项

- 用于获取匹配图像返回的JSON数组长度

- JSON格式应为数组格式，包含一个或多个匹配结果对象

- 返回的数量可以用于后续遍历所有匹配结果

---

# 解析JSON字符串 - JsonParse

## 函数简介

解析JSON字符串，将其转换为JSON对象句柄，便于后续操作。

## 接口名称

```
JsonParse
```

## DLL调用

```
long JsonParse(string str, int* err)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
str |
字符串 |
要解析的JSON字符串 |
|

|
err |
整数型指针 |
错误码输出参数，可为0 |
|

### 示例

```
[](#cb3-1)// 解析JSON字符串
[](#cb3-2)const char* jsonStr = "{\"name\":\"test\",\"age\":25}";
[](#cb3-3)int err = 0;
[](#cb3-4)long jsonObj = JsonParse(jsonStr, &err);
[](#cb3-5)if (jsonObj != 0 && err == 0) {
[](#cb3-6)    // 使用解析后的JSON对象
[](#cb3-7)    // ...
[](#cb3-8)    JsonFree(jsonObj); // 释放内存
[](#cb3-9)} else {
[](#cb3-10)    // 处理解析错误
[](#cb3-11)    printf("JSON解析失败，错误码: %d\n", err);
[](#cb3-12)}
```

## 返回值

返回解析后的JSON对象句柄，失败时返回0

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 返回的JSON对象句柄需要调用JsonFree释放内存

- 解析失败时返回0，错误码通过err参数返回

- 支持标准JSON格式，包括对象、数组、字符串、数字、布尔值和null

---

# 解析匹配图像JSON -
ParseMatchImageJson

## 函数简介

解析匹配图像JSON字符串，提取单个匹配结果的详细信息。

## 接口名称

```
ParseMatchImageJson
```

## DLL调用

```
int ParseMatchImageJson(string str, int* matchState, int* x, int* y, double* matchVal, double* angle, int* index)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
str |
字符串 |
匹配图像JSON字符串 |
|

|
matchState |
整数型指针 |
输出：匹配状态 |
|

|
x |
整数型指针 |
输出：匹配点X坐标 |
|

|
y |
整数型指针 |
输出：匹配点Y坐标 |
|

|
width |
整数型指针 |
输出：匹配图片高度 |
|

|
height |
整数型指针 |
输出：匹配图片高度 |
|

|
matchVal |
双精度指针 |
输出：匹配值 |
|

|
angle |
双精度指针 |
输出：匹配角度 |
|

|
index |
整数型指针 |
输出：匹配索引 |
|

### 示例

```
[](#cb3-1)// 解析单个匹配图像JSON
[](#cb3-2)const char* jsonStr = "{\"MatchVal\":0.85,\"MatchState\":1,\"Index\":0,\"Angle\":45.0,\"X\":50,,\"Y\":120,\"Width\":100,\"Height\":100}";
[](#cb3-3)int matchState = 0, x = 0, y = 0, index = 0,width=0,height=0;
[](#cb3-4)double matchVal = 0.0, angle = 0.0;
[](#cb3-5)
[](#cb3-6)int result = ParseMatchImageJson(jsonStr, &matchState, &x, &y,&width,&height &matchVal, &angle, &index);
[](#cb3-7)if (result == 1) {
[](#cb3-8)    printf("匹配状态: %d\n", matchState);
[](#cb3-9)    printf("匹配坐标: (%d, %d)\n", x, y);
[](#cb3-10)    printf("匹配大小: (%d, %d)\n", width, height);
[](#cb3-11)    printf("匹配值: %.2f\n", matchVal);
[](#cb3-12)    printf("匹配角度: %.2f\n", angle);
[](#cb3-13)    printf("匹配索引: %d\n", index);
[](#cb3-14)} else {
[](#cb3-15)    printf("JSON解析失败\n");
[](#cb3-16)}
```

## 返回值

返回操作结果错误码： - `1` - 解析成功 - `0` -
解析失败

## 注意事项

- 用于解析单个匹配结果的JSON字符串

- JSON格式应符合匹配图像接口返回的标准格式

- 所有输出参数必须提供有效指针

---

# 解析匹配图像多结果JSON
- ParseMatchImageAllJson

## 函数简介

解析匹配图像JSON数组，获取指定索引的匹配结果详细信息。

## 接口名称

```
ParseMatchImageAllJson
```

## DLL调用

```
int ParseMatchImageAllJson(string str, int parseIndex, int* matchState, int* x, int* y, double* matchVal, double* angle, int* index)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
str |
字符串 |
匹配图像JSON字符串 |
|

|
parseIndex |
整数型 |
解析索引（从0开始） |
|

|
matchState |
整数型指针 |
输出：匹配状态 |
|

|
x |
整数型指针 |
输出：匹配点X坐标 |
|

|
y |
整数型指针 |
输出：匹配点Y坐标 |
|

|
width |
整数型指针 |
输出：匹配图片高度 |
|

|
height |
整数型指针 |
输出：匹配图片高度 |
|

|
matchVal |
双精度指针 |
输出：匹配值 |
|

|
angle |
双精度指针 |
输出：匹配角度 |
|

|
index |
整数型指针 |
输出：匹配索引 |
|

### 示例

```
[](#cb3-1)// 解析匹配图像JSON数组中的指定索引
[](#cb3-2)const char* jsonStr = "[{\"MatchVal\":0.85,\"MatchState\":1,\"Index\":0,\"Angle\":45.0,,\"X\":50,,\"Y\":120,\"Width\":100,\"Height\":100},{\"MatchVal\":0.92,\"MatchState\":1,\"Index\":0,\"Angle\":0.0,,\"X\":50,,\"Y\":120,\"Width\":100,\"Height\":100}]";
[](#cb3-3)
[](#cb3-4)// 获取匹配结果数量
[](#cb3-5)int totalCount = GetMatchImageAllCount(jsonStr);
[](#cb3-6)
[](#cb3-7)// 遍历所有匹配结果
[](#cb3-8)for (int i = 0; i < totalCount; i++) {
[](#cb3-9)    int matchState = 0, x = 0, y = 0, index = 0,width=0,height=0;
[](#cb3-10)    double matchVal = 0.0, angle = 0.0;
[](#cb3-11)
[](#cb3-12)    int result = ParseMatchImageAllJson(jsonStr, i, &matchState, &x, &y,&width,&height, &matchVal, &angle, &index);
[](#cb3-13)    if (result == 1) {
[](#cb3-14)        printf("第%d个匹配结果:\n", i);
[](#cb3-15)        printf("  匹配状态: %d\n", matchState);
[](#cb3-16)        printf("  匹配坐标: (%d, %d)\n", x, y);
[](#cb3-17)        printf("  匹配值: %.2f\n", matchVal);
[](#cb3-18)        printf("  匹配角度: %.2f\n", angle);
[](#cb3-19)        printf("  匹配索引: %d\n", index);
[](#cb3-20)    }
[](#cb3-21)}
```

## 返回值

返回操作结果错误码： - `1` - 解析成功 - `0` -
解析失败

## 注意事项

- 用于解析JSON数组中的指定索引匹配结果

- parseIndex 参数从0开始计数

- 结合 GetMatchImageAllCount 使用可以遍历所有匹配结果

- 所有输出参数必须提供有效指针

---

# 设置JSON对象中的值 -
JsonSetValue

## 函数简介

设置JSON对象中指定键的值，支持设置任意类型的JSON值。

## 接口名称

```
JsonSetValue
```

## DLL调用

```
int JsonSetValue(long obj, string key, long value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
obj |
长整数型 |
JSON对象句柄 |
|

|
key |
字符串 |
键名 |
|

|
value |
长整数型 |
要设置的值句柄 |
|

### 示例

```
[](#cb3-1)// 设置JSON对象中的值
[](#cb3-2)long jsonObj = JsonCreateObject();
[](#cb3-3)
[](#cb3-4)// 创建子对象
[](#cb3-5)long subObj = JsonCreateObject();
[](#cb3-6)JsonSetString(subObj, "name", "test");
[](#cb3-7)JsonSetNumber(subObj, "age", 25);
[](#cb3-8)
[](#cb3-9)// 将子对象设置到主对象中
[](#cb3-10)int result = JsonSetValue(jsonObj, "user", subObj);
[](#cb3-11)if (result == 0) {
[](#cb3-12)    printf("设置成功\n");
[](#cb3-13)}
[](#cb3-14)
[](#cb3-15)// 注意：subObj的所有权转移给jsonObj，不需要单独释放
[](#cb3-16)JsonFree(jsonObj); // 释放主对象（会同时释放子对象）
```

## 返回值

返回操作结果错误码，0表示成功

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 设置成功后，value句柄的所有权转移给obj，不需要单独释放

- 如果key已存在，会覆盖原有值

- 支持设置对象、数组、字符串、数字等任意JSON类型

---

# 设置JSON对象中的字符串值 -
JsonSetString

## 函数简介

设置JSON对象中指定键的字符串值。

## 接口名称

```
JsonSetString
```

## DLL调用

```
int JsonSetString(long obj, string key, string value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
obj |
长整数型 |
JSON对象句柄 |
|

|
key |
字符串 |
键名 |
|

|
value |
字符串 |
字符串值 |
|

### 示例

```
[](#cb3-1)// 设置JSON对象中的字符串值
[](#cb3-2)long jsonObj = JsonCreateObject();
[](#cb3-3)
[](#cb3-4)// 设置基本字符串
[](#cb3-5)int result = JsonSetString(jsonObj, "name", "test");
[](#cb3-6)if (result == 0) {
[](#cb3-7)    printf("设置字符串成功\n");
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)// 设置包含特殊字符的字符串
[](#cb3-11)JsonSetString(jsonObj, "message", "Hello \"World\"");
[](#cb3-12)JsonSetString(jsonObj, "path", "C:\\Program Files\\App");
[](#cb3-13)
[](#cb3-14)// 序列化查看结果
[](#cb3-15)int err = 0;
[](#cb3-16)const char* jsonStr = JsonStringify(jsonObj, 2, &err);
[](#cb3-17)if (jsonStr != 0 && err == 0) {
[](#cb3-18)    printf("JSON: %s\n", jsonStr);
[](#cb3-19)    FreeStringPtr(jsonStr);
[](#cb3-20)}
[](#cb3-21)
[](#cb3-22)JsonFree(jsonObj);
```

## 返回值

返回操作结果错误码，0表示成功

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 如果key已存在，会覆盖原有值

- 支持包含特殊字符的字符串（会自动转义）

- 字符串值会被正确转义为JSON格式

---

# 设置JSON对象中的布尔值 -
JsonSetBool

## 函数简介

设置JSON对象中指定键的布尔值。

## 接口名称

```
JsonSetBool
```

## DLL调用

```
int JsonSetBool(long obj, string key, int value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
obj |
长整数型 |
JSON对象句柄 |
|

|
key |
字符串 |
键名 |
|

|
value |
整数型 |
布尔值（0表示false，非0表示true） |
|

### 示例

```
[](#cb3-1)// 设置JSON对象中的布尔值
[](#cb3-2)long jsonObj = JsonCreateObject();
[](#cb3-3)
[](#cb3-4)// 设置基本布尔值
[](#cb3-5)int result = JsonSetBool(jsonObj, "state", "1");
[](#cb3-6)if (result == 0) {
[](#cb3-7)    printf("设置布尔值成功\n");
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)// 序列化查看结果
[](#cb3-11)int err = 0;
[](#cb3-12)const char* jsonStr = JsonStringify(jsonObj, 2, &err);
[](#cb3-13)if (jsonStr != 0 && err == 0) {
[](#cb3-14)    printf("JSON: %s\n", jsonStr);
[](#cb3-15)    FreeStringPtr(jsonStr);
[](#cb3-16)}
[](#cb3-17)
[](#cb3-18)JsonFree(jsonObj);
```

## 返回值

返回操作结果错误码，0表示成功

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 如果key已存在，会覆盖原有值

---

# 设置JSON对象中的数值 -
JsonSetNumber

## 函数简介

设置JSON对象中指定键的数值。

## 接口名称

```
JsonSetNumber
```

## DLL调用

```
int JsonSetNumber(long obj, string key, double value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
obj |
长整数型 |
JSON对象句柄 |
|

|
key |
字符串 |
键名 |
|

|
value |
双精度浮点数 |
数值 |
|

### 示例

```
[](#cb3-1)// 设置JSON对象中的数值
[](#cb3-2)long jsonObj = JsonCreateObject();
[](#cb3-3)
[](#cb3-4)// 设置整数
[](#cb3-5)int result = JsonSetNumber(jsonObj, "age", 25);
[](#cb3-6)if (result == 0) {
[](#cb3-7)    printf("设置整数成功\n");
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)// 设置浮点数
[](#cb3-11)JsonSetNumber(jsonObj, "score", 98.5);
[](#cb3-12)JsonSetNumber(jsonObj, "pi", 3.14159);
[](#cb3-13)
[](#cb3-14)// 设置负数
[](#cb3-15)JsonSetNumber(jsonObj, "temperature", -5.2);
[](#cb3-16)
[](#cb3-17)// 序列化查看结果
[](#cb3-18)int err = 0;
[](#cb3-19)const char* jsonStr = JsonStringify(jsonObj, 2, &err);
[](#cb3-20)if (jsonStr != 0 && err == 0) {
[](#cb3-21)    printf("JSON: %s\n", jsonStr);
[](#cb3-22)    FreeStringPtr(jsonStr);
[](#cb3-23)}
[](#cb3-24)
[](#cb3-25)JsonFree(jsonObj);
```

## 返回值

返回操作结果错误码，0表示成功

## 错误码说明

|
错误码 |
说明 |
|

|
JSON_SUCCESS (0) |
操作成功 |
|

|
JSON_ERROR_INVALID_HANDLE (1) |
无效的句柄 |
|

|
JSON_ERROR_PARSE_FAILED (2) |
JSON解析失败 |
|

|
JSON_ERROR_TYPE_MISMATCH (3) |
类型不匹配 |
|

|
JSON_ERROR_KEY_NOT_FOUND (4) |
键不存在 |
|

|
JSON_ERROR_INDEX_OUT_OF_RANGE (5) |
索引超出范围 |
|

|
JSON_ERROR_UNKNOWN (6) |
未知错误 |
|

## 注意事项

- 如果key已存在，会覆盖原有值

- 支持整数和浮点数

- 数值会被正确格式化为JSON数字格式

---

# 释放JSON对象 - JsonFree

## 函数简介

释放JSON对象占用的内存，防止内存泄漏。

## 接口名称

```
JsonFree
```

## DLL调用

```
int JsonFree(long obj)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
obj |
长整数型 |
要释放的JSON对象句柄 |
|

### 示例

```
[](#cb3-1)// 创建并使用JSON对象
[](#cb3-2)long jsonObj = JsonCreateObject();
[](#cb3-3)JsonSetString(jsonObj, "name", "test");
[](#cb3-4)
[](#cb3-5)// 使用完毕后释放内存
[](#cb3-6)JsonFree(jsonObj);
```

## 返回值

成功返回1，失败返回0。

## 注意事项

- 必须调用此函数释放JSON对象内存，否则会造成内存泄漏

- 释放后的句柄不能再使用

- 可以安全地传递0作为参数（无操作）

---

## YOLO

# YOLO

AI模块

---

## 其他

# 从内存地址读取字符串 -
GetStringFromPtr

### 函数简介

从指定内存地址读取字符串,参考windows函数 [GetWindowText](https://learn.microsoft.com/zh-cn/windows/win32/api/winuser/nf-winuser-getwindowtexta)实现

### 接口名称

```
GetStringFromPtr
```

### DLL调用

```
int GetStringFromPtr(long ptr, LPSTR lpString, int size)
```

#### 参数定义:

-
`ptr` (长整型数): 字符串内存地址。

-
`lpString` (字符串): 接收字符串的缓冲区

-
`size` (整数型) : 缓冲区大小,可以通过 [GetStringSize](/其他/读取字符串大小%20-%20GetStringSize.html)接口读取字符串大小,size要+1用于存储终止符’\0’

#### 返回值:

整型数 : 成功返回字符串实际长度，失败返回0

#### 示例:

```
[](#cb3-1)long strPtr = 0x12345678; // 示例内存地址
[](#cb3-2)int size=ola.GetStringSize(strPtr)+1;+1 用于存储终止符 '\0'
[](#cb3-3)char* buffer = new char[size]{0}; // 使用 new[] 动态分配
[](#cb3-4)int length = ola.GetStringFromPtr(strPtr, buffer, sizeof(buffer));
[](#cb3-5)if (length > 0) {
[](#cb3-6)    printf("读取到的字符串: %s\n", buffer);
[](#cb3-7)} else {
[](#cb3-8)    printf("读取失败\n");
[](#cb3-9)}
```

### 备注

- 使用此函数时需要确保传入的内存地址有效且可访问

- 建议在使用前先通过GetStringSize接口获取实际需要的缓冲区大小

- 缓冲区大小不足可能导致字符串截断

---

# 创建OLA-COM对象

### 函数简介

创建OLA-COM对象,无需额外DLL可以实现免注册加载COM对象

#### 注意事项

- DLL与COM的调用模式不一样

- 免注册环境下COM类可以写成ola.olasoft ola olaplug ola.ola ola.olasoft
OlaPlug.OlaSoft 任意一种都可以注册com对象

### COM调用

```

COM("OlaPlug.OlaSoft")

```

### 返回值

欧拉COM对象

#### 示例:

@tab 按键精灵

```
[](#cb2-1)
[](#cb2-2)Public Declare Function InitCom lib "C:\OLAPlug_x86.dll" Alias "InitCom" () As Long
[](#cb2-3)TracePrint InitCom()
[](#cb2-4)Set ola = createobject("OlaPlug.OlaSoft")
[](#cb2-5)TracePrint ola.Ver()
```

@tab Tc

```
[](#cb3-1)
[](#cb3-2)var olaModule=dllcall("kernel32.dll","1ong","LoadLibraryA","char *","C:\\OLAPlug_x86.dll")
[](#cb3-3)var initCom_t=dllcall("kernel32.dll","long","GetProcAddress","long",olaModule,"char *","InitCom")
[](#cb3-4)pointercall("long",initCom_t)
[](#cb3-5)var ola = com("OlaPlug.OlaSoft")
[](#cb3-6)messagebox(ola.ver())
```

---

# 创建OLA对象

### 函数简介

创建OLA对象

#### 注意事项

DLL与COM的调用模式不一样

### DLL调用

```

long CreateCOLAPlugInterFace()

```

### 返回值

长整型数:

OLAPlug对象,用于后续接口的传参

#### 示例:

@tab c++

```
[](#cb2-1)#include <iostream>
[](#cb2-2)#include <windows.h>
[](#cb2-3)#include "OLAPlug.h"
[](#cb2-4)
[](#cb2-5)// 定义DLL导出函数的函数指针类型
[](#cb2-6)typedef OLAPlug* (*CreateCOLAPlugInterFaceFunc)();
[](#cb2-7)typedef int (*DestroyCOLAPlugInterFaceFunc)(OLAPlug* instance);
[](#cb2-8)typedef const char* (*VerFunc)(OLAPlug* instance);
[](#cb2-9)
[](#cb2-10)int main() {
[](#cb2-11)    // 加载DLL
[](#cb2-12)    HMODULE hModule = LoadLibrary(L"OLAPlugDll.dll");
[](#cb2-13)    if (!hModule) {
[](#cb2-14)        std::cerr << "Failed to load OLAPlugDll.dll" << std::endl;
[](#cb2-15)        return 1;
[](#cb2-16)    }
[](#cb2-17)
[](#cb2-18)    // 获取CreateCOLAPlugInterFace
[](#cb2-19)    CreateCOLAPlugInterFaceFunc CreateCOLAPlugInterFace = (CreateCOLAPlugInterFaceFunc)GetProcAddress(hModule, "CreateCOLAPlugInterFace");
[](#cb2-20)    if (!CreateCOLAPlugInterFace) {
[](#cb2-21)        std::cerr << "Failed to get CreateCOLAPlugInterFace address" << std::endl;
[](#cb2-22)        FreeLibrary(hModule);
[](#cb2-23)        return 1;
[](#cb2-24)    }
[](#cb2-25)
[](#cb2-26)    // 获取DestroyCOLAPlugInterFace
[](#cb2-27)    DestroyCOLAPlugInterFaceFunc DestroyCOLAPlugInterFace = (DestroyCOLAPlugInterFaceFunc)GetProcAddress(hModule, "DestroyCOLAPlugInterFace");
[](#cb2-28)    if (!DestroyCOLAPlugInterFace) {
[](#cb2-29)        std::cerr << "Failed to get DestroyCOLAPlugInterFace address" << std::endl;
[](#cb2-30)        FreeLibrary(hModule);
[](#cb2-31)        return 1;
[](#cb2-32)    }
[](#cb2-33)
[](#cb2-34)    // 获取Ver
[](#cb2-35)    VerFunc Ver = (VerFunc)GetProcAddress(hModule, "Ver");
[](#cb2-36)    if (!Ver) {
[](#cb2-37)        std::cerr << "Failed to get Ver address" << std::endl;
[](#cb2-38)        FreeLibrary(hModule);
[](#cb2-39)        return 1;
[](#cb2-40)    }
[](#cb2-41)
[](#cb2-42)    // 创建OLAPlug实例
[](#cb2-43)    OLAPlug* instance = CreateCOLAPlugInterFace();
[](#cb2-44)    if (!instance) {
[](#cb2-45)        std::cerr << "Failed to create OLAPlug instance" << std::endl;
[](#cb2-46)        FreeLibrary(hModule);
[](#cb2-47)        return 1;
[](#cb2-48)    }
[](#cb2-49)
[](#cb2-50)    // 调用Ver函数
[](#cb2-51)    const char* version = Ver(instance);
[](#cb2-52)    std::cout << "OLAPlug version: " << version << std::endl;
[](#cb2-53)
[](#cb2-54)    // 销毁OLAPlug实例
[](#cb2-55)    DestroyCOLAPlugInterFace(instance);
[](#cb2-56)
[](#cb2-57)    // 释放DLL
[](#cb2-58)    FreeLibrary(hModule);
[](#cb2-59)
[](#cb2-60)    return 0;
[](#cb2-61)}
```

@tab c##

```
[](#cb3-1)using System;
[](#cb3-2)using System.Runtime.InteropServices;
[](#cb3-3)
[](#cb3-4)class Program
[](#cb3-5){
[](#cb3-6)    [DllImport("kernel32.dll", SetLastError = true)]
[](#cb3-7)    private static extern IntPtr LoadLibrary(string lpFileName);
[](#cb3-8)
[](#cb3-9)    [DllImport("OLAPlugDll.dll")]
[](#cb3-10)    private static extern IntPtr CreateCOLAPlugInterFace();
[](#cb3-11)
[](#cb3-12)    static void Main()
[](#cb3-13)    {
[](#cb3-14)        // 加载DLL
[](#cb3-15)        IntPtr hModule = LoadLibrary("path/to/OLAPlugDll.dll");
[](#cb3-16)        if (hModule == IntPtr.Zero)
[](#cb3-17)        {
[](#cb3-18)            Console.Error.WriteLine("Failed to load DLL");
[](#cb3-19)            return;
[](#cb3-20)        }
[](#cb3-21)
[](#cb3-22)        // 调用函数
[](#cb3-23)        IntPtr result = CreateCOLAPlugInterFace();
[](#cb3-24)        if (result != IntPtr.Zero) {
[](#cb3-25)            Console.WriteLine("Function executed successfully, result: " + result);
[](#cb3-26)        } else {
[](#cb3-27)            Console.Error.WriteLine("Function execution failed");
[](#cb3-28)        }
[](#cb3-29)    }
[](#cb3-30)}
```

@tab python

```
[](#cb4-1)from ctypes import WinDLL
[](#cb4-2)
[](#cb4-3)# 假设DLL已经放在了合适的路径下
[](#cb4-4)olaplug_dll = WinDLL("path/to/OLAPlugDll.dll")
[](#cb4-5)
[](#cb4-6)# 调用函数
[](#cb4-7)result = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-8)if result:
[](#cb4-9)    print(f"Function executed successfully, result: {result}")
[](#cb4-10)else:
[](#cb4-11)    print("Function execution failed")
```

@tab java

```
[](#cb5-1)import com.sun.jna.Library;
[](#cb5-2)import com.sun.jna.NativeLibrary;
[](#cb5-3)import com.sun.jna.WString;
[](#cb5-4)import com.sun.jna.platform.win32.WinDef.HINSTANCE;
[](#cb5-5)
[](#cb5-6)public class DllDemo {
[](#cb5-7)    interface MyLibrary extends Library {
[](#cb5-8)        // 定义接口方法，映射到DLL中的函数
[](#cb5-9)        MyLibrary INSTANCE = (MyLibrary) NativeLibrary.getInstance("OLAPlugDll");
[](#cb5-10)        void* CreateCOLAPlugInterFace();
[](#cb5-11)    }
[](#cb5-12)
[](#cb5-13)    public static void main(String[] args) {
[](#cb5-14)        // 调用DLL中的函数
[](#cb5-15)        long result = (long) MyLibrary.INSTANCE.CreateCOLAPlugInterFace();
[](#cb5-16)        if (result != 0) {
[](#cb5-17)            System.out.println("Function executed successfully, result: " + result);
[](#cb5-18)        } else {
[](#cb5-19)            System.out.println("Function execution failed");
[](#cb5-20)        }
[](#cb5-21)    }
[](#cb5-22)}
```

@tab 易语言

```
[](#cb6-1).版本 2
[](#cb6-2).程序集 程序集1
[](#cb6-3).程序 易语言调用DLL示例
[](#cb6-4).子程序 _启动子程序, 整数型, 公开
[](#cb6-5).局部变量 接口指针, 整数型
[](#cb6-6)
[](#cb6-7)' 直接执行DLL中的函数，并将返回的指针保存到接口指针变量中
[](#cb6-8)接口指针 = 执行("CreateCOLAPlugInterFace", "OLAPlugDll.dll")
[](#cb6-9)
[](#cb6-10)' 检查函数是否成功执行
[](#cb6-11)如果 (接口指针 <> 0)
[](#cb6-12)    信息框("函数调用成功，返回指针: " + 到文本(接口指针), , #信息框仅确定按钮, #信息框图标信息)
[](#cb6-13)否则
[](#cb6-14)    信息框("函数调用失败，返回指针为0", , #信息框仅确定按钮, #信息框图标错误)
[](#cb6-15)如果结束
[](#cb6-16).子程序结束
```

---

# 执行cmd指令 - ExecuteCmd

### 函数简介

执行指定的CMD指令,并返回cmd的输出结果

### 接口名称

```
ExecuteCmd
```

### DLL调用

```
long ExecuteCmd(long ola, string cmd, string current_dir, int time_out)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `cmd` (字符串): 要执行的cmd命令。

- `current_dir` (字符串):
执行此cmd命令时所在目录。如果为空，表示使用当前目录。比如”“或者”c:“。

- `time_out` (整型数):
超时设置，单位是毫秒。0表示一直等待。大于0表示等待指定的时间后强制结束，防止卡死。

#### 示例:

待补充…

### 返回值

字符串:

cmd指令的执行结果. 返回空字符**串表示**执行失败.

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 注册到后台 - Reg

### 函数简介

调用此函数来注册，从而使用插件的高级功能.推荐使用此函数。**多个OLA对象仅需要注册一次**

### 接口名称

```
Reg
```

### 调用

```
int Reg(string userCode, string softCode, string featureList)
```

#### 参数定义:

- `userCode` (字符串): 用户码。

- `softCode` (字符串): 软件码。

- `featureList` (字符串): 功能列表。

#### 示例:

```
ola.Reg("aaa","bbb","OLA|OLAPlus")
```

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 解析返回结果数量 -
GetResultCount

### 函数简介

对插件接口的返回值进行解析，统计其中的元素个数。支持以下两类输入：

- JSON 数组（如
`["a","b","c"]`、`[1,2,3]`）

- 使用英文逗号`,` 或竖线`|` 分隔的字符串（如
`"a,b,c"`、`"a|b|c"`）

### 接口名称

```
GetResultCount
```

### DLL调用

```
int GetResultCount(string result)
```

#### 参数定义:

- `result` (字符串): 插件接口的返回值，支持 JSON
数组或以`,`/`|`分隔的字符串。

#### 示例:

```
[](#cb3-1)int c1 = GetResultCount("[1,2,3]");          // 返回 3
[](#cb3-2)int c2 = GetResultCount("a,b,c");            // 返回 3
[](#cb3-3)int c3 = GetResultCount("x|y|z");            // 返回 3
[](#cb3-4)int c4 = GetResultCount("");                 // 返回 0
```

### 返回值

整型数:

- 返回解析得到的元素个数；无法解析或为空时返回 0。

### 注意事项

- 当输入为空指针或空字符串时返回 0。

- JSON 需为数组格式（例如
`[ ... ]`）；若不是数组格式将按分隔字符串尝试解析。

---

# 读取字符串大小 -
GetStringSize

### 函数简介

读取字符串大小

### 接口名称

```
GetStringSize
```

### DLL调用

```
int32 GetStringSize(long ptr)
```

#### 参数定义:

- `ptr` (长整型数): 字符串内存地址。

#### 示例:

待补充…

### 返回值

整型数:

字符串缓冲区大小

---

# 释放OLA对象 -
DestroyCOLAPlugInterFace

### 函数简介

释放OLA对象内存

#### 注意事项

该接口为DLL版本专用

### DLL调用

```

int DestroyCOLAPlugInterFace(long ola)

```

### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 释放字符串内存 -
FreeStringPtr

### 函数简介

释放字符串内存

### 接口名称

```
FreeStringPtr
```

### DLL调用

```
int FreeStringPtr(long ptr)
```

#### 参数定义:

- `ptr` (长整型数): 要释放的字符串内存地址。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 释放字节流内存 -
FreeMemoryPtr

### 函数简介

释放字节流内存

### 接口名称

```
FreeMemoryPtr
```

### DLL调用

```
int FreeMemoryPtr(long ptr)
```

#### 参数定义:

- `ptr` (长整型数): 要释放的字节流地址。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

## 内存

# 32位整数转64位整数 -
Int32ToInt64

## 函数简介

把32位整数转换成64位整数。

## 接口名称

```
Int32ToInt64
```

## DLL调用

```
long Int32ToInt64(long instance, int v)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
v |
整数型 |
32位整数 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

64位整数

---

# 64位整数转32位整数 -
Int64ToInt32

## 函数简介

把64位整数转换成32位整数。

## 接口名称

```
Int64ToInt32
```

## DLL调用

```
int Int64ToInt32(long instance, long v)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
v |
长整数型 |
64位整数 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

32位整数

---

# 写入指定地址的单精度浮点数
- WriteFloat

## 函数简介

写入指定地址的单精度浮点数，地址支持CE数据格式。

```
* [[[<module>+offset1]+offset2]+offset3]
* <Game.exe>+1234+8+4
* [<Game.exe>+1234]+8+4
* [ [<Game.exe>+1234]+8 ]+4
* <Game.exe>+1234
* [0x12345678]+10
```

## 接口名称

```
WriteFloat
```

## DLL调用

```
int WriteFloat(long instance, long hwnd, string addr, float float_value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
字符串 |
地址，支持CE数据格式 |
|

|
float_value |
单精度浮点数 |
单精度浮点数 |
|

### 示例

```
[](#cb4-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 写入指定地址的单精度浮点数
- WriteFloatAddr

## 函数简介

写入指定地址的单精度浮点数。

## 接口名称

```
WriteFloatAddr
```

## DLL调用

```
int WriteFloatAddr(long instance, long hwnd, long addr, float float_value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
长整数型 |
地址 |
|

|
float_value |
单精度浮点数 |
单精度浮点数 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 写入指定地址的双精度浮点数
- WriteDouble

## 函数简介

写入指定地址的双精度浮点数，地址支持CE数据格式。

```
* [[[<module>+offset1]+offset2]+offset3]
* <Game.exe>+1234+8+4
* [<Game.exe>+1234]+8+4
* [ [<Game.exe>+1234]+8 ]+4
* <Game.exe>+1234
* [0x12345678]+10
```

## 接口名称

```
WriteDouble
```

## DLL调用

```
int WriteDouble(long instance, long hwnd, string addr, double double_value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
字符串 |
地址，支持CE数据格式 |
|

|
double_value |
双精度浮点数 |
双精度浮点数 |
|

### 示例

```
[](#cb4-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 写入指定地址的双精度浮点数
- WriteDoubleAddr

## 函数简介

写入指定地址的双精度浮点数。

## 接口名称

```
WriteDoubleAddr
```

## DLL调用

```
int WriteDoubleAddr(long instance, long hwnd, long addr, double double_value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
长整数型 |
地址 |
|

|
double_value |
双精度浮点数 |
双精度浮点数 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 写入指定地址的字符串 -
WriteString

## 函数简介

写入指定地址的字符串，支持多种字符串类型和CE数据格式。

## 接口名称

```
WriteString
```

## DLL调用

```
int WriteString(long instance, long hwnd, string addr, int type, string value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
字符串 |
地址，支持CE数据格式 |
|

|
type |
整数型 |
字符串类型(0:Ascii,1:Unicode,2:UTF8) |
|

|
value |
字符串 |
要写入的字符串 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 写入指定地址的字符串 -
WriteStringAddr

## 函数简介

写入指定地址的字符串。

## 接口名称

```
WriteStringAddr
```

## DLL调用

```
int WriteStringAddr(long instance, long hwnd, long addr, int type, string value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
长整数型 |
地址 |
|

|
type |
整数型 |
字符串类型(0:Ascii,1:Unicode,2:UTF8) |
|

|
value |
字符串 |
要写入的字符串 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 写入指定地址的数据 -
WriteData

## 函数简介

写入指定地址的数据，地址支持CE数据格式。

```
* [[[<module>+offset1]+offset2]+offset3]
* <Game.exe>+1234+8+4
* [<Game.exe>+1234]+8+4
* [ [<Game.exe>+1234]+8 ]+4
* <Game.exe>+1234
* [0x12345678]+10
```

## 接口名称

```
WriteData
```

## DLL调用

```
int WriteData(long instance, long hwnd, string addr, string data)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
字符串 |
地址，支持CE数据格式 |
|

|
data |
字符串 |
数据，二进制数据字符串，如”12 34 56 78” |
|

### 示例

```
[](#cb4-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 写入指定地址的数据 -
WriteDataAddr

## 函数简介

写入指定地址的数据。

## 接口名称

```
WriteDataAddr
```

## DLL调用

```
int WriteDataAddr(long instance, long hwnd, long addr, string data)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
长整数型 |
地址 |
|

|
data |
字符串 |
数据，二进制数据字符串，如”12 34 56 78” |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 写入指定地址的数据 -
WriteDataAddrFromBin

## 函数简介

写入指定地址的数据，数据以字符串数据地址形式传递。

## 接口名称

```
WriteDataAddrFromBin
```

## DLL调用

```
int WriteDataAddrFromBin(long instance, long hwnd, long addr, long data)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
长整数型 |
地址 |
|

|
data |
长整数型 |
字符串数据地址 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 写入指定地址的数据 -
WriteDataFromBin

## 函数简介

写入指定地址的数据，数据以字符串数据地址形式传递，地址支持CE数据格式。

```
* [[[<module>+offset1]+offset2]+offset3]
* <Game.exe>+1234+8+4
* [<Game.exe>+1234]+8+4
* [ [<Game.exe>+1234]+8 ]+4
* <Game.exe>+1234
* [0x12345678]+10
```

## 接口名称

```
WriteDataFromBin
```

## DLL调用

```
int WriteDataFromBin(long instance, long hwnd, string addr, long data)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
字符串 |
地址，支持CE数据格式 |
|

|
data |
长整数型 |
字符串数据地址 |
|

### 示例

```
[](#cb4-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 写入指定地址的整数 -
WriteInt

## 函数简介

写入指定地址的整数，支持多种整数类型和CE数据格式。

## 接口名称

```
WriteInt
```

## DLL调用

```
int WriteInt(long instance, long hwnd, string addr, int type, long value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
字符串 |
地址，支持CE数据格式 |
|

|
type |
整数型 |
整数类型(0:32位有符号,1:16位有符号,2:8位有符号,3:64位,4:32位无符号,5:16位无符号,6:8位无符号) |
|

|
value |
长整数型 |
要写入的整数值 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 写入指定地址的整数 -
WriteIntAddr

## 函数简介

写入指定地址的整数。

## 接口名称

```
WriteIntAddr
```

## DLL调用

```
int WriteIntAddr(long instance, long hwnd, long addr, int type, long value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
长整数型 |
地址 |
|

|
type |
整数型 |
整数类型(0:32位有符号,1:16位有符号,2:8位有符号,3:64位,4:32位无符号,5:16位无符号,6:8位无符号) |
|

|
value |
长整数型 |
要写入的整数值 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 单精度浮点数转二进制 -
FloatToData

## 函数简介

把单精度浮点数转换成二进制形式（IEEE 754标准）

## 接口名称

```
FloatToData
```

## DLL调用

```
long FloatToData(long instance, float float_value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
float_value |
单精度浮点数 |
float值 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 双精度浮点数转二进制 -
DoubleToData

## 函数简介

把双精度浮点数转换成二进制形式（IEEE 754标准）

## 接口名称

```
DoubleToData
```

## DLL调用

```
long DoubleToData(long instance, double double_value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html)
接口生成。句柄 |
|

|
double_value |
双精度浮点数 |
需要转换的double值 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针

## 注意事项

- 需要Memory权限

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 字符串转二进制 -
StringToData

## 函数简介

把字符串转换成二进制形式。

## 接口名称

```
StringToData
```

## DLL调用

```
long StringToData(long instance, string string_value, int type)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
string_value |
字符串 |
字符串值 |
|

|
type |
整数型 |
类型 0:Ascii 1:Unicode 2:UTF8 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 指定窗口修改内存保护属性
- VirtualProtectEx

## 函数简介

修改指定的内存保护属性。

## 接口名称

```
VirtualProtectEx
```

## DLL调用

```
int VirtualProtectEx(long instance, long hwnd, long addr, int size, int type, int protect)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄或进程ID |
|

|
addr |
长整数型 |
要修改的内存地址 |
|

|
size |
整数型 |
需要修改的内存大小 |
|

|
type |
整数型 |
内存类型(0:可读写可执行,1:可读可执行,2:可读写) |
|

|
protect |
整数型 |
修改前的保护属性 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回修改之前的读写属性，失败返回-1

---

# 指定窗口分配内存 -
VirtualAllocEx

## 函数简介

在指定的窗口所在进程分配一段内存。

## 接口名称

```
VirtualAllocEx
```

## DLL调用

```
long VirtualAllocEx(long instance, long hwnd, long addr, int size, int type)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄或进程ID |
|

|
addr |
长整数型 |
预期分配地址，0为自动分配 |
|

|
size |
整数型 |
分配的内存大小 |
|

|
type |
整数型 |
内存类型(0:可读写可执行,1:可读可执行,2:可读写) |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

分配的内存地址，0表示分配失败

---

# 指定窗口查询内存信息 -
VirtualQueryEx

## 函数简介

查询指定的内存信息。 结构体指针信息

```
typedef struct _MEMORY_BASIC_INFORMATION32 {

DWORD BaseAddress;

DWORD AllocationBase;

DWORD AllocationProtect;

DWORD RegionSize;

DWORD State;

DWORD Protect;

DWORD Type;

} MEMORY_BASIC_INFORMATION32, *PMEMORY_BASIC_INFORMATION32;

typedef struct DECLSPEC_ALIGN(16) _MEMORY_BASIC_INFORMATION64 {

ULONGLONG BaseAddress;

ULONGLONG AllocationBase;

DWORD     AllocationProtect;

DWORD     __alignment1;

ULONGLONG RegionSize;

DWORD     State;

DWORD     Protect;

DWORD     Type;

DWORD     __alignment2;

} MEMORY_BASIC_INFORMATION64, *PMEMORY_BASIC_INFORMATION64;

```

## 接口名称

```
VirtualQueryEx
```

## DLL调用

```
long VirtualQueryEx(long instance, long hwnd, long addr, long pmbi)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄或进程ID |
|

|
addr |
长整数型 |
要查询的内存地址 |
|

|
pmbi |
长整数型 |
内存信息结构体指针 |
|

### 示例

```
[](#cb4-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针，.
内容是”BaseAddress,AllocationBase,AllocationProtect,RegionSize,State,Protect,Type”
数值都是10进制表达.

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 指定窗口释放内存 -
VirtualFreeEx

## 函数简介

释放指定的内存。

## 接口名称

```
VirtualFreeEx
```

## DLL调用

```
int VirtualFreeEx(long instance, long hwnd, long addr)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄或进程ID |
|

|
addr |
长整数型 |
要释放的内存地址 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 搜索二进制数据 - FindData

## 函数简介

搜索指定的二进制数据,默认步长是1.默认开启多线程,默认搜索全部内存类型.如果要定制搜索,请用FindDataEx。

## 接口名称

```
FindData
```

## DLL调用

```
long FindData(long instance, long hwnd, string addr_range, string data)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr_range |
字符串 |
地址范围 |
|

|
data |
字符串 |
要搜索的二进制数据,支持单字节CE数据格式搜索,比如”00 01 23 45 * ?? ?b
c? * f1”等. |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 搜索二进制数据 - FindDataEx

## 函数简介

搜索指定的二进制数据,可定制步长、多线程、内存类型等。

## 接口名称

```
FindDataEx
```

## DLL调用

```
long FindDataEx(long instance, long hwnd, string addr_range, string data, int step, int multi_thread, int mode)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr_range |
字符串 |
地址范围 |
|

|
data |
字符串 |
要搜索的二进制数据,支持单字节CE数据格式搜索,比如”00 01 23 45 * ?? ?b
c? * f1”等. |
|

|
step |
整数型 |
步长 |
|

|
multi_thread |
整数型 |
是否开启多线程 |
|

|
mode |
整数型 |
搜索模式(0:全部,1:可写,2:不可写,4:可执行,8:不可执行,16:写时复制,32:不写时复制) |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针，格式: “addr1|addr2|…|addrn”

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 搜索单精度浮点数 - FindFloat

## 函数简介

搜索指定范围内的单精度浮点数。

## 接口名称

```
FindFloat
```

## DLL调用

```
long FindFloat(long instance, long hwnd, string addr_range, float float_value_min, float float_value_max)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr_range |
字符串 |
地址范围 |
|

|
float_value_min |
单精度浮点数 |
最小值 |
|

|
float_value_max |
单精度浮点数 |
最大值 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针，格式: “addr1|addr2|…|addrn”

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 搜索单精度浮点数 -
FindFloatEx

## 函数简介

搜索指定范围内的单精度浮点数,可定制步长、多线程、内存类型等。

## 接口名称

```
FindFloatEx
```

## DLL调用

```
long FindFloatEx(long instance, long hwnd, string addr_range, float float_value_min, float float_value_max, int step, int multi_thread, int mode)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr_range |
字符串 |
地址范围 |
|

|
float_value_min |
单精度浮点数 |
最小值 |
|

|
float_value_max |
单精度浮点数 |
最大值 |
|

|
step |
整数型 |
步长 |
|

|
multi_thread |
整数型 |
是否开启多线程 |
|

|
mode |
整数型 |
搜索模式(0:全部,1:可写,2:不可写,4:可执行,8:不可执行,16:写时复制,32:不写时复制) |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针，格式: “addr1|addr2|…|addrn”

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 搜索双精度浮点数 -
FindDouble

## 函数简介

搜索指定范围内的双精度浮点数。

## 接口名称

```
FindDouble
```

## DLL调用

```
long FindDouble(long instance, long hwnd, string addr_range, double double_value_min, double double_value_max)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr_range |
字符串 |
地址范围 |
|

|
double_value_min |
双精度浮点数 |
最小值 |
|

|
double_value_max |
双精度浮点数 |
最大值 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针，格式: “addr1|addr2|…|addrn”

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 搜索双精度浮点数 -
FindDoubleEx

## 函数简介

搜索指定范围内的双精度浮点数,可定制步长、多线程、内存类型等。

## 接口名称

```
FindDoubleEx
```

## DLL调用

```
long FindDoubleEx(long instance, long hwnd, string addr_range, double double_value_min, double double_value_max, int step, int multi_thread, int mode)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr_range |
字符串 |
地址范围 |
|

|
double_value_min |
双精度浮点数 |
最小值 |
|

|
double_value_max |
双精度浮点数 |
最大值 |
|

|
step |
整数型 |
步长 |
|

|
multi_thread |
整数型 |
是否开启多线程 |
|

|
mode |
整数型 |
搜索模式(0:全部,1:可写,2:不可写,4:可执行,8:不可执行,16:写时复制,32:不写时复制) |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针，格式: “addr1|addr2|…|addrn”

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 搜索字符串 - FindString

## 函数简介

搜索指定范围内的字符串。

## 接口名称

```
FindString
```

## DLL调用

```
long FindString(long instance, long hwnd, string addr_range, string string_value, int type)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr_range |
字符串 |
地址范围 |
|

|
string_value |
字符串 |
要搜索的字符串 |
|

|
type |
整数型 |
类型(0:Ascii,1:Unicode,2:UTF8) |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针，格式: “addr1|addr2|…|addrn”

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 搜索字符串 - FindStringEx

## 函数简介

搜索指定范围内的字符串,可定制步长、多线程、内存类型等。

## 接口名称

```
FindStringEx
```

## DLL调用

```
long FindStringEx(long instance, long hwnd, string addr_range, string string_value, int type, int step, int multi_thread, int mode)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr_range |
字符串 |
地址范围 |
|

|
string_value |
字符串 |
要搜索的字符串 |
|

|
type |
整数型 |
类型(0:Ascii,1:Unicode,2:UTF8) |
|

|
step |
整数型 |
步长 |
|

|
multi_thread |
整数型 |
是否开启多线程 |
|

|
mode |
整数型 |
搜索模式(0:全部,1:可写,2:不可写,4:可执行,8:不可执行,16:写时复制,32:不写时复制) |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针，格式: “addr1|addr2|…|addrn”

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 搜索长整型数 - FindInt

## 函数简介

搜索指定范围内的长整型数。

## 接口名称

```
FindInt
```

## DLL调用

```
long FindInt(long instance, long hwnd, string addr_range, long int_value_min, long int_value_max, int type)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr_range |
字符串 |
地址范围 |
|

|
int_value_min |
长整数型 |
最小值 |
|

|
int_value_max |
长整数型 |
最大值 |
|

|
type |
整数型 |
整数类型(0:32位,1:16位,2:8位,3:64位) |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针，格式: “addr1|addr2|…|addrn”

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 搜索长整型数 - FindIntEx

## 函数简介

搜索指定范围内的长整型数,可定制步长、多线程、内存类型等。

## 接口名称

```
FindIntEx
```

## DLL调用

```
long FindIntEx(long instance, long hwnd, string addr_range, long int_value_min, long int_value_max, int type, int step, int multi_thread, int mode)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr_range |
字符串 |
地址范围 |
|

|
int_value_min |
长整数型 |
最小值 |
|

|
int_value_max |
长整数型 |
最大值 |
|

|
type |
整数型 |
整数类型(0:32位,1:16位,2:8位,3:64位) |
|

|
step |
整数型 |
步长 |
|

|
multi_thread |
整数型 |
是否开启多线程 |
|

|
mode |
整数型 |
搜索模式(0:全部,1:可写,2:不可写,4:可执行,8:不可执行,16:写时复制,32:不写时复制) |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针，格式: “addr1|addr2|…|addrn”

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 获取模块基地址 -
GetModuleBaseAddr

## 函数简介

获取模块基地址。

## 接口名称

```
GetModuleBaseAddr
```

## DLL调用

```
long GetModuleBaseAddr(long instance, long hwnd, string module_name)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
module_name |
字符串 |
模块名 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回模块基地址，失败返回0

---

# 获取模块大小 - GetModuleSize

## 函数简介

获取模块大小。

## 接口名称

```
GetModuleSize
```

## DLL调用

```
int GetModuleSize(long instance, long hwnd, string module_name)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
module_name |
字符串 |
模块名 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回模块大小，失败返回0

---

# 获取远程API地址 -
GetRemoteApiAddress

## 函数简介

获取远程API地址。

## 接口名称

```
GetRemoteApiAddress
```

## DLL调用

```
long GetRemoteApiAddress(long instance, long hwnd, long base_addr, string fun_name)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
base_addr |
长整数型 |
基地址 |
|

|
fun_name |
字符串 |
函数名 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回远程API地址，失败返回0

---

# 设置是否把所有内存接口函数中的窗口句柄当作进程ID
- SetMemoryHwndAsProcessId

## 函数简介

设置是否把所有内存接口函数中的窗口句柄当作进程ID。

## 接口名称

```
SetMemoryHwndAsProcessId
```

## DLL调用

```
int SetMemoryHwndAsProcessId(long instance, int enable)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
enable |
整数型 |
是否启用(0:不启用,1:启用) |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 读取指定地址的单精度浮点数 -
ReadFloat

## 函数简介

读取指定地址的单精度浮点数，地址支持CE数据格式。

```
* [[[<module>+offset1]+offset2]+offset3]
* <Game.exe>+1234+8+4
* [<Game.exe>+1234]+8+4
* [ [<Game.exe>+1234]+8 ]+4
* <Game.exe>+1234
* [0x12345678]+10
```

## 接口名称

```
ReadFloat
```

## DLL调用

```
float ReadFloat(long instance, long hwnd, string addr)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
字符串 |
地址，支持CE数据格式 |
|

### 示例

```
[](#cb4-1)// 示例代码待补充
```

## 返回值

读取到的单精度浮点数

---

# 读取指定地址的单精度浮点数
- ReadFloatAddr

## 函数简介

读取指定地址的单精度浮点数。

## 接口名称

```
ReadFloatAddr
```

## DLL调用

```
float ReadFloatAddr(long instance, long hwnd, long addr)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
长整数型 |
地址 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

读取到的单精度浮点数

---

# 读取指定地址的双精度浮点数
- ReadDouble

## 函数简介

读取指定地址的双精度浮点数，地址支持CE数据格式。

```
* [[[<module>+offset1]+offset2]+offset3]
* <Game.exe>+1234+8+4
* [<Game.exe>+1234]+8+4
* [ [<Game.exe>+1234]+8 ]+4
* <Game.exe>+1234
* [0x12345678]+10
```

## 接口名称

```
ReadDouble
```

## DLL调用

```
double ReadDouble(long instance, long hwnd, string addr)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
字符串 |
地址，支持CE数据格式 |
|

### 示例

```
[](#cb4-1)// 示例代码待补充
```

## 返回值

读取到的双精度浮点数

---

# 读取指定地址的双精度浮点数
- ReadDoubleAddr

## 函数简介

读取指定地址的双精度浮点数。

## 接口名称

```
ReadDoubleAddr
```

## DLL调用

```
double ReadDoubleAddr(long instance, long hwnd, long addr)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
长整数型 |
地址 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

读取到的双精度浮点数

---

# 读取指定地址的字符串 -
ReadString

## 函数简介

读取指定地址的字符串，支持多种字符串类型和CE数据格式。

## 接口名称

```
ReadString
```

## DLL调用

```
long ReadString(long instance, long hwnd, string addr, int type, int len)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
字符串 |
地址，支持CE数据格式 |
|

|
type |
整数型 |
字符串类型(0:GBK,1:Unicode,2:UTF8) |
|

|
len |
整数型 |
需要读取的字节数，0为自动判定 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针，内容为UTF-8编码

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 读取指定地址的字符串 -
ReadStringAddr

## 函数简介

读取指定地址的字符串。

## 接口名称

```
ReadStringAddr
```

## DLL调用

```
long ReadStringAddr(long instance, long hwnd, long addr, int type, int len)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
长整数型 |
地址 |
|

|
type |
整数型 |
字符串类型(0:GBK,1:Unicode,2:UTF8) |
|

|
len |
整数型 |
需要读取的字节数，0为自动判定 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针，内容为UTF-8编码

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 读取指定地址的数据 -
ReadData

## 函数简介

读取指定地址的数据，地址支持CE数据格式。

```
* [[[<module>+offset1]+offset2]+offset3]
* <Game.exe>+1234+8+4
* [<Game.exe>+1234]+8+4
* [ [<Game.exe>+1234]+8 ]+4
* <Game.exe>+1234
* [0x12345678]+10
```

## 接口名称

```
ReadData
```

## DLL调用

```
long ReadData(long instance, long hwnd, string addr, int len)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
字符串 |
地址，支持CE数据格式 |
|

|
len |
整数型 |
长度 |
|

### 示例

```
[](#cb4-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针，格式: 16进制字符串，每个字节以空格分隔

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 读取指定地址的数据 -
ReadDataAddr

## 函数简介

读取指定地址的数据。

## 接口名称

```
ReadDataAddr
```

## DLL调用

```
long ReadDataAddr(long instance, long hwnd, long addr, int len)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
长整数型 |
地址 |
|

|
len |
整数型 |
长度 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针，格式: 16进制字符串，每个字节以空格分隔

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 读取指定地址的数据 -
ReadDataAddrToBin

## 函数简介

读取指定地址的数据。

## 接口名称

```
ReadDataAddrToBin
```

## DLL调用

```
long ReadDataAddrToBin(long instance, long hwnd, long addr, int len)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
长整数型 |
地址 |
|

|
len |
整数型 |
长度 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

长整数型 读取到的数据指针. 返回0表示读取失败.

## 注意事项

- 返回的内存地址需要调用FreeMemoryPtr释放内存

---

# 读取指定地址的数据 -
ReadDataToBin

## 函数简介

读取指定地址的数据，地址支持CE数据格式。

```
* [[[<module>+offset1]+offset2]+offset3]
* <Game.exe>+1234+8+4
* [<Game.exe>+1234]+8+4
* [ [<Game.exe>+1234]+8 ]+4
* <Game.exe>+1234
* [0x12345678]+10
```

## 接口名称

```
ReadDataToBin
```

## DLL调用

```
long ReadDataToBin(long instance, long hwnd, string addr, int len)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
字符串 |
地址，支持CE数据格式 |
|

|
len |
整数型 |
长度 |
|

### 示例

```
[](#cb4-1)// 示例代码待补充
```

## 返回值

长整数型 读取到的数据指针. 返回0表示读取失败.

## 注意事项

返回的内存地址需要调用FreeMemoryPtr释放内存

---

# 读取指定地址的长整型数 -
ReadInt

## 函数简介

读取指定地址的长整型数，支持多种整数类型和CE数据格式。

## 接口名称

```
ReadInt
```

## DLL调用

```
long ReadInt(long instance, long hwnd, string addr, int type)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
字符串 |
地址，支持CE数据格式 |
|

|
type |
整数型 |
整数类型(0:32位有符号,1:16位有符号,2:8位有符号,3:64位,4:32位无符号,5:16位无符号,6:8位无符号) |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

读取到的整数值（64位）

---

# 读取指定地址的长整型数 -
ReadIntAddr

## 函数简介

读取指定地址的长整型数。

## 接口名称

```
ReadIntAddr
```

## DLL调用

```
long ReadIntAddr(long instance, long hwnd, long addr, int type)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
长整数型 |
地址 |
|

|
type |
整数型 |
整数类型(0:32位有符号,1:16位有符号,2:8位有符号,3:64位,4:32位无符号,5:16位无符号,6:8位无符号) |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

读取到的整数值（64位）

---

# 释放进程内存 -
FreeProcessMemory

## 函数简介

释放进程内存。

## 接口名称

```
FreeProcessMemory
```

## DLL调用

```
int FreeProcessMemory(long instance, long hwnd)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

## 加密

# AES加密 - AESEncryptEx

## 函数简介

- AES加密，支持多种加密模式和填充类型。

## 接口名称

```
AESEncryptEx
```

## DLL调用

```
long AESEncryptEx(long instance, string source, string key, string iv, int mode, int paddingType)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
source |
字符串 |
源数据。 |
|

|
key |
字符串 |
密钥。 |
|

|
iv |
字符串 |
初始向量。 |
|

|
mode |
整数 |
加密模式：0-CBC；1-ECB；2-CFB；3-OFB；4-CTS。 |
|

|
paddingType |
整数 |
填充类型：0-PKCS7；1-Zeros；2-AnsiX923；3-ISO10126；4-NoPadding。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回加密后的数据；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

# AES加密简化版本 - AESEncrypt

## 函数简介

- AES加密简化版本，使用默认参数（CBC模式和PKCS7填充，默认IV为0）。

## 接口名称

```
AESEncrypt
```

## DLL调用

```
long AESEncrypt(long instance, string source, string key)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
source |
字符串 |
源数据。 |
|

|
key |
字符串 |
密钥字符串长度应为16/24/32个字符，对应AES-128/192/256。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回加密后的数据；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

- 此接口使用CBC模式和PKCS7填充，默认IV为0。如需自定义参数请使用
AESEncryptEx。

---

# AES解密 - AESDecryptEx

## 函数简介

- AES解密，支持多种加密模式和填充类型。

## 接口名称

```
AESDecryptEx
```

## DLL调用

```
long AESDecryptEx(long instance, string source, string key, string iv, int mode, int paddingType)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
source |
字符串 |
源数据。 |
|

|
key |
字符串 |
密钥。 |
|

|
iv |
字符串 |
初始向量。 |
|

|
mode |
整数 |
加密模式：0-CBC；1-ECB；2-CFB；3-OFB；4-CTS。 |
|

|
paddingType |
整数 |
填充类型：0-PKCS7；1-Zeros；2-AnsiX923；3-ISO10126；4-NoPadding。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回解密后的数据；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

- 解密时使用的加密模式和填充类型必须与加密时一致。

---

# AES解密简化版本 - AESDecrypt

## 函数简介

- AES解密简化版本，使用默认参数（CBC模式和PKCS7填充，默认IV为0）。

## 接口名称

```
AESDecrypt
```

## DLL调用

```
long AESDecrypt(long instance, string source, string key)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
source |
字符串 |
源数据。 |
|

|
key |
字符串 |
密钥字符串长度应为16/24/32个字符，对应AES-128/192/256。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回解密后的数据；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

- 此接口使用CBC模式和PKCS7填充，默认IV为0。如需自定义参数请使用
AESDecryptEx。

---

# Base64编码 - Base64Encode

## 函数简介

- 对数据进行Base64编码。

## 接口名称

```
Base64Encode
```

## DLL调用

```
long Base64Encode(long instance, string source)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
source |
字符串 |
要进行Base64编码的源数据。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回Base64编码后的字符串；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

# Base64解码 - Base64Decode

## 函数简介

- 对Base64编码的字符串进行解码。

## 接口名称

```
Base64Decode
```

## DLL调用

```
long Base64Decode(long instance, string source)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
source |
字符串 |
Base64编码的字符串。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回解码后的原始数据；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

# HMAC消息认证码 - HMAC

## 函数简介

- 使用HMAC算法生成消息认证码，用于验证数据的完整性和真实性。

## 接口名称

```
HMAC
```

## DLL调用

```
long HMAC(long instance, string source, string key, int shaType)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
source |
字符串 |
要进行HMAC计算的源数据。 |
|

|
key |
字符串 |
HMAC密钥。 |
|

|
shaType |
整数 |
哈希类型：0-MD5；1-SHA1；2-SHA256；3-SHA384；4-SHA512；5-SHA3-256；6-SHA3-384；7-SHA3-512。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回HMAC值；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

- 密钥应保持安全，不要泄露。

---

# MD5加密 - MD5Encrypt

## 函数简介

- 使用MD5算法对数据进行哈希加密。

## 接口名称

```
MD5Encrypt
```

## DLL调用

```
long MD5Encrypt(long instance, string source)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
source |
字符串 |
源数据。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回加密后的数据；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

- MD5算法已被认为不够安全，建议在需要更高安全性的场景中使用SHA256或更高版本的哈希算法。

---

# PBKDF2密钥派生函数 - PBKDF2

## 函数简介

- 使用PBKDF2算法从密码和盐值派生密钥。

## 接口名称

```
PBKDF2
```

## DLL调用

```
long PBKDF2(long instance, string password, string salt, int iterations, int keyLength, int shaType)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
password |
字符串 |
密码。 |
|

|
salt |
字符串 |
盐值。 |
|

|
iterations |
整数 |
迭代次数。 |
|

|
keyLength |
整数 |
派生密钥长度。 |
|

|
shaType |
整数 |
哈希类型：1-SHA1；2-SHA256；3-SHA384；4-SHA512。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回派生密钥；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

- 建议迭代次数至少为10000次以确保安全性。

---

# SHA系列哈希算法 - SHAHash

## 函数简介

- 使用SHA系列哈希算法对数据进行哈希计算。

## 接口名称

```
SHAHash
```

## DLL调用

```
long SHAHash(long instance, string source, int shaType)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
source |
字符串 |
要进行哈希计算的源数据。 |
|

|
shaType |
整数 |
哈希类型：0-MD5；1-SHA1；2-SHA256；3-SHA384；4-SHA512；5-SHA3-256；6-SHA3-384；7-SHA3-512。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回哈希后的数据；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

- 推荐使用SHA256或更高版本的哈希算法以确保安全性。

---

# 使用RSA公钥加密 -
EncryptWithRsa

## 函数简介

- 使用RSA公钥对数据进行加密。

## 接口名称

```
EncryptWithRsa
```

## DLL调用

```
long EncryptWithRsa(long instance, string message, string publicKey, int paddingType)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
message |
字符串 |
要加密的明文。 |
|

|
publicKey |
字符串 |
RSA公钥。 |
|

|
paddingType |
整数 |
填充类型：0-PKCS1；1-OAEP。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回加密后的密文字符串的指针；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

# 使用RSA公钥验证签名 -
VerifySignWithRsa

## 函数简介

- 使用RSA公钥验证数据的签名。

## 接口名称

```
VerifySignWithRsa
```

## DLL调用

```
int VerifySignWithRsa(long instance, string message, string signature, int shaType, int paddingType, string publicCer)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
message |
字符串 |
要验证的明文。 |
|

|
signature |
字符串 |
签名数据。 |
|

|
shaType |
整数 |
哈希类型：0-MD5；1-SHA1；2-SHA256；3-SHA384；4-SHA512；5-SHA3-256；6-SHA3-384；7-SHA3-512。 |
|

|
paddingType |
整数 |
填充类型：0-Pkcs1；1-Pss。 |
|

|
publicCer |
字符串 |
RSA公钥。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回验证结果；1表示验证成功，0表示验证失败。

## 注意事项

- 验证时使用的哈希类型和填充类型必须与签名时一致。

---

# 使用RSA私钥签名 -
SignWithRsa

## 函数简介

- 使用RSA私钥对数据进行数字签名。

## 接口名称

```
SignWithRsa
```

## DLL调用

```
long SignWithRsa(long instance, string message, string privateCer, int shaType, int paddingType)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
message |
字符串 |
要签名的明文。 |
|

|
privateCer |
字符串 |
RSA私钥。 |
|

|
shaType |
整数 |
哈希类型：0-MD5；1-SHA1；2-SHA256；3-SHA384；4-SHA512；5-SHA3-256；6-SHA3-384；7-SHA3-512。 |
|

|
paddingType |
整数 |
填充类型：0-Pkcs1；1-Pss。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回签名后的base64字符串的指针；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

# 使用RSA私钥解密 -
DecryptWithRsa

## 函数简介

- 使用RSA私钥对加密的密文进行解密。

## 接口名称

```
DecryptWithRsa
```

## DLL调用

```
long DecryptWithRsa(long instance, string cipher, string privateKey, int paddingType)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
cipher |
字符串 |
要解密的密文。 |
|

|
privateKey |
字符串 |
RSA私钥。 |
|

|
paddingType |
整数 |
填充类型：0-PKCS1；1-OAEP。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回解密后的明文字符串的指针；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

# 生成GUID - GenerateGuid

## 函数简介

- 生成全局唯一标识符(GUID)。

## 接口名称

```
GenerateGuid
```

## DLL调用

```
long GenerateGuid(long instance, int type)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
type |
整数 |
类型：0-带-的GUID如{123e4567-e89b-12d3-a456-426614174000}；1-不带-的GUID如123e4567e89b12d3a456426614174000。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回GUID字符串的指针；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

# 生成RSA密钥 - GenerateRSAKey

## 函数简介

- 生成RSA密钥对，包括公钥和私钥，支持多种格式和密钥大小。

## 接口名称

```
GenerateRSAKey
```

## DLL调用

```
int GenerateRSAKey(long instance, string publicKeyPath, string privateKeyPath, int type, int keySize)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
publicKeyPath |
字符串 |
公钥保存路径。 |
|

|
privateKeyPath |
字符串 |
私钥保存路径。 |
|

|
type |
整数 |
类型：0-生成pem格式秘钥；1-生成xml格式秘钥；2-生成PKCS1格式秘钥。 |
|

|
keySize |
整数 |
密钥大小：512-512位；1024-1024位；2048-2048位；4096-4096位。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回0；失败返回其他值。

## 注意事项

- 生成的密钥文件将保存到指定的路径。

- 建议使用2048位或更高位数的密钥以保证安全性。

---

# 生成随机字节 -
GenerateRandomBytes

## 函数简介

- 生成指定长度和类型的随机字节字符串。

## 接口名称

```
GenerateRandomBytes
```

## DLL调用

```
long GenerateRandomBytes(long instance, int length, int type)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
length |
整数 |
要生成的随机字节长度。 |
|

|
type |
整数 |
字符类型：0-十六进制字符(0-9A-F)；1-数字+大写字母(0-9A-Z)；2-数字+大小写字母(0-9A-Za-z)；3-可打印ASCII字符(包含特殊字符)；4-Base64字符集(A-Za-z0-9+/)。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回随机字节字符串的指针；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

- 可直接用作AES密钥，推荐长度：16/24/32。

---

# 计算文件MD5哈希值 - MD5File

## 函数简介

- 计算指定文件的MD5哈希值。

## 接口名称

```
MD5File
```

## DLL调用

```
long MD5File(long instance, string filePath)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
filePath |
字符串 |
要计算MD5哈希值的文件路径。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回MD5哈希值；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

- 文件路径必须是有效的文件路径。

---

# 计算文件SHA哈希值 - SHAFile

## 函数简介

- 计算指定文件的SHA系列哈希值。

## 接口名称

```
SHAFile
```

## DLL调用

```
long SHAFile(long instance, string filePath, int shaType)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
filePath |
字符串 |
要计算SHA哈希值的文件路径。 |
|

|
shaType |
整数 |
哈希类型：0-MD5；1-SHA1；2-SHA256；3-SHA384；4-SHA512；5-SHA3-256；6-SHA3-384；7-SHA3-512。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回哈希值；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

- 文件路径必须是有效的文件路径。

---

# 转换RSA公钥 -
ConvertRSAPublicKey

## 函数简介

- 将RSA公钥从一种格式转换为另一种格式。

## 接口名称

```
ConvertRSAPublicKey
```

## DLL调用

```
long ConvertRSAPublicKey(long instance, string publicKey, int inputType, int outputType)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
publicKey |
字符串 |
要转换的公钥。 |
|

|
inputType |
整数 |
输入类型：0-pem格式；1-xml格式；2-PKCS1格式。 |
|

|
outputType |
整数 |
输出类型：0-pem格式；1-xml格式；2-PKCS1格式。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回转换后的公钥字符串的指针；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

# 转换RSA私钥 -
ConvertRSAPrivateKey

## 函数简介

- 将RSA私钥从一种格式转换为另一种格式。

## 接口名称

```
ConvertRSAPrivateKey
```

## DLL调用

```
long ConvertRSAPrivateKey(long instance, string privateKey, int inputType, int outputType)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数 |
OLAPlug实例指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
privateKey |
字符串 |
要转换的私钥。 |
|

|
inputType |
整数 |
输入类型：0-pem格式；1-xml格式；2-PKCS1格式。 |
|

|
outputType |
整数 |
输出类型：0-pem格式；1-xml格式；2-PKCS1格式。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回转换后的私钥字符串的指针；失败返回0。

## 注意事项

- 返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

## 图像处理

# 16进制格式颜色转为ARGB -
Hex2ARGB

### 函数简介

将16进制格式的字符串转换为ARGB颜色值。此函数将标准的”AARRGGBB”格式的十六进制颜色字符串转换为ARGB4个颜色分量（透明、红、绿、蓝），适用于颜色格式转换、颜色值标准化等场景。

### 接口名称

```
Hex2ARGB
```

### DLL调用

```
int Hex2ARGB(long ola,string hex, int* a, int* r, int* g, int* b)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hex` (字符串):16进制颜色值

- `a` (整型数指针): 返回透明通道值，范围0-255 0为完全透明
255为完全不透明

- `r` (整型数指针): 返回红色分量值，范围0-255

- `g` (整型数指针): 返回绿色分量值，范围0-255

- `b` (整型数指针): 返回蓝色分量值，范围0-255

#### 示例:

### 返回值

整型数: - 0: 失败 - 1: 成功

---

# 16进制格式颜色转为RGB -
Hex2RGB

### 函数简介

将16进制格式的字符串转换为ARGB颜色值。此函数将标准的”RRGGBB”或者”AARRGGBB”格式的十六进制颜色字符串转换为RGB4个颜色分量（透明、红、绿、蓝），适用于颜色格式转换、颜色值标准化等场景。

### 接口名称

```
Hex2RGB
```

### DLL调用

```
int Hex2RGB(long ola,string hex, int* r, int* g, int* b)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hex` (字符串):16进制颜色值

- `r` (整型数指针): 返回红色分量值，范围0-255

- `g` (整型数指针): 返回绿色分量值，范围0-255

- `b` (整型数指针): 返回蓝色分量值，范围0-255

#### 示例:

### 返回值

整型数: - 0: 失败 - 1: 成功

---

# RGB颜色转为16进制格式 -
ARGB2Hex

### 函数简介

将ARGB颜色值转换为16进制格式的字符串。此函数将ARGB4个颜色分量（透明、红、绿、蓝）转换为标准的”AARRGGBB”格式的十六进制颜色字符串，适用于颜色格式转换、颜色值标准化等场景。

### 接口名称

```
ARGB2Hex
```

### DLL调用

```
long ARGB2Hex(long ola, int a, int r, int g, int b)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `a` (整型数): 透明通道值，范围0-255 0为完全透明
255为完全不透明

- `r` (整型数): 红色分量值，范围0-255

- `g` (整型数): 绿色分量值，范围0-255

- `b` (整型数): 蓝色分量值，范围0-255

#### 示例:

```
[](#cb3-1)// 转换RGB颜色为16进制格式
[](#cb3-2)long colorPtr = ARGB2Hex(ola, 255, 255, 0, 0);  // 红色
[](#cb3-3)if (colorPtr != 0) {
[](#cb3-4)    string color = GetStringFromPtr(colorPtr);
[](#cb3-5)    printf("红色转换为16进制: %s\n", color.c_str());  // 输出: ff0000
[](#cb3-6)
[](#cb3-7)    // 释放字符串内存
[](#cb3-8)    FreeStringPtr(ola, colorPtr);
[](#cb3-9)}
[](#cb3-10)
[](#cb3-11)// 转换其他颜色
[](#cb3-12)colorPtr = ARGB2Hex(ola,255, 0, 255, 0);  // 绿色
[](#cb3-13)if (colorPtr != 0) {
[](#cb3-14)    string color = GetStringFromPtr(colorPtr);
[](#cb3-15)    printf("绿色转换为16进制: %s\n", color.c_str());  // 输出: 00ff00
[](#cb3-16)    FreeStringPtr(ola, colorPtr);
[](#cb3-17)}
```

### 返回值

字符串: 返回转换后的16进制颜色字符串，格式为”RRGGBB”（小写）。例如：
- RGB(255,255, 0, 0) 返回 “ffff0000” - RGB(255,0, 255, 0) 返回
“ff00ff00” - RGB(255,0, 0, 255) 返回 “ff0000ff”

### 注意事项

- ARGB分量值必须在0-255范围内

- 返回的16进制字符串为小写

- DLL调用时，返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

- 建议在使用前检查ARGB分量值的有效性

- 返回的字符串可以直接用于其他需要16进制颜色格式的函数

- 颜色值可用于后续的颜色匹配和比较操作

- 建议在循环中转换颜色时注意内存管理

- 转换结果可用于图像处理、界面显示等场景

---

# Canny边缘检测 - CannyEdge

## 函数简介

使用 Canny 算法对图像进行边缘检测。

## 接口名称

```
CannyEdge
```

## DLL调用

```
int64_t CannyEdge(int64_t instance, int64_t ptr, int32_t kernelSize);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针。 |
|

|
kernelSize |
整数型 |
高斯平滑核大小（奇数），用于预处理降噪。 |
|

### 示例

```
[](#cb3-1)long image = LoadImage(ola, "D:/test/img.png");
[](#cb3-2)if (image) {
[](#cb3-3)    long edge = CannyEdge(ola, image, 3);
[](#cb3-4)    if (edge) {
[](#cb3-5)        ShowImage(ola, edge);
[](#cb3-6)        FreeImagePtr(ola, edge);
[](#cb3-7)    }
[](#cb3-8)    FreeImagePtr(ola, image);
[](#cb3-9)}
```

## 返回值

返回边缘图像句柄，失败返回0。

## 注意事项

- 输入图像会进行高斯预处理以降低噪声。

- 处理后的图像需调用 `FreeImagePtr` 释放。

---

# RGB转HSV - RGB2HSV

## 函数简介

将RGB颜色值转换为HSV颜色格式。此函数可以将RGB颜色空间的三个分量（红、绿、蓝）转换为HSV颜色空间的表示形式。HSV颜色空间更适合进行颜色分析和处理，适用于颜色识别、图像处理等场景。返回格式(H,S,V)

## 接口名称

```
RGB2HSV
```

## DLL调用

```
long RGB2HSV(long instance, int r, int g, int b)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
r |
整数型 |
红色分量值，范围0-255 |
|

|
g |
整数型 |
绿色分量值，范围0-255 |
|

|
b |
整数型 |
蓝色分量值，范围0-255 |
|

### 示例

```
[](#cb3-1)// 基本颜色转换
[](#cb3-2)long hsvRed = RGB2HSV(ola, 255, 0, 0);
[](#cb3-3)if (hsvRed != 0) {
[](#cb3-4)    char* hsvStr = (char*)hsvRed;
[](#cb3-5)    printf("红色HSV值: %s\n", hsvStr);
[](#cb3-6)    free(hsvStr);
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 绿色转换
[](#cb3-10)long hsvGreen = RGB2HSV(ola, 0, 255, 0);
[](#cb3-11)if (hsvGreen != 0) {
[](#cb3-12)    char* hsvStr = (char*)hsvGreen;
[](#cb3-13)    printf("绿色HSV值: %s\n", hsvStr);
[](#cb3-14)    free(hsvStr);
[](#cb3-15)}
[](#cb3-16)
[](#cb3-17)// 蓝色转换
[](#cb3-18)long hsvBlue = RGB2HSV(ola, 0, 0, 255);
[](#cb3-19)if (hsvBlue != 0) {
[](#cb3-20)    char* hsvStr = (char*)hsvBlue;
[](#cb3-21)    printf("蓝色HSV值: %s\n", hsvStr);
[](#cb3-22)    free(hsvStr);
[](#cb3-23)}
[](#cb3-24)
[](#cb3-25)// 黄色转换
[](#cb3-26)long hsvYellow = RGB2HSV(ola, 255, 255, 0);
[](#cb3-27)if (hsvYellow != 0) {
[](#cb3-28)    char* hsvStr = (char*)hsvYellow;
[](#cb3-29)    printf("黄色HSV值: %s\n", hsvStr);
[](#cb3-30)    free(hsvStr);
[](#cb3-31)}
[](#cb3-32)
[](#cb3-33)// 常见颜色转换示例
[](#cb3-34)int colors[][3] = {
[](#cb3-35)    {255, 0, 0},    // 红色
[](#cb3-36)    {0, 255, 0},    // 绿色
[](#cb3-37)    {0, 0, 255},    // 蓝色
[](#cb3-38)    {255, 255, 0},  // 黄色
[](#cb3-39)    {255, 0, 255},  // 洋红
[](#cb3-40)    {0, 255, 255},  // 青色
[](#cb3-41)    {255, 255, 255}, // 白色
[](#cb3-42)    {0, 0, 0}       // 黑色
[](#cb3-43)};
[](#cb3-44)
[](#cb3-45)char* colorNames[] = {"红色", "绿色", "蓝色", "黄色", "洋红", "青色", "白色", "黑色"};
[](#cb3-46)
[](#cb3-47)for (int i = 0; i < 8; i++) {
[](#cb3-48)    long hsvColor = RGB2HSV(ola, colors[i][0], colors[i][1], colors[i][2]);
[](#cb3-49)    if (hsvColor != 0) {
[](#cb3-50)        char* hsvStr = (char*)hsvColor;
[](#cb3-51)        printf("%s (%d,%d,%d) -> HSV: %s\n", colorNames[i], colors[i][0], colors[i][1], colors[i][2], hsvStr);
[](#cb3-52)        free(hsvStr);
[](#cb3-53)    }
[](#cb3-54)}
[](#cb3-55)
[](#cb3-56)// 与Hex2HSV函数对比
[](#cb3-57)long hsvFromRGB = RGB2HSV(ola, 255, 0, 0);
[](#cb3-58)long hsvFromHex = Hex2HSV(ola, "#FF0000");
[](#cb3-59)
[](#cb3-60)if (hsvFromRGB != 0 && hsvFromHex != 0) {
[](#cb3-61)    char* rgbStr = (char*)hsvFromRGB;
[](#cb3-62)    char* hexStr = (char*)hsvFromHex;
[](#cb3-63)    printf("RGB2HSV结果: %s\n", rgbStr);
[](#cb3-64)    printf("Hex2HSV结果: %s\n", hexStr);
[](#cb3-65)    free(rgbStr);
[](#cb3-66)    free(hexStr);
[](#cb3-67)}
[](#cb3-68)
[](#cb3-69)// 颜色范围转换示例
[](#cb3-70)for (int r = 0; r <= 255; r += 64) {
[](#cb3-71)    for (int g = 0; g <= 255; g += 64) {
[](#cb3-72)        for (int b = 0; b <= 255; b += 64) {
[](#cb3-73)            long hsvColor = RGB2HSV(ola, r, g, b);
[](#cb3-74)            if (hsvColor != 0) {
[](#cb3-75)                char* hsvStr = (char*)hsvColor;
[](#cb3-76)                printf("RGB(%d,%d,%d) -> HSV: %s\n", r, g, b, hsvStr);
[](#cb3-77)                free(hsvStr);
[](#cb3-78)            }
[](#cb3-79)        }
[](#cb3-80)    }
[](#cb3-81)}
```

## 返回值

int64_t: 返回HSV颜色字符串指针，需要手动释放内存

## 注意事项

- RGB分量值范围均为0-255

- 返回的HSV字符串需要手动释放内存

- HSV颜色空间更适合进行颜色分析和处理

- 与 [Hex2HSV](/图像处理/十六进制转HSV%20-%20Hex2HSV.html)
函数功能相同，但输入格式不同

- 适用于颜色识别、图像处理、颜色分析等场景

- HSV格式便于进行颜色范围匹配和颜色过滤

- 建议在颜色处理流程中使用HSV颜色空间

- RGB到HSV的转换是标准的颜色空间转换算法

---

# RGB颜色转为16进制格式
- GetColorHex(已弃用)

### 函数简介

将RGB颜色值转换为16进制格式的字符串。此函数将RGB三个颜色分量（红、绿、蓝）转换为标准的”RRGGBB”格式的十六进制颜色字符串，适用于颜色格式转换、颜色值标准化等场景。

### 接口名称

```
GetColorHex
```

### DLL调用

```
long GetColorHex(long ola, int r, int g, int b)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `r` (整型数): 红色分量值，范围0-255

- `g` (整型数): 绿色分量值，范围0-255

- `b` (整型数): 蓝色分量值，范围0-255

#### 示例:

```
[](#cb3-1)// 转换RGB颜色为16进制格式
[](#cb3-2)long colorPtr = GetColorHex(ola, 255, 0, 0);  // 红色
[](#cb3-3)if (colorPtr != 0) {
[](#cb3-4)    string color = GetStringFromPtr(colorPtr);
[](#cb3-5)    printf("红色转换为16进制: %s\n", color.c_str());  // 输出: ff0000
[](#cb3-6)
[](#cb3-7)    // 释放字符串内存
[](#cb3-8)    FreeStringPtr(ola, colorPtr);
[](#cb3-9)}
[](#cb3-10)
[](#cb3-11)// 转换其他颜色
[](#cb3-12)colorPtr = GetColorHex(ola, 0, 255, 0);  // 绿色
[](#cb3-13)if (colorPtr != 0) {
[](#cb3-14)    string color = GetStringFromPtr(colorPtr);
[](#cb3-15)    printf("绿色转换为16进制: %s\n", color.c_str());  // 输出: 00ff00
[](#cb3-16)    FreeStringPtr(ola, colorPtr);
[](#cb3-17)}
```

### 返回值

字符串: 返回转换后的16进制颜色字符串，格式为”RRGGBB”（小写）。例如：
- RGB(255, 0, 0) 返回 “ff0000” - RGB(0, 255, 0) 返回 “00ff00” - RGB(0,
0, 255) 返回 “0000ff”

### 注意事项

- RGB分量值必须在0-255范围内

- 返回的16进制字符串为小写

- DLL调用时，返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

- 颜色值不包含透明度信息

- 建议在使用前检查RGB分量值的有效性

- 返回的字符串可以直接用于其他需要16进制颜色格式的函数

- 如果需要带透明度的颜色值，请使用其他相关函数

- 颜色值可用于后续的颜色匹配和比较操作

- 建议在循环中转换颜色时注意内存管理

- 转换结果可用于图像处理、界面显示等场景

---

# RGB颜色转为16进制格式 -
RGB2Hex

### 函数简介

将RGB颜色值转换为16进制格式的字符串。此函数将RGB三个颜色分量（红、绿、蓝）转换为标准的”RRGGBB”格式的十六进制颜色字符串，适用于颜色格式转换、颜色值标准化等场景。

### 接口名称

```
RGB2Hex
```

### DLL调用

```
long RGB2Hex(long ola, int r, int g, int b)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `r` (整型数): 红色分量值，范围0-255

- `g` (整型数): 绿色分量值，范围0-255

- `b` (整型数): 蓝色分量值，范围0-255

#### 示例:

```
[](#cb3-1)// 转换RGB颜色为16进制格式
[](#cb3-2)long colorPtr = RGB2Hex(ola, 255, 0, 0);  // 红色
[](#cb3-3)if (colorPtr != 0) {
[](#cb3-4)    string color = GetStringFromPtr(colorPtr);
[](#cb3-5)    printf("红色转换为16进制: %s\n", color.c_str());  // 输出: ff0000
[](#cb3-6)
[](#cb3-7)    // 释放字符串内存
[](#cb3-8)    FreeStringPtr(ola, colorPtr);
[](#cb3-9)}
[](#cb3-10)
[](#cb3-11)// 转换其他颜色
[](#cb3-12)colorPtr = RGB2Hex(ola, 0, 255, 0);  // 绿色
[](#cb3-13)if (colorPtr != 0) {
[](#cb3-14)    string color = GetStringFromPtr(colorPtr);
[](#cb3-15)    printf("绿色转换为16进制: %s\n", color.c_str());  // 输出: 00ff00
[](#cb3-16)    FreeStringPtr(ola, colorPtr);
[](#cb3-17)}
```

### 返回值

字符串: 返回转换后的16进制颜色字符串，格式为”RRGGBB”（小写）。例如：
- RGB(255, 0, 0) 返回 “ff0000” - RGB(0, 255, 0) 返回 “00ff00” - RGB(0,
0, 255) 返回 “0000ff”

### 注意事项

- RGB分量值必须在0-255范围内

- 返回的16进制字符串为小写

- DLL调用时，返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

- 颜色值不包含透明度信息

- 建议在使用前检查RGB分量值的有效性

- 返回的字符串可以直接用于其他需要16进制颜色格式的函数

- 如果需要带透明度的颜色值，请使用其他相关函数

- 颜色值可用于后续的颜色匹配和比较操作

- 建议在循环中转换颜色时注意内存管理

- 转换结果可用于图像处理、界面显示等场景

---

# base64字符串转为图片 -
Base64ToImage

### 函数简介

将Base64编码的图片数据转换为图片对象。此函数可以将Base64格式的图片数据直接转换为内存中的图片对象，常用于网络传输的图片数据处理、剪贴板图片数据处理等场景。支持常见的图片格式如PNG、JPG、BMP等。

### 接口名称

```
Base64ToImage
```

### DLL调用

```
long Base64ToImage(long ola, string base64_str)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `base64_str` (字符串):
Base64编码的图片数据字符串，支持常见的图片格式如PNG、JPG、BMP等。

#### 示例:

```
[](#cb3-1)// 将Base64字符串转换为图片
[](#cb3-2)const char* base64_data = "iVBORw0KGgoAAAANSUhEUgAA..."; // Base64图片数据
[](#cb3-3)long image = Base64ToImage(ola, base64_data);
[](#cb3-4)if (image != 0) {
[](#cb3-5)    printf("Base64数据转换为图片成功，句柄：%ld\n", image);
[](#cb3-6)
[](#cb3-7)    // 获取转换后图片的大小
[](#cb3-8)    int width, height;
[](#cb3-9)    GetImageSize(ola, image, &width, &height);
[](#cb3-10)    printf("图片大小：%d x %d\n", width, height);
[](#cb3-11)
[](#cb3-12)    // 保存为文件
[](#cb3-13)    SaveImageFromPtr(ola, image, "D:\\test\\from_base64.png");
[](#cb3-14)
[](#cb3-15)    // 使用完后释放图片内存
[](#cb3-16)    FreeImagePtr(ola, image);
[](#cb3-17)} else {
[](#cb3-18)    printf("Base64数据转换失败\n");
[](#cb3-19)}
[](#cb3-20)
[](#cb3-21)// 图片转Base64后再转回图片
[](#cb3-22)long src_image = LoadImage(ola, "D:\\test\\sample.png");
[](#cb3-23)if (src_image != 0) {
[](#cb3-24)    // 转换为Base64
[](#cb3-25)    char* base64_str = ImageToBase64(ola, src_image);
[](#cb3-26)    if (base64_str != NULL) {
[](#cb3-27)        // 将Base64转回图片
[](#cb3-28)        long new_image = Base64ToImage(ola, base64_str);
[](#cb3-29)        if (new_image != 0) {
[](#cb3-30)            printf("图片转换来回成功\n");
[](#cb3-31)            FreeImagePtr(ola, new_image);
[](#cb3-32)        }
[](#cb3-33)
[](#cb3-34)        // 释放Base64字符串内存
[](#cb3-35)        FreeStringPtr(base64_str);
[](#cb3-36)    }
[](#cb3-37)
[](#cb3-38)    FreeImagePtr(ola, src_image);
[](#cb3-39)}
```

### 返回值

长整型数: - 0: 转换失败 - 非0: 转换成功，返回图片句柄

### 注意事项

- Base64字符串必须是有效的图片数据编码，否则转换会失败

- 支持的图片格式包括：PNG、JPG、BMP等常见格式

- 转换成功后必须使用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
释放图片内存

- 如果需要将图片转换为Base64字符串，可以使用 [ImageToBase64](/图像处理/图片转为base64字符串%20-%20ImageToBase64.html)
函数

- Base64字符串可能较长，注意内存使用，建议对大图片进行适当压缩后再转换

---

# 从路径拼接图片 -
ImageStitchFromPath

## 函数简介

从目录或通配路径批量读取图片并进行拼接，可返回拼接轨迹数据。

## 接口名称

```
ImageStitchFromPath
```

## DLL调用

```
int64_t ImageStitchFromPath(int64_t instance, char* path, int64_t* trajectory);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
path |
字符串 |
图片目录（如 C:/imgs/）。 |
|

|
trajectory |
长整数指针 |
输出参数，可为0；返回轨迹数据的字符串指针，需使用
`FreeStringPtr` 释放。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t traj = 0;
[](#cb3-3)int64_t result = ImageStitchFromPath(instance, "C:/imgs/", &traj);
[](#cb3-4)if (result) {
[](#cb3-5)    // 使用result
[](#cb3-6)    FreeImagePtr(instance, result);
[](#cb3-7)}
[](#cb3-8)if (traj) {
[](#cb3-9)    FreeStringPtr(traj);
[](#cb3-10)}
[](#cb3-11)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回拼接后的图像句柄，失败返回0。

## 注意事项

- 轨迹数据指针需使用 `FreeStringPtr` 释放。

- 返回的图像需使用 `FreeImagePtr` 释放。

---

# 保存图片 - SaveImageFromPtr

### 函数简介

将内存中的图片保存到指定文件。此函数可以将图片对象保存为常见的图片格式文件（如PNG、JPG、BMP等），保存格式由文件扩展名决定。支持保存透明度信息（PNG格式）和压缩质量设置（JPG格式）。

### 接口名称

```
SaveImageFromPtr
```

### DLL调用

```
int SaveImageFromPtr(long ola, long image_ptr, string file_path)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `image_ptr` (长整型数): 要保存的图片句柄。

- `file_path` (字符串):
保存的目标文件路径，包括文件名和扩展名。支持的格式包括：

.png：支持透明度，无损压缩

- .jpg：不支持透明度，有损压缩

- .bmp：不压缩，文件较大

#### 示例:

```
[](#cb3-1)// 加载图片并另存为不同格式
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\source.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    // 保存为PNG格式（保留透明度）
[](#cb3-5)    int ret = SaveImageFromPtr(ola, image, "D:\\test\\output.png");
[](#cb3-6)    if (ret == 1) {
[](#cb3-7)        printf("PNG格式保存成功\n");
[](#cb3-8)    }
[](#cb3-9)
[](#cb3-10)    // 保存为JPG格式
[](#cb3-11)    ret = SaveImageFromPtr(ola, image, "D:\\test\\output.jpg");
[](#cb3-12)    if (ret == 1) {
[](#cb3-13)        printf("JPG格式保存成功\n");
[](#cb3-14)    }
[](#cb3-15)
[](#cb3-16)    // 保存为BMP格式
[](#cb3-17)    ret = SaveImageFromPtr(ola, image, "D:\\test\\output.bmp");
[](#cb3-18)    if (ret == 1) {
[](#cb3-19)        printf("BMP格式保存成功\n");
[](#cb3-20)    }
[](#cb3-21)
[](#cb3-22)    FreeImagePtr(ola, image);
[](#cb3-23)}
[](#cb3-24)
[](#cb3-25)// 创建新图片并保存
[](#cb3-26)long new_image = CreateImage(ola, 200, 200);
[](#cb3-27)if (new_image != 0) {
[](#cb3-28)    // 绘制一些内容
[](#cb3-29)    DrawRectangle(ola, new_image, 50, 50, 150, 150, 0xFF0000);
[](#cb3-30)    DrawCircle(ola, new_image, 100, 100, 30, 0x00FF00);
[](#cb3-31)
[](#cb3-32)    // 保存绘制结果
[](#cb3-33)    if (SaveImageFromPtr(ola, new_image, "D:\\test\\drawing.png") == 1) {
[](#cb3-34)        printf("绘制结果保存成功\n");
[](#cb3-35)    } else {
[](#cb3-36)        printf("保存失败\n");
[](#cb3-37)    }
[](#cb3-38)
[](#cb3-39)    FreeImagePtr(ola, new_image);
[](#cb3-40)}
[](#cb3-41)
[](#cb3-42)// 确保目标目录存在
[](#cb3-43)char save_path[256] = "D:\\test\\screenshots";
[](#cb3-44)_mkdir(save_path);  // 创建目录
[](#cb3-45)
[](#cb3-46)// 保存带时间戳的文件名
[](#cb3-47)time_t now;
[](#cb3-48)time(&now);
[](#cb3-49)struct tm* timeinfo = localtime(&now);
[](#cb3-50)char filename[100];
[](#cb3-51)strftime(filename, sizeof(filename), "screenshot_%Y%m%d_%H%M%S.png", timeinfo);
[](#cb3-52)
[](#cb3-53)char full_path[512];
[](#cb3-54)sprintf(full_path, "%s\\%s", save_path, filename);
[](#cb3-55)
[](#cb3-56)// 保存图片
[](#cb3-57)long screen = GetScreenDataPtr(ola, 0, 0, 1920, 1080);
[](#cb3-58)if (screen != 0) {
[](#cb3-59)    if (SaveImageFromPtr(ola, screen, full_path) == 1) {
[](#cb3-60)        printf("截图保存成功：%s\n", full_path);
[](#cb3-61)    }
[](#cb3-62)    FreeImagePtr(ola, screen);
[](#cb3-63)}
```

### 返回值

整型数: - 0: 保存失败 - 1: 保存成功

### 注意事项

- 支持的文件格式由文件扩展名决定，常用格式包括：

.png：支持透明度，无损压缩

- .jpg：不支持透明度，有损压缩

- .bmp：不压缩，文件较大

- 保存前请确保目标目录存在且有写入权限

- 如果目标文件已存在，将被覆盖

- 建议使用绝对路径以避免路径问题

- 对于需要频繁保存的场景（如截图），建议使用时间戳或序号来避免文件名冲突

---

# 创建图片 - CreateImage

### 函数简介

创建一个指定大小的空白图片。此函数用于创建一个新的图片对象，可以指定图片的宽度和高度，创建的图片初始状态为全透明。创建的图片可以用于后续的绘制、像素操作等处理。

### 接口名称

```
CreateImage
```

### DLL调用

```
long CreateImage(long ola, int width, int height)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `width` (整型数): 要创建的图片宽度，单位为像素。

- `height` (整型数): 要创建的图片高度，单位为像素。

#### 示例:

```
[](#cb3-1)// 创建一个800x600的空白图片
[](#cb3-2)long image = CreateImage(ola, 800, 600);
[](#cb3-3)if (image != 0) {
[](#cb3-4)    printf("空白图片创建成功，句柄：%ld\n", image);
[](#cb3-5)
[](#cb3-6)    // 在图片上绘制一个红色矩形
[](#cb3-7)    DrawRectangle(ola, image, 100, 100, 300, 200, 0xFF0000);
[](#cb3-8)
[](#cb3-9)    // 保存图片到文件
[](#cb3-10)    SaveImageFromPtr(ola, image, "D:\\test\\new_image.png");
[](#cb3-11)
[](#cb3-12)    // 使用完后释放图片内存
[](#cb3-13)    FreeImagePtr(ola, image);
[](#cb3-14)} else {
[](#cb3-15)    printf("图片创建失败\n");
[](#cb3-16)}
[](#cb3-17)
[](#cb3-18)// 创建一个与现有图片相同大小的新图片
[](#cb3-19)long src_image = LoadImage(ola, "D:\\test\\sample.png");
[](#cb3-20)if (src_image != 0) {
[](#cb3-21)    int width, height;
[](#cb3-22)    GetImageSize(ola, src_image, &width, &height);
[](#cb3-23)
[](#cb3-24)    // 创建相同大小的新图片
[](#cb3-25)    long new_image = CreateImage(ola, width, height);
[](#cb3-26)    if (new_image != 0) {
[](#cb3-27)        printf("创建了一个 %d x %d 的新图片\n", width, height);
[](#cb3-28)
[](#cb3-29)        // 在这里可以进行图片处理操作
[](#cb3-30)        // ...
[](#cb3-31)
[](#cb3-32)        FreeImagePtr(ola, new_image);
[](#cb3-33)    }
[](#cb3-34)
[](#cb3-35)    FreeImagePtr(ola, src_image);
[](#cb3-36)}
```

### 返回值

长整型数: - 0: 创建失败 - 非0: 创建成功，返回图片句柄

### 注意事项

- 创建的图片初始状态为全透明

- 图片大小不要超过系统内存限制，建议单张图片不超过100MB

- 创建成功后必须使用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
释放图片内存

- 可以使用 [SetPixel](/图像处理/设置图片指定坐标的颜色%20-%20SetPixel.html)
或绘图函数来修改图片内容

- 如果需要创建带初始颜色的图片，可以在创建后使用 [SetColorsToNewColor](/图像处理/设置指定颜色为新的颜色%20-%20SetColorsToNewColor.html)
设置背景色

---

# 创建拼接实例 -
ImageStitchCreate

## 函数简介

创建图像拼接实例，用于逐张追加图片并生成拼接结果。

## 接口名称

```
ImageStitchCreate
```

## DLL调用

```
int64_t ImageStitchCreate(int64_t instance);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t st = ImageStitchCreate(instance);
[](#cb3-3)// ...
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回拼接实例句柄，失败返回0。

## 注意事项

- 使用完成后需调用 `ImageStitchFree` 释放实例。

---

# 加载图片 - LoadImage

### 函数简介

加载一张图片到内存,如果SetConfig配置了数据库连接则优先读取数据库内图片信息,如果数据库没有找到图片或者没有配置数据库,则从工作目录下读取指定文件。

### 接口名称

```
LoadImage
```

### DLL调用

```
long LoadImage(long ola, string file_path)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `file_path` (字符串):
图片文件的完整路径。支持相对路径和绝对路径。

#### 示例:

```
[](#cb3-1)// 加载本地图片文件
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\sample.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    printf("图片加载成功，句柄：%ld\n", image);
[](#cb3-5)
[](#cb3-6)    // 获取图片大小
[](#cb3-7)    int width, height;
[](#cb3-8)    GetImageSize(ola, image, &width, &height);
[](#cb3-9)    printf("图片大小：%d x %d\n", width, height);
[](#cb3-10)
[](#cb3-11)    // 使用完后释放图片内存
[](#cb3-12)    FreeImagePtr(ola, image);
[](#cb3-13)} else {
[](#cb3-14)    printf("图片加载失败\n");
[](#cb3-15)}
[](#cb3-16)
[](#cb3-17)// 加载相对路径的图片
[](#cb3-18)image = LoadImage(ola, ".\\images\\button.jpg");
[](#cb3-19)if (image != 0) {
[](#cb3-20)    printf("按钮图片加载成功\n");
[](#cb3-21)
[](#cb3-22)    // 在屏幕上查找该图片
[](#cb3-23)    int x = 0, y = 0;
[](#cb3-24)    if (FindPic(ola, 0, 0, 1920, 1080, image, &x, &y) == 1) {
[](#cb3-25)        printf("找到按钮位置：(%d, %d)\n", x, y);
[](#cb3-26)    }
[](#cb3-27)
[](#cb3-28)    FreeImagePtr(ola, image);
[](#cb3-29)}
```

### 返回值

长整型数: - 0: 加载失败 - 非0: 加载成功，返回OLAImage对象的地址

### 注意事项

- 支持的图片格式包括：BMP、JPG、PNG

- 加载成功后必须使用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
释放图片内存，否则会造成内存泄漏

- 建议使用绝对路径以避免路径问题，如果使用相对路径，需要确保当前工作目录正确

---

# 加载图片 -
LoadImageFromRGBData

### 函数简介

从RGB数据加载图片到内存。此函数支持从采集卡或其他RGB数据源直接加载图片，适用于需要处理实时图像数据的场景，如视频采集、图像处理等。

### 接口名称

```
LoadImageFromRGBData
```

### DLL调用

```
long LoadImageFromRGBData(long ola, int width, int height, long rgbdata, int stride)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `width` (整型数): 图片宽度，单位像素

- `height` (整型数): 图片高度，单位像素

- `rgbdata` (长整型数): RGB图片数据的地址

- `stride` (整型数): RGB图片数据的行跨度（每行字节数）

#### 示例:

```
[](#cb3-1)// 从采集卡数据加载图片
[](#cb3-2)int width = 1920;  // 图片宽度
[](#cb3-3)int height = 1080; // 图片高度
[](#cb3-4)long rgbData = GetCaptureCardData(); // 获取采集卡数据地址
[](#cb3-5)int stride = width * 3; // RGB格式，每像素3字节
[](#cb3-6)
[](#cb3-7)long imagePtr = LoadImageFromRGBData(ola, width, height, rgbData, stride);
[](#cb3-8)if (imagePtr != 0) {
[](#cb3-9)    // 使用加载的图片
[](#cb3-10)    // ...
[](#cb3-11)
[](#cb3-12)    // 使用完后释放内存
[](#cb3-13)    FreeImagePtr(ola, imagePtr);
[](#cb3-14)}
```

### 返回值

长整型数: 返回加载的OLAImage对象的地址。如果失败返回0。

### 注意事项

- RGB数据必须是有效的内存地址，否则可能导致程序崩溃

- 图片尺寸必须与实际数据匹配，否则可能导致图片显示异常

- stride参数必须正确设置，通常为width * 3（RGB格式）

- 图片使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口释放内存

- 确保RGB数据在图片使用期间保持有效

- 建议在加载大图片时注意内存使用

- 如果数据源是采集卡，请确保采集卡驱动正常工作

- RGB数据格式必须为24位真彩色（每像素3字节）

- 图片加载失败时返回0，请检查参数是否正确

- 建议在使用前验证RGB数据的有效性

---

# 加载文件夹下的所有图片
- LoadImagePath(已弃用)

### 函数简介

将指定文件夹下的所有图片加载到内存。此函数会递归遍历指定文件夹，加载所有支持的图片格式文件。由于此函数已被弃用，建议使用其他图片加载方式。

### 接口名称

```
LoadImagePath
```

### DLL调用

```
int LoadImagePath(long ola, string path)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `path` (字符串):
图片文件夹的路径，支持相对路径和绝对路径

#### 示例:

```
[](#cb3-1)// 加载指定文件夹下的所有图片
[](#cb3-2)string imagePath = "/OLA/pic/";
[](#cb3-3)int result = LoadImagePath(ola, imagePath);
[](#cb3-4)if (result == 1) {
[](#cb3-5)    printf("图片加载成功\n");
[](#cb3-6)} else {
[](#cb3-7)    printf("图片加载失败\n");
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)// 使用绝对路径加载图片
[](#cb3-11)string absPath = "D:/images/";
[](#cb3-12)int result = LoadImagePath(ola, absPath);
[](#cb3-13)if (result == 1) {
[](#cb3-14)    printf("图片加载成功\n");
[](#cb3-15)} else {
[](#cb3-16)    printf("图片加载失败\n");
[](#cb3-17)}
```

### 返回值

整型数: - 0: 加载失败 - 1: 加载成功

### 注意事项

- 此函数已被弃用，建议使用其他图片加载方式

- 路径可以是相对路径或绝对路径

- 函数会递归遍历指定文件夹下的所有子文件夹

- 支持的图片格式包括：BMP、JPG、PNG等常见格式

- 如果文件夹不存在，函数将返回失败

- 如果文件夹中没有支持的图片格式，函数将返回成功但不会加载任何图片

- 加载大量图片时需要注意内存使用

- 建议在使用前检查文件夹路径的有效性

- 路径中不要包含特殊字符

- 建议使用正斜杠(/)作为路径分隔符

---

# 十六进制转HSV - Hex2HSV

## 函数简介

将十六进制颜色值转换为HSV颜色格式。此函数可以将标准的十六进制颜色字符串（如”#FF0000”）转换为HSV颜色空间的表示形式。HSV颜色空间更适合进行颜色分析和处理，适用于颜色识别、图像处理等场景。返回格式(H,S,V)

## 接口名称

```
Hex2HSV
```

## DLL调用

```
long Hex2HSV(long instance, string hex)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hex |
字符串 |
十六进制颜色字符串，格式为”#RRGGBB”或”RRGGBB” |
|

### 示例

```
[](#cb3-1)// 基本颜色转换
[](#cb3-2)long hsvRed = Hex2HSV(ola, "#FF0000");
[](#cb3-3)if (hsvRed != 0) {
[](#cb3-4)    char* hsvStr = (char*)hsvRed;
[](#cb3-5)    printf("红色HSV值: %s\n", hsvStr);
[](#cb3-6)    free(hsvStr);
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 绿色转换
[](#cb3-10)long hsvGreen = Hex2HSV(ola, "#00FF00");
[](#cb3-11)if (hsvGreen != 0) {
[](#cb3-12)    char* hsvStr = (char*)hsvGreen;
[](#cb3-13)    printf("绿色HSV值: %s\n", hsvStr);
[](#cb3-14)    free(hsvStr);
[](#cb3-15)}
[](#cb3-16)
[](#cb3-17)// 蓝色转换
[](#cb3-18)long hsvBlue = Hex2HSV(ola, "#0000FF");
[](#cb3-19)if (hsvBlue != 0) {
[](#cb3-20)    char* hsvStr = (char*)hsvBlue;
[](#cb3-21)    printf("蓝色HSV值: %s\n", hsvStr);
[](#cb3-22)    free(hsvStr);
[](#cb3-23)}
[](#cb3-24)
[](#cb3-25)// 不带#号的十六进制颜色
[](#cb3-26)long hsvYellow = Hex2HSV(ola, "FFFF00");
[](#cb3-27)if (hsvYellow != 0) {
[](#cb3-28)    char* hsvStr = (char*)hsvYellow;
[](#cb3-29)    printf("黄色HSV值: %s\n", hsvStr);
[](#cb3-30)    free(hsvStr);
[](#cb3-31)}
[](#cb3-32)
[](#cb3-33)// 常见颜色转换示例
[](#cb3-34)char* colors[] = {"#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#FFFFFF", "#000000"};
[](#cb3-35)char* colorNames[] = {"红色", "绿色", "蓝色", "黄色", "洋红", "青色", "白色", "黑色"};
[](#cb3-36)
[](#cb3-37)for (int i = 0; i < 8; i++) {
[](#cb3-38)    long hsvColor = Hex2HSV(ola, colors[i]);
[](#cb3-39)    if (hsvColor != 0) {
[](#cb3-40)        char* hsvStr = (char*)hsvColor;
[](#cb3-41)        printf("%s (%s) -> HSV: %s\n", colorNames[i], colors[i], hsvStr);
[](#cb3-42)        free(hsvStr);
[](#cb3-43)    }
[](#cb3-44)}
[](#cb3-45)
[](#cb3-46)// 与RGB2HSV函数对比
[](#cb3-47)long hsvFromHex = Hex2HSV(ola, "#FF0000");
[](#cb3-48)long hsvFromRGB = RGB2HSV(ola, 255, 0, 0);
[](#cb3-49)
[](#cb3-50)if (hsvFromHex != 0 && hsvFromRGB != 0) {
[](#cb3-51)    char* hexStr = (char*)hsvFromHex;
[](#cb3-52)    char* rgbStr = (char*)hsvFromRGB;
[](#cb3-53)    printf("Hex2HSV结果: %s\n", hexStr);
[](#cb3-54)    printf("RGB2HSV结果: %s\n", rgbStr);
[](#cb3-55)    free(hexStr);
[](#cb3-56)    free(rgbStr);
[](#cb3-57)}
```

## 返回值

int64_t: 返回HSV颜色字符串指针，需要手动释放内存

## 注意事项

- 输入的十六进制颜色格式支持”#RRGGBB”或”RRGGBB”两种格式

- 返回的HSV字符串需要手动释放内存

- HSV颜色空间更适合进行颜色分析和处理

- 与 [RGB2HSV](/图像处理/RGB转HSV%20-%20RGB2HSV.html)
函数功能相同，但输入格式不同

- 适用于颜色识别、图像处理、颜色分析等场景

- HSV格式便于进行颜色范围匹配和颜色过滤

- 建议在颜色处理流程中使用HSV颜色空间

---

# 去除孤岛 - RemoveIslands

## 函数简介

去除图像中的孤岛（小面积连通区域）。此函数可以去除二值化图像中面积小于指定阈值的连通区域，常用于图像去噪、目标检测预处理等场景。适用于清理二值化图像中的噪声点和小面积干扰。

## 接口名称

```
RemoveIslands
```

## DLL调用

```
long RemoveIslands(long instance, long ptr, int minArea)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针，由图像处理函数返回 |
|

|
minArea |
整数型 |
最小面积阈值，小于此面积的连通区域将被去除 |
|

### 示例

```
[](#cb3-1)// 基本孤岛去除
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\noisy.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    // 转换为灰度图
[](#cb3-5)    long grayImage = ConvertColor(ola, image, 0);
[](#cb3-6)    if (grayImage != 0) {
[](#cb3-7)        // 二值化处理
[](#cb3-8)        long binaryImage = Threshold(ola, grayImage, 128.0, 255.0, 0);
[](#cb3-9)        if (binaryImage != 0) {
[](#cb3-10)            // 去除小面积孤岛
[](#cb3-11)            long cleanedImage = RemoveIslands(ola, binaryImage, 100);
[](#cb3-12)            if (cleanedImage != 0) {
[](#cb3-13)                printf("已去除面积小于100像素的孤岛\n");
[](#cb3-14)                ShowImage(ola, cleanedImage);
[](#cb3-15)                FreeImagePtr(ola, cleanedImage);
[](#cb3-16)            }
[](#cb3-17)            FreeImagePtr(ola, binaryImage);
[](#cb3-18)        }
[](#cb3-19)        FreeImagePtr(ola, grayImage);
[](#cb3-20)    }
[](#cb3-21)    FreeImagePtr(ola, image);
[](#cb3-22)}
[](#cb3-23)
[](#cb3-24)// 屏幕截图去噪处理
[](#cb3-25)long screen = GetScreenDataPtr(ola, 0, 0, 1920, 1080);
[](#cb3-26)if (screen != 0) {
[](#cb3-27)    // 转换为灰度
[](#cb3-28)    long grayScreen = ConvertColor(ola, screen, 0);
[](#cb3-29)    if (grayScreen != 0) {
[](#cb3-30)        // OTSU阈值化
[](#cb3-31)        long binaryScreen = Threshold(ola, grayScreen, 0.0, 255.0, 5);
[](#cb3-32)        if (binaryScreen != 0) {
[](#cb3-33)            // 去除小面积噪声
[](#cb3-34)            long cleanedScreen = RemoveIslands(ola, binaryScreen, 50);
[](#cb3-35)            if (cleanedScreen != 0) {
[](#cb3-36)                printf("屏幕截图已去除小面积噪声\n");
[](#cb3-37)                FreeImagePtr(ola, cleanedScreen);
[](#cb3-38)            }
[](#cb3-39)            FreeImagePtr(ola, binaryScreen);
[](#cb3-40)        }
[](#cb3-41)        FreeImagePtr(ola, grayScreen);
[](#cb3-42)    }
[](#cb3-43)    FreeImagePtr(ola, screen);
[](#cb3-44)}
[](#cb3-45)
[](#cb3-46)// 不同面积阈值的对比
[](#cb3-47)long image = LoadImage(ola, "D:\\test\\image.png");
[](#cb3-48)if (image != 0) {
[](#cb3-49)    long grayImage = ConvertColor(ola, image, 0);
[](#cb3-50)    if (grayImage != 0) {
[](#cb3-51)        long binaryImage = Threshold(ola, grayImage, 128.0, 255.0, 0);
[](#cb3-52)        if (binaryImage != 0) {
[](#cb3-53)            // 不同面积阈值处理
[](#cb3-54)            long cleaned10 = RemoveIslands(ola, binaryImage, 10);
[](#cb3-55)            long cleaned50 = RemoveIslands(ola, binaryImage, 50);
[](#cb3-56)            long cleaned100 = RemoveIslands(ola, binaryImage, 100);
[](#cb3-57)
[](#cb3-58)            printf("不同面积阈值处理完成\n");
[](#cb3-59)
[](#cb3-60)            // 释放内存
[](#cb3-61)            if (cleaned10 != 0) FreeImagePtr(ola, cleaned10);
[](#cb3-62)            if (cleaned50 != 0) FreeImagePtr(ola, cleaned50);
[](#cb3-63)            if (cleaned100 != 0) FreeImagePtr(ola, cleaned100);
[](#cb3-64)
[](#cb3-65)            FreeImagePtr(ola, binaryImage);
[](#cb3-66)        }
[](#cb3-67)        FreeImagePtr(ola, grayImage);
[](#cb3-68)    }
[](#cb3-69)    FreeImagePtr(ola, image);
[](#cb3-70)}
[](#cb3-71)
[](#cb3-72)// 图像处理流程示例
[](#cb3-73)long image = LoadImage(ola, "D:\\test\\target.png");
[](#cb3-74)if (image != 0) {
[](#cb3-75)    // 转换为灰度
[](#cb3-76)    long grayImage = ConvertColor(ola, image, 0);
[](#cb3-77)    if (grayImage != 0) {
[](#cb3-78)        // 阈值化
[](#cb3-79)        long binaryImage = Threshold(ola, grayImage, 128.0, 255.0, 0);
[](#cb3-80)        if (binaryImage != 0) {
[](#cb3-81)            // 去除小面积孤岛
[](#cb3-82)            long cleanedImage = RemoveIslands(ola, binaryImage, 100);
[](#cb3-83)            if (cleanedImage != 0) {
[](#cb3-84)                // 形态学梯度
[](#cb3-85)                long gradientImage = MorphGradient(ola, cleanedImage, 3);
[](#cb3-86)                if (gradientImage != 0) {
[](#cb3-87)                    printf("图像处理流程完成\n");
[](#cb3-88)                    FreeImagePtr(ola, gradientImage);
[](#cb3-89)                }
[](#cb3-90)                FreeImagePtr(ola, cleanedImage);
[](#cb3-91)            }
[](#cb3-92)            FreeImagePtr(ola, binaryImage);
[](#cb3-93)        }
[](#cb3-94)        FreeImagePtr(ola, grayImage);
[](#cb3-95)    }
[](#cb3-96)    FreeImagePtr(ola, image);
[](#cb3-97)}
```

## 返回值

int64_t: 返回处理后的图像指针

## 注意事项

- 此函数主要适用于二值化图像

- minArea参数决定了保留的连通区域的最小面积

- 面积小于minArea的连通区域将被完全去除

- 建议在阈值化处理后使用此函数

- 处理后的图像需要手动释放内存

- 与 [Threshold](/图像处理/图像阈值化%20-%20Threshold.html)
函数配合使用效果更佳

- 适用于图像去噪、目标检测预处理、OCR图像清理等场景

- 面积阈值的选择需要根据具体应用场景调整

---

# 取色 - GetColor

### 函数简介

获取指定坐标点(x,
y)的颜色值。此函数可以获取窗口上指定位置的颜色，返回格式为”AARRGGBB”的十六进制颜色字符串。适用于颜色检测、图像分析等场景。

### 接口名称

```
GetColor
```

### DLL调用

```
long GetColor(long ola, int x, int y)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x` (整型数): 要获取颜色的X坐标

- `y` (整型数): 要获取颜色的Y坐标

#### 示例:

```
[](#cb3-1)// 获取指定坐标的颜色
[](#cb3-2)long colorPtr = GetColor(ola, 100, 100);
[](#cb3-3)if (colorPtr != 0) {
[](#cb3-4)    // 获取颜色字符串
[](#cb3-5)    string color = GetStringFromPtr(colorPtr);
[](#cb3-6)    printf("坐标(100, 100)的颜色为：%s\n", color.c_str());
[](#cb3-7)
[](#cb3-8)    // 释放字符串内存
[](#cb3-9)    FreeStringPtr(ola, colorPtr);
[](#cb3-10)} else {
[](#cb3-11)    printf("获取颜色失败\n");
[](#cb3-12)}
[](#cb3-13)
[](#cb3-14)// 检查特定颜色
[](#cb3-15)long colorPtr = GetColor(ola, 30, 30);
[](#cb3-16)if (colorPtr != 0) {
[](#cb3-17)    string color = GetStringFromPtr(colorPtr);
[](#cb3-18)    if (color == "ffffff") {
[](#cb3-19)        printf("找到白色\n");
[](#cb3-20)    }
[](#cb3-21)    FreeStringPtr(ola, colorPtr);
[](#cb3-22)}
```

### 返回值

字符串:
返回指定坐标点的颜色值，格式为”RRGGBB”的十六进制字符串（小写）。如果获取失败返回空字符串。

### 注意事项

- 坐标必须在有效范围内，否则可能导致程序异常

- 返回的颜色字符串为小写，便于与工具匹配

- DLL调用时，返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

- 颜色格式为6位十六进制数，如”ffffff”表示白色

- 建议在使用前检查坐标是否有效

- 如果坐标超出屏幕范围，将返回空字符串

- 颜色值不包含透明度信息

- 建议在循环中获取颜色时注意内存管理

- 颜色值可用于后续的颜色匹配和比较操作

- 如果需要带透明度的颜色值，请使用其他相关函数

---

# 图像锐化 - Sharpen

## 函数简介

对图像进行锐化处理，增强边缘与细节。

## 接口名称

```
Sharpen
```

## DLL调用

```
int64_t Sharpen(int64_t instance, int64_t ptr);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针。 |
|

### 示例

```
[](#cb3-1)long image = LoadImage(ola, "D:/test/img.png");
[](#cb3-2)if (image) {
[](#cb3-3)    long result = Sharpen(ola, image);
[](#cb3-4)    if (result) {
[](#cb3-5)        FreeImagePtr(ola, result);
[](#cb3-6)    }
[](#cb3-7)    FreeImagePtr(ola, image);
[](#cb3-8)}
```

## 返回值

返回处理后的图像句柄，失败返回0。

## 注意事项

- 锐化可能会放大噪声，建议必要时先进行去噪。

- 处理后的图像需调用 `FreeImagePtr` 释放。

---

# 图像阈值化 - Threshold

## 函数简介

对图像进行阈值化处理。此函数支持多种阈值化方法，包括二值化、反二值化、截断、阈值化、反阈值化、OTSU自动阈值化等。适用于图像分割、目标检测、噪声去除等场景。

## 接口名称

```
Threshold
```

## DLL调用

```
long Threshold(long instance, long ptr, double thresh, double maxVal, int type)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针，由图像处理函数返回 |
|

|
thresh |
双精度浮点数 |
阈值 |
|

|
maxVal |
双精度浮点数 |
最大值 不超过255 |
|

|
type |
整数型 |
阈值化类型：
0: 二值化
1: 反二值化
2: 截断
3:
阈值化
4: 反阈值化
5: 阈值化OTSU
6: 反阈值化OTSU |
|

### 示例

```
[](#cb3-1)// 基本二值化处理
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\image.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    // 转换为灰度图
[](#cb3-5)    long grayImage = ConvertColor(ola, image, 0);
[](#cb3-6)    if (grayImage != 0) {
[](#cb3-7)        // 二值化处理
[](#cb3-8)        long binaryImage = Threshold(ola, grayImage, 128.0, 255.0, 0);
[](#cb3-9)        if (binaryImage != 0) {
[](#cb3-10)            printf("图像已二值化处理\n");
[](#cb3-11)            ShowImage(ola, binaryImage);
[](#cb3-12)            FreeImagePtr(ola, binaryImage);
[](#cb3-13)        }
[](#cb3-14)        FreeImagePtr(ola, grayImage);
[](#cb3-15)    }
[](#cb3-16)    FreeImagePtr(ola, image);
[](#cb3-17)}
[](#cb3-18)
[](#cb3-19)// 反二值化处理
[](#cb3-20)long image = LoadImage(ola, "D:\\test\\image.png");
[](#cb3-21)if (image != 0) {
[](#cb3-22)    long grayImage = ConvertColor(ola, image, 0);
[](#cb3-23)    if (grayImage != 0) {
[](#cb3-24)        // 反二值化
[](#cb3-25)        long invertedBinary = Threshold(ola, grayImage, 128.0, 255.0, 1);
[](#cb3-26)        if (invertedBinary != 0) {
[](#cb3-27)            printf("图像已反二值化处理\n");
[](#cb3-28)            FreeImagePtr(ola, invertedBinary);
[](#cb3-29)        }
[](#cb3-30)        FreeImagePtr(ola, grayImage);
[](#cb3-31)    }
[](#cb3-32)    FreeImagePtr(ola, image);
[](#cb3-33)}
[](#cb3-34)
[](#cb3-35)// 截断处理
[](#cb3-36)long image = LoadImage(ola, "D:\\test\\image.png");
[](#cb3-37)if (image != 0) {
[](#cb3-38)    long grayImage = ConvertColor(ola, image, 0);
[](#cb3-39)    if (grayImage != 0) {
[](#cb3-40)        // 截断处理
[](#cb3-41)        long truncatedImage = Threshold(ola, grayImage, 128.0, 255.0, 2);
[](#cb3-42)        if (truncatedImage != 0) {
[](#cb3-43)            printf("图像已截断处理\n");
[](#cb3-44)            FreeImagePtr(ola, truncatedImage);
[](#cb3-45)        }
[](#cb3-46)        FreeImagePtr(ola, grayImage);
[](#cb3-47)    }
[](#cb3-48)    FreeImagePtr(ola, image);
[](#cb3-49)}
[](#cb3-50)
[](#cb3-51)// OTSU自动阈值化
[](#cb3-52)long image = LoadImage(ola, "D:\\test\\image.png");
[](#cb3-53)if (image != 0) {
[](#cb3-54)    long grayImage = ConvertColor(ola, image, 0);
[](#cb3-55)    if (grayImage != 0) {
[](#cb3-56)        // OTSU自动阈值化（thresh参数会被忽略）
[](#cb3-57)        long otsuImage = Threshold(ola, grayImage, 0.0, 255.0, 5);
[](#cb3-58)        if (otsuImage != 0) {
[](#cb3-59)            printf("图像已OTSU阈值化处理\n");
[](#cb3-60)            FreeImagePtr(ola, otsuImage);
[](#cb3-61)        }
[](#cb3-62)        FreeImagePtr(ola, grayImage);
[](#cb3-63)    }
[](#cb3-64)    FreeImagePtr(ola, image);
[](#cb3-65)}
[](#cb3-66)
[](#cb3-67)// 屏幕截图阈值化处理
[](#cb3-68)long screen = GetScreenDataPtr(ola, 0, 0, 1920, 1080);
[](#cb3-69)if (screen != 0) {
[](#cb3-70)    // 转换为灰度
[](#cb3-71)    long grayScreen = ConvertColor(ola, screen, 0);
[](#cb3-72)    if (grayScreen != 0) {
[](#cb3-73)        // 进行OTSU阈值化
[](#cb3-74)        long binaryScreen = Threshold(ola, grayScreen, 0.0, 255.0, 5);
[](#cb3-75)        if (binaryScreen != 0) {
[](#cb3-76)            printf("屏幕截图已OTSU阈值化处理\n");
[](#cb3-77)            // 可以进一步处理，如去除孤岛
[](#cb3-78)            long cleanedScreen = RemoveIslands(ola, binaryScreen, 100);
[](#cb3-79)            if (cleanedScreen != 0) {
[](#cb3-80)                printf("已去除小面积孤岛\n");
[](#cb3-81)                FreeImagePtr(ola, cleanedScreen);
[](#cb3-82)            }
[](#cb3-83)            FreeImagePtr(ola, binaryScreen);
[](#cb3-84)        }
[](#cb3-85)        FreeImagePtr(ola, grayScreen);
[](#cb3-86)    }
[](#cb3-87)    FreeImagePtr(ola, screen);
[](#cb3-88)}
[](#cb3-89)
[](#cb3-90)// 不同阈值化类型对比
[](#cb3-91)long image = LoadImage(ola, "D:\\test\\image.png");
[](#cb3-92)if (image != 0) {
[](#cb3-93)    long grayImage = ConvertColor(ola, image, 0);
[](#cb3-94)    if (grayImage != 0) {
[](#cb3-95)        // 二值化
[](#cb3-96)        long binary = Threshold(ola, grayImage, 128.0, 255.0, 0);
[](#cb3-97)        // 反二值化
[](#cb3-98)        long inverted = Threshold(ola, grayImage, 128.0, 255.0, 1);
[](#cb3-99)        // 截断
[](#cb3-100)        long truncated = Threshold(ola, grayImage, 128.0, 255.0, 2);
[](#cb3-101)        // OTSU
[](#cb3-102)        long otsu = Threshold(ola, grayImage, 0.0, 255.0, 5);
[](#cb3-103)
[](#cb3-104)        printf("不同阈值化方法处理完成\n");
[](#cb3-105)
[](#cb3-106)        // 释放内存
[](#cb3-107)        if (binary != 0) FreeImagePtr(ola, binary);
[](#cb3-108)        if (inverted != 0) FreeImagePtr(ola, inverted);
[](#cb3-109)        if (truncated != 0) FreeImagePtr(ola, truncated);
[](#cb3-110)        if (otsu != 0) FreeImagePtr(ola, otsu);
[](#cb3-111)
[](#cb3-112)        FreeImagePtr(ola, grayImage);
[](#cb3-113)    }
[](#cb3-114)    FreeImagePtr(ola, image);
[](#cb3-115)}
```

## 返回值

int64_t: 返回处理后的图像指针

## 注意事项

- 阈值化类型说明：

0: 二值化 - 像素值大于阈值设为maxVal，否则设为0

- 1: 反二值化 - 像素值大于阈值设为0，否则设为maxVal

- 2: 截断 - 像素值大于阈值设为阈值，否则保持不变

- 3: 阈值化 - 像素值大于阈值设为maxVal，否则保持不变

- 4: 反阈值化 - 像素值大于阈值保持不变，否则设为maxVal

- 5: 阈值化OTSU - 自动计算最优阈值进行二值化

- 6: 反阈值化OTSU - 自动计算最优阈值进行反二值化

- OTSU方法会自动计算最优阈值，thresh参数会被忽略

- 建议先转换为灰度图像再进行阈值化处理

- 处理后的图像需要手动释放内存

- 与 [RemoveIslands](/图像处理/去除孤岛%20-%20RemoveIslands.html)
函数配合使用可以去除噪声

- 适用于图像分割、目标检测、OCR预处理等场景

---

# 图片转为base64字符串 -
ImageToBase64

### 函数简介

将图片对象转换为Base64编码的字符串。此函数可以将内存中的图片数据编码为Base64格式的字符串，便于网络传输、数据存储或在不同系统间交换图片数据。转换后的Base64字符串可以直接用于HTML的img标签或其他需要Base64图片数据的场景。

### 接口名称

```
ImageToBase64
```

### DLL调用

```
string ImageToBase64(long ola, long image_ptr)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `image_ptr` (长整型数): 要转换的图片句柄。

#### 示例:

```
[](#cb3-1)// 加载图片并转换为Base64字符串
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\sample.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    // 转换为Base64
[](#cb3-5)    char* base64_str = ImageToBase64(ola, image);
[](#cb3-6)    if (base64_str != NULL) {
[](#cb3-7)        printf("图片转换为Base64成功\n");
[](#cb3-8)        printf("Base64字符串前100个字符：%.100s...\n", base64_str);
[](#cb3-9)
[](#cb3-10)        // 可以将base64_str用于其他用途
[](#cb3-11)        // 例如保存到文件
[](#cb3-12)        FILE* fp = fopen("D:\\test\\image.base64", "w");
[](#cb3-13)        if (fp != NULL) {
[](#cb3-14)            fprintf(fp, "%s", base64_str);
[](#cb3-15)            fclose(fp);
[](#cb3-16)        }
[](#cb3-17)
[](#cb3-18)        // 转换回图片测试
[](#cb3-19)        long new_image = Base64ToImage(ola, base64_str);
[](#cb3-20)        if (new_image != 0) {
[](#cb3-21)            printf("Base64字符串转回图片成功\n");
[](#cb3-22)            FreeImagePtr(ola, new_image);
[](#cb3-23)        }
[](#cb3-24)
[](#cb3-25)        // 释放Base64字符串内存
[](#cb3-26)        FreeStringPtr(base64_str);
[](#cb3-27)    } else {
[](#cb3-28)        printf("转换为Base64失败\n");
[](#cb3-29)    }
[](#cb3-30)
[](#cb3-31)    FreeImagePtr(ola, image);
[](#cb3-32)}
[](#cb3-33)
[](#cb3-34)// 创建图片并转换为Base64
[](#cb3-35)long new_image = CreateImage(ola, 100, 100);
[](#cb3-36)if (new_image != 0) {
[](#cb3-37)    // 绘制一些内容
[](#cb3-38)    DrawRectangle(ola, new_image, 10, 10, 90, 90, 0xFF0000);
[](#cb3-39)
[](#cb3-40)    // 转换为Base64
[](#cb3-41)    char* base64_str = ImageToBase64(ola, new_image);
[](#cb3-42)    if (base64_str != NULL) {
[](#cb3-43)        printf("新创建的图片转换为Base64成功\n");
[](#cb3-44)        FreeStringPtr(base64_str);
[](#cb3-45)    }
[](#cb3-46)
[](#cb3-47)    FreeImagePtr(ola, new_image);
[](#cb3-48)}
```

### 返回值

字符串指针: - NULL: 转换失败 - 非NULL:
转换成功，返回Base64编码的字符串指针（DLL调用需要使用FreeStringPtr释放）

### 注意事项

- DLL调用返回的字符串指针需要使用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放内存

- Base64编码会使数据量增加约33%，大图片转换后的字符串会很长

- 如果需要将Base64字符串转回图片，可以使用 [Base64ToImage](/图像处理/base64字符串转为图片%20-%20Base64ToImage.html)
函数

- 建议在转换大图片前先进行适当压缩，以减少Base64字符串的长度

- 转换后的Base64字符串可以直接用于HTML的img标签，格式为：`<img src="data:image/png;base64,BASE64STRING">`

---

# 对比颜色 - CmpColor

### 函数简介

对比指定窗口坐标的颜色是否在指定的颜色范围区间，包含下限(>=
color1) 包含上限(<= color2)

### 接口名称

```
CmpColor
```

### DLL调用

```
int CmpColor(long ola, int x, int y,string color1,string color2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x` (整型数): 要对比颜色的X坐标

- `y` (整型数): 要对比颜色的Y坐标

- `color1` (字符串): 颜色起始范围，颜色格式
RRGGBB或者AARRGGBB

- `color2` (字符串): 颜色结束范围，颜色格式
RRGGBB或者AARRGGBB

#### 示例:

### 返回值

整型数 - 0: 失败 - 1: 成功

---

# 对比颜色 - CmpColorEx

### 函数简介

判断屏幕坐标点颜色是否在指定颜色模型范围内，返回 0/1 表示否/是。

**ColorModel:**

颜色每个通道单独计算范围，如颜色范围位3278FA，6496FF，实际对应R(50~100)
G(120 ~150) B(250 ~255)

包含下限(>= color1) 包含上限(<= color2)

支持ARGB模式如#FFFFFFFF

支持反色模式，交集并集查询颜色 - 0: 正常匹配，保留在颜色范围内的像素
- 1: 反色匹配，保留在颜色范围外的像素 - 2:
正常交集匹配，保留在颜色范围内的像素取交集 - 3:
反色交集匹配，保留在颜色范围外的像素取交集

如{“StartColor”: “3278FA”, “EndColor”: “6496FF”,“Type”:0}

### 接口名称

```
CmpColorEx
```

### DLL调用

```
int CmpColorEx(long ola, int x, int y, string colorJson)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x` (整型数): X坐标

- `y` (整型数): Y坐标

- `colorJson` (字符串):
颜色模型配置字符串，用于限定比较时的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

#### 示例:

```
[](#cb3-1)int ret = CmpColorEx(ola, 100, 200, "[{\"StartColor\":\"3278FA\",\"EndColor\":\"6496FF\",\"Type\":0}]");
```

### 返回值

整型数 - 0: 否 - 1: 是

---

# 对比颜色 - CmpColorHex

### 函数简介

对比指定颜色是否在指定的颜色范围区间，包含下限(>= color1)
包含上限(<= color2)支持AARRGGBB、RRGGBB颜色格式

### 接口名称

```
CmpColorHex
```

### DLL调用

```
int CmpColorHex(long ola,string color, string color1,string color2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `color` (字符串): 需要对比的颜色，颜色格式
RRGGBB或者AARRGGBB

- `color1` (字符串): 颜色起始范围，颜色格式
RRGGBB或者AARRGGBB

- `color2` (字符串): 颜色结束范围，颜色格式
RRGGBB或者AARRGGBB

#### 示例:

### 返回值

整型数 - 0: 失败 - 1: 成功

---

# 对比颜色 - CmpColorHexEx

### 函数简介

判断十六进制颜色是否在指定颜色模型范围内，返回 0/1 表示否/是。支持
AARRGGBB、RRGGBB 格式。

**ColorModel:**

颜色每个通道单独计算范围，如颜色范围位3278FA，6496FF，实际对应R(50~100)
G(120 ~150) B(250 ~255)

包含下限(>= color1) 包含上限(<= color2)

支持ARGB模式如#FFFFFFFF

支持反色模式，交集并集查询颜色 - 0: 正常匹配，保留在颜色范围内的像素
- 1: 反色匹配，保留在颜色范围外的像素 - 2:
正常交集匹配，保留在颜色范围内的像素取交集 - 3:
反色交集匹配，保留在颜色范围外的像素取交集

如{“StartColor”: “3278FA”, “EndColor”: “6496FF”,“Type”:0}

### 接口名称

```
CmpColorHexEx
```

### DLL调用

```
int CmpColorHexEx(long ola, string hex, string colorJson)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hex` (字符串): 颜色，格式 RRGGBB 或 AARRGGBB

- `colorJson` (字符串):
颜色模型配置字符串，用于限定比较时的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

#### 示例:

```
[](#cb3-1)int ret = CmpColorHexEx(ola, "#FFFFFFFF", "[{\"StartColor\":\"FFFFFF\",\"EndColor\":\"FFFFFF\",\"Type\":0}]");
```

### 返回值

整型数 - 0: 否 - 1: 是

---

# 对比颜色 - CmpColorPtr

### 函数简介

对比图片指定坐标是否在指定的颜色范围区间，包含下限(>= color1)
包含上限(<= color2)

### 接口名称

```
CmpColorPtr
```

### DLL调用

```
int CmpColorPtr(long ola,long img, int x, int y,string color1,string color2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `image1` (长整型数): OLAImage对象的地址

- `x` (整型数): 要对比颜色的X坐标

- `y` (整型数): 要对比颜色的Y坐标

- `color1` (字符串): 颜色起始范围，颜色格式
RRGGBB或者AARRGGBB

- `color2` (字符串): 颜色结束范围，颜色格式
RRGGBB或者AARRGGBB

#### 示例:

### 返回值

整型数 - 0: 失败 - 1: 成功

---

# 对比颜色 - CmpColorPtrEx

### 函数简介

判断图像坐标点颜色是否在指定颜色模型范围内，返回 0/1 表示否/是。

**ColorModel:**

颜色每个通道单独计算范围，如颜色范围位3278FA，6496FF，实际对应R(50~100)
G(120 ~150) B(250 ~255)

包含下限(>= color1) 包含上限(<= color2)

支持ARGB模式如#FFFFFFFF

支持反色模式，交集并集查询颜色 - 0: 正常匹配，保留在颜色范围内的像素
- 1: 反色匹配，保留在颜色范围外的像素 - 2:
正常交集匹配，保留在颜色范围内的像素取交集 - 3:
反色交集匹配，保留在颜色范围外的像素取交集

如{“StartColor”: “3278FA”, “EndColor”: “6496FF”,“Type”:0}

### 接口名称

```
CmpColorPtrEx
```

### DLL调用

```
int CmpColorPtrEx(long ola, long img, int x, int y, string colorJson)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `img` (长整型数): 图像句柄(OLAImage对象地址)

- `x` (整型数): X坐标

- `y` (整型数): Y坐标

- `colorJson` (字符串):
颜色模型配置字符串，用于限定比较时的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

#### 示例:

```
[](#cb3-1)int ret = CmpColorPtrEx(ola, img, 50, 60, "[{\"StartColor\":\"FFFFFF\",\"EndColor\":\"FFFFFF\",\"Type\":0}]");
```

### 返回值

整型数 - 0: 否 - 1: 是

---

# 弹窗显示图片 - ShowImage

### 函数简介

在独立窗口中显示图片，主要用于调试和测试阶段。此函数会创建一个新窗口来显示指定的图片，方便查看图片处理的结果。

### 接口名称

```
ShowImage
```

### DLL调用

```
int ShowImage(long ola, long imagePtr)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `imagePtr` (长整型数):
OLAImage对象的地址，要显示的图片指针

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)long ola = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 加载图片
[](#cb3-5)long imagePtr = LoadImage(ola, "test.bmp");
[](#cb3-6)
[](#cb3-7)// 显示图片
[](#cb3-8)int ret = ShowImage(ola, imagePtr);
[](#cb3-9)
[](#cb3-10)// 检查操作是否成功
[](#cb3-11)if (ret == 1) {
[](#cb3-12)    // 显示成功
[](#cb3-13)    // 等待用户关闭窗口
[](#cb3-14)    Sleep(1000);
[](#cb3-15)} else {
[](#cb3-16)    // 显示失败
[](#cb3-17)}
[](#cb3-18)
[](#cb3-19)// 释放图片内存
[](#cb3-20)FreeImagePtr(ola, imagePtr);
```

### 返回值

整型数: - 0: 失败 - 1: 成功

### 注意事项

- 此函数主要用于调试和测试，不建议在生产环境中使用

- 显示的窗口会阻塞程序执行，直到用户关闭窗口

- 可以同时显示多个图片，每个图片会在独立的窗口中显示

- 图片窗口支持基本的缩放操作

- 确保在显示图片前，图片指针是有效的

- 显示完成后，记得调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
释放图片内存

### 相关函数

- [LoadImage](/图像处理/加载图片%20-%20LoadImage.html):
加载图片

- [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html):
释放图片内存

- [SaveImage](图像处理/保存图片%20-%20SaveImage.html):
保存图片

---

# 弹窗显示图片 -
ShowImageFromFile

## 函数简介

显示指定路径的图片文件。此函数可以直接从文件路径加载并显示图片，支持常见的图片格式如PNG、JPG、BMP等。适用于快速预览图片文件内容。

## 接口名称

```
ShowImageFromFile
```

## DLL调用

```
int ShowImageFromFile(long instance, string file)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
file |
字符串 |
图片文件路径，支持相对路径和绝对路径 |
|

### 示例

```
[](#cb3-1)// 显示指定路径的图片
[](#cb3-2)char image_path[] = "D:\\test\\image.png";
[](#cb3-3)int result = ShowImageFromFile(ola, image_path);
[](#cb3-4)if (result == 1) {
[](#cb3-5)    printf("图片显示成功\n");
[](#cb3-6)} else {
[](#cb3-7)    printf("图片显示失败\n");
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)// 显示当前目录下的图片
[](#cb3-11)char current_image[] = "screenshot.png";
[](#cb3-12)int result = ShowImageFromFile(ola, current_image);
[](#cb3-13)if (result == 1) {
[](#cb3-14)    printf("当前目录图片显示成功\n");
[](#cb3-15)}
[](#cb3-16)
[](#cb3-17)// 显示不同格式的图片
[](#cb3-18)char* image_files[] = {
[](#cb3-19)    "D:\\images\\photo.jpg",
[](#cb3-20)    "D:\\images\\icon.png",
[](#cb3-21)    "D:\\images\\logo.bmp"
[](#cb3-22)};
[](#cb3-23)
[](#cb3-24)for (int i = 0; i < 3; i++) {
[](#cb3-25)    int result = ShowImageFromFile(ola, image_files[i]);
[](#cb3-26)    if (result == 1) {
[](#cb3-27)        printf("图片 %s 显示成功\n", image_files[i]);
[](#cb3-28)    } else {
[](#cb3-29)        printf("图片 %s 显示失败\n", image_files[i]);
[](#cb3-30)    }
[](#cb3-31)}
[](#cb3-32)
[](#cb3-33)// 显示截图文件
[](#cb3-34)char screenshot_path[] = "D:\\screenshots\\capture_20231201.png";
[](#cb3-35)int result = ShowImageFromFile(ola, screenshot_path);
[](#cb3-36)if (result == 1) {
[](#cb3-37)    printf("截图显示成功\n");
[](#cb3-38)}
[](#cb3-39)
[](#cb3-40)// 检查文件是否存在后显示
[](#cb3-41)char image_path[] = "D:\\test\\image.png";
[](#cb3-42)// 这里可以添加文件存在性检查
[](#cb3-43)int result = ShowImageFromFile(ola, image_path);
[](#cb3-44)if (result == 1) {
[](#cb3-45)    printf("图片显示成功\n");
[](#cb3-46)} else {
[](#cb3-47)    printf("图片文件不存在或格式不支持\n");
[](#cb3-48)}
```

## 返回值

整数型: - 1: 显示成功 - 0: 显示失败

## 注意事项

- 支持常见的图片格式：PNG、JPG、BMP、GIF等

- 文件路径可以是相对路径或绝对路径

- 如果文件不存在或格式不支持，函数将返回失败

- 显示的图片窗口可能需要用户手动关闭

- 建议在显示大图片前检查文件大小

- 此函数适用于图片预览、调试和验证图片文件内容

---

# 形态学开运算 - MorphOpen

## 函数简介

对图像进行开运算（先腐蚀后膨胀），去除小噪点同时保持整体形状。

## 接口名称

```
MorphOpen
```

## DLL调用

```
int64_t MorphOpen(int64_t instance, int64_t ptr, int32_t kernelSize);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针。 |
|

|
kernelSize |
整数型 |
结构元素核大小，建议使用奇数（3、5、7等）。 |
|

### 示例

```
[](#cb3-1)long image = LoadImage(ola, "D:/test/bin.png");
[](#cb3-2)if (image) {
[](#cb3-3)    long result = MorphOpen(ola, image, 3);
[](#cb3-4)    if (result) {
[](#cb3-5)        FreeImagePtr(ola, result);
[](#cb3-6)    }
[](#cb3-7)    FreeImagePtr(ola, image);
[](#cb3-8)}
```

## 返回值

返回处理后的图像句柄，失败返回0。

## 注意事项

- 与 `MorphClose` 配合可实现形态学细化清理。

- 处理后的图像需调用 `FreeImagePtr` 释放。

---

# 形态学梯度 - MorphGradient

## 函数简介

计算图像的形态学梯度。此函数通过形态学操作计算图像的梯度，可以突出图像的边缘信息。形态学梯度是膨胀图像与腐蚀图像的差值，能够有效地检测图像中的边缘和轮廓。

## 接口名称

```
MorphGradient
```

## DLL调用

```
long MorphGradient(long instance, long ptr, int kernelSize)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针，由图像处理函数返回 |
|

|
kernelSize |
整数型 |
形态学核的大小，通常为奇数（3、5、7等） |
|

### 示例

```
[](#cb3-1)// 基本形态学梯度计算
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\image.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    // 转换为灰度图
[](#cb3-5)    long grayImage = ConvertColor(ola, image, 0);
[](#cb3-6)    if (grayImage != 0) {
[](#cb3-7)        // 计算形态学梯度
[](#cb3-8)        long gradientImage = MorphGradient(ola, grayImage, 3);
[](#cb3-9)        if (gradientImage != 0) {
[](#cb3-10)            printf("形态学梯度计算完成\n");
[](#cb3-11)            ShowImage(ola, gradientImage);
[](#cb3-12)            FreeImagePtr(ola, gradientImage);
[](#cb3-13)        }
[](#cb3-14)        FreeImagePtr(ola, grayImage);
[](#cb3-15)    }
[](#cb3-16)    FreeImagePtr(ola, image);
[](#cb3-17)}
[](#cb3-18)
[](#cb3-19)// 不同核大小的对比
[](#cb3-20)long image = LoadImage(ola, "D:\\test\\image.png");
[](#cb3-21)if (image != 0) {
[](#cb3-22)    long grayImage = ConvertColor(ola, image, 0);
[](#cb3-23)    if (grayImage != 0) {
[](#cb3-24)        // 不同核大小的形态学梯度
[](#cb3-25)        long gradient3 = MorphGradient(ola, grayImage, 3);
[](#cb3-26)        long gradient5 = MorphGradient(ola, grayImage, 5);
[](#cb3-27)        long gradient7 = MorphGradient(ola, grayImage, 7);
[](#cb3-28)
[](#cb3-29)        printf("不同核大小的形态学梯度计算完成\n");
[](#cb3-30)
[](#cb3-31)        // 释放内存
[](#cb3-32)        if (gradient3 != 0) FreeImagePtr(ola, gradient3);
[](#cb3-33)        if (gradient5 != 0) FreeImagePtr(ola, gradient5);
[](#cb3-34)        if (gradient7 != 0) FreeImagePtr(ola, gradient7);
[](#cb3-35)
[](#cb3-36)        FreeImagePtr(ola, grayImage);
[](#cb3-37)    }
[](#cb3-38)    FreeImagePtr(ola, image);
[](#cb3-39)}
[](#cb3-40)
[](#cb3-41)// 图像处理流程中的形态学梯度
[](#cb3-42)long image = LoadImage(ola, "D:\\test\\target.png");
[](#cb3-43)if (image != 0) {
[](#cb3-44)    // 转换为灰度
[](#cb3-45)    long grayImage = ConvertColor(ola, image, 0);
[](#cb3-46)    if (grayImage != 0) {
[](#cb3-47)        // 阈值化
[](#cb3-48)        long binaryImage = Threshold(ola, grayImage, 128.0, 255.0, 0);
[](#cb3-49)        if (binaryImage != 0) {
[](#cb3-50)            // 去除小面积孤岛
[](#cb3-51)            long cleanedImage = RemoveIslands(ola, binaryImage, 100);
[](#cb3-52)            if (cleanedImage != 0) {
[](#cb3-53)                // 计算形态学梯度
[](#cb3-54)                long gradientImage = MorphGradient(ola, cleanedImage, 3);
[](#cb3-55)                if (gradientImage != 0) {
[](#cb3-56)                    printf("图像处理流程完成，已计算形态学梯度\n");
[](#cb3-57)                    FreeImagePtr(ola, gradientImage);
[](#cb3-58)                }
[](#cb3-59)                FreeImagePtr(ola, cleanedImage);
[](#cb3-60)            }
[](#cb3-61)            FreeImagePtr(ola, binaryImage);
[](#cb3-62)        }
[](#cb3-63)        FreeImagePtr(ola, grayImage);
[](#cb3-64)    }
[](#cb3-65)    FreeImagePtr(ola, image);
[](#cb3-66)}
[](#cb3-67)
[](#cb3-68)// 屏幕截图的边缘检测
[](#cb3-69)long screen = GetScreenDataPtr(ola, 0, 0, 1920, 1080);
[](#cb3-70)if (screen != 0) {
[](#cb3-71)    // 转换为灰度
[](#cb3-72)    long grayScreen = ConvertColor(ola, screen, 0);
[](#cb3-73)    if (grayScreen != 0) {
[](#cb3-74)        // 计算形态学梯度进行边缘检测
[](#cb3-75)        long edgeImage = MorphGradient(ola, grayScreen, 5);
[](#cb3-76)        if (edgeImage != 0) {
[](#cb3-77)            printf("屏幕截图边缘检测完成\n");
[](#cb3-78)            FreeImagePtr(ola, edgeImage);
[](#cb3-79)        }
[](#cb3-80)        FreeImagePtr(ola, grayScreen);
[](#cb3-81)    }
[](#cb3-82)    FreeImagePtr(ola, screen);
[](#cb3-83)}
[](#cb3-84)
[](#cb3-85)// 结合其他图像处理函数
[](#cb3-86)long image = LoadImage(ola, "D:\\test\\complex.png");
[](#cb3-87)if (image != 0) {
[](#cb3-88)    long grayImage = ConvertColor(ola, image, 0);
[](#cb3-89)    if (grayImage != 0) {
[](#cb3-90)        // 先进行形态学梯度
[](#cb3-91)        long gradientImage = MorphGradient(ola, grayImage, 3);
[](#cb3-92)        if (gradientImage != 0) {
[](#cb3-93)            // 对梯度图像进行阈值化
[](#cb3-94)            long binaryGradient = Threshold(ola, gradientImage, 50.0, 255.0, 0);
[](#cb3-95)            if (binaryGradient != 0) {
[](#cb3-96)                printf("梯度图像二值化完成\n");
[](#cb3-97)                FreeImagePtr(ola, binaryGradient);
[](#cb3-98)            }
[](#cb3-99)            FreeImagePtr(ola, gradientImage);
[](#cb3-100)        }
[](#cb3-101)        FreeImagePtr(ola, grayImage);
[](#cb3-102)    }
[](#cb3-103)    FreeImagePtr(ola, image);
[](#cb3-104)}
```

## 返回值

int64_t: 返回形态学梯度图像指针

## 注意事项

- 形态学梯度 = 膨胀图像 - 腐蚀图像

- kernelSize参数决定了形态学操作的结构元素大小

- 较大的核会产生更粗的边缘，较小的核会产生更细的边缘

- 建议使用奇数作为核大小（3、5、7等）

- 处理后的图像需要手动释放内存

- 适用于边缘检测、轮廓提取、图像分割等场景

- 与 [Threshold](/图像处理/图像阈值化%20-%20Threshold.html)
函数配合使用可以提取边缘

- 形态学梯度能够有效突出图像的边缘信息

---

# 形态学闭运算 - MorphClose

## 函数简介

对图像进行闭运算（先膨胀后腐蚀），用于填补小孔洞、连接相邻区域。

## 接口名称

```
MorphClose
```

## DLL调用

```
int64_t MorphClose(int64_t instance, int64_t ptr, int32_t kernelSize);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针。 |
|

|
kernelSize |
整数型 |
结构元素核大小，建议使用奇数（3、5、7等）。 |
|

### 示例

```
[](#cb3-1)long image = LoadImage(ola, "D:/test/bin.png");
[](#cb3-2)if (image) {
[](#cb3-3)    long result = MorphClose(ola, image, 5);
[](#cb3-4)    if (result) {
[](#cb3-5)        FreeImagePtr(ola, result);
[](#cb3-6)    }
[](#cb3-7)    FreeImagePtr(ola, image);
[](#cb3-8)}
```

## 返回值

返回处理后的图像句柄，失败返回0。

## 注意事项

- 与 `MorphOpen` 配合可实现形态学细化清理。

- 处理后的图像需调用 `FreeImagePtr` 释放。

---

# 形态学顶帽 - MorphTophat

## 函数简介

对图像进行形态学顶帽操作（Top-hat），用于提取比结构元素更亮的细小区域。

## 接口名称

```
MorphTophat
```

## DLL调用

```
int64_t MorphTophat(int64_t instance, int64_t ptr, int32_t kernelSize);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针。 |
|

|
kernelSize |
整数型 |
结构元素核大小，建议使用奇数（3、5、7等）。 |
|

### 示例

```
[](#cb3-1)long image = LoadImage(ola, "D:/test/img.png");
[](#cb3-2)if (image) {
[](#cb3-3)    long result = MorphTophat(ola, image, 5);
[](#cb3-4)    if (result) {
[](#cb3-5)        ShowImage(ola, result);
[](#cb3-6)        FreeImagePtr(ola, result);
[](#cb3-7)    }
[](#cb3-8)    FreeImagePtr(ola, image);
[](#cb3-9)}
```

## 返回值

返回处理后的图像句柄，失败返回0。

## 注意事项

- kernelSize 越大，提取的结构越粗。

- 处理后的图像需调用 `FreeImagePtr` 释放。

---

# 形态学黑帽 - MorphBlackhat

## 函数简介

对图像进行形态学黑帽操作（Black-hat），用于提取比结构元素更暗的细小区域。

## 接口名称

```
MorphBlackhat
```

## DLL调用

```
int64_t MorphBlackhat(int64_t instance, int64_t ptr, int32_t kernelSize);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针。 |
|

|
kernelSize |
整数型 |
结构元素核大小，建议使用奇数（3、5、7等）。 |
|

### 示例

```
[](#cb3-1)long image = LoadImage(ola, "D:/test/img.png");
[](#cb3-2)if (image) {
[](#cb3-3)    long result = MorphBlackhat(ola, image, 5);
[](#cb3-4)    if (result) {
[](#cb3-5)        ShowImage(ola, result);
[](#cb3-6)        FreeImagePtr(ola, result);
[](#cb3-7)    }
[](#cb3-8)    FreeImagePtr(ola, image);
[](#cb3-9)}
```

## 返回值

返回处理后的图像句柄，失败返回0。

## 注意事项

- kernelSize 越大，提取的结构越粗。

- 处理后的图像需调用 `FreeImagePtr` 释放。

---

# 快速ROI - FastROI

## 函数简介

快速ROI（Region of
Interest）函数，返回图像中不为0的最大区域图像。此函数可以自动识别图像中的有效区域并返回该区域的图像指针，适用于图像预处理和目标检测等应用场景。

## 接口名称

```
FastROI
```

## DLL调用

```
long FastROI(long instance, long ptr)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针，由图像处理函数返回 |
|

### 示例

```
[](#cb3-1)// 加载图像并进行快速ROI处理
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\image.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    long roiImage = FastROI(ola, image);
[](#cb3-5)
[](#cb3-6)    if (roiImage != 0) {
[](#cb3-7)        // 显示ROI结果
[](#cb3-8)        ShowImage(roiImage);
[](#cb3-9)
[](#cb3-10)        // 释放ROI图像内存
[](#cb3-11)        FreeImagePtr(ola, roiImage);
[](#cb3-12)    }
[](#cb3-13)
[](#cb3-14)    // 释放原图像内存
[](#cb3-15)    FreeImagePtr(ola, image);
[](#cb3-16)}
[](#cb3-17)
[](#cb3-18)// 对截图进行快速ROI处理
[](#cb3-19)long screen = GetScreenDataPtr(ola, 0, 0, 1920, 1080);
[](#cb3-20)if (screen != 0) {
[](#cb3-21)    long roiScreen = FastROI(ola, screen);
[](#cb3-22)
[](#cb3-23)    if (roiScreen != 0) {
[](#cb3-24)        printf("快速ROI处理完成\n");
[](#cb3-25)        // 处理ROI结果
[](#cb3-26)
[](#cb3-27)        FreeImagePtr(ola, roiScreen);
[](#cb3-28)    }
[](#cb3-29)
[](#cb3-30)    FreeImagePtr(ola, screen);
[](#cb3-31)}
```

## 返回值

长整数型:

- 成功：返回ROI图像对象的地址

- 失败：返回0

## 注意事项

- 返回的ROI图像为原图像中不为0的最大连通区域

- 使用完ROI图像后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口进行内存释放

- 此函数适用于图像预处理，可以自动去除图像边缘的无效区域

- ROI区域基于图像中非零像素的连通性计算得出

- 适用于需要提取图像主要内容的场景

---

# 截图GIF - CaptureGif

### 函数简介

抓取指定区域(x1, y1, x2,
y2)的动画并保存为GIF格式。此函数可以捕获指定区域的连续画面，生成动态GIF图片，适用于需要记录屏幕操作、动画效果等场景。当delay参数为0时，将只截取静态图片。

### 接口名称

```
CaptureGif
```

### DLL调用

```
int CaptureGif(long ola, int x1, int y1, int x2, int y2, string file, int delay, int time)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 区域的左上X坐标

- `y1` (整型数): 区域的左上Y坐标

- `x2` (整型数): 区域的右下X坐标

- `y2` (整型数): 区域的右下Y坐标

- `file` (字符串):
保存的文件名，支持相对路径和绝对路径。如果使用相对路径，文件将保存在SetPath设置的目录下

- `delay` (整型数):
动画帧间隔，单位毫秒。如果为0，表示只截取静态图片

- `time` (整型数): 总共截取的时间，单位毫秒

#### 示例:

```
[](#cb3-1)// 截取整个客户区的动画，每100毫秒一帧，持续3秒
[](#cb3-2)int result = CaptureGif(ola, 0, 0, 0, 0, "animation.gif", 100, 3000);
[](#cb3-3)if (result == 1) {
[](#cb3-4)    printf("GIF保存成功\n");
[](#cb3-5)} else {
[](#cb3-6)    printf("GIF保存失败\n");
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 截取指定区域的静态图片
[](#cb3-10)int result = CaptureGif(ola, 100, 100, 300, 300, "static.gif", 0, 0);
[](#cb3-11)if (result == 1) {
[](#cb3-12)    printf("图片保存成功\n");
[](#cb3-13)} else {
[](#cb3-14)    printf("图片保存失败\n");
[](#cb3-15)}
[](#cb3-16)
[](#cb3-17)// 使用绝对路径保存
[](#cb3-18)int result = CaptureGif(ola, 0, 0, 0, 0, "D:/screenshots/animation.gif", 100, 3000);
[](#cb3-19)if (result == 1) {
[](#cb3-20)    printf("GIF保存成功\n");
[](#cb3-21)} else {
[](#cb3-22)    printf("GIF保存失败\n");
[](#cb3-23)}
```

### 返回值

整型数: - 0: 截图保存失败 - 1: 截图保存成功

### 注意事项

- 坐标范围必须有效，否则可能导致截图失败

- 文件路径必须有效，且目标目录必须存在

- 如果文件已存在，将被覆盖

- 使用相对路径时，文件将保存在SetPath设置的目录下

- delay参数为0时，将只截取静态图片

- time参数必须大于等于0

- 建议delay参数不要设置太小，否则可能导致GIF文件过大

- 截图区域不要超出屏幕范围

- 建议使用绝对路径以避免路径解析问题

- 如果目标目录不存在，需要先创建目录

- 生成GIF时可能需要较大的内存空间

- 建议在录制动画前确保系统资源充足

---

# 截图并保存成文件 - Capture

### 函数简介

抓取指定区域(x1, y1, x2,
y2)的图像并保存为文件。此函数可以根据文件后缀名自动识别保存格式，支持BMP、PNG、JPG等常见图片格式。适用于需要截取屏幕或窗口特定区域的场景。
图片大小为 x2-x1,y2-y1 ### 接口名称

```
Capture
```

### DLL调用

```
int Capture(long ola, int x1, int y1, int x2, int y2, string file)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 区域的左上X坐标

- `y1` (整型数): 区域的左上Y坐标

- `x2` (整型数): 区域的右下X坐标

- `y2` (整型数): 区域的右下Y坐标

- `file` (字符串):
保存的文件名，支持相对路径和绝对路径。如果使用相对路径，文件将保存在SetPath设置的目录下

#### 示例:

```
[](#cb3-1)// 截取整个客户区并保存为BMP
[](#cb3-2)int result = Capture(ola, 0, 0, 0, 0, "screen.bmp");
[](#cb3-3)if (result == 1) {
[](#cb3-4)    printf("截图保存成功\n");
[](#cb3-5)} else {
[](#cb3-6)    printf("截图保存失败\n");
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 截取指定区域并保存为PNG
[](#cb3-10)int result = Capture(ola, 100, 100, 300, 300, "region.png");
[](#cb3-11)if (result == 1) {
[](#cb3-12)    printf("截图保存成功\n");
[](#cb3-13)} else {
[](#cb3-14)    printf("截图保存失败\n");
[](#cb3-15)}
[](#cb3-16)
[](#cb3-17)// 使用绝对路径保存
[](#cb3-18)int result = Capture(ola, 0, 0, 0, 0, "D:/screenshots/screen.jpg");
[](#cb3-19)if (result == 1) {
[](#cb3-20)    printf("截图保存成功\n");
[](#cb3-21)} else {
[](#cb3-22)    printf("截图保存失败\n");
[](#cb3-23)}
```

### 返回值

整型数: - 0: 截图保存失败 - 1: 截图保存成功

### 注意事项

- 坐标范围必须有效，否则可能导致截图失败

- 文件路径必须有效，且目标目录必须存在

- 文件后缀名决定保存格式，支持.bmp、.png、.jpg等

- 如果文件已存在，将被覆盖

- 使用相对路径时，文件将保存在SetPath设置的目录下

- 建议在保存前检查目标目录的写入权限

- 截图区域不要超出屏幕范围

- 保存JPG格式时可能会有一定的压缩损失

- 建议使用绝对路径以避免路径解析问题

- 如果目标目录不存在，需要先创建目录

---

# 截图返回字节流 -
GetScreenData

### 函数简介

获取指定区域的图像数据，以二进制数据的方式返回。数据格式为BBGGRRAA（BGRA格式），每个像素占用4字节。此函数比GetScreenDataBmp具有更高的读取效率，适用于需要快速获取屏幕图像数据的场景。

图像尺寸计算： - 图像宽度 = stride / 4 - 图像高度 = size / stride

当x1, y1, x2, y2参数都传0时，将获取窗口整个客户区的图像。

- 此接口线程不安全无法并发调用(不推荐使用)

- 建议使用GetScreenDataPtr + GetImageData + FreeImagePtr
接口安全读取BMP数据

### 接口名称

```
GetScreenData
```

### DLL调用

```
int GetScreenData(long ola, int x1, int y1, int x2, int y2, long* data, int* size, int* stride)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 区域的左上X坐标

- `y1` (整型数): 区域的左上Y坐标

- `x2` (整型数): 区域的右下X坐标

- `y2` (整型数): 区域的右下Y坐标

- `data` (长整型数指针): 返回图片数据的指针地址

- `size` (整型数指针): 返回图片数据的总长度（字节数）

- `stride` (整型数指针): 返回图片每行数据的字节数

#### 示例:

```
[](#cb3-1)// 获取指定区域的图像数据
[](#cb3-2)long data = 0;
[](#cb3-3)int size = 0;
[](#cb3-4)int stride = 0;
[](#cb3-5)
[](#cb3-6)if (GetScreenData(ola, 0, 0, 800, 600, &data, &size, &stride)) {
[](#cb3-7)    // 计算图像尺寸
[](#cb3-8)    int width = stride / 4;
[](#cb3-9)    int height = size / stride;
[](#cb3-10)
[](#cb3-11)    // 处理图像数据
[](#cb3-12)    unsigned char* imageData = (unsigned char*)data;
[](#cb3-13)    // ... 处理图像数据 ...
[](#cb3-14)
[](#cb3-15)    printf("图像尺寸: %dx%d\n", width, height);
[](#cb3-16)    printf("数据大小: %d 字节\n", size);
[](#cb3-17)    printf("每行字节数: %d\n", stride);
[](#cb3-18)} else {
[](#cb3-19)    printf("获取图像数据失败\n");
[](#cb3-20)}
[](#cb3-21)
[](#cb3-22)// 获取整个客户区
[](#cb3-23)if (GetScreenData(ola, 0, 0, 0, 0, &data, &size, &stride)) {
[](#cb3-24)    // ... 处理图像数据 ...
[](#cb3-25)}
```

### 返回值

整型数: - 1: 成功获取图像数据 - 0: 获取失败

### 注意事项

- 数据格式为BBGGRRAA（BGRA格式），每个像素占用4字节

- 图像尺寸可以通过stride和size计算得出

- 获取的数据指针保存在当前对象中，下次调用此接口时会自动释放

- 需要将数据拷贝到自己的字节集中再使用

- 坐标范围必须在有效范围内

- 建议在使用前检查坐标是否有效

- 处理大尺寸图像时注意内存使用

- 数据指针在下次调用前有效

- 如果需要保存图像，建议及时处理数据

- 建议在循环中获取图像时注意内存管理

---

# 截图返回字节流 -
GetScreenDataBmp

### 函数简介

获取指定区域的图像数据，以BMP格式的二进制数据方式返回。此函数返回标准的BMP文件格式数据，可以直接保存为BMP文件或进行BMP格式的图像处理。当x1,
y1, x2, y2参数都传0时，将获取窗口整个客户区的图像。 -
此接口线程不安全无法并发调用(不推荐使用) - 建议使用GetScreenDataPtr +
GetImageBmpData + FreeImagePtr 接口安全读取BMP数据 ### 接口名称

```
GetScreenDataBmp
```

### DLL调用

```
int GetScreenDataBmp(long ola, int x1, int y1, int x2, int y2, long* data, int* size)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 区域的左上X坐标

- `y1` (整型数): 区域的左上Y坐标

- `x2` (整型数): 区域的右下X坐标

- `y2` (整型数): 区域的右下Y坐标

- `data` (长整型数指针): 返回BMP图片数据的指针地址

- `size` (整型数指针):
返回BMP图片数据的总长度（字节数）

#### 示例:

```
[](#cb3-1)// 获取指定区域的BMP图像数据
[](#cb3-2)long data = 0;
[](#cb3-3)int size = 0;
[](#cb3-4)
[](#cb3-5)if (GetScreenDataBmp(ola, 0, 0, 800, 600, &data, &size)) {
[](#cb3-6)    // 处理BMP数据
[](#cb3-7)    unsigned char* bmpData = (unsigned char*)data;
[](#cb3-8)
[](#cb3-9)    // 保存为BMP文件
[](#cb3-10)    FILE* file = fopen("screenshot.bmp", "wb");
[](#cb3-11)    if (file) {
[](#cb3-12)        fwrite(bmpData, 1, size, file);
[](#cb3-13)        fclose(file);
[](#cb3-14)        printf("BMP文件保存成功，大小: %d 字节\n", size);
[](#cb3-15)    }
[](#cb3-16)
[](#cb3-17)    // 或者进行其他BMP格式处理
[](#cb3-18)    // ... 处理BMP数据 ...
[](#cb3-19)} else {
[](#cb3-20)    printf("获取BMP图像数据失败\n");
[](#cb3-21)}
[](#cb3-22)
[](#cb3-23)// 获取整个客户区
[](#cb3-24)if (GetScreenDataBmp(ola, 0, 0, 0, 0, &data, &size)) {
[](#cb3-25)    // ... 处理BMP数据 ...
[](#cb3-26)}
```

### 返回值

整型数: - 1: 成功获取BMP图像数据 - 0: 获取失败

### 注意事项

- 返回的数据是标准的BMP文件格式，包含BMP文件头

- 可以直接将数据保存为BMP文件

- 获取的数据指针保存在当前对象中，下次调用此接口时会自动释放

- 需要将数据拷贝到自己的字节集中再使用

- 坐标范围必须在有效范围内

- 建议在使用前检查坐标是否有效

- 处理大尺寸图像时注意内存使用

- 数据指针在下次调用前有效

- 如果需要保存图像，建议及时处理数据

- 建议在循环中获取图像时注意内存管理

- BMP格式相比其他格式占用空间较大，但兼容性最好

- 如果需要更高效的图像数据获取，可以考虑使用GetScreenData函数

---

# 拷贝图片 - CopyImage

### 函数简介

创建图片的完整副本。此函数可以复制一个OLAImage对象，生成一个具有相同内容的新图片对象。适用于需要在不修改原图的情况下对图片进行处理或保存的场景。

### 接口名称

```
CopyImage
```

### DLL调用

```
long CopyImage(long ola, long imagePtr)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `imagePtr` (长整型数): 要复制的OLAImage对象的地址

#### 示例:

```
[](#cb3-1)// 加载原始图片
[](#cb3-2)long imagePtr = LoadImage(ola, "/OLA/pic/pic.bmp");
[](#cb3-3)if (imagePtr != 0) {
[](#cb3-4)    // 创建图片副本
[](#cb3-5)    long copyPtr = CopyImage(ola, imagePtr);
[](#cb3-6)    if (copyPtr != 0) {
[](#cb3-7)        // 使用复制的图片
[](#cb3-8)        // ...
[](#cb3-9)
[](#cb3-10)        // 使用完后释放复制的图片内存
[](#cb3-11)        FreeImagePtr(ola, copyPtr);
[](#cb3-12)    } else {
[](#cb3-13)        printf("图片复制失败\n");
[](#cb3-14)    }
[](#cb3-15)
[](#cb3-16)    // 释放原始图片内存
[](#cb3-17)    FreeImagePtr(ola, imagePtr);
[](#cb3-18)}
```

### 返回值

长整型数: 返回复制的OLAImage对象的地址。如果复制失败返回0。

### 注意事项

- 原始图片指针必须有效，否则可能导致程序异常

- 复制的图片与原图完全相同，包括尺寸和内容

- 复制后的图片与原图完全独立，修改一个不会影响另一个

- 复制的图片使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口释放内存

- 原始图片的内存需要单独释放，不会自动释放

- 建议在复制大图片时注意内存使用

- 如果原始图片指针无效，函数将返回0

- 复制操作会占用额外的内存空间，请确保系统有足够的内存

- 建议在复制前检查原始图片是否成功加载

- 如果复制失败，请检查原始图片指针是否有效

---

# 拼接图片 - ConcatImage

### 函数简介

将两张图片拼接成一张新图片。此函数可以将两张图片按照指定的方向（水平或垂直）拼接在一起，生成一张新的图片。常用于图片合成、长图制作、图片对比等场景。支持不同尺寸图片的拼接，可以自动调整对齐方式。

### 接口名称

```
ConcatImage
```

### DLL调用

```
long ConcatImage(long ola, long image_ptr1, long image_ptr2, int gap, string color, int direction)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `image_ptr1` (长整型数): 第一张图片的句柄。

- `image_ptr2` (长整型数): 第二张图片的句柄。

- `gap` (整型数): 两张图片之间的间隙

- `color` (字符串型) : 填充两张图片之间的间隙的颜色

- `direction` (整型数): 拼接方向：

0: 水平拼接（左右）

- 1: 垂直拼接（上下）

#### 示例:

```
[](#cb3-1)// 加载两张图片
[](#cb3-2)long image1 = LoadImage(ola, "D:\\test\\left.png");
[](#cb3-3)long image2 = LoadImage(ola, "D:\\test\\right.png");
[](#cb3-4)
[](#cb3-5)if (image1 != 0 && image2 != 0) {
[](#cb3-6)    // 水平拼接（左右）
[](#cb3-7)    long horizontal = ConcatImage(ola, image1, image2, 3, "#FFFFFF", 0);
[](#cb3-8)    if (horizontal != 0) {
[](#cb3-9)        SaveImageFromPtr(ola, horizontal, "D:\\test\\horizontal.png");
[](#cb3-10)        printf("水平拼接完成\n");
[](#cb3-11)        FreeImagePtr(ola, horizontal);
[](#cb3-12)    }
[](#cb3-13)
[](#cb3-14)    // 垂直拼接（上下）
[](#cb3-15)    long vertical = ConcatImage(ola, image1, image2, 3, "#FFFFFF", 1);
[](#cb3-16)    if (vertical != 0) {
[](#cb3-17)        SaveImageFromPtr(ola, vertical, "D:\\test\\vertical.png");
[](#cb3-18)        printf("垂直拼接完成\n");
[](#cb3-19)        FreeImagePtr(ola, vertical);
[](#cb3-20)    }
[](#cb3-21)
[](#cb3-22)    // 释放原图内存
[](#cb3-23)    FreeImagePtr(ola, image1);
[](#cb3-24)    FreeImagePtr(ola, image2);
[](#cb3-25)}
[](#cb3-26)
[](#cb3-27)// 多图片拼接示例（制作长图）
[](#cb3-28)void CreateLongImage(const char** image_paths, int count, const char* output_path) {
[](#cb3-29)    if (count < 2) return;
[](#cb3-30)
[](#cb3-31)    // 加载第一张图片
[](#cb3-32)    long result = LoadImage(ola, image_paths[0]);
[](#cb3-33)    if (result == 0) return;
[](#cb3-34)
[](#cb3-35)    // 依次拼接其他图片
[](#cb3-36)    for (int i = 1; i < count; i++) {
[](#cb3-37)        long next = LoadImage(ola, image_paths[i]);
[](#cb3-38)        if (next != 0) {
[](#cb3-39)            long temp = ConcatImage(ola, result, next, 1);  // 垂直拼接
[](#cb3-40)            FreeImagePtr(ola, result);
[](#cb3-41)            FreeImagePtr(ola, next);
[](#cb3-42)            result = temp;
[](#cb3-43)        }
[](#cb3-44)    }
[](#cb3-45)
[](#cb3-46)    // 保存结果
[](#cb3-47)    if (result != 0) {
[](#cb3-48)        SaveImageFromPtr(ola, result, output_path);
[](#cb3-49)        FreeImagePtr(ola, result);
[](#cb3-50)    }
[](#cb3-51)}
[](#cb3-52)
[](#cb3-53)// 制作图片对比（左右对比）
[](#cb3-54)void CreateComparisonImage(const char* before_path, const char* after_path, const char* output_path) {
[](#cb3-55)    long before = LoadImage(ola, before_path);
[](#cb3-56)    long after = LoadImage(ola, after_path);
[](#cb3-57)
[](#cb3-58)    if (before != 0 && after != 0) {
[](#cb3-59)        // 确保两张图片高度相同
[](#cb3-60)        int width1, height1, width2, height2;
[](#cb3-61)        GetImageSize(ola, before, &width1, &height1);
[](#cb3-62)        GetImageSize(ola, after, &width2, &height2);
[](#cb3-63)
[](#cb3-64)        if (height1 != height2) {
[](#cb3-65)            // 调整高度
[](#cb3-66)            int target_height = height1 < height2 ? height1 : height2;
[](#cb3-67)            long resized_before = ReSize(ola, before, width1 * target_height / height1, target_height);
[](#cb3-68)            long resized_after = ReSize(ola, after, width2 * target_height / height2, target_height);
[](#cb3-69)
[](#cb3-70)            if (resized_before != 0 && resized_after != 0) {
[](#cb3-71)                // 水平拼接调整后的图片
[](#cb3-72)                long comparison = ConcatImage(ola, resized_before, resized_after, 0);
[](#cb3-73)                if (comparison != 0) {
[](#cb3-74)                    SaveImageFromPtr(ola, comparison, output_path);
[](#cb3-75)                    FreeImagePtr(ola, comparison);
[](#cb3-76)                }
[](#cb3-77)
[](#cb3-78)                FreeImagePtr(ola, resized_before);
[](#cb3-79)                FreeImagePtr(ola, resized_after);
[](#cb3-80)            }
[](#cb3-81)        } else {
[](#cb3-82)            // 直接水平拼接
[](#cb3-83)            long comparison = ConcatImage(ola, before, after, 0);
[](#cb3-84)            if (comparison != 0) {
[](#cb3-85)                SaveImageFromPtr(ola, comparison, output_path);
[](#cb3-86)                FreeImagePtr(ola, comparison);
[](#cb3-87)            }
[](#cb3-88)        }
[](#cb3-89)
[](#cb3-90)        FreeImagePtr(ola, before);
[](#cb3-91)        FreeImagePtr(ola, after);
[](#cb3-92)    }
[](#cb3-93)}
```

### 返回值

长整型数: - 0: 拼接失败 - 非0: 拼接成功，返回新图片的句柄

### 注意事项

- 水平拼接时，两张图片的高度最好相同，否则会以较小的高度为准

- 垂直拼接时，两张图片的宽度最好相同，否则会以较小的宽度为准

- 拼接后会返回新的图片句柄，原图片不会被修改

- 新图片句柄使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
释放内存

- 如果需要在拼接前调整图片大小，可以配合使用 [ReSize](/图像处理/调整图片大小%20-%20ReSize.html) 或 [ScalePixels](/图像处理/调整图片大小%20-%20ScalePixels.html)
函数

---

# 拼接图片追加 -
ImageStitchAppend

## 函数简介

向拼接实例追加一张图像。

## 接口名称

```
ImageStitchAppend
```

## DLL调用

```
int32_t ImageStitchAppend(int64_t instance, int64_t imageStitch, int64_t image);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
imageStitch |
长整数型 |
拼接实例句柄。 |
|

|
image |
长整数型 |
图像句柄。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t st = ImageStitchCreate(instance);
[](#cb3-3)int64_t img = LoadImage(instance, "C:/imgs/1.png");
[](#cb3-4)int32_t ok = ImageStitchAppend(instance, st, img);
[](#cb3-5)printf("append: %d\n", ok);
[](#cb3-6)FreeImagePtr(instance, img);
[](#cb3-7)ImageStitchFree(instance, st);
[](#cb3-8)DestroyCOLAPlugInterFace(instance);
```

## 返回值

0 失败，1 成功。

## 注意事项

- 确保 `image` 有效且与实例期望的尺寸/通道兼容。

---

# 指定区域数据是否卡屏 -
IsDisplayDead

判断指定的区域，在指定的时间内(秒),图像数据是否一直不变.(卡屏).
(或者绑定的窗口不存在也返回1)

没有卡屏立马返回

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

### 接口名称

```
IsDisplayDead
```

### DLL调用

```
int IsDisplayDead(long ola, int x1, int y1, int x2, int y2, int time)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `time` (整型数): 识别间隔，单位毫秒

#### 示例:

待补充…

### 返回值

整型数:

0正常,1卡屏

---

# 旋转图片 - RotateImage

### 函数简介

将图片旋转指定的角度。此函数可以将图片按照指定的角度进行旋转，支持任意角度的旋转，并自动调整输出图片的大小以容纳旋转后的内容。旋转时使用高质量的插值算法以保持图像质量，适用于图像预处理、界面设计等场景。

### 接口名称

```
RotateImage
```

### DLL调用

```
long RotateImage(long ola, long image_ptr, double angle)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `image_ptr` (长整型数): 要旋转的图片句柄。

- `angle` (双精度浮点数):
旋转角度，单位为度，正值表示顺时针旋转，负值表示逆时针旋转。

#### 示例:

```
[](#cb3-1)// 加载图片并进行旋转
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\source.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    // 获取原图尺寸
[](#cb3-5)    int width, height;
[](#cb3-6)    GetImageSize(ola, image, &width, &height);
[](#cb3-7)    printf("原图大小：%d x %d\n", width, height);
[](#cb3-8)
[](#cb3-9)    // 旋转90度（顺时针）
[](#cb3-10)    long rotated90 = RotateImage(ola, image, 90.0f);
[](#cb3-11)    if (rotated90 != 0) {
[](#cb3-12)        SaveImageFromPtr(ola, rotated90, "D:\\test\\rotated90.png");
[](#cb3-13)        printf("90度旋转完成\n");
[](#cb3-14)        FreeImagePtr(ola, rotated90);
[](#cb3-15)    }
[](#cb3-16)
[](#cb3-17)    // 旋转180度
[](#cb3-18)    long rotated180 = RotateImage(ola, image, 180.0f);
[](#cb3-19)    if (rotated180 != 0) {
[](#cb3-20)        SaveImageFromPtr(ola, rotated180, "D:\\test\\rotated180.png");
[](#cb3-21)        printf("180度旋转完成\n");
[](#cb3-22)        FreeImagePtr(ola, rotated180);
[](#cb3-23)    }
[](#cb3-24)
[](#cb3-25)    // 旋转45度（会自动调整输出图片大小）
[](#cb3-26)    long rotated45 = RotateImage(ola, image, 45.0f);
[](#cb3-27)    if (rotated45 != 0) {
[](#cb3-28)        SaveImageFromPtr(ola, rotated45, "D:\\test\\rotated45.png");
[](#cb3-29)        printf("45度旋转完成\n");
[](#cb3-30)        FreeImagePtr(ola, rotated45);
[](#cb3-31)    }
[](#cb3-32)
[](#cb3-33)    // 逆时针旋转30度
[](#cb3-34)    long rotatedMinus30 = RotateImage(ola, image, -30.0f);
[](#cb3-35)    if (rotatedMinus30 != 0) {
[](#cb3-36)        SaveImageFromPtr(ola, rotatedMinus30, "D:\\test\\rotated_minus30.png");
[](#cb3-37)        printf("逆时针30度旋转完成\n");
[](#cb3-38)        FreeImagePtr(ola, rotatedMinus30);
[](#cb3-39)    }
[](#cb3-40)
[](#cb3-41)    FreeImagePtr(ola, image);
[](#cb3-42)}
[](#cb3-43)
[](#cb3-44)// 批量处理图片旋转的辅助函数
[](#cb3-45)void RotateImages(const char* input_dir, const char* output_dir, float angle) {
[](#cb3-46)    char search_path[256];
[](#cb3-47)    sprintf(search_path, "%s\\*.png", input_dir);
[](#cb3-48)
[](#cb3-49)    WIN32_FIND_DATA fd;
[](#cb3-50)    HANDLE hFind = FindFirstFile(search_path, &fd);
[](#cb3-51)    if (hFind != INVALID_HANDLE_VALUE) {
[](#cb3-52)        do {
[](#cb3-53)            if (!(fd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)) {
[](#cb3-54)                char input_path[512], output_path[512];
[](#cb3-55)                sprintf(input_path, "%s\\%s", input_dir, fd.cFileName);
[](#cb3-56)                sprintf(output_path, "%s\\rotated_%s", output_dir, fd.cFileName);
[](#cb3-57)
[](#cb3-58)                long image = LoadImage(ola, input_path);
[](#cb3-59)                if (image != 0) {
[](#cb3-60)                    long rotated = RotateImage(ola, image, angle);
[](#cb3-61)                    if (rotated != 0) {
[](#cb3-62)                        SaveImageFromPtr(ola, rotated, output_path);
[](#cb3-63)                        FreeImagePtr(ola, rotated);
[](#cb3-64)                    }
[](#cb3-65)                    FreeImagePtr(ola, image);
[](#cb3-66)                }
[](#cb3-67)            }
[](#cb3-68)        } while (FindNextFile(hFind, &fd));
[](#cb3-69)        FindClose(hFind);
[](#cb3-70)    }
[](#cb3-71)}
```

### 返回值

长整型数: - 0: 旋转失败 - 非0: 旋转成功，返回新图片的句柄

### 注意事项

- 旋转角度为正值时顺时针旋转，为负值时逆时针旋转

- 对于非90度的倍数旋转，输出图片的尺寸会自动调整以容纳完整的旋转结果

- 旋转后会返回新的图片句柄，原图片不会被修改

- 新图片句柄使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
释放内存

- 如果需要在旋转的同时调整图片大小，可以配合使用 [ReSize](/图像处理/调整图片大小%20-%20ReSize.html) 或 [ScalePixels](/图像处理/调整图片大小%20-%20ScalePixels.html)
函数

---

# 查找所有符合的颜色 -
FindColorList

### 函数简介

查找指定区域内符合指定颜色范围的所有颜色点。此函数可以在指定区域内搜索所有符合特定颜色范围的像素点，并返回它们的坐标列表。适用于需要批量查找颜色点的场景，如区域分析、图像特征提取等。

每个通道单独计算范围，如颜色范围位3278FA，6496FF，实际对应R(50~100)
G(120 ~150) B(250 ~255)

包含下限(>= color1) 包含上限(<= color2)

支持ARGB模式如#FFFFFFFF

x1,y1,x2,y2传0,0,0,0 为截取绑定窗口整个客户区

返回数据为相对窗口坐标

### 接口名称

```
FindColorList
```

### DLL调用

```
long FindColorList(long ola, int x1,int y1,int x2,int y2,string color1,string color2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 区域的左上X坐标

- `y1` (整型数): 区域的左上Y坐标

- `x2` (整型数): 区域的右下X坐标

- `y2` (整型数): 区域的右下Y坐标

- `color1` (字符串): 颜色起始范围，颜色格式 RRGGBB

- `color2` (字符串): 颜色结束范围，颜色格式 RRGGBB

#### 示例:

```
[](#cb3-1)// 在窗口客户区查找所有指定颜色点
[](#cb3-2)long result = FindColorList(ola, 0, 0, 0, 0, "057093", "057093");
[](#cb3-3)if (result != 0) {
[](#cb3-4)    // 解析返回的JSON字符串
[](#cb3-5)    // 注意：使用完后需要调用FreeStringPtr释放内存
[](#cb3-6)    printf("找到颜色点列表：%s\n", result);
[](#cb3-7)    FreeStringPtr(ola, result);
[](#cb3-8)} else {
[](#cb3-9)    printf("未找到颜色点\n");
[](#cb3-10)}
[](#cb3-11)
[](#cb3-12)// 在指定区域查找所有白色点
[](#cb3-13)long result = FindColorList(ola, 100, 100, 200, 200, "FFFFFF", "FFFFFF");
[](#cb3-14)if (result != 0) {
[](#cb3-15)    // 解析返回的JSON字符串
[](#cb3-16)    printf("找到白色点列表：%s\n", result);
[](#cb3-17)    FreeStringPtr(ola, result);
[](#cb3-18)} else {
[](#cb3-19)    printf("未找到白色点\n");
[](#cb3-20)}
```

### 返回值

字符串: 返回识别到的坐标点列表的JSON字符串，格式如下：

```
[](#cb4-1)[
[](#cb4-2)  {
[](#cb4-3)    "X": 19,
[](#cb4-4)    "Y": 18
[](#cb4-5)  },
[](#cb4-6)  {
[](#cb4-7)    "X": 20,
[](#cb4-8)    "Y": 18
[](#cb4-9)  },
[](#cb4-10)  {
[](#cb4-11)    "X": 22,
[](#cb4-12)    "Y": 18
[](#cb4-13)  }
[](#cb4-14)]
```

### 注意事项

- 颜色范围使用RRGGBB格式，每个通道单独计算范围

- 支持ARGB模式，如#FFFFFFFF

- 当x1,y1,x2,y2都传0时，会查找整个窗口客户区

- 返回的坐标是相对于窗口客户区的坐标

- 返回的JSON字符串需要解析后才能使用

- DLL调用返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

- 颜色范围越大，匹配的像素点越多，但可能会影响查找精度

- 如果区域内符合条件的点较多，返回的JSON字符串可能会很长，请注意内存使用

---

# 查找所有符合的颜色 -
FindColorListEx

### 函数简介

在绑定窗口中查找指定区域内所有符合颜色模型的像素点，返回坐标列表。适合批量分析、区域检测、特征提取等场景。

**ColorModel:**

颜色每个通道单独计算范围，如颜色范围位 3278FA，6496FF，实际对应
R(50~100) / G(120~150) / B(250~255)。

包含下限(>= StartColor) 与上限(<= EndColor)；支持 ARGB 形式（如
`#FFFFFFFF`）。

支持反色/交集/并集等模式（按实现为准），示例：

```
{"StartColor":"3278FA","EndColor":"6496FF","Type":0}
```

`x1,y1,x2,y2` 传 `0,0,0,0`
为查找绑定窗口整个客户区；返回坐标为相对绑定窗口客户区坐标。

### 接口名称

```
FindColorListEx
```

### DLL调用

```
long FindColorListEx(long ola, int x1, int y1, int x2, int y2, string colorJson)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 生成。

- `x1` (整型数): 区域左上角 X 坐标

- `y1` (整型数): 区域左上角 Y 坐标

- `x2` (整型数): 区域右下角 X 坐标

- `y2` (整型数): 区域右下角 Y 坐标

- `colorJson` (字符串):
颜色模型配置字符串，用于限定颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

#### 示例:

```
[](#cb4-1)long p = FindColorListEx(ola, 0, 0, 0, 0,
[](#cb4-2)    "[{\"StartColor\":\"3278FA\",\"EndColor\":\"6496FF\",\"Type\":0}]");
[](#cb4-3)if (p != 0) {
[](#cb4-4)    // p 指向JSON字符串，使用完需要释放
[](#cb4-5)    // 示例输出: [{"X":10,"Y":20},{"X":30,"Y":40}]
[](#cb4-6)    FreeStringPtr(ola, p);
[](#cb4-7)}
```

### 返回值

字符串:

返回所有匹配点坐标的 JSON 字符串，格式如下：

```
[](#cb5-1)[
[](#cb5-2)  { "X": 19, "Y": 18 },
[](#cb5-3)  { "X": 20, "Y": 18 },
[](#cb5-4)  { "X": 22, "Y": 18 }
[](#cb5-5)]
```

### 注意事项

- 返回的字符串指针需调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放。

- 当 `x1,y1,x2,y2` 全为 0 时，搜索整个绑定窗口客户区。

- 返回坐标为相对绑定窗口客户区坐标。

- 颜色范围越大，匹配点越多，可能影响查找耗时与内存。

---

# 查找指定区域内的所有颜色块
- FindColorBlockList

### 函数简介

查找指定区域内符合指定颜色范围的所有颜色块坐标点。此函数可以在指定区域内搜索所有符合特定颜色范围的颜色块，并返回它们的左上角坐标列表。适用于需要批量查找颜色区域的场景，如UI元素批量定位、图像特征批量识别等。

**ColorModel:**

颜色每个通道单独计算范围，如颜色范围位3278FA，6496FF，实际对应R(50~100)
G(120 ~150) B(250 ~255)

包含下限(>= color1) 包含上限(<= color2)

支持ARGB模式如#FFFFFFFF

支持反色模式，交集并集查询颜色 - 0: 正常匹配，保留在颜色范围内的像素
- 1: 反色匹配，保留在颜色范围外的像素 - 2:
正常交集匹配，保留在颜色范围内的像素取交集 - 3:
反色交集匹配，保留在颜色范围外的像素取交集

如{“StartColor”: “3278FA”, “EndColor”: “6496FF”,“Type”:0}

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

返回数据为相对窗口坐标

### 接口名称

```
FindColorBlockList
```

### DLL调用

```
long FindColorBlockList(long ola, int x1, int y1, int x2, int y2, string colorList, int count, int width, int height, int type)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `count` (整型数):
在宽度为width,高度为height的颜色块中，符合color颜色的最小数量

- `width` (整型数): 色块宽度

- `height` (整型数): 色块高度

- `type` (整型数): 是否去重

0: 不去重

- 1: 去重

#### 示例:

```
[](#cb3-1)// 在窗口客户区查找所有颜色块
[](#cb3-2)string colorList = "[{\"StartColor\": \"3278FA\", \"EndColor\": \"6496FF\", \"Type\": 0}]";
[](#cb3-3)long result = FindColorBlockList(ola, 0, 0, 0, 0, colorList, 10, 20, 20, 0);
[](#cb3-4)if (result != 0) {
[](#cb3-5)    // 解析返回的JSON字符串
[](#cb3-6)    // 注意：使用完后需要调用FreeStringPtr释放内存
[](#cb3-7)    printf("找到颜色块列表：%s\n", result);
[](#cb3-8)    FreeStringPtr(ola, result);
[](#cb3-9)} else {
[](#cb3-10)    printf("未找到颜色块\n");
[](#cb3-11)}
[](#cb3-12)
[](#cb3-13)// 在指定区域查找所有白色块（去重）
[](#cb3-14)string colorList = "[{\"StartColor\": \"FFFFFF\", \"EndColor\": \"FFFFFF\", \"Type\": 0}]";
[](#cb3-15)long result = FindColorBlockList(ola, 100, 100, 200, 200, colorList, 5, 10, 10, 1);
[](#cb3-16)if (result != 0) {
[](#cb3-17)    printf("找到白色块列表：%s\n", result);
[](#cb3-18)    FreeStringPtr(ola, result);
[](#cb3-19)} else {
[](#cb3-20)    printf("未找到白色块\n");
[](#cb3-21)}
```

### 返回值

字符串: 返回识别到的颜色块列表的JSON字符串，格式如下：

```
[](#cb4-1)[
[](#cb4-2)  {
[](#cb4-3)    "x": 1,
[](#cb4-4)    "y": 2
[](#cb4-5)  },
[](#cb4-6)  {
[](#cb4-7)    "x": 2,
[](#cb4-8)    "y": 1
[](#cb4-9)  }
[](#cb4-10)]
```

### 注意事项

- 颜色范围使用RRGGBB格式，每个通道单独计算范围

- 支持ARGB模式，如#FFFFFFFF

- 颜色匹配类型说明：

0: 正常匹配，保留在颜色范围内的像素

- 1: 反色匹配，保留在颜色范围外的像素

- 2: 正常交集匹配，保留在颜色范围内的像素取交集

- 3: 反色交集匹配，保留在颜色范围外的像素取交集

- 当x1,y1,x2,y2都传0时，会查找整个窗口客户区

- 返回的坐标是相对于窗口客户区的坐标

- count参数决定了颜色块中需要匹配的最小像素数量

- width和height参数决定了颜色块的大小

- type参数可以控制是否对结果进行去重处理

- 颜色范围越大，匹配的像素点越多，但可能会影响查找精度

- 如果区域内符合条件的点较多，返回的JSON字符串可能会很长，请注意内存使用

- DLL调用返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

---

# 查找指定区域内的所有颜色块
- FindColorBlockListEx

### 函数简介

在绑定窗口中查找符合指定颜色范围的所有颜色块，支持去重与方向优先策略。

### 接口名称

```
FindColorBlockListEx
```

### DLL调用

```
long FindColorBlockListEx(int64_t instance, int32_t x1, int32_t y1, int32_t x2, int32_t y2,
string colorList, int32_t count, int32_t width, int32_t height,
int32_t type, int32_t dir)
```

#### 参数定义

- `instance` (长整型数): OLAPlug对象指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 生成

- `x1`/`y1`/`x2`/`y2`
(整型数): 搜索区域（全0为整个客户区）

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `count` (整型数): 色块最小匹配像素数量

- `width` (整型数): 颜色块的宽度，单位为像素。

- `height` (整型数): 颜色块的高度，单位为像素。

- `type` (整型数): 0 不重复，1 重复

- `dir` (整型数): 查找方向

0: 左→右，上→下

- 1: 左→右，下→上

- 2: 右→左，上→下

- 3: 右→左，下→上

- 4: 从中心向外

- 5: 上→下，左→右

- 6: 上→下，右→左

- 7: 下→上，左→右

- 8: 下→上，右→左

#### 返回值

- 返回JSON字符串指针，形如：`[{"x":1,"y":2},{"x":2,"y":1}]`；未找到返回空指针

- 使用完需调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放

#### 示例

```
[](#cb3-1)long json_ptr = FindColorBlockListEx(ola, 0, 0, 0, 0, color_json, 10, 20, 20, 0, 0);
[](#cb3-2)if (json_ptr) {
[](#cb3-3)    printf("%s\n", (char*)json_ptr);
[](#cb3-4)    FreeStringPtr(ola, json_ptr);
[](#cb3-5)}
```

---

# 查找指定区域内的所有颜色块
- FindColorBlockListPtr

### 函数简介

查找指定图像内符合指定颜色范围的所有颜色块坐标点

**ColorModel:**

颜色每个通道单独计算范围，如颜色范围位3278FA，6496FF，实际对应R(50~100)
G(120 ~150) B(250 ~255)

支持ARGB模式如#FFFFFFFF

支持反色模式，交集并集查询颜色 - 0: 正常匹配，保留在颜色范围内的像素
- 1: 反色匹配，保留在颜色范围外的像素 - 2:
正常交集匹配，保留在颜色范围内的像素取交集 - 3:
反色交集匹配，保留在颜色范围外的像素取交集 如{“StartColor”: “3278FA”,
“EndColor”: “6496FF”,“Type”:0}

### 接口名称

```
FindColorBlockListPtr
```

### DLL调用

```
long FindColorBlockListPtr(long ola, long image_ptr, string colors, int min_count, int block_width, int block_height, int dedup)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `image_ptr` (长整型数): 要搜索的图片句柄。

- `colors` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `min_count` (整型数):
在指定宽高的颜色块中，符合颜色条件的最小像素数量。

- `block_width` (整型数): 颜色块的宽度，单位为像素。

- `block_height` (整型数): 颜色块的高度，单位为像素。

- `dedup` (整型数): 是否去重：

0: 不去重

- 1: 去重

### 返回值

字符串:

```
[{"x":1,y:"2"},{"x":2,y:"1"}]
```

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 查找指定区域内的所有颜色块
- FindColorBlockListPtrEx

### 函数简介

在内存图像中查找符合指定颜色范围的所有颜色块，支持去重与方向优先策略。

### 接口名称

```
FindColorBlockListPtrEx
```

### DLL调用

```
long FindColorBlockListPtrEx(int64_t instance, int64_t ptr, string colorList,
int32_t count, int32_t width, int32_t height,
int32_t type, int32_t dir)
```

#### 参数定义

- `instance` (长整型数): OLAPlug对象指针

- `ptr` (长整型数): 图像句柄

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `count` (整型数): 色块最小匹配像素数量

- `width` (整型数): 颜色块的宽度，单位为像素。

- `height` (整型数): 颜色块的高度，单位为像素。

- `type` (整型数): 0 不重复，1 重复

- `dir` (整型数): 查找方向

0: 左→右，上→下

- 1: 左→右，下→上

- 2: 右→左，上→下

- 3: 右→左，下→上

- 4: 从中心向外

- 5: 上→下，左→右

- 6: 上→下，右→左

- 7: 下→上，左→右

- 8: 下→上，右→左

#### 返回值

- 返回JSON字符串指针；未找到返回空指针

- 使用完需调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放

#### 示例

```
[](#cb3-1)long json_ptr = FindColorBlockListPtrEx(ola, image_ptr, color_json, 5, 10, 10, 1, 4);
[](#cb3-2)if (json_ptr) {
[](#cb3-3)    printf("%s\n", (char*)json_ptr);
[](#cb3-4)    FreeStringPtr(ola, json_ptr);
[](#cb3-5)}
```

---

# 查找指定区域内的颜色块
- FindColorBlock

### 函数简介

查找指定区域内符合指定颜色范围的第一个颜色块坐标点。此函数可以在指定区域内搜索符合特定颜色范围的第一个颜色块，并返回其左上角坐标。适用于需要查找特定颜色区域的场景，如UI元素定位、图像特征识别等。

**ColorModel**:

颜色每个通道单独计算范围，如颜色范围位3278FA，6496FF，实际对应R(50~100)
G(120 ~150) B(250 ~255)

包含下限(>= color1) 包含上限(<= color2)

支持ARGB模式如#FFFFFFFF

支持反色模式，交集并集查询颜色 - 0: 正常匹配，保留在颜色范围内的像素
- 1: 反色匹配，保留在颜色范围外的像素 - 2:
正常交集匹配，保留在颜色范围内的像素取交集 - 3:
反色交集匹配，保留在颜色范围外的像素取交集 如{“StartColor”: “3278FA”,
“EndColor”: “6496FF”,“Type”:0}

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

返回数据为相对窗口坐标

### 接口名称

```
FindColorBlock
```

### DLL调用

```
int FindColorBlock(long ola, int x1, int y1, int x2, int y2, string colorList, int count, int width, int height, int* x, int* y)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `count` (整型数):
在宽度为width,高度为height的颜色块中，符合color颜色的最小数量

- `width` (整型数): 色块宽度

- `height` (整型数): 色块高度

- `x` (整型数指针): 返回颜色坐标X坐标

- `y` (整型数指针): 返回颜色坐标Y坐标

#### 示例:

```
[](#cb3-1)// 在窗口客户区查找颜色块
[](#cb3-2)int x = 0, y = 0;
[](#cb3-3)string colorList = "[{\"StartColor\": \"3278FA\", \"EndColor\": \"6496FF\", \"Type\": 0}]";
[](#cb3-4)int ret = FindColorBlock(ola, 0, 0, 0, 0, colorList, 10, 20, 20, &x, &y);
[](#cb3-5)if (ret == 1) {
[](#cb3-6)    printf("找到颜色块，左上角坐标：(%d, %d)\n", x, y);
[](#cb3-7)} else {
[](#cb3-8)    printf("未找到颜色块\n");
[](#cb3-9)}
[](#cb3-10)
[](#cb3-11)// 在指定区域查找颜色块
[](#cb3-12)int x = 0, y = 0;
[](#cb3-13)string colorList = "[{\"StartColor\": \"FFFFFF\", \"EndColor\": \"FFFFFF\", \"Type\": 0}]";
[](#cb3-14)int ret = FindColorBlock(ola, 100, 100, 200, 200, colorList, 5, 10, 10, &x, &y);
[](#cb3-15)if (ret == 1) {
[](#cb3-16)    printf("找到白色块，左上角坐标：(%d, %d)\n", x, y);
[](#cb3-17)} else {
[](#cb3-18)    printf("未找到白色块\n");
[](#cb3-19)}
```

### 返回值

整型数: - 0: 失败，未找到符合条件的颜色块 - 1:
成功，找到符合条件的颜色块

### 注意事项

- 颜色范围使用RRGGBB格式，每个通道单独计算范围

- 支持ARGB模式，如#FFFFFFFF

- 颜色匹配类型说明：

0: 正常匹配，保留在颜色范围内的像素

- 1: 反色匹配，保留在颜色范围外的像素

- 2: 正常交集匹配，保留在颜色范围内的像素取交集

- 3: 反色交集匹配，保留在颜色范围外的像素取交集

- 当x1,y1,x2,y2都传0时，会查找整个窗口客户区

- 返回的坐标是相对于窗口客户区的坐标

- count参数决定了颜色块中需要匹配的最小像素数量

- width和height参数决定了颜色块的大小

- 颜色范围越大，匹配的像素点越多，但可能会影响查找精度

- 如果区域内符合条件的点较多，建议适当调整count、width和height参数

---

# 查找指定区域内的颜色块 -
FindColorBlockEx

### 函数简介

在绑定窗口中查找符合指定颜色范围的第一个颜色块中心点，支持方向优先策略。

### 接口名称

```
FindColorBlockEx
```

### DLL调用

```
int32_t FindColorBlockEx(int64_t instance, int32_t x1, int32_t y1, int32_t x2, int32_t y2,
string colorList, int32_t count, int32_t width, int32_t height,
int32_t dir, int32_t* x, int32_t* y)
```

#### 参数定义

- `instance` (长整型数): OLAPlug对象指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 生成

- `x1`/`y1`/`x2`/`y2`
(整型数): 搜索区域左上角与右下角坐标（全0为整个客户区）

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `count` (整型数): 在
`width`×`height`
的色块中，需满足颜色条件的最小像素数量

- `width` (整型数): 颜色块的宽度，单位为像素。

- `height` (整型数): 颜色块的高度，单位为像素。

- `dir` (整型数): 查找方向

0: 左→右，上→下

- 1: 左→右，下→上

- 2: 右→左，上→下

- 3: 右→左，下→上

- 4: 从中心向外

- 5: 上→下，左→右

- 6: 上→下，右→左

- 7: 下→上，左→右

- 8: 下→上，右→左

- `x` (整型数指针): 返回找到的颜色块左上角的X坐标。

- `y` (整型数指针): 返回找到的颜色块左上角的Y坐标。

#### 示例

```
[](#cb3-1)int x = 0, y = 0;
[](#cb3-2)string colorList = "[{\"StartColor\":\"3278FA\",\"EndColor\":\"6496FF\",\"Type\":0}]";
[](#cb3-3)int32_t ret = FindColorBlockEx(ola, 0, 0, 0, 0, colorList, 10, 20, 20, 0, &x, &y);
```

### 返回值

- 0: 未找到

- 1: 找到

### 注意事项

- 颜色范围为 RRGGBB，支持 ARGB（如 #FFFFFFFF）与反色/交集模式

- 坐标返回为相对窗口客户区

---

# 查找指定区域内的颜色块 -
FindColorBlockPtr

### 函数简介

查找指定图像内符合指定颜色范围的第一个颜色块坐标点

**ColorModel**:

颜色每个通道单独计算范围，如颜色范围位3278FA，6496FF，实际对应R(50~100)
G(120 ~150) B(250 ~255)

包含下限(>= color1) 包含上限(<= color2)

支持ARGB模式如#FFFFFFFF

支持反色模式，交集并集查询颜色 - 0: 正常匹配，保留在颜色范围内的像素
- 1: 反色匹配，保留在颜色范围外的像素 - 2:
正常交集匹配，保留在颜色范围内的像素取交集 - 3:
反色交集匹配，保留在颜色范围外的像素取交集 如{“StartColor”: “3278FA”,
“EndColor”: “6496FF”,“Type”:0}

### 接口名称

```
FindColorBlockPtr
```

### DLL调用

```
int FindColorBlockPtr(long ola, long image_ptr, string colors, int min_count, int block_width, int block_height, int* x, int* y)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `image_ptr` (长整型数): 要搜索的图片句柄。

- `colors` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `min_count` (整型数):
在指定宽高的颜色块中，符合颜色条件的最小像素数量。

- `block_width` (整型数): 颜色块的宽度，单位为像素。

- `block_height` (整型数): 颜色块的高度，单位为像素。

- `x` (整型数指针): 返回找到的颜色块左上角的X坐标。

- `y` (整型数指针): 返回找到的颜色块左上角的Y坐标。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 查找指定区域内的颜色块
- FindColorBlockPtrEx

### 函数简介

在内存图像中查找符合指定颜色范围的第一个颜色块中心点，支持方向优先策略。

### 接口名称

```
FindColorBlockPtrEx
```

### DLL调用

```
int32_t FindColorBlockPtrEx(int64_t instance, int64_t ptr, string colorList,
int32_t count, int32_t width, int32_t height, int32_t dir,
int32_t* x, int32_t* y)
```

#### 参数定义

- `instance` (长整型数): OLAPlug对象指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 生成

- `ptr` (长整型数): 图像句柄

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `count` (整型数): 在
`width`×`height`
的色块中，需满足颜色条件的最小像素数量

- `width` (整型数): 颜色块的宽度，单位为像素。

- `height` (整型数): 颜色块的高度，单位为像素。

- `dir` (整型数): 查找方向

0: 左→右，上→下

- 1: 左→右，下→上

- 2: 右→左，上→下

- 3: 右→左，下→上

- 4: 从中心向外

- 5: 上→下，左→右

- 6: 上→下，右→左

- 7: 下→上，左→右

- 8: 下→上，右→左

- `x` (整型数指针): 返回找到的颜色块左上角的X坐标。

- `y` (整型数指针): 返回找到的颜色块左上角的Y坐标。

#### 示例

```
[](#cb3-1)int x = 0, y = 0;
[](#cb3-2)string colorList = "[{\"StartColor\":\"FFFFFF\",\"EndColor\":\"FFFFFF\",\"Type\":0}]";
[](#cb3-3)int32_t ret = FindColorBlockPtrEx(ola, image_ptr, colorList, 5, 10, 10, 4, &x, &y);
```

### 返回值

- 0: 未找到

- 1: 找到

---

# 查找指定颜色范围坐标 -
FindMultiColor

### 函数简介

查找指定区域内符合指定颜色范围的第一个坐标点。此函数可以在指定区域内搜索符合特定颜色范围的第一个像素点，并返回其坐标。支持多种搜索方向，可以灵活应用于图像识别、自动化测试等场景。

**ColorModel:**

颜色每个通道单独计算范围，如颜色范围位3278FA，6496FF，实际对应R(50~100)
G(120 ~150) B(250 ~255)

包含下限(>= color1) 包含上限(<= color2)

支持ARGB模式如#FFFFFFFF

支持反色模式，交集并集查询颜色 - 0: 正常匹配，保留在颜色范围内的像素
- 1: 反色匹配，保留在颜色范围外的像素 - 2:
正常交集匹配，保留在颜色范围内的像素取交集 - 3:
反色交集匹配，保留在颜色范围外的像素取交集 如{“StartColor”: “3278FA”,
“EndColor”: “6496FF”,“Type”:0}

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

返回数据为相对窗口坐标

### 接口名称

```
FindMultiColor
```

### DLL调用

```
int FindMultiColor(long ola, int x1, int y1, int x2, int y2, string colorList, string pointColorList, int dir, int* x, int* y)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `pointColorList`(字符串):
点阵颜色列表，支持JSON格式或简化字符串格式，格式说明见 [点阵颜色列表格式说明
-
PointColorListFormat](/图像处理/点阵颜色列表格式说明%20-%20PointColorListFormat.html)。JSON格式示例：`[{"Point":{"X":0,"Y":2},"Colors":[{"StartColor":"#0A7497","EndColor":"#0A7497","Type":0}]}]`；简化格式示例：`aabbcc|aaffaa-101010,-5|-3|123456-050607|454545-303030|565656`

- `dir` (整型数): 查找方向

0: 从左到右,从上到下

- 1: 从左到右,从下到上

- 2: 从右到左,从上到下

- 3: 从右到左,从下到上

- 4: 从中心往外查找

- 5: 从上到下,从左到右

- 6: 从上到下,从右到左

- 7: 从下到上,从左到右

- 8: 从下到上,从右到左

- `x` (整型数指针): 返回颜色坐标X坐标

- `y` (整型数指针): 返回颜色坐标Y坐标

#### 示例:

```
[](#cb3-1)// 在窗口客户区查找指定颜色
[](#cb3-2)int x = 0, y = 0;
[](#cb3-3)string colorList = "[{\"StartColor\": \"3278FA\", \"EndColor\": \"6496FF\", \"Type\": 0}]";
[](#cb3-4)int ret = FindMultiColor(ola, 0, 0, 0, 0, colorList, 0, &x, &y);
[](#cb3-5)if (ret == 1) {
[](#cb3-6)    printf("找到颜色点，坐标：(%d, %d)\n", x, y);
[](#cb3-7)} else {
[](#cb3-8)    printf("未找到颜色点\n");
[](#cb3-9)}
[](#cb3-10)
[](#cb3-11)// 在指定区域查找颜色（从中心往外查找）
[](#cb3-12)int x = 0, y = 0;
[](#cb3-13)string colorList = "[{\"StartColor\": \"FFFFFF\", \"EndColor\": \"FFFFFF\", \"Type\": 0}]";
[](#cb3-14)int ret = FindMultiColor(ola, 100, 100, 200, 200, colorList, 4, &x, &y);
[](#cb3-15)if (ret == 1) {
[](#cb3-16)    printf("找到白色点，坐标：(%d, %d)\n", x, y);
[](#cb3-17)} else {
[](#cb3-18)    printf("未找到白色点\n");
[](#cb3-19)}
```

### 返回值

整型数: - 0: 失败，未找到符合条件的颜色点 - 1:
成功，找到符合条件的颜色点

### 注意事项

- 颜色范围使用RRGGBB格式，每个通道单独计算范围

- 支持ARGB模式，如#FFFFFFFF

- 颜色匹配类型说明：

0: 正常匹配，保留在颜色范围内的像素

- 1: 反色匹配，保留在颜色范围外的像素

- 2: 正常交集匹配，保留在颜色范围内的像素取交集

- 3: 反色交集匹配，保留在颜色范围外的像素取交集

- 当x1,y1,x2,y2都传0时，会查找整个窗口客户区

- 返回的坐标是相对于窗口客户区的坐标

- 不同的查找方向会影响查找效率和结果，建议根据实际需求选择合适的查找方向

- 颜色范围越大，匹配的像素点越多，但可能会影响查找精度

- 使用反色模式时，会查找不在指定颜色范围内的点

- 使用交集模式时，需要同时满足所有颜色条件

- 使用并集模式时，满足任一颜色条件即可

---

# 查找指定颜色范围坐标 -
FindMultiColorFromPtr

### 函数简介

查找图片指定颜色范围的第一个坐标点。此函数可以在指定的图片中搜索符合特定颜色范围的第一个像素点，并返回其坐标。支持多种搜索方向，可以灵活应用于图像识别、自动化测试等场景。

**ColorModel:**

颜色每个通道单独计算范围，如颜色范围位3278FA，6496FF，实际对应R(50~100)
G(120 ~150) B(250 ~255)

包含下限(>= color1) 包含上限(<= color2)

支持ARGB模式如#FFFFFFFF

支持反色模式，交集并集查询颜色 - 0: 正常匹配，保留在颜色范围内的像素
- 1: 反色匹配，保留在颜色范围外的像素 - 2:
正常交集匹配，保留在颜色范围内的像素取交集 - 3:
反色交集匹配，保留在颜色范围外的像素取交集 如{“StartColor”: “3278FA”,
“EndColor”: “6496FF”,“Type”:0}

### 接口名称

```
FindMultiColorFromPtr
```

### DLL调用

```
int FindMultiColorFromPtr(long ola, long imgPtr, string colorList, string pointColorList, int dir, int* x, int* y)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `imgPtr` (长整型数): OLAImage对象的地址

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `pointColorList`(字符串):
点阵颜色列表，支持JSON格式或简化字符串格式，格式说明见 [点阵颜色列表格式说明
-
PointColorListFormat](/图像处理/点阵颜色列表格式说明%20-%20PointColorListFormat.html)。JSON格式示例：`[{"Point":{"X":0,"Y":2},"Colors":[{"StartColor":"#0A7497","EndColor":"#0A7497","Type":0}]}]`；简化格式示例：`aabbcc|aaffaa-101010,-5|-3|123456-050607|454545-303030|565656`

- `dir` (整型数): 查找方向

0: 从左到右,从上到下

- 1: 从左到右,从下到上

- 2: 从右到左,从上到下

- 3: 从右到左,从下到上

- 4: 从中心往外查找

- 5: 从上到下,从左到右

- 6: 从上到下,从右到左

- 7: 从下到上,从左到右

- 8: 从下到上,从右到左

- `x` (整型数指针): 返回颜色坐标X坐标

- `y` (整型数指针): 返回颜色坐标Y坐标

#### 示例:

```
[](#cb3-1)// 在图片中查找指定颜色
[](#cb3-2)int x = 0, y = 0;
[](#cb3-3)string colorList = "[{\"StartColor\": \"3278FA\", \"EndColor\": \"6496FF\", \"Type\": 0}]";
[](#cb3-4)int ret = FindMultiColorFromPtr(ola, imagePtr, colorList, 0, &x, &y);
[](#cb3-5)if (ret == 1) {
[](#cb3-6)    printf("找到颜色点，坐标：(%d, %d)\n", x, y);
[](#cb3-7)} else {
[](#cb3-8)    printf("未找到颜色点\n");
[](#cb3-9)}
[](#cb3-10)
[](#cb3-11)// 在图片中查找颜色（从中心往外查找）
[](#cb3-12)int x = 0, y = 0;
[](#cb3-13)string colorList = "[{\"StartColor\": \"FFFFFF\", \"EndColor\": \"FFFFFF\", \"Type\": 0}]";
[](#cb3-14)int ret = FindMultiColorFromPtr(ola, imagePtr, colorList, 4, &x, &y);
[](#cb3-15)if (ret == 1) {
[](#cb3-16)    printf("找到白色点，坐标：(%d, %d)\n", x, y);
[](#cb3-17)} else {
[](#cb3-18)    printf("未找到白色点\n");
[](#cb3-19)}
```

### 返回值

整型数: - 0: 失败，未找到符合条件的颜色点 - 1:
成功，找到符合条件的颜色点

### 注意事项

- 颜色范围使用RRGGBB格式，每个通道单独计算范围

- 支持ARGB模式，如#FFFFFFFF

- 颜色匹配类型说明：

0: 正常匹配，保留在颜色范围内的像素

- 1: 反色匹配，保留在颜色范围外的像素

- 2: 正常交集匹配，保留在颜色范围内的像素取交集

- 3: 反色交集匹配，保留在颜色范围外的像素取交集

- 返回的坐标是相对于图片的坐标

- 不同的查找方向会影响查找效率和结果，建议根据实际需求选择合适的查找方向

- 颜色范围越大，匹配的像素点越多，但可能会影响查找精度

- 使用反色模式时，会查找不在指定颜色范围内的点

- 使用交集模式时，需要同时满足所有颜色条件

- 使用并集模式时，满足任一颜色条件即可

- 确保传入的图片指针是有效的，否则可能导致程序崩溃

---

# 查找指定颜色范围坐标
- FindMultiColorList

### 函数简介

查找指定区域内符合指定颜色范围的所有颜色点。此函数可以在指定区域内搜索所有符合特定颜色范围的像素点，并返回它们的坐标列表。适用于需要批量查找颜色点的场景，如区域分析、图像特征提取等。

### 接口名称

```
FindMultiColorList
```

### DLL调用

```
long FindMultiColorList(long ola, int x1, int y1, int x2, int y2, string colorList, string pointColorList)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `pointColorList`(字符串):
点阵颜色列表，支持JSON格式或简化字符串格式，格式说明见 [点阵颜色列表格式说明
-
PointColorListFormat](/图像处理/点阵颜色列表格式说明%20-%20PointColorListFormat.html)。JSON格式示例：`[{"Point":{"X":0,"Y":2},"Colors":[{"StartColor":"#0A7497","EndColor":"#0A7497","Type":0}]}]`；简化格式示例：`aabbcc|aaffaa-101010,-5|-3|123456-050607|454545-303030|565656`

#### 示例:

```
[](#cb3-1)// 在窗口客户区查找所有指定颜色点
[](#cb3-2)string colorList = "[{\"StartColor\": \"3278FA\", \"EndColor\": \"6496FF\", \"Type\": 0}]";
[](#cb3-3)long result = FindMultiColorList(ola, 0, 0, 0, 0, colorList);
[](#cb3-4)if (result != 0) {
[](#cb3-5)    // 解析返回的JSON字符串
[](#cb3-6)    // 注意：使用完后需要调用FreeStringPtr释放内存
[](#cb3-7)    printf("找到颜色点列表：%s\n", result);
[](#cb3-8)    FreeStringPtr(ola, result);
[](#cb3-9)} else {
[](#cb3-10)    printf("未找到颜色点\n");
[](#cb3-11)}
[](#cb3-12)
[](#cb3-13)// 在指定区域查找所有白色点
[](#cb3-14)string colorList = "[{\"StartColor\": \"FFFFFF\", \"EndColor\": \"FFFFFF\", \"Type\": 0}]";
[](#cb3-15)long result = FindMultiColorList(ola, 100, 100, 200, 200, colorList);
[](#cb3-16)if (result != 0) {
[](#cb3-17)    printf("找到白色点列表：%s\n", result);
[](#cb3-18)    FreeStringPtr(ola, result);
[](#cb3-19)} else {
[](#cb3-20)    printf("未找到白色点\n");
[](#cb3-21)}
```

### 返回值

字符串: 返回识别到的坐标点列表的JSON字符串，格式如下：

```
[](#cb4-1)[
[](#cb4-2)  {
[](#cb4-3)    "x": 1,
[](#cb4-4)    "y": 2
[](#cb4-5)  },
[](#cb4-6)  {
[](#cb4-7)    "x": 2,
[](#cb4-8)    "y": 1
[](#cb4-9)  }
[](#cb4-10)]
```

### 注意事项

- 颜色范围使用RRGGBB格式，每个通道单独计算范围

- 支持ARGB模式，如#FFFFFFFF

- 颜色匹配类型说明：

0: 正常匹配，保留在颜色范围内的像素

- 1: 反色匹配，保留在颜色范围外的像素

- 2: 正常交集匹配，保留在颜色范围内的像素取交集

- 3: 反色交集匹配，保留在颜色范围外的像素取交集

- 当x1,y1,x2,y2都传0时，会查找整个窗口客户区

- 返回的坐标是相对于窗口客户区的坐标

- 返回的JSON字符串需要解析后才能使用

- DLL调用返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

- 颜色范围越大，匹配的像素点越多，但可能会影响查找精度

- 如果区域内符合条件的点较多，返回的JSON字符串可能会很长，请注意内存使用

- 使用反色模式时，会查找不在指定颜色范围内的点

- 使用交集模式时，需要同时满足所有颜色条件

- 使用并集模式时，满足任一颜色条件即可

---

# 查找指定颜色范围坐标
- FindMultiColorListFromPtr

### 函数简介

查找图片符合指定颜色范围的所有颜色点。此函数可以在指定的图片中搜索所有符合特定颜色范围的像素点，并返回它们的坐标列表。适用于需要批量查找颜色点的场景，如图像分析、特征提取等。

**ColorModel:**

颜色每个通道单独计算范围，如颜色范围位3278FA，6496FF，实际对应R(50~100)
G(120 ~150) B(250 ~255)

包含下限(>= color1) 包含上限(<= color2)

支持ARGB模式如#FFFFFFFF

支持反色模式，交集并集查询颜色 - 0: 正常匹配，保留在颜色范围内的像素
- 1: 反色匹配，保留在颜色范围外的像素 - 2:
正常交集匹配，保留在颜色范围内的像素取交集 - 3:
反色交集匹配，保留在颜色范围外的像素取交集 如{“StartColor”: “3278FA”,
“EndColor”: “6496FF”,“Type”:0}

### 接口名称

```
FindMultiColorListFromPtr
```

### DLL调用

```
long FindMultiColorListFromPtr(long ola, long imgPtr, string colorList, string pointColorList)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `imgPtr` (长整型数): OLAImage对象的地址

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `pointColorList`(字符串):
点阵颜色列表，支持JSON格式或简化字符串格式，格式说明见 [点阵颜色列表格式说明
-
PointColorListFormat](/图像处理/点阵颜色列表格式说明%20-%20PointColorListFormat.html)。JSON格式示例：`[{"Point":{"X":0,"Y":2},"Colors":[{"StartColor":"#0A7497","EndColor":"#0A7497","Type":0}]}]`；简化格式示例：`aabbcc|aaffaa-101010,-5|-3|123456-050607|454545-303030|565656`

#### 示例:

```
[](#cb3-1)// 在图片中查找所有指定颜色点
[](#cb3-2)string colorList = "[{\"StartColor\": \"3278FA\", \"EndColor\": \"6496FF\", \"Type\": 0}]";
[](#cb3-3)long result = FindMultiColorListFromPtr(ola, imagePtr, colorList);
[](#cb3-4)if (result != 0) {
[](#cb3-5)    // 解析返回的JSON字符串
[](#cb3-6)    // 注意：使用完后需要调用FreeStringPtr释放内存
[](#cb3-7)    printf("找到颜色点列表：%s\n", result);
[](#cb3-8)    FreeStringPtr(ola, result);
[](#cb3-9)} else {
[](#cb3-10)    printf("未找到颜色点\n");
[](#cb3-11)}
[](#cb3-12)
[](#cb3-13)// 在图片中查找所有白色点
[](#cb3-14)string colorList = "[{\"StartColor\": \"FFFFFF\", \"EndColor\": \"FFFFFF\", \"Type\": 0}]";
[](#cb3-15)long result = FindMultiColorListFromPtr(ola, imagePtr, colorList);
[](#cb3-16)if (result != 0) {
[](#cb3-17)    printf("找到白色点列表：%s\n", result);
[](#cb3-18)    FreeStringPtr(ola, result);
[](#cb3-19)} else {
[](#cb3-20)    printf("未找到白色点\n");
[](#cb3-21)}
```

### 返回值

字符串: 返回识别到的坐标点列表的JSON字符串，格式如下：

```
[](#cb4-1)[
[](#cb4-2)  {
[](#cb4-3)    "x": 1,
[](#cb4-4)    "y": 2
[](#cb4-5)  },
[](#cb4-6)  {
[](#cb4-7)    "x": 2,
[](#cb4-8)    "y": 1
[](#cb4-9)  }
[](#cb4-10)]
```

### 注意事项

- 颜色范围使用RRGGBB格式，每个通道单独计算范围

- 支持ARGB模式，如#FFFFFFFF

- 颜色匹配类型说明：

0: 正常匹配，保留在颜色范围内的像素

- 1: 反色匹配，保留在颜色范围外的像素

- 2: 正常交集匹配，保留在颜色范围内的像素取交集

- 3: 反色交集匹配，保留在颜色范围外的像素取交集

- 返回的坐标是相对于图片的坐标

- 返回的JSON字符串需要解析后才能使用

- DLL调用返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

- 颜色范围越大，匹配的像素点越多，但可能会影响查找精度

- 如果图片中符合条件的点较多，返回的JSON字符串可能会很长，请注意内存使用

- 使用反色模式时，会查找不在指定颜色范围内的点

- 使用交集模式时，需要同时满足所有颜色条件

- 使用并集模式时，满足任一颜色条件即可

- 确保传入的图片指针是有效的，否则可能导致程序崩溃

---

# 查找符合的颜色 - FindColor

### 函数简介

查找指定区域内符合指定颜色范围的第一个坐标点。此函数可以在指定区域内搜索符合特定颜色范围的第一个像素点，并返回其坐标。支持多种搜索方向，可以灵活应用于图像识别、自动化测试等场景。

每个通道单独计算范围，如颜色范围位3278FA，6496FF，实际对应R(50~100)
G(120 ~150) B(250 ~255)

包含下限(>= color1) 包含上限(<= color2)

支持ARGB模式如#FFFFFFFF

x1,y1,x2,y2传0,0,0,0 为查找绑定窗口整个客户区

返回数据为相对窗口坐标

### 接口名称

```
FindColor
```

### DLL调用

```
int FindColor(long ola, int x1,int y1,int x2,int y2,string color1,string color2,int dir,int* intX,int* intY)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 区域的左上X坐标

- `y1` (整型数): 区域的左上Y坐标

- `x2` (整型数): 区域的右下X坐标

- `y2` (整型数): 区域的右下Y坐标

- `color1` (字符串): 颜色起始范围，颜色格式 RRGGBB

- `color2` (字符串): 颜色结束范围，颜色格式 RRGGBB

- `dir` (整型数): 查找方向：

0: 从左到右,从上到下

- 1: 从左到右,从下到上

- 2: 从右到左,从上到下

- 3: 从右到左,从下到上

- 4: 从中心往外查找

- 5: 从上到下,从左到右

- 6: 从上到下,从右到左

- 7: 从下到上,从左到右

- 8: 从下到上,从右到左

- `intX` (整型数指针): 返回X坐标

- `intY` (整型数指针): 返回Y坐标

#### 示例:

```
[](#cb3-1)// 在窗口客户区查找指定颜色
[](#cb3-2)int x = 0, y = 0;
[](#cb3-3)int ret = FindColor(ola, 0, 0, 0, 0, "057093", "057093", 0, &x, &y);
[](#cb3-4)if (ret == 1) {
[](#cb3-5)    printf("找到颜色点，坐标：(%d, %d)\n", x, y);
[](#cb3-6)} else {
[](#cb3-7)    printf("未找到颜色点\n");
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)// 在指定区域查找颜色
[](#cb3-11)int x = 0, y = 0;
[](#cb3-12)int ret = FindColor(ola, 100, 100, 200, 200, "FFFFFF", "FFFFFF", 4, &x, &y);
[](#cb3-13)if (ret == 1) {
[](#cb3-14)    printf("找到白色点，坐标：(%d, %d)\n", x, y);
[](#cb3-15)} else {
[](#cb3-16)    printf("未找到白色点\n");
[](#cb3-17)}
```

### 返回值

整型数: - 0: 失败，未找到符合条件的颜色点 - 1:
成功，找到符合条件的颜色点

### 注意事项

- 颜色范围使用RRGGBB格式，每个通道单独计算范围

- 支持ARGB模式，如#FFFFFFFF

- 当x1,y1,x2,y2都传0时，会查找整个窗口客户区

- 返回的坐标是相对于窗口客户区的坐标

- 不同的查找方向会影响查找效率和结果，建议根据实际需求选择合适的查找方向

- 颜色范围越大，匹配的像素点越多，但可能会影响查找精度

---

# 查找符合的颜色 - FindColorEx

### 函数简介

在绑定窗口中查找符合指定颜色模型的第一个坐标点。此函数在指定区域内搜索符合颜色模型的数据并返回首个匹配坐标，支持多种搜索方向，可用于图像识别与自动化场景。

**ColorModel:**

颜色每个通道单独计算范围，如颜色范围位 3278FA，6496FF，实际对应
R(50~100) / G(120~150) / B(250~255)。

包含下限(>= StartColor) 与上限(<= EndColor)；支持 ARGB 形式（如
`#FFFFFFFF`）。

支持反色/交集/并集等模式（按实现为准），示例：

```
{"StartColor":"3278FA","EndColor":"6496FF","Type":0}
```

`x1,y1,x2,y2` 传 `0,0,0,0`
为查找绑定窗口整个客户区；返回坐标为相对绑定窗口客户区坐标。

### 接口名称

```
FindColorEx
```

### DLL调用

```
int FindColorEx(long ola, int x1, int y1, int x2, int y2, string colorJson, int dir, int* x, int* y)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 生成。

- `x1` (整型数): 区域左上角 X 坐标

- `y1` (整型数): 区域左上角 Y 坐标

- `x2` (整型数): 区域右下角 X 坐标

- `y2` (整型数): 区域右下角 Y 坐标

- `colorJson` (字符串):
颜色模型配置字符串，用于限定颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `dir` (整型数): 查找方向

0: 从左到右,从上到下

- 1: 从左到右,从下到上

- 2: 从右到左,从上到下

- 3: 从右到左,从下到上

- 4: 从中心往外查找

- 5: 从上到下,从左到右

- 6: 从上到下,从右到左

- 7: 从下到上,从左到右

- 8: 从下到上,从右到左

- `x` (整型数指针): 返回匹配点 X 坐标

- `y` (整型数指针): 返回匹配点 Y 坐标

#### 示例:

```
[](#cb4-1)int x = 0, y = 0;
[](#cb4-2)string cj = "[{\"StartColor\":\"3278FA\",\"EndColor\":\"6496FF\",\"Type\":0}]";
[](#cb4-3)int ret = FindColorEx(ola, 0, 0, 0, 0, cj, 0, &x, &y);
[](#cb4-4)if (ret == 1) {
[](#cb4-5)    // 找到坐标 (x, y)
[](#cb4-6)}
```

### 返回值

整型数: - 0: 未找到 - 1: 找到

### 注意事项

- 当 `x1,y1,x2,y2` 全为 0 时，搜索整个绑定窗口客户区。

- 返回坐标为相对绑定窗口客户区坐标。

- 查找方向会影响效率与结果，建议根据实际需求选择合适的方向。

---

# 点阵颜色列表格式说明 -
PointColorListFormat

## 概述

`pointColorList` 点阵颜色列表用于在
`FindMultiColor`、`FindMultiColorList`
等接口中定义多个参考点的颜色信息。
本说明文档统一介绍所有支持的点阵颜色列表表示方式，接口文档只需简单引用本页即可。

## 1. JSON
格式（原有写法，完全兼容）

```
[](#cb1-1)[
[](#cb1-2)  {
[](#cb1-3)    "Point": {"X": 0, "Y": 2},
[](#cb1-4)    "Colors": [
[](#cb1-5)      {
[](#cb1-6)        "StartColor": "#0A7497",
[](#cb1-7)        "EndColor": "#0A7497",
[](#cb1-8)        "Type": 0
[](#cb1-9)      }
[](#cb1-10)    ]
[](#cb1-11)  },
[](#cb1-12)  {
[](#cb1-13)    "Point": {"X": -5, "Y": -3},
[](#cb1-14)    "Colors": [
[](#cb1-15)      {
[](#cb1-16)        "StartColor": "#123456",
[](#cb1-17)        "EndColor": "#050607",
[](#cb1-18)        "Type": 0
[](#cb1-19)      },
[](#cb1-20)      {
[](#cb1-21)        "StartColor": "#454545",
[](#cb1-22)        "EndColor": "#303030",
[](#cb1-23)        "Type": 0
[](#cb1-24)      },
[](#cb1-25)      {
[](#cb1-26)        "StartColor": "#565656",
[](#cb1-27)        "EndColor": "#565656",
[](#cb1-28)        "Type": 0
[](#cb1-29)      }
[](#cb1-30)    ]
[](#cb1-31)  }
[](#cb1-32)]
```

- `Point` 表示相对于第一个点的坐标偏移量（X, Y）

- `Colors` 数组包含该点需要匹配的颜色列表

- `StartColor` / `EndColor` 支持以下形式：

`#AARRGGBB`

- `AARRGGBB`

- `#RRGGBB`

- `RRGGBB`

- `Type` 说明：

`0`：正常匹配（保留在颜色范围内的像素）

- `1`：反色匹配（保留在颜色范围外的像素）

- `2`：正常交集匹配

- `3`：反色交集匹配

## 2. 简化字符串格式（新增）

### 基本格式

```
颜色列表1,坐标偏移X|坐标偏移Y|颜色列表2|颜色列表3|...
```

### 格式说明

- **第一个点**：直接写颜色列表，不需要坐标（默认为
0,0）

- **坐标偏移**：使用 `,X|Y`
格式，表示相对于第一个点的偏移量

`X` 为 X 坐标偏移（可为负数，如 `-5`）

- `Y` 为 Y 坐标偏移（可为负数，如 `-3`）

- **后续点**：使用 `|`
分隔，每个点包含其颜色列表

- **颜色格式**：支持以下格式（参考 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)）：

单独颜色：`RRGGBB` 或 `#RRGGBB`

- 偏色区间：`RRGGBB-DRDGDB`（基准色-偏移量）

- 多个颜色用 `|` 分隔

### 示例

#### 示例 1：简单点阵

```
aabbcc,-5|-3|123456
```

对应含义： - 第一个点（0, 0）：颜色 `aabbcc` -
第二个点（-5, -3）：颜色 `123456`

#### 示例 2：多颜色点阵

```
aabbcc|aaffaa-101010,-5|-3|123456-050607|454545-303030|565656
```

对应含义： - 第一个点（0, 0）：颜色列表 -
`aabbcc`（精确颜色） -
`aaffaa-101010`（偏色区间，基准色
`aaffaa`，允许偏移 `101010`） - 第二个点（-5,
-3）：颜色列表 - `123456-050607`（偏色区间） -
`454545-303030`（偏色区间） -
`565656`（精确颜色）

#### 示例 3：多个点

```
ff0000,10|5|00ff00,20|10|0000ff
```

对应含义： - 第一个点（0, 0）：颜色 `ff0000`（红色） -
第二个点（10, 5）：颜色 `00ff00`（绿色） - 第三个点（20,
10）：颜色 `0000ff`（蓝色）

### 格式规则

- **第一个点**：不需要坐标偏移，直接写颜色列表

- **坐标偏移格式**：`,X|Y`（逗号后跟 X
偏移，竖线后跟 Y 偏移）

- **颜色分隔**：同一点的多个颜色用 `|`
分隔

- **点分隔**：不同点之间用 `|`
分隔，但坐标偏移前用 `,` 标识

- **颜色格式**：支持单独颜色、偏色区间等（详见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)）

### 注意事项

- 坐标偏移可以为负数，表示向左或向上偏移

- 颜色格式支持所有 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html) 中定义的格式

- 简化格式相比 JSON 格式更易书写，但功能完全等价

- 建议在简单场景使用简化格式，复杂场景使用 JSON
格式以获得更好的可读性

---

# 生成二维码 - CreateQRCode

### 函数简介

生成二维码

### 接口名称

```
CreateQRCode
```

### DLL调用

```
long CreateQRCode(long ola, string str, int pixelsPerModule)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `str` (字符串): 生成二维码的字符串数据

- `pixelsPerModule` (整型数): 每个数据像素大小

#### 示例:

待补充…

### 返回值

长整型数:

OLAImage对象的地址

**注意**：图片使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口进行释放

---

# 生成二维码 - CreateQRCodeEx

### 函数简介

生成二维码

### 接口名称

```
CreateQRCodeEx
```

### DLL调用

```
long CreateQRCode(long ola, string str, int pixelsPerModule,int version, int correctionLevel, int mode, int structureNumber)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `str` (字符串): 生成二维码的字符串数据

- `pixelsPerModule` (整型数): 每个数据像素大小

- `version` (整型数): 二维码版本

- `correctionLevel` (整型数): 容错等级

CORRECT_LEVEL_L = 0,

- CORRECT_LEVEL_M = 1,

- CORRECT_LEVEL_Q = 2,

- CORRECT_LEVEL_H = 3

- `mode` (整型数): 字节编码模式

MODE_AUTO = -1,

- MODE_NUMERIC = 1, // 0b0001

- MODE_ALPHANUMERIC = 2, // 0b0010

- MODE_BYTE = 4, // 0b0100

- MODE_ECI = 7, // 0b0111

- MODE_KANJI = 8, // 0b1000

- MODE_STRUCTURED_APPEND = 3 // 0b0011

- `structureNumber` (整型数): 结构化追加的首个码索引

#### 示例:

待补充…

### 返回值

长整型数:

OLAImage对象的地址

**注意**：图片使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口进行释放

---

# 移除图片差异部分 -
RemoveImageDiff

### 函数简介

比较两张图片，移除它们之间的差异部分，将差异部分设置为透明。此函数可用于查找画面中不变的坐标点，适用于图像对比、变化检测等场景。函数会保留两张图片中完全相同的部分，将不同的部分设置为透明。

### 接口名称

```
RemoveImageDiff
```

### DLL调用

```
long RemoveImageDiff(long ola, long imgPtr1, long imgPtr2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `imgPtr1` (长整型数): 第一张图片的OLAImage对象地址

- `imgPtr2` (长整型数): 第二张图片的OLAImage对象地址

#### 示例:

```
[](#cb3-1)// 加载两张要比较的图片
[](#cb3-2)long image1 = LoadImage(ola, "image1.png");
[](#cb3-3)long image2 = LoadImage(ola, "image2.png");
[](#cb3-4)
[](#cb3-5)if (image1 != 0 && image2 != 0) {
[](#cb3-6)    // 移除差异部分
[](#cb3-7)    long resultImage = RemoveImageDiff(ola, image1, image2);
[](#cb3-8)    if (resultImage != 0) {
[](#cb3-9)        // 保存处理后的图片
[](#cb3-10)        SaveImageFromPtr(ola, resultImage, "result.png");
[](#cb3-11)
[](#cb3-12)        // 释放内存
[](#cb3-13)        FreeImagePtr(ola, resultImage);
[](#cb3-14)    }
[](#cb3-15)
[](#cb3-16)    // 释放原始图片内存
[](#cb3-17)    FreeImagePtr(ola, image1);
[](#cb3-18)    FreeImagePtr(ola, image2);
[](#cb3-19)}
```

### 返回值

长整型数: - 成功：返回处理后的OLAImage对象地址 - 失败：返回0

### 注意事项

- 两张图片必须具有相同的尺寸，否则将返回失败

- 处理后的图片中，相同的部分保持原样，不同的部分将被设置为透明

- 原始图片不会被修改，函数返回新的图片对象

- 使用完毕后必须调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
释放内存

- 建议在使用前检查图片指针的有效性

- 处理大图片时注意内存使用

- 图片比较是像素级的精确比较

- 如果需要模糊比较，请使用其他相关函数

- 建议在比较前确保两张图片的格式相同

- 透明部分可以用于后续的图像处理或坐标点提取

---

# 移除除指定颜色外的所有颜色
- RemoveOtherColors

### 函数简介

移除图像中除指定颜色范围外的所有颜色，将非指定颜色范围的像素设置为透明。此函数可用于图像处理中的颜色提取、背景去除等场景。支持多个颜色范围的指定，每个颜色范围可以设置不同的匹配类型。

### 接口名称

```
RemoveOtherColors
```

### DLL调用

```
long RemoveOtherColors(long ola, long ptr, string colorList)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `ptr` (长整型数): OLAImage对象的地址

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

#### 示例:

```
[](#cb3-1)// 定义要保留的颜色范围
[](#cb3-2)string colorList = R"([
[](#cb3-3)    {
[](#cb3-4)        "StartColor": "3278FA",
[](#cb3-5)        "EndColor": "6496FF",
[](#cb3-6)        "Type": 0
[](#cb3-7)    },
[](#cb3-8)    {
[](#cb3-9)        "StartColor": "FF0000",
[](#cb3-10)        "EndColor": "FF3333",
[](#cb3-11)        "Type": 1
[](#cb3-12)    }
[](#cb3-13)])";
[](#cb3-14)
[](#cb3-15)// 加载原始图片
[](#cb3-16)long originalImage = LoadImage(ola, "original.png");
[](#cb3-17)if (originalImage != 0) {
[](#cb3-18)    // 移除其他颜色
[](#cb3-19)    long resultImage = RemoveOtherColors(ola, originalImage, colorList);
[](#cb3-20)    if (resultImage != 0) {
[](#cb3-21)        // 保存处理后的图片
[](#cb3-22)        SaveImageFromPtr(ola, resultImage, "result.png");
[](#cb3-23)
[](#cb3-24)        // 释放内存
[](#cb3-25)        FreeImagePtr(ola, resultImage);
[](#cb3-26)    }
[](#cb3-27)
[](#cb3-28)    // 释放原始图片内存
[](#cb3-29)    FreeImagePtr(ola, originalImage);
[](#cb3-30)}
```

### 返回值

长整型数: - 成功：返回处理后的OLAImage对象地址 - 失败：返回0

### 注意事项

- 颜色值必须使用RRGGBB格式的十六进制字符串

- 支持多个颜色范围的指定，每个范围可以设置不同的匹配类型

- 颜色匹配类型说明：

0: 正常匹配，保留在颜色范围内的像素

- 1: 反色匹配，保留在颜色范围外的像素

- 2: 正常交集匹配，保留在颜色范围内的像素取交集

- 3: 反色交集匹配，保留在颜色范围外的像素取交集

- 处理后的图片中，非指定颜色范围的像素将被设置为透明

- 原始图片不会被修改，函数返回新的图片对象

- 使用完毕后必须调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
释放内存

- 颜色范围必须有效，起始颜色不能大于结束颜色

- 建议在使用前检查图片指针和颜色列表的有效性

- 处理大图片时注意内存使用

- 颜色匹配是精确的，如果需要模糊匹配，请使用其他相关函数

---

# 绘制圆形 - DrawCircle

### 函数简介

在图片中绘制圆形。支持实线圆和填充圆，可以指定颜色和透明度。

### 接口名称

```
DrawCircle
```

### DLL调用

```
long DrawCircle(long ola, long ptr, int x, int y, int radius, int thickness, string color)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `ptr` (长整型数): OLAImage对象的地址

- `x` (整型数): 圆心X坐标

- `y` (整型数): 圆心Y坐标

- `radius` (整型数): 圆的半径，单位为像素

- `thickness` (整型数): 线条的粗细

正值: 表示圆形轮廓的线条粗细

- 负值: 表示绘制填充圆

- `color` (字符串): 填充的颜色，支持ARGB格式，如”#FFFFFFFF”

前两位: Alpha通道，00-FF，表示透明度

- 中间两位: Red通道，00-FF

- 后四位: Green和Blue通道，各00-FF

#### 示例:

```
[](#cb3-1)// 加载原图
[](#cb3-2)long imagePtr = ola.LoadImage("test.bmp");
[](#cb3-3)
[](#cb3-4)// 绘制一个红色实心圆
[](#cb3-5)long filledCircle = ola.DrawCircle(imagePtr, 100, 100, 50, -1, "#FFFF0000");
[](#cb3-6)
[](#cb3-7)// 绘制一个蓝色空心圆，线条粗细为2像素
[](#cb3-8)long outlineCircle = ola.DrawCircle(imagePtr, 200, 200, 30, 2, "#FF0000FF");
[](#cb3-9)
[](#cb3-10)// 绘制一个半透明的绿色实心圆
[](#cb3-11)long transparentCircle = ola.DrawCircle(imagePtr, 300, 300, 40, -1, "#8000FF00");
[](#cb3-12)
[](#cb3-13)// 显示结果
[](#cb3-14)ola.ShowImage(filledCircle);
[](#cb3-15)
[](#cb3-16)// 释放内存
[](#cb3-17)ola.FreeImagePtr(imagePtr);
[](#cb3-18)ola.FreeImagePtr(filledCircle);
[](#cb3-19)ola.FreeImagePtr(outlineCircle);
[](#cb3-20)ola.FreeImagePtr(transparentCircle);
```

### 返回值

长整型数: 返回新的OLAImage对象的地址

**注意**： - 图片使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口释放内存 - 原图不会被修改，而是返回一个新的图片对象 -
坐标系原点(0,0)在图片左上角 -
确保圆形的范围不超出图片边界，否则可能会被裁剪

---

# 绘制多边形 - DrawFillPoly

### 函数简介

在图片中绘制多边形。

### 接口名称

```
DrawFillPoly
```

### DLL调用

```
long DrawFillPoly(long ola, long ptr, string pointList, string color)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `ptr` (长整型数): OLAImage对象的地址

- `pointList` (字符串):
坐标点列表JSON字符串，格式如：[{“x”:1,“y”:“2”},{“x”:2,“y”:“1”},{“x”:10,“y”:“11”}]

- `color` (字符串): 填充的颜色，支持ARGB格式，如
#FFFFFFFF

#### 示例:

待补充…

### 返回值

长整型数:

OLAImage对象的地址

**注意**：图片使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口进行释放

---

# 绘制矩形 - DrawRectangle

### 函数简介

在图片中绘制矩形。支持实线矩形和填充矩形，可以指定颜色和透明度。此函数支持ARGB颜色格式，可以设置带透明度的颜色。适用于图像编辑、界面绘制等场景。

### 接口名称

```
DrawRectangle
```

### DLL调用

```
long DrawRectangle(long ola, long ptr, int x1, int y1, int x2, int y2, int thickness, string color)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `ptr` (长整型数): OLAImage对象的地址

- `x1` (整型数): 矩形左上角的X坐标

- `y1` (整型数): 矩形左上角的Y坐标

- `x2` (整型数): 矩形右下角的X坐标

- `y2` (整型数): 矩形右下角的Y坐标

- `thickness` (整型数): 线条的粗细

正值: 表示矩形轮廓的线条粗细

- 负值: 表示绘制填充矩形

- `color` (字符串): 填充的颜色，支持ARGB格式，如”#FFFFFFFF”

前两位: Alpha通道，00-FF，表示透明度

- 中间两位: Red通道，00-FF

- 后四位: Green和Blue通道，各00-FF

#### 示例:

```
[](#cb3-1)// 加载原图
[](#cb3-2)long imagePtr = ola.LoadImage("test.bmp");
[](#cb3-3)
[](#cb3-4)// 绘制一个红色填充矩形
[](#cb3-5)long filledRect = ola.DrawRectangle(imagePtr, 50, 50, 150, 150, -1, "#FFFF0000");
[](#cb3-6)
[](#cb3-7)// 绘制一个蓝色边框矩形，线条粗细为2像素
[](#cb3-8)long outlineRect = ola.DrawRectangle(imagePtr, 200, 200, 300, 300, 2, "#FF0000FF");
[](#cb3-9)
[](#cb3-10)// 绘制一个半透明的绿色填充矩形
[](#cb3-11)long transparentRect = ola.DrawRectangle(imagePtr, 350, 350, 450, 450, -1, "#8000FF00");
[](#cb3-12)
[](#cb3-13)// 显示结果
[](#cb3-14)ola.ShowImage(filledRect);
[](#cb3-15)
[](#cb3-16)// 释放内存
[](#cb3-17)ola.FreeImagePtr(imagePtr);
[](#cb3-18)ola.FreeImagePtr(filledRect);
[](#cb3-19)ola.FreeImagePtr(outlineRect);
[](#cb3-20)ola.FreeImagePtr(transparentRect);
```

### 返回值

长整型数: 返回新的OLAImage对象的地址

### 注意事项

- 颜色值支持两种格式：

不透明颜色：6位十六进制，如”#FFFFFF”

- 带透明度颜色：8位十六进制，如”#FFFFFFFF”（前两位为透明度）

- 坐标必须在图片的有效范围内

- 原图不会被修改，而是返回一个新的图片对象

- 使用完毕后必须调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
释放内存

- 建议在使用前检查图片指针和坐标的有效性

- 线条粗细的绝对值必须大于0

- 颜色值不区分大小写

- 建议在修改前保存原始图片的备份

- 修改后的图片需要重新保存才能永久保存更改

- 绘制大矩形时注意性能影响

- 如果需要绘制其他形状，请使用其他相关函数

---

# 翻转图像 - Flip

## 函数简介

按照给定翻转代码对图像进行翻转。

flipCode：0 为 X 轴翻转，1 为 Y 轴翻转，2 为同时翻转。

## 接口名称

```
Flip
```

## DLL调用

```
int64_t Flip(int64_t instance, int64_t ptr, int32_t flipCode);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针。 |
|

|
flipCode |
整数型 |
翻转代码：0 X 轴，1 Y 轴，2 同时翻转。 |
|

### 示例

```
[](#cb3-1)long image = LoadImage(ola, "D:/test/img.png");
[](#cb3-2)if (image) {
[](#cb3-3)    long flipped = Flip(ola, image, 2);
[](#cb3-4)    if (flipped) {
[](#cb3-5)        FreeImagePtr(ola, flipped);
[](#cb3-6)    }
[](#cb3-7)    FreeImagePtr(ola, image);
[](#cb3-8)}
```

## 返回值

返回翻转后的图像句柄，失败返回0。

## 注意事项

- 处理后的图像需调用 `FreeImagePtr` 释放。

---

# 腐蚀 - Erosion

## 函数简介

对图像进行形态学腐蚀操作，使前景区域收缩，去除细小噪点。

## 接口名称

```
Erosion
```

## DLL调用

```
int64_t Erosion(int64_t instance, int64_t ptr, int32_t kernelSize);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针。 |
|

|
kernelSize |
整数型 |
结构元素核大小，建议使用奇数（3、5、7等）。 |
|

### 示例

```
[](#cb3-1)long image = LoadImage(ola, "D:/test/bin.png");
[](#cb3-2)if (image) {
[](#cb3-3)    long result = Erosion(ola, image, 3);
[](#cb3-4)    if (result) {
[](#cb3-5)        FreeImagePtr(ola, result);
[](#cb3-6)    }
[](#cb3-7)    FreeImagePtr(ola, image);
[](#cb3-8)}
```

## 返回值

返回处理后的图像句柄，失败返回0。

## 注意事项

- 与 `Dilation` 配合可实现开闭运算。

- 处理后的图像需调用 `FreeImagePtr` 释放。

---

# 膨胀 - Dilation

## 函数简介

对图像进行形态学膨胀操作，使前景区域扩张，填补小孔洞。

## 接口名称

```
Dilation
```

## DLL调用

```
int64_t Dilation(int64_t instance, int64_t ptr, int32_t kernelSize);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针。 |
|

|
kernelSize |
整数型 |
结构元素核大小，建议使用奇数（3、5、7等）。 |
|

### 示例

```
[](#cb3-1)long image = LoadImage(ola, "D:/test/bin.png");
[](#cb3-2)if (image) {
[](#cb3-3)    long result = Dilation(ola, image, 3);
[](#cb3-4)    if (result) {
[](#cb3-5)        FreeImagePtr(ola, result);
[](#cb3-6)    }
[](#cb3-7)    FreeImagePtr(ola, image);
[](#cb3-8)}
```

## 返回值

返回处理后的图像句柄，失败返回0。

## 注意事项

- 与 `Erosion` 配合可实现开闭运算。

- 处理后的图像需调用 `FreeImagePtr` 释放。

---

# 获取ROI区域 - GetROIRegion

## 函数简介

获取ROI（Region of
Interest）区域的坐标信息。此函数可以获取图像中ROI区域的边界坐标，返回区域的左上角和右下角坐标值，用于确定感兴趣区域的具体位置和大小。

## 接口名称

```
GetROIRegion
```

## DLL调用

```
int GetROIRegion(long instance, long ptr, int* x1, int* y1, int* x2, int* y2)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针，由图像处理函数返回 |
|

|
x1 |
整数指针 |
输出参数，ROI区域左上角的X坐标 |
|

|
y1 |
整数指针 |
输出参数，ROI区域左上角的Y坐标 |
|

|
x2 |
整数指针 |
输出参数，ROI区域右下角的X坐标 |
|

|
y2 |
整数指针 |
输出参数，ROI区域右下角的Y坐标 |
|

### 示例

```
[](#cb3-1)// 获取图像的ROI区域坐标
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\image.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    int x1, y1, x2, y2;
[](#cb3-5)
[](#cb3-6)    if (GetROIRegion(ola, image, &x1, &y1, &x2, &y2) == 1) {
[](#cb3-7)        printf("ROI区域坐标: (%d, %d) - (%d, %d)\n", x1, y1, x2, y2);
[](#cb3-8)        printf("ROI区域大小: %d x %d\n", x2 - x1, y2 - y1);
[](#cb3-9)
[](#cb3-10)        // 可以根据ROI坐标进行进一步处理
[](#cb3-11)        long roiImage = Cropped(ola, image, x1, y1, x2, y2);
[](#cb3-12)        if (roiImage != 0) {
[](#cb3-13)            ShowImage(roiImage);
[](#cb3-14)            FreeImagePtr(ola, roiImage);
[](#cb3-15)        }
[](#cb3-16)    }
[](#cb3-17)
[](#cb3-18)    FreeImagePtr(ola, image);
[](#cb3-19)}
[](#cb3-20)
[](#cb3-21)// 获取截图ROI区域
[](#cb3-22)long screen = GetScreenDataPtr(ola, 0, 0, 1920, 1080);
[](#cb3-23)if (screen != 0) {
[](#cb3-24)    int x1, y1, x2, y2;
[](#cb3-25)
[](#cb3-26)    if (GetROIRegion(ola, screen, &x1, &y1, &x2, &y2) == 1) {
[](#cb3-27)        printf("屏幕ROI区域: (%d, %d) - (%d, %d)\n", x1, y1, x2, y2);
[](#cb3-28)
[](#cb3-29)        // 使用ROI坐标进行精确截图
[](#cb3-30)        long roiScreen = GetScreenDataPtr(ola, x1, y1, x2 - x1, y2 - y1);
[](#cb3-31)        if (roiScreen != 0) {
[](#cb3-32)            // 处理ROI截图
[](#cb3-33)            FreeImagePtr(ola, roiScreen);
[](#cb3-34)        }
[](#cb3-35)    }
[](#cb3-36)
[](#cb3-37)    FreeImagePtr(ola, screen);
[](#cb3-38)}
```

## 返回值

整数型:

- 成功：返回1

- 失败：返回0

## 注意事项

- 坐标系统基于图像坐标系，原点在左上角

- x1, y1 为ROI区域的左上角坐标

- x2, y2 为ROI区域的右下角坐标

- ROI区域大小计算为 (x2-x1) × (y2-y1)

- 此函数通常与 [FastROI](/图像处理/快速ROI%20-%20FastROI.html) 函数配合使用

- 适用于需要获取图像有效区域边界信息的场景

- 返回的坐标可以用于后续的图像裁剪、区域分析等操作

---

# 获取二值化图像
- GetThresholdImageFromMultiColorPtr

### 函数简介

根据指定的颜色范围列表，将图片转换为二值化图像。此函数可以保留指定颜色范围内的像素，其他像素将被设置为黑色。支持多个颜色范围，每个范围可以指定不同的处理类型。

### 接口名称

```
GetThresholdImageFromMultiColorPtr
```

### DLL调用

```
long GetThresholdImageFromMultiColorPtr(long ola, long imgPtr, string colorList)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `imgPtr` (长整型数): OLAImage对象的地址，源图片指针

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)long ola = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 加载源图片
[](#cb3-5)long srcImage = LoadImage(ola, "test.bmp");
[](#cb3-6)
[](#cb3-7)// 定义颜色范围列表
[](#cb3-8)string colorList = "[{\"StartColor\":\"3278FA\",\"EndColor\":\"6496FF\",\"Type\":0}]";
[](#cb3-9)
[](#cb3-10)// 获取二值化图像
[](#cb3-11)long thresholdImage = GetThresholdImageFromMultiColorPtr(ola, srcImage, colorList);
[](#cb3-12)
[](#cb3-13)// 检查操作是否成功
[](#cb3-14)if (thresholdImage != 0) {
[](#cb3-15)    // 显示结果
[](#cb3-16)    ShowImage(ola, thresholdImage);
[](#cb3-17)
[](#cb3-18)    // 释放内存
[](#cb3-19)    FreeImagePtr(ola, thresholdImage);
[](#cb3-20)} else {
[](#cb3-21)    // 处理失败
[](#cb3-22)}
[](#cb3-23)
[](#cb3-24)// 释放源图片内存
[](#cb3-25)FreeImagePtr(ola, srcImage);
```

### 返回值

长整型数: - 0: 失败 - 非0: 成功，返回新的OLAImage对象的地址

### 注意事项

- 颜色值使用十六进制格式，不包含#前缀

- 每个颜色范围包含起始颜色和结束颜色，形成一个颜色区间

- Type参数决定处理方式：

0: 保留颜色范围内的像素，其他像素设为黑色

- 1: 保留颜色范围外的像素，范围内像素设为黑色

- 可以指定多个颜色范围，每个范围独立处理

- 返回的图片需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
释放内存

- 原图不会被修改，而是返回一个新的图片对象

- 颜色比较采用RGB颜色空间，不考虑Alpha通道

### 相关函数

- [LoadImage](/图像处理/加载图片%20-%20LoadImage.html):
加载图片

- [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html):
释放图片内存

- [ShowImage](/图像处理/弹窗显示图片%20-%20ShowImage.html):
显示图片

---

# 获取像素颜色 - GetColorPtr

## 函数简介

从指定的图片中获取指定坐标 `(x, y)`
处的颜色值,颜色返回格式”AARRGGBB”

## 函数原型

```
[](#cb1-1)long GetColorPtr(long ola, long source, int x, int y);
```

## 参数定义

- `ola`: OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `source`: 源对象的指针，通常是一个图像或画布对象。

- `x`: 要获取颜色的像素点的横坐标。

- `y`: 要获取颜色的像素点的纵坐标。

## 返回值

- 返回值：颜色返回格式”AARRGGBB”

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long source = OLAServer.LoadImage("image.png"); // 假设有一个加载图像的函数
[](#cb2-19)            Console.WriteLine($"LoadImage 返回:{source}");
[](#cb2-20)
[](#cb2-21)            // 获取颜色指针
[](#cb2-22)            int x = 100;
[](#cb2-23)            int y = 200;
[](#cb2-24)            long colorPtr = OLAServer.GetColorPtr(source, x, y);
[](#cb2-25)            if (colorPtr != 0)
[](#cb2-26)            {
[](#cb2-27)                // 假设颜色值是一个32位的整数（ARGB格式）
[](#cb2-28)                int colorValue = Marshal.ReadInt32(new IntPtr(colorPtr));
[](#cb2-29)                Console.WriteLine($"坐标 ({x}, {y}) 处的颜色值: {colorValue}");
[](#cb2-30)            }
[](#cb2-31)            else
[](#cb2-32)            {
[](#cb2-33)                Console.WriteLine("获取颜色失败。");
[](#cb2-34)            }
[](#cb2-35)        }
[](#cb2-36)    }
[](#cb2-37)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 加载图像
[](#cb3-10)source = OLAServer.LoadImage("image.png")  # 假设有一个加载图像的函数
[](#cb3-11)print(f"LoadImage 返回: {source}")
[](#cb3-12)
[](#cb3-13)# 获取颜色指针
[](#cb3-14)x = 100
[](#cb3-15)y = 200
[](#cb3-16)colorPtr = OLAServer.GetColorPtr(source, x, y)
[](#cb3-17)if colorPtr != 0:
[](#cb3-18)    # 假设颜色值是一个32位的整数（ARGB格式）
[](#cb3-19)    colorValue = ctypes.cast(colorPtr, ctypes.POINTER(ctypes.c_int32)).contents.value
[](#cb3-20)    print(f"坐标 ({x}, {y}) 处的颜色值: {colorValue}")
[](#cb3-21)else:
[](#cb3-22)    print("获取颜色失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 加载图像
[](#cb4-27)olaplug_dll.LoadImage.argtypes = [c_void_p, c_char_p]
[](#cb4-28)olaplug_dll.LoadImage.restype = c_void_p
[](#cb4-29)source = olaplug_dll.LoadImage(ola_obj, "image.png".encode('utf-8'))
[](#cb4-30)print(f"LoadImage 返回: {source}")
[](#cb4-31)
[](#cb4-32)# 5. 获取颜色指针
[](#cb4-33)x = 100
[](#cb4-34)y = 200
[](#cb4-35)olaplug_dll.GetColorPtr.argtypes = [c_void_p, c_void_p, c_int32, c_int32]
[](#cb4-36)olaplug_dll.GetColorPtr.restype = c_void_p
[](#cb4-37)colorPtr = olaplug_dll.GetColorPtr(ola_obj, source, x, y)
[](#cb4-38)if colorPtr != 0:
[](#cb4-39)    # 假设颜色值是一个32位的整数（ARGB格式）
[](#cb4-40)    colorValue = ctypes.cast(colorPtr, ctypes.POINTER(ctypes.c_int32)).contents.value
[](#cb4-41)    print(f"坐标 ({x}, {y}) 处的颜色值: {colorValue}")
[](#cb4-42)else:
[](#cb4-43)    print("获取颜色失败。")
```

### 返回值

字符串: 颜色字符串(注意这里都是小写字符，和工具相匹配)

**注意**：

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 获取前景点 -
GetForegroundPoints

## 函数简介

获取二值化图像中的前景点坐标信息。此函数可以检测图像中的前景对象，并返回所有前景点的坐标信息，以JSON格式返回。适用于图像分割、目标检测、轮廓分析等场景。

## 接口名称

```
GetForegroundPoints
```

## DLL调用

```
long GetForegroundPoints(long instance, long ptr)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针，由图像处理函数返回 |
|

### 示例

```
[](#cb3-1)// 获取图像前景点
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\image.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    long pointsPtr = GetForegroundPoints(ola, image);
[](#cb3-5)    if (pointsPtr != 0) {
[](#cb3-6)        // 获取JSON字符串
[](#cb3-7)        char* jsonStr = (char*)pointsPtr;
[](#cb3-8)        printf("前景点JSON: %s\n", jsonStr);
[](#cb3-9)
[](#cb3-10)        // 解析JSON格式的前景点坐标
[](#cb3-11)        // 格式: [{"x":10,"y":10},{"x":20,"y":20}]
[](#cb3-12)
[](#cb3-13)        // 释放内存
[](#cb3-14)        free(pointsPtr);
[](#cb3-15)    }
[](#cb3-16)
[](#cb3-17)    FreeImagePtr(ola, image);
[](#cb3-18)}
[](#cb3-19)
[](#cb3-20)// 获取二值化图像的前景点
[](#cb3-21)long screen = GetScreenDataPtr(ola, 0, 0, 1920, 1080);
[](#cb3-22)if (screen != 0) {
[](#cb3-23)    // 先进行二值化处理
[](#cb3-24)    long thresholded = Threshold(ola, screen, 128.0, 255.0, 0);
[](#cb3-25)    if (thresholded != 0) {
[](#cb3-26)        long pointsPtr = GetForegroundPoints(ola, thresholded);
[](#cb3-27)        if (pointsPtr != 0) {
[](#cb3-28)            printf("前景点数量: %s\n", (char*)pointsPtr);
[](#cb3-29)            free(pointsPtr);
[](#cb3-30)        }
[](#cb3-31)        FreeImagePtr(ola, thresholded);
[](#cb3-32)    }
[](#cb3-33)    FreeImagePtr(ola, screen);
[](#cb3-34)}
[](#cb3-35)
[](#cb3-36)// 结合其他图像处理函数使用
[](#cb3-37)long image = LoadImage(ola, "D:\\test\\target.png");
[](#cb3-38)if (image != 0) {
[](#cb3-39)    // 转换为灰度图
[](#cb3-40)    long grayImage = ConvertColor(ola, image, 0);
[](#cb3-41)    if (grayImage != 0) {
[](#cb3-42)        // 阈值化
[](#cb3-43)        long binaryImage = Threshold(ola, grayImage, 128.0, 255.0, 0);
[](#cb3-44)        if (binaryImage != 0) {
[](#cb3-45)            // 获取前景点
[](#cb3-46)            long pointsPtr = GetForegroundPoints(ola, binaryImage);
[](#cb3-47)            if (pointsPtr != 0) {
[](#cb3-48)                printf("处理后的前景点: %s\n", (char*)pointsPtr);
[](#cb3-49)                free(pointsPtr);
[](#cb3-50)            }
[](#cb3-51)            FreeImagePtr(ola, binaryImage);
[](#cb3-52)        }
[](#cb3-53)        FreeImagePtr(ola, grayImage);
[](#cb3-54)    }
[](#cb3-55)    FreeImagePtr(ola, image);
[](#cb3-56)}
```

## 返回值

long: 返回前景点数组的JSON字符串指针，格式为
`[{"x":10,"y":10},{"x":20,"y":20}]`

## 注意事项

- 返回的JSON字符串需要手动释放内存

- 前景点检测基于图像的非零像素

- 适用于二值化图像或经过预处理的图像

- 返回的坐标基于图像坐标系，原点在左上角

- 建议与 [Threshold](/图像处理/图像阈值化%20-%20Threshold.html)
函数配合使用

- JSON格式便于后续处理和解析

- 适用于目标检测、轮廓分析、图像分割等应用场景

---

# 获取图片大小 - GetImageSize

### 函数简介

获取指定图片的宽度和高度。此函数可用于获取已加载到内存中的图片尺寸信息，返回的尺寸单位为像素。这对于图像处理、界面布局、图像匹配等操作非常有用。

### 接口名称

```
GetImageSize
```

### DLL调用

```
int GetImageSize(long ola, long image_ptr, int* width, int* height)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `image_ptr` (长整型数):
图片句柄，由图片加载函数返回。

- `width` (整型数指针): 返回图片的宽度（像素）。

- `height` (整型数指针): 返回图片的高度（像素）。

#### 示例:

```
[](#cb3-1)// 获取单个图片的大小
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\sample.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    int width, height;
[](#cb3-5)    int ret = GetImageSize(ola, image, &width, &height);
[](#cb3-6)    if (ret == 1) {
[](#cb3-7)        printf("图片大小：%d x %d 像素\n", width, height);
[](#cb3-8)
[](#cb3-9)        // 计算图片的宽高比
[](#cb3-10)        float aspect_ratio = (float)width / height;
[](#cb3-11)        printf("宽高比：%.2f\n", aspect_ratio);
[](#cb3-12)
[](#cb3-13)        // 计算图片的总像素数
[](#cb3-14)        int total_pixels = width * height;
[](#cb3-15)        printf("总像素数：%d\n", total_pixels);
[](#cb3-16)    } else {
[](#cb3-17)        printf("获取图片大小失败\n");
[](#cb3-18)    }
[](#cb3-19)
[](#cb3-20)    FreeImagePtr(ola, image);
[](#cb3-21)}
[](#cb3-22)
[](#cb3-23)// 比较两张图片的大小
[](#cb3-24)long image1 = LoadImage(ola, "D:\\test\\pic1.jpg");
[](#cb3-25)long image2 = LoadImage(ola, "D:\\test\\pic2.jpg");
[](#cb3-26)if (image1 != 0 && image2 != 0) {
[](#cb3-27)    int width1, height1, width2, height2;
[](#cb3-28)    GetImageSize(ola, image1, &width1, &height1);
[](#cb3-29)    GetImageSize(ola, image2, &width2, &height2);
[](#cb3-30)
[](#cb3-31)    printf("图片1大小：%d x %d\n", width1, height1);
[](#cb3-32)    printf("图片2大小：%d x %d\n", width2, height2);
[](#cb3-33)
[](#cb3-34)    if (width1 * height1 > width2 * height2) {
[](#cb3-35)        printf("图片1的尺寸更大\n");
[](#cb3-36)    } else if (width1 * height1 < width2 * height2) {
[](#cb3-37)        printf("图片2的尺寸更大\n");
[](#cb3-38)    } else {
[](#cb3-39)        printf("两张图片尺寸相同\n");
[](#cb3-40)    }
[](#cb3-41)
[](#cb3-42)    FreeImagePtr(ola, image1);
[](#cb3-43)    FreeImagePtr(ola, image2);
[](#cb3-44)}
```

### 返回值

整型数: - 0: 获取失败 - 1: 获取成功

### 注意事项

- 使用此函数前，确保图片已经成功加载到内存中

- 返回的尺寸单位为像素，与图片的实际物理尺寸（如打印尺寸）可能不同

- 对于动态图（如GIF），返回的是第一帧的尺寸

- 如果需要调整图片大小，可以使用 [ReSize](/图像处理/调整图片大小%20-%20ReSize.html) 或 [ScalePixels](/图像处理/调整图片大小%20-%20ScalePixels.html)
函数

- 在进行图像匹配操作前，建议先检查目标图片和模板图片的尺寸是否合适

---

# 获取拼接结果 -
ImageStitchGetResult

## 函数简介

获取当前拼接实例的拼接结果图像，可返回轨迹数据。

## 接口名称

```
ImageStitchGetResult
```

## DLL调用

```
int64_t ImageStitchGetResult(int64_t instance, int64_t imageStitch, int64_t* trajectory);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
imageStitch |
长整数型 |
拼接实例句柄。 |
|

|
trajectory |
长整数指针 |
输出参数，可为0；返回轨迹数据的字符串指针，需使用
`FreeStringPtr` 释放。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t st = ImageStitchCreate(instance);
[](#cb3-3)// ... append images
[](#cb3-4)int64_t traj = 0;
[](#cb3-5)int64_t result = ImageStitchGetResult(instance, st, &traj);
[](#cb3-6)if (result) {
[](#cb3-7)    FreeImagePtr(instance, result);
[](#cb3-8)}
[](#cb3-9)if (traj) {
[](#cb3-10)    FreeStringPtr(traj);
[](#cb3-11)}
[](#cb3-12)ImageStitchFree(instance, st);
[](#cb3-13)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回拼接后的图像句柄，失败返回0。

## 注意事项

- 轨迹数据指针需使用 `FreeStringPtr` 释放。

- 返回的图像需使用 `FreeImagePtr` 释放。

---

# 获取指定区域二值化图像
-GetThresholdImageFromMultiColor

获取指定区域二值化图像,只保留指定颜色

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

### 接口名称

```
GetThresholdImageFromMultiColor
```

### DLL调用

```
long GetThresholdImageFromMultiColor(long ola, int x1, int y1, int x2, int y2, string colorList)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

#### 示例:

待补充…

### 返回值

长整型数:

OLAImage对象的地址

**注意**：图片使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口进行释放

---

# 获取指定区域刷新率 -
GetWindowsFps

获取指定区域刷新率

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

### 接口名称

```
GetWindowsFps
```

### DLL调用

```
int GetWindowsFps(long ola, int x1, int y1, int x2, int y2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

#### 示例:

待补充…

### 返回值

整型数: 刷新率

---

# 获取指定区域图象 -
GetScreenDataPtr

### 函数简介

获取指定区域的图像

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

### 接口名称

```
GetScreenDataPtr
```

### DLL调用

```
long GetScreenDataPtr(long ola, int x1, int y1, int x2, int y2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `x1` (整型数): 区域的左上X坐标

- `y1` (整型数): 区域的左上Y坐标

- `x2` (整型数): 区域的右下X坐标

- `y2` (整型数): 区域的右下Y坐标

#### 示例:

待补充…

### 返回值

长整型数: OLAImage对象的地址

---

# 获取指定颜色数量 -
GetColorNum

### 函数简介

查找指定区域内符合指定颜色范围的所有颜色数量。此函数可以统计指定区域中符合特定颜色范围的像素点数量，适用于图像分析、颜色统计等场景。

**ColorModel:**

颜色每个通道单独计算范围，如颜色范围位3278FA，6496FF，实际对应R(50~100)
G(120 ~150) B(250 ~255)

支持ARGB模式如#FFFFFFFF

支持反色模式，交集并集查询颜色 - 0: 正常匹配，保留在颜色范围内的像素
- 1: 反色匹配，保留在颜色范围外的像素 - 2:
正常交集匹配，保留在颜色范围内的像素取交集 - 3:
反色交集匹配，保留在颜色范围外的像素取交集 如{“StartColor”: “3278FA”,
“EndColor”: “6496FF”,“Type”:0}

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

### 接口名称

```
GetColorNum
```

### DLL调用

```
int GetColorNum(long ola, int x1, int y1, int x2, int y2, string colorList)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

#### 示例:

```
[](#cb3-1)// 在指定区域查找白色像素点数量
[](#cb3-2)string colorList = "[{\"StartColor\": \"FFFFFF\", \"EndColor\": \"FFFFFF\", \"Type\": 0}]";
[](#cb3-3)int count = GetColorNum(ola, 100, 100, 200, 200, colorList);
[](#cb3-4)printf("找到白色像素点数量：%d\n", count);
[](#cb3-5)
[](#cb3-6)// 在指定区域查找多个颜色范围的像素点数量
[](#cb3-7)string colorList = "[{\"StartColor\": \"3278FA\", \"EndColor\": \"6496FF\", \"Type\": 0}, {\"StartColor\": \"FF0000\", \"EndColor\": \"FF0000\", \"Type\": 0}]";
[](#cb3-8)int count = GetColorNum(ola, 0, 0, 0, 0, colorList);  // 在整个客户区查找
[](#cb3-9)printf("找到符合颜色范围的像素点数量：%d\n", count);
```

### 返回值

整型数: 返回指定区域内符合颜色范围的像素点数量。如果失败返回0。

### 注意事项

- 颜色范围使用RRGGBB格式，每个通道单独计算范围

- 支持ARGB模式，如#FFFFFFFF

- 颜色匹配类型说明：

0: 正常匹配，保留在颜色范围内的像素

- 1: 反色匹配，保留在颜色范围外的像素

- 2: 正常交集匹配，保留在颜色范围内的像素取交集

- 3: 反色交集匹配，保留在颜色范围外的像素取交集

- 坐标范围必须有效，否则可能导致程序异常

- 颜色列表格式必须正确，否则可能导致程序异常

- 使用反色模式时，会统计不在指定颜色范围内的点

- 使用交集模式时，需要同时满足所有颜色条件

- 使用并集模式时，满足任一颜色条件即可

- 如果区域较大，统计过程可能需要一定时间

- 建议在统计大区域时注意性能影响

---

# 获取指定颜色数量 -
GetColorNumPtr

### 函数简介

查找指定图像内符合指定颜色范围的所有颜色数量。此函数可以统计指定图片中符合特定颜色范围的像素点数量，适用于图像分析、颜色统计等场景。与GetColorNum不同，此函数直接处理图片对象而不是屏幕区域。

**ColorModel:**

颜色每个通道单独计算范围，如颜色范围位3278FA，6496FF，实际对应R(50~100)
G(120 ~150) B(250 ~255)

支持ARGB模式如#FFFFFFFF

支持反色模式，交集并集查询颜色 - 0: 正常匹配，保留在颜色范围内的像素
- 1: 反色匹配，保留在颜色范围外的像素 - 2:
正常交集匹配，保留在颜色范围内的像素取交集 - 3:
反色交集匹配，保留在颜色范围外的像素取交集 如{“StartColor”: “3278FA”,
“EndColor”: “6496FF”,“Type”:0}

### 接口名称

```
GetColorNumPtr
```

### DLL调用

```
int GetColorNumPtr(long ola, long imgPtr, string colorList)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `imgPtr` (长整型数): OLAImage对象的地址

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

#### 示例:

```
[](#cb3-1)// 加载图片
[](#cb3-2)long imagePtr = LoadImage(ola, "/OLA/pic/pic.bmp");
[](#cb3-3)if (imagePtr != 0) {
[](#cb3-4)    // 在图片中查找白色像素点数量
[](#cb3-5)    string colorList = "[{\"StartColor\": \"FFFFFF\", \"EndColor\": \"FFFFFF\", \"Type\": 0}]";
[](#cb3-6)    int count = GetColorNumPtr(ola, imagePtr, colorList);
[](#cb3-7)    printf("找到白色像素点数量：%d\n", count);
[](#cb3-8)
[](#cb3-9)    // 在图片中查找多个颜色范围的像素点数量
[](#cb3-10)    string colorList = "[{\"StartColor\": \"3278FA\", \"EndColor\": \"6496FF\", \"Type\": 0}, {\"StartColor\": \"FF0000\", \"EndColor\": \"FF0000\", \"Type\": 0}]";
[](#cb3-11)    int count = GetColorNumPtr(ola, imagePtr, colorList);
[](#cb3-12)    printf("找到符合颜色范围的像素点数量：%d\n", count);
[](#cb3-13)
[](#cb3-14)    // 释放图片内存
[](#cb3-15)    FreeImagePtr(ola, imagePtr);
[](#cb3-16)}
```

### 返回值

整型数: 返回指定图片中符合颜色范围的像素点数量。如果失败返回0。

### 注意事项

- 颜色范围使用RRGGBB格式，每个通道单独计算范围

- 支持ARGB模式，如#FFFFFFFF

- 颜色匹配类型说明：

0: 正常匹配，保留在颜色范围内的像素

- 1: 反色匹配，保留在颜色范围外的像素

- 2: 正常交集匹配，保留在颜色范围内的像素取交集

- 3: 反色交集匹配，保留在颜色范围外的像素取交集

- 图片指针必须有效，否则可能导致程序异常

- 颜色列表格式必须正确，否则可能导致程序异常

- 使用反色模式时，会统计不在指定颜色范围内的点

- 使用交集模式时，需要同时满足所有颜色条件

- 使用并集模式时，满足任一颜色条件即可

- 如果图片较大，统计过程可能需要一定时间

- 建议在统计大图片时注意性能影响

- 图片使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口释放内存

---

# 获取连通域 -
GetConnectedComponents

## 函数简介

获取图像中的连通域信息。连通域是指图像中具有相同或相似颜色值的相邻像素组成的区域。此函数可以识别图像中的连通区域并返回其坐标信息。

## 接口名称

```
GetConnectedComponents
```

## DLL调用

```
long GetConnectedComponents(long instance, long ptr, string points, int tolerance)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针，由图像处理函数返回 |
|

|
points |
字符串 |
连通域点数组，格式为JSON，如[{“x”:10,“y”:10},{“x”:20,“y”:20}] |
|

|
tolerance |
整数型 |
连通域阈值，用于判断像素是否属于同一连通域 |
|

### 示例

```
[](#cb3-1)// 加载图像并获取连通域
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\image.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    char points[4096]; // 足够大的缓冲区存储结果
[](#cb3-5)    int tolerance = 10; // 设置连通域阈值
[](#cb3-6)
[](#cb3-7)    long result = GetConnectedComponents(ola, image, points, tolerance);
[](#cb3-8)
[](#cb3-9)    ShowImage(result);
[](#cb3-10)
[](#cb3-11)    FreeImagePtr(ola, result);
[](#cb3-12)
[](#cb3-13)    FreeImagePtr(ola, image);
[](#cb3-14)}
[](#cb3-15)
[](#cb3-16)// 对截图进行连通域分析
[](#cb3-17)long screen = GetScreenDataPtr(ola, 0, 0, 1920, 1080);
[](#cb3-18)if (screen != 0) {
[](#cb3-19)    char points[8192]; // 更大的缓冲区用于复杂图像
[](#cb3-20)    int tolerance = 5; // 较小的阈值，更精确的连通域
[](#cb3-21)
[](#cb3-22)    if (GetConnectedComponents(ola, screen, points, tolerance) == 1) {
[](#cb3-23)        printf("屏幕截图连通域分析完成\n");
[](#cb3-24)        // 处理连通域数据
[](#cb3-25)    }
[](#cb3-26)
[](#cb3-27)    FreeImagePtr(ola, screen);
[](#cb3-28)}
```

## 返回值

长整数型:

OLAImage对象的地址

## 注意事项

- 返回的连通域为二值化图像,后续可以用做蒙版进行高级操作

- tolerance参数影响连通域的识别精度，值越小连通域越精确

- 建议为points参数分配足够大的缓冲区以存储所有连通域数据

- 连通域坐标基于图像坐标系，原点在左上角

- 此函数适用于图像分割、目标检测等应用场景

---

# 裁剪图片 - Cropped

### 函数简介

裁剪图片,图片大小为 x2-x1,y2-y1 ### 接口名称

```
Cropped
```

### DLL调用

```
long Cropped(long ola, long image, int x1, int y1, int x2, int y2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `image` (长整型数): OLAImage对象的地址

- `x1` (整型数): 区域的左上角X坐标

- `y1` (整型数): 区域的左上角Y坐标

- `x2` (整型数): 区域的右下角X坐标

- `y2` (整型数): 区域的右下角Y坐标

#### 示例:

待补充…

### 返回值

裁剪后的图像指针

**注意**：图片使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口进行释放

---

# 覆盖图片 - CoverImage

### 函数简介

将一张图片覆盖到另一张图片上。此函数可以将源图片覆盖到目标图片的指定位置，支持透明度设置。适用于图片合成、水印添加等场景。

### 接口名称

```
CoverImage
```

### DLL调用

```
int CoverImage(long ola, long srcPtr, long dstPtr, int x, int y, int alpha)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `srcPtr` (长整型数): 源图片的OLAImage对象的地址

- `dstPtr` (长整型数): 目标图片的OLAImage对象的地址

- `x` (整型数): 覆盖位置的X坐标

- `y` (整型数): 覆盖位置的Y坐标

- `alpha` (整型数):
透明度，范围0-255，0表示完全透明，255表示完全不透明

#### 示例:

```
[](#cb3-1)// 加载源图片和目标图片
[](#cb3-2)long srcPtr = LoadImage(ola, "/OLA/pic/watermark.png");
[](#cb3-3)long dstPtr = LoadImage(ola, "/OLA/pic/background.png");
[](#cb3-4)if (srcPtr != 0 && dstPtr != 0) {
[](#cb3-5)    // 在目标图片的(100, 100)位置覆盖源图片，透明度为128
[](#cb3-6)    int result = CoverImage(ola, srcPtr, dstPtr, 100, 100, 128);
[](#cb3-7)    if (result == 1) {
[](#cb3-8)        printf("图片覆盖成功\n");
[](#cb3-9)    } else {
[](#cb3-10)        printf("图片覆盖失败\n");
[](#cb3-11)    }
[](#cb3-12)
[](#cb3-13)    // 释放图片内存
[](#cb3-14)    FreeImagePtr(ola, srcPtr);
[](#cb3-15)    FreeImagePtr(ola, dstPtr);
[](#cb3-16)}
```

### 返回值

整型数: - 0: 覆盖失败 - 1: 覆盖成功

### 注意事项

- 源图片和目标图片的指针必须有效，否则可能导致程序异常

- 覆盖位置(x, y)必须在目标图片范围内

- 透明度参数必须在0-255范围内

- 源图片超出目标图片范围的部分将被裁剪

- 图片使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口释放内存

- 建议在覆盖前检查图片尺寸，确保不会超出目标图片范围

- 如果源图片或目标图片指针无效，函数将返回0

- 透明度为0时，源图片完全透明，不会影响目标图片

- 透明度为255时，源图片完全不透明，完全覆盖目标图片

- 建议在覆盖大图片时注意内存使用

---

# 解析二维码 - DecodeQRCode

### 函数简介

解析图片中的二维码内容。此函数可以识别并解析图片中的二维码，返回二维码中包含的文本信息。适用于需要读取二维码信息的场景，如扫码登录、信息获取等。

### 接口名称

```
DecodeQRCode
```

### DLL调用

```
long DecodeQRCode(long ola, long ptr)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `ptr` (长整型数): 包含二维码的OLAImage对象的地址

#### 示例:

```
[](#cb3-1)// 加载包含二维码的图片
[](#cb3-2)long imagePtr = LoadImage(ola, "/OLA/pic/qrcode.png");
[](#cb3-3)if (imagePtr != 0) {
[](#cb3-4)    // 解析二维码
[](#cb3-5)    long qrContentPtr = DecodeQRCode(ola, imagePtr);
[](#cb3-6)    if (qrContentPtr != 0) {
[](#cb3-7)        // 获取二维码内容
[](#cb3-8)        string qrContent = GetStringFromPtr(qrContentPtr);
[](#cb3-9)        printf("二维码内容：%s\n", qrContent.c_str());
[](#cb3-10)
[](#cb3-11)        // 释放字符串内存
[](#cb3-12)        FreeStringPtr(ola, qrContentPtr);
[](#cb3-13)    } else {
[](#cb3-14)        printf("二维码解析失败\n");
[](#cb3-15)    }
[](#cb3-16)
[](#cb3-17)    // 释放图片内存
[](#cb3-18)    FreeImagePtr(ola, imagePtr);
[](#cb3-19)}
```

### 返回值

字符串: 返回二维码中包含的文本内容。如果解析失败返回空字符串。

### 注意事项

- 图片必须包含有效的二维码，否则将返回空字符串

- 图片质量会影响二维码的识别率，建议使用清晰的图片

- 支持常见的二维码格式，如QR Code、Data Matrix等

- 图片使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口释放内存

- DLL调用时，返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

- 建议在解析前检查图片是否成功加载

- 如果二维码被遮挡或损坏，可能无法正确解析

- 图片尺寸过小可能影响识别效果

- 建议使用PNG或BMP格式的图片，以获得更好的识别效果

- 如果二维码内容包含特殊字符，请确保正确处理返回的字符串

---

# 设置图片指定坐标的颜色 -
SetPixel

### 函数简介

设置图片中指定坐标点的颜色为新的颜色值。此函数支持ARGB颜色格式，可以设置带透明度的颜色。适用于图像编辑、像素级修改等场景。

### 接口名称

```
SetPixel
```

### DLL调用

```
int SetPixel(long ola, long image, int x, int y, string color)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `image` (长整型数): OLAImage对象的地址

- `x` (整型数): 要设置颜色的X坐标

- `y` (整型数): 要设置颜色的Y坐标

- `color` (字符串):
要设置的颜色值，支持ARGB格式，如”#FFFFFFFF”（带透明度）或”#FFFFFF”（不透明）

#### 示例:

```
[](#cb3-1)// 加载图片
[](#cb3-2)long image = LoadImage(ola, "image.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    // 设置指定坐标的颜色（不透明）
[](#cb3-5)    if (SetPixel(ola, image, 100, 100, "#FF0000")) {
[](#cb3-6)        printf("设置红色成功\n");
[](#cb3-7)    }
[](#cb3-8)
[](#cb3-9)    // 设置指定坐标的颜色（带透明度）
[](#cb3-10)    if (SetPixel(ola, image, 200, 200, "#80FF0000")) {
[](#cb3-11)        printf("设置半透明红色成功\n");
[](#cb3-12)    }
[](#cb3-13)
[](#cb3-14)    // 保存修改后的图片
[](#cb3-15)    SaveImageFromPtr(ola, image, "result.png");
[](#cb3-16)
[](#cb3-17)    // 释放内存
[](#cb3-18)    FreeImagePtr(ola, image);
[](#cb3-19)}
```

### 返回值

整型数: - 1: 成功设置颜色 - 0: 设置失败

### 注意事项

- 颜色值支持两种格式：

不透明颜色：6位十六进制，如”#FFFFFF”

- 带透明度颜色：8位十六进制，如”#FFFFFFFF”（前两位为透明度）

- 坐标必须在图片的有效范围内

- 原始图片会被直接修改

- 使用完毕后必须调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
释放内存

- 建议在使用前检查图片指针和坐标的有效性

- 处理大图片时注意性能影响

- 如果需要批量修改多个像素，建议使用 [SetPixelList](/图像处理/设置图片指定坐标集的颜色%20-%20SetPixelList.html)
函数

- 颜色值不区分大小写

- 建议在修改前保存原始图片的备份

- 修改后的图片需要重新保存才能永久保存更改

---

# 设置图片指定坐标集的颜色 -
SetPixelList

### 函数简介

批量设置图片中多个指定坐标点的颜色为新的颜色值。此函数支持ARGB颜色格式，可以一次性设置多个像素点的颜色，比多次调用SetPixel更高效。适用于需要批量修改图片像素的场景。

### 接口名称

```
SetPixelList
```

### DLL调用

```
int SetPixelList(long ola, long image, string points, string color)
```

#### 参数定义:

-
`ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html)
接口生成。

-
`image` (长整型数): OLAImage对象的地址

-
`points` (字符串): 坐标集的JSON字符串，格式如下：

```
[](#cb3-1)[
[](#cb3-2)  {"x": 0, "y": 0},
[](#cb3-3)  {"x": 1, "y": 1},
[](#cb3-4)  {"x": 2, "y": 2}
[](#cb3-5)]
```

-
`color` (字符串):
要设置的颜色值，支持ARGB格式，如”#FFFFFFFF”（带透明度）或”#FFFFFF”（不透明）

#### 示例:

```
[](#cb4-1)// 加载图片
[](#cb4-2)long image = LoadImage(ola, "image.png");
[](#cb4-3)if (image != 0) {
[](#cb4-4)    // 定义要修改的坐标点列表
[](#cb4-5)    string points = R"([
[](#cb4-6)        {"x": 100, "y": 100},
[](#cb4-7)        {"x": 101, "y": 100},
[](#cb4-8)        {"x": 102, "y": 100}
[](#cb4-9)    ])";
[](#cb4-10)
[](#cb4-11)    // 设置多个坐标点的颜色（不透明）
[](#cb4-12)    if (SetPixelList(ola, image, points, "#FF0000")) {
[](#cb4-13)        printf("批量设置红色成功\n");
[](#cb4-14)    }
[](#cb4-15)
[](#cb4-16)    // 设置多个坐标点的颜色（带透明度）
[](#cb4-17)    if (SetPixelList(ola, image, points, "#80FF0000")) {
[](#cb4-18)        printf("批量设置半透明红色成功\n");
[](#cb4-19)    }
[](#cb4-20)
[](#cb4-21)    // 保存修改后的图片
[](#cb4-22)    SaveImageFromPtr(ola, image, "result.png");
[](#cb4-23)
[](#cb4-24)    // 释放内存
[](#cb4-25)    FreeImagePtr(ola, image);
[](#cb4-26)}
```

### 返回值

整型数: - 1: 成功设置颜色 - 0: 设置失败

### 注意事项

- 颜色值支持两种格式：

不透明颜色：6位十六进制，如”#FFFFFF”

- 带透明度颜色：8位十六进制，如”#FFFFFFFF”（前两位为透明度）

- 所有坐标点必须在图片的有效范围内

- 原始图片会被直接修改

- 使用完毕后必须调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
释放内存

- 建议在使用前检查图片指针和坐标的有效性

- 处理大量坐标点时注意性能影响

- 如果只需要修改单个像素，建议使用 [SetPixel](/图像处理/设置图片指定坐标的颜色%20-%20SetPixel.html)
函数

- 颜色值不区分大小写

- 建议在修改前保存原始图片的备份

- 修改后的图片需要重新保存才能永久保存更改

- JSON字符串中的坐标点数量没有限制，但建议控制在一个合理的范围内

- 如果坐标点列表为空，函数将返回成功但不进行任何修改

---

# 设置指定颜色为新的颜色
- SetColorsToNewColor

### 函数简介

将图片中指定的颜色替换为新的颜色。此函数可以批量修改图片中所有匹配指定颜色的像素点，支持颜色范围匹配和精确匹配。常用于图片颜色替换、背景色修改、主题色更改等场景。可以同时替换多个颜色。

### 接口名称

```
SetColorsToNewColor
```

### DLL调用

```
int SetColorsToNewColor(long ola, long image_ptr, string colors_json, string new_colors)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `image_ptr` (长整型数): 要修改的图片句柄。

- `colors_json` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `new_colors` (字符串):
要设置的颜色值，支持ARGB格式，如”#FFFFFFFF”（带透明度）或”#FFFFFF”（不透明）

#### 示例:

### 返回值

整型数: - 0: 替换失败 - 1: 替换成功

### 注意事项

- 处理大图片时，较大的相似度值可能会显著增加处理时间

---

# 读取图片BMP字节流 -
GetImageBmpData

### 函数简介

获取指定图像,用BMP数据格式返回

#### 注意事项

使用完成需要调用[FreeImageData](/图像处理/释放指定图片内存1%20-%20FreeImageData.html)接口释放内存

### 接口名称

```
GetImageBmpData
```

### DLL调用

```
int GetImageBmpData(long ola, long ptr, long* data, int* size)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `ptr` (长整型数): OLAImage对象的地址

- `data` (长整型数指针) 返回图片的数据指针

- `size`(整型数指针): 返回图片的数据长度

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 读取图片PNG字节流 -
GetImagePngData

### 函数简介

获取指定图像,用PNG数据格式返回

#### 注意事项

使用完成需要调用[FreeImageData](/图像处理/释放指定图片内存1%20-%20FreeImageData.html)接口释放内存

### 接口名称

```
GetImagePngData
```

### DLL调用

```
int GetImagePngData(long ola, long ptr, long* data, int* size)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `ptr` (长整型数): OLAImage对象的地址

- `data` (长整型数指针) 返回图片的数据指针

- `size`(整型数指针): 返回图片的数据长度

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 读取图片大小 - GetImageSize

### 函数简介

读取图片大小

### 接口名称

```
GetImageSize
```

### DLL调用

```
int GetImageSize(long ola, long ptr, int* width, int* height)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `ptr` (长整型数): OLAImage对象的地址

- `width`(整型数指针): 返回图像宽度

- `height`(整型数指针): 返回图像高度

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 读取图片字节流 -
GetImageData

### 函数简介

获取指定图像,用二进制数据的方式返回,数据格式BBGGRRAA,一个像素4字节BGRA格式。图象宽度=stride
/ 4 ，图象高度=size / stride

#### 注意事项

图像指针释放后([FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html))，data地址的数据就会被释放,需要把数据对象拷贝到自己的字节集中再使用。

### 接口名称

```
GetImageData
```

### DLL调用

```
int GetImageData(long ola, long ptr, long* data, int* size, int* stride)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `ptr` (长整型数): OLAImage对象的地址

- `data` (长整型数指针) 返回图片的数据指针

- `size`(整型数指针): 返回图片的数据长度

- `stride`(整型数指针):
返回图片的步长数据(图片每行数据字节数)

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 调整图片大小 - ReSize

### 函数简介

调整图片的尺寸大小。此函数可以将图片缩放到指定的宽度和高度，支持等比例缩放和自由缩放。缩放过程使用高质量的插值算法，以保证缩放后的图片质量。常用于图片预处理、缩略图生成、界面适配等场景。

### 接口名称

```
ReSize
```

### DLL调用

```
long ReSize(long ola, long image_ptr, int new_width, int new_height)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `image_ptr` (长整型数): 要调整大小的图片句柄。

- `new_width` (整型数): 目标宽度，单位为像素。

- `new_height` (整型数): 目标高度，单位为像素。

#### 示例:

```
[](#cb3-1)// 加载原图并获取尺寸
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\source.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    int width, height;
[](#cb3-5)    GetImageSize(ola, image, &width, &height);
[](#cb3-6)    printf("原图大小：%d x %d\n", width, height);
[](#cb3-7)
[](#cb3-8)    // 缩小到50%
[](#cb3-9)    long small_image = ReSize(ola, image, width/2, height/2);
[](#cb3-10)    if (small_image != 0) {
[](#cb3-11)        printf("图片缩小成功\n");
[](#cb3-12)        SaveImageFromPtr(ola, small_image, "D:\\test\\small.png");
[](#cb3-13)        FreeImagePtr(ola, small_image);
[](#cb3-14)    }
[](#cb3-15)
[](#cb3-16)    // 放大到200%
[](#cb3-17)    long large_image = ReSize(ola, image, width*2, height*2);
[](#cb3-18)    if (large_image != 0) {
[](#cb3-19)        printf("图片放大成功\n");
[](#cb3-20)        SaveImageFromPtr(ola, large_image, "D:\\test\\large.png");
[](#cb3-21)        FreeImagePtr(ola, large_image);
[](#cb3-22)    }
[](#cb3-23)
[](#cb3-24)    // 等比例缩放到指定宽度
[](#cb3-25)    int target_width = 800;
[](#cb3-26)    float scale = (float)target_width / width;
[](#cb3-27)    int target_height = (整型数)(height * scale);
[](#cb3-28)    long scaled_image = ReSize(ola, image, target_width, target_height);
[](#cb3-29)    if (scaled_image != 0) {
[](#cb3-30)        printf("等比例缩放成功\n");
[](#cb3-31)        SaveImageFromPtr(ola, scaled_image, "D:\\test\\scaled.png");
[](#cb3-32)        FreeImagePtr(ola, scaled_image);
[](#cb3-33)    }
[](#cb3-34)
[](#cb3-35)    FreeImagePtr(ola, image);
[](#cb3-36)}
[](#cb3-37)
[](#cb3-38)// 批量处理图片尺寸
[](#cb3-39)const int MAX_WIDTH = 1024;
[](#cb3-40)const int MAX_HEIGHT = 768;
[](#cb3-41)
[](#cb3-42)void ProcessImage(const char* input_path, const char* output_path) {
[](#cb3-43)    long image = LoadImage(ola, input_path);
[](#cb3-44)    if (image != 0) {
[](#cb3-45)        int width, height;
[](#cb3-46)        GetImageSize(ola, image, &width, &height);
[](#cb3-47)
[](#cb3-48)        // 如果图片超过最大尺寸，进行等比例缩放
[](#cb3-49)        if (width > MAX_WIDTH || height > MAX_HEIGHT) {
[](#cb3-50)            float scale_w = (float)MAX_WIDTH / width;
[](#cb3-51)            float scale_h = (float)MAX_HEIGHT / height;
[](#cb3-52)            float scale = scale_w < scale_h ? scale_w : scale_h;
[](#cb3-53)
[](#cb3-54)            int new_width = (整型数)(width * scale);
[](#cb3-55)            int new_height = (整型数)(height * scale);
[](#cb3-56)
[](#cb3-57)            long resized = ReSize(ola, image, new_width, new_height);
[](#cb3-58)            if (resized != 0) {
[](#cb3-59)                SaveImageFromPtr(ola, resized, output_path);
[](#cb3-60)                FreeImagePtr(ola, resized);
[](#cb3-61)            }
[](#cb3-62)        } else {
[](#cb3-63)            // 直接保存原图
[](#cb3-64)            SaveImageFromPtr(ola, image, output_path);
[](#cb3-65)        }
[](#cb3-66)
[](#cb3-67)        FreeImagePtr(ola, image);
[](#cb3-68)    }
[](#cb3-69)}
```

### 返回值

长整型数: - 0: 调整失败 - 非0: 调整成功，返回新图片的句柄

### 注意事项

- 调整后会返回新的图片句柄，原图片不会被修改

- 新图片句柄使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
释放内存

- 缩小图片通常不会损失太多质量，但过度放大可能会导致图片模糊

- 为保持图片比例，建议使用等比例缩放

- 如果需要更高级的缩放选项（如指定插值算法），可以使用 [ScalePixels](/图像处理/调整图片大小%20-%20ScalePixels.html)
函数

---

# 调整图片大小 - ScalePixels

### 函数简介

调整图片大小，按指定倍率放大图片像素。此函数可以对图片进行像素级别的放大，保持图片清晰度，适用于需要放大图片但保持清晰度的场景，如图像处理、UI设计等。

### 接口名称

```
ScalePixels
```

### DLL调用

```
long ScalePixels(long ola, long ptr, int scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `ptr` (长整型数): 原OLAImage对象的地址

- `scale` (整型数): 像素放大倍率，必须大于0

#### 示例:

```
[](#cb3-1)// 加载图片
[](#cb3-2)long imagePtr = LoadImage(ola, "/OLA/pic/pic.bmp");
[](#cb3-3)if (imagePtr != 0) {
[](#cb3-4)    // 将图片放大2倍
[](#cb3-5)    long scaledImagePtr = ScalePixels(ola, imagePtr, 2);
[](#cb3-6)    if (scaledImagePtr != 0) {
[](#cb3-7)        // 使用放大后的图片
[](#cb3-8)        // ...
[](#cb3-9)
[](#cb3-10)        // 使用完后释放内存
[](#cb3-11)        FreeImagePtr(ola, scaledImagePtr);
[](#cb3-12)    }
[](#cb3-13)
[](#cb3-14)    // 释放原图内存
[](#cb3-15)    FreeImagePtr(ola, imagePtr);
[](#cb3-16)}
```

### 返回值

长整型数: 返回放大后的OLAImage对象的地址。如果失败返回0。

### 注意事项

- 放大倍率必须大于0，否则可能导致程序异常

- 放大后的图片会占用更多内存，请注意内存使用

- 放大后的图片尺寸会相应增加，请注意处理大图片时的性能影响

- 图片使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口释放内存

- 原图片的内存需要单独释放，不会自动释放

- 放大后的图片会保持原图的清晰度，但可能会增加文件大小

- 建议在放大图片前检查内存是否充足

- 如果原图片指针无效，函数将返回0

---

# 转换颜色格式 - ConvertColor

## 函数简介

转换图像的颜色格式。此函数支持多种颜色格式转换，包括灰度转换、BGRA转RGBA、BGRA转BGR、BGRA转HSVA、BGRA转HSV等。适用于图像预处理、颜色空间转换等场景。

## 接口名称

```
ConvertColor
```

## DLL调用

```
long ConvertColor(long instance, long ptr, int type)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针，由图像处理函数返回 |
|

|
type |
整数型 |
转换类型：
0: 转为灰度
1: BGRA转RGBA
2: BGRA转BGR
3:
BGRA转HSVA
4: BGRA转HSV |
|

### 示例

```
[](#cb3-1)// 加载图像并转换为灰度
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\color.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    // 转换为灰度图
[](#cb3-5)    long grayImage = ConvertColor(ola, image, 0);
[](#cb3-6)    if (grayImage != 0) {
[](#cb3-7)        printf("图像已转换为灰度格式\n");
[](#cb3-8)        ShowImage(ola, grayImage);
[](#cb3-9)        FreeImagePtr(ola, grayImage);
[](#cb3-10)    }
[](#cb3-11)    FreeImagePtr(ola, image);
[](#cb3-12)}
[](#cb3-13)
[](#cb3-14)// BGRA转RGBA格式
[](#cb3-15)long image = LoadImage(ola, "D:\\test\\bgra.png");
[](#cb3-16)if (image != 0) {
[](#cb3-17)    // BGRA转RGBA
[](#cb3-18)    long rgbaImage = ConvertColor(ola, image, 1);
[](#cb3-19)    if (rgbaImage != 0) {
[](#cb3-20)        printf("BGRA已转换为RGBA格式\n");
[](#cb3-21)        FreeImagePtr(ola, rgbaImage);
[](#cb3-22)    }
[](#cb3-23)    FreeImagePtr(ola, image);
[](#cb3-24)}
[](#cb3-25)
[](#cb3-26)// BGRA转BGR格式
[](#cb3-27)long image = LoadImage(ola, "D:\\test\\bgra.png");
[](#cb3-28)if (image != 0) {
[](#cb3-29)    // BGRA转BGR
[](#cb3-30)    long bgrImage = ConvertColor(ola, image, 2);
[](#cb3-31)    if (bgrImage != 0) {
[](#cb3-32)        printf("BGRA已转换为BGR格式\n");
[](#cb3-33)        FreeImagePtr(ola, bgrImage);
[](#cb3-34)    }
[](#cb3-35)    FreeImagePtr(ola, image);
[](#cb3-36)}
[](#cb3-37)
[](#cb3-38)// BGRA转HSVA格式
[](#cb3-39)long image = LoadImage(ola, "D:\\test\\color.png");
[](#cb3-40)if (image != 0) {
[](#cb3-41)    // BGRA转HSVA
[](#cb3-42)    long hsvaImage = ConvertColor(ola, image, 3);
[](#cb3-43)    if (hsvaImage != 0) {
[](#cb3-44)        printf("BGRA已转换为HSVA格式\n");
[](#cb3-45)        FreeImagePtr(ola, hsvaImage);
[](#cb3-46)    }
[](#cb3-47)    FreeImagePtr(ola, image);
[](#cb3-48)}
[](#cb3-49)
[](#cb3-50)// BGRA转HSV格式
[](#cb3-51)long image = LoadImage(ola, "D:\\test\\color.png");
[](#cb3-52)if (image != 0) {
[](#cb3-53)    // BGRA转HSV
[](#cb3-54)    long hsvImage = ConvertColor(ola, image, 4);
[](#cb3-55)    if (hsvImage != 0) {
[](#cb3-56)        printf("BGRA已转换为HSV格式\n");
[](#cb3-57)        FreeImagePtr(ola, hsvImage);
[](#cb3-58)    }
[](#cb3-59)    FreeImagePtr(ola, image);
[](#cb3-60)}
[](#cb3-61)
[](#cb3-62)// 图像处理流程示例
[](#cb3-63)long screen = GetScreenDataPtr(ola, 0, 0, 1920, 1080);
[](#cb3-64)if (screen != 0) {
[](#cb3-65)    // 转换为灰度
[](#cb3-66)    long grayScreen = ConvertColor(ola, screen, 0);
[](#cb3-67)    if (grayScreen != 0) {
[](#cb3-68)        // 进行阈值化处理
[](#cb3-69)        long binaryScreen = Threshold(ola, grayScreen, 128.0, 255.0, 0);
[](#cb3-70)        if (binaryScreen != 0) {
[](#cb3-71)            printf("屏幕截图已处理为二值图像\n");
[](#cb3-72)            FreeImagePtr(ola, binaryScreen);
[](#cb3-73)        }
[](#cb3-74)        FreeImagePtr(ola, grayScreen);
[](#cb3-75)    }
[](#cb3-76)    FreeImagePtr(ola, screen);
[](#cb3-77)}
```

## 返回值

int64_t: 返回转换后的图像指针

## 注意事项

- 转换类型说明：

0: 转为灰度 - 适用于图像预处理、特征提取

- 1: BGRA转RGBA - 适用于OpenGL等图形库

- 2: BGRA转BGR - 适用于OpenCV等计算机视觉库

- 3: BGRA转HSVA - 适用于颜色分析、图像分割

- 4: BGRA转HSV - 适用于颜色识别、图像处理

- 转换后的图像需要手动释放内存

- 灰度转换会丢失颜色信息，但保留亮度信息

- HSV颜色空间更适合进行颜色分析和处理

- 建议在图像处理流程中合理使用颜色转换

- 与 [Threshold](/图像处理/图像阈值化%20-%20Threshold.html)
函数配合使用效果更佳

---

# 载入bmp图片 -
LoadImageFromBmpData

### 函数简介

将BMP图片载入缓存

### 接口名称

```
LoadImageFromBmpData
```

### DLL调用

```
long LoadImageFromBmpData(long ola, long data, long dataSize)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `data` (长整型数): 图片内存地址

- `dataSize` (长整型数): 图片的大小

#### 示例:

待补充…

### 返回值

长整型数:

拷贝后的的OLAImage对象的地址

**注意**：图片使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口进行释放

---

# 释放所有内存 - FreeImageAll

### 函数简介

释放所有已加载的图片内存。此函数会一次性释放所有通过图片加载函数（LoadImage）分配的内存，通常在程序退出或需要清理所有图片资源时使用。使用此函数可以避免逐个释放图片内存，但需要注意释放后所有图片句柄都将失效。

### 接口名称

```
FreeImageAll
```

### DLL调用

```
int FreeImageAll(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

```
[](#cb3-1)// 加载多个图片
[](#cb3-2)long images[10];
[](#cb3-3)int count = 0;
[](#cb3-4)
[](#cb3-5)// 加载一组图片
[](#cb3-6)for (int i = 0; i < 5; i++) {
[](#cb3-7)    char path[100];
[](#cb3-8)    sprintf(path, "D:\\test\\pic%d.png", i);
[](#cb3-9)    images[count] = LoadImage(ola, path);
[](#cb3-10)    if (images[count] != 0) {
[](#cb3-11)        count++;
[](#cb3-12)    }
[](#cb3-13)}
[](#cb3-14)
[](#cb3-15)// 创建一些新图片
[](#cb3-16)for (int i = 0; i < 3; i++) {
[](#cb3-17)    images[count] = CreateImage(ola, 100, 100);
[](#cb3-18)    if (images[count] != 0) {
[](#cb3-19)        count++;
[](#cb3-20)    }
[](#cb3-21)}
[](#cb3-22)
[](#cb3-23)printf("共加载和创建了 %d 个图片\n", count);
[](#cb3-24)
[](#cb3-25)// 使用这些图片进行处理
[](#cb3-26)// ...
[](#cb3-27)
[](#cb3-28)// 处理完成后，一次性释放所有图片内存
[](#cb3-29)int ret = FreeImageAll(ola);
[](#cb3-30)if (ret == 1) {
[](#cb3-31)    printf("所有图片内存释放成功\n");
[](#cb3-32)} else {
[](#cb3-33)    printf("释放内存失败\n");
[](#cb3-34)}
[](#cb3-35)
[](#cb3-36)// 注意：此时所有images数组中的句柄都已失效
[](#cb3-37)// 如果需要继续使用图片，需要重新加载
```

### 返回值

整型数: - 0: 释放失败 - 1: 释放成功

### 注意事项

- 调用此函数后，所有已加载的图片句柄都将失效，不能再使用

- 如果只需要释放特定图片的内存，请使用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
函数

- 此函数通常在以下情况使用：

程序退出前的清理工作

- 需要释放大量图片内存时

- 切换场景或重新加载所有资源时

- 释放后如果需要继续使用图片，必须重新加载

- 建议在调用此函数前，确保没有正在进行的图片处理操作

---

# 释放拼接实例 -
ImageStitchFree

## 函数简介

释放由 `ImageStitchCreate` 创建的拼接实例资源。

## 接口名称

```
ImageStitchFree
```

## DLL调用

```
int32_t ImageStitchFree(int64_t instance, int64_t imageStitch);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
imageStitch |
长整数型 |
拼接实例句柄。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t st = ImageStitchCreate(instance);
[](#cb3-3)int32_t ok = ImageStitchFree(instance, st);
[](#cb3-4)printf("free: %d\n", ok);
[](#cb3-5)DestroyCOLAPlugInterFace(instance);
```

## 返回值

0 失败，1 成功。

## 注意事项

- 释放前确保已不再使用该实例。

---

# 释放指定图片内存 -
FreeImagePtr

### 函数简介

释放指定图片句柄占用的内存。当不再需要使用某个图片时，必须调用此函数释放其占用的内存，否则会造成内存泄漏。此函数通常与
[LoadImage](/图像处理/加载图片%20-%20LoadImage.html)
等图片加载函数配对使用。

### 接口名称

```
FreeImagePtr
```

### DLL调用

```
int FreeImagePtr(long ola, long image_ptr)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `image_ptr` (长整型数):
要释放的图片句柄，由图片加载函数返回。

#### 示例:

```
[](#cb3-1)// 加载并使用图片，然后释放内存
[](#cb3-2)long image = LoadImage(ola, "D:\\test\\sample.png");
[](#cb3-3)if (image != 0) {
[](#cb3-4)    // 使用图片进行操作
[](#cb3-5)    int width, height;
[](#cb3-6)    GetImageSize(ola, image, &width, &height);
[](#cb3-7)    printf("图片大小：%d x %d\n", width, height);
[](#cb3-8)
[](#cb3-9)    // 操作完成后释放内存
[](#cb3-10)    int ret = FreeImagePtr(ola, image);
[](#cb3-11)    if (ret == 1) {
[](#cb3-12)        printf("图片内存释放成功\n");
[](#cb3-13)    } else {
[](#cb3-14)        printf("图片内存释放失败\n");
[](#cb3-15)    }
[](#cb3-16)}
[](#cb3-17)
[](#cb3-18)// 批量处理图片示例
[](#cb3-19)long images[10];
[](#cb3-20)int count = 0;
[](#cb3-21)
[](#cb3-22)// 加载多张图片
[](#cb3-23)for (int i = 0; i < 10; i++) {
[](#cb3-24)    char path[100];
[](#cb3-25)    sprintf(path, "D:\\test\\pic%d.png", i);
[](#cb3-26)    images[count] = LoadImage(ola, path);
[](#cb3-27)    if (images[count] != 0) {
[](#cb3-28)        count++;
[](#cb3-29)    }
[](#cb3-30)}
[](#cb3-31)
[](#cb3-32)// 使用图片进行处理
[](#cb3-33)// ...
[](#cb3-34)
[](#cb3-35)// 释放所有加载的图片
[](#cb3-36)for (int i = 0; i < count; i++) {
[](#cb3-37)    FreeImagePtr(ola, images[i]);
[](#cb3-38)}
```

### 返回值

整型数: - 0: 释放失败 - 1: 释放成功

### 注意事项

- 必须对每个成功加载的图片调用此函数进行释放，否则会造成内存泄漏

- 不要重复释放同一个图片句柄，这可能导致程序崩溃

- 释放后的图片句柄不能再使用，需要重新加载

- 如果需要释放所有已加载的图片，可以使用 [FreeImageAll](/图像处理/释放所有内存%20-%20FreeImageAll.html)
函数

- 对于通过 [LoadImagePath](/图像处理/加载文件夹下的所有图片%20-%20LoadImagePath.html)
加载的图片，应使用 [FreeImagePath](/图像处理/释放路径下图片内存%20-%20FreeImagePath.html)
函数释放

---

# 释放指定图片内存1 -
FreeImageData

### 函数简介

释放指定图片BMP等数据流格式地址

### 接口名称

```
FreeImageData
```

### DLL调用

```
int FreeImageData(long ola, long ptr)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `ptr` (长整型数): BMP等数据流格式地址

#### 示例:

待补充…

#### 返回值:

1:成功 0:失败

---

# 释放指定图片路径内存 -
FreeImagePath

### 函数简介

释放指定路径下的图片内存

### 接口名称

```
FreeImagePath
```

### DLL调用

```
int FreeImagePath(long ola, string path)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `path` (字符串): 待释放的图片的路径

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 颜色模型说明 - ColorModel

## 概述

`colorJson` /
颜色模型字符串用于在图像处理、图像识别、文字识别等接口中限定颜色范围。
本说明文档统一介绍所有支持的颜色表示方式，接口文档只需简单引用本页即可。

## 1. JSON
格式（原有写法，完全兼容）

```
[](#cb1-1)[
[](#cb1-2)  {
[](#cb1-3)    "StartColor": "3278FA",
[](#cb1-4)    "EndColor": "6496FF",
[](#cb1-5)    "Type": 0
[](#cb1-6)  },
[](#cb1-7)  {
[](#cb1-8)    "StartColor": "#AABBCC",
[](#cb1-9)    "EndColor": "#DDEEFF",
[](#cb1-10)    "Type": 1
[](#cb1-11)  }
[](#cb1-12)]
```

- `StartColor` / `EndColor` 支持以下形式：

`#AARRGGBB`

- `AARRGGBB`

- `#RRGGBB`

- `RRGGBB`

- `Type` 说明：

`0`：正常匹配（保留在颜色范围内的像素）

- `1`：反色匹配（保留在颜色范围外的像素）

- `2`：正常交集匹配

- `3`：反色交集匹配

## 2.
偏色区间格式：`"RRGGBB-DRDGDB"`

- 基本格式：`"基准色-偏移量"`，例如：

`"AABBCC-000000"`

- `"DDEEFF-202020"`

- 多个区间用 `|` 分隔，例如：

`"AABBCC-000000|DDEEFF-202020"`

- 含义：

左侧为基准色 `RRGGBB`

- 右侧 `DRDGDB` 表示每个通道允许的偏移范围

### 反色模式

- 在字符串前面加 `@` 即表示反色模式：

`"@AABBCC-000000|DDEEFF-202020"`

## 3.
颜色区间范围格式：`"RRGGBB~RRGGBB"`

- 基本格式：`"起始色~结束色"`，例如：

`"000000~FFFFFF"` 表示从 `#000000` 到
`#FFFFFF` 的连续颜色范围

- 支持多个区间，用 `|` 分隔，例如：

`"AABBCC~BBCCDD|AAAAAA~FFFFFF"`

### 反色模式

- 在字符串前面加 `@` 即表示反色模式：

`"@AABBCC~BBCCDD|AAAAAA~FFFFFF"`

## 4. 单独颜色格式

- 支持直接填写单个颜色值：

`#AARRGGBB`

- `AARRGGBB`

- `#RRGGBB`

- `RRGGBB`

- 支持多个颜色，用 `|` 组合，例如：

`"#FF0000|00FF00|0000FF"`

### 反色模式

- 在字符串前面加 `@` 表示对这些颜色进行反选：

`"@FF0000|00FF00"`

## 5. 使用建议

- 简单场景可直接使用单独颜色或颜色区间格式，便于书写。

- 需要精细控制时，推荐使用 JSON 格式并明确设置
`Type`。

- 不同接口中 `colorJson` 的业务含义略有差异（如过滤背景色 /
限制前景色），具体请参考对应接口文档的简要说明。

---

# 骨架化 - Skeletonize

## 函数简介

对二值图像进行骨架化处理，提取细化的骨架结构。

## 接口名称

```
Skeletonize
```

## DLL调用

```
int64_t Skeletonize(int64_t instance, int64_t ptr);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针（推荐二值图）。 |
|

### 示例

```
[](#cb3-1)long image = LoadImage(ola, "D:/test/bin.png");
[](#cb3-2)if (image) {
[](#cb3-3)    long result = Skeletonize(ola, image);
[](#cb3-4)    if (result) {
[](#cb3-5)        FreeImagePtr(ola, result);
[](#cb3-6)    }
[](#cb3-7)    FreeImagePtr(ola, image);
[](#cb3-8)}
```

## 返回值

返回骨架化后的图像句柄，失败返回0。

## 注意事项

- 骨架化对输入阈值化效果敏感，建议先做去噪与阈值化。

- 处理后的图像需调用 `FreeImagePtr` 释放。

---

# 高斯模糊 - GaussianBlur

## 函数简介

对图像执行高斯模糊，降低噪声并平滑图像。

## 接口名称

```
GaussianBlur
```

## DLL调用

```
int64_t GaussianBlur(int64_t instance, int64_t ptr, int32_t kernelSize);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针。 |
|

|
kernelSize |
整数型 |
高斯核大小（奇数）。 |
|

### 示例

```
[](#cb3-1)long image = LoadImage(ola, "D:/test/img.png");
[](#cb3-2)if (image) {
[](#cb3-3)    long result = GaussianBlur(ola, image, 5);
[](#cb3-4)    if (result) {
[](#cb3-5)        FreeImagePtr(ola, result);
[](#cb3-6)    }
[](#cb3-7)    FreeImagePtr(ola, image);
[](#cb3-8)}
```

## 返回值

返回处理后的图像句柄，失败返回0。

## 注意事项

- 处理后的图像需调用 `FreeImagePtr` 释放。

---

## 图像数据库

# 初始化OLA数据库 -
InitOlaDatabase

## 函数简介

初始化OLA数据库，执行必要的初始化操作，例如创建表、初始化数据等。

## 函数原型

```
[](#cb1-1)int InitOlaDatabase(long ola, const long db);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 初始化OLA数据库
[](#cb2-22)            int result = OLAServer.InitOlaDatabase(db);
[](#cb2-23)            if (result == 1)
[](#cb2-24)            {
[](#cb2-25)                Console.WriteLine("OLA数据库初始化成功。");
[](#cb2-26)            }
[](#cb2-27)            else
[](#cb2-28)            {
[](#cb2-29)                Console.WriteLine("OLA数据库初始化失败。");
[](#cb2-30)            }
[](#cb2-31)        }
[](#cb2-32)    }
[](#cb2-33)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 初始化OLA数据库
[](#cb3-14)result = OLAServer.InitOlaDatabase(db)
[](#cb3-15)if result == 1:
[](#cb3-16)    print("OLA数据库初始化成功。")
[](#cb3-17)else:
[](#cb3-18)    print("OLA数据库初始化失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 初始化OLA数据库
[](#cb4-33)olaplug_dll.InitOlaDatabase.argtypes = [c_void_p, c_void_p]
[](#cb4-34)olaplug_dll.InitOlaDatabase.restype = c_int32
[](#cb4-35)result = olaplug_dll.InitOlaDatabase(ola_obj, db)
[](#cb4-36)if result == 1:
[](#cb4-37)    print("OLA数据库初始化成功。")
[](#cb4-38)else:
[](#cb4-39)    print("OLA数据库初始化失败。")
```

## 注意事项

- 该函数用于初始化OLA数据库，通常包括创建必要的表、初始化默认数据等操作。

- 如果初始化失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保在数据库打开后调用此函数，否则可能导致未定义行为。

---

# 从目录初始化OLA图像 -
InitOlaImageFromDir

## 函数简介

从指定目录中加载图像文件，并将其初始化到OLA数据库中。可以选择是否覆盖已存在的图像数据。

## 函数原型

```
[](#cb1-1)int InitOlaImageFromDir(long ola, const long db, string dir, int cover);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `dirPath` (字符串): 图片目录路径。

- `cover` (布尔值): 是否覆盖已存在的图像数据。

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 从目录初始化OLA图像
[](#cb2-22)            string imageDir = "C:/images";
[](#cb2-23)            int cover = 1; // 覆盖已存在的图像数据
[](#cb2-24)            int result = OLAServer.InitOlaImageFromDir(db, imageDir, cover);
[](#cb2-25)            if (result == 1)
[](#cb2-26)            {
[](#cb2-27)                Console.WriteLine("OLA图像初始化成功。");
[](#cb2-28)            }
[](#cb2-29)            else
[](#cb2-30)            {
[](#cb2-31)                Console.WriteLine("OLA图像初始化失败。");
[](#cb2-32)            }
[](#cb2-33)        }
[](#cb2-34)    }
[](#cb2-35)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 从目录初始化OLA图像
[](#cb3-14)imageDir = "C:/images"
[](#cb3-15)cover = 1  # 覆盖已存在的图像数据
[](#cb3-16)result = OLAServer.InitOlaImageFromDir(db, imageDir, cover)
[](#cb3-17)if result == 1:
[](#cb3-18)    print("OLA图像初始化成功。")
[](#cb3-19)else:
[](#cb3-20)    print("OLA图像初始化失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 从目录初始化OLA图像
[](#cb4-33)imageDir = "C:/images"
[](#cb4-34)cover = 1  # 覆盖已存在的图像数据
[](#cb4-35)olaplug_dll.InitOlaImageFromDir.argtypes = [c_void_p, c_void_p, c_char_p, c_int32]
[](#cb4-36)olaplug_dll.InitOlaImageFromDir.restype = c_int32
[](#cb4-37)result = olaplug_dll.InitOlaImageFromDir(ola_obj, db, imageDir.encode('utf-8'), cover)
[](#cb4-38)if result == 1:
[](#cb4-39)    print("OLA图像初始化成功。")
[](#cb4-40)else:
[](#cb4-41)    print("OLA图像初始化失败。")
```

## 注意事项

- 该函数用于从指定目录中加载图像文件，并将其初始化到OLA数据库中。适用于批量导入图像数据的场景。

- `cover` 参数用于控制是否覆盖已存在的图像数据。设置为
`1` 时，会覆盖现有数据；设置为 `0`
时，会跳过已存在的图像。

- 如果初始化失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保目录路径正确，且图像文件格式受支持，否则可能导致初始化失败。

---

# 导入OLA图像 - ImportOlaImage

## 函数简介

将指定目录中的图像文件导入到OLA数据库中。可以选择是否覆盖已存在的图像数据。

## 函数原型

```
[](#cb1-1)int ImportOlaImage(long ola, const long db, string dir, string fileName, int cover);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `dir` (字符串): 图像文件所在的目录路径。

- `fileName` (字符串): 要导入的图像文件名。

- `cover` (布尔值): 是否覆盖已存在的图像数据。

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 导入OLA图像
[](#cb2-22)            string imageDir = "C:/images";
[](#cb2-23)            string fileName = "image.png";
[](#cb2-24)            int cover = 1; // 覆盖已存在的图像数据
[](#cb2-25)            int result = OLAServer.ImportOlaImage(db, imageDir, fileName, cover);
[](#cb2-26)            if (result == 1)
[](#cb2-27)            {
[](#cb2-28)                Console.WriteLine("OLA图像导入成功。");
[](#cb2-29)            }
[](#cb2-30)            else
[](#cb2-31)            {
[](#cb2-32)                Console.WriteLine("OLA图像导入失败。");
[](#cb2-33)            }
[](#cb2-34)        }
[](#cb2-35)    }
[](#cb2-36)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 导入OLA图像
[](#cb3-14)imageDir = "C:/images"
[](#cb3-15)fileName = "image.png"
[](#cb3-16)cover = 1  # 覆盖已存在的图像数据
[](#cb3-17)result = OLAServer.ImportOlaImage(db, imageDir, fileName, cover)
[](#cb3-18)if result == 1:
[](#cb3-19)    print("OLA图像导入成功。")
[](#cb3-20)else:
[](#cb3-21)    print("OLA图像导入失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 导入OLA图像
[](#cb4-33)imageDir = "C:/images"
[](#cb4-34)fileName = "image.png"
[](#cb4-35)cover = 1  # 覆盖已存在的图像数据
[](#cb4-36)olaplug_dll.ImportOlaImage.argtypes = [c_void_p, c_void_p, c_char_p, c_char_p, c_int32]
[](#cb4-37)olaplug_dll.ImportOlaImage.restype = c_int32
[](#cb4-38)result = olaplug_dll.ImportOlaImage(ola_obj, db, imageDir.encode('utf-8'), fileName.encode('utf-8'), cover)
[](#cb4-39)if result == 1:
[](#cb4-40)    print("OLA图像导入成功。")
[](#cb4-41)else:
[](#cb4-42)    print("OLA图像导入失败。")
```

## 注意事项

- 该函数用于将指定目录中的图像文件导入到OLA数据库中，适用于单个图像文件的导入场景。

- `cover` 参数用于控制是否覆盖已存在的图像数据。设置为
`1` 时，会覆盖现有数据；设置为 `0`
时，会跳过已存在的图像。

- 如果导入失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保目录路径和文件名正确，且图像文件格式受支持，否则可能导致导入失败。

---

# 导出OLA图像到目录 -
ExportOlaImageDir

## 函数简介

将OLA数据库中的图像数据导出到指定目录。

## 函数原型

```
[](#cb1-1)int ExportOlaImageDir(long ola, const long db, string dir, string exportDir);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `dirPath` (字符串): 图片目录路径。

- `exportPath` (字符串): 导出路径。

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 导出OLA图像到目录
[](#cb2-22)            string imageDir = "C:/images";
[](#cb2-23)            string exportDir = "C:/exported_images";
[](#cb2-24)            int result = OLAServer.ExportOlaImageDir(db, imageDir, exportDir);
[](#cb2-25)            if (result == 1)
[](#cb2-26)            {
[](#cb2-27)                Console.WriteLine("OLA图像导出成功。");
[](#cb2-28)            }
[](#cb2-29)            else
[](#cb2-30)            {
[](#cb2-31)                Console.WriteLine("OLA图像导出失败。");
[](#cb2-32)            }
[](#cb2-33)        }
[](#cb2-34)    }
[](#cb2-35)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 导出OLA图像到目录
[](#cb3-14)imageDir = "C:/images"
[](#cb3-15)exportDir = "C:/exported_images"
[](#cb3-16)result = OLAServer.ExportOlaImageDir(db, imageDir, exportDir)
[](#cb3-17)if result == 1:
[](#cb3-18)    print("OLA图像导出成功。")
[](#cb3-19)else:
[](#cb3-20)    print("OLA图像导出失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 导出OLA图像到目录
[](#cb4-33)imageDir = "C:/images"
[](#cb4-34)exportDir = "C:/exported_images"
[](#cb4-35)olaplug_dll.ExportOlaImageDir.argtypes = [c_void_p, c_void_p, c_char_p, c_char_p]
[](#cb4-36)olaplug_dll.ExportOlaImageDir.restype = c_int32
[](#cb4-37)result = olaplug_dll.ExportOlaImageDir(ola_obj, db, imageDir.encode('utf-8'), exportDir.encode('utf-8'))
[](#cb4-38)if result == 1:
[](#cb4-39)    print("OLA图像导出成功。")
[](#cb4-40)else:
[](#cb4-41)    print("OLA图像导出失败。")
```

## 注意事项

- 该函数用于将OLA数据库中的图像数据导出到指定目录，适用于批量导出图像数据的场景。

- 如果导出失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保目录路径正确，且图像数据存在于数据库中，否则可能导致导出失败。

- 导出的图像文件将保存在 `exportDir`
指定的目录中，确保目标目录有足够的存储空间。

---

# 移除OLA图像 - RemoveOlaImage

## 函数简介

从OLA数据库中移除指定目录和文件名的图像数据。

## 函数原型

```
[](#cb1-1)int RemoveOlaImage(long ola, const long db, string dir, string fileName);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `dir` (字符串): 图像文件在数据库中的目录路径。

- `fileName` (字符串): 图像文件名。

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 移除OLA图像
[](#cb2-22)            string imageDir = "C:/images";
[](#cb2-23)            string fileName = "image.png";
[](#cb2-24)            int result = OLAServer.RemoveOlaImage(db, imageDir, fileName);
[](#cb2-25)            if (result == 1)
[](#cb2-26)            {
[](#cb2-27)                Console.WriteLine("OLA图像移除成功。");
[](#cb2-28)            }
[](#cb2-29)            else
[](#cb2-30)            {
[](#cb2-31)                Console.WriteLine("OLA图像移除失败。");
[](#cb2-32)            }
[](#cb2-33)        }
[](#cb2-34)    }
[](#cb2-35)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 移除OLA图像
[](#cb3-14)imageDir = "C:/images"
[](#cb3-15)fileName = "image.png"
[](#cb3-16)result = OLAServer.RemoveOlaImage(db, imageDir, fileName)
[](#cb3-17)if result == 1:
[](#cb3-18)    print("OLA图像移除成功。")
[](#cb3-19)else:
[](#cb3-20)    print("OLA图像移除失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 移除OLA图像
[](#cb4-33)imageDir = "C:/images"
[](#cb4-34)fileName = "image.png"
[](#cb4-35)olaplug_dll.RemoveOlaImage.argtypes = [c_void_p, c_void_p, c_char_p, c_char_p]
[](#cb4-36)olaplug_dll.RemoveOlaImage.restype = c_int32
[](#cb4-37)result = olaplug_dll.RemoveOlaImage(ola_obj, db, imageDir.encode('utf-8'), fileName.encode('utf-8'))
[](#cb4-38)if result == 1:
[](#cb4-39)    print("OLA图像移除成功。")
[](#cb4-40)else:
[](#cb4-41)    print("OLA图像移除失败。")
```

## 注意事项

- 该函数用于从OLA数据库中移除指定目录和文件名的图像数据，适用于删除单个图像数据的场景。

- 如果移除失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保目录路径和文件名正确，且图像数据存在于数据库中，否则可能导致移除失败。

---

# 从目录移除OLA图像 -
RemoveOlaImageFromDir

## 函数简介

从OLA数据库中移除指定目录中的图像数据。

## 函数原型

```
[](#cb1-1)int RemoveOlaImageFromDir(long ola, const long db, string dir);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `dir` (字符串): 图片目录路径。

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 从目录移除OLA图像
[](#cb2-22)            string imageDir = "C:/images";
[](#cb2-23)            int result = OLAServer.RemoveOlaImageFromDir(db, imageDir);
[](#cb2-24)            if (result == 1)
[](#cb2-25)            {
[](#cb2-26)                Console.WriteLine("OLA图像移除成功。");
[](#cb2-27)            }
[](#cb2-28)            else
[](#cb2-29)            {
[](#cb2-30)                Console.WriteLine("OLA图像移除失败。");
[](#cb2-31)            }
[](#cb2-32)        }
[](#cb2-33)    }
[](#cb2-34)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 从目录移除OLA图像
[](#cb3-14)imageDir = "C:/images"
[](#cb3-15)result = OLAServer.RemoveOlaImageFromDir(db, imageDir)
[](#cb3-16)if result == 1:
[](#cb3-17)    print("OLA图像移除成功。")
[](#cb3-18)else:
[](#cb3-19)    print("OLA图像移除失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 从目录移除OLA图像
[](#cb4-33)imageDir = "C:/images"
[](#cb4-34)olaplug_dll.RemoveOlaImageFromDir.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-35)olaplug_dll.RemoveOlaImageFromDir.restype = c_int32
[](#cb4-36)result = olaplug_dll.RemoveOlaImageFromDir(ola_obj, db, imageDir.encode('utf-8'))
[](#cb4-37)if result == 1:
[](#cb4-38)    print("OLA图像移除成功。")
[](#cb4-39)else:
[](#cb4-40)    print("OLA图像移除失败。")
```

## 注意事项

- 该函数用于从OLA数据库中移除指定目录中的图像数据，适用于批量删除图像数据的场景。

- 如果移除失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保目录路径正确，且图像数据存在于数据库中，否则可能导致移除失败。

---

# 获取OLA图像 - GetOlaImage

## 函数简介

从OLA数据库中获取指定目录和文件名的图像数据，返回图像对象的指针。

## 函数原型

```
[](#cb1-1)long GetOlaImage(long ola, const long db, string dir, string fileName);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `dirPath` (字符串): 图片目录路径。

- `fileName` (字符串): 图片文件名。

## 返回值

- 返回值：图像对象的指针。如果操作失败，返回 `0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 获取OLA图像
[](#cb2-22)            string imageDir = "C:/images";
[](#cb2-23)            string fileName = "image.png";
[](#cb2-24)            long imagePtr = OLAServer.GetOlaImage(db, imageDir, fileName);
[](#cb2-25)            if (imagePtr != 0)
[](#cb2-26)            {
[](#cb2-27)                Console.WriteLine("OLA图像获取成功。");
[](#cb2-28)                // 使用图像对象进行后续操作
[](#cb2-29)            }
[](#cb2-30)            else
[](#cb2-31)            {
[](#cb2-32)                Console.WriteLine("OLA图像获取失败。");
[](#cb2-33)            }
[](#cb2-34)        }
[](#cb2-35)    }
[](#cb2-36)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 获取OLA图像
[](#cb3-14)imageDir = "C:/images"
[](#cb3-15)fileName = "image.png"
[](#cb3-16)imagePtr = OLAServer.GetOlaImage(db, imageDir, fileName)
[](#cb3-17)if imagePtr != 0:
[](#cb3-18)    print("OLA图像获取成功。")
[](#cb3-19)    # 使用图像对象进行后续操作
[](#cb3-20)else:
[](#cb3-21)    print("OLA图像获取失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 获取OLA图像
[](#cb4-33)imageDir = "C:/images"
[](#cb4-34)fileName = "image.png"
[](#cb4-35)olaplug_dll.GetOlaImage.argtypes = [c_void_p, c_void_p, c_char_p, c_char_p]
[](#cb4-36)olaplug_dll.GetOlaImage.restype = c_void_p
[](#cb4-37)imagePtr = olaplug_dll.GetOlaImage(ola_obj, db, imageDir.encode('utf-8'), fileName.encode('utf-8'))
[](#cb4-38)if imagePtr != 0:
[](#cb4-39)    print("OLA图像获取成功。")
[](#cb4-40)    # 使用图像对象进行后续操作
[](#cb4-41)else:
[](#cb4-42)    print("OLA图像获取失败。")
```

## 注意事项

- 该函数用于从OLA数据库中获取指定目录和文件名的图像数据，适用于从数据库中检索图像的场景。

- 如果图像不存在或操作失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保目录路径和文件名正确，且图像数据存在于数据库中，否则可能导致获取失败。

- 使用完返回的图像对象指针后，应妥善处理资源，避免内存泄漏。

---

## 图像识别

# 匹配动画窗口 -
MatchAnimationFromPath

### 函数简介

匹配动画窗口，可用于GIF动画识别。可在识别指定时间内动图。查找到立马返回结果，返回相对绑定窗口坐标坐标

识别结果最长等待时间为time+1000ms

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

返回数据类型解析:

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

### 接口名称

```
MatchAnimationFromPath
```

### DLL调用

```
long MatchAnimationFromPath(long ola, int x1, int y1, int x2, int y2, string templ, double matchVal, int type, double angle, double scale,int delay, int  time, int threadCount)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 查找区域的左上角X坐标。

- `y1` (整型数): 查找区域的左上角Y坐标。

- `x2` (整型数): 查找区域的右下角X坐标。

- `y2` (整型数): 查找区域的右下角Y坐标。

- `templ` (字符串):
模板图片的路径，可以是多个图片,比如”test.bmp|test2.bmp|test3.bmp”。

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1。

- `type` (整型数): 匹配类型：

1：灰度匹配，速度快

- 2：彩色匹配

- 3：透明匹配

- 4：透明彩色权重匹配

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续进行匹配,直到匹配成功,角度越小匹配次数越多时间越长。0为不旋转速度最快。

- `scale` (双精度浮点数): 窗口缩放比例，默认为1 可以通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口读取当前窗口缩放。

- `delay` (整型数): 动画间隔，单位毫秒。

- `time` (整型数): 总共识别多久的动画，单位毫秒。

- `threadCount` (整型数):
用于查找的线程数线程数根据delay帧率自行调整，过小会导致识别时间到期未识别完，过大会导致CPU占用过大。

#### 示例:

待补充…

### 返回值

字符串:

返回匹配结果，如

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 匹配动画窗口1 -
MatchAnimationFromPtr

### 函数简介

匹配动画窗口，可用于GIF动画识别。可在识别指定时间内动图。查找到立马返回结果，返回相对绑定窗口坐标坐标

识别结果最长等待时间为time + 1000ms

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

返回数据类型解析:

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

### 接口名称

```
MatchAnimationFromPtr
```

### DLL调用

```
long MatchAnimationFromPtr(long ola, int x1, int y1, int x2, int y2, long templ, double matchVal, int type, double angle, double scale, int delay, int time, int threadCount)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `templ` (长整型数): OLAImage对象的地址，由[LoadImage](/图像处理/加载图片%20-%20LoadImage.html)等接口生成

- `matchVal` (双精度浮点数):
相似度阈值，范围0-1，如0.85表示85%相似度

- `type` (整型数): 匹配类型

1：灰度匹配，速度快

- 2：彩色匹配

- 3：透明匹配

- 4：透明彩色权重匹配

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续匹配，直到匹配成功。角度越小匹配次数越多，时间越长。0为不旋转，速度最快

- `scale` (双精度浮点数): 窗口缩放比例，默认为1。可通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口获取当前窗口缩放

- `delay` (整型数): 动画帧间隔，单位毫秒

- `time` (整型数): 总识别时间，单位毫秒

- `threadCount` (整型数):
用于查找的线程数。线程数需要根据delay帧率自行调整：

过小会导致识别时间到期未识别完

- 过大会导致CPU占用过大

#### 示例:

```
[](#cb4-1)// 创建OLA对象
[](#cb4-2)long ola = CreateCOLAPlugInterFace();
[](#cb4-3)
[](#cb4-4)// 加载模板图片
[](#cb4-5)long templ = LoadImage(ola, "animation.bmp");
[](#cb4-6)
[](#cb4-7)// 执行动画匹配
[](#cb4-8)long ret = MatchAnimationFromPtr(ola, 0, 0, 0, 0, templ, 0.85, 1, 45.0, 1.0, 20, 1000, 5);
[](#cb4-9)
[](#cb4-10)// 检查操作是否成功
[](#cb4-11)if (ret != 0) {
[](#cb4-12)    // 获取匹配结果
[](#cb4-13)    char* result = (char*)ret;
[](#cb4-14)    printf("匹配结果: %s\n", result);
[](#cb4-15)
[](#cb4-16)    // 释放返回的字符串内存
[](#cb4-17)    FreeStringPtr(result);
[](#cb4-18)} else {
[](#cb4-19)    // 匹配失败
[](#cb4-20)}
[](#cb4-21)
[](#cb4-22)// 释放模板图片内存
[](#cb4-23)FreeImagePtr(ola, templ);
```

### 注意事项

- 当x1, y1, x2, y2都传0时，将搜索整个窗口客户区

- 识别结果最长等待时间为time + 1000ms

- 匹配类型的选择：

灰度匹配速度最快，但精度较低

- 彩色匹配精度较高，但速度较慢

- 透明匹配适用于带透明通道的图片

- 线程数的选择：

建议根据动画帧率和CPU核心数来设置

- 一般建议设置为CPU核心数的1-2倍

- 角度参数影响匹配时间和精度：

角度越小，匹配次数越多，时间越长

- 角度为0时速度最快，但可能错过旋转的目标

- 缩放比例应与窗口实际缩放比例一致

- DLL调用返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放内存

- 返回的坐标是相对于绑定窗口客户区的坐标

### 相关函数

- [LoadImage](/图像处理/加载图片%20-%20LoadImage.html):
加载图片

- [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html):
释放图片内存

- [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html):
释放字符串内存

- [GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html):
获取窗口缩放比例

---

# 匹配图片 -
MatchImageFromPathAll

### 函数简介

匹配所有符合模板图片的位置信息

返回数据类型解析:

```
[{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}]
```

### 接口名称

```
MatchImageFromPathAll
```

### DLL调用

```
long MatchImageFromPathAll(long ola, string source, string templ, double matchVal, int type, double angle, double scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `source` (字符串): 源图片的路径

- `templ` (字符串):
模板图片的路径，可以是多个图片，比如”test.bmp|test2.bmp|test3.bmp”

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1

- `type` (整型数): 匹配类型：

灰度匹配，速度快

- 彩色匹配

- 透明匹配

- 透明彩色权重匹配

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续进行匹配，直到匹配成功，角度越小匹配次数越多时间越长。0为不旋转速度最快

- `scale` (双精度浮点数): 源图缩放比例，默认为1，可以通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口读取当前窗口缩放

#### 示例:

待补充…

### 返回值

字符串:

返回匹配结果，如

```
[{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
},
{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
}
]
```

**注意：**

多图识别时Index字段标识是第几个图片返回的结果索引从0开始

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 匹配图片1 -
MatchImageFromPath

### 函数简介

匹配符合模板图片的坐标，默认返回最优结果

返回数据类型解析:

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

### 接口名称

```
MatchImageFromPath
```

### DLL调用

```
long MatchImageFromPath(long ola, string source, string templ, double matchVal, int type, double angle, double scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `source` (字符串): 源图片的路径

- `templ` (字符串):
模板图片的路径，可以是多个图片，比如”test.bmp|test2.bmp|test3.bmp”

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1

- `type` (整型数): 匹配类型：

灰度匹配，速度快

- 彩色匹配

- 透明匹配

- 透明彩色权重匹配

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续进行匹配，直到匹配成功，角度越小匹配次数越多时间越长。0为不旋转速度最快

- `scale` (双精度浮点数): 窗口缩放比例，默认为1，可以通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口读取当前窗口缩放

#### 示例:

待补充…

### 返回值

字符串:

返回匹配结果，如

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

**注意：**

多图识别时Index字段标识是第几个图片返回的结果索引从0开始

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 匹配图片2 -
MatchImageFromPtrAll

### 函数简介

匹配所有符合模板图片的位置信息

返回数据类型解析:

```
[{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}]
```

### 接口名称

```
MatchImageFromPtrAll
```

### DLL调用

```
long MatchImageFromPtrAll(long ola, long source, long templ, double matchVal, int type, double angle, double scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `source` (长整型数): OLAImage对象的地址

- `templ` (长整型数): OLAImage对象的地址，由[LoadImage](/图像处理/加载图片%20-%20LoadImage.html)
等接口生成

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1

- `type` (整型数): 匹配类型：

灰度匹配，速度快

- 彩色匹配

- 透明匹配

- 透明彩色权重匹配

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续进行匹配，直到匹配成功，角度越小匹配次数越多时间越长。0为不旋转速度最快

- `scale` (双精度浮点数): 源图缩放比例，默认为1，可以通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口读取当前窗口缩放

#### 示例:

待补充…

### 返回值

字符串:

返回匹配结果，如

```
[{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
},
{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
}
]
```

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 匹配图片3 -
MatchImageFromPtr

### 函数简介

匹配符合模板图片的坐标，默认返回最优结果

返回数据类型解析:

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

### 接口名称

```
MatchImageFromPtr
```

### DLL调用

```
long MatchImageFromPtr(long ola, long source, long templ, double matchVal, int type, double angle, double scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `source` (长整型数): OLAImage对象的地址

- `templ` (长整型数): OLAImage对象的地址，由[LoadImage](/图像处理/加载图片%20-%20LoadImage.html)
等接口生成

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1

- `type` (整型数): 匹配类型：

灰度匹配，速度快

- 彩色匹配

- 透明匹配

- 透明彩色权重匹配

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续进行匹配，直到匹配成功，角度越小匹配次数越多时间越长。0为不旋转速度最快

- `scale` (双精度浮点数): 窗口缩放比例，默认为1，可以通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口读取当前窗口缩放

#### 示例:

待补充…

### 返回值

字符串:

返回匹配结果，如

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 匹配图片4 -
MatchImagePtrFromPath

### 函数简介

匹配符合模板图片的坐标，默认返回最优结果

返回数据类型解析:

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

### 接口名称

```
MatchImagePtrFromPath
```

### DLL调用

```
long MatchImagePtrFromPath(long ola, long source, string templ, double matchVal, int type, double angle, double scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `source` (长整型数): OLAImage对象的地址

- `templ` (字符串):
模板图片的路径，可以是多个图片，比如”test.bmp|test2.bmp|test3.bmp”

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1

- `type` (整型数): 匹配类型：

灰度匹配，速度快

- 彩色匹配

- 透明匹配

- 透明彩色权重匹配

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续进行匹配，直到匹配成功，角度越小匹配次数越多时间越长。0为不旋转速度最快

- `scale` (双精度浮点数): 窗口缩放比例，默认为1，可以通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口读取当前窗口缩放

#### 示例:

```
[](#cb4-1)// 加载源图片
[](#cb4-2)long sourceImg = ola.LoadImage("source.bmp");
[](#cb4-3)
[](#cb4-4)// 匹配图片，使用灰度匹配，相似度0.85，不旋转
[](#cb4-5)string result = ola.MatchImagePtrFromPath(sourceImg, "template.bmp", 0.85, 1, 0.0, 1.0);
[](#cb4-6)
[](#cb4-7)    // 解析JSON结果
[](#cb4-8)    // {
[](#cb4-9)    //     "MatchVal": 0.85,//数据相似度
[](#cb4-10)    //     "MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
[](#cb4-11)    //     "Index": 0,//多图识别时的返回索引
[](#cb4-12)    //     "Angle": 45.0,//识别结果角度
[](#cb4-13)    //     "X": 100,//识别结果X坐标
[](#cb4-14)    //     "Y": 200,//识别结果Y坐标
[](#cb4-15)    //     "Width":100,//识别结果宽度
[](#cb4-16)    //     "Height":100//识别结果高度
[](#cb4-17)    // }
[](#cb4-18)
[](#cb4-19)// 使用完后释放图片内存
[](#cb4-20)ola.FreeImagePtr(sourceImg);
```

### 返回值

字符串: 返回JSON格式的匹配结果，包含以下字段： -
`MatchVal` (双精度浮点数): 实际匹配的相似度值 -
`MatchState` (boolean): 是否匹配成功 - `Index`
(整型数): 多图匹配时的图片索引，从0开始 - `Angle`
(双精度浮点数): 匹配到的图像旋转角度 - `X`: 匹配点X坐标 -
`Y`: 匹配点Y坐标 - `Width`: 匹配模板宽度 -
`Height`: 匹配模板高度

**注意**： -
多图识别时，Index字段标识是第几个图片返回的结果，索引从0开始 -
DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

---

# 匹配图片5 -
MatchImagePtrFromPathAll

### 函数简介

匹配所有符合模板图片的位置信息

返回数据类型解析:

```
[{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}]
```

### 接口名称

```
MatchImagePtrFromPathAll
```

### DLL调用

```
long MatchImagePtrFromPathAll(long ola, long source, string templ, double matchVal, int type, double angle, double scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `source` (长整型数): OLAImage对象的地址

- `templ` (字符串):
模板图片的路径，可以是多个图片，比如”test.bmp|test2.bmp|test3.bmp”

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1

- `type` (整型数): 匹配类型：

灰度匹配，速度快

- 彩色匹配

- 透明匹配

- 透明彩色权重匹配

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续进行匹配，直到匹配成功，角度越小匹配次数越多时间越长。0为不旋转速度最快

- `scale` (双精度浮点数): 源图缩放比例，默认为1，可以通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口读取当前窗口缩放

#### 示例:

```
[](#cb4-1)// 加载源图片
[](#cb4-2)long sourceImg = ola.LoadImage("source.bmp");
[](#cb4-3)
[](#cb4-4)// 匹配所有符合条件的位置，使用灰度匹配，相似度0.85，不旋转
[](#cb4-5)string result = ola.MatchImagePtrFromPathAll(sourceImg, "template.bmp", 0.85, 1, 0.0, 1.0);
[](#cb4-6)
[](#cb4-7)// 解析返回的JSON结果
[](#cb4-8)// 返回格式示例：
[](#cb4-9)// [{
[](#cb4-10)//     "MatchVal": 0.85,//数据相似度
[](#cb4-11)//     "MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
[](#cb4-12)//     "Index": 0,//多图识别时的返回索引
[](#cb4-13)//     "Angle": 45.0,//识别结果角度
[](#cb4-14)//     "X": 100,//识别结果X坐标
[](#cb4-15)//     "Y": 200,//识别结果Y坐标
[](#cb4-16)//     "Width":100,//识别结果宽度
[](#cb4-17)//     "Height":100//识别结果高度
[](#cb4-18)// },
[](#cb4-19)// {
[](#cb4-20)//     "MatchVal": 0.85,//数据相似度
[](#cb4-21)//     "MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
[](#cb4-22)//     "Index": 0,//多图识别时的返回索引
[](#cb4-23)//     "Angle": 45.0,//识别结果角度
[](#cb4-24)//     "X": 100,//识别结果X坐标
[](#cb4-25)//     "Y": 200,//识别结果Y坐标
[](#cb4-26)//     "Width":100,//识别结果宽度
[](#cb4-27)//     "Height":100//识别结果高度
[](#cb4-28)// }]
[](#cb4-29)
[](#cb4-30)// 使用完后释放图片内存
[](#cb4-31)ola.FreeImagePtr(sourceImg);
```

### 返回值

字符串: 返回JSON数组格式的匹配结果，每个元素包含以下字段： -
`MatchVal` (双精度浮点数): 实际匹配的相似度值 -
`MatchState` (boolean): 是否匹配成功 - `Index`
(整型数): 多图匹配时的图片索引，从0开始 - `Angle`
(双精度浮点数): 匹配到的图像旋转角度 - `X`: 匹配点X坐标 -
`Y`: 匹配点Y坐标 - `Width`: 匹配模板宽度 -
`Height`: 匹配模板高度

**注意**： -
多图识别时，Index字段标识是第几个图片返回的结果，索引从0开始 -
DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存 - 返回结果按匹配相似度从高到低排序

#### 示例:

```
source = LoadImage("OLA/pic/source.bmp")
ret = MatchImagePtrFromPathAll(source,"OLA/pic/pic.bmp", 0.85, 1, 50.0, 1.0)
messagebox(ret) #ret为json字符串
```

### 返回值

字符串:

返回匹配结果，如

```
[{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
},
{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
}
]
```

**注意：**

多图识别时Index字段标识是第几个图片返回的结果索引从0开始

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 匹配绑定窗口图片 -
MatchWindowsFromPathAll

### 函数简介

匹配所有符合模板图片的位置信息，返回相对绑定窗口坐标坐标

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

返回数据类型解析:

```
[{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}]
```

### 接口名称

```
MatchWindowsFromPathAll
```

### DLL调用

```
long MatchWindowsFromPathAll(long ola, int x1, int y1, int x2, int y2, string templ, double matchVal, int type, double angle, double scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `templ` (字符串):
模板图片的路径，可以是多个图片,比如”test.bmp|test2.bmp|test3.bmp”

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1

- `type` (整型数): 匹配类型：

灰度匹配，速度快

- 彩色匹配

- 透明匹配

- 透明彩色权重匹配

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续进行匹配,直到匹配成功,角度越小匹配次数越多时间越长。0为不旋转速度最快

- `scale` (双精度浮点数): 窗口缩放比例，默认为1，可以通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口读取当前窗口缩放

#### 示例:

待补充…

### 返回值

字符串:

返回匹配结果，如

```
[{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
},
{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
}
]
```

**注意：**
多图识别时Index字段标识是第几个图片返回的结果索引从0开始

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 匹配绑定窗口图片1 -
MatchWindowsFromPtr

### 函数简介

匹配符合模板图片的坐标，返回相对绑定窗口坐标坐标，默认返回最优结果

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

返回数据类型解析:

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

### 接口名称

```
MatchWindowsFromPtr
```

### DLL调用

```
long MatchWindowsFromPtr(long ola, int x1, int y1, int x2, int y2, long templ, double matchVal, int type, double angle, double scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 查找区域的左上角X坐标。

- `y1` (整型数): 查找区域的左上角Y坐标。

- `x2` (整型数): 查找区域的右下角X坐标。

- `y2` (整型数): 查找区域的右下角Y坐标。

- `templ` (长整型数): OLAImage对象的地址,由[LoadImage](/图像处理/加载图片%20-%20LoadImage.html)
等接口生成。

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1。

- `type` (整型数): 匹配类型：

1：灰度匹配，速度快

- 2：彩色匹配

- 3：透明匹配

- 4：透明彩色权重匹配

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续进行匹配,直到匹配成功,角度越小匹配次数越多时间越长。0为不旋转速度最快。

- `scale` (双精度浮点数): 窗口缩放比例，默认为1 可以通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口读取当前窗口缩放。

#### 示例:

待补充…

### 返回值

字符串:

返回匹配结果，如

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 匹配绑定窗口图片2 -
MatchWindowsFromPtrAll

### 函数简介

匹配所有符合模板图片的坐标，返回相对绑定窗口坐标坐标

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

返回数据类型解析:

```
[{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}]
```

### 接口名称

```
MatchWindowsFromPtrAll
```

### DLL调用

```
long MatchWindowsFromPtrAll(long ola, int x1, int y1, int x2, int y2, long templ, double matchVal, int type, double angle, double scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `templ` (长整型数): OLAImage对象的地址，由[LoadImage](/图像处理/加载图片%20-%20LoadImage.html)
等接口生成

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1

- `type` (整型数): 匹配类型：

灰度匹配，速度快

- 彩色匹配

- 透明匹配

- 透明彩色权重匹配

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续进行匹配,直到匹配成功,角度越小匹配次数越多时间越长。0为不旋转速度最快

- `scale` (双精度浮点数): 窗口缩放比例，默认为1，可以通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口读取当前窗口缩放

#### 示例:

待补充…

### 返回值

字符串:

返回匹配结果，如

```
[{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
},
{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
}
]
```

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 匹配绑定窗口图片3 -
MatchWindowsFromPath

### 函数简介

匹配符合模板图片的坐标，返回相对绑定窗口坐标坐标，默认返回最优结果

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

返回数据类型解析:

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

### 接口名称

```
MatchWindowsFromPath
```

### DLL调用

```
long MatchWindowsFromPath(long ola, int x1, int y1, int x2, int y2, string templ, double matchVal, int type, double angle, double scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `templ` (字符串):
模板图片的路径，可以是多个图片,比如”test.bmp|test2.bmp|test3.bmp”

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1

- `type` (整型数): 匹配类型：

灰度匹配，速度快

- 彩色匹配

- 透明匹配

- 透明彩色权重匹配

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续进行匹配,直到匹配成功,角度越小匹配次数越多时间越长。0为不旋转速度最快

- `scale` (双精度浮点数): 窗口缩放比例，默认为1，可以通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口读取当前窗口缩放

#### 示例:

待补充…

### 返回值

字符串:

返回匹配结果，如

```
{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
}
```

**注意：**

多图识别时Index字段标识是第几个图片返回的结果索引从0开始

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 匹配绑定窗口图片4
- MatchWindowsThresholdFromPtr

### 函数简介

二值化后匹配符合模板图片的坐标，返回相对绑定窗口坐标坐标，默认返回最优结果

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

返回数据类型解析:

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

### 接口名称

```
MatchWindowsThresholdFromPtr
```

### DLL调用

```
long MatchWindowsThresholdFromPtr(long ola, int x1, int y1, int x2, int y2, string colorJson, long templ, double matchVal, double angle, double scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `colorJson` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `templ` (长整型数): OLAImage对象的地址，由[LoadImage](/图像处理/加载图片%20-%20LoadImage.html)
等接口生成

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续进行匹配,直到匹配成功,角度越小匹配次数越多时间越长。0为不旋转速度最快

- `scale` (双精度浮点数): 窗口缩放比例，默认为1，可以通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口读取当前窗口缩放

#### 示例:

待补充…

### 返回值

字符串:

返回匹配结果，如

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 匹配绑定窗口图片5
- MatchWindowsThresholdFromPtrAll

### 函数简介

二值化后匹配符合模板图片的坐标，返回相对绑定窗口坐标坐标

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

返回数据类型解析:

```
[{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}]
```

### 接口名称

```
MatchWindowsThresholdFromPtrAll
```

### DLL调用

```
long MatchWindowsThresholdFromPtrAll(long ola, int x1, int y1, int x2, int y2, string colorJson, long templ, double matchVal, double angle, double scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `colorJson` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `templ` (长整型数): OLAImage对象的地址，由[LoadImage](/图像处理/加载图片%20-%20LoadImage.html)
等接口生成

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续进行匹配,直到匹配成功,角度越小匹配次数越多时间越长。0为不旋转速度最快

- `scale` (双精度浮点数): 窗口缩放比例，默认为1，可以通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口读取当前窗口缩放

#### 示例:

待补充…

### 返回值

字符串:

返回匹配结果，如

```
[{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
},
{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
}
]
```

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 匹配绑定窗口图片6
- MatchWindowsThresholdFromPath

### 函数简介

在绑定窗口的指定区域内，通过二值化处理后匹配符合模板图片的坐标。此函数支持多模板匹配、旋转匹配和缩放匹配，返回相对绑定窗口的坐标位置。适用于需要精确图像识别的场景，如游戏自动化、界面测试等。

当x1, y1, x2, y2参数都传0时，将匹配窗口整个客户区。

### 接口名称

```
MatchWindowsThresholdFromPath
```

### DLL调用

```
long MatchWindowsThresholdFromPath(long ola, int x1, int y1, int x2, int y2, string colorJson, string templ, double matchVal, double angle, double scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `colorJson` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `templ` (字符串):
模板图片的路径，支持多个图片，用”|“分隔，如”test.bmp|test2.bmp|test3.bmp”

- `matchVal` (双精度浮点数):
相似度阈值，范围0-1，如0.85表示85%相似度

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续匹配，直到匹配成功。角度越小匹配次数越多，时间越长。0表示不旋转，速度最快

- `scale` (双精度浮点数): 窗口缩放比例，默认为1。可通过 [GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)
接口获取当前窗口缩放比例

#### 示例:

```
[](#cb3-1)// 定义颜色范围
[](#cb3-2)string colorJson = R"([
[](#cb3-3)    {
[](#cb3-4)        "StartColor": "3278FA",
[](#cb3-5)        "EndColor": "6496FF",
[](#cb3-6)        "Type": 0
[](#cb3-7)    },
[](#cb3-8)    {
[](#cb3-9)        "StartColor": "FF0000",
[](#cb3-10)        "EndColor": "FF3333",
[](#cb3-11)        "Type": 1
[](#cb3-12)    }
[](#cb3-13)])";
[](#cb3-14)
[](#cb3-15)// 匹配图片
[](#cb3-16)long resultPtr = MatchWindowsThresholdFromPath(ola, 0, 0, 800, 600, colorJson, "templates/button.bmp", 0.85, 45.0, 1.0);
[](#cb3-17)if (resultPtr != 0) {
[](#cb3-18)    string result = GetStringFromPtr(resultPtr);
[](#cb3-19)    printf("匹配结果: %s\n", result.c_str());
[](#cb3-20)
[](#cb3-21)    // 解析JSON结果
[](#cb3-22)    // {
[](#cb3-23)    //     "MatchVal": 0.85,//数据相似度
[](#cb3-24)    //     "MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
[](#cb3-25)    //     "Index": 0,//多图识别时的返回索引
[](#cb3-26)    //     "Angle": 45.0,//识别结果角度
[](#cb3-27)    //     "X": 100,//识别结果X坐标
[](#cb3-28)    //     "Y": 200,//识别结果Y坐标
[](#cb3-29)    //     "Width":100,//识别结果宽度
[](#cb3-30)    //     "Height":100//识别结果高度
[](#cb3-31)    // }
[](#cb3-32)
[](#cb3-33)    // 释放字符串内存
[](#cb3-34)    FreeStringPtr(ola, resultPtr);
[](#cb3-35)}
```

### 返回值

字符串: 返回JSON格式的匹配结果，包含以下字段： -
`MatchVal`: 数据相似度，范围0-1 - `MatchState`:
是否大于指定精度，用于快速判断识别结果 - `Index`:
多图识别时的返回索引 - `Angle`: 识别结果角度 -
`X`: 匹配点X坐标 - `Y`: 匹配点Y坐标 -
`Width`: 匹配模板宽度 - `Height`: 匹配模板高度

### 注意事项

- 颜色值必须使用RRGGBB格式的十六进制字符串

- 支持多个颜色范围的指定，每个范围可以设置不同的匹配类型

- 颜色匹配类型说明：

0: 正常匹配，保留在颜色范围内的像素

- 1: 反色匹配，保留在颜色范围外的像素

- 2: 正常交集匹配，保留在颜色范围内的像素取交集

- 3: 反色交集匹配，保留在颜色范围外的像素取交集

- 模板图片路径支持多个图片，用”|“分隔

- 相似度阈值范围必须在0-1之间

- 旋转角度越小，匹配次数越多，耗时越长

- 窗口缩放比例必须与实际情况相符

- DLL调用时，返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

- 建议在使用前检查参数的有效性

- 处理大图片时注意性能影响

- 返回的坐标是相对于绑定窗口的坐标

- 如果匹配失败，MatchState将为false

---

# 匹配绑定窗口图片7
- MatchWindowsThresholdFromPathAll

### 函数简介

二值化后匹配符合模板图片的坐标，返回相对绑定窗口坐标坐标

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

返回数据类型解析:

```
[{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}]
```

### 接口名称

```
MatchWindowsThresholdFromPathAll
```

### DLL调用

```
long MatchWindowsThresholdFromPathAll(long ola, int x1, int y1, int x2, int y2, string colorJson, string templ, double matchVal, double angle, double scale)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `x1` (整型数): 查找区域的左上角X坐标

- `y1` (整型数): 查找区域的左上角Y坐标

- `x2` (整型数): 查找区域的右下角X坐标

- `y2` (整型数): 查找区域的右下角Y坐标

- `colorJson` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `templ` (字符串):
模板图片的路径，支持多个图片，用”|“分隔，如”test.bmp|test2.bmp|test3.bmp”

- `matchVal` (双精度浮点数):
相似度阈值，范围0-1，如0.85表示85%相似度

- `angle` (双精度浮点数):
旋转角度，每次匹配后旋转指定角度继续匹配，直到匹配成功。角度越小匹配次数越多，时间越长。0为不旋转，速度最快

- `scale` (双精度浮点数): 窗口缩放比例，默认为1。可通过[GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html)接口获取当前窗口缩放

#### 示例:

```
[](#cb4-1)// 创建OLA对象
[](#cb4-2)long ola = CreateCOLAPlugInterFace();
[](#cb4-3)
[](#cb4-4)// 定义颜色范围列表
[](#cb4-5)string colorJson = "[{\"StartColor\":\"3278FA\",\"EndColor\":\"6496FF\",\"Type\":0}]";
[](#cb4-6)
[](#cb4-7)// 执行匹配
[](#cb4-8)long ret = MatchWindowsThresholdFromPathAll(ola, 0, 0, 0, 0, colorJson, "test.bmp|test2.bmp", 0.85, 45.0, 1.0);
[](#cb4-9)
[](#cb4-10)// 检查操作是否成功
[](#cb4-11)if (ret != 0) {
[](#cb4-12)    // 获取匹配结果
[](#cb4-13)    char* result = (char*)ret;
[](#cb4-14)    printf("匹配结果: %s\n", result);
[](#cb4-15)
[](#cb4-16)    // 释放返回的字符串内存
[](#cb4-17)    FreeStringPtr(result);
[](#cb4-18)} else {
[](#cb4-19)    // 匹配失败
[](#cb4-20)}
```

#### 示例:

```
[](#cb5-1)// 定义颜色范围列表
[](#cb5-2)string colorJson = "[{\"StartColor\":\"3278FA\",\"EndColor\":\"6496FF\",\"Type\":0}]";
[](#cb5-3)
[](#cb5-4)// 执行匹配
[](#cb5-5)string result = ola.MatchWindowsThresholdFromPathAll(0, 0, 0, 0, colorJson, "test.bmp|test2.bmp", 0.85, 45.0, 1.0);
[](#cb5-6)
[](#cb5-7)// 检查操作是否成功
[](#cb5-8)if (!result.empty()) {
[](#cb5-9)    // 匹配成功，result包含匹配结果
[](#cb5-10)    cout << "匹配结果: " << result << endl;
[](#cb5-11)} else {
[](#cb5-12)    // 匹配失败
[](#cb5-13)}
```

### 返回值

字符串: 返回JSON格式的匹配结果数组，每个匹配结果包含以下字段：

```
[](#cb6-1){
[](#cb6-2)    "MatchVal": 0.85,//数据相似度
[](#cb6-3)    "MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
[](#cb6-4)    "Index": 0,//多图识别时的返回索引
[](#cb6-5)    "Angle": 45.0,//识别结果角度
[](#cb6-6)    "X": 100,//识别结果X坐标
[](#cb6-7)    "Y": 200,//识别结果Y坐标
[](#cb6-8)    "Width":100,//识别结果宽度
[](#cb6-9)    "Height":100//识别结果高度
[](#cb6-10)}
```

### 注意事项

- 当x1, y1, x2, y2都传0时，将搜索整个窗口客户区

- 颜色值使用十六进制格式，不包含#前缀

- 支持多个模板图片，用”|“分隔

- 角度参数影响匹配时间和精度：

角度越小，匹配次数越多，时间越长

- 角度为0时速度最快，但可能错过旋转的目标

- 缩放比例应与窗口实际缩放比例一致

- DLL调用返回的字符串指针需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放内存

- 返回的坐标是相对于绑定窗口客户区的坐标

### 相关函数

- [GetScaleFromWindows](/窗口/获取绑定窗口缩放比例%20-%20GetScaleFromWindows.html):
获取窗口缩放比例

- [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html):
释放字符串内存

- [MatchWindowsFromPathAll](/图像识别/匹配绑定窗口图片%20-%20MatchWindowsFromPathAll.html):
普通图片匹配

---

# 图片比较-均方误差 -
CalculateMSE

### 函数简介

获取均方误差

### 接口名称

```
CalculateMSE
```

### DLL调用

```
double CalculateMSE(long ola, long imgPtr1, long imgPtr2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `imgPtr1` (长整型数): 第一个OLAImage对象的地址

- `imgPtr2` (长整型数): 第二个OLAImage对象的地址

#### 示例:

待补充…

### 返回值

双精度浮点数:
两个图像的均方误差，值越小表示图像越相似，0表示完全相同

---

# 图片比较-完整比较 -
IsSameImage

### 函数简介

两个图片完全比较完全一样返回true

### 接口名称

```
IsSameImage
```

### DLL调用

```
int IsSameImage(long ola, long imgPtr1, long imgPtr2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `imgPtr1` (长整型数): 第一个OLAImage对象的地址

- `imgPtr2` (长整型数): 第二个OLAImage对象的地址

#### 示例:

待补充…

### 返回值

整型数: - 1: 图片完全一致 - 0: 图片不一致

---

# 图片比较-直方图比较 -
CalculateHistograms

### 函数简介

计算两张图片的直方图相似度。此函数通过比较两张图片的颜色分布直方图来判断它们的相似程度，返回一个0到1之间的相似度值。值越接近1表示图片越相似。

### 接口名称

```
CalculateHistograms
```

### DLL调用

```
double CalculateHistograms(long ola, long imgPtr1, long imgPtr2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `imgPtr1` (长整型数): 第一张图片的OLAImage对象地址

- `imgPtr2` (长整型数): 第二张图片的OLAImage对象地址

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)long ola = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 加载两张图片
[](#cb3-5)long img1 = LoadImage(ola, "test1.bmp");
[](#cb3-6)long img2 = LoadImage(ola, "test2.bmp");
[](#cb3-7)
[](#cb3-8)// 计算直方图相似度
[](#cb3-9)double similarity = CalculateHistograms(ola, img1, img2);
[](#cb3-10)
[](#cb3-11)// 输出相似度
[](#cb3-12)printf("图片相似度: %.2f\n", similarity);
[](#cb3-13)
[](#cb3-14)// 释放图片内存
[](#cb3-15)FreeImagePtr(ola, img1);
[](#cb3-16)FreeImagePtr(ola, img2);
```

### 返回值

双精度浮点数: - 范围：0.0 到 1.0 - 1.0 表示完全相同的图片 - 0.0
表示完全不同的图片 - 值越接近1表示图片越相似

### 注意事项

- 此函数比较的是图片的整体颜色分布，而不是像素级别的比较

- 比较结果受图片亮度、对比度等因素影响

- 建议在比较前对图片进行预处理，如调整大小、亮度等

- 返回的相似度值仅供参考，具体阈值需要根据实际应用场景确定

- 确保在比较完成后释放图片内存

### 相关函数

- [LoadImage](/图像处理/加载图片%20-%20LoadImage.html):
加载图片

- [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html):
释放图片内存

- [CalculateSSIM](/图像识别/图片比较-结构相似性指数%20-%20CalculateSSIM.html):
结构相似性比较

- [CalculateMSE](/图像识别/图片比较-均方误差%20-%20CalculateMSE.html):
均方误差比较

---

# 图片比较-结构相似性指数
- CalculateSSIM

### 函数简介

获取结构相似性指数

### 接口名称

```
CalculateSSIM
```

### DLL调用

```
double CalculateSSIM(long ola, long imgPtr1, long imgPtr2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `imgPtr1` (长整型数): 第一个OLAImage对象的地址

- `imgPtr2` (长整型数): 第二个OLAImage对象的地址

#### 示例:

待补充…

### 返回值

双精度浮点数:
两个图像的结构相似性指数，范围为0到1，值越大表示图像越相似

---

# 是否显示匹配结果弹窗 -
ShowMatchWindow

### 函数简介

是否显示匹配结果弹窗(测试使用),默认不显示

### 接口名称

```
ShowMatchWindow
```

### DLL调用

```
int ShowMatchWindow(long ola, int flag)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `flag` (整型数): 显示控制：

0: 不显示弹窗

- 1: 显示弹窗

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

## 屏幕绘制

# 创建按钮 - DrawGuiButton

## 函数简介

创建按钮对象，支持文本与尺寸设置。

## 接口名称

```
DrawGuiButton
```

## DLL调用

```
int64_t DrawGuiButton(int64_t instance, int64_t parentHandle, char* text,
int32_t x, int32_t y, int32_t width, int32_t height);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
parentHandle |
长整数型 |
父对象句柄（窗口/面板）。 |
|

|
text |
字符串 |
按钮文本。 |
|

|
x |
整数型 |
左上角X。 |
|

|
y |
整数型 |
左上角Y。 |
|

|
width |
整数型 |
宽度。 |
|

|
height |
整数型 |
高度。 |
|

### 示例

```
[](#cb3-1)int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t win = DrawGuiWindow(ola, "Demo", 100, 100, 600, 400, 0);
[](#cb3-3)int64_t btn = DrawGuiButton(ola, win, "OK", 20, 20, 80, 30);
[](#cb3-4)// ...
[](#cb3-5)DestroyCOLAPlugInterFace(ola);
```

## 返回值

按钮句柄，失败返回0。

---

# 创建窗口 - DrawGuiWindow

## 函数简介

创建绘制窗口对象。

## 接口名称

```
DrawGuiWindow
```

## DLL调用

```
int64_t DrawGuiWindow(int64_t instance, char* title, int32_t x, int32_t y,
int32_t width, int32_t height, int32_t style);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
title |
字符串 |
窗口标题。 |
|

|
x |
整数型 |
左上角X。 |
|

|
y |
整数型 |
左上角Y。 |
|

|
width |
整数型 |
宽度。 |
|

|
height |
整数型 |
高度。 |
|

|
style |
整数型 |
窗口样式，0.普通窗口, 1.提示框 |
|

### 示例

```
[](#cb3-1)int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t win = DrawGuiWindow(ola, "Demo", 100, 100, 600, 400, 0);
[](#cb3-3)// ...
[](#cb3-4)DestroyCOLAPlugInterFace(ola);
```

## 返回值

窗口句柄，失败返回0。

---

# 创建面板 - DrawGuiPanel

## 函数简介

创建面板对象，可作为窗口或其他面板的子容器。

## 接口名称

```
DrawGuiPanel
```

## DLL调用

```
int64_t DrawGuiPanel(int64_t instance, int64_t parentHandle, int32_t x,
int32_t y, int32_t width, int32_t height);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
parentHandle |
长整数型 |
父对象句柄（窗口/面板）。 |
|

|
x |
整数型 |
左上角X。 |
|

|
y |
整数型 |
左上角Y。 |
|

|
width |
整数型 |
宽度。 |
|

|
height |
整数型 |
高度。 |
|

### 示例

```
[](#cb3-1)int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t win = DrawGuiWindow(ola, "Demo", 100, 100, 600, 400, 0);
[](#cb3-3)int64_t panel = DrawGuiPanel(ola, win, 10, 10, 200, 200);
[](#cb3-4)// ...
[](#cb3-5)DestroyCOLAPlugInterFace(ola);
```

## 返回值

面板句柄，失败返回0。

---

# 删除对象 -
DrawGuiDeleteObject

## 函数简介

删除指定的绘制对象。

## 接口名称

```
DrawGuiDeleteObject
```

## DLL调用

```
int32_t DrawGuiDeleteObject(int64_t instance, int64_t handle);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
对象句柄。 |
|

### 示例

```
[](#cb3-1)DrawGuiDeleteObject(ola, obj);
```

## 返回值

0 失败，1 成功。

---

# 启用绘制 -
DrawGuiSetGuiActive

## 函数简介

启用或禁用绘制系统。

## 接口名称

```
DrawGuiSetGuiActive
```

## DLL调用

```
int32_t DrawGuiSetGuiActive(int64_t instance, int32_t active);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
active |
整数型 |
1 启用，0 禁用。 |
|

### 示例

```
[](#cb3-1)int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-2)DrawGuiSetGuiActive(ola, 1);
[](#cb3-3)DestroyCOLAPlugInterFace(ola);
```

## 返回值

0 失败，1 成功。

---

# 是否启用绘制 -
DrawGuiIsGuiActive

## 函数简介

查询绘制系统是否已启用。

## 接口名称

```
DrawGuiIsGuiActive
```

## DLL调用

```
int32_t DrawGuiIsGuiActive(int64_t instance);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

### 示例

```
[](#cb3-1)int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t active = DrawGuiIsGuiActive(ola);
[](#cb3-3)printf("active=%d\n", active);
[](#cb3-4)DestroyCOLAPlugInterFace(ola);
```

## 返回值

0 未启用，1 已启用。

---

# 是否穿透点击 -
DrawGuiIsGuiClickThrough

## 函数简介

查询绘制窗口是否设置为可穿透点击。

## 接口名称

```
DrawGuiIsGuiClickThrough
```

## DLL调用

```
int32_t DrawGuiIsGuiClickThrough(int64_t instance);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

### 示例

```
[](#cb3-1)int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t v = DrawGuiIsGuiClickThrough(ola);
[](#cb3-3)printf("clickThrough=%d\n", v);
[](#cb3-4)DestroyCOLAPlugInterFace(ola);
```

## 返回值

0 否，1 是。

---

# 清空所有对象 -
DrawGuiClearAll

## 函数简介

清空并删除所有绘制对象。

## 接口名称

```
DrawGuiClearAll
```

## DLL调用

```
int32_t DrawGuiClearAll(int64_t instance);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

### 示例

```
[](#cb3-1)DrawGuiClearAll(ola);
```

## 返回值

0 失败，1 成功。

---

# 点是否在对象内 -
DrawGuiIsPointInObject

## 函数简介

判断坐标点是否位于指定绘制对象内。

## 接口名称

```
DrawGuiIsPointInObject
```

## DLL调用

```
int32_t DrawGuiIsPointInObject(int64_t instance, int64_t handle, int32_t x, int32_t y);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
对象句柄。 |
|

|
x |
整数型 |
X 坐标。 |
|

|
y |
整数型 |
Y 坐标。 |
|

### 示例

```
[](#cb3-1)int32_t inside = DrawGuiIsPointInObject(ola, obj, 150, 160);
```

## 返回值

0 否，1 是。

---

# 绘制图片 - DrawGuiImage

## 函数简介

创建图片绘制对象。

## 接口名称

```
DrawGuiImage
```

## DLL调用

```
int64_t DrawGuiImage(int64_t instance, char* imagePath, int32_t x, int32_t y);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
imagePath |
字符串 |
图片文件路径。 |
|

|
x |
整数型 |
左上角X。 |
|

|
y |
整数型 |
左上角Y。 |
|

### 示例

```
[](#cb3-1)int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t img = DrawGuiImage(ola, "C:/imgs/logo.png", 10, 10);
[](#cb3-3)// ...
[](#cb3-4)DestroyCOLAPlugInterFace(ola);
```

## 返回值

对象句柄，失败返回0。

---

# 绘制图片指针 -
DrawGuiImagePtr

## 函数简介

基于已有的内存图片指针创建绘制对象，将图片绘制到指定位置。

## 接口名称

```
DrawGuiImagePtr
```

## DLL调用

```
int64_t DrawGuiImagePtr(int64_t instance, int64_t imagePtr, int32_t x, int32_t y);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
imagePtr |
长整数型 |
图片指针（通常为图像处理相关接口返回的图像句柄）。 |
|

|
x |
整数型 |
绘制区域左上角 X 坐标。 |
|

|
y |
整数型 |
绘制区域左上角 Y 坐标。 |
|

### 示例

```
[](#cb3-1)int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-2)// 例如通过图像处理接口加载图片
[](#cb3-3)int64_t img = LoadImage(ola, "C:/imgs/logo.png");
[](#cb3-4)int64_t obj = DrawGuiImagePtr(ola, img, 10, 10);
[](#cb3-5)// ...
[](#cb3-6)DestroyCOLAPlugInterFace(ola);
```

## 返回值

对象句柄，失败返回0。

## 注意事项

- `imagePtr`
需要是有效的图像句柄，在绘制对象使用期间不要提前释放。

- 适合已经在内存中的图像复用场景，相比直接从路径绘制可以减少重复加载开销。

---

# 绘制圆形 - DrawGuiCircle

## 函数简介

创建圆形绘制对象，支持填充/描边模式与线宽设置。

## 接口名称

```
DrawGuiCircle
```

## DLL调用

```
int64_t DrawGuiCircle(int64_t instance, int32_t x, int32_t y,
int32_t radius, int32_t mode, double lineThickness);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
x |
整数型 |
圆心X。 |
|

|
y |
整数型 |
圆心Y。 |
|

|
radius |
整数型 |
半径。 |
|

|
mode |
整数型 |
绘制模式，0 填充,1边框。 |
|

|
lineThickness |
双精度型 |
线宽（像素），对描边模式有效。 |
|

### 示例

```
[](#cb3-1)int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t c = DrawGuiCircle(ola, 200, 200, 60, 1, 2.0);
[](#cb3-3)// ...
[](#cb3-4)DestroyCOLAPlugInterFace(ola);
```

## 返回值

对象句柄，失败返回0。

## 注意事项

- 颜色、透明度等可通过属性设置接口进行配置。

---

# 绘制文本 - DrawGuiText

## 函数简介

创建文本绘制对象，支持字体、字号与对齐方式设置。

## 接口名称

```
DrawGuiText
```

## DLL调用

```
int64_t DrawGuiText(int64_t instance, char* text, int32_t x, int32_t y,
char* fontPath, int32_t fontSize, int32_t align);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
text |
字符串 |
文本内容。 |
|

|
x |
整数型 |
左上角X。 |
|

|
y |
整数型 |
左上角Y。 |
|

|
fontPath |
字符串 |
字体路径（ttf/otf）。 |
|

|
fontSize |
整数型 |
字号（像素）。 |
|

|
align |
整数型 |
0左对齐,1居中对齐,右对齐 |
|

### 示例

```
[](#cb3-1)int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t t = DrawGuiText(ola, "Hello", 100, 100, "C:/Windows/Fonts/msyh.ttc", 18, 0);
[](#cb3-3)// ...
[](#cb3-4)DestroyCOLAPlugInterFace(ola);
```

## 返回值

对象句柄，失败返回0。

---

# 绘制直线 - DrawGuiLine

## 函数简介

创建直线绘制对象，支持线宽设置。

## 接口名称

```
DrawGuiLine
```

## DLL调用

```
int64_t DrawGuiLine(int64_t instance, int32_t x1, int32_t y1, int32_t x2,
int32_t y2, double lineThickness);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
x1 |
整数型 |
起点X。 |
|

|
y1 |
整数型 |
起点Y。 |
|

|
x2 |
整数型 |
终点X。 |
|

|
y2 |
整数型 |
终点Y。 |
|

|
lineThickness |
双精度型 |
线宽（像素）。 |
|

### 示例

```
[](#cb3-1)int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t l = DrawGuiLine(ola, 50, 50, 300, 50, 2.0);
[](#cb3-3)// ...
[](#cb3-4)DestroyCOLAPlugInterFace(ola);
```

## 返回值

对象句柄，失败返回0。

---

# 绘制矩形 - DrawGuiRectangle

## 函数简介

创建矩形绘制对象，支持填充/描边模式与线宽设置。

## 接口名称

```
DrawGuiRectangle
```

## DLL调用

```
int64_t DrawGuiRectangle(int64_t instance, int32_t x, int32_t y,
int32_t width, int32_t height, int32_t mode,
double lineThickness);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
x |
整数型 |
左上角X。 |
|

|
y |
整数型 |
左上角Y。 |
|

|
width |
整数型 |
宽度。 |
|

|
height |
整数型 |
高度。 |
|

|
mode |
整数型 |
绘制模式，0 填充,1边框。 |
|

|
lineThickness |
双精度型 |
线宽（像素），对描边模式有效。 |
|

### 示例

```
[](#cb3-1)int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t r = DrawGuiRectangle(ola, 100, 100, 200, 120, 1, 2.0);
[](#cb3-3)// ...
[](#cb3-4)DestroyCOLAPlugInterFace(ola);
```

## 返回值

对象句柄，失败返回0。

## 注意事项

- 颜色、透明度等可通过属性设置接口进行配置。

---

# 获取位置 -
DrawGuiGetPosition

## 函数简介

获取绘制对象的左上角坐标。

## 接口名称

```
DrawGuiGetPosition
```

## DLL调用

```
int32_t DrawGuiGetPosition(int64_t instance, int64_t handle, int32_t* x, int32_t* y);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
对象句柄。 |
|

|
x |
整数指针 |
返回左上角X（输出）。 |
|

|
y |
整数指针 |
返回左上角Y（输出）。 |
|

### 示例

```
[](#cb3-1)int32_t x=0,y=0;
[](#cb3-2)DrawGuiGetPosition(ola, obj, &x, &y);
```

## 返回值

0 失败，1 成功。

---

# 获取对象类型 -
DrawGuiGetDrawObjectType

## 函数简介

获取绘制对象的类型编号（见 DrawType）。

## 接口名称

```
DrawGuiGetDrawObjectType
```

## DLL调用

```
int32_t DrawGuiGetDrawObjectType(int64_t instance, int64_t handle);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
对象句柄。 |
|

### 示例

```
[](#cb3-1)int32_t t = DrawGuiGetDrawObjectType(ola, obj);
```

## 返回值

对象类型编号。

---

# 获取尺寸 - DrawGuiGetSize

## 函数简介

获取绘制对象的宽度与高度。

## 接口名称

```
DrawGuiGetSize
```

## DLL调用

```
int32_t DrawGuiGetSize(int64_t instance, int64_t handle, int32_t* width, int32_t* height);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
对象句柄。 |
|

|
width |
整数指针 |
返回宽度（输出）。 |
|

|
height |
整数指针 |
返回高度（输出）。 |
|

### 示例

```
[](#cb3-1)int32_t w=0,h=0;
[](#cb3-2)DrawGuiGetSize(ola, obj, &w, &h);
```

## 返回值

0 失败，1 成功。

---

# 设置Z序 - DrawGuiSetZOrder

## 函数简介

设置绘制对象的Z序（绘制顺序）。

## 接口名称

```
DrawGuiSetZOrder
```

## DLL调用

```
int32_t DrawGuiSetZOrder(int64_t instance, int64_t handle, int32_t zOrder);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
对象句柄。 |
|

|
zOrder |
整数型 |
Z序值，数值越大越靠前。 |
|

### 示例

```
[](#cb3-1)DrawGuiSetZOrder(ola, obj, 100);
```

## 返回值

0 失败，1 成功。

---

# 设置位置 -
DrawGuiSetPosition

## 函数简介

设置绘制对象的位置（左上角坐标）。

## 接口名称

```
DrawGuiSetPosition
```

## DLL调用

```
int32_t DrawGuiSetPosition(int64_t instance, int64_t handle, int32_t x, int32_t y);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
对象句柄。 |
|

|
x |
整数型 |
左上角X。 |
|

|
y |
整数型 |
左上角Y。 |
|

### 示例

```
[](#cb3-1)DrawGuiSetPosition(ola, obj, 100, 100);
```

## 返回值

0 失败，1 成功。

---

# 设置可见性 -
DrawGuiSetVisible

## 函数简介

设置绘制对象的可见性。

## 接口名称

```
DrawGuiSetVisible
```

## DLL调用

```
int32_t DrawGuiSetVisible(int64_t instance, int64_t handle, int32_t visible);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
对象句柄。 |
|

|
visible |
整数型 |
1 可见，0 隐藏。 |
|

### 示例

```
[](#cb3-1)DrawGuiSetVisible(ola, obj, 1);
```

## 返回值

0 失败，1 成功。

---

# 设置字体 - DrawGuiSetFont

## 函数简介

设置文本对象的字体与字号。

## 接口名称

```
DrawGuiSetFont
```

## DLL调用

```
int32_t DrawGuiSetFont(int64_t instance, int64_t handle, char* fontPath, int32_t fontSize);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
文本对象句柄。 |
|

|
fontPath |
字符串 |
字体文件路径（ttf/otf）。 |
|

|
fontSize |
整数型 |
字号（像素）。 |
|

### 示例

```
[](#cb3-1)DrawGuiSetFont(ola, text, "C:/Windows/Fonts/msyh.ttc", 18);
```

## 返回值

0 失败，1 成功。

---

# 设置尺寸 - DrawGuiSetSize

## 函数简介

设置绘制对象的尺寸（宽度与高度）。

## 接口名称

```
DrawGuiSetSize
```

## DLL调用

```
int32_t DrawGuiSetSize(int64_t instance, int64_t handle, int32_t width, int32_t height);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
对象句柄。 |
|

|
width |
整数型 |
宽度。 |
|

|
height |
整数型 |
高度。 |
|

### 示例

```
[](#cb3-1)DrawGuiSetSize(ola, obj, 320, 200);
```

## 返回值

0 失败，1 成功。

---

# 设置按钮回调 -
DrawGuiSetButtonCallback

## 函数简介

为按钮对象设置点击回调函数。

## 接口名称

```
DrawGuiSetButtonCallback
```

## DLL调用

```
int32_t DrawGuiSetButtonCallback(int64_t instance, int64_t handle, DrawGuiButtonCallback callback);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
按钮对象句柄。 |
|

|
callback |
回调函数 |
按钮回调函数指针。 |
|

### 示例

```
[](#cb3-1)// 伪代码示例，具体回调签名以头文件为准
[](#cb3-2)void OnClick(int64_t h) { printf("clicked %lld\n", h); }
[](#cb3-3)DrawGuiSetButtonCallback(ola, btn, OnClick);
```

## 返回值

0 失败，1 成功。

---

# 设置文本内容 -
DrawGuiSetText

## 函数简介

设置文本对象的内容。

## 接口名称

```
DrawGuiSetText
```

## DLL调用

```
int32_t DrawGuiSetText(int64_t instance, int64_t handle, char* text);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
文本对象句柄。 |
|

|
text |
字符串 |
文本内容。 |
|

### 示例

```
[](#cb3-1)DrawGuiSetText(ola, text, "New Text");
```

## 返回值

0 失败，1 成功。

---

# 设置文本对齐 -
DrawGuiSetTextAlign

## 函数简介

设置文本对象的对齐方式。

## 接口名称

```
DrawGuiSetTextAlign
```

## DLL调用

```
int32_t DrawGuiSetTextAlign(int64_t instance, int64_t handle, int32_t align);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
文本对象句柄。 |
|

|
align |
整数型 |
0左对齐,1居中对齐,右对齐 |
|

### 示例

```
[](#cb3-1)DrawGuiSetTextAlign(ola, text, 0);
```

## 返回值

0 失败，1 成功。

---

# 设置父子关系 -
DrawGuiSetParent

## 函数简介

设置绘制对象的父子关系。

## 接口名称

```
DrawGuiSetParent
```

## DLL调用

```
int32_t DrawGuiSetParent(int64_t instance, int64_t handle, int64_t parentHandle);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
子对象句柄。 |
|

|
parentHandle |
长整数型 |
父对象句柄。 |
|

### 示例

```
[](#cb3-1)DrawGuiSetParent(ola, child, parent);
```

## 返回值

0 失败，1 成功。

---

# 设置穿透点击 -
DrawGuiSetGuiClickThrough

## 函数简介

设置绘制窗口是否可穿透点击。

## 接口名称

```
DrawGuiSetGuiClickThrough
```

## DLL调用

```
int32_t DrawGuiSetGuiClickThrough(int64_t instance, int32_t enabled);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
enabled |
整数型 |
1 可穿透，0 不可穿透。 |
|

### 示例

```
[](#cb3-1)int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-2)DrawGuiSetGuiClickThrough(ola, 1);
[](#cb3-3)DestroyCOLAPlugInterFace(ola);
```

## 返回值

0 失败，1 成功。

---

# 设置窗口标题 -
DrawGuiSetWindowTitle

## 函数简介

设置窗口对象的标题文本。

## 接口名称

```
DrawGuiSetWindowTitle
```

## DLL调用

```
int32_t DrawGuiSetWindowTitle(int64_t instance, int64_t handle, char* title);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
窗口句柄。 |
|

|
title |
字符串 |
标题文本。 |
|

### 示例

```
[](#cb3-1)DrawGuiSetWindowTitle(ola, win, "Demo Window");
```

## 返回值

0 失败，1 成功。

---

# 设置窗口样式 -
DrawGuiSetWindowStyle

## 函数简介

设置窗口对象的样式。

## 接口名称

```
DrawGuiSetWindowStyle
```

## DLL调用

```
int32_t DrawGuiSetWindowStyle(int64_t instance, int64_t handle, int32_t style);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
窗口句柄。 |
|

|
style |
整数型 |
窗口样式，0.普通窗口, 1.提示框 |
|

### 示例

```
[](#cb3-1)DrawGuiSetWindowStyle(ola, win, 0);
```

## 返回值

0 失败，1 成功。

---

# 设置窗口置顶 -
DrawGuiSetWindowTopMost

## 函数简介

设置窗口是否置顶显示。

## 接口名称

```
DrawGuiSetWindowTopMost
```

## DLL调用

```
int32_t DrawGuiSetWindowTopMost(int64_t instance, int64_t handle, int32_t topMost);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
窗口句柄。 |
|

|
topMost |
整数型 |
1 置顶，0 取消置顶。 |
|

### 示例

```
[](#cb3-1)DrawGuiSetWindowTopMost(ola, win, 1);
```

## 返回值

0 失败，1 成功。

---

# 设置窗口透明度 -
DrawGuiSetWindowTransparency

## 函数简介

设置窗口对象的整体透明度。

## 接口名称

```
DrawGuiSetWindowTransparency
```

## DLL调用

```
int32_t DrawGuiSetWindowTransparency(int64_t instance, int64_t handle, int32_t alpha);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
窗口句柄。 |
|

|
alpha |
整数型 |
透明度（0-255）。 |
|

### 示例

```
[](#cb3-1)DrawGuiSetWindowTransparency(ola, win, 200);
```

## 返回值

0 失败，1 成功。

---

# 设置线宽 -
DrawGuiSetLineThickness

## 函数简介

设置绘制对象的线宽（像素）。

## 接口名称

```
DrawGuiSetLineThickness
```

## DLL调用

```
int32_t DrawGuiSetLineThickness(int64_t instance, int64_t handle, double thickness);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
对象句柄。 |
|

|
thickness |
双精度型 |
线宽（像素）。 |
|

### 示例

```
[](#cb3-1)DrawGuiSetLineThickness(ola, obj, 3.0);
```

## 返回值

0 失败，1 成功。

---

# 设置绘制模式 -
DrawGuiSetDrawMode

## 函数简介

设置绘制对象的绘制模式（填充/描边等）。

## 接口名称

```
DrawGuiSetDrawMode
```

## DLL调用

```
int32_t DrawGuiSetDrawMode(int64_t instance, int64_t handle, int32_t mode);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
对象句柄。 |
|

|
mode |
整数型 |
绘制模式，0 填充,1边框。 |
|

### 示例

```
[](#cb3-1)DrawGuiSetDrawMode(ola, obj, 1);
```

## 返回值

0 失败，1 成功。

---

# 设置透明度 - DrawGuiSetAlpha

## 函数简介

设置绘制对象整体透明度。

## 接口名称

```
DrawGuiSetAlpha
```

## DLL调用

```
int32_t DrawGuiSetAlpha(int64_t instance, int64_t handle, int32_t alpha);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
对象句柄。 |
|

|
alpha |
整数型 |
透明度（0-255）。 |
|

### 示例

```
[](#cb3-1)DrawGuiSetAlpha(ola, obj, 180);
```

## 返回值

0 失败，1 成功。

---

# 设置颜色 - DrawGuiSetColor

## 函数简介

设置绘制对象的颜色（RGBA）。

## 接口名称

```
DrawGuiSetColor
```

## DLL调用

```
int32_t DrawGuiSetColor(int64_t instance, int64_t handle, int32_t r, int32_t g,
int32_t b, int32_t a);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
对象句柄。 |
|

|
r |
整数型 |
红色分量（0-255）。 |
|

|
g |
整数型 |
绿色分量（0-255）。 |
|

|
b |
整数型 |
蓝色分量（0-255）。 |
|

|
a |
整数型 |
透明度（0-255）。 |
|

### 示例

```
[](#cb3-1)DrawGuiSetColor(ola, obj, 255, 0, 0, 200);
```

## 返回值

0 失败，1 成功。

---

# 设置鼠标回调 -
DrawGuiSetMouseCallback

## 函数简介

为目标对象设置鼠标事件回调函数。

## 接口名称

```
DrawGuiSetMouseCallback
```

## DLL调用

```
int32_t DrawGuiSetMouseCallback(int64_t instance, int64_t handle, DrawGuiMouseCallback callback);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
目标对象句柄。 |
|

|
callback |
回调函数 |
鼠标回调函数指针。 |
|

### 示例

```
[](#cb3-1)// 伪代码示例，具体回调签名以头文件为准
[](#cb3-2)void OnMouse(int x, int y, int type) { /* ... */ }
[](#cb3-3)DrawGuiSetMouseCallback(ola, obj, OnMouse);
```

## 返回值

0 失败，1 成功。

---

# 释放绘制资源 -
DrawGuiCleanup

## 函数简介

释放绘制系统资源并清理所有对象。

## 接口名称

```
DrawGuiCleanup
```

## DLL调用

```
int32_t DrawGuiCleanup(int64_t instance);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

### 示例

```
[](#cb3-1)int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t ok = DrawGuiCleanup(ola);
[](#cb3-3)DestroyCOLAPlugInterFace(ola);
```

## 返回值

0 失败，1 成功。

## 注意事项

- 调用后已创建的绘制对象将被全部销毁。

---

## 快捷键

# 停止快捷键监听 -
StopHotkeyHook

### 函数简介

停止快捷键监听

### 接口名称

```
StopHotkeyHook
```

### DLL调用

```
int StopHotkeyHook(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

### 返回值

全局键盘鼠标钩子关闭状态

整型数:

0 : 失败

1 : 成功

---

# 卸载键盘快捷键 -
UnregisterHotkey

### 函数简介

- 卸载键盘快捷键监听

### 接口名称

```
UnregisterHotkey
```

### DLL调用

```
int UnregisterHotkey(long ola, int keycode, int modifiers)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `keycode` (整型数): 按键码

- `modifiers` (整型数):
修饰键组合，使用Modifier枚举值的位或组合，比如按下Ctrl+Alt
modifiers:2+8=10 具体取值如下：

左Shift键掩码（值1）

- 左Ctrl键掩码（值2）

- 左Meta键掩码（值4）

- 左Alt键掩码（值8）

- 右Shift键掩码（值16）

- 右Ctrl键掩码（值32）

- 右Meta键掩码（值64）

- 右Alt键掩码（值128）

### 返回值

卸载监听状态

整型数:

1 : 成功

0 : 失败

---

# 卸载鼠标拖动快捷键 -
UnregisterMouseDrag

### 函数简介

- 卸载鼠标拖动快捷键

### 接口名称

```
UnregisterMouseDrag
```

### DLL调用

```
int UnregisterMouseDrag(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

### 返回值

卸载监听状态

整型数:

1 : 成功

0 : 失败

---

# 卸载鼠标滚轮快捷键 -
UnregisterMouseWheel

### 函数简介

- 卸载鼠标滚轮快捷键

### 接口名称

```
UnregisterMouseWheel
```

### DLL调用

```
int UnregisterMouseWheel(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

### 返回值

卸载监听状态

整型数:

1 : 成功

0 : 失败

---

# 卸载鼠标点击快捷键 -
UnregisterMouseButton

### 函数简介

- 卸载鼠标点击快捷键

### 接口名称

```
UnregisterMouseButton
```

### DLL调用

```
int UnregisterMouseButton(long ola, int button, int type)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `button` (整型数): 按键类型，取值如下：

鼠标左键（值1）

- 鼠标右键（值2）

- 鼠标中间（值3）

- 拓展键1（值4）

- 拓展键2（值5）

- `type` (整型数):
按键状态，使用Modifier枚举值的位或组合，取值如下：

鼠标点击（值0）

- 鼠标按下（值1）

- 鼠标释放（值2）

### 返回值

卸载监听状态

整型数:

1 : 成功

0 : 失败

---

# 卸载鼠标移动快捷键 -
UnregisterMouseMove

### 函数简介

- 卸载鼠标移动快捷键

### 接口名称

```
UnregisterMouseMove
```

### DLL调用

```
int UnregisterMouseMove(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

### 返回值

卸载监听状态

整型数:

1 : 成功

0 : 失败

---

# 启动快捷键监听 -
StartHotkeyHook

### 函数简介

启动快捷键监听

### 接口名称

```
StartHotkeyHook
```

### DLL调用

```
int StartHotkeyHook(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

### 返回值

全局键盘鼠标钩子启动状态

整型数:

0 : 失败

1 : 成功

---

# 注册键盘快捷键 -
RegisterHotkey

### 函数简介

- 注册键盘快捷键监听,可监听单个按键、组合键等，同一组按键只能创建一个监听

- 注册键盘快捷键监听前需要调用StartHotkeyHook安装键盘鼠标钩子

- 回调函数 int HotKeyCallback(int keycode, int modifiers)

参考接口参数定义

- 返回值0继续传递按键信息,返回1阻断消息传递

- keycode传0可以监听所有按键信息

- 参考windows函数 [SetWindowsHookExW](https://learn.microsoft.com/zh-cn/windows/win32/api/winuser/nf-winuser-setwindowshookexw)实现

### 接口名称

```
RegisterHotkey
```

### DLL调用

```
int RegisterHotkey(long ola, int keycode, int modifiers,HotKeyCallback callback)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `keycode` (整型数): 按键码

- `modifiers` (整型数):
修饰键组合，使用Modifier枚举值的位或组合，比如按下Ctrl+Alt
modifiers:2+8=10 具体取值如下：

左Shift键掩码（值1）

- 左Ctrl键掩码（值2）

- 左Meta键掩码（值4）

- 左Alt键掩码（值8）

- 右Shift键掩码（值16）

- 右Ctrl键掩码（值32）

- 右Meta键掩码（值64）

- 右Alt键掩码（值128）

- `callback` 回调函数 int HotKeyCallback(int keycode, int
modifiers) 参考接口参数定义

### 返回值

注册监听状态

整型数:

1 : 成功

0 : 失败

---

# 注册鼠标拖动快捷键 -
RegisterMouseDrag

### 函数简介

- 注册鼠标拖动快捷键监听,可监听鼠标移动

- 注册鼠标快捷键监听前需要调用StartHotkeyHook安装键盘鼠标钩子

- 回调函数 void MouseDragCallback(int x, int y) 参数定义

x 鼠标X坐标

- y 鼠标Y坐标

- 参考windows函数 [SetWindowsHookExW](https://learn.microsoft.com/zh-cn/windows/win32/api/winuser/nf-winuser-setwindowshookexw)实现

### 接口名称

```
RegisterMouseDrag
```

### DLL调用

```
int RegisterMouseDrag(long ola ,MouseDragCallback callback)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `callback` 回调函数 void MouseDragCallback(int x, int y)
参数定义

x 鼠标X坐标

- y 鼠标Y坐标

### 返回值

注册监听状态

整型数:

1 : 成功

0 : 失败

---

# 注册鼠标滚轮快捷键 -
RegisterMouseWheel

### 函数简介

- 注册鼠标滚轮快捷键监听,可监听滚动方向及滚动量

- 注册鼠标快捷键监听前需要调用StartHotkeyHook安装键盘鼠标钩子

- 回调函数 void MouseWheelCallback(int x, int y, int amount, int
rotation) 参数定义

x 鼠标X坐标

- y 鼠标Y坐标

- amount 滚动量

- rotation 滚动方向

- 参考windows函数 [SetWindowsHookExW](https://learn.microsoft.com/zh-cn/windows/win32/api/winuser/nf-winuser-setwindowshookexw)实现

### 接口名称

```
RegisterMouseWheel
```

### DLL调用

```
int RegisterMouseWheel(long ola ,MouseWheelCallback callback)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `callback` 回调函数 void MouseWheelCallback(int x, int y,
int amount, int rotation)

x 鼠标X坐标

- y 鼠标Y坐标

- amount 滚动量

- rotation 滚动方向

### 返回值

注册监听状态

整型数:

1 : 成功

0 : 失败

---

# 注册鼠标点击快捷键 -
RegisterMouseButton

### 函数简介

- 注册鼠标点击快捷键,可监听鼠标点击及点击次数

- 注册鼠标快捷键监听前需要调用StartHotkeyHook安装键盘鼠标钩子

- 回调函数 void MouseCallback(int button,int x, int y, int clicks)

button 参考参数定义

- x X坐标

- y Y坐标

- clicks 点击次数

- 参考windows函数 [SetWindowsHookExW](https://learn.microsoft.com/zh-cn/windows/win32/api/winuser/nf-winuser-setwindowshookexw)实现

### 接口名称

```
RegisterMouseButton
```

### DLL调用

```
int RegisterMouseButton(long ola, int button, int type ,MouseCallback callback)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `button` (整型数): 按键类型，取值如下：

鼠标左键（值1）

- 鼠标右键（值2）

- 鼠标中间（值3）

- 拓展键1（值4）

- 拓展键2（值5）

- `type` (整型数):
按键状态，使用Modifier枚举值的位或组合，取值如下：

鼠标点击（值0）

- 鼠标按下（值1）

- 鼠标释放（值2）

- `callback` 回调函数 void MouseCallback(int button,int x,
int y, int clicks)

button 参考参数定义

- x X坐标

- y Y坐标

- clicks 点击次数

### 返回值

注册监听状态

整型数:

1 : 成功

0 : 失败

---

# 注册鼠标移动快捷键 -
RegisterMouseMove

### 函数简介

- 注册鼠标移动快捷键监听,可监听鼠标移动

- 注册鼠标快捷键监听前需要调用StartHotkeyHook安装键盘鼠标钩子

- 回调函数 void MouseMoveCallback(int x, int y) 参数定义

x 鼠标X坐标

- y 鼠标Y坐标

- 参考windows函数 [SetWindowsHookExW](https://learn.microsoft.com/zh-cn/windows/win32/api/winuser/nf-winuser-setwindowshookexw)实现

### 接口名称

```
RegisterMouseMove
```

### DLL调用

```
int RegisterMouseMove(long ola ,MouseMoveCallback callback)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `callback` 回调函数 void MouseMoveCallback(int x, int y)
参数定义

x 鼠标X坐标

- y 鼠标Y坐标

### 返回值

注册监听状态

整型数:

1 : 成功

0 : 失败

---

## 数据库

# 关闭数据库 - CloseDatabase

## 函数简介

关闭已打开的数据库，释放相关资源。

## 函数原型

```
int CloseDatabase(long ola, const long db);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

## 返回值

返回值：操作结果。成功返回 1，失败返回 0。

## 示例

### SDK

@tab C##

csharp 复制 using System; using OLA.ServiceCenter.PlugFactory;

namespace OLADemo { internal class Program { static OLAPlugServer
OLAServer; static void Main(string[] args) { OLAServer = new
OLAPlugServer(); var regResult = OLAServer.Reg( OLAServer.UserCode,
OLAServer.SoftCode, OLAServer.FeatureList );
OLAServer.CreateCOLAPlugInterFace(); long db =
OLAServer.OpenDatabase(“OLAPlugDemo.db”, “olaplug”);
Console.WriteLine($“OpenDatabase 返回:{db}”);

```
// 关闭数据库
int result = OLAServer.CloseDatabase(db);
if (result == 1)
{
Console.WriteLine("数据库关闭成功。");
}
else
{
Console.WriteLine("数据库关闭失败。");
}
}
}
```

} @tab Python

python 复制 from OLAPlugServer import OLAPlugServer

# 实例化

OLAServer = OLAPlugServer() # 注册 OLAServer.Reg(OLAServer.UserCode,
OLAServer.SoftCode, OLAServer.FeatureList) # 创建OLAPlug对象
OLAServer.CreateCOLAPlugInterFace() # 打开数据库 db =
OLAServer.OpenDatabase(‘OLAPlug.db’, ‘OLAPlug’)
print(f”openDatabaseResult={db}“)

# 关闭数据库

result = OLAServer.CloseDatabase(db) if result == 1:
print(“数据库关闭成功。”) else: print(“数据库关闭失败。”)

### 原生方式

@tab Python

python 复制 import os import sys from ctypes import *

# 1. 加载dll

# 此处路径为插件所在路径，请根据实际情况修改。

# 32位python使用x86版本，64位python使用x64版本

if sys.maxsize > 2**32: olaplug_dll =
WinDLL(os.path.abspath(os.path.join(os.getcwd(), ‘OLAPlug_x64.dll’)))
else: olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(),
‘OLAPlug_x86.dll’)))

# 2. 注册到后台

UserCode = “c38e200f116d4fa8bd0deb45ccb523ea” SoftCode =
“701bc92ba84642c68845e7a06c10fd99” FeatureList = “OLA|OLAPlus”
olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
olaplug_dll.Reg.restype = c_int32 result =
olaplug_dll.Reg(UserCode.encode(‘utf-8’), SoftCode.encode(‘utf-8’),
FeatureList.encode(‘utf-8’)) print(f’注册结果返回: {result}’)

# 3. 创建ola对象

olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p ola_obj =
olaplug_dll.CreateCOLAPlugInterFace()

# 4. 打开数据库

olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
olaplug_dll.OpenDatabase.restype = c_void_p db =
olaplug_dll.OpenDatabase(ola_obj, “OLAPlugDemo.db”.encode(‘utf-8’),
“olaplug”.encode(‘utf-8’)) print(f”openDatabaseResult={db}“)

# 5. 关闭数据库

olaplug_dll.CloseDatabase.argtypes = [c_void_p, c_void_p]
olaplug_dll.CloseDatabase.restype = c_int32 result =
olaplug_dll.CloseDatabase(ola_obj, db) if result == 1:
print(“数据库关闭成功。”) else: print(“数据库关闭失败。”)

## 注意事项

关闭数据库后，相关的数据库对象指针将不再有效，后续操作将导致未定义行为。

确保在不再使用数据库时调用此函数，以释放相关资源。

---

# 创建数据库 - CreateDatabase

## 函数简介

创建数据库，返回一个数据库对象。若文件存在则返回失败

## 函数原型

```
long CreateDatabase(long ola, string dbName, string password)
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `dbName` (字符串): 数据库文件路径

- `password` (字符串): 数据库密码

## 返回值

- 返回值：数据库对象，若打开失败，返回0

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.CreateDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"CreateDatabase 返回:{db}");
[](#cb2-20)        }
[](#cb2-21)    }
[](#cb2-22)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)
[](#cb3-4)# 实例化
[](#cb3-5)OLAServer = OLAPlugServer()
[](#cb3-6)# 注册
[](#cb3-7)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-8)# 创建OLAPlug对象
[](#cb3-9)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-10)# 调用函数
[](#cb3-11)db = OLAServer.CreateDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-12)print(f"CreateDatabaseResult={db}")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)
[](#cb4-6)# 1. 加载dll
[](#cb4-7)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-8)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-9)if sys.maxsize > 2**32:
[](#cb4-10)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-11)else:
[](#cb4-12)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-13)
[](#cb4-14)# 2. 注册到后台
[](#cb4-15)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-16)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-17)FeatureList = "OLA|OLAPlus"
[](#cb4-18)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-19)olaplug_dll.Reg.restype = c_int32
[](#cb4-20)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-21)print(f'注册结果返回: {result}')
[](#cb4-22)
[](#cb4-23)# 3. 创建ola对象
[](#cb4-24)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-25)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-26)
[](#cb4-27)# 4. 调用函数
[](#cb4-28)olaplug_dll.CreateDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-29)olaplug_dll.CreateDatabase.restype = c_void_p
[](#cb4-30)db = olaplug_dll.CreateDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-31)print(f"CreateDatabaseResult={db}")
```

---

# 打开内存数据库 -
OpenMemoryDatabase

## 函数简介

打开内存中的数据库，返回一个数据库对象指针。

## 函数原型

```
int64_t OpenMemoryDatabase(int64_t instance, int64_t address, int32_t size, string password)
```

## 参数定义

- `instance` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `address` (长整型数): 数据库所在的内存首地址

- `size` (整型数): 数据库内存区域大小（字节）

- `password` (字符串): 数据库密码

## 返回值

- 返回值：数据库对象指针，若打开失败，返回0

## 示例

```
[](#cb2-1)#include <stdint.h>
[](#cb2-2)#include <stdio.h>
[](#cb2-3)
[](#cb2-4)int main() {
[](#cb2-5)    int64_t ola = CreateCOLAPlugInterFace();
[](#cb2-6)
[](#cb2-7)    int64_t db_addr = 0x10000000; // 示例地址
[](#cb2-8)    int32_t db_size = 1024 * 1024; // 1MB 示例
[](#cb2-9)
[](#cb2-10)    int64_t db = OpenMemoryDatabase(ola, db_addr, db_size, "olaplug");
[](#cb2-11)    printf("OpenMemoryDatabase=%lld\n", (long long)db);
[](#cb2-12)
[](#cb2-13)    // 使用完成后请根据数据库使用方式进行关闭/清理
[](#cb2-14)    DestroyCOLAPlugInterFace(ola);
[](#cb2-15)    return 0;
[](#cb2-16)}
```

## 注意事项

- `address` 与 `size`
需指向包含完整数据库内容的有效内存区域

- 如需口令保护，确保 `password` 正确

- 使用完成后请按数据库相关接口流程进行资源释放

---

# 打开数据库 - OpenDatabase

## 函数简介

打开数据库，返回一个数据库对象。若文件不存在则返回失败0

## 函数原型

```
long OpenDatabase(long ola, string dbName, string password)
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `dbName` (字符串): 数据库文件路径

- `password` (字符串): 数据库密码

## 返回值

- 返回值：数据库对象，若打开失败，返回0

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)        }
[](#cb2-21)    }
[](#cb2-22)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)
[](#cb3-4)# 实例化
[](#cb3-5)OLAServer = OLAPlugServer()
[](#cb3-6)# 注册
[](#cb3-7)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-8)# 创建OLAPlug对象
[](#cb3-9)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-10)# 调用函数
[](#cb3-11)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-12)print(f"openDatabaseResult={db}")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)
[](#cb4-6)# 1. 加载dll
[](#cb4-7)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-8)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-9)if sys.maxsize > 2**32:
[](#cb4-10)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-11)else:
[](#cb4-12)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-13)
[](#cb4-14)# 2. 注册到后台
[](#cb4-15)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-16)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-17)FeatureList = "OLA|OLAPlus"
[](#cb4-18)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-19)olaplug_dll.Reg.restype = c_int32
[](#cb4-20)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-21)print(f'注册结果返回: {result}')
[](#cb4-22)
[](#cb4-23)# 3. 创建ola对象
[](#cb4-24)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-25)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-26)
[](#cb4-27)# 4. 调用函数
[](#cb4-28)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-29)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-30)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-31)print(f"openDatabaseResult={db}")
```

---

# 执行SQL - ExecuteSql

## 函数简介

执行指定的SQL语句，通常用于执行更新（UPDATE）、插入（INSERT）或删除（DELETE）操作。返回操作结果。

## 函数原型

```
[](#cb1-1)int ExecuteSql(long ola, const long db, string sql);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `sql` (字符串): 要执行的SQL语句。

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行SQL语句（插入操作）
[](#cb2-22)            string sql = "INSERT INTO MyTable (Column1, Column2) VALUES ('Value1', 'Value2')";
[](#cb2-23)            int result = OLAServer.ExecuteSql(db, sql);
[](#cb2-24)            if (result == 1)
[](#cb2-25)            {
[](#cb2-26)                Console.WriteLine("SQL执行成功。");
[](#cb2-27)            }
[](#cb2-28)            else
[](#cb2-29)            {
[](#cb2-30)                Console.WriteLine("SQL执行失败。");
[](#cb2-31)            }
[](#cb2-32)        }
[](#cb2-33)    }
[](#cb2-34)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 执行SQL语句（插入操作）
[](#cb3-14)sql = "INSERT INTO MyTable (Column1, Column2) VALUES ('Value1', 'Value2')"
[](#cb3-15)result = OLAServer.ExecuteSql(db, sql)
[](#cb3-16)if result == 1:
[](#cb3-17)    print("SQL执行成功。")
[](#cb3-18)else:
[](#cb3-19)    print("SQL执行失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 执行SQL语句（插入操作）
[](#cb4-33)sql = "INSERT INTO MyTable (Column1, Column2) VALUES ('Value1', 'Value2')"
[](#cb4-34)olaplug_dll.ExecuteSql.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-35)olaplug_dll.ExecuteSql.restype = c_int32
[](#cb4-36)result = olaplug_dll.ExecuteSql(ola_obj, db, sql.encode('utf-8'))
[](#cb4-37)if result == 1:
[](#cb4-38)    print("SQL执行成功。")
[](#cb4-39)else:
[](#cb4-40)    print("SQL执行失败。")
```

## 注意事项

- 该函数适用于执行不返回结果集的SQL语句，如
`INSERT`、`UPDATE`、`DELETE` 等。

- 如果SQL语句执行失败，函数将返回 `0`，可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保传入的SQL语句语法正确，且表名和列名存在，否则可能导致执行失败。

---

# 执行快速查询 - ExecuteScalar

## 函数简介

执行指定的SQL查询语句，并返回结果集中第一行的第一列的值。通常用于执行返回单个值的查询操作，例如
`COUNT`、`SUM`、`MAX` 等聚合函数。

## 函数原型

```
[](#cb1-1)int ExecuteScalar(long ola, const long db, string sql);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `sql` (字符串): 要执行的SQL查询语句。

## 返回值

- 返回值：查询结果中第一行第一列的值。如果查询失败或结果集为空，返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行查询并返回第一行第一列的值
[](#cb2-22)            string sql = "SELECT COUNT(*) FROM MyTable";
[](#cb2-23)            int result = OLAServer.ExecuteScalar(db, sql);
[](#cb2-24)            Console.WriteLine($"查询结果: {result}");
[](#cb2-25)        }
[](#cb2-26)    }
[](#cb2-27)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 执行查询并返回第一行第一列的值
[](#cb3-14)sql = "SELECT COUNT(*) FROM MyTable"
[](#cb3-15)result = OLAServer.ExecuteScalar(db, sql)
[](#cb3-16)print(f"查询结果: {result}")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 执行查询并返回第一行第一列的值
[](#cb4-33)sql = "SELECT COUNT(*) FROM MyTable"
[](#cb4-34)olaplug_dll.ExecuteScalar.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-35)olaplug_dll.ExecuteScalar.restype = c_int32
[](#cb4-36)result = olaplug_dll.ExecuteScalar(ola_obj, db, sql.encode('utf-8'))
[](#cb4-37)print(f"查询结果: {result}")
```

## 注意事项

- 该函数适用于执行返回单个值的查询操作，例如
`COUNT`、`SUM`、`MAX` 等聚合函数。

- 如果查询失败或结果集为空，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保传入的SQL查询语句语法正确，且表名和列名存在，否则可能导致查询失败。

---

# 读取double数据 - GetDouble

## 函数简介

读取double类型的数据

## 函数原型

```
[](#cb1-1)double GetDouble(long ola, long stmt, int columnIndex);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

- `columnIndex` (整型数): 列索引，从0开始。

## 返回值

- 返回值：数据的值。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行SQL语句（插入操作）
[](#cb2-22)            string tableName = "user";
[](#cb2-23)            result = OLAServer.ExecuteSql(db, $"DROP TABLE IF EXISTS {tableName}");
[](#cb2-24)            result = OLAServer.ExecuteSql(db, $"CREATE TABLE {tableName} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, balance REAL)");
[](#cb2-25)            result = OLAServer.ExecuteSql(db, $"DELETE FROM {tableName} WHERE 1=1");
[](#cb2-26)            for (int i = 1; i <= 5; i++)
[](#cb2-27)            {
[](#cb2-28)                result = OLAServer.ExecuteSql(db, $"INSERT INTO {tableName}(name, balance) VALUES ('用户{i}', {100 + i / 100})");
[](#cb2-29)                Console.WriteLine($"ExecuteSql 插入数据 返回:{result}");
[](#cb2-30)            }
[](#cb2-31)            //读取数据
[](#cb2-32)            long stmt = OLAServer.ExecuteReader(db, $"SELECT * FROM {tableName}");
[](#cb2-33)            while (OLAServer.Read(stmt))
[](#cb2-34)            {
[](#cb2-35)                var id = OLAServer.GetInt32(stmt, 0);
[](#cb2-36)                var name = OLAServer.GetString(stmt, 1);
[](#cb2-37)                var balance = OLAServer.GetDouble(stmt, 2);
[](#cb2-38)                Console.WriteLine($"Read 数据:id={id},name={name},balance={balance}");
[](#cb2-39)            };
[](#cb2-40)        }
[](#cb2-41)    }
[](#cb2-42)}
```

@tab Python

```
[](#cb3-1)# 待补充
```

### 原生方式

@tab Python

```
[](#cb4-1)# 待补充
```

## 注意事项

---

# 读取double数据 -
GetDoubleByColumnName

## 函数简介

读取double类型的数据

## 函数原型

```
[](#cb1-1)double GetDoubleByColumnName(long ola, long stmt, string columnName);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

- `columnName` (字符串): 列名称。

## 返回值

- 返回值：数据的值。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行SQL语句（插入操作）
[](#cb2-22)            string tableName = "user";
[](#cb2-23)            result = OLAServer.ExecuteSql(db, $"DROP TABLE IF EXISTS {tableName}");
[](#cb2-24)            result = OLAServer.ExecuteSql(db, $"CREATE TABLE {tableName} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, balance REAL)");
[](#cb2-25)            result = OLAServer.ExecuteSql(db, $"DELETE FROM {tableName} WHERE 1=1");
[](#cb2-26)            for (int i = 1; i <= 5; i++)
[](#cb2-27)            {
[](#cb2-28)                result = OLAServer.ExecuteSql(db, $"INSERT INTO {tableName}(name, balance) VALUES ('用户{i}', {100 + i / 100})");
[](#cb2-29)                Console.WriteLine($"ExecuteSql 插入数据 返回:{result}");
[](#cb2-30)            }
[](#cb2-31)            //读取数据
[](#cb2-32)            long stmt = OLAServer.ExecuteReader(db, $"SELECT * FROM {tableName}");
[](#cb2-33)            while (OLAServer.Read(stmt))
[](#cb2-34)            {
[](#cb2-35)                var id = OLAServer.GetInt32ByColumnName(stmt, "id");
[](#cb2-36)                var name = OLAServer.GetStringByColumnName(stmt, "name");
[](#cb2-37)                var balance = OLAServer.GetDoubleByColumnName(stmt, "balance");
[](#cb2-38)                Console.WriteLine($"Read 数据:id={id},name={name},balance={balance}");
[](#cb2-39)            };
[](#cb2-40)        }
[](#cb2-41)    }
[](#cb2-42)}
```

@tab Python

```
[](#cb3-1)# 待补充
```

### 原生方式

@tab Python

```
[](#cb4-1)# 待补充
```

## 注意事项

---

# 读取int32数据 - GetInt32

## 函数简介

读取int32类型的数据

## 函数原型

```
[](#cb1-1)int GetInt32(long ola, long stmt, int columnIndex);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

- `columnIndex` (整型数): 列索引，从0开始。

## 返回值

- 返回值：数据的值。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行SQL语句（插入操作）
[](#cb2-22)            string tableName = "user";
[](#cb2-23)            result = OLAServer.ExecuteSql(db, $"DROP TABLE IF EXISTS {tableName}");
[](#cb2-24)            result = OLAServer.ExecuteSql(db, $"CREATE TABLE {tableName} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, balance REAL)");
[](#cb2-25)            result = OLAServer.ExecuteSql(db, $"DELETE FROM {tableName} WHERE 1=1");
[](#cb2-26)            for (int i = 1; i <= 5; i++)
[](#cb2-27)            {
[](#cb2-28)                result = OLAServer.ExecuteSql(db, $"INSERT INTO {tableName}(name, balance) VALUES ('用户{i}', {100 + i / 100})");
[](#cb2-29)                Console.WriteLine($"ExecuteSql 插入数据 返回:{result}");
[](#cb2-30)            }
[](#cb2-31)            //读取数据
[](#cb2-32)            long stmt = OLAServer.ExecuteReader(db, $"SELECT * FROM {tableName}");
[](#cb2-33)            while (OLAServer.Read(stmt))
[](#cb2-34)            {
[](#cb2-35)                var id = OLAServer.GetInt32(stmt, 0);
[](#cb2-36)                var name = OLAServer.GetString(stmt, 1);
[](#cb2-37)                var balance = OLAServer.GetDouble(stmt, 2);
[](#cb2-38)                Console.WriteLine($"Read 数据:id={id},name={name},balance={balance}");
[](#cb2-39)            };
[](#cb2-40)        }
[](#cb2-41)    }
[](#cb2-42)}
```

@tab Python

```
[](#cb3-1)# 待补充
```

### 原生方式

@tab Python

```
[](#cb4-1)# 待补充
```

## 注意事项

---

# 读取int数据 -
GetInt32ByColumnName

## 函数简介

读取int类型的数据

## 函数原型

```
[](#cb1-1)int GetInt64ByColumnName(long ola, long stmt, string columnName);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

- `columnName` (字符串): 列名称。

## 返回值

- 返回值：数据的值。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行SQL语句（插入操作）
[](#cb2-22)            string tableName = "user";
[](#cb2-23)            result = OLAServer.ExecuteSql(db, $"DROP TABLE IF EXISTS {tableName}");
[](#cb2-24)            result = OLAServer.ExecuteSql(db, $"CREATE TABLE {tableName} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, balance REAL)");
[](#cb2-25)            result = OLAServer.ExecuteSql(db, $"DELETE FROM {tableName} WHERE 1=1");
[](#cb2-26)            for (int i = 1; i <= 5; i++)
[](#cb2-27)            {
[](#cb2-28)                result = OLAServer.ExecuteSql(db, $"INSERT INTO {tableName}(name, balance) VALUES ('用户{i}', {100 + i / 100})");
[](#cb2-29)                Console.WriteLine($"ExecuteSql 插入数据 返回:{result}");
[](#cb2-30)            }
[](#cb2-31)            //读取数据
[](#cb2-32)            long stmt = OLAServer.ExecuteReader(db, $"SELECT * FROM {tableName}");
[](#cb2-33)            while (OLAServer.Read(stmt))
[](#cb2-34)            {
[](#cb2-35)                var id = OLAServer.GetInt32ByColumnName(stmt, "id");
[](#cb2-36)                var name = OLAServer.GetStringByColumnName(stmt, "name");
[](#cb2-37)                var balance = OLAServer.GetDoubleByColumnName(stmt, "balance");
[](#cb2-38)                Console.WriteLine($"Read 数据:id={id},name={name},balance={balance}");
[](#cb2-39)            };
[](#cb2-40)        }
[](#cb2-41)    }
[](#cb2-42)}
```

@tab Python

```
[](#cb3-1)# 待补充
```

### 原生方式

@tab Python

```
[](#cb4-1)# 待补充
```

## 注意事项

---

# 读取int64数据 - GetInt64

## 函数简介

读取int64类型的数据

## 函数原型

```
[](#cb1-1)long GetInt32(long ola, long stmt, int columnIndex);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

- `columnIndex` (整型数): 列索引，从0开始。

## 返回值

- 返回值：数据的值。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行SQL语句（插入操作）
[](#cb2-22)            string tableName = "user";
[](#cb2-23)            result = OLAServer.ExecuteSql(db, $"DROP TABLE IF EXISTS {tableName}");
[](#cb2-24)            result = OLAServer.ExecuteSql(db, $"CREATE TABLE {tableName} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, balance REAL)");
[](#cb2-25)            result = OLAServer.ExecuteSql(db, $"DELETE FROM {tableName} WHERE 1=1");
[](#cb2-26)            for (int i = 1; i <= 5; i++)
[](#cb2-27)            {
[](#cb2-28)                result = OLAServer.ExecuteSql(db, $"INSERT INTO {tableName}(name, balance) VALUES ('用户{i}', {100 + i / 100})");
[](#cb2-29)                Console.WriteLine($"ExecuteSql 插入数据 返回:{result}");
[](#cb2-30)            }
[](#cb2-31)            //读取数据
[](#cb2-32)            long stmt = OLAServer.ExecuteReader(db, $"SELECT * FROM {tableName}");
[](#cb2-33)            while (OLAServer.Read(stmt))
[](#cb2-34)            {
[](#cb2-35)                var id = OLAServer.GetInt32(stmt, 0);
[](#cb2-36)                var name = OLAServer.GetString(stmt, 1);
[](#cb2-37)                var balance = OLAServer.GetDouble(stmt, 2);
[](#cb2-38)                Console.WriteLine($"Read 数据:id={id},name={name},balance={balance}");
[](#cb2-39)            };
[](#cb2-40)        }
[](#cb2-41)    }
[](#cb2-42)}
```

@tab Python

```
[](#cb3-1)# 待补充
```

### 原生方式

@tab Python

```
[](#cb4-1)# 待补充
```

## 注意事项

---

# 读取long数据 -
GetInt64ByColumnName

## 函数简介

读取long类型的数据

## 函数原型

```
[](#cb1-1)long GetInt64ByColumnName(long ola, long stmt, string columnName);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

- `columnName` (字符串): 列名称。

## 返回值

- 返回值：数据的值。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行SQL语句（插入操作）
[](#cb2-22)            string tableName = "user";
[](#cb2-23)            result = OLAServer.ExecuteSql(db, $"DROP TABLE IF EXISTS {tableName}");
[](#cb2-24)            result = OLAServer.ExecuteSql(db, $"CREATE TABLE {tableName} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, balance REAL)");
[](#cb2-25)            result = OLAServer.ExecuteSql(db, $"DELETE FROM {tableName} WHERE 1=1");
[](#cb2-26)            for (int i = 1; i <= 5; i++)
[](#cb2-27)            {
[](#cb2-28)                result = OLAServer.ExecuteSql(db, $"INSERT INTO {tableName}(name, balance) VALUES ('用户{i}', {100 + i / 100})");
[](#cb2-29)                Console.WriteLine($"ExecuteSql 插入数据 返回:{result}");
[](#cb2-30)            }
[](#cb2-31)            //读取数据
[](#cb2-32)            long stmt = OLAServer.ExecuteReader(db, $"SELECT * FROM {tableName}");
[](#cb2-33)            while (OLAServer.Read(stmt))
[](#cb2-34)            {
[](#cb2-35)                var id = OLAServer.GetInt32ByColumnName(stmt, "id");
[](#cb2-36)                var name = OLAServer.GetStringByColumnName(stmt, "name");
[](#cb2-37)                var balance = OLAServer.GetDoubleByColumnName(stmt, "balance");
[](#cb2-38)                Console.WriteLine($"Read 数据:id={id},name={name},balance={balance}");
[](#cb2-39)            };
[](#cb2-40)        }
[](#cb2-41)    }
[](#cb2-42)}
```

@tab Python

```
[](#cb3-1)# 待补充
```

### 原生方式

@tab Python

```
[](#cb4-1)# 待补充
```

## 注意事项

---

# 读取列名称 - GetColumnName

## 函数简介

读取查询结果集中指定列的名称，返回列名的字符串指针。

## 函数原型

```
[](#cb1-1)long GetColumnName(long ola, long stmt, int columnIndex);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

- `columnIndex` (整型数): 列索引，从0开始。

## 返回值

- 返回值：列名的字符串指针。如果操作失败，返回 `0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行查询并返回STMT指针
[](#cb2-22)            string sql = "SELECT * FROM MyTable";
[](#cb2-23)            long stmtPtr = OLAServer.ExecuteReader(db, sql);
[](#cb2-24)            if (stmtPtr != 0)
[](#cb2-25)            {
[](#cb2-26)                Console.WriteLine("查询成功，STMT指针已返回。");
[](#cb2-27)
[](#cb2-28)                // 读取列数量
[](#cb2-29)                int columnCount = OLAServer.GetColumnCount(stmtPtr);
[](#cb2-30)                Console.WriteLine($"查询结果的列数: {columnCount}");
[](#cb2-31)
[](#cb2-32)                // 遍历列并读取列名
[](#cb2-33)                for (int i = 0; i < columnCount; i++)
[](#cb2-34)                {
[](#cb2-35)                    long columnNamePtr = OLAServer.GetColumnName(stmtPtr, i);
[](#cb2-36)                    if (columnNamePtr != 0)
[](#cb2-37)                    {
[](#cb2-38)                        string columnName = Marshal.PtrToStringAnsi(new IntPtr(columnNamePtr));
[](#cb2-39)                        Console.WriteLine($"列 {i} 的名称: {columnName}");
[](#cb2-40)                    }
[](#cb2-41)                    else
[](#cb2-42)                    {
[](#cb2-43)                        Console.WriteLine($"读取列 {i} 的名称失败。");
[](#cb2-44)                    }
[](#cb2-45)                }
[](#cb2-46)            }
[](#cb2-47)            else
[](#cb2-48)            {
[](#cb2-49)                Console.WriteLine("查询失败。");
[](#cb2-50)            }
[](#cb2-51)        }
[](#cb2-52)    }
[](#cb2-53)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 执行查询并返回STMT指针
[](#cb3-14)sql = "SELECT * FROM MyTable"
[](#cb3-15)stmtPtr = OLAServer.ExecuteReader(db, sql)
[](#cb3-16)if stmtPtr != 0:
[](#cb3-17)    print("查询成功，STMT指针已返回。")
[](#cb3-18)
[](#cb3-19)    # 读取列数量
[](#cb3-20)    columnCount = OLAServer.GetColumnCount(stmtPtr)
[](#cb3-21)    print(f"查询结果的列数: {columnCount}")
[](#cb3-22)
[](#cb3-23)    # 遍历列并读取列名
[](#cb3-24)    for i in range(columnCount):
[](#cb3-25)        columnNamePtr = OLAServer.GetColumnName(stmtPtr, i)
[](#cb3-26)        if columnNamePtr != 0:
[](#cb3-27)            columnName = ctypes.cast(columnNamePtr, ctypes.c_char_p).value.decode('utf-8')
[](#cb3-28)            print(f"列 {i} 的名称: {columnName}")
[](#cb3-29)        else:
[](#cb3-30)            print(f"读取列 {i} 的名称失败。")
[](#cb3-31)else:
[](#cb3-32)    print("查询失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 执行查询并返回STMT指针
[](#cb4-33)sql = "SELECT * FROM MyTable"
[](#cb4-34)olaplug_dll.ExecuteReader.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-35)olaplug_dll.ExecuteReader.restype = c_void_p
[](#cb4-36)stmtPtr = olaplug_dll.ExecuteReader(ola_obj, db, sql.encode('utf-8'))
[](#cb4-37)if stmtPtr != 0:
[](#cb4-38)    print("查询成功，STMT指针已返回。")
[](#cb4-39)
[](#cb4-40)    # 读取列数量
[](#cb4-41)    olaplug_dll.GetColumnCount.argtypes = [c_void_p, c_void_p]
[](#cb4-42)    olaplug_dll.GetColumnCount.restype = c_int32
[](#cb4-43)    columnCount = olaplug_dll.GetColumnCount(ola_obj, stmtPtr)
[](#cb4-44)    print(f"查询结果的列数: {columnCount}")
[](#cb4-45)
[](#cb4-46)    # 遍历列并读取列名
[](#cb4-47)    for i in range(columnCount):
[](#cb4-48)        olaplug_dll.GetColumnName.argtypes = [c_void_p, c_void_p, c_int]
[](#cb4-49)        olaplug_dll.GetColumnName.restype = c_void_p
[](#cb4-50)        columnNamePtr = olaplug_dll.GetColumnName(ola_obj, stmtPtr, i)
[](#cb4-51)        if columnNamePtr != 0:
[](#cb4-52)            columnName = ctypes.cast(columnNamePtr, ctypes.c_char_p).value.decode('utf-8')
[](#cb4-53)            print(f"列 {i} 的名称: {columnName}")
[](#cb4-54)        else:
[](#cb4-55)            print(f"读取列 {i} 的名称失败。")
[](#cb4-56)else:
[](#cb4-57)    print("查询失败。")
```

## 注意事项

- 该函数用于获取查询结果集中指定列的名称，通常与 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html) 和
[GetColumnCount](/数据库/读取列数量%20-%20GetColumnCount.html)
配合使用。

- 如果列索引无效或操作失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 使用完返回的字符串指针后，应妥善处理内存，避免内存泄漏。

---

# 读取列数量 - GetColumnCount

## 函数简介

读取查询结果集中的列数量，返回结果集的列数。

## 函数原型

```
[](#cb1-1)int GetColumnCount(long ola, long stmt);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

## 返回值

- 返回值：查询结果集的列数。如果操作失败，返回 `0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行查询并返回STMT指针
[](#cb2-22)            string sql = "SELECT * FROM MyTable";
[](#cb2-23)            long stmtPtr = OLAServer.ExecuteReader(db, sql);
[](#cb2-24)            if (stmtPtr != 0)
[](#cb2-25)            {
[](#cb2-26)                Console.WriteLine("查询成功，STMT指针已返回。");
[](#cb2-27)
[](#cb2-28)                // 读取查询结果的列数量
[](#cb2-29)                int columnCount = OLAServer.GetColumnCount(stmtPtr);
[](#cb2-30)                Console.WriteLine($"查询结果的列数: {columnCount}");
[](#cb2-31)            }
[](#cb2-32)            else
[](#cb2-33)            {
[](#cb2-34)                Console.WriteLine("查询失败。");
[](#cb2-35)            }
[](#cb2-36)        }
[](#cb2-37)    }
[](#cb2-38)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 执行查询并返回STMT指针
[](#cb3-14)sql = "SELECT * FROM MyTable"
[](#cb3-15)stmtPtr = OLAServer.ExecuteReader(db, sql)
[](#cb3-16)if stmtPtr != 0:
[](#cb3-17)    print("查询成功，STMT指针已返回。")
[](#cb3-18)
[](#cb3-19)    # 读取查询结果的列数量
[](#cb3-20)    columnCount = OLAServer.GetColumnCount(stmtPtr)
[](#cb3-21)    print(f"查询结果的列数: {columnCount}")
[](#cb3-22)else:
[](#cb3-23)    print("查询失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 执行查询并返回STMT指针
[](#cb4-33)sql = "SELECT * FROM MyTable"
[](#cb4-34)olaplug_dll.ExecuteReader.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-35)olaplug_dll.ExecuteReader.restype = c_void_p
[](#cb4-36)stmtPtr = olaplug_dll.ExecuteReader(ola_obj, db, sql.encode('utf-8'))
[](#cb4-37)if stmtPtr != 0:
[](#cb4-38)    print("查询成功，STMT指针已返回。")
[](#cb4-39)
[](#cb4-40)    # 读取查询结果的列数量
[](#cb4-41)    olaplug_dll.GetColumnCount.argtypes = [c_void_p, c_void_p]
[](#cb4-42)    olaplug_dll.GetColumnCount.restype = c_int32
[](#cb4-43)    columnCount = olaplug_dll.GetColumnCount(ola_obj, stmtPtr)
[](#cb4-44)    print(f"查询结果的列数: {columnCount}")
[](#cb4-45)else:
[](#cb4-46)    print("查询失败。")
```

## 注意事项

- 该函数用于获取查询结果集的列数，通常与 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
配合使用。

- 如果查询失败或结果集为空，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 使用完STMT指针后，应妥善处理资源，避免内存泄漏。

---

# 读取列类型 - GetColumnType

## 函数简介

读取查询结果集中指定列的数据类型，返回列的类型代码。

## 函数原型

```
[](#cb1-1)int GetColumnType(long ola, long stmt, int columnIndex);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

- `columnIndex` (整型数): 列索引，从0开始。

## 返回值

- 返回值：列的类型代码，具体如下：

`SQLITE_INTEGER`：整数类型，返回 `1`。

- `SQLITE_FLOAT`：浮点数类型，返回 `2`。

- `SQLITE_TEXT`：文本类型，返回 `3`。

- `SQLITE_BLOB`：二进制大对象类型，返回
`4`。

- `SQLITE_NULL`：空值类型，返回 `5`。

- 如果操作失败，返回 `0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行查询并返回STMT指针
[](#cb2-22)            string sql = "SELECT * FROM MyTable";
[](#cb2-23)            long stmtPtr = OLAServer.ExecuteReader(db, sql);
[](#cb2-24)            if (stmtPtr != 0)
[](#cb2-25)            {
[](#cb2-26)                Console.WriteLine("查询成功，STMT指针已返回。");
[](#cb2-27)
[](#cb2-28)                // 读取列数量
[](#cb2-29)                int columnCount = OLAServer.GetColumnCount(stmtPtr);
[](#cb2-30)                Console.WriteLine($"查询结果的列数: {columnCount}");
[](#cb2-31)
[](#cb2-32)                // 遍历列并读取列类型
[](#cb2-33)                for (int i = 0; i < columnCount; i++)
[](#cb2-34)                {
[](#cb2-35)                    int columnType = OLAServer.GetColumnType(stmtPtr, i);
[](#cb2-36)                    string typeName = columnType switch
[](#cb2-37)                    {
[](#cb2-38)                        1 => "SQLITE_INTEGER",
[](#cb2-39)                        2 => "SQLITE_FLOAT",
[](#cb2-40)                        3 => "SQLITE_TEXT",
[](#cb2-41)                        4 => "SQLITE_BLOB",
[](#cb2-42)                        5 => "SQLITE_NULL",
[](#cb2-43)                        _ => "UNKNOWN"
[](#cb2-44)                    };
[](#cb2-45)                    Console.WriteLine($"列 {i} 的类型: {typeName}");
[](#cb2-46)                }
[](#cb2-47)            }
[](#cb2-48)            else
[](#cb2-49)            {
[](#cb2-50)                Console.WriteLine("查询失败。");
[](#cb2-51)            }
[](#cb2-52)        }
[](#cb2-53)    }
[](#cb2-54)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 执行查询并返回STMT指针
[](#cb3-14)sql = "SELECT * FROM MyTable"
[](#cb3-15)stmtPtr = OLAServer.ExecuteReader(db, sql)
[](#cb3-16)if stmtPtr != 0:
[](#cb3-17)    print("查询成功，STMT指针已返回。")
[](#cb3-18)
[](#cb3-19)    # 读取列数量
[](#cb3-20)    columnCount = OLAServer.GetColumnCount(stmtPtr)
[](#cb3-21)    print(f"查询结果的列数: {columnCount}")
[](#cb3-22)
[](#cb3-23)    # 遍历列并读取列类型
[](#cb3-24)    for i in range(columnCount):
[](#cb3-25)        columnType = OLAServer.GetColumnType(stmtPtr, i)
[](#cb3-26)        typeName = {
[](#cb3-27)            1: "SQLITE_INTEGER",
[](#cb3-28)            2: "SQLITE_FLOAT",
[](#cb3-29)            3: "SQLITE_TEXT",
[](#cb3-30)            4: "SQLITE_BLOB",
[](#cb3-31)            5: "SQLITE_NULL"
[](#cb3-32)        }.get(columnType, "UNKNOWN")
[](#cb3-33)        print(f"列 {i} 的类型: {typeName}")
[](#cb3-34)else:
[](#cb3-35)    print("查询失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 执行查询并返回STMT指针
[](#cb4-33)sql = "SELECT * FROM MyTable"
[](#cb4-34)olaplug_dll.ExecuteReader.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-35)olaplug_dll.ExecuteReader.restype = c_void_p
[](#cb4-36)stmtPtr = olaplug_dll.ExecuteReader(ola_obj, db, sql.encode('utf-8'))
[](#cb4-37)if stmtPtr != 0:
[](#cb4-38)    print("查询成功，STMT指针已返回。")
[](#cb4-39)
[](#cb4-40)    # 读取列数量
[](#cb4-41)    olaplug_dll.GetColumnCount.argtypes = [c_void_p, c_void_p]
[](#cb4-42)    olaplug_dll.GetColumnCount.restype = c_int32
[](#cb4-43)    columnCount = olaplug_dll.GetColumnCount(ola_obj, stmtPtr)
[](#cb4-44)    print(f"查询结果的列数: {columnCount}")
[](#cb4-45)
[](#cb4-46)    # 遍历列并读取列类型
[](#cb4-47)    for i in range(columnCount):
[](#cb4-48)        olaplug_dll.GetColumnType.argtypes = [c_void_p, c_void_p, c_int]
[](#cb4-49)        olaplug_dll.GetColumnType.restype = c_int32
[](#cb4-50)        columnType = olaplug_dll.GetColumnType(ola_obj, stmtPtr, i)
[](#cb4-51)        typeName = {
[](#cb4-52)            1: "SQLITE_INTEGER",
[](#cb4-53)            2: "SQLITE_FLOAT",
[](#cb4-54)            3: "SQLITE_TEXT",
[](#cb4-55)            4: "SQLITE_BLOB",
[](#cb4-56)            5: "SQLITE_NULL"
[](#cb4-57)        }.get(columnType, "UNKNOWN")
[](#cb4-58)        print(f"列 {i} 的类型: {typeName}")
[](#cb4-59)else:
[](#cb4-60)    print("查询失败。")
```

## 注意事项

- 该函数用于获取查询结果集中指定列的数据类型，通常与 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html) 和
[GetColumnCount](/数据库/读取列数量%20-%20GetColumnCount.html)
配合使用。

- 如果列索引无效或操作失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 列类型代码与SQLite数据库的类型定义一致，具体如下：

`SQLITE_INTEGER`：整数类型，返回 `1`。

- `SQLITE_FLOAT`：浮点数类型，返回 `2`。

- `SQLITE_TEXT`：文本类型，返回 `3`。

- `SQLITE_BLOB`：二进制大对象类型，返回
`4`。

- `SQLITE_NULL`：空值类型，返回 `5`。

---

# 读取列索引 - GetColumnIndex

## 函数简介

根据列名读取查询结果集中指定列的索引，返回列的索引（从 `0`
开始）。

## 函数原型

```
[](#cb1-1)int GetColumnIndex(long ola, long stmt, string columnName);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

- `columnName` (字符串): 列名称。

## 返回值

- 返回值：列的索引（从 `0`
开始）。如果列名不存在或操作失败，返回 `-1`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行查询并返回STMT指针
[](#cb2-22)            string sql = "SELECT * FROM MyTable";
[](#cb2-23)            long stmtPtr = OLAServer.ExecuteReader(db, sql);
[](#cb2-24)            if (stmtPtr != 0)
[](#cb2-25)            {
[](#cb2-26)                Console.WriteLine("查询成功，STMT指针已返回。");
[](#cb2-27)
[](#cb2-28)                // 读取列索引
[](#cb2-29)                string columnName = "MyColumn";
[](#cb2-30)                int columnIndex = OLAServer.GetColumnIndex(stmtPtr, columnName);
[](#cb2-31)                if (columnIndex != -1)
[](#cb2-32)                {
[](#cb2-33)                    Console.WriteLine($"列 '{columnName}' 的索引: {columnIndex}");
[](#cb2-34)                }
[](#cb2-35)                else
[](#cb2-36)                {
[](#cb2-37)                    Console.WriteLine($"列 '{columnName}' 不存在或读取失败。");
[](#cb2-38)                }
[](#cb2-39)            }
[](#cb2-40)            else
[](#cb2-41)            {
[](#cb2-42)                Console.WriteLine("查询失败。");
[](#cb2-43)            }
[](#cb2-44)        }
[](#cb2-45)    }
[](#cb2-46)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 执行查询并返回STMT指针
[](#cb3-14)sql = "SELECT * FROM MyTable"
[](#cb3-15)stmtPtr = OLAServer.ExecuteReader(db, sql)
[](#cb3-16)if stmtPtr != 0:
[](#cb3-17)    print("查询成功，STMT指针已返回。")
[](#cb3-18)
[](#cb3-19)    # 读取列索引
[](#cb3-20)    columnName = "MyColumn"
[](#cb3-21)    columnIndex = OLAServer.GetColumnIndex(stmtPtr, columnName)
[](#cb3-22)    if columnIndex != -1:
[](#cb3-23)        print(f"列 '{columnName}' 的索引: {columnIndex}")
[](#cb3-24)    else:
[](#cb3-25)        print(f"列 '{columnName}' 不存在或读取失败。")
[](#cb3-26)else:
[](#cb3-27)    print("查询失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 执行查询并返回STMT指针
[](#cb4-33)sql = "SELECT * FROM MyTable"
[](#cb4-34)olaplug_dll.ExecuteReader.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-35)olaplug_dll.ExecuteReader.restype = c_void_p
[](#cb4-36)stmtPtr = olaplug_dll.ExecuteReader(ola_obj, db, sql.encode('utf-8'))
[](#cb4-37)if stmtPtr != 0:
[](#cb4-38)    print("查询成功，STMT指针已返回。")
[](#cb4-39)
[](#cb4-40)    # 读取列索引
[](#cb4-41)    columnName = "MyColumn"
[](#cb4-42)    olaplug_dll.GetColumnIndex.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-43)    olaplug_dll.GetColumnIndex.restype = c_int32
[](#cb4-44)    columnIndex = olaplug_dll.GetColumnIndex(ola_obj, stmtPtr, columnName.encode('utf-8'))
[](#cb4-45)    if columnIndex != -1:
[](#cb4-46)        print(f"列 '{columnName}' 的索引: {columnIndex}")
[](#cb4-47)    else:
[](#cb4-48)        print(f"列 '{columnName}' 不存在或读取失败。")
[](#cb4-49)else:
[](#cb4-50)    print("查询失败。")
```

## 注意事项

- 该函数用于根据列名获取查询结果集中指定列的索引，通常与 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html) 和
[GetColumnName](/数据库/读取列名称%20-%20GetColumnName.html)
配合使用。

- 如果列名不存在或操作失败，函数将返回 `-1`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 列名区分大小写，确保传入的列名与数据库中的列名一致。

---

# 读取string数据 - GetString

## 函数简介

读取string类型的数据

## 函数原型

```
[](#cb1-1)long GetString(long ola, long stmt, int columnIndex);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

- `columnIndex` (整型数): 列索引，从0开始。

## 返回值

- 返回值：数据的值。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行SQL语句（插入操作）
[](#cb2-22)            string tableName = "user";
[](#cb2-23)            result = OLAServer.ExecuteSql(db, $"DROP TABLE IF EXISTS {tableName}");
[](#cb2-24)            result = OLAServer.ExecuteSql(db, $"CREATE TABLE {tableName} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, balance REAL)");
[](#cb2-25)            result = OLAServer.ExecuteSql(db, $"DELETE FROM {tableName} WHERE 1=1");
[](#cb2-26)            for (int i = 1; i <= 5; i++)
[](#cb2-27)            {
[](#cb2-28)                result = OLAServer.ExecuteSql(db, $"INSERT INTO {tableName}(name, balance) VALUES ('用户{i}', {100 + i / 100})");
[](#cb2-29)                Console.WriteLine($"ExecuteSql 插入数据 返回:{result}");
[](#cb2-30)            }
[](#cb2-31)            //读取数据
[](#cb2-32)            long stmt = OLAServer.ExecuteReader(db, $"SELECT * FROM {tableName}");
[](#cb2-33)            while (OLAServer.Read(stmt))
[](#cb2-34)            {
[](#cb2-35)                var id = OLAServer.GetInt32(stmt, 0);
[](#cb2-36)                var name = OLAServer.GetString(stmt, 1);
[](#cb2-37)                var balance = OLAServer.GetDouble(stmt, 2);
[](#cb2-38)                Console.WriteLine($"Read 数据:id={id},name={name},balance={balance}");
[](#cb2-39)            };
[](#cb2-40)        }
[](#cb2-41)    }
[](#cb2-42)}
```

@tab Python

```
[](#cb3-1)# 待补充
```

### 原生方式

@tab Python

```
[](#cb4-1)# 待补充
```

## 注意事项

---

# 读取string数据 -
GetStringByColumnName

## 函数简介

读取string类型的数据

## 函数原型

```
[](#cb1-1)long GetStringByColumnName(long ola, long stmt, string columnName);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

- `columnName` (字符串): 列名称。

## 返回值

- 返回值：数据的值。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行SQL语句（插入操作）
[](#cb2-22)            string tableName = "user";
[](#cb2-23)            result = OLAServer.ExecuteSql(db, $"DROP TABLE IF EXISTS {tableName}");
[](#cb2-24)            result = OLAServer.ExecuteSql(db, $"CREATE TABLE {tableName} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, balance REAL)");
[](#cb2-25)            result = OLAServer.ExecuteSql(db, $"DELETE FROM {tableName} WHERE 1=1");
[](#cb2-26)            for (int i = 1; i <= 5; i++)
[](#cb2-27)            {
[](#cb2-28)                result = OLAServer.ExecuteSql(db, $"INSERT INTO {tableName}(name, balance) VALUES ('用户{i}', {100 + i / 100})");
[](#cb2-29)                Console.WriteLine($"ExecuteSql 插入数据 返回:{result}");
[](#cb2-30)            }
[](#cb2-31)            //读取数据
[](#cb2-32)            long stmt = OLAServer.ExecuteReader(db, $"SELECT * FROM {tableName}");
[](#cb2-33)            while (OLAServer.Read(stmt))
[](#cb2-34)            {
[](#cb2-35)                var id = OLAServer.GetInt32ByColumnName(stmt, "id");
[](#cb2-36)                var name = OLAServer.GetStringByColumnName(stmt, "name");
[](#cb2-37)                var balance = OLAServer.GetDoubleByColumnName(stmt, "balance");
[](#cb2-38)                Console.WriteLine($"Read 数据:id={id},name={name},balance={balance}");
[](#cb2-39)            };
[](#cb2-40)        }
[](#cb2-41)    }
[](#cb2-42)}
```

@tab Python

```
[](#cb3-1)# 待补充
```

### 原生方式

@tab Python

```
[](#cb4-1)# 待补充
```

## 注意事项

---

# 读取所有表名 -
GetAllTableNames

## 函数简介

读取数据库中所有表的名称，返回一个包含表名的字符串列表指针。

## 函数原型

```
[](#cb1-1)long GetAllTableNames(long ola, const long db);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

## 返回值

- 返回值：包含所有表名的字符串列表指针。如果操作失败，返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 读取所有表名
[](#cb2-22)            long tableNamesPtr = OLAServer.GetAllTableNames(db);
[](#cb2-23)            if (tableNamesPtr != 0)
[](#cb2-24)            {
[](#cb2-25)                // 假设返回的是一个以逗号分隔的表名字符串
[](#cb2-26)                string tableNames = Marshal.PtrToStringAnsi(new IntPtr(tableNamesPtr));
[](#cb2-27)                string[] tables = tableNames.Split(',');
[](#cb2-28)                Console.WriteLine("数据库中的表名:");
[](#cb2-29)                foreach (var table in tables)
[](#cb2-30)                {
[](#cb2-31)                    Console.WriteLine(table);
[](#cb2-32)                }
[](#cb2-33)            }
[](#cb2-34)            else
[](#cb2-35)            {
[](#cb2-36)                Console.WriteLine("读取表名失败。");
[](#cb2-37)            }
[](#cb2-38)        }
[](#cb2-39)    }
[](#cb2-40)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 读取所有表名
[](#cb3-14)tableNamesPtr = OLAServer.GetAllTableNames(db)
[](#cb3-15)if tableNamesPtr != 0:
[](#cb3-16)    # 假设返回的是一个以逗号分隔的表名字符串
[](#cb3-17)    tableNames = ctypes.cast(tableNamesPtr, ctypes.c_char_p).value.decode('utf-8')
[](#cb3-18)    tables = tableNames.split(',')
[](#cb3-19)    print("数据库中的表名:")
[](#cb3-20)    for table in tables:
[](#cb3-21)        print(table)
[](#cb3-22)else:
[](#cb3-23)    print("读取表名失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 读取所有表名
[](#cb4-33)olaplug_dll.GetAllTableNames.argtypes = [c_void_p, c_void_p]
[](#cb4-34)olaplug_dll.GetAllTableNames.restype = c_void_p
[](#cb4-35)tableNamesPtr = olaplug_dll.GetAllTableNames(ola_obj, db)
[](#cb4-36)if tableNamesPtr != 0:
[](#cb4-37)    # 假设返回的是一个以逗号分隔的表名字符串
[](#cb4-38)    tableNames = ctypes.cast(tableNamesPtr, ctypes.c_char_p).value.decode('utf-8')
[](#cb4-39)    tables = tableNames.split(',')
[](#cb4-40)    print("数据库中的表名:")
[](#cb4-41)    for table in tables:
[](#cb4-42)        print(table)
[](#cb4-43)else:
[](#cb4-44)    print("读取表名失败。")
```

## 注意事项

- 返回的表名字符串列表通常是以特定分隔符（如逗号）分隔的字符串，需要根据实际情况进行解析。

- 如果数据库中没有表或操作失败，函数将返回 `0`。

- 使用完返回的字符串指针后，应妥善处理内存，避免内存泄漏。

---

# 读取查询结果的数量 -
GetDataCount

## 函数简介

读取查询结果集中数据的行数，返回结果集的行数。

## 函数原型

```
[](#cb1-1)int GetDataCount(long ola, long stmt);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

## 返回值

- 返回值：查询结果集的行数。如果操作失败，返回 `0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行查询并返回STMT指针
[](#cb2-22)            string sql = "SELECT * FROM MyTable";
[](#cb2-23)            long stmtPtr = OLAServer.ExecuteReader(db, sql);
[](#cb2-24)            if (stmtPtr != 0)
[](#cb2-25)            {
[](#cb2-26)                Console.WriteLine("查询成功，STMT指针已返回。");
[](#cb2-27)
[](#cb2-28)                // 读取查询结果的数量
[](#cb2-29)                int rowCount = OLAServer.GetDataCount(stmtPtr);
[](#cb2-30)                Console.WriteLine($"查询结果的行数: {rowCount}");
[](#cb2-31)            }
[](#cb2-32)            else
[](#cb2-33)            {
[](#cb2-34)                Console.WriteLine("查询失败。");
[](#cb2-35)            }
[](#cb2-36)        }
[](#cb2-37)    }
[](#cb2-38)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 执行查询并返回STMT指针
[](#cb3-14)sql = "SELECT * FROM MyTable"
[](#cb3-15)stmtPtr = OLAServer.ExecuteReader(db, sql)
[](#cb3-16)if stmtPtr != 0:
[](#cb3-17)    print("查询成功，STMT指针已返回。")
[](#cb3-18)
[](#cb3-19)    # 读取查询结果的数量
[](#cb3-20)    rowCount = OLAServer.GetDataCount(stmtPtr)
[](#cb3-21)    print(f"查询结果的行数: {rowCount}")
[](#cb3-22)else:
[](#cb3-23)    print("查询失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 执行查询并返回STMT指针
[](#cb4-33)sql = "SELECT * FROM MyTable"
[](#cb4-34)olaplug_dll.ExecuteReader.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-35)olaplug_dll.ExecuteReader.restype = c_void_p
[](#cb4-36)stmtPtr = olaplug_dll.ExecuteReader(ola_obj, db, sql.encode('utf-8'))
[](#cb4-37)if stmtPtr != 0:
[](#cb4-38)    print("查询成功，STMT指针已返回。")
[](#cb4-39)
[](#cb4-40)    # 读取查询结果的数量
[](#cb4-41)    olaplug_dll.GetDataCount.argtypes = [c_void_p, c_void_p]
[](#cb4-42)    olaplug_dll.GetDataCount.restype = c_int32
[](#cb4-43)    rowCount = olaplug_dll.GetDataCount(ola_obj, stmtPtr)
[](#cb4-44)    print(f"查询结果的行数: {rowCount}")
[](#cb4-45)else:
[](#cb4-46)    print("查询失败。")
```

## 注意事项

- 该函数用于获取查询结果集的行数，通常与 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
配合使用。

- 如果查询失败或结果集为空，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 使用完STMT指针后，应妥善处理资源，避免内存泄漏。

---

# 读取游标 - Read

## 函数简介

从STMT（Statement）指针中读取下一行数据，返回读取结果。通常用于遍历查询结果集。

## 函数原型

```
[](#cb1-1)int Read(long ola, long stmt);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

## 返回值

- 返回值：读取结果。成功读取一行数据返回
`1`，如果没有更多数据或读取失败，返回 `0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行查询并返回STMT指针
[](#cb2-22)            string sql = "SELECT * FROM MyTable";
[](#cb2-23)            long stmtPtr = OLAServer.ExecuteReader(db, sql);
[](#cb2-24)            if (stmtPtr != 0)
[](#cb2-25)            {
[](#cb2-26)                Console.WriteLine("查询成功，STMT指针已返回。");
[](#cb2-27)
[](#cb2-28)                // 遍历结果集
[](#cb2-29)                while (OLAServer.Read(stmtPtr) == 1)
[](#cb2-30)                {
[](#cb2-31)                    // 读取当前行的数据（假设有一个获取数据的函数）
[](#cb2-32)                    // string rowData = OLAServer.GetRowData(stmtPtr);
[](#cb2-33)                    // Console.WriteLine(rowData);
[](#cb2-34)                }
[](#cb2-35)            }
[](#cb2-36)            else
[](#cb2-37)            {
[](#cb2-38)                Console.WriteLine("查询失败。");
[](#cb2-39)            }
[](#cb2-40)        }
[](#cb2-41)    }
[](#cb2-42)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 执行查询并返回STMT指针
[](#cb3-14)sql = "SELECT * FROM MyTable"
[](#cb3-15)stmtPtr = OLAServer.ExecuteReader(db, sql)
[](#cb3-16)if stmtPtr != 0:
[](#cb3-17)    print("查询成功，STMT指针已返回。")
[](#cb3-18)
[](#cb3-19)    # 遍历结果集
[](#cb3-20)    while OLAServer.Read(stmtPtr) == 1:
[](#cb3-21)        # 读取当前行的数据（假设有一个获取数据的函数）
[](#cb3-22)        # rowData = OLAServer.GetRowData(stmtPtr)
[](#cb3-23)        # print(rowData)
[](#cb3-24)        pass
[](#cb3-25)else:
[](#cb3-26)    print("查询失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 执行查询并返回STMT指针
[](#cb4-33)sql = "SELECT * FROM MyTable"
[](#cb4-34)olaplug_dll.ExecuteReader.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-35)olaplug_dll.ExecuteReader.restype = c_void_p
[](#cb4-36)stmtPtr = olaplug_dll.ExecuteReader(ola_obj, db, sql.encode('utf-8'))
[](#cb4-37)if stmtPtr != 0:
[](#cb4-38)    print("查询成功，STMT指针已返回。")
[](#cb4-39)
[](#cb4-40)    # 遍历结果集
[](#cb4-41)    while olaplug_dll.Read(ola_obj, stmtPtr) == 1:
[](#cb4-42)        # 读取当前行的数据（假设有一个获取数据的函数）
[](#cb4-43)        # rowData = olaplug_dll.GetRowData(stmtPtr)
[](#cb4-44)        # print(rowData)
[](#cb4-45)        pass
[](#cb4-46)else:
[](#cb4-47)    print("查询失败。")
```

## 注意事项

- 该函数用于逐行读取查询结果集，通常与 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
配合使用。

- 如果没有更多数据或读取失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 使用完STMT指针后，应妥善处理资源，避免内存泄漏。

---

# 执行查询 - ExecuteReader

## 函数简介

执行指定的SQL查询语句，并返回一个STMT（Statement）指针，用于遍历查询结果集。该函数适用于需要逐行读取查询结果的场景。

## 函数原型

```
[](#cb1-1)long ExecuteReader(long ola, const long db, string sql);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `sql` (字符串): 要执行的SQL查询语句。

## 返回值

- 返回值：STMT指针，用于遍历查询结果集。如果查询失败，返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行查询并返回STMT指针
[](#cb2-22)            string sql = "SELECT * FROM MyTable";
[](#cb2-23)            long stmtPtr = OLAServer.ExecuteReader(db, sql);
[](#cb2-24)            if (stmtPtr != 0)
[](#cb2-25)            {
[](#cb2-26)                Console.WriteLine("查询成功，STMT指针已返回。");
[](#cb2-27)                // 遍历结果集的代码（假设有一个遍历函数）
[](#cb2-28)                // OLAServer.TraverseResultSet(stmtPtr);
[](#cb2-29)            }
[](#cb2-30)            else
[](#cb2-31)            {
[](#cb2-32)                Console.WriteLine("查询失败。");
[](#cb2-33)            }
[](#cb2-34)        }
[](#cb2-35)    }
[](#cb2-36)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 执行查询并返回STMT指针
[](#cb3-14)sql = "SELECT * FROM MyTable"
[](#cb3-15)stmtPtr = OLAServer.ExecuteReader(db, sql)
[](#cb3-16)if stmtPtr != 0:
[](#cb3-17)    print("查询成功，STMT指针已返回。")
[](#cb3-18)    # 遍历结果集的代码（假设有一个遍历函数）
[](#cb3-19)    # OLAServer.TraverseResultSet(stmtPtr)
[](#cb3-20)else:
[](#cb3-21)    print("查询失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 执行查询并返回STMT指针
[](#cb4-33)sql = "SELECT * FROM MyTable"
[](#cb4-34)olaplug_dll.ExecuteReader.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-35)olaplug_dll.ExecuteReader.restype = c_void_p
[](#cb4-36)stmtPtr = olaplug_dll.ExecuteReader(ola_obj, db, sql.encode('utf-8'))
[](#cb4-37)if stmtPtr != 0:
[](#cb4-38)    print("查询成功，STMT指针已返回。")
[](#cb4-39)    # 遍历结果集的代码（假设有一个遍历函数）
[](#cb4-40)    # olaplug_dll.TraverseResultSet(stmtPtr)
[](#cb4-41)else:
[](#cb4-42)    print("查询失败。")
```

## 注意事项

- 该函数适用于需要逐行读取查询结果的场景，返回的STMT指针可以用于遍历结果集。

- 如果查询失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 使用完STMT指针后，应妥善处理资源，避免内存泄漏。

---

# 读取表结构信息 -
GetTableInfo

## 函数简介

读取指定表的结构信息，返回包含表结构信息的字符串指针。

## 函数原型

```
[](#cb1-1)long GetTableInfo(long ola, const long db, string tableName);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `tableName` (字符串): 表名称。

## 返回值

- 返回值：包含表结构信息的字符串指针。如果操作失败，返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 读取表结构信息
[](#cb2-22)            string tableName = "MyTable";
[](#cb2-23)            long tableInfoPtr = OLAServer.GetTableInfo(db, tableName);
[](#cb2-24)            if (tableInfoPtr != 0)
[](#cb2-25)            {
[](#cb2-26)                string tableInfo = Marshal.PtrToStringAnsi(new IntPtr(tableInfoPtr));
[](#cb2-27)                Console.WriteLine($"表 {tableName} 的结构信息:");
[](#cb2-28)                Console.WriteLine(tableInfo);
[](#cb2-29)            }
[](#cb2-30)            else
[](#cb2-31)            {
[](#cb2-32)                Console.WriteLine($"读取表 {tableName} 的结构信息失败。");
[](#cb2-33)            }
[](#cb2-34)        }
[](#cb2-35)    }
[](#cb2-36)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 读取表结构信息
[](#cb3-14)tableName = "MyTable"
[](#cb3-15)tableInfoPtr = OLAServer.GetTableInfo(db, tableName)
[](#cb3-16)if tableInfoPtr != 0:
[](#cb3-17)    tableInfo = ctypes.cast(tableInfoPtr, ctypes.c_char_p).value.decode('utf-8')
[](#cb3-18)    print(f"表 {tableName} 的结构信息:")
[](#cb3-19)    print(tableInfo)
[](#cb3-20)else:
[](#cb3-21)    print(f"读取表 {tableName} 的结构信息失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 读取表结构信息
[](#cb4-33)tableName = "MyTable"
[](#cb4-34)olaplug_dll.GetTableInfo.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-35)olaplug_dll.GetTableInfo.restype = c_void_p
[](#cb4-36)tableInfoPtr = olaplug_dll.GetTableInfo(ola_obj, db, tableName.encode('utf-8'))
[](#cb4-37)if tableInfoPtr != 0:
[](#cb4-38)    tableInfo = ctypes.cast(tableInfoPtr, ctypes.c_char_p).value.decode('utf-8')
[](#cb4-39)    print(f"表 {tableName} 的结构信息:")
[](#cb4-40)    print(tableInfo)
[](#cb4-41)else:
[](#cb4-42)    print(f"读取表 {tableName} 的结构信息失败。")
```

## 注意事项

- 返回的表结构信息通常是一个字符串，可能包含表的列名、列类型、约束等信息，具体格式取决于数据库的实现。

- 如果表不存在或操作失败，函数将返回 `0`。

- 使用完返回的字符串指针后，应妥善处理内存，避免内存泄漏。

---

# 读取表结构详细信息 -
GetTableInfoDetail

## 函数简介

读取指定表的详细结构信息，返回包含表详细结构信息的字符串指针。与
`GetTableInfo`
相比，此函数提供更详细的表结构信息，例如列的类型、长度、是否为主键、是否为外键等。

## 函数原型

```
[](#cb1-1)long GetTableInfoDetail(long ola, const long db, string tableName);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `tableName` (字符串): 表名称。

## 返回值

- 返回值：包含表详细结构信息的字符串指针。如果操作失败，返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 读取表详细结构信息
[](#cb2-22)            string tableName = "MyTable";
[](#cb2-23)            long tableInfoDetailPtr = OLAServer.GetTableInfoDetail(db, tableName);
[](#cb2-24)            if (tableInfoDetailPtr != 0)
[](#cb2-25)            {
[](#cb2-26)                string tableInfoDetail = Marshal.PtrToStringAnsi(new IntPtr(tableInfoDetailPtr));
[](#cb2-27)                Console.WriteLine($"表 {tableName} 的详细结构信息:");
[](#cb2-28)                Console.WriteLine(tableInfoDetail);
[](#cb2-29)            }
[](#cb2-30)            else
[](#cb2-31)            {
[](#cb2-32)                Console.WriteLine($"读取表 {tableName} 的详细结构信息失败。");
[](#cb2-33)            }
[](#cb2-34)        }
[](#cb2-35)    }
[](#cb2-36)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 读取表详细结构信息
[](#cb3-14)tableName = "MyTable"
[](#cb3-15)tableInfoDetailPtr = OLAServer.GetTableInfoDetail(db, tableName)
[](#cb3-16)if tableInfoDetailPtr != 0:
[](#cb3-17)    tableInfoDetail = ctypes.cast(tableInfoDetailPtr, ctypes.c_char_p).value.decode('utf-8')
[](#cb3-18)    print(f"表 {tableName} 的详细结构信息:")
[](#cb3-19)    print(tableInfoDetail)
[](#cb3-20)else:
[](#cb3-21)    print(f"读取表 {tableName} 的详细结构信息失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 读取表详细结构信息
[](#cb4-33)tableName = "MyTable"
[](#cb4-34)olaplug_dll.GetTableInfoDetail.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-35)olaplug_dll.GetTableInfoDetail.restype = c_void_p
[](#cb4-36)tableInfoDetailPtr = olaplug_dll.GetTableInfoDetail(ola_obj, db, tableName.encode('utf-8'))
[](#cb4-37)if tableInfoDetailPtr != 0:
[](#cb4-38)    tableInfoDetail = ctypes.cast(tableInfoDetailPtr, ctypes.c_char_p).value.decode('utf-8')
[](#cb4-39)    print(f"表 {tableName} 的详细结构信息:")
[](#cb4-40)    print(tableInfoDetail)
[](#cb4-41)else:
[](#cb4-42)    print(f"读取表 {tableName} 的详细结构信息失败。")
```

## 注意事项

- 返回的表详细结构信息通常是一个字符串，可能包含列名、列类型、列长度、是否为主键、是否为外键、默认值等详细信息，具体格式取决于数据库的实现。

- 如果表不存在或操作失败，函数将返回 `0`。

- 使用完返回的字符串指针后，应妥善处理内存，避免内存泄漏。

---

# 读取错误信息 -
GetDatabaseError

## 函数简介

读取数据库操作中的错误信息，返回错误信息的字符串指针。

## 函数原型

```
[](#cb1-1)long GetDatabaseError(long ola, const long db);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

## 返回值

- 返回值：错误信息的字符串指针。如果操作失败或没有错误信息，返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 读取错误信息
[](#cb2-22)            long errorPtr = OLAServer.GetDatabaseError(db);
[](#cb2-23)            if (errorPtr != 0)
[](#cb2-24)            {
[](#cb2-25)                string errorMessage = Marshal.PtrToStringAnsi(new IntPtr(errorPtr));
[](#cb2-26)                Console.WriteLine($"数据库错误信息: {errorMessage}");
[](#cb2-27)            }
[](#cb2-28)            else
[](#cb2-29)            {
[](#cb2-30)                Console.WriteLine("没有错误信息。");
[](#cb2-31)            }
[](#cb2-32)        }
[](#cb2-33)    }
[](#cb2-34)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 读取错误信息
[](#cb3-14)errorPtr = OLAServer.GetDatabaseError(db)
[](#cb3-15)if errorPtr != 0:
[](#cb3-16)    errorMessage = ctypes.cast(errorPtr, ctypes.c_char_p).value.decode('utf-8')
[](#cb3-17)    print(f"数据库错误信息: {errorMessage}")
[](#cb3-18)else:
[](#cb3-19)    print("没有错误信息。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 读取错误信息
[](#cb4-33)olaplug_dll.GetDatabaseError.argtypes = [c_void_p, c_void_p]
[](#cb4-34)olaplug_dll.GetDatabaseError.restype = c_void_p
[](#cb4-35)errorPtr = olaplug_dll.GetDatabaseError(ola_obj, db)
[](#cb4-36)if errorPtr != 0:
[](#cb4-37)    errorMessage = ctypes.cast(errorPtr, ctypes.c_char_p).value.decode('utf-8')
[](#cb4-38)    print(f"数据库错误信息: {errorMessage}")
[](#cb4-39)else:
[](#cb4-40)    print("没有错误信息。")
```

## 注意事项

- 如果数据库操作没有发生错误，`GetDatabaseError` 将返回
`0`。

- 返回的错误信息字符串指针在使用完毕后应妥善处理，避免内存泄漏。

---

# 销毁STMT对象 - Finalize

## 函数简介

销毁STMT（Statement）对象，释放相关资源。在读取完数据后必须调用此函数，以避免内存泄漏。

## 函数原型

```
[](#cb1-1)int Finalize(long ola, long stmt);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `stmt` (长整型数): 数据库语句对象指针，由 [ExecuteReader](/数据库/读取结果集%20-%20ExecuteReader.html)
接口返回。

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```
[](#cb2-1)using System;
[](#cb2-2)using OLA.ServiceCenter.PlugFactory;
[](#cb2-3)
[](#cb2-4)namespace OLADemo
[](#cb2-5){
[](#cb2-6)    internal class Program
[](#cb2-7)    {
[](#cb2-8)        static OLAPlugServer OLAServer;
[](#cb2-9)        static void Main(string[] args)
[](#cb2-10)        {
[](#cb2-11)            OLAServer = new OLAPlugServer();
[](#cb2-12)            var regResult = OLAServer.Reg(
[](#cb2-13)                OLAServer.UserCode,
[](#cb2-14)                OLAServer.SoftCode,
[](#cb2-15)                OLAServer.FeatureList
[](#cb2-16)            );
[](#cb2-17)            OLAServer.CreateCOLAPlugInterFace();
[](#cb2-18)            long db = OLAServer.OpenDatabase("OLAPlugDemo.db", "olaplug");
[](#cb2-19)            Console.WriteLine($"OpenDatabase 返回:{db}");
[](#cb2-20)
[](#cb2-21)            // 执行查询并返回STMT指针
[](#cb2-22)            string sql = "SELECT * FROM MyTable";
[](#cb2-23)            long stmtPtr = OLAServer.ExecuteReader(db, sql);
[](#cb2-24)            if (stmtPtr != 0)
[](#cb2-25)            {
[](#cb2-26)                Console.WriteLine("查询成功，STMT指针已返回。");
[](#cb2-27)
[](#cb2-28)                // 读取数据（假设有一个读取数据的函数）
[](#cb2-29)                // OLAServer.Read(stmtPtr);
[](#cb2-30)
[](#cb2-31)                // 销毁STMT对象
[](#cb2-32)                int result = OLAServer.Finalize(stmtPtr);
[](#cb2-33)                if (result == 1)
[](#cb2-34)                {
[](#cb2-35)                    Console.WriteLine("STMT对象销毁成功。");
[](#cb2-36)                }
[](#cb2-37)                else
[](#cb2-38)                {
[](#cb2-39)                    Console.WriteLine("STMT对象销毁失败。");
[](#cb2-40)                }
[](#cb2-41)            }
[](#cb2-42)            else
[](#cb2-43)            {
[](#cb2-44)                Console.WriteLine("查询失败。");
[](#cb2-45)            }
[](#cb2-46)        }
[](#cb2-47)    }
[](#cb2-48)}
```

@tab Python

```
[](#cb3-1)from OLAPlugServer import OLAPlugServer
[](#cb3-2)
[](#cb3-3)# 实例化
[](#cb3-4)OLAServer = OLAPlugServer()
[](#cb3-5)# 注册
[](#cb3-6)OLAServer.Reg(OLAServer.UserCode, OLAServer.SoftCode, OLAServer.FeatureList)
[](#cb3-7)# 创建OLAPlug对象
[](#cb3-8)OLAServer.CreateCOLAPlugInterFace()
[](#cb3-9)# 打开数据库
[](#cb3-10)db = OLAServer.OpenDatabase('OLAPlug.db', 'OLAPlug')
[](#cb3-11)print(f"openDatabaseResult={db}")
[](#cb3-12)
[](#cb3-13)# 执行查询并返回STMT指针
[](#cb3-14)sql = "SELECT * FROM MyTable"
[](#cb3-15)stmtPtr = OLAServer.ExecuteReader(db, sql)
[](#cb3-16)if stmtPtr != 0:
[](#cb3-17)    print("查询成功，STMT指针已返回。")
[](#cb3-18)
[](#cb3-19)    # 读取数据（假设有一个读取数据的函数）
[](#cb3-20)    # OLAServer.Read(stmtPtr)
[](#cb3-21)
[](#cb3-22)    # 销毁STMT对象
[](#cb3-23)    result = OLAServer.Finalize(stmtPtr)
[](#cb3-24)    if result == 1:
[](#cb3-25)        print("STMT对象销毁成功。")
[](#cb3-26)    else:
[](#cb3-27)        print("STMT对象销毁失败。")
[](#cb3-28)else:
[](#cb3-29)    print("查询失败。")
```

### 原生方式

@tab Python

```
[](#cb4-1)import os
[](#cb4-2)import sys
[](#cb4-3)from ctypes import *
[](#cb4-4)
[](#cb4-5)# 1. 加载dll
[](#cb4-6)# 此处路径为插件所在路径，请根据实际情况修改。
[](#cb4-7)# 32位python使用x86版本，64位python使用x64版本
[](#cb4-8)if sys.maxsize > 2**32:
[](#cb4-9)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x64.dll')))
[](#cb4-10)else:
[](#cb4-11)    olaplug_dll = WinDLL(os.path.abspath(os.path.join(os.getcwd(), 'OLAPlug_x86.dll')))
[](#cb4-12)
[](#cb4-13)# 2. 注册到后台
[](#cb4-14)UserCode = "c38e200f116d4fa8bd0deb45ccb523ea"
[](#cb4-15)SoftCode = "701bc92ba84642c68845e7a06c10fd99"
[](#cb4-16)FeatureList = "OLA|OLAPlus"
[](#cb4-17)olaplug_dll.Reg.argtypes = [c_char_p, c_char_p, c_char_p]
[](#cb4-18)olaplug_dll.Reg.restype = c_int32
[](#cb4-19)result = olaplug_dll.Reg(UserCode.encode('utf-8'), SoftCode.encode('utf-8'), FeatureList.encode('utf-8'))
[](#cb4-20)print(f'注册结果返回: {result}')
[](#cb4-21)
[](#cb4-22)# 3. 创建ola对象
[](#cb4-23)olaplug_dll.CreateCOLAPlugInterFace.restype = c_void_p
[](#cb4-24)ola_obj = olaplug_dll.CreateCOLAPlugInterFace()
[](#cb4-25)
[](#cb4-26)# 4. 打开数据库
[](#cb4-27)olaplug_dll.OpenDatabase.argtypes = [c_void_p, c_char_p, c_char_p]
[](#cb4-28)olaplug_dll.OpenDatabase.restype = c_void_p
[](#cb4-29)db = olaplug_dll.OpenDatabase(ola_obj, "OLAPlugDemo.db".encode('utf-8'), "olaplug".encode('utf-8'))
[](#cb4-30)print(f"openDatabaseResult={db}")
[](#cb4-31)
[](#cb4-32)# 5. 执行查询并返回STMT指针
[](#cb4-33)sql = "SELECT * FROM MyTable"
[](#cb4-34)olaplug_dll.ExecuteReader.argtypes = [c_void_p, c_void_p, c_char_p]
[](#cb4-35)olaplug_dll.ExecuteReader.restype = c_void_p
[](#cb4-36)stmtPtr = olaplug_dll.ExecuteReader(ola_obj, db, sql.encode('utf-8'))
[](#cb4-37)if stmtPtr != 0:
[](#cb4-38)    print("查询成功，STMT指针已返回。")
[](#cb4-39)
[](#cb4-40)    # 读取数据（假设有一个读取数据的函数）
[](#cb4-41)    # olaplug_dll.Read(stmtPtr)
[](#cb4-42)
[](#cb4-43)    # 销毁STMT对象
[](#cb4-44)    olaplug_dll.Finalize.argtypes = [c_void_p, c_void_p]
[](#cb4-45)    olaplug_dll.Finalize.restype = c_int32
[](#cb4-46)    result = olaplug_dll.Finalize(ola_obj, stmtPtr)
[](#cb4-47)    if result == 1:
[](#cb4-48)        print("STMT对象销毁成功。")
[](#cb4-49)    else:
[](#cb4-50)        print("STMT对象销毁失败。")
[](#cb4-51)else:
[](#cb4-52)    print("查询失败。")
```

## 注意事项

- 该函数用于销毁STMT对象并释放相关资源，通常在读取完数据后调用，以避免内存泄漏。

- 如果操作失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保在不再使用STMT对象时调用此函数，否则可能导致资源泄漏。

---

## 文件



---

# 写入字节到文件 -
WriteBytesToFile

### 函数简介

将内存中的字节流数据写入到指定文件,支持二进制数据写入。

### 接口名称

```
WriteBytesToFile
```

### DLL调用

```
[](#cb2-1)int32_t WriteBytesToFile(int64_t instance, const char* filePath, int64_t dataAddr, int32_t dataSize)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `filePath` (字符串): 目标文件的完整路径

- `dataAddr` (长整型数):
要写入的数据在内存中的起始地址

- `dataSize` (整型数): 要写入的数据大小(字节)

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 准备要写入的数据
[](#cb3-5)unsigned char data[] = {0x4D, 0x5A, 0x90, 0x00, 0x03, 0x00, 0x00, 0x00};
[](#cb3-6)int32_t dataSize = sizeof(data);
[](#cb3-7)
[](#cb3-8)// 写入字节到文件
[](#cb3-9)int32_t result = WriteBytesToFile(
[](#cb3-10)    instance,
[](#cb3-11)    "C:\\Output\\binary_data.bin",
[](#cb3-12)    (int64_t)data,
[](#cb3-13)    dataSize
[](#cb3-14));
[](#cb3-15)
[](#cb3-16)if (result == 1) {
[](#cb3-17)    printf("成功写入字节到文件\n");
[](#cb3-18)} else {
[](#cb3-19)    printf("写入失败\n");
[](#cb3-20)}
[](#cb3-21)
[](#cb3-22)// 释放资源
[](#cb3-23)DestroyCOLAPlugInterFace(instance);
```

#### 高级示例 - 写入图片数据:

```
[](#cb4-1)// 从截图获取图片数据
[](#cb4-2)int64_t imagePtr = GetScreenDataPtr(instance, 0, 0, 800, 600);
[](#cb4-3)
[](#cb4-4)if (imagePtr != 0) {
[](#cb4-5)    // 获取图片BMP字节流
[](#cb4-6)    int64_t bmpDataPtr = GetImageBmpData(instance, imagePtr);
[](#cb4-7)
[](#cb4-8)    if (bmpDataPtr != 0) {
[](#cb4-9)        // 获取数据大小
[](#cb4-10)        int32_t dataSize = GetStringSize(instance, bmpDataPtr);
[](#cb4-11)
[](#cb4-12)        // 写入到文件
[](#cb4-13)        int32_t result = WriteBytesToFile(
[](#cb4-14)            instance,
[](#cb4-15)            "C:\\Screenshots\\screen.bmp",
[](#cb4-16)            bmpDataPtr,
[](#cb4-17)            dataSize
[](#cb4-18)        );
[](#cb4-19)
[](#cb4-20)        // 释放内存
[](#cb4-21)        FreeMemoryPtr(instance, bmpDataPtr);
[](#cb4-22)    }
[](#cb4-23)
[](#cb4-24)    FreeImagePtr(instance, imagePtr);
[](#cb4-25)}
```

#### 追加写入示例:

```
[](#cb5-1)// 先读取现有文件内容
[](#cb5-2)int64_t existingDataPtr = ReadBytesFromFile(instance, "C:\\Data\\log.bin");
[](#cb5-3)
[](#cb5-4)if (existingDataPtr != 0) {
[](#cb5-5)    int32_t existingSize = GetStringSize(instance, existingDataPtr);
[](#cb5-6)
[](#cb5-7)    // 准备新数据
[](#cb5-8)    unsigned char newData[] = {0x01, 0x02, 0x03, 0x04};
[](#cb5-9)    int32_t newSize = sizeof(newData);
[](#cb5-10)
[](#cb5-11)    // 合并数据
[](#cb5-12)    unsigned char* combined = (unsigned char*)malloc(existingSize + newSize);
[](#cb5-13)    memcpy(combined, (void*)existingDataPtr, existingSize);
[](#cb5-14)    memcpy(combined + existingSize, newData, newSize);
[](#cb5-15)
[](#cb5-16)    // 写入合并后的数据
[](#cb5-17)    WriteBytesToFile(instance, "C:\\Data\\log.bin", (int64_t)combined, existingSize + newSize);
[](#cb5-18)
[](#cb5-19)    free(combined);
[](#cb5-20)    FreeMemoryPtr(instance, existingDataPtr);
[](#cb5-21)}
```

### 返回值

整型数: - 1: 成功 - 0: 失败

### 注意事项

- 如果文件已存在,将覆盖原有内容

- 如果目录不存在,写入会失败

- 确保有足够的磁盘空间

- 确保对目标路径有写入权限

- dataAddr必须指向有效的内存地址

- dataSize必须与实际数据大小一致,否则可能写入错误数据

- 支持写入任意二进制数据,包括可执行文件、图片、音频等

- 写入大文件时注意性能影响

- 建议在写入前检查文件路径的有效性

- 使用绝对路径可以避免路径解析问题

- 写入系统目录可能需要管理员权限

---

# 创建文件 - CreateFile

## 函数简介

- 在指定路径创建一个新的空文件。

## 接口名称

```
CreateFile
```

## DLL调用

```
int CreateFile(long instance, string path)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
path |
字符串 |
要创建的文件完整路径。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

操作结果，0 失败，1 成功。

## 注意事项

- 若文件已存在，具体行为取决于底层实现（可能覆盖或失败）。

---

# 创建文件夹 - CreateFolder

## 函数简介

- 在指定路径创建一个新的文件夹。

## 接口名称

```
CreateFolder
```

## DLL调用

```
int CreateFolder(long instance, string path)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
path |
字符串 |
要创建的文件夹完整路径。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

操作结果，0 失败，1 成功。

## 注意事项

- 若目标文件夹已存在，具体行为取决于底层实现（可能返回失败）。

---

# 删除文件 - DeleteFile

## 函数简介

- 删除指定路径的文件。

## 接口名称

```
DeleteFile
```

## DLL调用

```
int DeleteFile(long instance, string path)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
path |
字符串 |
要删除的文件完整路径。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

操作结果，0 失败，1 成功。

## 注意事项

- 若文件正在被占用，可能删除失败。

---

# 删除文件夹 - DeleteFolder

## 函数简介

- 删除指定路径的文件夹。

## 接口名称

```
DeleteFolder
```

## DLL调用

```
int DeleteFolder(long instance, string path)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
path |
字符串 |
要删除的文件夹完整路径。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

操作结果，0 失败，1 成功。

## 注意事项

- 若文件夹非空，删除行为取决于底层实现（可能删除失败）。

---

# 判断文件夹是否存在 -
IsDirectory

## 函数简介

- 判断指定路径的文件夹是否存在。

## 接口名称

```
IsDirectory
```

## DLL调用

```
int IsDirectory(long instance, string path)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
path |
字符串 |
要判断的文件夹路径。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

是否存在，0 不存在或失败，非0 表示存在。

## 注意事项

- 路径无效时返回0。

---

# 判断文件或目录是否存在
- FileOrDirectoryExists

## 函数简介

- 判断指定路径的文件或目录是否存在。

## 接口名称

```
FileOrDirectoryExists
```

## DLL调用

```
int FileOrDirectoryExists(long instance, string path)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
path |
字符串 |
要判断的文件或目录路径。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

是否存在，0 不存在或失败，非0 表示存在。

## 注意事项

- 路径无效或没有访问权限时返回0。

---

# 判断文件是否存在 - IsFile

## 函数简介

- 判断指定路径的文件是否存在。

## 接口名称

```
IsFile
```

## DLL调用

```
int IsFile(long instance, string path)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
path |
字符串 |
要判断的文件路径。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

是否存在，0 不存在或失败，非0 表示存在。

## 注意事项

- 路径无效时返回0。

---

# 复制文件 - CopyFile

## 函数简介

- 将源文件复制到目标路径。

## 接口名称

```
CopyFile
```

## DLL调用

```
int CopyFile(long instance, string src, string dst)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
src |
字符串 |
源文件完整路径。 |
|

|
dst |
字符串 |
目标文件完整路径。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

操作结果，0 失败，1 成功。

## 注意事项

- 若目标文件已存在，覆盖与否取决于底层实现。

---

# 移动文件 - MoveFile

## 函数简介

- 将源文件移动到目标路径，相当于剪切操作。

## 接口名称

```
MoveFile
```

## DLL调用

```
int MoveFile(long instance, string src, string dst)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
src |
字符串 |
源文件完整路径。 |
|

|
dst |
字符串 |
目标文件完整路径。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

操作结果，0 失败，1 成功。

## 注意事项

- 跨盘移动时可能表现为复制+删除，视底层实现而定。

---

# 获取文件列表 - GetFileList

## 函数简介

- 获取指定文件夹下的文件列表，可按基础目录返回相对路径。

## 接口名称

```
GetFileList
```

## DLL调用

```
long GetFileList(long instance, string path, string baseDir)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
path |
字符串 |
要枚举的文件夹路径。 |
|

|
baseDir |
字符串 |
基础目录，不为空时返回相对于该目录的路径；为空时返回绝对路径。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回文件列表字符串的指针，失败返回0。

## 注意事项

- 返回的字符串指针需调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

# 获取文件名 - GetFileName

## 函数简介

- 获取指定路径的文件名，可选择是否包含扩展名。

## 接口名称

```
GetFileName
```

## DLL调用

```
long GetFileName(long instance, string path, int withExtension)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
path |
字符串 |
文件完整路径。 |
|

|
withExtension |
整数型 |
是否包含扩展名，0 不包含，非0 包含。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回文件名字符串的指针，失败返回0。

## 注意事项

- 返回的字符串指针需调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

# 获取文件大小 - GetFileSize

## 函数简介

- 获取指定文件的大小（字节数）。

## 接口名称

```
GetFileSize
```

## DLL调用

```
long GetFileSize(long instance, string path)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
path |
字符串 |
要获取大小的文件完整路径。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

文件大小（字节），失败返回0。

## 注意事项

- 当文件不存在或路径无效时返回0。

---

# 获取文件夹列表 -
GetFolderList

## 函数简介

- 获取指定路径下的文件夹列表，可按基础目录返回相对路径。

## 接口名称

```
GetFolderList
```

## DLL调用

```
long GetFolderList(long instance, string path, string baseDir)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
path |
字符串 |
要枚举的文件夹路径。 |
|

|
baseDir |
字符串 |
基础目录，不为空时返回相对于该目录的路径；为空时返回绝对路径。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回文件夹列表字符串的指针，失败返回0。

## 注意事项

- 返回的字符串指针需调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

# 读取文件字符串 -
ReadFileString

## 函数简介

- 按指定编码读取文件内容，并以字符串形式返回。

## 接口名称

```
ReadFileString
```

## DLL调用

```
long ReadFileString(long instance, string filePath, int encoding)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
filePath |
字符串 |
要读取的文件完整路径。 |
|

|
encoding |
整数型 |
字符编码方式：-1 自动检测；0 GBK；1 Unicode；2 UTF-8；3
UTF-8(BOM自动去除)。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回文件内容字符串的指针，失败返回0。

## 注意事项

- 返回的字符串指针需调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

# 读取文件字节 -
ReadBytesFromFile

## 函数简介

- 从文件中读取指定偏移量和大小的字节数据。

## 接口名称

```
ReadBytesFromFile
```

## DLL调用

```
long ReadBytesFromFile(long instance, string filePath, int offset, long size)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
filePath |
字符串 |
要读取的文件完整路径。 |
|

|
offset |
整数型 |
起始偏移量（字节）。 |
|

|
size |
长整数型 |
读取的字节数，0 表示读取整个文件。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回字节缓冲区指针，失败返回0。

## 注意事项

- 返回的缓冲区指针需调用 [FreeMemoryPtr](/其他/释放字节流内存%20-%20FreeMemoryPtr.html)
接口释放内存。

---

# 转为相对路径 -
ToRelativePath

## 函数简介

- 将给定路径转换为相对路径。

## 接口名称

```
ToRelativePath
```

## DLL调用

```
long ToRelativePath(long instance, string path)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
path |
字符串 |
要转换的路径（绝对路径）。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回相对路径字符串的指针，失败返回0。

## 注意事项

- 返回的字符串指针需调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

# 转为绝对路径 -
ToAbsolutePath

## 函数简介

- 将给定路径转换为绝对路径。

## 接口名称

```
ToAbsolutePath
```

## DLL调用

```
long ToAbsolutePath(long instance, string path)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
path |
字符串 |
要转换的路径（相对或绝对路径）。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回绝对路径字符串的指针，失败返回0。

## 注意事项

- 返回的字符串指针需调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存。

---

# 重命名文件 - RenameFile

## 函数简介

- 重命名或移动指定文件。

## 接口名称

```
RenameFile
```

## DLL调用

```
int RenameFile(long instance, string src, string dst)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
src |
字符串 |
原文件完整路径。 |
|

|
dst |
字符串 |
新文件完整路径（可包含新的目录或文件名）。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

操作结果，0 失败，1 成功。

## 注意事项

- 若目标文件已存在，行为取决于底层实现（可能覆盖或失败）。

---

## 文字识别

# 从字库中识别文字 -
OcrFromDict

## 函数简介

- 从字库中识别文字。需提前加载数据库,参考接口SetConfig

- x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

- 支持多个字库同时识别适配字体变形等场景，多个字库用|分割
。如dict1|dict2

## 接口名称

```
OcrFromDict
```

## DLL调用

```
long OcrFromDict(long instance, int x1, int y1, int x2, int y2, string colorJson, string dict_name, double matchVal)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
x1 |
整数型 |
左上角x坐标 |
|

|
y1 |
整数型 |
左上角y坐标 |
|

|
x2 |
整数型 |
右下角x坐标 |
|

|
y2 |
整数型 |
右下角y坐标 |
|

|
colorJson |
字符串 |
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00` |
|

|
dict_name |
字符串 |
字库名称,为空时搜索所有字库 |
|

|
matchVal |
双精度浮点数 |
匹配值 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

识别到的文字(二进制字符串的指针)

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 从字库中识别文字 -
OcrFromDictDetails

## 函数简介

- 从字库中识别文字。需提前加载数据库,参考接口SetConfig

- x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客

- 支持多个字库同时识别适配字体变形等场景，多个字库用|分割
。如dict1|dict2

## 接口名称

```
OcrFromDictDetails
```

## DLL调用

```
long OcrFromDictDetails(long instance, int x1, int y1, int x2, int y2, string colorJson, string dict_name, double matchVal)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
x1 |
整数型 |
左上角x坐标 |
|

|
y1 |
整数型 |
左上角y坐标 |
|

|
x2 |
整数型 |
右下角x坐标 |
|

|
y2 |
整数型 |
右下角y坐标 |
|

|
colorJson |
字符串 |
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00` |
|

|
dict_name |
字符串 |
字库名称,为空时搜索所有字库 |
|

|
matchVal |
双精度浮点数 |
匹配值 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

字符串指针地址

返回识别到的字符串,如：

```
{
"Regions": [
{
"Score": 0,
"Text": "bbbbbb",
"Center": {
"x": 100,
"y": 200
},
"Vertices": [
{
"x": 75,
"y": 190
},
{
"x": 125,
"y": 190
},
{
"x": 125,
"y": 210
},
{
"x": 75,
"y": 210
}
],
"Angle": 0
}
],
"Text": "bbbbbb"
}
```

Regions集合为所有识别到的数据集 Score为识别评分,分值越高越准确,
Center为识别结果中心点 Size为识别范围 Angle为识别结果角度
Vertices为识别结果的4个顶点

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 从字库中识别文字 -
OcrFromDictPtr

## 函数简介

-
从字库中识别文字。需提前加载数据库,参考接口SetConfig

-
支持多个字库同时识别适配字体变形等场景，多个字库用|分割
。如dict1|dict2

## 接口名称

```
OcrFromDictPtr
```

## DLL调用

```
long OcrFromDictPtr(long instance, long ptr, string colorJson, string dict_name, double matchVal)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针 |
|

|
colorJson |
字符串 |
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00` |
|

|
dict_name |
字符串 |
字库名称,为空时搜索所有字库 |
|

|
matchVal |
双精度浮点数 |
匹配值 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

识别到的文字(二进制字符串的指针)

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 从字库中识别文字 -
OcrFromDictPtrDetails

## 函数简介

- 从字库中识别文字。需提前加载数据库,参考接口SetConfig

- 支持多个字库同时识别适配字体变形等场景，多个字库用|分割
。如dict1|dict2

## 接口名称

```
OcrFromDictPtrDetails
```

## DLL调用

```
long OcrFromDictPtrDetails(long instance, long ptr, string colorJson, string dict_name, double matchVal)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
ptr |
长整数型 |
图像指针 |
|

|
colorJson |
字符串 |
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00` |
|

|
dict_name |
字符串 |
字库名称,为空时搜索所有字库 |
|

|
matchVal |
双精度浮点数 |
匹配值 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

字符串:

返回识别到的字符串,如：

```
{
"Regions": [
{
"Score": 0,
"Text": "bbbbbb",
"Center": {
"x": 100,
"y": 200
},
"Vertices": [
{
"x": 75,
"y": 190
},
{
"x": 125,
"y": 190
},
{
"x": 125,
"y": 210
},
{
"x": 75,
"y": 210
}
],
"Angle": 0
}
],
"Text": "bbbbbb"
}
```

Regions集合为所有识别到的数据集 Score为识别评分,分值越高越准确,
Center为识别结果中心点 Size为识别范围 Angle为识别结果角度
Vertices为识别结果的4个顶点

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 加载字库图片 -
InitDictFromDir

## 函数简介

从指定目录中加载字库文件，并将其初始化到OLA数据库中。可以选择是否覆盖已存在的字库数据。

## 函数原型

```
[](#cb1-1)int InitDictFromDir(long ola, const long db, string dict_name, string dict_path, int cover);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `dict_name` (字符串): 字库名称。

- `dict_path` (字符串): 字库图片文件夹路径。

- `cover` (布尔值): 是否覆盖已存在的图像数据。

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```

```

@tab Python

```

```

### 原生方式

@tab Python

```

```

## 注意事项

- 该函数用于从指定目录中加载字库图片文件，并将其初始化到OLA数据库中。适用于批量导入字库的场景。

- `cover` 参数用于控制是否覆盖已存在的图像数据。设置为
`1` 时，会覆盖现有数据；设置为 `0`
时，会跳过已存在的图像。

- 如果初始化失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保目录路径正确，且图像文件格式受支持，否则可能导致初始化失败。

---

# 导出字库数据 - ExportDict

## 函数简介

将OLA数据库中的图像数据导出到指定目录。

## 函数原型

```
[](#cb1-1)int ExportDict(long ola, const long db, string dict_name, string exportDir);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `dictName` (字符串): 字库名称。

- `exportPath` (字符串): 导出路径。

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```

```

@tab Python

```

```

### 原生方式

@tab Python

```

```

## 注意事项

- 该函数用于将OLA数据库中的图像数据导出到指定目录，适用于批量导出字库图像数据的场景。

- 如果导出失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保目录路径正确，且图像数据存在于数据库中，否则可能导致导出失败。

- 导出的图像文件将保存在 `exportDir`
指定的目录中，确保目标目录有足够的存储空间。

---

# 快速识别数字 - FastNumberOcr

### 函数简介

快速识别指定窗口区域内的数字，使用预定义的数字图片模板进行匹配识别。

### 接口名称

```
FastNumberOcr
```

### DLL调用

```
int32_t FastNumberOcr(int64_t instance, int32_t x1, int32_t y1, int32_t x2, int32_t y2, const char* numbers, const char* colorJson, double matchVal)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 区域左上角X坐标。

- `y1` (整型数): 区域左上角Y坐标。

- `x2` (整型数): 区域右下角X坐标。

- `y2` (整型数): 区域右下角Y坐标。

- `numbers` (字符串):
0~9数字图片地址，多个数字用|分割，如img/0.png|img/1.png|img/2.png|img/3.png|img/4.png|img/5.png|img/6.png|img/7.png|img/8.png|img/9.png

- `colorJson` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `matchVal` (双精度浮点数): 识别率阈值，范围0.0-1.0。

#### 示例:

```
[](#cb3-1)// 快速识别指定区域数字示例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 绑定窗口
[](#cb3-5)BindWindow(instance, "记事本", "normal", "normal", "", 0);
[](#cb3-6)
[](#cb3-7)// 设置数字图片路径
[](#cb3-8)const char* numbers = "img/0.png|img/1.png|img/2.png|img/3.png|img/4.png|img/5.png|img/6.png|img/7.png|img/8.png|img/9.png";
[](#cb3-9)
[](#cb3-10)// 设置颜色JSON配置
[](#cb3-11)const char* colorJson = "[{\"StartColor\": \"3278FA\", \"EndColor\": \"6496FF\", \"Type\": 0}, {\"StartColor\": \"3278FA\", \"EndColor\": \"6496FF\", \"Type\": 1}]";
[](#cb3-12)
[](#cb3-13)// 执行数字识别，识别区域(100,100,200,150)
[](#cb3-14)double matchVal = 0.8;
[](#cb3-15)int32_t result = FastNumberOcr(instance, 100, 100, 200, 150, numbers, colorJson, matchVal);
[](#cb3-16)
[](#cb3-17)if (result >= 0) {
[](#cb3-18)    printf("识别到的数字: %d\n", result);
[](#cb3-19)} else {
[](#cb3-20)    printf("识别失败\n");
[](#cb3-21)}
[](#cb3-22)
[](#cb3-23)// 释放资源
[](#cb3-24)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数:

- 返回识别到的数字

- 如果识别失败返回-1

### 注意事项

- 需要预先准备0-9数字的二值化图片模板

- 数字图片路径用|符号分隔

- colorJson参数用于指定识别区域的颜色范围，提高识别准确性

- matchVal参数控制识别精度，值越高要求匹配度越精确

- 使用前需要先绑定窗口

- 坐标范围为窗口客户区坐标

- 建议在识别前对图片进行预处理，提高识别成功率

---

# 快速识别数字 -
FastNumberOcrFromPtr

### 函数简介

快速识别图片中的数字，使用预定义的数字图片模板进行匹配识别。

### 接口名称

```
FastNumberOcrFromPtr
```

### DLL调用

```
int32_t FastNumberOcrFromPtr(int64_t instance, int64_t source, const char* numbers, const char* colorJson, double matchVal)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `source` (长整型数): 源图片对象的指针。

- `numbers` (字符串):
0~9数字图片地址，多个数字用|分割，如img/0.png|img/1.png|img/2.png|img/3.png|img/4.png|img/5.png|img/6.png|img/7.png|img/8.png|img/9.png

- `colorJson` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `matchVal` (双精度浮点数): 识别率阈值，范围0.0-1.0。

#### 示例:

```
[](#cb3-1)// 快速识别数字示例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)int64_t source = CreateImage("screenshot.png");
[](#cb3-4)
[](#cb3-5)// 设置数字图片路径
[](#cb3-6)const char* numbers = "img/0.png|img/1.png|img/2.png|img/3.png|img/4.png|img/5.png|img/6.png|img/7.png|img/8.png|img/9.png";
[](#cb3-7)
[](#cb3-8)// 设置颜色JSON配置
[](#cb3-9)const char* colorJson = "[{\"StartColor\": \"3278FA\", \"EndColor\": \"6496FF\", \"Type\": 0}, {\"StartColor\": \"3278FA\", \"EndColor\": \"6496FF\", \"Type\": 1}]";
[](#cb3-10)
[](#cb3-11)// 执行数字识别
[](#cb3-12)double matchVal = 0.8;
[](#cb3-13)int32_t result = FastNumberOcrFromPtr(instance, source, numbers, colorJson, matchVal);
[](#cb3-14)
[](#cb3-15)if (result >= 0) {
[](#cb3-16)    printf("识别到的数字: %d\n", result);
[](#cb3-17)} else {
[](#cb3-18)    printf("识别失败\n");
[](#cb3-19)}
[](#cb3-20)
[](#cb3-21)// 释放资源
[](#cb3-22)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数:

- 返回识别到的数字

- 如果识别失败返回-1

### 注意事项

- 需要预先准备0-9数字的二值化图片模板

- 数字图片路径用|符号分隔

- colorJson参数用于指定识别区域的颜色范围，提高识别准确性

- matchVal参数控制识别精度，值越高要求匹配度越精确

- 建议在识别前对图片进行预处理，提高识别成功率

---

# 指定bmp图片识字 -
OcrFromBmpData

### 函数简介

指定bmp图片文字识别

### 接口名称

```
OcrFromBmpData
```

### DLL调用

```
long OcrFromBmpData(long ola, long imgPtr, int size)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `imgPtr` (长整型数): bmp图片数据流地址

- `size` (整型数): 图片大小

#### 示例:

待补充…

### 返回值

字符串:

返回识别到的字符串

**注意:**

**字体比较特殊或者背景复杂识别不准确的,建议用图像识别来处理.**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 指定bmp图片详细信息
- OcrFromBmpDataDetails

### 函数简介

识别bmp格式图片的文字

### 接口名称

```
OcrFromBmpDataDetails
```

### DLL调用

```
long OcrFromBmpDataDetails(long ola, long imgPtr, int size)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `imgPtr` (长整型数): bmp图片数据流地址。

- `size` (整型数): 图片大小。

#### 示例:

待补充…

### 返回值

字符串:

返回识别到的字符串，如：

```
{
"Regions": [
{
"Score": 0,
"Text": "bbbbbb",
"Center": {
"x": 100,
"y": 200
},
"Vertices": [
{
"x": 75,
"y": 190
},
{
"x": 125,
"y": 190
},
{
"x": 125,
"y": 210
},
{
"x": 75,
"y": 210
}
],
"Angle": 0
}
],
"Text": "bbbbbb"
}
```

Regions集合为所有识别到的数据集 Score为识别评分,分值越高越准确,
Center为识别结果中心点 Size为识别范围 Angle为识别结果角度
Vertices为识别结果的4个顶点

**注意:**

**字体比较特殊或者背景复杂识别不准确的,建议用图像识别来处理.**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 指定区域识字 - Ocr

### 函数简介

识别窗口范围(x1,y1,x2,y2)内的文字

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

### 接口名称

```
Ocr
```

### DLL调用

```
long Ocr(long ola, int x1,int y1,int x2,int y2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 区域左上角X坐标。

- `y1` (整型数): 区域左上角Y坐标。

- `x2` (整型数): 区域右下角X坐标。

- `y2` (整型数): 区域右下角Y坐标。

#### 示例:

待补充…

### 返回值

字符串:

返回识别到的字符串

**注意:**

**字体比较特殊或者背景复杂识别不准确的,建议用图像识别来处理.**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 指定区域识字 - OcrV5

### 函数简介

-
识别窗口范围(x1,y1,x2,y2)内的文字

-
x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

-
使用ppocrV5模型,支持自定义模型

### 接口名称

```
OcrV5
```

### DLL调用

```
long OcrV5(long ola, int x1,int y1,int x2,int y2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 区域左上角X坐标。

- `y1` (整型数): 区域左上角Y坐标。

- `x2` (整型数): 区域右下角X坐标。

- `y2` (整型数): 区域右下角Y坐标。

#### 示例:

待补充…

### 返回值

字符串:

返回识别到的字符串

**注意:**

**字体比较特殊或者背景复杂识别不准确的,建议用图像识别来处理.**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 指定区域详细信息- OcrDetails

### 函数简介

识别屏幕范围(x1,y1,x2,y2)内的文字

x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

返回数据为相对窗口坐标

### 接口名称

```
OcrDetails
```

### DLL调用

```
long OcrDetails(long ola, int x1,int y1,int x2,int y2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 区域左上角X坐标。

- `y1` (整型数): 区域左上角Y坐标。

- `x2` (整型数): 区域右下角X坐标。

- `y2` (整型数): 区域右下角Y坐标。

#### 示例:

待补充…

### 返回值

字符串:

返回识别到的字符串,如：

```
{
"Regions": [
{
"Score": 0,
"Text": "bbbbbb",
"Center": {
"x": 100,
"y": 200
},
"Vertices": [
{
"x": 75,
"y": 190
},
{
"x": 125,
"y": 190
},
{
"x": 125,
"y": 210
},
{
"x": 75,
"y": 210
}
],
"Angle": 0
}
],
"Text": "bbbbbb"
}
```

Regions集合为所有识别到的数据集 Score为识别评分,分值越高越准确,
Center为识别结果中心点 Size为识别范围 Angle为识别结果角度
Vertices为识别结果的4个顶点

**注意:**

**字体比较特殊或者背景复杂识别不准确的,建议用图像识别来处理.**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 指定区域详细信息-
OcrV5Details

### 函数简介

-
识别屏幕范围(x1,y1,x2,y2)内的文字

-
x1 , y1, x2, y2传 0, 0, 0, 0 为窗口整个客户区

-
返回数据为相对窗口坐标

-
使用ppocrV5模型,支持自定义模型

### 接口名称

```
OcrV5Details
```

### DLL调用

```
long OcrV5Details(long ola, int x1,int y1,int x2,int y2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 区域左上角X坐标。

- `y1` (整型数): 区域左上角Y坐标。

- `x2` (整型数): 区域右下角X坐标。

- `y2` (整型数): 区域右下角Y坐标。

#### 示例:

待补充…

### 返回值

字符串:

返回识别到的字符串,如：

```
{
"Regions": [
{
"Score": 0,
"Text": "bbbbbb",
"Center": {
"x": 100,
"y": 200
},
"Vertices": [
{
"x": 75,
"y": 190
},
{
"x": 125,
"y": 190
},
{
"x": 125,
"y": 210
},
{
"x": 75,
"y": 210
}
],
"Angle": 0
}
],
"Text": "bbbbbb"
}
```

Regions集合为所有识别到的数据集 Score为识别评分,分值越高越准确,
Center为识别结果中心点 Size为识别范围 Angle为识别结果角度
Vertices为识别结果的4个顶点

**注意:**

**字体比较特殊或者背景复杂识别不准确的,建议用图像识别来处理.**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 指定图片识字 - OcrFromPtr

### 函数简介

指定图片文字识别

### 接口名称

```
OcrFromPtr
```

### DLL调用

```
long OcrFromPtr(long ola, long imgPtr)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `source` (长整型数): 源图片对象的指针。

#### 示例:

待补充…

### 返回值

字符串:

返回识别到的字符串

**注意:**

**字体比较特殊或者背景复杂识别不准确的,建议用图像识别来处理.**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 指定图片识字 - OcrV5FromPtr

### 函数简介

指定图片文字识别,使用ppocrV5模型,支持自定义模型

### 接口名称

```
OcrV5FromPtr
```

### DLL调用

```
long OcrV5FromPtr(long ola, long imgPtr)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `source` (长整型数): 源图片对象的指针。

#### 示例:

待补充…

### 返回值

字符串:

返回识别到的字符串

**注意:**

**字体比较特殊或者背景复杂识别不准确的,建议用图像识别来处理.**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 指定图片详细信息 -
OcrFromPtrDetails

### 函数简介

指定图片的详细信息

### 接口名称

```
OcrFromPtrDetails
```

### DLL调用

```
long OcrFromPtrDetails(long ola, long imgPtr)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `imgPtr` (长整型数): 源图片对象的指针。

#### 示例:

待补充…

### 返回值

字符串:

返回识别到的字符串,如：

```
{
"Regions": [
{
"Score": 0,
"Text": "bbbbbb",
"Center": {
"x": 100,
"y": 200
},
"Vertices": [
{
"x": 75,
"y": 190
},
{
"x": 125,
"y": 190
},
{
"x": 125,
"y": 210
},
{
"x": 75,
"y": 210
}
],
"Angle": 0
}
],
"Text": "bbbbbb"
}
```

Regions集合为所有识别到的数据集 Score为识别评分,分值越高越准确,
Center为识别结果中心点 Size为识别范围 Angle为识别结果角度
Vertices为识别结果的4个顶点

**注意:**

**字体比较特殊或者背景复杂识别不准确的,建议用图像识别来处理.**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 指定图片详细信息 -
OcrV5FromPtrDetails

### 函数简介

指定图片的详细信息,使用ppocrV5模型,支持自定义模型

### 接口名称

```
OcrV5FromPtrDetails
```

### DLL调用

```
long OcrV5FromPtrDetails(long ola, long imgPtr)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `imgPtr` (长整型数): 源图片对象的指针。

#### 示例:

待补充…

### 返回值

字符串:

返回识别到的字符串,如：

```
{
"Regions": [
{
"Score": 0,
"Text": "bbbbbb",
"Center": {
"x": 100,
"y": 200
},
"Vertices": [
{
"x": 75,
"y": 190
},
{
"x": 125,
"y": 190
},
{
"x": 125,
"y": 210
},
{
"x": 75,
"y": 210
}
],
"Angle": 0
}
],
"Text": "bbbbbb"
}
```

Regions集合为所有识别到的数据集 Score为识别评分,分值越高越准确,
Center为识别结果中心点 Size为识别范围 Angle为识别结果角度
Vertices为识别结果的4个顶点

**注意:**

**字体比较特殊或者背景复杂识别不准确的,建议用图像识别来处理.**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 查找文字 - FindStr

## 函数简介

查找指定文字的坐标，返回相对绑定窗口坐标坐标，返回最优坐标。

## 函数原型

```
[](#cb1-1)int FindStr(long ola,int x1, int y1, int x2, int y2, string str, string colorList,  string dict, double matchVal, int* outX, int* outY);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 查找区域的左上角X坐标。

- `y1` (整型数): 查找区域的左上角Y坐标。

- `x2` (整型数): 查找区域的右下角X坐标。

- `y2` (整型数): 查找区域的右下角Y坐标。

- `str` (字符串): 要查找的文字。

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `dict` (字符串): 字库名称,为空时搜索所有字库

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1。

- `outX` (整型数指针): 输出参数，返回的X坐标。

- `outY` (整型数指针): 输出参数，返回的Y坐标。

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```

```

@tab Python

```

```

### 原生方式

@tab Python

```

```

---

# 查找文字 - FindStrDetail

## 函数简介

查找指定文字的坐标，默认返回最优结果，支持ShowMatchWindow弹窗显示结果

返回数据类型解析:

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

## 函数原型

```
[](#cb2-1)long FindStrDetail(long ola,int x1, int y1, int x2, int y2, string str, string colorList,string dict, double matchVal);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x1` (整型数): 查找区域的左上角X坐标。

- `y1` (整型数): 查找区域的左上角Y坐标。

- `x2` (整型数): 查找区域的右下角X坐标。

- `y2` (整型数): 查找区域的右下角Y坐标。

- `str` (字符串): 要查找的文字。

- `colorList` (字符串):
颜色模型配置字符串，用于限定图像匹配中的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00`

- `dict` (字符串): 字库名称,为空时搜索所有字库

- `matchVal` (双精度浮点数): 相似度，如0.85，最大为1。

## 返回值

字符串: 返回JSON格式的匹配结果，包含以下字段： -
`MatchVal` (双精度浮点数): 实际匹配的相似度值 -
`MatchState` (boolean): 是否匹配成功 - `Index`
(整型数): 多图匹配时的图片索引，从0开始 - `Angle`
(双精度浮点数): 匹配到的图像旋转角度 - `X`: 匹配点X坐标 -
`Y`: 匹配点Y坐标 - `Width`: 匹配模板宽度 -
`Height`: 匹配模板高度

**注意**： - DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

---

# 查找文字 - FindStrFromPtr

## 函数简介

查找图片中的文字。

返回数据类型解析:

```
{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}
```

## 接口名称

```
FindStrFromPtr
```

## DLL调用

```
long FindStrFromPtr(long instance, long source, string str, string colorJson, string dict, double matchVal)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
source |
长整数型 |
图片 |
|

|
str |
字符串 |
查找字符串 |
|

|
colorJson |
字符串 |
颜色模型配置字符串，用于限定识别区域的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00` |
|

|
dict |
字符串 |
字库名称,为空时搜索所有字库 |
|

|
matchVal |
双精度浮点数 |
匹配值 |
|

### 示例

```
[](#cb4-1)// 示例代码待补充
```

## 返回值

查找到的结果（格式为二进制字符串指针） **注意**： -
DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

---

# 查找文字返回全部结果 -
FindStrAll

## 函数简介

查找文字返回全部结果。

返回数据类型解析:

```
[{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}]
```

## 接口名称

```
FindStrAll
```

## DLL调用

```
long FindStrAll(long instance, int x1, int y1, int x2, int y2, string str, string colorJson,string dict,double matchVal)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
x1 |
整数型 |
左上角x坐标 |
|

|
y1 |
整数型 |
左上角y坐标 |
|

|
x2 |
整数型 |
右下角x坐标 |
|

|
y2 |
整数型 |
右下角y坐标 |
|

|
str |
字符串 |
查找字符串 |
|

|
colorJson |
字符串 |
颜色模型配置字符串，用于限定识别区域的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00` |
|

|
dict |
字符串 |
字库名称,为空时搜索所有字库 |
|

|
matchVal |
双精度浮点数 |
匹配值 |
|

### 示例

```
[](#cb4-1)// 示例代码待补充
```

## 返回值

查找到的全部结果（格式为二进制字符串指针）

返回匹配结果，如

```
[{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
},
{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
}
]
```

**注意**： - DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

---

# 查找文字返回全部结果 -
FindStrFromPtrAll

## 函数简介

查找文字返回全部结果。

返回数据类型解析:

```
[{
"MatchVal": 0.85,//数据相似度
"MatchState": true,//返回数据是否大于指定精度,用于快速判断识别结果
"Index": 0,//多图识别时的返回索引
"Angle": 45.0,//识别结果角度
"X": 100,//识别结果X坐标
"Y": 200,//识别结果Y坐标
"Width":100,//识别结果宽度
"Height":100//识别结果高度
}]
```

## 接口名称

```
FindStrFromPtrAll
```

## DLL调用

```
long FindStrFromPtrAll(long instance, long source, string str, string colorJson,string dict,double matchVal)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
source |
长整数型 |
图片 |
|

|
str |
字符串 |
查找字符串 |
|

|
colorJson |
字符串 |
颜色模型配置字符串，用于限定识别区域的颜色范围，格式说明见 [颜色模型说明 -
ColorModel](/图像处理/颜色模型说明%20-%20ColorModel.html)。JSON格式示例：`[{"StartColor":"3278FA","EndColor":"6496FF","Type":0}]`；简化格式示例：`3278FA-000000|6496FF-202020`
或 `3278FA~6496FF` 或 `FF0000|00FF00` |
|

|
dict |
字符串 |
字库名称,为空时搜索所有字库 |
|

|
matchVal |
双精度浮点数 |
匹配值 |
|

### 示例

```
[](#cb4-1)// 示例代码待补充
```

## 返回值

查找到的全部结果（格式为二进制字符串指针）

返回匹配结果，如

```
[{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
},
{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
}
]
```

**注意**： - DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

---

# 添加字库数据 -
ImportDictWord

## 函数简介

将指定目录中的字库图片文件导入到OLA数据库中。可以选择是否覆盖已存在的字库数据。

## 函数原型

```
[](#cb1-1)int ImportDictWord(long ola, const long db, string dict_name, string pic_file_name, int cover);
```

## 参数定义

- `ola`: OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db`: 数据库对象指针，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口返回。

- `dict_name`: 字库名称。

- `pic_file_name`: 要导入的图像文件名。

- `cover`: 是否覆盖已存在的图像数据。`1`
表示覆盖，`0` 表示不覆盖。

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```

```

@tab Python

```

```

### 原生方式

@tab Python

```

```

## 注意事项

- 该函数用于将指定目录中的字库图像文件导入到OLA数据库中，适用于单个字库图像文件的导入场景。

- `cover` 参数用于控制是否覆盖已存在的图像数据。设置为
`1` 时，会覆盖现有数据；设置为 `0`
时，会跳过已存在的图像。

- 如果导入失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保目录路径和文件名正确，且图像文件格式受支持，否则可能导致导入失败。

---

# 移除字库 - RemoveDict

## 函数简介

从OLA数据库中移除指定字库名称的图像数据。

## 函数原型

```
[](#cb1-1)int RemoveDict(long ola, const long db, string dict_name);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `dict_name` (字符串): 字库名称。

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```

```

@tab Python

```

```

### 原生方式

@tab Python

```

```

## 注意事项

- 该函数用于从OLA数据库中移除指定字库名称的图像数据，适用于批量删除字库数据的场景。

- 如果移除失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保字库名称正确，且字库图像数据存在于数据库中，否则可能导致移除失败。

---

# 移除词典词条 -
RemoveDictWord

## 函数简介

从OLA数据库中移除指定字库名称和词条名的图像数据。

## 函数原型

```
[](#cb1-1)int RemoveDictWord(long ola, const long db, string dict_name, string word);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `dictName` (字符串): 字库名称。

- `word` (字符串): 要移除的文字。

## 返回值

- 返回值：操作结果。成功返回 `1`，失败返回
`0`。

## 示例

### SDK

@tab C##

```

```

@tab Python

```

```

### 原生方式

@tab Python

```

```

## 注意事项

- 该函数用于从OLA数据库中移除指定字库名称和词条的图像数据，适用于删除单个词条数据的场景。

- 如果移除失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保字库名称和词条名正确，且字库图像数据存在于数据库中，否则可能导致移除失败。

---

# 获取OCR配置 - GetOcrConfig

## 函数简介

获取OCR（光学字符识别）的配置参数。此函数可以读取PP-OCRv5模型的各种配置参数，包括GPU设置、检测参数、识别参数、分类参数等。适用于需要查看或验证当前OCR配置的场景。

## 接口名称

```
GetOcrConfig
```

## DLL调用

```
long GetOcrConfig(long instance, string configKey)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
configKey |
字符串 |
配置键名称，支持所有OCR配置参数 |
|

### 示例

```
[](#cb3-1)// 获取GPU相关配置
[](#cb3-2)long gpuConfig = GetOcrConfig(ola, "OcrUseGpu");
[](#cb3-3)if (gpuConfig != 0) {
[](#cb3-4)    char* gpuStr = (char*)gpuConfig;
[](#cb3-5)    printf("GPU使用状态: %s\n", gpuStr);
[](#cb3-6)    free(gpuStr);
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 获取检测模型路径
[](#cb3-10)long detModelPath = GetOcrConfig(ola, "OcrDetModelDir");
[](#cb3-11)if (detModelPath != 0) {
[](#cb3-12)    char* pathStr = (char*)detModelPath;
[](#cb3-13)    printf("检测模型路径: %s\n", pathStr);
[](#cb3-14)    free(pathStr);
[](#cb3-15)}
[](#cb3-16)
[](#cb3-17)// 获取识别模型路径
[](#cb3-18)long recModelPath = GetOcrConfig(ola, "OcrRecModelDir");
[](#cb3-19)if (recModelPath != 0) {
[](#cb3-20)    char* pathStr = (char*)recModelPath;
[](#cb3-21)    printf("识别模型路径: %s\n", pathStr);
[](#cb3-22)    free(pathStr);
[](#cb3-23)}
[](#cb3-24)
[](#cb3-25)// 获取CPU线程数配置
[](#cb3-26)long cpuThreads = GetOcrConfig(ola, "OcrCpuThreads");
[](#cb3-27)if (cpuThreads != 0) {
[](#cb3-28)    char* threadsStr = (char*)cpuThreads;
[](#cb3-29)    printf("CPU线程数: %s\n", threadsStr);
[](#cb3-30)    free(threadsStr);
[](#cb3-31)}
[](#cb3-32)
[](#cb3-33)// 获取检测阈值配置
[](#cb3-34)long detThresh = GetOcrConfig(ola, "OcrDetDbThresh");
[](#cb3-35)if (detThresh != 0) {
[](#cb3-36)    char* threshStr = (char*)detThresh;
[](#cb3-37)    printf("检测DB阈值: %s\n", threshStr);
[](#cb3-38)    free(threshStr);
[](#cb3-39)}
[](#cb3-40)
[](#cb3-41)// 获取识别批处理数量
[](#cb3-42)long recBatchNum = GetOcrConfig(ola, "OcrRecBatchNum");
[](#cb3-43)if (recBatchNum != 0) {
[](#cb3-44)    char* batchStr = (char*)recBatchNum;
[](#cb3-45)    printf("识别批处理数量: %s\n", batchStr);
[](#cb3-46)    free(batchStr);
[](#cb3-47)}
[](#cb3-48)
[](#cb3-49)// 获取推理精度配置
[](#cb3-50)long precision = GetOcrConfig(ola, "OcrPrecision");
[](#cb3-51)if (precision != 0) {
[](#cb3-52)    char* precisionStr = (char*)precision;
[](#cb3-53)    printf("推理精度: %s\n", precisionStr);
[](#cb3-54)    free(precisionStr);
[](#cb3-55)}
[](#cb3-56)
[](#cb3-57)// 获取GPU内存配置
[](#cb3-58)long gpuMem = GetOcrConfig(ola, "OcrGpuMem");
[](#cb3-59)if (gpuMem != 0) {
[](#cb3-60)    char* memStr = (char*)gpuMem;
[](#cb3-61)    printf("GPU内存大小: %s MB\n", memStr);
[](#cb3-62)    free(memStr);
[](#cb3-63)}
[](#cb3-64)
[](#cb3-65)// 获取分类阈值配置
[](#cb3-66)long clsThresh = GetOcrConfig(ola, "OcrClsThresh");
[](#cb3-67)if (clsThresh != 0) {
[](#cb3-68)    char* threshStr = (char*)clsThresh;
[](#cb3-69)    printf("分类阈值: %s\n", threshStr);
[](#cb3-70)    free(threshStr);
[](#cb3-71)}
[](#cb3-72)
[](#cb3-73)// 获取字符字典路径
[](#cb3-74)long charDictPath = GetOcrConfig(ola, "OcrRecCharDictPath");
[](#cb3-75)if (charDictPath != 0) {
[](#cb3-76)    char* dictStr = (char*)charDictPath;
[](#cb3-77)    printf("字符字典路径: %s\n", dictStr);
[](#cb3-78)    free(dictStr);
[](#cb3-79)}
```

## 返回值

long: 返回配置值的字符串指针，需要手动释放内存

## 注意事项

- 返回的字符串需要手动释放内存

- 支持所有OCR配置参数，包括：

### GPU相关参数

- **OcrUseGpu** (bool):
是否使用GPU推理，false使用CPU，true使用GPU，默认false

- **OcrUseTensorrt** (bool):
是否使用TensorRT加速，默认false

- **OcrGpuId** (int):
GPU设备ID，0表示第一个GPU，默认0

- **OcrGpuMem** (int): GPU内存大小(MB)，默认4000

### CPU相关参数

- **OcrCpuThreads** (int): CPU线程数，默认8

- **OcrEnableMkldnn** (bool):
是否启用MKL-DNN加速，默认true

### 推理相关参数

- **OcrPrecision** (string):
推理精度，可选fp32/fp16/int8，默认”int8”

- **OcrBenchmark** (bool):
是否启用性能基准测试，默认false

- **OcrOutput** (string):
基准测试日志保存路径，默认”./output/”

- **OcrImageDir** (string): 输入图像目录，默认””

- **OcrType** (string):
执行类型，ocr或structure，默认”ocr”

### 检测相关参数

- **OcrDetModelDir** (string):
检测模型路径，默认”./OCRv5_model/PP-OCRv5_mobile_det_infer/”

- **OcrLimitType** (string):
输入图像限制类型，max或min，默认”max”

- **OcrLimitSideLen** (int):
输入图像限制边长，默认960

- **OcrDetDbThresh** (double):
检测DB阈值，范围0.0-1.0，默认0.3

- **OcrDetDbBoxThresh** (double):
检测DB框阈值，范围0.0-1.0，默认0.6

- **OcrDetDbUnclipRatio** (double):
检测DB未裁剪比例，默认1.5

- **OcrUseDilation** (bool):
是否对输出图使用膨胀操作，默认false

- **OcrDetDbScoreMode** (string):
检测DB评分模式，fast或slow，默认”slow”

- **OcrVisualize** (bool):
是否显示检测结果，默认true

### 识别相关参数

- **OcrRecModelDir** (string):
识别模型路径，默认”./OCRv5_model/PP-OCRv5_mobile_rec_infer/”

- **OcrRecBatchNum** (int): 识别批处理数量，默认6

- **OcrRecCharDictPath** (string):
识别字符字典路径，默认”./ppocr/utils/ppocr_keys_v1.txt”

- **OcrRecImgH** (int): 识别图像高度，默认48

- **OcrRecImgW** (int): 识别图像宽度，默认320

### 分类相关参数

- **OcrUseAngleCls** (bool):
是否使用角度分类，默认false

- **OcrClsModelDir** (string): 分类模型路径，默认””

- **OcrClsThresh** (double):
分类阈值，范围0.0-1.0，默认0.9

- **OcrClsBatchNum** (int): 分类批处理数量，默认1

### 布局相关参数

- **OcrLayoutModelDir** (string):
布局模型路径，默认””

- **OcrLayoutDictPath** (string):
布局字典路径，默认”./ppocr/utils/dict/layout_dict/layout_publaynet_dict.txt”

- **OcrLayoutScoreThreshold** (double):
布局评分阈值，范围0.0-1.0，默认0.5

- **OcrLayoutNmsThreshold** (double):
布局NMS阈值，范围0.0-1.0，默认0.5

### 表格相关参数

- **OcrTableModelDir** (string):
表格结构模型路径，默认””

- **OcrTableMaxLen** (int): 表格最大长度，默认488

- **OcrTableBatchNum** (int): 表格批处理数量，默认1

- **OcrMergeNoSpanStructure** (bool):
是否合并无跨度结构，默认true

- **OcrTableCharDictPath** (string):
表格字符字典路径，默认”./ppocr/utils/dict/table_structure_dict_ch.txt”

### 前向相关参数

- **OcrDet** (bool): 是否使用检测，默认true

- **OcrRec** (bool): 是否使用识别，默认true

- **OcrCls** (bool): 是否使用分类，默认false

- **OcrTable** (bool): 是否使用表格结构，默认false

- **OcrLayout** (bool): 是否使用布局分析，默认false

### 注意事项

- 配置值以JSON字符串形式返回，需要根据参数类型进行转换

- 与 [SetOcrConfig](/文字识别/设置OCR配置%20-%20SetOcrConfig.html) 和
[SetOcrConfigByKey](/文字识别/设置OCR配置键值%20-%20SetOcrConfigByKey.html)
函数配合使用

- 适用于OCR配置管理和调试场景

---

# 设置OCR配置 - SetOcrConfig

## 函数简介

设置OCR（光学字符识别）的配置参数。此函数可以通过JSON格式的配置字符串批量设置PP-OCRv5模型的各种参数，包括GPU设置、检测参数、识别参数、分类参数等。适用于需要批量配置OCR参数的场景。

## 接口名称

```
SetOcrConfig
```

## DLL调用

```
int SetOcrConfig(long instance, string configStr)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
configStr |
字符串 |
JSON格式的配置字符串，包含多个OCR配置参数 |
|

### 示例

```
[](#cb3-1)// 基本GPU配置设置
[](#cb3-2)string gpuConfig = "{\"OcrUseGpu\":true,\"OcrGpuId\":0,\"OcrGpuMem\":4000}";
[](#cb3-3)int result = SetOcrConfig(ola, gpuConfig);
[](#cb3-4)if (result == 1) {
[](#cb3-5)    printf("GPU配置设置成功\n");
[](#cb3-6)} else {
[](#cb3-7)    printf("GPU配置设置失败\n");
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)// 检测模型配置
[](#cb3-11)string detConfig = "{\"OcrDetModelDir\":\"./OCRv5_model/PP-OCRv5_mobile_det_infer/\",\"OcrDetDbThresh\":0.3,\"OcrDetDbBoxThresh\":0.6}";
[](#cb3-12)int result = SetOcrConfig(ola, detConfig);
[](#cb3-13)if (result == 1) {
[](#cb3-14)    printf("检测模型配置设置成功\n");
[](#cb3-15)} else {
[](#cb3-16)    printf("检测模型配置设置失败\n");
[](#cb3-17)}
[](#cb3-18)
[](#cb3-19)// 识别模型配置
[](#cb3-20)string recConfig = "{\"OcrRecModelDir\":\"./OCRv5_model/PP-OCRv5_mobile_rec_infer/\",\"OcrRecBatchNum\":6,\"OcrRecCharDictPath\":\"./ppocr/utils/ppocr_keys_v1.txt\"}";
[](#cb3-21)int result = SetOcrConfig(ola, recConfig);
[](#cb3-22)if (result == 1) {
[](#cb3-23)    printf("识别模型配置设置成功\n");
[](#cb3-24)} else {
[](#cb3-25)    printf("识别模型配置设置失败\n");
[](#cb3-26)}
[](#cb3-27)
[](#cb3-28)// CPU配置设置
[](#cb3-29)string cpuConfig = "{\"OcrCpuThreads\":8,\"OcrEnableMkldnn\":true,\"OcrPrecision\":\"int8\"}";
[](#cb3-30)int result = SetOcrConfig(ola, cpuConfig);
[](#cb3-31)if (result == 1) {
[](#cb3-32)    printf("CPU配置设置成功\n");
[](#cb3-33)} else {
[](#cb3-34)    printf("CPU配置设置失败\n");
[](#cb3-35)}
[](#cb3-36)
[](#cb3-37)// 分类模型配置
[](#cb3-38)string clsConfig = "{\"OcrUseAngleCls\":false,\"OcrClsModelDir\":\"\",\"OcrClsThresh\":0.9}";
[](#cb3-39)int result = SetOcrConfig(ola, clsConfig);
[](#cb3-40)if (result == 1) {
[](#cb3-41)    printf("分类模型配置设置成功\n");
[](#cb3-42)} else {
[](#cb3-43)    printf("分类模型配置设置失败\n");
[](#cb3-44)}
[](#cb3-45)
[](#cb3-46)// 布局模型配置
[](#cb3-47)string layoutConfig = "{\"OcrLayoutModelDir\":\"\",\"OcrLayoutScoreThreshold\":0.5,\"OcrLayoutNmsThreshold\":0.5}";
[](#cb3-48)int result = SetOcrConfig(ola, layoutConfig);
[](#cb3-49)if (result == 1) {
[](#cb3-50)    printf("布局模型配置设置成功\n");
[](#cb3-51)} else {
[](#cb3-52)    printf("布局模型配置设置失败\n");
[](#cb3-53)}
[](#cb3-54)
[](#cb3-55)// 表格模型配置
[](#cb3-56)string tableConfig = "{\"OcrTableModelDir\":\"\",\"OcrTableMaxLen\":488,\"OcrTableBatchNum\":1}";
[](#cb3-57)int result = SetOcrConfig(ola, tableConfig);
[](#cb3-58)if (result == 1) {
[](#cb3-59)    printf("表格模型配置设置成功\n");
[](#cb3-60)} else {
[](#cb3-61)    printf("表格模型配置设置失败\n");
[](#cb3-62)}
[](#cb3-63)
[](#cb3-64)// 完整配置示例
[](#cb3-65)string fullConfig = "{\"OcrUseGpu\":false,\"OcrCpuThreads\":8,\"OcrDetModelDir\":\"./OCRv5_model/PP-OCRv5_mobile_det_infer/\",\"OcrRecModelDir\":\"./OCRv5_model/PP-OCRv5_mobile_rec_infer/\",\"OcrDetDbThresh\":0.3,\"OcrRecBatchNum\":6}";
[](#cb3-66)int result = SetOcrConfig(ola, fullConfig);
[](#cb3-67)if (result == 1) {
[](#cb3-68)    printf("完整OCR配置设置成功\n");
[](#cb3-69)} else {
[](#cb3-70)    printf("完整OCR配置设置失败\n");
[](#cb3-71)}
[](#cb3-72)
[](#cb3-73)// 性能优化配置
[](#cb3-74)string perfConfig = "{\"OcrUseGpu\":true,\"OcrUseTensorrt\":true,\"OcrGpuId\":0,\"OcrGpuMem\":4000,\"OcrCpuThreads\":8,\"OcrEnableMkldnn\":true,\"OcrPrecision\":\"int8\"}";
[](#cb3-75)int result = SetOcrConfig(ola, perfConfig);
[](#cb3-76)if (result == 1) {
[](#cb3-77)    printf("性能优化配置设置成功\n");
[](#cb3-78)} else {
[](#cb3-79)    printf("性能优化配置设置失败\n");
[](#cb3-80)}
```

## 返回值

int: 返回设置结果 - 1: 设置成功 - 0: 设置失败

## 注意事项

- 配置字符串必须为有效的JSON格式

- 支持的配置参数包括：

### GPU相关参数

- **OcrUseGpu** (bool):
是否使用GPU推理，false使用CPU，true使用GPU，默认false

- **OcrUseTensorrt** (bool):
是否使用TensorRT加速，默认false

- **OcrGpuId** (int):
GPU设备ID，0表示第一个GPU，默认0

- **OcrGpuMem** (int): GPU内存大小(MB)，默认4000

### CPU相关参数

- **OcrCpuThreads** (int): CPU线程数，默认8

- **OcrEnableMkldnn** (bool):
是否启用MKL-DNN加速，默认true

### 推理相关参数

- **OcrPrecision** (string):
推理精度，可选fp32/fp16/int8，默认”int8”

- **OcrBenchmark** (bool):
是否启用性能基准测试，默认false

- **OcrOutput** (string):
基准测试日志保存路径，默认”./output/”

- **OcrImageDir** (string): 输入图像目录，默认””

- **OcrType** (string):
执行类型，ocr或structure，默认”ocr”

### 检测相关参数

- **OcrDetModelDir** (string):
检测模型路径，默认”./OCRv5_model/PP-OCRv5_mobile_det_infer/”

- **OcrLimitType** (string):
输入图像限制类型，max或min，默认”max”

- **OcrLimitSideLen** (int):
输入图像限制边长，默认960

- **OcrDetDbThresh** (double):
检测DB阈值，范围0.0-1.0，默认0.3

- **OcrDetDbBoxThresh** (double):
检测DB框阈值，范围0.0-1.0，默认0.6

- **OcrDetDbUnclipRatio** (double):
检测DB未裁剪比例，默认1.5

- **OcrUseDilation** (bool):
是否对输出图使用膨胀操作，默认false

- **OcrDetDbScoreMode** (string):
检测DB评分模式，fast或slow，默认”slow”

- **OcrVisualize** (bool):
是否显示检测结果，默认true

### 识别相关参数

- **OcrRecModelDir** (string):
识别模型路径，默认”./OCRv5_model/PP-OCRv5_mobile_rec_infer/”

- **OcrRecBatchNum** (int): 识别批处理数量，默认6

- **OcrRecCharDictPath** (string):
识别字符字典路径，默认”./ppocr/utils/ppocr_keys_v1.txt”

- **OcrRecImgH** (int): 识别图像高度，默认48

- **OcrRecImgW** (int): 识别图像宽度，默认320

### 分类相关参数

- **OcrUseAngleCls** (bool):
是否使用角度分类，默认false

- **OcrClsModelDir** (string): 分类模型路径，默认””

- **OcrClsThresh** (double):
分类阈值，范围0.0-1.0，默认0.9

- **OcrClsBatchNum** (int): 分类批处理数量，默认1

### 布局相关参数

- **OcrLayoutModelDir** (string):
布局模型路径，默认””

- **OcrLayoutDictPath** (string):
布局字典路径，默认”./ppocr/utils/dict/layout_dict/layout_publaynet_dict.txt”

- **OcrLayoutScoreThreshold** (double):
布局评分阈值，范围0.0-1.0，默认0.5

- **OcrLayoutNmsThreshold** (double):
布局NMS阈值，范围0.0-1.0，默认0.5

### 表格相关参数

- **OcrTableModelDir** (string):
表格结构模型路径，默认””

- **OcrTableMaxLen** (int): 表格最大长度，默认488

- **OcrTableBatchNum** (int): 表格批处理数量，默认1

- **OcrMergeNoSpanStructure** (bool):
是否合并无跨度结构，默认true

- **OcrTableCharDictPath** (string):
表格字符字典路径，默认”./ppocr/utils/dict/table_structure_dict_ch.txt”

### 前向相关参数

- **OcrDet** (bool): 是否使用检测，默认true

- **OcrRec** (bool): 是否使用识别，默认true

- **OcrCls** (bool): 是否使用分类，默认false

- **OcrTable** (bool): 是否使用表格结构，默认false

- **OcrLayout** (bool): 是否使用布局分析，默认false

### 注意事项

- 与 [GetOcrConfig](/文字识别/获取OCR配置%20-%20GetOcrConfig.html) 和
[SetOcrConfigByKey](/文字识别/设置OCR配置键值%20-%20SetOcrConfigByKey.html)
函数配合使用

- 适用于OCR配置管理和性能优化场景

---

# 设置OCR配置键值 -
SetOcrConfigByKey

## 函数简介

通过键值对的方式设置OCR（光学字符识别）的单个配置参数。此函数可以单独设置PP-OCRv5模型的特定参数，包括GPU设置、检测参数、识别参数、分类参数等。适用于需要精确控制单个OCR参数的场景。

## 接口名称

```
SetOcrConfigByKey
```

## DLL调用

```
int SetOcrConfigByKey(long instance, string key, string value)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
key |
字符串 |
配置键名称，支持所有OCR配置参数 |
|

|
value |
字符串 |
配置值，根据参数类型设置相应的值 |
|

### 示例

```
[](#cb3-1)// 设置GPU使用状态
[](#cb3-2)int result = SetOcrConfigByKey(ola, "OcrUseGpu", "true");
[](#cb3-3)if (result == 1) {
[](#cb3-4)    printf("GPU使用状态设置成功\n");
[](#cb3-5)} else {
[](#cb3-6)    printf("GPU使用状态设置失败\n");
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 设置GPU设备ID
[](#cb3-10)result = SetOcrConfigByKey(ola, "OcrGpuId", "0");
[](#cb3-11)if (result == 1) {
[](#cb3-12)    printf("GPU设备ID设置成功\n");
[](#cb3-13)} else {
[](#cb3-14)    printf("GPU设备ID设置失败\n");
[](#cb3-15)}
[](#cb3-16)
[](#cb3-17)// 设置GPU内存大小
[](#cb3-18)result = SetOcrConfigByKey(ola, "OcrGpuMem", "4000");
[](#cb3-19)if (result == 1) {
[](#cb3-20)    printf("GPU内存大小设置成功\n");
[](#cb3-21)} else {
[](#cb3-22)    printf("GPU内存大小设置失败\n");
[](#cb3-23)}
[](#cb3-24)
[](#cb3-25)// 设置CPU线程数
[](#cb3-26)result = SetOcrConfigByKey(ola, "OcrCpuThreads", "8");
[](#cb3-27)if (result == 1) {
[](#cb3-28)    printf("CPU线程数设置成功\n");
[](#cb3-29)} else {
[](#cb3-30)    printf("CPU线程数设置失败\n");
[](#cb3-31)}
[](#cb3-32)
[](#cb3-33)// 设置检测模型路径
[](#cb3-34)result = SetOcrConfigByKey(ola, "OcrDetModelDir", "./OCRv5_model/PP-OCRv5_mobile_det_infer/");
[](#cb3-35)if (result == 1) {
[](#cb3-36)    printf("检测模型路径设置成功\n");
[](#cb3-37)} else {
[](#cb3-38)    printf("检测模型路径设置失败\n");
[](#cb3-39)}
[](#cb3-40)
[](#cb3-41)// 设置识别模型路径
[](#cb3-42)result = SetOcrConfigByKey(ola, "OcrRecModelDir", "./OCRv5_model/PP-OCRv5_mobile_rec_infer/");
[](#cb3-43)if (result == 1) {
[](#cb3-44)    printf("识别模型路径设置成功\n");
[](#cb3-45)} else {
[](#cb3-46)    printf("识别模型路径设置失败\n");
[](#cb3-47)}
[](#cb3-48)
[](#cb3-49)// 设置检测DB阈值
[](#cb3-50)result = SetOcrConfigByKey(ola, "OcrDetDbThresh", "0.3");
[](#cb3-51)if (result == 1) {
[](#cb3-52)    printf("检测DB阈值设置成功\n");
[](#cb3-53)} else {
[](#cb3-54)    printf("检测DB阈值设置失败\n");
[](#cb3-55)}
[](#cb3-56)
[](#cb3-57)// 设置检测DB框阈值
[](#cb3-58)result = SetOcrConfigByKey(ola, "OcrDetDbBoxThresh", "0.6");
[](#cb3-59)if (result == 1) {
[](#cb3-60)    printf("检测DB框阈值设置成功\n");
[](#cb3-61)} else {
[](#cb3-62)    printf("检测DB框阈值设置失败\n");
[](#cb3-63)}
[](#cb3-64)
[](#cb3-65)// 设置识别批处理数量
[](#cb3-66)result = SetOcrConfigByKey(ola, "OcrRecBatchNum", "6");
[](#cb3-67)if (result == 1) {
[](#cb3-68)    printf("识别批处理数量设置成功\n");
[](#cb3-69)} else {
[](#cb3-70)    printf("识别批处理数量设置失败\n");
[](#cb3-71)}
[](#cb3-72)
[](#cb3-73)// 设置推理精度
[](#cb3-74)result = SetOcrConfigByKey(ola, "OcrPrecision", "int8");
[](#cb3-75)if (result == 1) {
[](#cb3-76)    printf("推理精度设置成功\n");
[](#cb3-77)} else {
[](#cb3-78)    printf("推理精度设置失败\n");
[](#cb3-79)}
[](#cb3-80)
[](#cb3-81)// 设置字符字典路径
[](#cb3-82)result = SetOcrConfigByKey(ola, "OcrRecCharDictPath", "./ppocr/utils/ppocr_keys_v1.txt");
[](#cb3-83)if (result == 1) {
[](#cb3-84)    printf("字符字典路径设置成功\n");
[](#cb3-85)} else {
[](#cb3-86)    printf("字符字典路径设置失败\n");
[](#cb3-87)}
[](#cb3-88)
[](#cb3-89)// 设置分类阈值
[](#cb3-90)result = SetOcrConfigByKey(ola, "OcrClsThresh", "0.9");
[](#cb3-91)if (result == 1) {
[](#cb3-92)    printf("分类阈值设置成功\n");
[](#cb3-93)} else {
[](#cb3-94)    printf("分类阈值设置失败\n");
[](#cb3-95)}
[](#cb3-96)
[](#cb3-97)// 设置是否使用角度分类
[](#cb3-98)result = SetOcrConfigByKey(ola, "OcrUseAngleCls", "false");
[](#cb3-99)if (result == 1) {
[](#cb3-100)    printf("角度分类设置成功\n");
[](#cb3-101)} else {
[](#cb3-102)    printf("角度分类设置失败\n");
[](#cb3-103)}
[](#cb3-104)
[](#cb3-105)// 设置是否启用MKL-DNN加速
[](#cb3-106)result = SetOcrConfigByKey(ola, "OcrEnableMkldnn", "true");
[](#cb3-107)if (result == 1) {
[](#cb3-108)    printf("MKL-DNN加速设置成功\n");
[](#cb3-109)} else {
[](#cb3-110)    printf("MKL-DNN加速设置失败\n");
[](#cb3-111)}
[](#cb3-112)
[](#cb3-113)// 设置是否使用TensorRT加速
[](#cb3-114)result = SetOcrConfigByKey(ola, "OcrUseTensorrt", "false");
[](#cb3-115)if (result == 1) {
[](#cb3-116)    printf("TensorRT加速设置成功\n");
[](#cb3-117)} else {
[](#cb3-118)    printf("TensorRT加速设置失败\n");
[](#cb3-119)}
[](#cb3-120)
[](#cb3-121)// 设置输入图像限制边长
[](#cb3-122)result = SetOcrConfigByKey(ola, "OcrLimitSideLen", "960");
[](#cb3-123)if (result == 1) {
[](#cb3-124)    printf("输入图像限制边长设置成功\n");
[](#cb3-125)} else {
[](#cb3-126)    printf("输入图像限制边长设置失败\n");
[](#cb3-127)}
[](#cb3-128)
[](#cb3-129)// 设置识别图像高度
[](#cb3-130)result = SetOcrConfigByKey(ola, "OcrRecImgH", "48");
[](#cb3-131)if (result == 1) {
[](#cb3-132)    printf("识别图像高度设置成功\n");
[](#cb3-133)} else {
[](#cb3-134)    printf("识别图像高度设置失败\n");
[](#cb3-135)}
[](#cb3-136)
[](#cb3-137)// 设置识别图像宽度
[](#cb3-138)result = SetOcrConfigByKey(ola, "OcrRecImgW", "320");
[](#cb3-139)if (result == 1) {
[](#cb3-140)    printf("识别图像宽度设置成功\n");
[](#cb3-141)} else {
[](#cb3-142)    printf("识别图像宽度设置失败\n");
[](#cb3-143)}
```

## 返回值

int: 返回设置结果 - 1: 设置成功 - 0: 设置失败

## 注意事项

- 支持的配置参数包括：

### GPU相关参数

- **OcrUseGpu** (bool):
是否使用GPU推理，false使用CPU，true使用GPU，默认false

- **OcrUseTensorrt** (bool):
是否使用TensorRT加速，默认false

- **OcrGpuId** (int):
GPU设备ID，0表示第一个GPU，默认0

- **OcrGpuMem** (int): GPU内存大小(MB)，默认4000

### CPU相关参数

- **OcrCpuThreads** (int): CPU线程数，默认8

- **OcrEnableMkldnn** (bool):
是否启用MKL-DNN加速，默认true

### 推理相关参数

- **OcrPrecision** (string):
推理精度，可选fp32/fp16/int8，默认”int8”

- **OcrBenchmark** (bool):
是否启用性能基准测试，默认false

- **OcrOutput** (string):
基准测试日志保存路径，默认”./output/”

- **OcrImageDir** (string): 输入图像目录，默认””

- **OcrType** (string):
执行类型，ocr或structure，默认”ocr”

### 检测相关参数

- **OcrDetModelDir** (string):
检测模型路径，默认”./OCRv5_model/PP-OCRv5_mobile_det_infer/”

- **OcrLimitType** (string):
输入图像限制类型，max或min，默认”max”

- **OcrLimitSideLen** (int):
输入图像限制边长，默认960

- **OcrDetDbThresh** (double):
检测DB阈值，范围0.0-1.0，默认0.3

- **OcrDetDbBoxThresh** (double):
检测DB框阈值，范围0.0-1.0，默认0.6

- **OcrDetDbUnclipRatio** (double):
检测DB未裁剪比例，默认1.5

- **OcrUseDilation** (bool):
是否对输出图使用膨胀操作，默认false

- **OcrDetDbScoreMode** (string):
检测DB评分模式，fast或slow，默认”slow”

- **OcrVisualize** (bool):
是否显示检测结果，默认true

### 识别相关参数

- **OcrRecModelDir** (string):
识别模型路径，默认”./OCRv5_model/PP-OCRv5_mobile_rec_infer/”

- **OcrRecBatchNum** (int): 识别批处理数量，默认6

- **OcrRecCharDictPath** (string):
识别字符字典路径，默认”./ppocr/utils/ppocr_keys_v1.txt”

- **OcrRecImgH** (int): 识别图像高度，默认48

- **OcrRecImgW** (int): 识别图像宽度，默认320

### 分类相关参数

- **OcrUseAngleCls** (bool):
是否使用角度分类，默认false

- **OcrClsModelDir** (string): 分类模型路径，默认””

- **OcrClsThresh** (double):
分类阈值，范围0.0-1.0，默认0.9

- **OcrClsBatchNum** (int): 分类批处理数量，默认1

### 布局相关参数

- **OcrLayoutModelDir** (string):
布局模型路径，默认””

- **OcrLayoutDictPath** (string):
布局字典路径，默认”./ppocr/utils/dict/layout_dict/layout_publaynet_dict.txt”

- **OcrLayoutScoreThreshold** (double):
布局评分阈值，范围0.0-1.0，默认0.5

- **OcrLayoutNmsThreshold** (double):
布局NMS阈值，范围0.0-1.0，默认0.5

### 表格相关参数

- **OcrTableModelDir** (string):
表格结构模型路径，默认””

- **OcrTableMaxLen** (int): 表格最大长度，默认488

- **OcrTableBatchNum** (int): 表格批处理数量，默认1

- **OcrMergeNoSpanStructure** (bool):
是否合并无跨度结构，默认true

- **OcrTableCharDictPath** (string):
表格字符字典路径，默认”./ppocr/utils/dict/table_structure_dict_ch.txt”

### 前向相关参数

- **OcrDet** (bool): 是否使用检测，默认true

- **OcrRec** (bool): 是否使用识别，默认true

- **OcrCls** (bool): 是否使用分类，默认false

- **OcrTable** (bool): 是否使用表格结构，默认false

- **OcrLayout** (bool): 是否使用布局分析，默认false

### 注意事项

- 布尔值参数使用”true”或”false”字符串

- 数值参数使用字符串格式

- 路径参数使用字符串格式

- 配置修改后需要重新初始化OCR模型才能生效

- 与 [GetOcrConfig](/文字识别/获取OCR配置%20-%20GetOcrConfig.html) 和
[SetOcrConfig](/文字识别/设置OCR配置%20-%20SetOcrConfig.html)
函数配合使用

- 适用于精确控制单个OCR参数的场景

---

# 读取字库图片 - GetDictImage

## 函数简介

从OLA数据库中获取指定字库和指定文字(可多个)的图像数据，支持设置文字间隔与方向，返回图像对象的指针。

## 函数原型

```
[](#cb1-1)long GetDictImage(long ola, const long db, string dict_name, string word, int gap, int dir);
```

## 参数定义

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `db` (长整型数): 数据库连接句柄，由 [OpenDatabase](/数据库/打开数据库%20-%20OpenDatabase.html)
接口生成。

- `dictName` (字符串): 字库名称。

- `word` (字符串): 要读取的文字。

- `gap`: 文字间隔，单位为像素。

- `dir`: 拼接方向，0-水平拼接，1-垂直拼接

## 返回值

- 返回值：图像对象的指针。如果操作失败，返回 `0`。

## 示例

### SDK

@tab C##

```

```

@tab Python

```

```

### 原生方式

@tab Python

```

```

## 注意事项

- 该函数用于从OLA数据库中获取指定字典名称和文字的图像数据，适用于从数据库中查找指定文字的场景。

- 如果图像不存在或操作失败，函数将返回 `0`。可以通过 [GetDatabaseError](/数据库/读取错误信息%20-%20GetDatabaseError.html)
函数获取详细的错误信息。

- 确保字典名称和文字正确，且图像数据存在于数据库中，否则可能导致获取失败。

- 使用完返回的图像对象指针后，应妥善处理资源，避免内存泄漏。

---

## 汇编

# 执行汇编指令 - AsmCall

## 函数简介

在指定进程中执行汇编指令。支持多种执行模式，可以在当前进程、目标进程或已注入的进程中执行汇编代码。此函数提供了强大的底层控制能力，适用于高级系统编程和逆向工程。

## 接口名称

```
AsmCall
```

## DLL调用

```
long AsmCall(long instance, long hwnd, string asmStr, int type, long baseAddr)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄或进程ID，根据type参数决定用途 |
|

|
asmStr |
字符串 |
汇编语言字符串，大小写均可，如”mov eax,1”，也支持输入机器码 |
|

|
type |
整数型 |
执行类型：
*0 在本进程中执行(创建线程),hwnd无效
* 1
在hwnd指定进程内执行(创建远程线程)
* 2
在已注入绑定的目标进程创建线程执行(需排队)
* 3
同模式2,但在hwnd所在线程直接执行
* 4 同模式0,但在当前线程直接执行

* 5 在hwnd指定进程内执行(APC注入)
* 6
直接在hwnd所在线程执行 |
|

|
baseAddr |
长整数型 |
汇编指令所在的地址，如果为0则自动分配内存 |
|

### 示例

```
[](#cb3-1)// 在当前进程中执行简单汇编指令
[](#cb3-2)char asm_code[] = "mov eax, 123\nret";
[](#cb3-3)long result = AsmCall(ola, 0, asm_code, 0, 0);
[](#cb3-4)printf("执行结果: %ld\n", result);
[](#cb3-5)
[](#cb3-6)// 在目标进程中执行汇编指令
[](#cb3-7)long target_hwnd = FindWindow(ola, "Notepad", "");
[](#cb3-8)if (target_hwnd != 0) {
[](#cb3-9)    char asm_code[] = "mov eax, 456\nret";
[](#cb3-10)    long result = AsmCall(ola, target_hwnd, asm_code, 1, 0);
[](#cb3-11)    printf("远程执行结果: %ld\n", result);
[](#cb3-12)}
[](#cb3-13)
[](#cb3-14)// 在指定地址执行汇编指令
[](#cb3-15)char asm_code[] = "push ebp\nmov ebp, esp\nmov eax, 789\npop ebp\nret";
[](#cb3-16)long base_addr = 0x10000000; // 指定基地址
[](#cb3-17)long result = AsmCall(ola, 0, asm_code, 0, base_addr);
[](#cb3-18)
[](#cb3-19)// 在已注入的进程中执行
[](#cb3-20)long target_hwnd = FindWindow(ola, "Calculator", "");
[](#cb3-21)if (target_hwnd != 0) {
[](#cb3-22)    char asm_code[] = "mov eax, 999\nret";
[](#cb3-23)    long result = AsmCall(ola, target_hwnd, asm_code, 2, 0);
[](#cb3-24)    printf("注入进程执行结果: %ld\n", result);
[](#cb3-25)}
[](#cb3-26)
[](#cb3-27)// 直接在当前线程执行
[](#cb3-28)char asm_code[] = "mov eax, 111\nmov edx, 222\nret";
[](#cb3-29)long result = AsmCall(ola, 0, asm_code, 4, 0);
[](#cb3-30)printf("当前线程执行结果: %ld\n", result);
```

## 返回值

长整数型: - 32位进程返回EAX - 64位进程返回RAX - 执行失败返回0

## 注意事项

- 使用此函数需要谨慎，错误的汇编指令可能导致程序崩溃

- 建议在测试环境中先验证汇编代码的正确性

- 不同执行模式适用于不同的应用场景，请根据需求选择合适的type参数

- 在目标进程中执行需要相应的权限

- 使用APC注入模式(type=5)需要开启memory防护盾

- 返回值的解释取决于汇编指令的具体内容

- 建议在使用前备份重要数据

---

# 机器码转汇编 - Disassemble

## 函数简介

将指定的机器码转换为汇编语言输出。支持多种架构和模式，包括x86、ARM、ARM64等，以及16位、32位、64位模式。此函数适用于逆向工程和代码分析。

## 接口名称

```
Disassemble
```

## DLL调用

```
long Disassemble(long instance, string asmCode, long baseAddr, int arch, int mode, int showType)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
asmCode |
字符串 |
机器码，形式如”aa bb cc”这样的16进制表示的字符串(空格无所谓) |
|

|
baseAddr |
长整数型 |
指令所在的地址 |
|

|
arch |
整数型 |
架构类型：
0: x86
1: arm
2: arm64 |
|

|
mode |
整数型 |
模式：
16: 16位
32: 32位
64: 64位 |
|

|
showType |
整数型 |
显示类型：
0: 显示详细汇编信息
1: 只显示机器码 |
|

### 示例

```
[](#cb3-1)// x86 32位机器码转汇编
[](#cb3-2)char machine_code[] = "B8 7B 00 00 00"; // mov eax, 123
[](#cb3-3)long result = Disassemble(ola, machine_code, 0x10000000, 0, 32, 0);
[](#cb3-4)if (result != 0) {
[](#cb3-5)    char* asm_code = (char*)result;
[](#cb3-6)    printf("汇编代码: %s\n", asm_code);
[](#cb3-7)    FreeStringPtr(ola, result);
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)// x86 64位机器码转汇编
[](#cb3-11)char machine_code_64[] = "48 C7 C0 C8 01 00 00"; // mov rax, 456
[](#cb3-12)long result = Disassemble(ola, machine_code_64, 0x10000000, 0, 64, 0);
[](#cb3-13)if (result != 0) {
[](#cb3-14)    char* asm_code = (char*)result;
[](#cb3-15)    printf("64位汇编代码: %s\n", asm_code);
[](#cb3-16)    FreeStringPtr(ola, result);
[](#cb3-17)}
[](#cb3-18)
[](#cb3-19)// ARM 32位机器码转汇编
[](#cb3-20)char arm_machine_code[] = "E3 A0 00 7B"; // mov r0, #123
[](#cb3-21)long result = Disassemble(ola, arm_machine_code, 0x10000000, 1, 32, 0);
[](#cb3-22)if (result != 0) {
[](#cb3-23)    char* asm_code = (char*)result;
[](#cb3-24)    printf("ARM汇编代码: %s\n", asm_code);
[](#cb3-25)    FreeStringPtr(ola, result);
[](#cb3-26)}
[](#cb3-27)
[](#cb3-28)// 复杂机器码转汇编
[](#cb3-29)char complex_machine_code[] = "55 89 E5 83 EC 10 8B 45 08 5D C3";
[](#cb3-30)long result = Disassemble(ola, complex_machine_code, 0x10000000, 0, 32, 0);
[](#cb3-31)if (result != 0) {
[](#cb3-32)    char* asm_code = (char*)result;
[](#cb3-33)    printf("复杂汇编代码: %s\n", asm_code);
[](#cb3-34)    FreeStringPtr(ola, result);
[](#cb3-35)}
[](#cb3-36)
[](#cb3-37)// 只显示机器码
[](#cb3-38)char simple_machine_code[] = "90 90 90"; // nop nop nop
[](#cb3-39)long result = Disassemble(ola, simple_machine_code, 0x10000000, 0, 32, 1);
[](#cb3-40)if (result != 0) {
[](#cb3-41)    char* asm_code = (char*)result;
[](#cb3-42)    printf("机器码显示: %s\n", asm_code);
[](#cb3-43)    FreeStringPtr(ola, result);
[](#cb3-44)}
[](#cb3-45)
[](#cb3-46)// 多条指令解析
[](#cb3-47)char multi_instructions[] = "B8 01 00 00 00 89 C2 C3";
[](#cb3-48)long result = Disassemble(ola, multi_instructions, 0x10000000, 0, 32, 0);
[](#cb3-49)if (result != 0) {
[](#cb3-50)    char* asm_code = (char*)result;
[](#cb3-51)    printf("多条指令: %s\n", asm_code);
[](#cb3-52)    // 多条指令以"|"连接
[](#cb3-53)    FreeStringPtr(ola, result);
[](#cb3-54)}
```

## 返回值

长整数型: - 成功返回汇编语言字符串的指针 - 失败返回0

## 注意事项

- 返回的字符串指针需要调用FreeStringPtr释放内存

- 如果有多条指令，则每条指令以字符”|“连接

- showType=0时显示详细汇编信息，包括地址、机器码、汇编指令

- showType=1时只显示机器码

- 机器码输入格式为16进制字符串，空格可以忽略

- 不同架构和模式支持的指令集不同

- baseAddr参数用于计算相对地址和符号解析

- 此函数适用于逆向工程、代码分析和调试工具开发

---

# 汇编转机器码 - Assemble

## 函数简介

将汇编语言字符串转换为机器码并以16进制字符串的形式输出。支持多种架构和模式，包括x86、ARM、ARM64等，以及16位、32位、64位模式。此函数适用于汇编代码分析和逆向工程。

## 接口名称

```
Assemble
```

## DLL调用

```
long Assemble(long instance, string asmStr, long baseAddr, int arch, int mode)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
asmStr |
字符串 |
汇编语言字符串，大小写均可，如”mov eax,1” |
|

|
baseAddr |
长整数型 |
汇编指令所在的地址，用于计算相对地址 |
|

|
arch |
整数型 |
架构类型：
0: x86
1: arm
2: arm64 |
|

|
mode |
整数型 |
模式：
16: 16位
32: 32位
64: 64位 |
|

### 示例

```
[](#cb3-1)// x86 32位汇编转机器码
[](#cb3-2)char asm_code[] = "mov eax, 123";
[](#cb3-3)long result = Assemble(ola, asm_code, 0x10000000, 0, 32);
[](#cb3-4)if (result != 0) {
[](#cb3-5)    char* machine_code = (char*)result;
[](#cb3-6)    printf("机器码: %s\n", machine_code);
[](#cb3-7)    FreeStringPtr(ola, result);
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)// x86 64位汇编转机器码
[](#cb3-11)char asm_code_64[] = "mov rax, 456";
[](#cb3-12)long result = Assemble(ola, asm_code_64, 0x10000000, 0, 64);
[](#cb3-13)if (result != 0) {
[](#cb3-14)    char* machine_code = (char*)result;
[](#cb3-15)    printf("64位机器码: %s\n", machine_code);
[](#cb3-16)    FreeStringPtr(ola, result);
[](#cb3-17)}
[](#cb3-18)
[](#cb3-19)// ARM 32位汇编转机器码
[](#cb3-20)char arm_code[] = "mov r0, #123";
[](#cb3-21)long result = Assemble(ola, arm_code, 0x10000000, 1, 32);
[](#cb3-22)if (result != 0) {
[](#cb3-23)    char* machine_code = (char*)result;
[](#cb3-24)    printf("ARM机器码: %s\n", machine_code);
[](#cb3-25)    FreeStringPtr(ola, result);
[](#cb3-26)}
[](#cb3-27)
[](#cb3-28)// 复杂汇编指令转换
[](#cb3-29)char complex_asm[] = "push ebp\nmov ebp, esp\nsub esp, 16\nmov eax, [ebp+8]\npop ebp\nret";
[](#cb3-30)long result = Assemble(ola, complex_asm, 0x10000000, 0, 32);
[](#cb3-31)if (result != 0) {
[](#cb3-32)    char* machine_code = (char*)result;
[](#cb3-33)    printf("复杂指令机器码: %s\n", machine_code);
[](#cb3-34)    FreeStringPtr(ola, result);
[](#cb3-35)}
[](#cb3-36)
[](#cb3-37)// 使用相对地址的汇编指令
[](#cb3-38)char rel_asm[] = "call 0x10001000";
[](#cb3-39)long result = Assemble(ola, rel_asm, 0x10000000, 0, 32);
[](#cb3-40)if (result != 0) {
[](#cb3-41)    char* machine_code = (char*)result;
[](#cb3-42)    printf("相对地址机器码: %s\n", machine_code);
[](#cb3-43)    FreeStringPtr(ola, result);
[](#cb3-44)}
```

## 返回值

长整数型: - 成功返回机器码字符串的指针 - 失败返回0

## 注意事项

- 返回的字符串指针需要调用FreeStringPtr释放内存

- 支持的汇编语法取决于底层汇编器

- baseAddr参数用于计算相对地址，对于绝对地址指令可以设为0

- 不同架构和模式支持的指令集不同

- 建议在使用前验证汇编语法的正确性

- 机器码输出格式为16进制字符串，如”aa bb cc”

- 此函数适用于代码分析和逆向工程工具开发

---

## 注入

# 从URL注入DLL - InjectFromUrl

### 函数简介

从网络URL下载DLL文件并注入到指定窗口进程,支持远程注入场景。(部分模式文件会落盘)

### 接口名称

```
InjectFromUrl
```

### DLL调用

```
[](#cb2-1)int32_t InjectFromUrl(int64_t instance, int64_t hwnd, const char* url, int32_t type, int32_t bypassGuard)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 目标窗口句柄

- `url` (字符串): DLL文件的下载URL地址

- `type` (整型数): 注入类型,可选值:

1: 标准注入(CreateRemoteThread)

- 2: 驱动注入模式1

- 3: 驱动注入模式2

- 4: 驱动注入模式3

- `bypassGuard` (整型数): 是否绕过保护

0: 不绕过

- 1: 尝试绕过常见反注入保护

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 查找目标窗口
[](#cb3-5)int64_t hwnd = FindWindow(instance, "", "目标程序", "", 0);
[](#cb3-6)
[](#cb3-7)if (hwnd != 0) {
[](#cb3-8)    // 从URL下载并注入DLL
[](#cb3-9)    int32_t result = InjectFromUrl(
[](#cb3-10)        instance,
[](#cb3-11)        hwnd,
[](#cb3-12)        "https://example.com/dlls/inject.dll",
[](#cb3-13)        0,  // 标准注入
[](#cb3-14)        0   // 不绕过保护
[](#cb3-15)    );
[](#cb3-16)
[](#cb3-17)    if (result == 1) {
[](#cb3-18)        printf("从URL注入DLL成功\n");
[](#cb3-19)    } else {
[](#cb3-20)        printf("从URL注入DLL失败\n");
[](#cb3-21)    }
[](#cb3-22)
[](#cb3-23)    // 使用HTTPS下载并注入
[](#cb3-24)    result = InjectFromUrl(
[](#cb3-25)        instance,
[](#cb3-26)        hwnd,
[](#cb3-27)        "https://secure-server.com/modules/hook.dll",
[](#cb3-28)        1,  // APC注入
[](#cb3-29)        1   // 绕过保护
[](#cb3-30)    );
[](#cb3-31)}
[](#cb3-32)
[](#cb3-33)// 释放资源
[](#cb3-34)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数: - 1: 成功 - 0: 失败

### 注意事项

- URL必须可访问且指向有效的DLL文件

- 需要网络连接,下载可能需要一定时间

- 下载的DLL会临时保存到本地再进行注入

- 建议使用HTTPS协议确保传输安全

- 下载失败或DLL损坏会导致注入失败

- 防火墙或杀毒软件可能会拦截下载

- 下载的临时文件会在注入后清理

- 目标进程必须有足够的权限允许注入

- 不同注入类型的成功率和兼容性可能不同

- 32位进程只能注入32位DLL,64位进程只能注入64位DLL

- 注入系统进程或受保护进程需要管理员权限

- 某些网络环境可能不支持直接下载可执行文件

- 建议验证下载文件的完整性和来源安全性

---

# 从内存注入DLL -
InjectFromBuffer

### 函数简介

从内存缓冲区直接注入DLL到指定窗口进程,无需落地文件,隐蔽性最强。(部分模式文件会落盘)

### 接口名称

```
InjectFromBuffer
```

### DLL调用

```
[](#cb2-1)int32_t InjectFromBuffer(int64_t instance, int64_t hwnd, int64_t bufferAddr, int32_t bufferSize, int32_t type, int32_t bypassGuard)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 目标窗口句柄

- `bufferAddr` (长整型数): DLL数据在内存中的起始地址

- `bufferSize` (整型数): DLL数据的大小(字节)

- `type` (整型数): 注入类型,可选值:

1: 标准注入(CreateRemoteThread)

- 2: 驱动注入模式1

- 3: 驱动注入模式2

- 4: 驱动注入模式3

- `bypassGuard` (整型数): 是否绕过保护

0: 不绕过

- 1: 尝试绕过常见反注入保护

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 读取DLL文件到内存
[](#cb3-5)FILE* fp = fopen("C:\\MyDlls\\inject.dll", "rb");
[](#cb3-6)if (fp != NULL) {
[](#cb3-7)    // 获取文件大小
[](#cb3-8)    fseek(fp, 0, SEEK_END);
[](#cb3-9)    int32_t fileSize = ftell(fp);
[](#cb3-10)    fseek(fp, 0, SEEK_SET);
[](#cb3-11)
[](#cb3-12)    // 分配内存并读取文件
[](#cb3-13)    unsigned char* buffer = (unsigned char*)malloc(fileSize);
[](#cb3-14)    fread(buffer, 1, fileSize, fp);
[](#cb3-15)    fclose(fp);
[](#cb3-16)
[](#cb3-17)    // 查找目标窗口
[](#cb3-18)    int64_t hwnd = FindWindow(instance, "", "目标程序", "", 0);
[](#cb3-19)
[](#cb3-20)    if (hwnd != 0) {
[](#cb3-21)        // 从内存注入DLL
[](#cb3-22)        int32_t result = InjectFromBuffer(
[](#cb3-23)            instance,
[](#cb3-24)            hwnd,
[](#cb3-25)            (int64_t)buffer,
[](#cb3-26)            fileSize,
[](#cb3-27)            3,  // 手动映射注入(推荐用于内存注入)
[](#cb3-28)            1   // 绕过保护
[](#cb3-29)        );
[](#cb3-30)
[](#cb3-31)        if (result == 1) {
[](#cb3-32)            printf("从内存注入DLL成功\n");
[](#cb3-33)        } else {
[](#cb3-34)            printf("从内存注入DLL失败\n");
[](#cb3-35)        }
[](#cb3-36)    }
[](#cb3-37)
[](#cb3-38)    // 释放内存
[](#cb3-39)    free(buffer);
[](#cb3-40)}
[](#cb3-41)
[](#cb3-42)// 释放资源
[](#cb3-43)DestroyCOLAPlugInterFace(instance);
```

#### 高级示例 - 从资源加载并注入:

```
[](#cb4-1)// 从程序资源中加载DLL数据
[](#cb4-2)HRSRC hResource = FindResource(NULL, MAKEINTRESOURCE(IDR_DLL_DATA), RT_RCDATA);
[](#cb4-3)if (hResource) {
[](#cb4-4)    HGLOBAL hLoadedResource = LoadResource(NULL, hResource);
[](#cb4-5)    if (hLoadedResource) {
[](#cb4-6)        int64_t bufferAddr = (int64_t)LockResource(hLoadedResource);
[](#cb4-7)        int32_t bufferSize = SizeofResource(NULL, hResource);
[](#cb4-8)
[](#cb4-9)        int64_t hwnd = FindWindow(instance, "", "目标程序", "", 0);
[](#cb4-10)        if (hwnd != 0) {
[](#cb4-11)            // 从资源内存注入
[](#cb4-12)            int32_t result = InjectFromBuffer(
[](#cb4-13)                instance,
[](#cb4-14)                hwnd,
[](#cb4-15)                bufferAddr,
[](#cb4-16)                bufferSize,
[](#cb4-17)                3,  // 手动映射注入
[](#cb4-18)                1   // 绕过保护
[](#cb4-19)            );
[](#cb4-20)        }
[](#cb4-21)    }
[](#cb4-22)}
```

### 返回值

整型数: - 1: 成功 - 0: 失败

### 注意事项

- DLL数据必须完整且有效,缓冲区不能损坏

- 内存注入无需落地文件,隐蔽性最强

- 推荐使用手动映射注入(type=3)以获得最佳兼容性

- 标准注入(type=0)可能无法从内存加载

- 确保bufferAddr指向的内存在注入完成前保持有效

- 注入完成后可以立即释放bufferAddr指向的内存

- 目标进程必须有足够的权限允许注入

- 32位进程只能注入32位DLL,64位进程只能注入64位DLL

- 注入系统进程或受保护进程需要管理员权限

- 内存注入可以有效规避部分文件监控类反注入

- 某些杀毒软件的内存扫描仍可能检测到注入行为

- 建议对DLL数据进行加密,在注入前解密以提高隐蔽性

- bufferSize必须与实际DLL文件大小完全一致

---

# 注入DLL - Inject

### 函数简介

向指定窗口进程注入DLL文件,支持多种注入类型和绕过保护选项。

### 接口名称

```
Inject
```

### DLL调用

```
[](#cb2-1)int32_t Inject(int64_t instance, int64_t hwnd, const char* dll_path, int32_t type, int32_t bypassGuard)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 目标窗口句柄

- `dll_path` (字符串): DLL文件的完整路径

- `type` (整型数): 注入类型,可选值:

1: 标准注入(CreateRemoteThread)

- 2: 驱动注入模式1

- 3: 驱动注入模式2

- 4: 驱动注入模式3

- `bypassGuard` (整型数): 是否绕过保护

0: 不绕过

- 1: 尝试绕过常见反注入保护

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 查找目标窗口
[](#cb3-5)int64_t hwnd = FindWindow(instance, "", "目标程序", "", 0);
[](#cb3-6)
[](#cb3-7)if (hwnd != 0) {
[](#cb3-8)    // 使用标准注入方式
[](#cb3-9)    int32_t result = Inject(
[](#cb3-10)        instance,
[](#cb3-11)        hwnd,
[](#cb3-12)        "C:\\MyDlls\\inject.dll",
[](#cb3-13)        0,  // 标准注入
[](#cb3-14)        0   // 不绕过保护
[](#cb3-15)    );
[](#cb3-16)
[](#cb3-17)    if (result == 1) {
[](#cb3-18)        printf("DLL注入成功\n");
[](#cb3-19)    } else {
[](#cb3-20)        printf("DLL注入失败\n");
[](#cb3-21)    }
[](#cb3-22)
[](#cb3-23)    // 使用APC注入并绕过保护
[](#cb3-24)    result = Inject(
[](#cb3-25)        instance,
[](#cb3-26)        hwnd,
[](#cb3-27)        "C:\\MyDlls\\hook.dll",
[](#cb3-28)        1,  // APC注入
[](#cb3-29)        1   // 绕过保护
[](#cb3-30)    );
[](#cb3-31)}
[](#cb3-32)
[](#cb3-33)// 释放资源
[](#cb3-34)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数: - 1: 成功 - 0: 失败

### 注意事项

- DLL文件必须存在且路径正确

- 目标进程必须有足够的权限允许注入

- 不同注入类型的成功率和兼容性可能不同

- 标准注入(type=0)最稳定,但容易被检测

- 手动映射注入(type=3)隐蔽性最好,但兼容性较差

- 绕过保护选项可能无法对抗所有反注入机制

- 注入系统进程或受保护进程需要管理员权限

- 32位进程只能注入32位DLL,64位进程只能注入64位DLL

- 建议在注入前确认DLL的架构与目标进程匹配

- 注入失败可能导致目标进程崩溃,请谨慎使用

- 某些杀毒软件可能会拦截DLL注入操作

---

## 注册表

# 从文件恢复注册表 -
RegistryRestoreFromFile

### 函数简介

从.reg格式文件恢复注册表键,用于恢复之前的备份。

### 接口名称

```
RegistryRestoreFromFile
```

### DLL调用

```
[](#cb2-1)int32_t RegistryRestoreFromFile(int64_t instance, const char* filePath)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `filePath` (字符串): 备份文件路径(.reg格式)

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 从文件恢复注册表
[](#cb3-5)int32_t result = RegistryRestoreFromFile(
[](#cb3-6)    instance,
[](#cb3-7)    "C:\\Backup\\olaplug_config.reg"
[](#cb3-8));
[](#cb3-9)
[](#cb3-10)if (result == 1) {
[](#cb3-11)    printf("成功从文件恢复注册表\n");
[](#cb3-12)} else {
[](#cb3-13)    printf("恢复失败\n");
[](#cb3-14)}
[](#cb3-15)
[](#cb3-16)// 批量恢复多个配置
[](#cb3-17)const char* backupFiles[] = {
[](#cb3-18)    "C:\\Backup\\config1.reg",
[](#cb3-19)    "C:\\Backup\\config2.reg",
[](#cb3-20)    "C:\\Backup\\config3.reg"
[](#cb3-21)};
[](#cb3-22)
[](#cb3-23)for (int i = 0; i < 3; i++) {
[](#cb3-24)    result = RegistryRestoreFromFile(instance, backupFiles[i]);
[](#cb3-25)    if (result == 1) {
[](#cb3-26)        printf("成功恢复: %s\n", backupFiles[i]);
[](#cb3-27)    } else {
[](#cb3-28)        printf("恢复失败: %s\n", backupFiles[i]);
[](#cb3-29)    }
[](#cb3-30)}
[](#cb3-31)
[](#cb3-32)// 释放资源
[](#cb3-33)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数: - 1: 成功 - 0: 失败

### 注意事项

- 文件必须是标准.reg格式

- 恢复操作会覆盖现有的同名键和值

- 恢复系统级键可能需要管理员权限

- 建议在恢复前先备份当前配置

- 确保.reg文件来源可信,避免导入恶意配置

- 文件编码必须为UTF-16 LE或ANSI

- 恢复后可能需要重启应用程序或系统才能生效

---

# 关闭注册表键 -
RegistryCloseKey

### 函数简介

关闭注册表键句柄,释放系统资源。关闭后句柄失效,不可再使用。

### 接口名称

```
RegistryCloseKey
```

### DLL调用

```
[](#cb2-1)int32_t RegistryCloseKey(int64_t instance, int64_t key)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key` (长整型数): 注册表键句柄,由 [RegistryOpenKey](/注册表/打开注册表键%20-%20RegistryOpenKey.html)
或 [RegistryCreateKey](/注册表/创建注册表键%20-%20RegistryCreateKey.html)
返回

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 打开注册表键
[](#cb3-5)int64_t key = RegistryOpenKey(instance, 1, "Software\\Microsoft\\Windows");
[](#cb3-6)
[](#cb3-7)if (key != 0) {
[](#cb3-8)    // 执行操作...
[](#cb3-9)
[](#cb3-10)    // 关闭注册表键
[](#cb3-11)    int32_t result = RegistryCloseKey(instance, key);
[](#cb3-12)    if (result == 1) {
[](#cb3-13)        printf("成功关闭注册表键\n");
[](#cb3-14)    } else {
[](#cb3-15)        printf("关闭注册表键失败\n");
[](#cb3-16)    }
[](#cb3-17)}
[](#cb3-18)
[](#cb3-19)// 释放资源
[](#cb3-20)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数: - 1: 成功 - 0: 失败

### 注意事项

- 关闭后句柄失效,不可再使用

- 每个打开的注册表键都必须调用此函数关闭,避免资源泄漏

- 重复关闭同一个句柄可能导致失败

- 建议在程序退出前确保所有注册表键都已正确关闭

---

# 创建注册表键 -
RegistryCreateKey

### 函数简介

创建并打开注册表键,如果键已存在则直接打开。用于确保键存在的场景。

### 接口名称

```
RegistryCreateKey
```

### DLL调用

```
[](#cb2-1)int64_t RegistryCreateKey(int64_t instance, int32_t rootKey, const char* subKey)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `rootKey` (整型数): 根键类型,可选值如下:

0: HKEY_CLASSES_ROOT

- 1: HKEY_CURRENT_USER

- 2: HKEY_LOCAL_MACHINE

- 3: HKEY_USERS

- 4: HKEY_CURRENT_CONFIG

- `subKey` (字符串): 子键路径,例如 “Software\OLAPlug”

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建或打开注册表键
[](#cb3-5)int64_t key = RegistryCreateKey(instance, 1, "Software\\OLAPlug\\Config");
[](#cb3-6)
[](#cb3-7)if (key != 0) {
[](#cb3-8)    printf("成功创建/打开注册表键\n");
[](#cb3-9)
[](#cb3-10)    // 写入字符串值
[](#cb3-11)    RegistrySetString(instance, key, "AppName", "OLAPlug");
[](#cb3-12)
[](#cb3-13)    // 写入整型值
[](#cb3-14)    RegistrySetDword(instance, key, "Version", 100);
[](#cb3-15)
[](#cb3-16)    // 关闭注册表键
[](#cb3-17)    RegistryCloseKey(instance, key);
[](#cb3-18)} else {
[](#cb3-19)    printf("创建/打开注册表键失败\n");
[](#cb3-20)}
[](#cb3-21)
[](#cb3-22)// 释放资源
[](#cb3-23)DestroyCOLAPlugInterFace(instance);
```

### 返回值

长整型数: - 成功: 返回注册表键句柄(非0值) - 失败: 返回 0

### 注意事项

- 如果键已存在,则直接打开已有键,不会覆盖现有数据

- 使用完成后必须调用 [RegistryCloseKey](/注册表/关闭注册表键%20-%20RegistryCloseKey.html)
释放句柄

- 创建系统级键(如 HKEY_LOCAL_MACHINE 下)可能需要管理员权限

- 如果仅需打开已存在的键,建议使用 [RegistryOpenKey](/注册表/打开注册表键%20-%20RegistryOpenKey.html)

---

# 删除注册表值 -
RegistryDeleteValue

### 函数简介

删除指定名称的注册表值,此操作不可逆。

### 接口名称

```
RegistryDeleteValue
```

### DLL调用

```
[](#cb2-1)int32_t RegistryDeleteValue(int64_t instance, int64_t key, const char* valueName)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key` (长整型数): 注册表键句柄,由 [RegistryOpenKey](/注册表/打开注册表键%20-%20RegistryOpenKey.html)
或 [RegistryCreateKey](/注册表/创建注册表键%20-%20RegistryCreateKey.html)
返回

- `valueName` (字符串): 值名称

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 打开注册表键
[](#cb3-5)int64_t key = RegistryOpenKey(instance, 1, "Software\\OLAPlug\\Config");
[](#cb3-6)
[](#cb3-7)if (key != 0) {
[](#cb3-8)    // 删除临时配置值
[](#cb3-9)    int32_t result = RegistryDeleteValue(instance, key, "TempConfig");
[](#cb3-10)
[](#cb3-11)    if (result == 1) {
[](#cb3-12)        printf("成功删除注册表值\n");
[](#cb3-13)    } else {
[](#cb3-14)        printf("删除失败或值不存在\n");
[](#cb3-15)    }
[](#cb3-16)
[](#cb3-17)    // 删除多个临时值
[](#cb3-18)    const char* tempValues[] = {"Temp1", "Temp2", "Temp3"};
[](#cb3-19)    for (int i = 0; i < 3; i++) {
[](#cb3-20)        RegistryDeleteValue(instance, key, tempValues[i]);
[](#cb3-21)    }
[](#cb3-22)
[](#cb3-23)    // 关闭注册表键
[](#cb3-24)    RegistryCloseKey(instance, key);
[](#cb3-25)}
[](#cb3-26)
[](#cb3-27)// 释放资源
[](#cb3-28)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数: - 1: 成功或值不存在 - 0: 失败

### 注意事项

- 删除操作不可逆,建议在删除前备份重要数据

- 如果值不存在,函数仍返回成功(1)

- 不会删除注册表键本身,仅删除键下的值

- 删除系统关键值可能导致系统不稳定

- 建议在删除前确认值确实不再需要

---

# 删除注册表键 -
RegistryDeleteKey

### 函数简介

删除指定的注册表键,支持递归删除子键。此操作不可逆,建议谨慎使用。

### 接口名称

```
RegistryDeleteKey
```

### DLL调用

```
[](#cb2-1)int32_t RegistryDeleteKey(int64_t instance, int32_t rootKey, const char* subKey, int32_t recursive)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `rootKey` (整型数): 根键类型,可选值如下:

0: HKEY_CLASSES_ROOT

- 1: HKEY_CURRENT_USER

- 2: HKEY_LOCAL_MACHINE

- 3: HKEY_USERS

- 4: HKEY_CURRENT_CONFIG

- `subKey` (字符串): 子键路径

- `recursive` (整型数): 是否递归删除子键

1: 递归删除所有子键

- 0: 仅删除当前键(当前键必须没有子键)

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 检查键是否存在
[](#cb3-5)if (RegistryKeyExists(instance, 1, "Software\\OLAPlug\\TempData")) {
[](#cb3-6)    // 非递归删除(仅当没有子键时成功)
[](#cb3-7)    int32_t result = RegistryDeleteKey(instance, 1, "Software\\OLAPlug\\TempData", 0);
[](#cb3-8)
[](#cb3-9)    if (result == 1) {
[](#cb3-10)        printf("成功删除注册表键\n");
[](#cb3-11)    } else {
[](#cb3-12)        printf("删除失败,可能存在子键\n");
[](#cb3-13)
[](#cb3-14)        // 递归删除
[](#cb3-15)        result = RegistryDeleteKey(instance, 1, "Software\\OLAPlug\\TempData", 1);
[](#cb3-16)        if (result == 1) {
[](#cb3-17)            printf("递归删除成功\n");
[](#cb3-18)        }
[](#cb3-19)    }
[](#cb3-20)}
[](#cb3-21)
[](#cb3-22)// 释放资源
[](#cb3-23)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数: - 1: 成功 - 0: 失败

### 注意事项

- 删除操作不可逆,建议在删除前备份重要数据

- 递归删除会删除所有子键和值,使用时务必谨慎

- 删除系统关键键可能导致系统不稳定,避免误删系统配置

- 建议在删除前使用 [RegistryBackupToFile](/注册表/备份注册表到文件%20-%20RegistryBackupToFile.html)
进行备份

- 删除 HKEY_LOCAL_MACHINE 下的键可能需要管理员权限

- 如果键正在被其他程序使用,删除可能失败

---

# 判断注册表键是否存在 -
RegistryKeyExists

### 函数简介

判断指定的注册表键是否存在,用于在操作前进行检查。

### 接口名称

```
RegistryKeyExists
```

### DLL调用

```
[](#cb2-1)int32_t RegistryKeyExists(int64_t instance, int32_t rootKey, const char* subKey)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `rootKey` (整型数): 根键类型,可选值如下:

0: HKEY_CLASSES_ROOT

- 1: HKEY_CURRENT_USER

- 2: HKEY_LOCAL_MACHINE

- 3: HKEY_USERS

- 4: HKEY_CURRENT_CONFIG

- `subKey` (字符串): 子键路径

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 检查注册表键是否存在
[](#cb3-5)int32_t exists = RegistryKeyExists(instance, 1, "Software\\OLAPlug");
[](#cb3-6)
[](#cb3-7)if (exists == 1) {
[](#cb3-8)    printf("注册表键存在\n");
[](#cb3-9)    // 打开键进行操作
[](#cb3-10)    int64_t key = RegistryOpenKey(instance, 1, "Software\\OLAPlug");
[](#cb3-11)    // ...
[](#cb3-12)    RegistryCloseKey(instance, key);
[](#cb3-13)} else {
[](#cb3-14)    printf("注册表键不存在,需要创建\n");
[](#cb3-15)    // 创建键
[](#cb3-16)    int64_t key = RegistryCreateKey(instance, 1, "Software\\OLAPlug");
[](#cb3-17)    // ...
[](#cb3-18)    RegistryCloseKey(instance, key);
[](#cb3-19)}
[](#cb3-20)
[](#cb3-21)// 释放资源
[](#cb3-22)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数: - 1: 存在 - 0: 不存在

### 注意事项

- 此函数仅判断键是否存在,不打开键

- 可用于在创建或打开键之前进行检查

- 对于系统关键键,建议先检查存在性再操作

---

# 备份注册表到文件 -
RegistryBackupToFile

### 函数简介

备份注册表键到.reg格式文件,可以使用regedit导入恢复。

### 接口名称

```
RegistryBackupToFile
```

### DLL调用

```
[](#cb2-1)int32_t RegistryBackupToFile(int64_t instance, int32_t rootKey, const char* subKey, const char* filePath)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `rootKey` (整型数): 根键类型,可选值如下:

0: HKEY_CLASSES_ROOT

- 1: HKEY_CURRENT_USER

- 2: HKEY_LOCAL_MACHINE

- 3: HKEY_USERS

- 4: HKEY_CURRENT_CONFIG

- `subKey` (字符串): 子键路径

- `filePath` (字符串): 备份文件路径(.reg格式)

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 备份OLAPlug配置
[](#cb3-5)int32_t result = RegistryBackupToFile(
[](#cb3-6)    instance,
[](#cb3-7)    1,  // HKEY_CURRENT_USER
[](#cb3-8)    "Software\\OLAPlug",
[](#cb3-9)    "C:\\Backup\\olaplug_config.reg"
[](#cb3-10));
[](#cb3-11)
[](#cb3-12)if (result == 1) {
[](#cb3-13)    printf("成功备份注册表到文件\n");
[](#cb3-14)} else {
[](#cb3-15)    printf("备份失败\n");
[](#cb3-16)}
[](#cb3-17)
[](#cb3-18)// 备份系统关键配置(需要管理员权限)
[](#cb3-19)result = RegistryBackupToFile(
[](#cb3-20)    instance,
[](#cb3-21)    2,  // HKEY_LOCAL_MACHINE
[](#cb3-22)    "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall",
[](#cb3-23)    "C:\\Backup\\installed_programs.reg"
[](#cb3-24));
[](#cb3-25)
[](#cb3-26)// 释放资源
[](#cb3-27)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数: - 1: 成功 - 0: 失败

### 注意事项

- 文件将以标准.reg格式保存,可以使用regedit导入

- 备份文件包含指定键及其所有子键和值

- 建议在修改重要配置前先备份

- 备份系统级键可能需要管理员权限

- 确保目标文件路径可写

- 备份文件为文本格式,可以用文本编辑器查看

- 文件编码为UTF-16 LE(Windows标准.reg格式)

---

# 打开注册表键 -
RegistryOpenKey

### 函数简介

打开已存在的注册表键，用于后续读取或修改操作。仅在键已存在时返回有效句柄。

### 接口名称

```
RegistryOpenKey
```

### DLL调用

```
[](#cb2-1)int64_t RegistryOpenKey(int64_t instance, int32_t rootKey, const char* subKey)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `rootKey` (整型数): 根键类型,可选值如下:

0: HKEY_CLASSES_ROOT

- 1: HKEY_CURRENT_USER

- 2: HKEY_LOCAL_MACHINE

- 3: HKEY_USERS

- 4: HKEY_CURRENT_CONFIG

- `subKey` (字符串): 子键路径,例如
“Software\Microsoft\Windows”

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 打开注册表键
[](#cb3-5)int64_t key = RegistryOpenKey(instance, 1, "Software\\Microsoft\\Windows\\CurrentVersion");
[](#cb3-6)
[](#cb3-7)if (key != 0) {
[](#cb3-8)    printf("成功打开注册表键\n");
[](#cb3-9)
[](#cb3-10)    // ... 执行读写操作 ...
[](#cb3-11)
[](#cb3-12)    // 关闭注册表键
[](#cb3-13)    RegistryCloseKey(instance, key);
[](#cb3-14)} else {
[](#cb3-15)    printf("打开注册表键失败\n");
[](#cb3-16)}
[](#cb3-17)
[](#cb3-18)// 释放资源
[](#cb3-19)DestroyCOLAPlugInterFace(instance);
```

### 返回值

长整型数: - 成功: 返回注册表键句柄(非0值) - 失败: 返回 0

### 注意事项

- 仅在键已存在时返回有效句柄,如果键不存在将返回 0

- 使用完成后必须调用 [RegistryCloseKey](/注册表/关闭注册表键%20-%20RegistryCloseKey.html)
释放句柄

- 建议在操作敏感系统键时谨慎处理,避免误操作

- 如果需要在键不存在时自动创建,请使用 [RegistryCreateKey](/注册表/创建注册表键%20-%20RegistryCreateKey.html)

---

# 搜索注册表键 -
RegistrySearchKeys

### 函数简介

在注册表中搜索匹配指定模式的键,支持通配符和递归搜索。

### 接口名称

```
RegistrySearchKeys
```

### DLL调用

```
[](#cb2-1)int64_t RegistrySearchKeys(int64_t instance, int32_t rootKey, const char* searchPath, const char* searchPattern, int32_t recursive)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `rootKey` (整型数): 根键类型

- `searchPath` (字符串): 搜索起始路径

- `searchPattern` (字符串): 搜索模式,支持通配符 * 和 ?

`*` 匹配任意多个字符

- `?` 匹配单个字符

- `recursive` (整型数): 是否递归搜索

1: 递归搜索所有子键

- 0: 仅搜索当前层级

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 搜索所有OLA相关的键(递归)
[](#cb3-5)int64_t resultPtr = RegistrySearchKeys(
[](#cb3-6)    instance,
[](#cb3-7)    1,  // HKEY_CURRENT_USER
[](#cb3-8)    "Software",
[](#cb3-9)    "*OLA*",
[](#cb3-10)    1   // 递归搜索
[](#cb3-11));
[](#cb3-12)
[](#cb3-13)if (resultPtr != 0) {
[](#cb3-14)    const char* json = (const char*)resultPtr;
[](#cb3-15)    printf("搜索结果: %s\n", json);
[](#cb3-16)    // 输出示例: ["Software\\OLAPlug","Software\\OLAPlug\\Config"]
[](#cb3-17)
[](#cb3-18)    // 释放字符串内存
[](#cb3-19)    FreeStringPtr(instance, resultPtr);
[](#cb3-20)}
[](#cb3-21)
[](#cb3-22)// 搜索特定版本的软件
[](#cb3-23)resultPtr = RegistrySearchKeys(
[](#cb3-24)    instance,
[](#cb3-25)    2,  // HKEY_LOCAL_MACHINE
[](#cb3-26)    "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall",
[](#cb3-27)    "*2.0*",
[](#cb3-28)    0   // 不递归
[](#cb3-29));
[](#cb3-30)
[](#cb3-31)if (resultPtr != 0) {
[](#cb3-32)    printf("找到的软件: %s\n", (const char*)resultPtr);
[](#cb3-33)    FreeStringPtr(instance, resultPtr);
[](#cb3-34)}
[](#cb3-35)
[](#cb3-36)// 释放资源
[](#cb3-37)DestroyCOLAPlugInterFace(instance);
```

### 返回值

长整型数: - 成功: 返回JSON数组字符串句柄,包含匹配的键路径,例如
`["path1","path2"]` - 失败或无匹配: 返回 0 或空数组
`[]`

### 注意事项

- 返回的字符串句柄需使用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放

- 搜索模式不区分大小写

- 递归搜索可能耗时较长,建议缩小搜索范围

- 搜索系统关键路径时要谨慎,避免影响性能

- 返回的路径为完整的子键路径

- `*` 可以匹配路径分隔符,`?`
只匹配单个非分隔符字符

---

# 枚举值名称 -
RegistryEnumValues

### 函数简介

枚举当前注册表键下的所有值名称,返回JSON数组格式。

### 接口名称

```
RegistryEnumValues
```

### DLL调用

```
[](#cb2-1)int64_t RegistryEnumValues(int64_t instance, int64_t key)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key` (长整型数): 注册表键句柄,由 [RegistryOpenKey](/注册表/打开注册表键%20-%20RegistryOpenKey.html)
或 [RegistryCreateKey](/注册表/创建注册表键%20-%20RegistryCreateKey.html)
返回

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 打开注册表键
[](#cb3-5)int64_t key = RegistryOpenKey(instance, 1, "Software\\OLAPlug\\Config");
[](#cb3-6)
[](#cb3-7)if (key != 0) {
[](#cb3-8)    // 枚举所有值名称
[](#cb3-9)    int64_t jsonPtr = RegistryEnumValues(instance, key);
[](#cb3-10)
[](#cb3-11)    if (jsonPtr != 0) {
[](#cb3-12)        const char* json = (const char*)jsonPtr;
[](#cb3-13)        printf("值名称列表: %s\n", json);
[](#cb3-14)        // 输出示例: ["AppName","Version","Enabled","InstallPath"]
[](#cb3-15)
[](#cb3-16)        // 可以遍历每个值名称并读取其值
[](#cb3-17)        // 使用JSON解析库解析返回的数组
[](#cb3-18)
[](#cb3-19)        // 释放字符串内存
[](#cb3-20)        FreeStringPtr(instance, jsonPtr);
[](#cb3-21)    } else {
[](#cb3-22)        printf("没有值或枚举失败\n");
[](#cb3-23)    }
[](#cb3-24)
[](#cb3-25)    // 关闭注册表键
[](#cb3-26)    RegistryCloseKey(instance, key);
[](#cb3-27)}
[](#cb3-28)
[](#cb3-29)// 释放资源
[](#cb3-30)DestroyCOLAPlugInterFace(instance);
```

### 返回值

长整型数: - 成功: 返回包含所有值名称的JSON数组字符串句柄,例如
`["Value1","Value2"]` - 失败或无值: 返回 0 或空数组
`[]`

### 注意事项

- 返回的字符串句柄需使用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放

- 返回的是JSON数组格式,需要解析后使用

- 默认值(空名称)可能显示为空字符串 `""`

- 如果键下没有值,返回空数组 `[]`

- 值名称按字母顺序排列

- 不包含值的类型和数据,仅包含名称

---

# 枚举子键 -
RegistryEnumSubKeys

### 函数简介

枚举当前注册表键下的所有子键名称,返回JSON数组格式。

### 接口名称

```
RegistryEnumSubKeys
```

### DLL调用

```
[](#cb2-1)int64_t RegistryEnumSubKeys(int64_t instance, int64_t key)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key` (长整型数): 注册表键句柄,由 [RegistryOpenKey](/注册表/打开注册表键%20-%20RegistryOpenKey.html)
或 [RegistryCreateKey](/注册表/创建注册表键%20-%20RegistryCreateKey.html)
返回

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 打开注册表键
[](#cb3-5)int64_t key = RegistryOpenKey(instance, 1, "Software\\Microsoft\\Windows\\CurrentVersion");
[](#cb3-6)
[](#cb3-7)if (key != 0) {
[](#cb3-8)    // 枚举所有子键
[](#cb3-9)    int64_t jsonPtr = RegistryEnumSubKeys(instance, key);
[](#cb3-10)
[](#cb3-11)    if (jsonPtr != 0) {
[](#cb3-12)        const char* json = (const char*)jsonPtr;
[](#cb3-13)        printf("子键列表: %s\n", json);
[](#cb3-14)        // 输出示例: ["Uninstall","Run","RunOnce","Explorer"]
[](#cb3-15)
[](#cb3-16)        // 解析JSON数组,遍历每个子键
[](#cb3-17)        // 可以使用JSON解析库处理返回的数据
[](#cb3-18)
[](#cb3-19)        // 释放字符串内存
[](#cb3-20)        FreeStringPtr(instance, jsonPtr);
[](#cb3-21)    } else {
[](#cb3-22)        printf("没有子键或枚举失败\n");
[](#cb3-23)    }
[](#cb3-24)
[](#cb3-25)    // 关闭注册表键
[](#cb3-26)    RegistryCloseKey(instance, key);
[](#cb3-27)}
[](#cb3-28)
[](#cb3-29)// 释放资源
[](#cb3-30)DestroyCOLAPlugInterFace(instance);
```

### 返回值

长整型数: - 成功: 返回包含所有子键名称的JSON数组字符串句柄,例如
`["SubKey1","SubKey2"]` - 失败或无子键: 返回 0 或空数组
`[]`

### 注意事项

- 返回的字符串句柄需使用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放

- 返回的是JSON数组格式,需要解析后使用

- 仅返回直接子键名称,不包含子键的子键

- 如果键下没有子键,返回空数组 `[]`

- 子键名称按字母顺序排列

---

# 比较注册表键 -
RegistryCompareKeys

### 函数简介

比较两个注册表键的内容,返回比较结果的JSON字符串。

### 接口名称

```
RegistryCompareKeys
```

### DLL调用

```
[](#cb2-1)int64_t RegistryCompareKeys(int64_t instance, int32_t rootKey1, const char* subKey1, int32_t rootKey2, const char* subKey2)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `rootKey1` (整型数): 第一个根键类型

- `subKey1` (字符串): 第一个子键路径

- `rootKey2` (整型数): 第二个根键类型

- `subKey2` (字符串): 第二个子键路径

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 比较两个配置键
[](#cb3-5)int64_t resultPtr = RegistryCompareKeys(
[](#cb3-6)    instance,
[](#cb3-7)    1, "Software\\OLAPlug\\Config",  // HKEY_CURRENT_USER
[](#cb3-8)    1, "Software\\OLAPlug\\ConfigBackup"
[](#cb3-9));
[](#cb3-10)
[](#cb3-11)if (resultPtr != 0) {
[](#cb3-12)    const char* json = (const char*)resultPtr;
[](#cb3-13)    printf("比较结果: %s\n", json);
[](#cb3-14)
[](#cb3-15)    // JSON格式示例:
[](#cb3-16)    // {
[](#cb3-17)    //     "equal": false,
[](#cb3-18)    //     "differences": [
[](#cb3-19)    //         {"type": "value_changed", "name": "Version", "value1": "1.0", "value2": "1.1"},
[](#cb3-20)    //         {"type": "value_added", "name": "NewFeature", "value2": "enabled"},
[](#cb3-21)    //         {"type": "value_removed", "name": "OldSetting"}
[](#cb3-22)    //     ]
[](#cb3-23)    // }
[](#cb3-24)
[](#cb3-25)    // 释放字符串内存
[](#cb3-26)    FreeStringPtr(instance, resultPtr);
[](#cb3-27)} else {
[](#cb3-28)    printf("比较失败\n");
[](#cb3-29)}
[](#cb3-30)
[](#cb3-31)// 释放资源
[](#cb3-32)DestroyCOLAPlugInterFace(instance);
```

### 返回值

长整型数: - 成功: 返回JSON字符串句柄,包含比较结果 - 失败: 返回 0

返回的JSON结构:

```
[](#cb4-1){
[](#cb4-2)    "equal": true/false,
[](#cb4-3)    "differences": [
[](#cb4-4)        {
[](#cb4-5)            "type": "value_changed|value_added|value_removed|subkey_changed",
[](#cb4-6)            "name": "值或子键名称",
[](#cb4-7)            "value1": "第一个键的值",
[](#cb4-8)            "value2": "第二个键的值"
[](#cb4-9)        }
[](#cb4-10)    ]
[](#cb4-11)}
```

### 注意事项

- 返回的字符串句柄需使用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放

- 比较结果包含值的差异和子键的差异

- 如果两个键完全相同,`equal` 字段为
`true`,`differences` 数组为空

- 可用于配置迁移前的验证

- 比较操作不会修改任何注册表内容

---

# 获取Windows版本信息
- RegistryGetWindowsVersion

### 函数简介

获取Windows系统版本信息,返回包含版本详情的JSON对象。

### 接口名称

```
RegistryGetWindowsVersion
```

### DLL调用

```
[](#cb2-1)int64_t RegistryGetWindowsVersion(int64_t instance)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 获取Windows版本信息
[](#cb3-5)int64_t jsonPtr = RegistryGetWindowsVersion(instance);
[](#cb3-6)
[](#cb3-7)if (jsonPtr != 0) {
[](#cb3-8)    const char* json = (const char*)jsonPtr;
[](#cb3-9)    printf("Windows版本信息: %s\n", json);
[](#cb3-10)
[](#cb3-11)    // JSON格式示例:
[](#cb3-12)    // {
[](#cb3-13)    //     "productName": "Windows 10 Pro",
[](#cb3-14)    //     "currentVersion": "10.0",
[](#cb3-15)    //     "currentBuild": "19045",
[](#cb3-16)    //     "releaseId": "2009",
[](#cb3-17)    //     "displayVersion": "22H2",
[](#cb3-18)    //     "buildBranch": "vb_release",
[](#cb3-19)    //     "ubr": 2006,
[](#cb3-20)    //     "installDate": 1577836800,
[](#cb3-21)    //     "registeredOwner": "User",
[](#cb3-22)    //     "registeredOrganization": "Organization"
[](#cb3-23)    // }
[](#cb3-24)
[](#cb3-25)    // 可以根据版本信息判断系统兼容性
[](#cb3-26)    // 或者显示系统信息给用户
[](#cb3-27)
[](#cb3-28)    // 释放字符串内存
[](#cb3-29)    FreeStringPtr(instance, jsonPtr);
[](#cb3-30)} else {
[](#cb3-31)    printf("获取版本信息失败\n");
[](#cb3-32)}
[](#cb3-33)
[](#cb3-34)// 释放资源
[](#cb3-35)DestroyCOLAPlugInterFace(instance);
```

### 返回值

长整型数: - 成功: 返回JSON对象字符串句柄,包含Windows版本信息 - 失败:
返回 0

返回的JSON对象包含以下字段: - `productName`: 产品名称(如
“Windows 10 Pro”) - `currentVersion`: 主版本号(如 “10.0”) -
`currentBuild`: 内部版本号(如 “19045”) -
`releaseId`: 发布版本标识(如 “2009”) -
`displayVersion`: 显示版本(如 “22H2”) -
`buildBranch`: 构建分支 - `ubr`: Update Build
Revision - `installDate`: 安装日期(Unix时间戳) -
`registeredOwner`: 注册所有者 -
`registeredOrganization`: 注册组织(可选)

### 注意事项

- 返回的字符串句柄需使用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放

- 版本信息从注册表
`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion`
读取

- 部分字段在某些Windows版本中可能不存在

- 可用于判断系统版本兼容性

- `currentVersion` 在Windows 10及以后都显示为
“10.0”,需要结合 `currentBuild` 判断具体版本

- Windows 11的 `currentBuild` 为 22000 或更高

---

# 获取已安装软件列表
- RegistryGetInstalledSoftware

### 函数简介

获取系统已安装软件列表,返回包含软件信息的JSON数组。该函数会同时扫描32位和64位软件列表。

### 接口名称

```
RegistryGetInstalledSoftware
```

### DLL调用

```
[](#cb2-1)int64_t RegistryGetInstalledSoftware(int64_t instance)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 获取已安装软件列表
[](#cb3-5)int64_t jsonPtr = RegistryGetInstalledSoftware(instance);
[](#cb3-6)
[](#cb3-7)if (jsonPtr != 0) {
[](#cb3-8)    const char* json = (const char*)jsonPtr;
[](#cb3-9)    printf("已安装软件列表: %s\n", json);
[](#cb3-10)
[](#cb3-11)    // JSON格式示例:
[](#cb3-12)    // [
[](#cb3-13)    //     {
[](#cb3-14)    //         "name": "Microsoft Office",
[](#cb3-15)    //         "version": "16.0.5134.1000",
[](#cb3-16)    //         "publisher": "Microsoft Corporation",
[](#cb3-17)    //         "installDate": "20230101",
[](#cb3-18)    //         "installLocation": "C:\\Program Files\\Microsoft Office",
[](#cb3-19)    //         "uninstallString": "C:\\Program Files\\Microsoft Office\\setup.exe /uninstall"
[](#cb3-20)    //     },
[](#cb3-21)    //     {
[](#cb3-22)    //         "name": "OLAPlug",
[](#cb3-23)    //         "version": "1.0.0",
[](#cb3-24)    //         "publisher": "OLA",
[](#cb3-25)    //         "installDate": "20240101"
[](#cb3-26)    //     }
[](#cb3-27)    // ]
[](#cb3-28)
[](#cb3-29)    // 可以使用JSON解析库处理返回的数据
[](#cb3-30)    // 例如统计软件数量、搜索特定软件等
[](#cb3-31)
[](#cb3-32)    // 释放字符串内存
[](#cb3-33)    FreeStringPtr(instance, jsonPtr);
[](#cb3-34)} else {
[](#cb3-35)    printf("获取软件列表失败\n");
[](#cb3-36)}
[](#cb3-37)
[](#cb3-38)// 释放资源
[](#cb3-39)DestroyCOLAPlugInterFace(instance);
```

### 返回值

长整型数: - 成功: 返回JSON数组字符串句柄,包含软件信息 - 失败: 返回
0

返回的JSON数组中每个软件对象包含以下字段: - `name`:
软件名称 - `version`: 版本号 - `publisher`: 发行商
- `installDate`: 安装日期(YYYYMMDD格式) -
`installLocation`: 安装位置(可选) -
`uninstallString`: 卸载命令(可选)

### 注意事项

- 返回的字符串句柄需使用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放

- 该函数会同时扫描32位和64位软件列表

- 扫描过程可能耗时较长,建议在后台线程执行

- 某些便携软件可能不会出现在列表中

- 返回的信息取决于软件在注册表中记录的内容

- 部分字段可能为空,取决于软件的安装信息完整性

- 列表包含用户级和系统级安装的软件

---

# 获取环境变量 -
RegistryGetEnvironmentVariable

### 函数简介

获取环境变量的值,支持读取用户级和系统级环境变量。

### 接口名称

```
RegistryGetEnvironmentVariable
```

### DLL调用

```
[](#cb2-1)int64_t RegistryGetEnvironmentVariable(int64_t instance, const char* name, int32_t systemWide)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `name` (字符串): 环境变量名称

- `systemWide` (整型数): 是否从系统级环境变量读取

1: 系统级

- 0: 当前用户级

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 获取用户级环境变量
[](#cb3-5)int64_t valuePtr = RegistryGetEnvironmentVariable(instance, "OLA_HOME", 0);
[](#cb3-6)if (valuePtr != 0) {
[](#cb3-7)    printf("OLA_HOME: %s\n", (const char*)valuePtr);
[](#cb3-8)    FreeStringPtr(instance, valuePtr);
[](#cb3-9)} else {
[](#cb3-10)    printf("OLA_HOME环境变量不存在\n");
[](#cb3-11)}
[](#cb3-12)
[](#cb3-13)// 获取系统级PATH
[](#cb3-14)valuePtr = RegistryGetEnvironmentVariable(instance, "PATH", 1);
[](#cb3-15)if (valuePtr != 0) {
[](#cb3-16)    printf("系统PATH: %s\n", (const char*)valuePtr);
[](#cb3-17)    FreeStringPtr(instance, valuePtr);
[](#cb3-18)}
[](#cb3-19)
[](#cb3-20)// 获取常见系统环境变量
[](#cb3-21)const char* commonVars[] = {"TEMP", "TMP", "USERPROFILE", "SYSTEMROOT"};
[](#cb3-22)for (int i = 0; i < 4; i++) {
[](#cb3-23)    valuePtr = RegistryGetEnvironmentVariable(instance, commonVars[i], 0);
[](#cb3-24)    if (valuePtr != 0) {
[](#cb3-25)        printf("%s: %s\n", commonVars[i], (const char*)valuePtr);
[](#cb3-26)        FreeStringPtr(instance, valuePtr);
[](#cb3-27)    }
[](#cb3-28)}
[](#cb3-29)
[](#cb3-30)// 释放资源
[](#cb3-31)DestroyCOLAPlugInterFace(instance);
```

### 返回值

长整型数: - 成功: 返回环境变量值的字符串句柄 - 失败或不存在: 返回
0

### 注意事项

- 返回的字符串句柄需使用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放

- 环境变量名称不区分大小写

- 系统级环境变量存储在 HKEY_LOCAL_MACHINEManager

- 用户级环境变量存储在 HKEY_CURRENT_USER

- 返回 0 表示环境变量不存在或读取失败

---

# 获取用户注册表路径
- RegistryGetUserRegistryPath

### 函数简介

获取用户配置相关的注册表路径,用于访问用户特定的系统配置。

### 接口名称

```
RegistryGetUserRegistryPath
```

### DLL调用

```
[](#cb2-1)int64_t RegistryGetUserRegistryPath(int64_t instance)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 获取用户注册表路径
[](#cb3-5)int64_t pathPtr = RegistryGetUserRegistryPath(instance);
[](#cb3-6)
[](#cb3-7)if (pathPtr != 0) {
[](#cb3-8)    const char* path = (const char*)pathPtr;
[](#cb3-9)    printf("用户注册表路径: %s\n", path);
[](#cb3-10)    // 示例输出: Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders
[](#cb3-11)
[](#cb3-12)    // 使用此路径打开注册表键
[](#cb3-13)    int64_t key = RegistryOpenKey(instance, 1, path); // 1 = HKEY_CURRENT_USER
[](#cb3-14)    if (key != 0) {
[](#cb3-15)        // 读取用户配置...
[](#cb3-16)        RegistryCloseKey(instance, key);
[](#cb3-17)    }
[](#cb3-18)
[](#cb3-19)    // 释放字符串内存
[](#cb3-20)    FreeStringPtr(instance, pathPtr);
[](#cb3-21)}
[](#cb3-22)
[](#cb3-23)// 释放资源
[](#cb3-24)DestroyCOLAPlugInterFace(instance);
```

### 返回值

长整型数: - 成功: 返回注册表路径字符串句柄 - 失败: 返回 0

### 注意事项

- 返回的字符串句柄需使用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放

- 返回的路径通常指向用户Shell文件夹配置

- 该路径下包含桌面、文档、下载等用户文件夹的位置信息

- 路径相对于 HKEY_CURRENT_USER 根键

---

# 获取系统注册表路径
- RegistryGetSystemRegistryPath

### 函数简介

获取系统配置相关的注册表路径,用于访问系统级配置信息。

### 接口名称

```
RegistryGetSystemRegistryPath
```

### DLL调用

```
[](#cb2-1)int64_t RegistryGetSystemRegistryPath(int64_t instance)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 获取系统注册表路径
[](#cb3-5)int64_t pathPtr = RegistryGetSystemRegistryPath(instance);
[](#cb3-6)
[](#cb3-7)if (pathPtr != 0) {
[](#cb3-8)    const char* path = (const char*)pathPtr;
[](#cb3-9)    printf("系统注册表路径: %s\n", path);
[](#cb3-10)    // 示例输出: Software\Microsoft\Windows\CurrentVersion
[](#cb3-11)
[](#cb3-12)    // 使用此路径打开注册表键
[](#cb3-13)    int64_t key = RegistryOpenKey(instance, 2, path); // 2 = HKEY_LOCAL_MACHINE
[](#cb3-14)    if (key != 0) {
[](#cb3-15)        // 读取系统配置...
[](#cb3-16)        RegistryCloseKey(instance, key);
[](#cb3-17)    }
[](#cb3-18)
[](#cb3-19)    // 释放字符串内存
[](#cb3-20)    FreeStringPtr(instance, pathPtr);
[](#cb3-21)}
[](#cb3-22)
[](#cb3-23)// 释放资源
[](#cb3-24)DestroyCOLAPlugInterFace(instance);
```

### 返回值

长整型数: - 成功: 返回注册表路径字符串句柄 - 失败: 返回 0

### 注意事项

- 返回的字符串句柄需使用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放

- 返回的路径通常指向Windows CurrentVersion配置

- 该路径下包含系统版本、安装路径、卸载信息等

- 路径相对于 HKEY_LOCAL_MACHINE 根键

- 访问此路径下的某些键可能需要管理员权限

---

# 设置32位整型值 -
RegistrySetDword

### 函数简介

设置32位整型的注册表值(REG_DWORD),用于存储数值型配置。

### 接口名称

```
RegistrySetDword
```

### DLL调用

```
[](#cb2-1)int32_t RegistrySetDword(int64_t instance, int64_t key, const char* valueName, int32_t value)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key` (长整型数): 注册表键句柄,由 [RegistryOpenKey](/注册表/打开注册表键%20-%20RegistryOpenKey.html)
或 [RegistryCreateKey](/注册表/创建注册表键%20-%20RegistryCreateKey.html)
返回

- `valueName` (字符串): 值名称

- `value` (整型数): 要写入的32位整型值

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建或打开注册表键
[](#cb3-5)int64_t key = RegistryCreateKey(instance, 1, "Software\\OLAPlug\\Config");
[](#cb3-6)
[](#cb3-7)if (key != 0) {
[](#cb3-8)    // 设置版本号
[](#cb3-9)    int32_t result = RegistrySetDword(instance, key, "Version", 100);
[](#cb3-10)    if (result == 1) {
[](#cb3-11)        printf("成功设置版本号\n");
[](#cb3-12)    }
[](#cb3-13)
[](#cb3-14)    // 设置最大连接数
[](#cb3-15)    result = RegistrySetDword(instance, key, "MaxConnections", 1000);
[](#cb3-16)
[](#cb3-17)    // 设置启用标志(0或1)
[](#cb3-18)    result = RegistrySetDword(instance, key, "Enabled", 1);
[](#cb3-19)
[](#cb3-20)    // 关闭注册表键
[](#cb3-21)    RegistryCloseKey(instance, key);
[](#cb3-22)}
[](#cb3-23)
[](#cb3-24)// 释放资源
[](#cb3-25)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数: - 1: 成功 - 0: 失败

### 注意事项

- 如果值名称已存在,将覆盖原有值

- REG_DWORD 类型为32位无符号整数,范围为 0 到 4,294,967,295

- 负数会被解释为无符号整数的补码形式

- 常用于存储版本号、标志位、计数器等数值配置

---

# 设置64位整型值 -
RegistrySetQword

### 函数简介

设置64位整型的注册表值(REG_QWORD),用于存储大数值型配置。

### 接口名称

```
RegistrySetQword
```

### DLL调用

```
[](#cb2-1)int32_t RegistrySetQword(int64_t instance, int64_t key, const char* valueName, int64_t value)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key` (长整型数): 注册表键句柄,由 [RegistryOpenKey](/注册表/打开注册表键%20-%20RegistryOpenKey.html)
或 [RegistryCreateKey](/注册表/创建注册表键%20-%20RegistryCreateKey.html)
返回

- `valueName` (字符串): 值名称

- `value` (长整型数): 要写入的64位整型值

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建或打开注册表键
[](#cb3-5)int64_t key = RegistryCreateKey(instance, 1, "Software\\OLAPlug\\Statistics");
[](#cb3-6)
[](#cb3-7)if (key != 0) {
[](#cb3-8)    // 设置总访问次数(大数值)
[](#cb3-9)    int32_t result = RegistrySetQword(instance, key, "TotalVisits", 10000000000LL);
[](#cb3-10)    if (result == 1) {
[](#cb3-11)        printf("成功设置访问次数\n");
[](#cb3-12)    }
[](#cb3-13)
[](#cb3-14)    // 设置文件大小(字节)
[](#cb3-15)    result = RegistrySetQword(instance, key, "FileSize", 5368709120LL); // 5GB
[](#cb3-16)
[](#cb3-17)    // 设置时间戳(毫秒)
[](#cb3-18)    int64_t timestamp = 1640000000000LL;
[](#cb3-19)    result = RegistrySetQword(instance, key, "LastUpdate", timestamp);
[](#cb3-20)
[](#cb3-21)    // 关闭注册表键
[](#cb3-22)    RegistryCloseKey(instance, key);
[](#cb3-23)}
[](#cb3-24)
[](#cb3-25)// 释放资源
[](#cb3-26)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数: - 1: 成功 - 0: 失败

### 注意事项

- 如果值名称已存在,将覆盖原有值

- REG_QWORD 类型为64位无符号整数,范围为 0 到
18,446,744,073,709,551,615

- 适用于存储大数值,如文件大小、时间戳、大数计数器等

- 在32位系统上也可以使用此类型

---

# 设置字符串值 -
RegistrySetString

### 函数简介

设置字符串类型的注册表值(REG_SZ),用于存储文本信息。

### 接口名称

```
RegistrySetString
```

### DLL调用

```
[](#cb2-1)int32_t RegistrySetString(int64_t instance, int64_t key, const char* valueName, const char* value)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key` (长整型数): 注册表键句柄,由 [RegistryOpenKey](/注册表/打开注册表键%20-%20RegistryOpenKey.html)
或 [RegistryCreateKey](/注册表/创建注册表键%20-%20RegistryCreateKey.html)
返回

- `valueName` (字符串): 值名称,空字符串表示默认值

- `value` (字符串): 字符串值内容

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建或打开注册表键
[](#cb3-5)int64_t key = RegistryCreateKey(instance, 1, "Software\\OLAPlug\\Config");
[](#cb3-6)
[](#cb3-7)if (key != 0) {
[](#cb3-8)    // 设置字符串值
[](#cb3-9)    int32_t result = RegistrySetString(instance, key, "AppName", "OLAPlug Application");
[](#cb3-10)    if (result == 1) {
[](#cb3-11)        printf("成功设置字符串值\n");
[](#cb3-12)    }
[](#cb3-13)
[](#cb3-14)    // 设置默认值
[](#cb3-15)    result = RegistrySetString(instance, key, "", "默认配置");
[](#cb3-16)
[](#cb3-17)    // 设置路径值
[](#cb3-18)    result = RegistrySetString(instance, key, "InstallPath", "C:\\Program Files\\OLAPlug");
[](#cb3-19)
[](#cb3-20)    // 关闭注册表键
[](#cb3-21)    RegistryCloseKey(instance, key);
[](#cb3-22)}
[](#cb3-23)
[](#cb3-24)// 释放资源
[](#cb3-25)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数: - 1: 成功 - 0: 失败

### 注意事项

- 如果值名称已存在,将覆盖原有值

- 空字符串作为值名称表示设置默认值

- 字符串值类型为 REG_SZ,不会展开环境变量

- 如果需要展开环境变量,系统会自动处理 REG_EXPAND_SZ 类型

- 支持 Unicode 字符串

---

# 设置环境变量 -
RegistrySetEnvironmentVariable

### 函数简介

设置环境变量,内部基于注册表与系统API实现,支持用户级和系统级环境变量。

### 接口名称

```
RegistrySetEnvironmentVariable
```

### DLL调用

```
[](#cb2-1)int32_t RegistrySetEnvironmentVariable(int64_t instance, const char* name, const char* value, int32_t systemWide)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `name` (字符串): 环境变量名称

- `value` (字符串): 环境变量值

- `systemWide` (整型数): 是否为系统级环境变量

1: 系统级(所有用户可见)

- 0: 当前用户级

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 设置用户级环境变量
[](#cb3-5)int32_t result = RegistrySetEnvironmentVariable(instance, "OLA_HOME", "C:\\OLAPlug", 0);
[](#cb3-6)if (result == 1) {
[](#cb3-7)    printf("成功设置用户级环境变量\n");
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)// 设置用户级PATH(追加)
[](#cb3-11)// 注意:需要先读取现有PATH,然后追加新路径
[](#cb3-12)int64_t existingPath = RegistryGetEnvironmentVariable(instance, "PATH", 0);
[](#cb3-13)if (existingPath != 0) {
[](#cb3-14)    char newPath[4096];
[](#cb3-15)    snprintf(newPath, sizeof(newPath), "%s;C:\\OLAPlug\\bin", (const char*)existingPath);
[](#cb3-16)    RegistrySetEnvironmentVariable(instance, "PATH", newPath, 0);
[](#cb3-17)    FreeStringPtr(instance, existingPath);
[](#cb3-18)}
[](#cb3-19)
[](#cb3-20)// 设置系统级环境变量(需要管理员权限)
[](#cb3-21)result = RegistrySetEnvironmentVariable(instance, "OLA_SYSTEM_CONFIG", "C:\\Program Files\\OLAPlug\\config", 1);
[](#cb3-22)if (result == 1) {
[](#cb3-23)    printf("成功设置系统级环境变量\n");
[](#cb3-24)} else {
[](#cb3-25)    printf("设置失败,可能需要管理员权限\n");
[](#cb3-26)}
[](#cb3-27)
[](#cb3-28)// 释放资源
[](#cb3-29)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数: - 1: 成功 - 0: 失败

### 注意事项

- 设置系统级环境变量(systemWide=1)需要管理员权限

- 环境变量设置后可能需要重新启动应用程序或系统才能生效

- 修改PATH等系统变量时建议先读取现有值,再追加新值

- 环境变量名称不区分大小写

- 设置后会立即写入注册表,但当前进程需要刷新才能获取新值

- 系统级环境变量存储在 HKEY_LOCAL_MACHINEManager

- 用户级环境变量存储在 HKEY_CURRENT_USER

---

# 读取32位整型值 -
RegistryGetDword

### 函数简介

读取32位整型的注册表值(REG_DWORD),用于获取数值型配置。

### 接口名称

```
RegistryGetDword
```

### DLL调用

```
[](#cb2-1)int32_t RegistryGetDword(int64_t instance, int64_t key, const char* valueName)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key` (长整型数): 注册表键句柄,由 [RegistryOpenKey](/注册表/打开注册表键%20-%20RegistryOpenKey.html)
或 [RegistryCreateKey](/注册表/创建注册表键%20-%20RegistryCreateKey.html)
返回

- `valueName` (字符串): 值名称

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 打开注册表键
[](#cb3-5)int64_t key = RegistryOpenKey(instance, 1, "Software\\OLAPlug\\Config");
[](#cb3-6)
[](#cb3-7)if (key != 0) {
[](#cb3-8)    // 读取版本号
[](#cb3-9)    int32_t version = RegistryGetDword(instance, key, "Version");
[](#cb3-10)    printf("版本号: %d\n", version);
[](#cb3-11)
[](#cb3-12)    // 读取最大连接数
[](#cb3-13)    int32_t maxConn = RegistryGetDword(instance, key, "MaxConnections");
[](#cb3-14)    printf("最大连接数: %d\n", maxConn);
[](#cb3-15)
[](#cb3-16)    // 读取启用标志
[](#cb3-17)    int32_t enabled = RegistryGetDword(instance, key, "Enabled");
[](#cb3-18)    if (enabled == 1) {
[](#cb3-19)        printf("功能已启用\n");
[](#cb3-20)    } else {
[](#cb3-21)        printf("功能未启用\n");
[](#cb3-22)    }
[](#cb3-23)
[](#cb3-24)    // 关闭注册表键
[](#cb3-25)    RegistryCloseKey(instance, key);
[](#cb3-26)}
[](#cb3-27)
[](#cb3-28)// 释放资源
[](#cb3-29)DestroyCOLAPlugInterFace(instance);
```

### 返回值

整型数: - 成功: 返回读取到的32位整型值 - 失败或不存在: 返回 0

### 注意事项

- 如果值不存在或类型不匹配,将返回 0

- 无法区分返回的 0 是实际值还是错误标志,建议先用 [RegistryKeyExists](/注册表/判断注册表键是否存在%20-%20RegistryKeyExists.html)
检查

- REG_DWORD 类型为32位无符号整数

- 读取前建议确认值的类型正确

---

# 读取64位整型值 -
RegistryGetQword

### 函数简介

读取64位整型的注册表值(REG_QWORD),用于获取大数值型配置。

### 接口名称

```
RegistryGetQword
```

### DLL调用

```
[](#cb2-1)int64_t RegistryGetQword(int64_t instance, int64_t key, const char* valueName)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key` (长整型数): 注册表键句柄,由 [RegistryOpenKey](/注册表/打开注册表键%20-%20RegistryOpenKey.html)
或 [RegistryCreateKey](/注册表/创建注册表键%20-%20RegistryCreateKey.html)
返回

- `valueName` (字符串): 值名称

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 打开注册表键
[](#cb3-5)int64_t key = RegistryOpenKey(instance, 1, "Software\\OLAPlug\\Statistics");
[](#cb3-6)
[](#cb3-7)if (key != 0) {
[](#cb3-8)    // 读取总访问次数
[](#cb3-9)    int64_t totalVisits = RegistryGetQword(instance, key, "TotalVisits");
[](#cb3-10)    printf("总访问次数: %lld\n", totalVisits);
[](#cb3-11)
[](#cb3-12)    // 读取文件大小
[](#cb3-13)    int64_t fileSize = RegistryGetQword(instance, key, "FileSize");
[](#cb3-14)    printf("文件大小: %lld 字节 (%.2f GB)\n", fileSize, fileSize / (1024.0 * 1024.0 * 1024.0));
[](#cb3-15)
[](#cb3-16)    // 读取时间戳
[](#cb3-17)    int64_t timestamp = RegistryGetQword(instance, key, "LastUpdate");
[](#cb3-18)    printf("最后更新时间戳: %lld\n", timestamp);
[](#cb3-19)
[](#cb3-20)    // 关闭注册表键
[](#cb3-21)    RegistryCloseKey(instance, key);
[](#cb3-22)}
[](#cb3-23)
[](#cb3-24)// 释放资源
[](#cb3-25)DestroyCOLAPlugInterFace(instance);
```

### 返回值

长整型数: - 成功: 返回读取到的64位整型值 - 失败或不存在: 返回 0

### 注意事项

- 如果值不存在或类型不匹配,将返回 0

- 无法区分返回的 0 是实际值还是错误标志

- REG_QWORD 类型为64位无符号整数

- 适用于读取大数值,如文件大小、时间戳等

- 读取前建议确认值的类型正确

---

# 读取字符串值 -
RegistryGetString

### 函数简介

读取字符串类型的注册表值(REG_SZ/REG_EXPAND_SZ),用于获取文本信息。

### 接口名称

```
RegistryGetString
```

### DLL调用

```
[](#cb2-1)int64_t RegistryGetString(int64_t instance, int64_t key, const char* valueName)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针,由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key` (长整型数): 注册表键句柄,由 [RegistryOpenKey](/注册表/打开注册表键%20-%20RegistryOpenKey.html)
或 [RegistryCreateKey](/注册表/创建注册表键%20-%20RegistryCreateKey.html)
返回

- `valueName` (字符串): 值名称,空字符串表示读取默认值

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 打开注册表键
[](#cb3-5)int64_t key = RegistryOpenKey(instance, 1, "Software\\OLAPlug\\Config");
[](#cb3-6)
[](#cb3-7)if (key != 0) {
[](#cb3-8)    // 读取字符串值
[](#cb3-9)    int64_t strPtr = RegistryGetString(instance, key, "AppName");
[](#cb3-10)
[](#cb3-11)    if (strPtr != 0) {
[](#cb3-12)        const char* appName = (const char*)strPtr;
[](#cb3-13)        printf("应用名称: %s\n", appName);
[](#cb3-14)
[](#cb3-15)        // 释放字符串内存
[](#cb3-16)        FreeStringPtr(instance, strPtr);
[](#cb3-17)    } else {
[](#cb3-18)        printf("读取字符串值失败或值不存在\n");
[](#cb3-19)    }
[](#cb3-20)
[](#cb3-21)    // 读取默认值
[](#cb3-22)    strPtr = RegistryGetString(instance, key, "");
[](#cb3-23)    if (strPtr != 0) {
[](#cb3-24)        printf("默认值: %s\n", (const char*)strPtr);
[](#cb3-25)        FreeStringPtr(instance, strPtr);
[](#cb3-26)    }
[](#cb3-27)
[](#cb3-28)    // 关闭注册表键
[](#cb3-29)    RegistryCloseKey(instance, key);
[](#cb3-30)}
[](#cb3-31)
[](#cb3-32)// 释放资源
[](#cb3-33)DestroyCOLAPlugInterFace(instance);
```

### 返回值

长整型数: - 成功: 返回字符串内容的句柄(非0值) - 失败或不存在: 返回
0

### 注意事项

- 返回的字符串句柄需使用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放

- 空字符串作为值名称表示读取默认值

- 支持读取 REG_SZ 和 REG_EXPAND_SZ 类型

- 如果值类型不是字符串类型,将返回 0

- 返回值为 0 可能表示值不存在或读取失败

---

## 窗口

# 发送剪贴板内容 - SendPaste

### 函数简介

向指定窗口发送粘贴命令，将剪贴板的内容发送到目标窗口。该函数会模拟键盘的
Ctrl+V 组合键操作，将当前剪贴板中的内容粘贴到目标窗口中。

### 接口名称

```
SendPaste
```

### DLL调用

```
int SendPaste(long ola, long hwnd)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数):
目标窗口的句柄。窗口必须处于激活状态才能成功接收粘贴命令。

#### 示例:

```
[](#cb3-1)// 向窗口发送粘贴命令
[](#cb3-2)int ret = SendPaste(ola, hwnd);
[](#cb3-3)if (ret == 1) {
[](#cb3-4)    printf("剪贴板内容粘贴成功\n");
[](#cb3-5)} else {
[](#cb3-6)    printf("剪贴板内容粘贴失败\n");
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 先设置剪贴板内容，再发送粘贴命令
[](#cb3-10)SetClipboard(ola, "Hello World");
[](#cb3-11)ret = SendPaste(ola, hwnd);
[](#cb3-12)if (ret == 1) {
[](#cb3-13)    printf("文本粘贴成功\n");
[](#cb3-14)} else {
[](#cb3-15)    printf("文本粘贴失败\n");
[](#cb3-16)}
```

### 返回值

整型数: - 0: 粘贴失败 - 1: 粘贴成功

### 注意事项

- 使用此函数前，请确保目标窗口已经激活（获得焦点）

- 如果目标窗口不支持粘贴操作，函数将返回失败

- 某些应用程序可能会拦截或修改粘贴操作，导致粘贴内容与预期不符

- 建议在使用此函数前，先使用 [SetClipboard](/窗口/设置剪贴板%20-%20SetClipboard.html)
函数设置剪贴板内容

- 对于某些特殊窗口，可能需要先使用 [SetWindowText](/窗口/设置窗口标题%20-%20SetWindowText.html)
函数设置窗口标题，以确保窗口能够正确接收粘贴命令

---

# 发送字符串 - SendString

### 函数简介

向指定窗口发送文本数据。该函数会模拟键盘输入，将指定的文本字符串发送到目标窗口。支持发送普通文本、特殊字符（如制表符、换行符等）以及组合键。

### 接口名称

```
SendString
```

### DLL调用

```
int SendString(long ola, long hwnd, string string)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数):
目标窗口的句柄。窗口必须处于激活状态才能成功接收文本。

- `string` (字符串): 要发送的文本数据。支持以下特殊字符：

`\t`: 制表符

- `\n`: 换行符

- `\r`: 回车符

#### 示例:

```
[](#cb3-1)// 向窗口发送普通文本
[](#cb3-2)int ret = SendString(ola, hwnd, "Hello World");
[](#cb3-3)if (ret == 1) {
[](#cb3-4)    printf("文本发送成功\n");
[](#cb3-5)} else {
[](#cb3-6)    printf("文本发送失败\n");
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 向窗口发送带格式的文本
[](#cb3-10)ret = SendString(ola, hwnd, "用户名：admin\n密码：123456\n");
[](#cb3-11)if (ret == 1) {
[](#cb3-12)    printf("带格式文本发送成功\n");
[](#cb3-13)}
[](#cb3-14)
[](#cb3-15)// 使用特殊字符模拟按键操作
[](#cb3-16)ret = SendString(ola, hwnd, "{CTRL}A{DELETE}");  // 全选并删除
[](#cb3-17)if (ret == 1) {
[](#cb3-18)    printf("按键操作执行成功\n");
[](#cb3-19)}
```

### 返回值

整型数: - 0: 发送失败 - 1: 发送成功

### 注意事项

- 使用此函数前，请确保目标窗口已经激活（获得焦点）

- 某些应用程序可能会拦截或修改发送的文本，导致实际输入与预期不符

- 对于某些特殊窗口，可能需要先使用 [SetWindowText](/窗口/设置窗口标题%20-%20SetWindowText.html)
函数设置窗口标题

- 如果需要发送剪贴板内容，建议使用 [SendPaste](/窗口/发送剪贴板内容%20-%20SendPaste.html) 函数

- 发送大量文本时，建议适当添加延时，以确保文本能够被正确接收

---

# 发送字符串 - SendStringEx

## 函数简介

发送字符串到指定地址，支持多种字符串编码格式。

## 接口名称

```
SendStringEx
```

## DLL调用

```
int OLA_CALL_TYPE SendStringEx(long instance, long hwnd, long addr, int len, int type);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
addr |
长整数型 |
地址 |
|

|
len |
整数型 |
长度 |
|

|
type |
整数型 |
字符串类型,取值如下
0 : GBK字符串
1 : Unicode字符串
2 :
UTF8字符串 |
|

### 示例

```
[](#cb3-1)// 发送GBK字符串到指定地址
[](#cb3-2)int32_t result = SendStringEx(instance, hwnd, addr, strlen("Hello World"), 0);
[](#cb3-3)
[](#cb3-4)// 发送Unicode字符串到指定地址
[](#cb3-5)int32_t result = SendStringEx(instance, hwnd, addr, wcslen(L"Hello World"), 1);
[](#cb3-6)
[](#cb3-7)// 发送UTF8字符串到指定地址
[](#cb3-8)int32_t result = SendStringEx(instance, hwnd, addr, strlen("Hello World"), 2);
```

## 返回值

返回操作结果，成功返回1，失败返回0。

## 注意事项

- 确保目标地址有足够的空间存储字符串

- 根据字符串类型正确设置type参数

- 确保窗口句柄有效

- 注意字符串长度计算，不同编码格式的字符串长度可能不同

---

# 屏幕坐标转窗口坐标 -
ScreenToClient

### 函数简介

将屏幕坐标转换为窗口客户区坐标。该函数用于将相对于屏幕左上角的绝对坐标转换为相对于窗口客户区左上角的相对坐标。这在处理全局鼠标事件、拖放操作等需要将屏幕坐标转换为窗口内部坐标的场景中非常有用。

### 接口名称

```
ScreenToClient
```

### DLL调用

```
int ScreenToClient(long ola, long hwnd, int* x, int* y)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 目标窗口的句柄。

- `x` (整型数指针):
传入屏幕X坐标，返回对应的客户区X坐标。

- `y` (整型数指针):
传入屏幕Y坐标，返回对应的客户区Y坐标。

#### 示例:

```
[](#cb3-1)// 获取当前鼠标位置并转换为窗口客户区坐标
[](#cb3-2)int x, y;
[](#cb3-3)GetCursorPos(&x, &y);
[](#cb3-4)int ret = ScreenToClient(ola, hwnd, &x, &y);
[](#cb3-5)if (ret == 1) {
[](#cb3-6)    printf("鼠标在客户区的位置：(%d, %d)\n", x, y);
[](#cb3-7)} else {
[](#cb3-8)    printf("坐标转换失败\n");
[](#cb3-9)}
[](#cb3-10)
[](#cb3-11)// 判断鼠标是否在客户区内
[](#cb3-12)int x1, y1, x2, y2;
[](#cb3-13)GetClientRect(ola, hwnd, &x1, &y1, &x2, &y2);
[](#cb3-14)if (x >= 0 && x <= x2 && y >= 0 && y <= y2) {
[](#cb3-15)    printf("鼠标在客户区内\n");
[](#cb3-16)} else {
[](#cb3-17)    printf("鼠标在客户区外\n");
[](#cb3-18)}
[](#cb3-19)
[](#cb3-20)// 将屏幕上的一个矩形区域转换为客户区坐标
[](#cb3-21)int rect_left = 100, rect_top = 100;
[](#cb3-22)int rect_right = 200, rect_bottom = 200;
[](#cb3-23)ret = ScreenToClient(ola, hwnd, &rect_left, &rect_top);
[](#cb3-24)ret &= ScreenToClient(ola, hwnd, &rect_right, &rect_bottom);
[](#cb3-25)if (ret == 1) {
[](#cb3-26)    printf("矩形在客户区的位置：左上(%d, %d), 右下(%d, %d)\n",
[](#cb3-27)           rect_left, rect_top, rect_right, rect_bottom);
[](#cb3-28)}
```

### 返回值

整型数: - 0: 转换失败 - 1: 转换成功

### 注意事项

- 窗口必须处于可见状态，否则坐标转换可能失败

- 传入的坐标是相对于屏幕左上角的绝对坐标

- 返回的坐标是相对于客户区左上角的相对坐标，可能为负值（表示点在客户区外）

- 如果需要将客户区坐标转换为屏幕坐标，请使用 [ClientToScreen](/窗口/窗口坐标转屏幕坐标%20-%20ClientToScreen.html)
函数

- 在处理拖放操作时，通常需要使用此函数将屏幕坐标转换为客户区坐标

---

# 强制卸载DLL -
ReleaseWindowsDll

### 函数简介

强制卸载已经注入到指定窗口的Hook
DLL。此函数用于清理和释放窗口相关的DLL资源，但需要谨慎使用，因为它会影响其他使用相同DLL的OLA对象。

### 接口名称

```
ReleaseWindowsDll
```

### DLL调用

```
int ReleaseWindowsDll(long ola, long hwnd)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数):
指定的窗口句柄，必须是有效的窗口句柄。

#### 示例:

```
[](#cb3-1)// 强制卸载指定窗口的Hook DLL
[](#cb3-2)int ret = ReleaseWindowsDll(ola, hwnd);
[](#cb3-3)if (ret == 1) {
[](#cb3-4)    printf("Hook DLL unloaded successfully\n");
[](#cb3-5)
[](#cb3-6)    // 验证窗口状态
[](#cb3-7)    if (GetWindowState(ola, hwnd, 2) == 1) {  // 检查是否可见
[](#cb3-8)        printf("Window is still visible after DLL unload\n");
[](#cb3-9)    }
[](#cb3-10)} else {
[](#cb3-11)    printf("Failed to unload Hook DLL\n");
[](#cb3-12)}
[](#cb3-13)
[](#cb3-14)// 在进程退出前清理所有Hook DLL
[](#cb3-15)void CleanupHookDLLs() {
[](#cb3-16)    // 获取所有相关窗口
[](#cb3-17)    long hwndArray[10];  // 假设最多有10个相关窗口
[](#cb3-18)    int count = 0;
[](#cb3-19)
[](#cb3-20)    // 这里需要实现获取相关窗口的逻辑
[](#cb3-21)    // ...
[](#cb3-22)
[](#cb3-23)    // 卸载每个窗口的Hook DLL
[](#cb3-24)    for (int i = 0; i < count; i++) {
[](#cb3-25)        ret = ReleaseWindowsDll(ola, hwndArray[i]);
[](#cb3-26)        if (ret == 1) {
[](#cb3-27)            printf("Successfully unloaded Hook DLL from window %ld\n", hwndArray[i]);
[](#cb3-28)        } else {
[](#cb3-29)            printf("Failed to unload Hook DLL from window %ld\n", hwndArray[i]);
[](#cb3-30)        }
[](#cb3-31)    }
[](#cb3-32)}
[](#cb3-33)
[](#cb3-34)// 安全卸载单个窗口的Hook DLL
[](#cb3-35)bool SafeUnloadHookDLL(long targetHwnd) {
[](#cb3-36)    // 首先检查窗口是否存在
[](#cb3-37)    if (GetWindowState(ola, targetHwnd, 0) == 0) {
[](#cb3-38)        printf("Window does not exist\n");
[](#cb3-39)        return false;
[](#cb3-40)    }
[](#cb3-41)
[](#cb3-42)    // 尝试卸载DLL
[](#cb3-43)    int ret = ReleaseWindowsDll(ola, targetHwnd);
[](#cb3-44)    if (ret == 1) {
[](#cb3-45)        printf("Hook DLL unloaded successfully from window %ld\n", targetHwnd);
[](#cb3-46)        return true;
[](#cb3-47)    } else {
[](#cb3-48)        printf("Failed to unload Hook DLL from window %ld\n", targetHwnd);
[](#cb3-49)        return false;
[](#cb3-50)    }
[](#cb3-51)}
```

### 返回值

整型数: - `0`:
卸载失败（可能原因：无效的窗口句柄、DLL已卸载、权限不足等） -
`1`: 卸载成功

### 注意事项

- 此操作为强制卸载，会影响使用相同DLL的其他OLA对象

- 建议在以下情况下使用此函数：

程序退出前的清理工作

- 确认没有其他OLA对象需要使用该DLL

- 处理DLL加载异常的情况

- 卸载DLL后，相关的功能将无法使用

- 建议在卸载前保存必要的数据

- 某些系统窗口可能会拒绝DLL卸载操作

- 如果有多个OLA对象共享DLL，应协调好卸载时机

- 建议实现错误处理和日志记录机制

- 在批量操作时要注意性能和稳定性

---

# 拓展找窗口 - FindWindowEx

### 函数简介

查找符合类名或者标题名的窗口。如果指定了父窗口句柄，则在父窗口的第一层子窗口中查找；否则在顶层窗口中查找。该函数支持模糊匹配，可以更灵活地查找目标窗口。

### 接口名称

```
FindWindowEx
```

### DLL调用

```
long FindWindowEx(long ola, long parent, string class, string title)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `parent` (长整型数):
父窗口句柄。如果为0，则在顶层窗口中查找。

- `class` (字符串):
窗口类名，支持模糊匹配。如果为空字符串，则匹配所有类名。

- `title` (字符串):
窗口标题，支持模糊匹配。如果为空字符串，则匹配所有标题。

#### 示例:

```
[](#cb3-1)// 在顶层窗口中查找标题包含"记事本"的窗口
[](#cb3-2)long hwnd = FindWindowEx(ola, 0, "", "记事本");
[](#cb3-3)if (hwnd != 0) {
[](#cb3-4)    printf("找到记事本窗口，句柄为：%ld\n", hwnd);
[](#cb3-5)} else {
[](#cb3-6)    printf("未找到记事本窗口\n");
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 在指定父窗口下查找类名包含"Button"的子窗口
[](#cb3-10)hwnd = FindWindowEx(ola, parent_hwnd, "Button", "");
[](#cb3-11)if (hwnd != 0) {
[](#cb3-12)    printf("找到按钮窗口，句柄为：%ld\n", hwnd);
[](#cb3-13)} else {
[](#cb3-14)    printf("未找到按钮窗口\n");
[](#cb3-15)}
[](#cb3-16)
[](#cb3-17)// 同时指定类名和标题进行精确查找
[](#cb3-18)hwnd = FindWindowEx(ola, 0, "Notepad", "无标题 - 记事本");
[](#cb3-19)if (hwnd != 0) {
[](#cb3-20)    printf("找到指定窗口，句柄为：%ld\n", hwnd);
[](#cb3-21)}
```

### 返回值

长整型数: - 返回找到的窗口句柄 - 如果未找到匹配的窗口，返回0

### 注意事项

- 该函数只查找第一层子窗口，不会递归查找子窗口的子窗口

- 如果同时指定了类名和标题，则两个条件都必须满足才会返回窗口句柄

- 模糊匹配时，只要窗口类名或标题包含指定的字符串即可匹配成功

- 建议在使用此函数前，先使用 [FindWindow](/窗口/查找窗口%20-%20FindWindow.html)
函数获取父窗口句柄

- 对于某些特殊窗口，可能需要使用 [FindWindowSuper](/窗口/查找特殊窗口%20-%20FindWindowSuper.html)
函数进行查找

---

# 枚举特殊窗口 -
EnumWindowSuper

### 函数简介

枚举窗口

### 接口名称

```
EnumWindowSuper
```

### DLL调用

```
string EnumWindowSuper(long ola, string spec1, int flag1, int type1, string spec2, int flag2, int type2, int sort)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `spec1` (字符串): 查找串1，内容取决于flag1的值。

- `flag1` (整型数): 查找串1的类型，可选值：

0: 标题

- 1: 程序名字（如notepad）

- 2: 类名

- 3: 程序路径（不含盘符，如）

- 4: 父句柄（十进制字符串）

- 5: 父窗口标题

- 6: 父窗口类名

- 7: 顶级窗口句柄（十进制字符串）

- 8: 顶级窗口标题

- 9: 顶级窗口类名

- `type1` (整型数): 查找串1的匹配方式：

0: 精确匹配

- 1: 模糊匹配

- `spec2` (字符串): 查找串2，内容取决于flag2的值。

- `flag2` (整型数): 查找串2的类型，可选值同flag1。

- `type2` (整型数): 查找串2的匹配方式：

0: 精确匹配

- 1: 模糊匹配

- `sort` (整型数): 排序方式：

0: 不排序

- 1: 按窗口打开顺序排序

#### 示例:

待补充…

### 返回值

字符串:

返回所有匹配的窗口句柄字符串,格式”hwnd1,hwnd2,hwnd3”

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 枚举窗口 - EnumWindow

### 函数简介

根据指定条件，枚举系统中符合条件的窗口。该函数可以用于查找特定窗口、获取窗口列表、查找子窗口等操作，支持多种过滤条件组合使用。

### 接口名称

```
EnumWindow
```

### DLL调用

```
long EnumWindow(long ola, long parent, string title, string class_name, int filter)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `parent` (长整型数):
父窗口句柄，获取的窗口必须是该窗口的子窗口。当为0时获取桌面的子窗口。

- `title` (字符串):
窗口标题，支持模糊匹配。如果为空字符串，则不匹配标题。

- `class_name` (字符串):
窗口类名，支持模糊匹配。如果为空字符串，则不匹配类名。

- `filter` (整型数): 过滤条件，可以组合使用（值相加）：

1: 匹配窗口标题（参数title有效）

- 2: 匹配窗口类名（参数class_name有效）

- 4: 只匹配第一个进程的窗口

- 8: 匹配顶级窗口（所有者窗口为0）

- 16: 匹配可见窗口

#### 示例:

```
[](#cb3-1)// 查找所有可见的顶级窗口，标题包含"记事本"
[](#cb3-2)long strPtr = EnumWindow(ola, 0, "记事本", "", 1 + 8 + 16);
[](#cb3-3)if (strPtr != 0) {
[](#cb3-4)    char* hwndList = (char*)strPtr;
[](#cb3-5)    printf("找到记事本窗口：%s\n", hwndList);
[](#cb3-6)
[](#cb3-7)    // 解析窗口句柄列表
[](#cb3-8)    char* hwnd = strtok(hwndList, ",");
[](#cb3-9)    while (hwnd != NULL) {
[](#cb3-10)        printf("窗口句柄：%s\n", hwnd);
[](#cb3-11)        hwnd = strtok(NULL, ",");
[](#cb3-12)    }
[](#cb3-13)
[](#cb3-14)    // 释放内存
[](#cb3-15)    FreeStringPtr(strPtr);
[](#cb3-16)}
[](#cb3-17)
[](#cb3-18)// 查找指定父窗口下所有可见的子窗口，类名包含"Button"
[](#cb3-19)strPtr = EnumWindow(ola, parent_hwnd, "", "Button", 2 + 16);
[](#cb3-20)if (strPtr != 0) {
[](#cb3-21)    char* hwndList = (char*)strPtr;
[](#cb3-22)    printf("找到按钮窗口：%s\n", hwndList);
[](#cb3-23)
[](#cb3-24)    // 解析窗口句柄列表
[](#cb3-25)    char* hwnd = strtok(hwndList, ",");
[](#cb3-26)    while (hwnd != NULL) {
[](#cb3-27)        printf("按钮句柄：%s\n", hwnd);
[](#cb3-28)        hwnd = strtok(NULL, ",");
[](#cb3-29)    }
[](#cb3-30)
[](#cb3-31)    // 释放内存
[](#cb3-32)    FreeStringPtr(strPtr);
[](#cb3-33)}
[](#cb3-34)
[](#cb3-35)// 查找所有可见的顶级窗口
[](#cb3-36)strPtr = EnumWindow(ola, 0, "", "", 8 + 16);
[](#cb3-37)if (strPtr != 0) {
[](#cb3-38)    char* hwndList = (char*)strPtr;
[](#cb3-39)    printf("所有可见顶级窗口：%s\n", hwndList);
[](#cb3-40)    FreeStringPtr(strPtr);
[](#cb3-41)}
```

### 返回值

字符串: - 返回所有匹配的窗口句柄字符串，格式为”hwnd1,hwnd2,hwnd3” -
如果没有找到匹配的窗口，返回空字符串

### 注意事项

- DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

- 过滤条件可以组合使用，例如：1+8+16
表示匹配标题、顶级窗口和可见窗口

- 某些窗口可能无法被枚举，这取决于当前用户的权限和窗口的状态

- 建议在使用此函数前，先使用 [GetWindowTitle](/窗口/获取窗口标题%20-%20GetWindowTitle.html) 和
[GetWindowClass](/窗口/获取窗口类名%20-%20GetWindowClass.html)
函数获取窗口信息

- 如果需要查找特定进程的窗口，可以使用 [EnumWindowByProcess](/窗口/枚举进程窗口%20-%20EnumWindowByProcess.html)
函数

---

# 枚举进程 - EnumProcess

### 函数简介

根据指定进程名，枚举系统中符合条件的进程PID，按进程启动顺序排序。该函数可以用于查找特定应用程序的所有运行实例，支持模糊匹配进程名。

### 接口名称

```
EnumProcess
```

### DLL调用

```
long EnumProcess(long ola, string name)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `name` (字符串): 进程名，支持以下格式：

完整进程名：如”notepad.exe”

- 部分进程名：如”notepad”

- 通配符：如”.exe”

- 空字符串：枚举所有进程

#### 示例:

```
[](#cb3-1)// 枚举所有记事本进程
[](#cb3-2)long strPtr = EnumProcess(ola, "notepad.exe");
[](#cb3-3)if (strPtr != 0) {
[](#cb3-4)    char* pidList = (char*)strPtr;
[](#cb3-5)    printf("找到记事本进程：%s\n", pidList);
[](#cb3-6)
[](#cb3-7)    // 解析进程ID列表
[](#cb3-8)    char* pid = strtok(pidList, ",");
[](#cb3-9)    while (pid != NULL) {
[](#cb3-10)        printf("进程ID：%s\n", pid);
[](#cb3-11)        pid = strtok(NULL, ",");
[](#cb3-12)    }
[](#cb3-13)
[](#cb3-14)    // 释放内存
[](#cb3-15)    FreeStringPtr(strPtr);
[](#cb3-16)}
[](#cb3-17)
[](#cb3-18)// 枚举所有Chrome浏览器进程
[](#cb3-19)strPtr = EnumProcess(ola, "chrome.exe");
[](#cb3-20)if (strPtr != 0) {
[](#cb3-21)    char* pidList = (char*)strPtr;
[](#cb3-22)    printf("找到Chrome进程：%s\n", pidList);
[](#cb3-23)
[](#cb3-24)    // 解析进程ID列表
[](#cb3-25)    char* pid = strtok(pidList, ",");
[](#cb3-26)    while (pid != NULL) {
[](#cb3-27)        printf("进程ID：%s\n", pid);
[](#cb3-28)        pid = strtok(NULL, ",");
[](#cb3-29)    }
[](#cb3-30)
[](#cb3-31)    // 释放内存
[](#cb3-32)    FreeStringPtr(strPtr);
[](#cb3-33)}
[](#cb3-34)
[](#cb3-35)// 枚举所有进程
[](#cb3-36)strPtr = EnumProcess(ola, "");
[](#cb3-37)if (strPtr != 0) {
[](#cb3-38)    char* pidList = (char*)strPtr;
[](#cb3-39)    printf("所有进程：%s\n", pidList);
[](#cb3-40)    FreeStringPtr(strPtr);
[](#cb3-41)}
```

### 返回值

字符串: - 返回所有匹配的进程PID，按进程启动顺序排序 -
返回格式为”pid1,pid2,pid3” - 如果没有找到匹配的进程，返回空字符串

### 注意事项

- DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

- 进程ID列表中的进程按启动时间排序，越早启动的进程排在越前面

- 某些系统进程可能无法被枚举，这取决于当前用户的权限

- 建议在使用此函数前，先使用 [GetProcessInfo](/窗口/获取进程详细信息%20-%20GetProcessInfo.html)
函数获取进程的详细信息

- 如果需要查找特定窗口的进程，可以使用 [GetWindowProcessId](/窗口/获取进程ID%20-%20GetWindowProcessId.html)
函数

---

# 枚举进程窗口 -
EnumWindowByProcess

### 函数简介

根据指定进程以及其它条件，枚举系统中符合条件的窗口

### 接口名称

```
EnumWindowByProcess
```

### DLL调用

```
long EnumWindowByProcess(long ola, string process_name, string title, string class_name, int filter)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `process_name` (字符串):
进程映像名，如”svchost.exe”。此参数精确匹配但不区分大小写。

- `title` (字符串): 窗口标题，支持模糊匹配。

- `class_name` (字符串): 窗口类名，支持模糊匹配。

- `filter` (整型数): 过滤条件，可以组合使用（值相加）：

1: 匹配窗口标题（参数title有效）

- 2: 匹配窗口类名（参数class_name有效）

- 4: 只匹配指定映像名的第一个进程

- 8: 匹配顶级窗口（所有者窗口为0）

- 16: 匹配可见窗口

#### 示例:

```
// 查找进程"notepad.exe"的所有可见顶级窗口，标题包含"记事本"
long strPtr = EnumWindowByProcess(ola, "notepad.exe", "记事本", "", 1 + 8 + 16);
if (strPtr != 0) {
// 使用窗口句柄列表
// 返回格式: "hwnd1,hwnd2,hwnd3"
// ...
// 释放内存
FreeStringPtr(strPtr);
}

// 查找进程"chrome.exe"的所有可见窗口，类名包含"Chrome"
strPtr = EnumWindowByProcess(ola, "chrome.exe", "", "Chrome", 2 + 16);
if (strPtr != 0) {
// 使用窗口句柄列表
// ...
FreeStringPtr(strPtr);
}
```

### 返回值

字符串: - 返回所有匹配的窗口句柄字符串，格式为”hwnd1,hwnd2,hwnd3”

**注意：** - DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

---

# 枚举进程窗口 -
EnumWindowByProcessId

### 函数简介

根据指定进程ID以及其它条件，枚举系统中符合条件的窗口。该函数可以用于查找特定进程的所有窗口，支持多种过滤条件组合使用，如窗口标题、类名、可见性等。

### 接口名称

```
EnumWindowByProcessId
```

### DLL调用

```
long EnumWindowByProcessId(long ola, long pid, string title, string class_name, int filter)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `pid` (长整型数): 进程ID。可以通过 [GetWindowProcessId](/窗口/获取进程ID%20-%20GetWindowProcessId.html)
函数获取。

- `title` (字符串):
窗口标题，支持模糊匹配。如果为空字符串，则不匹配标题。

- `class_name` (字符串):
窗口类名，支持模糊匹配。如果为空字符串，则不匹配类名。

- `filter` (整型数): 过滤条件，可以组合使用（值相加）：

1: 匹配窗口标题（参数title有效）

- 2: 匹配窗口类名（参数class_name有效）

- 4: 只匹配指定进程ID的第一个窗口

- 8: 匹配顶级窗口（所有者窗口为0）

- 16: 匹配可见窗口

#### 示例:

```
[](#cb3-1)// 查找进程ID为1234的所有可见顶级窗口，标题包含"记事本"
[](#cb3-2)long strPtr = EnumWindowByProcessId(ola, 1234, "记事本", "", 1 + 8 + 16);
[](#cb3-3)if (strPtr != 0) {
[](#cb3-4)    char* hwndList = (char*)strPtr;
[](#cb3-5)    printf("找到记事本窗口：%s\n", hwndList);
[](#cb3-6)
[](#cb3-7)    // 解析窗口句柄列表
[](#cb3-8)    char* hwnd = strtok(hwndList, ",");
[](#cb3-9)    while (hwnd != NULL) {
[](#cb3-10)        printf("窗口句柄：%s\n", hwnd);
[](#cb3-11)        hwnd = strtok(NULL, ",");
[](#cb3-12)    }
[](#cb3-13)
[](#cb3-14)    // 释放内存
[](#cb3-15)    FreeStringPtr(strPtr);
[](#cb3-16)}
[](#cb3-17)
[](#cb3-18)// 查找进程ID为5678的所有可见窗口，类名包含"Chrome"
[](#cb3-19)strPtr = EnumWindowByProcessId(ola, 5678, "", "Chrome", 2 + 16);
[](#cb3-20)if (strPtr != 0) {
[](#cb3-21)    char* hwndList = (char*)strPtr;
[](#cb3-22)    printf("找到Chrome窗口：%s\n", hwndList);
[](#cb3-23)
[](#cb3-24)    // 解析窗口句柄列表
[](#cb3-25)    char* hwnd = strtok(hwndList, ",");
[](#cb3-26)    while (hwnd != NULL) {
[](#cb3-27)        printf("窗口句柄：%s\n", hwnd);
[](#cb3-28)        hwnd = strtok(NULL, ",");
[](#cb3-29)    }
[](#cb3-30)
[](#cb3-31)    // 释放内存
[](#cb3-32)    FreeStringPtr(strPtr);
[](#cb3-33)}
[](#cb3-34)
[](#cb3-35)// 查找进程ID为1234的第一个可见窗口
[](#cb3-36)strPtr = EnumWindowByProcessId(ola, 1234, "", "", 4 + 16);
[](#cb3-37)if (strPtr != 0) {
[](#cb3-38)    char* hwndList = (char*)strPtr;
[](#cb3-39)    printf("找到第一个窗口：%s\n", hwndList);
[](#cb3-40)    FreeStringPtr(strPtr);
[](#cb3-41)}
```

### 返回值

字符串: - 返回所有匹配的窗口句柄字符串，格式为”hwnd1,hwnd2,hwnd3” -
如果没有找到匹配的窗口，返回空字符串

### 注意事项

- DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

- 过滤条件可以组合使用，例如：1+8+16
表示匹配标题、顶级窗口和可见窗口

- 如果指定了进程ID为0，将枚举所有进程的窗口

- 建议在使用此函数前，先使用 [GetWindowProcessId](/窗口/获取进程ID%20-%20GetWindowProcessId.html)
函数获取正确的进程ID

- 如果需要查找特定进程的所有窗口，可以使用 [EnumWindowByProcess](/窗口/枚举进程窗口%20-%20EnumWindowByProcess.html)
函数

---

# 查找特殊窗口 -
FindWindowSuper

### 函数简介

根据多种条件组合查找特定窗口。该函数提供了更灵活的窗口查找方式，支持两个条件的组合查询，可以基于窗口标题、类名、程序名、路径等多种属性进行精确或模糊匹配。

### 接口名称

```
FindWindowSuper
```

### DLL调用

```
long FindWindowSuper(long ola, string spec1, int flag1, int type1, string spec2, int flag2, int type2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `spec1` (字符串):
第一个查找条件的内容，具体含义由flag1决定。

- `flag1` (整型数): 指定spec1的内容类型：

0: 窗口标题

- 1: 程序名（如”notepad”）

- 2: 窗口类名

- 3: 程序路径（不含盘符，如”“）

- 4: 父窗口句柄（十进制字符串）

- 5: 父窗口标题

- 6: 父窗口类名

- 7: 顶级窗口句柄（十进制字符串）

- 8: 顶级窗口标题

- 9: 顶级窗口类名

- `type1` (整型数): 第一个条件的匹配方式：

0: 精确匹配

- 1: 模糊匹配

- `spec2` (字符串):
第二个查找条件的内容，具体含义由flag2决定。

- `flag2` (整型数): 指定spec2的内容类型，取值同flag1。

- `type2` (整型数): 第二个条件的匹配方式：

0: 精确匹配

- 1: 模糊匹配

#### 示例:

```
[](#cb3-1)// 查找标题包含"记事本"且类名为"Notepad"的窗口
[](#cb3-2)long hwnd = FindWindowSuper(ola, "记事本", 0, 1, "Notepad", 2, 0, 0);
[](#cb3-3)if (hwnd != 0) {
[](#cb3-4)    printf("找到记事本窗口，句柄：%ld\n", hwnd);
[](#cb3-5)} else {
[](#cb3-6)    printf("未找到记事本窗口\n");
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 查找父窗口标题包含"Chrome"且程序路径包含"Google"的窗口
[](#cb3-10)hwnd = FindWindowSuper(ola, "Chrome", 5, 1, "\\Google\\", 3, 1, 0);
[](#cb3-11)if (hwnd != 0) {
[](#cb3-12)    printf("找到Chrome窗口，句柄：%ld\n", hwnd);
[](#cb3-13)} else {
[](#cb3-14)    printf("未找到Chrome窗口\n");
[](#cb3-15)}
[](#cb3-16)
[](#cb3-17)// 查找程序名为"notepad"且类名为"Notepad"的窗口
[](#cb3-18)hwnd = FindWindowSuper(ola, "notepad", 1, 0, "Notepad", 2, 0, 0);
[](#cb3-19)if (hwnd != 0) {
[](#cb3-20)    printf("找到记事本窗口，句柄：%ld\n", hwnd);
[](#cb3-21)}
[](#cb3-22)
[](#cb3-23)// 查找顶级窗口标题包含"Microsoft"且程序路径包含"Office"的窗口
[](#cb3-24)hwnd = FindWindowSuper(ola, "Microsoft", 8, 1, "\\Office\\", 3, 1, 0);
[](#cb3-25)if (hwnd != 0) {
[](#cb3-26)    printf("找到Office窗口，句柄：%ld\n", hwnd);
[](#cb3-27)}
```

### 返回值

长整型数: - 返回找到的窗口句柄 - 如果未找到匹配的窗口，返回0

### 注意事项

- 两个条件必须同时满足才会返回窗口句柄

- 模糊匹配时，只要窗口属性包含指定的字符串即可匹配成功

- 程序路径匹配时不区分大小写，且不需要包含盘符

- 建议在使用此函数前，先使用 [GetWindowTitle](/窗口/获取窗口标题%20-%20GetWindowTitle.html)、[GetWindowClass](/窗口/获取窗口类名%20-%20GetWindowClass.html)
等函数获取窗口信息

- 如果需要查找多个符合条件的窗口，可以使用 [EnumWindowSuper](/窗口/枚举特殊窗口%20-%20EnumWindowSuper.html)
函数

---

# 查找窗口 - FindWindow

### 函数简介

查找符合类名或者标题名的顶层可见窗口

### 接口名称

```
FindWindow
```

### DLL调用

```
long FindWindow(long ola, string class, string title)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `class` (字符串):
窗口类名，支持模糊匹配。如果为空字符串，则匹配所有类名。

- `title` (字符串):
窗口标题，支持模糊匹配。如果为空字符串，则匹配所有标题。

#### 示例:

```
// 查找标题包含"记事本"的窗口
long hwnd = FindWindow(ola, "", "记事本");
if (hwnd != 0) {
printf("Found Notepad window: %ld\n", hwnd);
}

// 查找类名包含"Chrome"的窗口
hwnd = FindWindow(ola, "Chrome", "");
if (hwnd != 0) {
printf("Found Chrome window: %ld\n", hwnd);
}
```

### 返回值

长整型数: - 返回找到的窗口句柄 - 如果未找到匹配的窗口，返回0

---

# 查看绑定窗口 - GetBindWindow

### 函数简介

获取当前对象已经绑定的窗口句柄，如果没有绑定窗口则返回0

### 接口名称

```
GetBindWindow
```

### DLL调用

```
long GetBindWindow(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

```
long hwnd = GetBindWindow(ola);
if (hwnd != 0) {
printf("Currently bound to window: %ld\n", hwnd);
} else {
printf("No window currently bound\n");
}
```

### 返回值

长整型数: - 返回当前绑定的窗口句柄 - 如果没有绑定窗口，返回0

---

# 移动窗口 - MoveWindow

### 函数简介

移动指定窗口到指定位置。该函数会将窗口的左上角移动到指定的屏幕坐标位置，保持窗口的当前大小不变。坐标是相对于屏幕左上角的绝对坐标。

### 接口名称

```
MoveWindow
```

### DLL调用

```
int MoveWindow(long ola, long hwnd, int x, int y)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 目标窗口的句柄。

- `x` (整型数): 窗口左上角的目标X坐标（屏幕坐标）。

- `y` (整型数): 窗口左上角的目标Y坐标（屏幕坐标）。

#### 示例:

```
[](#cb3-1)// 移动窗口到屏幕坐标(100, 200)
[](#cb3-2)int ret = MoveWindow(ola, hwnd, 100, 200);
[](#cb3-3)if (ret == 1) {
[](#cb3-4)    printf("窗口移动成功\n");
[](#cb3-5)} else {
[](#cb3-6)    printf("窗口移动失败\n");
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 获取当前窗口位置并向右移动100像素
[](#cb3-10)int x, y;
[](#cb3-11)GetWindowRect(hwnd, &x, &y, NULL, NULL);
[](#cb3-12)ret = MoveWindow(ola, hwnd, x + 100, y);
[](#cb3-13)if (ret == 1) {
[](#cb3-14)    printf("窗口向右移动成功\n");
[](#cb3-15)}
[](#cb3-16)
[](#cb3-17)// 将窗口移动到屏幕中心
[](#cb3-18)int screen_width = GetSystemMetrics(SM_CXSCREEN);
[](#cb3-19)int screen_height = GetSystemMetrics(SM_CYSCREEN);
[](#cb3-20)int window_width, window_height;
[](#cb3-21)GetWindowRect(hwnd, NULL, NULL, &window_width, &window_height);
[](#cb3-22)ret = MoveWindow(ola, hwnd,
[](#cb3-23)    (screen_width - window_width) / 2,
[](#cb3-24)    (screen_height - window_height) / 2);
[](#cb3-25)if (ret == 1) {
[](#cb3-26)    printf("窗口居中成功\n");
[](#cb3-27)}
```

### 返回值

整型数: - 0: 移动失败 - 1: 移动成功

### 注意事项

- 窗口必须处于可见状态，否则移动可能失败

- 坐标是相对于屏幕左上角的绝对坐标

- 移动窗口不会改变窗口的大小

- 建议在使用此函数前，先使用 [GetWindowRect](/窗口/获取窗口区域%20-%20GetWindowRect.html)
函数获取窗口当前位置

- 如果需要同时改变窗口的大小和位置，可以使用 [SetWindowSize](/窗口/设置窗口大小%20-%20SetWindowSize.html)
函数

---

# 窗口坐标转屏幕坐标 -
ClientToScreen

### 函数简介

将窗口客户区坐标转换为屏幕坐标。该函数用于将相对于窗口客户区左上角的坐标转换为相对于屏幕左上角的绝对坐标。这在处理鼠标点击、窗口绘制等需要在不同坐标系统之间转换的场景中非常有用。

### 接口名称

```
ClientToScreen
```

### DLL调用

```
int ClientToScreen(long ola, long hwnd, int* x, int* y)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 目标窗口的句柄。

- `x` (整型数指针):
传入客户区X坐标，返回对应的屏幕X坐标。

- `y` (整型数指针):
传入客户区Y坐标，返回对应的屏幕Y坐标。

#### 示例:

```
[](#cb3-1)// 将客户区坐标(50, 50)转换为屏幕坐标
[](#cb3-2)int x = 50, y = 50;
[](#cb3-3)int ret = ClientToScreen(ola, hwnd, &x, &y);
[](#cb3-4)if (ret == 1) {
[](#cb3-5)    printf("屏幕坐标：(%d, %d)\n", x, y);
[](#cb3-6)} else {
[](#cb3-7)    printf("坐标转换失败\n");
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)// 获取客户区中心点的屏幕坐标
[](#cb3-11)int x1, y1, x2, y2;
[](#cb3-12)GetClientRect(ola, hwnd, &x1, &y1, &x2, &y2);
[](#cb3-13)x = (x2 - x1) / 2;  // 客户区中心点X坐标
[](#cb3-14)y = (y2 - y1) / 2;  // 客户区中心点Y坐标
[](#cb3-15)ret = ClientToScreen(ola, hwnd, &x, &y);
[](#cb3-16)if (ret == 1) {
[](#cb3-17)    printf("客户区中心点的屏幕坐标：(%d, %d)\n", x, y);
[](#cb3-18)}
[](#cb3-19)
[](#cb3-20)// 将鼠标移动到客户区指定位置
[](#cb3-21)int client_x = 100, client_y = 100;
[](#cb3-22)ret = ClientToScreen(ola, hwnd, &client_x, &client_y);
[](#cb3-23)if (ret == 1) {
[](#cb3-24)    MoveMouse(ola, client_x, client_y);
[](#cb3-25)    printf("鼠标已移动到指定位置\n");
[](#cb3-26)}
```

### 返回值

整型数: - 0: 转换失败 - 1: 转换成功

### 注意事项

- 窗口必须处于可见状态，否则坐标转换可能失败

- 传入的坐标是相对于客户区左上角的相对坐标

- 返回的坐标是相对于屏幕左上角的绝对坐标

- 如果需要将屏幕坐标转换为客户区坐标，请使用 [ScreenToClient](/窗口/屏幕坐标转窗口坐标%20-%20ScreenToClient.html)
函数

- 在多显示器系统中，返回的坐标是相对于主显示器左上角的绝对坐标

---

# 绑定窗口 - BindWindow

### 函数简介

绑定指定的窗口,并指定这个窗口的屏幕颜色获取方式,鼠标仿真模式,键盘仿真模式,以及模式设定

### 接口名称

```
BindWindow
```

### DLL调用

```
int BindWindow(long ola, long hwnd, string display, string mouse, string keyboard, int mode)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 指定的窗口句柄。

- `display` (字符串): 屏幕颜色获取方式，取值有以下几种：

“normal”: 正常模式,平常我们用的前台截屏模式

- “gdi”: gdi模式

- “gdi2”: gdi2模式,此模式兼容性较强,但是速度比gdi模式要慢许多

- “gdi3”: gdi3模式,此模式兼容性较强,但是速度比gdi模式要慢许多

- “gdi4”: gdi4模式,支持小程序,浏览器截图

- “gdi5”: gdi5模式,支持小程序,浏览器截图

- “dxgi”: DXGI模式, 支持小程序和浏览器截图,在windows10
1903及以上版本中支持

- “vnc”: vnc模式

- “dx”: dx模式(需要管理员权限)

- `mouse` (字符串): 鼠标仿真模式，取值有以下几种：

“normal”: 正常模式,平常我们用的前台鼠标模式

- “windows”: Windows模式,采取模拟windows消息方式

- “windows3”:
Windows3模式,采取模拟windows消息方式,适用于多窗口的进程

- “vnc”: vnc模式

- dx模式组合(使用”|“连接)：

“dx.mouse.position.lock.api”: 通过封锁系统API来锁定鼠标位置

- “dx.mouse.position.lock.message”:
通过封锁系统消息来锁定鼠标位置

- “dx.mouse.focus.input.api”: 通过封锁系统API来锁定鼠标输入焦点

- “dx.mouse.focus.input.message”:
通过封锁系统消息来锁定鼠标输入焦点

- “dx.mouse.clip.lock.api”: 通过封锁系统API来锁定刷新区域

- “dx.mouse.input.lock.api”: 通过封锁系统API来锁定鼠标输入接口

- “dx.mouse.state.api”: 通过封锁系统API来锁定鼠标输入状态

- “dx.mouse.state.message”: 通过封锁系统消息来锁定鼠标输入状态

- “dx.mouse.api”: 通过封锁系统API来模拟dx鼠标输入

- “dx.mouse.cursor”: 开启后台获取鼠标特征码

- “dx.mouse.raw.input”: 特定窗口鼠标操作支持

- “dx.mouse.input.lock.api2”: 防止前台鼠标移动

- “dx.mouse.input.lock.api3”: 防止前台鼠标移动

- “dx.mouse.raw.input.active”: 配合dx.mouse.raw.input使用

- `keyboard` (字符串): 键盘仿真模式，取值有以下几种：

“normal”: 正常模式,平常我们用的前台键盘模式

- “windows”: Windows模式,采取模拟windows消息方式

- “vnc”: vnc模式

- dx模式组合(使用”|“连接)：

“dx.keypad.input.lock.api”: 通过封锁系统API来锁定键盘输入接口

- “dx.keypad.state.api”: 通过封锁系统API来锁定键盘输入状态

- “dx.keypad.api”: 通过封锁系统API来模拟dx键盘输入

- “dx.keypad.raw.input”: 特定窗口键盘操作支持

- “dx.keypad.raw.input.active”: 配合dx.keypad.raw.input使用

- `mode` (整型数): 模式设定，取值：

0: 推荐模式，此模式比较通用，而且后台效果是最好的

- 1: 远程线程注入

- 2:
驱动注入模式1,当0,1无法使用时使用,需要加载驱动,第一次使用驱动会下载PDB文件绑定时间会变长.

- 3:
驱动注入模式2,当0,1无法使用时使用,需要加载驱动,第一次使用驱动会下载PDB文件绑定时间会变长.

- 4:
驱动注入模式3,当0,1无法使用时使用,需要加载驱动,第一次使用驱动会下载PDB文件绑定时间会变长.

#### 示例:

待补充…

### 返回值

整型数: - 0: 失败 - 1: 成功

---

# 绑定窗口高级 - BindWindowEx

### 函数简介

绑定指定的窗口,并指定这个窗口的屏幕颜色获取方式,鼠标仿真模式,键盘仿真模式,以及模式设定

### 接口名称

```
BindWindowEx
```

### DLL调用

```
int BindWindowEx(long ola, long hwnd, string display, string mouse, string keyboard, string public, int mode)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 指定的窗口句柄。

- `display` (字符串): 屏幕颜色获取方式，可选值：

“normal”: 正常模式，前台截屏模式

- “gdi”: GDI模式

- “gdi2”: GDI2模式，兼容性较强但速度较慢

- “gdi3”: GDI3模式，兼容性较强但速度较慢

- “gdi4”: GDI4模式，支持小程序和浏览器截图

- “gdi5”: GDI5模式，支持小程序和浏览器截图

- “dxgi”: DXGI模式, 支持小程序和浏览器截图,在windows10
1903及以上版本中支持

- “vnc”: VNC模式

- “dx”: DX模式（需要管理员权限）

- `mouse` (字符串): 鼠标仿真模式，可选值：

“normal”: 正常模式，前台鼠标模式

- “windows”: Windows模式，模拟windows消息

- “windows3”:
Windows3模式,采取模拟windows消息方式,适用于多窗口的进程

- “vnc”: VNC模式

- DX模式组合（使用”|“连接）：

“dx.mouse.position.lock.api”: 通过API锁定鼠标位置

- “dx.mouse.position.lock.message”: 通过消息锁定鼠标位置

- “dx.mouse.focus.input.api”: 通过API锁定鼠标输入焦点

- “dx.mouse.focus.input.message”: 通过消息锁定鼠标输入焦点

- “dx.mouse.clip.lock.api”: 通过API锁定刷新区域

- “dx.mouse.input.lock.api”: 通过API锁定鼠标输入接口

- “dx.mouse.state.api”: 通过API锁定鼠标输入状态

- “dx.mouse.state.message”: 通过消息锁定鼠标输入状态

- “dx.mouse.api”: 通过API模拟DX鼠标输入

- “dx.mouse.cursor”: 后台获取鼠标特征码

- “dx.mouse.raw.input”: 特殊窗口鼠标操作支持

- “dx.mouse.input.lock.api2”: 前台鼠标移动控制

- “dx.mouse.input.lock.api3”: 前台鼠标移动控制

- “dx.mouse.raw.input.active”: 配合raw.input的后台支持

- `keyboard` (字符串): 键盘仿真模式，可选值：

“normal”: 正常模式，前台键盘模式

- “windows”: Windows模式，模拟windows消息

- “vnc”: VNC模式

- DX模式组合（使用”|“连接）：

“dx.keypad.input.lock.api”: 通过API锁定键盘输入接口

- “dx.keypad.state.api”: 通过API锁定键盘输入状态

- “dx.keypad.api”: 通过API模拟DX键盘输入

- “dx.keypad.raw.input”: 特殊窗口键盘操作支持

- “dx.keypad.raw.input.active”: 配合raw.input的后台支持

- `public` (字符串): 通用绑定模式（暂未启用）。

“dx.public.graphic.revert” 翻转DX截图的图像结果

- “dx.public.active.api” 自动定时发送激活命令

- “dx.public.active.api2” 自动定时发送激活命令2

- “ola.bypass.guard” 绑定失败的时候可以尝试打开

- `mode` (整型数): 模式设定，取值：

0: 推荐模式，此模式比较通用，而且后台效果是最好的

- 1: 远程线程注入

- 2:
驱动注入模式1,当0,1无法使用时使用,需要加载驱动,第一次使用驱动会下载PDB文件绑定时间会变长.

- 3:
驱动注入模式2,当0,1无法使用时使用,需要加载驱动,第一次使用驱动会下载PDB文件绑定时间会变长.

- 4:
驱动注入模式3,当0,1无法使用时使用,需要加载驱动,第一次使用驱动会下载PDB文件绑定时间会变长.

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 获取客户区域 - GetClientRect

### 函数简介

获取指定窗口的客户区域坐标。客户区是指窗口的工作区域，不包括标题栏、菜单栏、工具栏、状态栏和边框等非客户区。返回的坐标是相对于客户区左上角的相对坐标，左上角坐标总是(0,0)。

### 接口名称

```
GetClientRect
```

### DLL调用

```
int GetClientRect(long ola, long hwnd, int* x1, int* y1, int* x2, int* y2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 目标窗口的句柄。

- `x1` (整型数指针): 返回客户区左上角的X坐标，总是0。

- `y1` (整型数指针): 返回客户区左上角的Y坐标，总是0。

- `x2` (整型数指针):
返回客户区右下角的X坐标，即客户区宽度。

- `y2` (整型数指针):
返回客户区右下角的Y坐标，即客户区高度。

#### 示例:

```
[](#cb3-1)// 获取窗口客户区大小
[](#cb3-2)int x1, y1, x2, y2;
[](#cb3-3)int ret = GetClientRect(ola, hwnd, &x1, &y1, &x2, &y2);
[](#cb3-4)if (ret == 1) {
[](#cb3-5)    printf("客户区大小：宽度=%d, 高度=%d\n", x2 - x1, y2 - y1);
[](#cb3-6)} else {
[](#cb3-7)    printf("获取客户区域失败\n");
[](#cb3-8)}
[](#cb3-9)
[](#cb3-10)// 计算非客户区大小（边框、标题栏等）
[](#cb3-11)int wx1, wy1, wx2, wy2;
[](#cb3-12)GetWindowRect(ola, hwnd, &wx1, &wy1, &wx2, &wy2);
[](#cb3-13)int border_width = (wx2 - wx1) - (x2 - x1);
[](#cb3-14)int border_height = (wy2 - wy1) - (y2 - y1);
[](#cb3-15)printf("非客户区大小：宽度=%d, 高度=%d\n", border_width, border_height);
[](#cb3-16)
[](#cb3-17)// 设置客户区大小为800x600
[](#cb3-18)int new_width = 800;
[](#cb3-19)int new_height = 600;
[](#cb3-20)SetClientSize(ola, hwnd, new_width, new_height);
```

### 返回值

整型数: - 0: 获取失败 - 1: 获取成功

### 注意事项

- 窗口必须处于可见状态，否则获取可能失败

- 返回的坐标是相对于客户区左上角的相对坐标，(x1,y1)总是(0,0)

- (x2,y2)表示客户区的宽度和高度，而不是屏幕坐标

- 如果需要获取包含非客户区的窗口区域，请使用 [GetWindowRect](/窗口/获取窗口区域%20-%20GetWindowRect.html)
函数

- 如果需要将客户区坐标转换为屏幕坐标，请使用 [ClientToScreen](/窗口/窗口坐标转屏幕坐标%20-%20ClientToScreen.html)
函数

---

# 获取剪贴板内容 -
GetClipboard

### 函数简介

获取剪贴板的内容

### 接口名称

```
GetClipboard
```

### DLL调用

```
long GetClipboard(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

```
long strPtr = GetClipboard(ola);
if (strPtr != 0) {
// 使用剪贴板内容
// ...
// 释放内存
FreeStringPtr(strPtr);
}
```

### 返回值

字符串: - 返回剪贴板的内容

**注意：** - DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

---

# 获取坐标所在窗口句柄 -
GetPointWindow

### 函数简介

获取给定坐标的可见窗口句柄，可以获取到按键自带的插件无法获取到的句柄

### 接口名称

```
GetPointWindow
```

### DLL调用

```
long GetPointWindow(long ola, int x, int y)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x` (整型数): 屏幕X坐标。

- `y` (整型数): 屏幕Y坐标。

#### 示例:

```
long hwnd = GetPointWindow(ola, 100, 200);
if (hwnd != 0) {
printf("Window handle at point (100,200): %ld\n", hwnd);
}
```

### 返回值

长整型数: - 返回指定坐标处可见窗口的句柄

---

# 获取客户区大小 -
GetClientSize

### 函数简介

获取窗口客户区域的宽度和高度

### 接口名称

```
GetClientSize
```

### DLL调用

```
int GetClientSize(long ola, long hwnd, int* width, int* height)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 指定的窗口句柄。

- `width` (整型数指针): 用于返回客户区域宽度。

- `height` (整型数指针): 用于返回客户区域高度。

#### 示例:

```
int width = 0, height = 0;
int ret = GetClientSize(ola, hwnd, &width, &height);
if (ret == 1) {
printf("Client area size: width=%d, height=%d\n", width, height);
} else {
printf("Failed to get client size\n");
}
```

### 返回值

整型数: - 0: 获取失败 - 1: 获取成功

---

# 获取焦点窗口 -
GetForegroundFocus

### 函数简介

获取顶层活动窗口中具有输入焦点的窗口句柄

### 接口名称

```
GetForegroundFocus
```

### DLL调用

```
long GetForegroundFocus(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

```
long hwnd = GetForegroundFocus(ola);
if (hwnd != 0) {
printf("Focus window handle: %ld\n", hwnd);
}
```

### 返回值

长整型数: - 返回具有输入焦点的窗口句柄

---

# 获取特殊窗口 -
GetSpecialWindow

### 函数简介

获取特殊窗口，如桌面窗口或任务栏窗口

### 接口名称

```
GetSpecialWindow
```

### DLL调用

```
long GetSpecialWindow(long ola, int flag)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `flag` (整型数): 指定要获取的特殊窗口类型：

0: 获取桌面窗口

- 1: 获取任务栏窗口

#### 示例:

```
// 获取桌面窗口
long desk_hwnd = GetSpecialWindow(ola, 0);
if (desk_hwnd != 0) {
printf("Desktop window handle: %ld\n", desk_hwnd);
}

// 获取任务栏窗口
long taskbar_hwnd = GetSpecialWindow(ola, 1);
if (taskbar_hwnd != 0) {
printf("Taskbar window handle: %ld\n", taskbar_hwnd);
}
```

### 返回值

长整型数: - 返回指定特殊窗口的句柄

---

# 获取窗口 - GetWindow

### 函数简介

获取给定窗口相关的窗口句柄，如父窗口、子窗口、相邻窗口等

### 接口名称

```
GetWindow
```

### DLL调用

```
long GetWindow(long ola, long hwnd, int flag)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 窗口句柄。

- `flag` (整型数): 指定要获取的窗口类型：

0: 获取父窗口

- 1: 获取第一个子窗口

- 2: 获取First窗口

- 3: 获取Last窗口

- 4: 获取下一个窗口

- 5: 获取上一个窗口

- 6: 获取拥有者窗口

- 7: 获取顶层窗口

#### 示例:

```
// 获取父窗口
long parent_hwnd = GetWindow(ola, hwnd, 0);
if (parent_hwnd != 0) {
printf("Parent window handle: %ld\n", parent_hwnd);
}

// 获取第一个子窗口
long child_hwnd = GetWindow(ola, hwnd, 1);
if (child_hwnd != 0) {
printf("First child window handle: %ld\n", child_hwnd);
}

// 获取拥有者窗口
long owner_hwnd = GetWindow(ola, hwnd, 6);
if (owner_hwnd != 0) {
printf("Owner window handle: %ld\n", owner_hwnd);
}
```

### 返回值

长整型数: - 返回指定类型的窗口句柄

---

# 获取窗口DPI感知比例
- GetWindowDpiAwarenessScale

### 函数简介

获取绑定窗口DPI感知比例

### 接口名称

```
GetWindowDpiAwarenessScale
```

### DLL调用

```
double GetWindowDpiAwarenessScale(long ola, long hwnd)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 窗口句柄。

#### 示例:

```
double scale = GetWindowDpiAwarenessScale(ola, hwnd);
```

### 返回值

双精度浮点数: - 返回窗口的DPI感知缩放比例，例如：1.5

---

# 获取窗口区域 - GetWindowRect

### 函数简介

获取指定窗口的屏幕坐标区域。该函数返回窗口的左上角和右下角坐标，这些坐标是相对于屏幕左上角的绝对坐标。返回的区域包括窗口的标题栏、边框和客户区。

### 接口名称

```
GetWindowRect
```

### DLL调用

```
int GetWindowRect(long ola, long hwnd, int* x1, int* y1, int* x2, int* y2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 目标窗口的句柄。

- `x1` (整型数指针): 返回窗口左上角的X坐标。

- `y1` (整型数指针): 返回窗口左上角的Y坐标。

- `x2` (整型数指针): 返回窗口右下角的X坐标。

- `y2` (整型数指针): 返回窗口右下角的Y坐标。

#### 示例:

```
[](#cb3-1)// 获取窗口区域
[](#cb3-2)int x1, y1, x2, y2;
[](#cb3-3)int ret = GetWindowRect(ola, hwnd, &x1, &y1, &x2, &y2);
[](#cb3-4)if (ret == 1) {
[](#cb3-5)    printf("窗口位置：左上角(%d, %d), 右下角(%d, %d)\n", x1, y1, x2, y2);
[](#cb3-6)    printf("窗口大小：宽度=%d, 高度=%d\n", x2 - x1, y2 - y1);
[](#cb3-7)} else {
[](#cb3-8)    printf("获取窗口区域失败\n");
[](#cb3-9)}
[](#cb3-10)
[](#cb3-11)// 判断鼠标是否在窗口区域内
[](#cb3-12)int mouse_x, mouse_y;
[](#cb3-13)GetCursorPos(&mouse_x, &mouse_y);
[](#cb3-14)if (mouse_x >= x1 && mouse_x <= x2 && mouse_y >= y1 && mouse_y <= y2) {
[](#cb3-15)    printf("鼠标在窗口区域内\n");
[](#cb3-16)}
[](#cb3-17)
[](#cb3-18)// 将窗口移动到屏幕中心
[](#cb3-19)int screen_width = GetSystemMetrics(SM_CXSCREEN);
[](#cb3-20)int screen_height = GetSystemMetrics(SM_CYSCREEN);
[](#cb3-21)int window_width = x2 - x1;
[](#cb3-22)int window_height = y2 - y1;
[](#cb3-23)MoveWindow(ola, hwnd,
[](#cb3-24)    (screen_width - window_width) / 2,
[](#cb3-25)    (screen_height - window_height) / 2);
```

### 返回值

整型数: - 0: 获取失败 - 1: 获取成功

### 注意事项

- 窗口必须处于可见状态，否则获取可能失败

- 返回的坐标是相对于屏幕左上角的绝对坐标

- 返回的区域包括窗口的非客户区（标题栏、边框等）

- 如果只需要获取客户区域，请使用 [GetClientRect](/窗口/获取到客户区域%20-%20GetClientRect.html)
函数

- 对于多显示器系统，坐标值可能为负数，这表示窗口位于主显示器左侧或上方的显示器上

---

# 获取窗口所在路径 -
GetWindowProcessPath

### 函数简介

获取指定窗口所在的进程的exe文件全路径

### 接口名称

```
GetWindowProcessPath
```

### DLL调用

```
long GetWindowProcessPath(long ola, long hwnd)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 窗口句柄。

#### 示例:

```
long pathPtr = GetWindowProcessPath(ola, hwnd);
if (pathPtr != 0) {
// 使用路径字符串
// ...
// 释放内存
FreeStringPtr(pathPtr);
}
```

### 返回值

字符串: - 返回进程的exe文件全路径

**注意：** - DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

---

# 获取窗口标题 -
GetWindowTitle

### 函数简介

获取窗口的标题

### 接口名称

```
GetWindowTitle
```

### DLL调用

```
long GetWindowTitle(long ola, long hwnd)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 指定的窗口句柄。

#### 示例:

```
long titlePtr = GetWindowTitle(ola, hwnd);
if (titlePtr != 0) {
// 使用标题字符串
// ...
// 释放内存
FreeStringPtr(titlePtr);
}
```

### 返回值

字符串: - 返回窗口的标题字符串

**注意：** - DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

---

# 获取窗口状态 -
GetWindowState

### 函数简介

获取指定窗口的状态属性，包括存在性、激活状态、可见性、最小化状态等。此函数用于检查窗口的各种状态属性。

### 接口名称

```
GetWindowState
```

### DLL调用

```
int GetWindowState(long ola, long hwnd, int flag)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数):
指定的窗口句柄，必须是有效的窗口句柄。

- `flag` (整型数): 要检查的窗口状态，可选值如下：

`0`: 判断窗口是否存在（检查句柄的有效性）

- `1`: 判断窗口是否处于激活状态（是否为前台窗口）

- `2`: 判断窗口是否可见（是否显示在屏幕上）

- `3`: 判断窗口是否最小化（是否处于最小化状态）

- `4`: 判断窗口是否最大化（是否处于最大化状态）

- `5`: 判断窗口是否置顶（是否总在最前）

- `6`: 判断窗口是否无响应（是否处于”未响应”状态）

- `7`: 判断窗口是否可用（是否能接收用户输入）

#### 示例:

```
[](#cb3-1)// 检查窗口是否存在并且可见
[](#cb3-2)int state = GetWindowState(ola, hwnd, 0);
[](#cb3-3)if (state == 1) {
[](#cb3-4)    printf("Window exists\n");
[](#cb3-5)    state = GetWindowState(ola, hwnd, 2);
[](#cb3-6)    if (state == 1) {
[](#cb3-7)        printf("Window is visible\n");
[](#cb3-8)    } else {
[](#cb3-9)        printf("Window is hidden\n");
[](#cb3-10)    }
[](#cb3-11)} else {
[](#cb3-12)    printf("Window does not exist\n");
[](#cb3-13)}
[](#cb3-14)
[](#cb3-15)// 检查窗口的激活和响应状态
[](#cb3-16)state = GetWindowState(ola, hwnd, 1);
[](#cb3-17)if (state == 1) {
[](#cb3-18)    printf("Window is active\n");
[](#cb3-19)    state = GetWindowState(ola, hwnd, 6);
[](#cb3-20)    if (state == 0) {
[](#cb3-21)        printf("Window is responding\n");
[](#cb3-22)    } else {
[](#cb3-23)        printf("Window is not responding\n");
[](#cb3-24)    }
[](#cb3-25)} else {
[](#cb3-26)    printf("Window is not active\n");
[](#cb3-27)}
[](#cb3-28)
[](#cb3-29)// 检查窗口的显示状态
[](#cb3-30)state = GetWindowState(ola, hwnd, 3);
[](#cb3-31)if (state == 1) {
[](#cb3-32)    printf("Window is minimized\n");
[](#cb3-33)} else {
[](#cb3-34)    state = GetWindowState(ola, hwnd, 4);
[](#cb3-35)    if (state == 1) {
[](#cb3-36)        printf("Window is maximized\n");
[](#cb3-37)    } else {
[](#cb3-38)        printf("Window is in normal state\n");
[](#cb3-39)    }
[](#cb3-40)}
```

### 返回值

整型数: - `0`: 指定的状态条件不满足（或窗口句柄无效） -
`1`: 指定的状态条件满足

### 注意事项

- 在检查窗口状态前，建议先使用flag=0确认窗口是否存在

- 某些状态可能会同时存在（如窗口可以同时是可见的和置顶的）

- 窗口的”无响应”状态检查可能需要一定时间

- 对于系统窗口或特权窗口，某些状态可能无法正确获取

---

# 获取窗口类名 -
GetWindowClass

### 函数简介

获取窗口的类名

### 接口名称

```
GetWindowClass
```

### DLL调用

```
long GetWindowClass(long ola, long hwnd)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 指定的窗口句柄。

#### 示例:

```
long classNamePtr = GetWindowClass(ola, hwnd);
if (classNamePtr != 0) {
// 使用类名字符串
// ...
// 释放内存
FreeStringPtr(classNamePtr);
}
```

### 返回值

字符串: - 返回窗口的类名字符串

**注意：** - DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

---

# 获取线程ID -
GetWindowThreadId

### 函数简介

获取指定窗口所在的线程ID

### 接口名称

```
GetWindowThreadId
```

### DLL调用

```
long GetWindowThreadId(long ola, long hwnd)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 窗口句柄。

#### 示例:

```
long threadId = GetWindowThreadId(ola, hwnd);
printf("Thread ID: %ld\n", threadId);
```

### 返回值

长整型数: - 返回窗口所在的线程ID

---

# 获取绑定窗口缩放比例
- GetScaleFromWindows

### 函数简介

获取绑定窗口缩放比例

### 接口名称

```
GetScaleFromWindows
```

### DLL调用

```
double GetScaleFromWindows(long ola, long hwnd)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 窗口句柄。

#### 示例:

```
double scale = GetScaleFromWindows(ola, hwnd);
printf("Window scale: %.2f\n", scale);
```

### 返回值

双精度浮点数: - 返回窗口的缩放比例，例如：0.8

---

# 获取进程ID -
GetWindowProcessId

### 函数简介

获取指定窗口所在的进程ID

### 接口名称

```
GetWindowProcessId
```

### DLL调用

```
long GetWindowProcessId(long ola, long hwnd)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 窗口句柄。

#### 示例:

```
long pid = GetWindowProcessId(ola, hwnd);
if (pid != 0) {
printf("Window process ID: %ld\n", pid);
}
```

### 返回值

长整型数: - 返回指定窗口所在的进程ID

---

# 获取进程详细信息 -
GetProcessInfo

### 函数简介

根据指定的pid获取进程详细信息，包括进程名、进程全路径、CPU占用率（百分比）、内存占用量（字节）

### 接口名称

```
GetProcessInfo
```

### DLL调用

```
long GetProcessInfo(long ola, long pid)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `pid` (长整型数): 进程ID。

#### 示例:

```
long strPtr = GetProcessInfo(ola, pid);
if (strPtr != 0) {
// 使用进程信息
// 返回格式: "进程名|进程路径|CPU占用率|内存占用量"
// ...
// 释放内存
FreeStringPtr(strPtr);
}
```

### 返回值

字符串: - 返回格式为 “进程名|进程路径|CPU占用率|内存占用量” -
CPU占用率以百分比表示 - 内存占用量以字节为单位

**注意：** - DLL调用返回字符串指针地址，需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
接口释放内存

---

# 获取顶层窗口句柄 -
GetForegroundWindow

### 函数简介

获取顶层活动窗口，可以获取到按键自带插件无法获取到的句柄

### 接口名称

```
GetForegroundWindow
```

### DLL调用

```
long GetForegroundWindow(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

```
long hwnd = GetForegroundWindow(ola);
if (hwnd != 0) {
printf("Foreground window handle: %ld\n", hwnd);
}
```

### 返回值

长整型数: - 返回顶层活动窗口的句柄

---

# 获取鼠标所在窗口句柄
- GetMousePointWindow

### 函数简介

获取鼠标指向的窗口句柄

### 接口名称

```
GetMousePointWindow
```

### DLL调用

```
long GetMousePointWindow(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

```
long hwnd = GetMousePointWindow(ola);
if (hwnd != 0) {
printf("Mouse point window handle: %ld\n", hwnd);
}
```

### 返回值

长整型数: - 返回鼠标指向的窗口句柄

---

# 解绑窗口 - UnBindWindow

### 函数简介

解绑窗口，取消之前通过 [BindWindow](/窗口/绑定窗口%20-%20BindWindow.html) 或 [BindWindowEx](/窗口/绑定窗口高级%20-%20BindWindowEx.html)
绑定的窗口

### 接口名称

```
UnBindWindow
```

### DLL调用

```
int UnBindWindow(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

```
int ret = UnBindWindow(ola);
if (ret == 1) {
printf("Window unbind successful\n");
} else {
printf("Window unbind failed\n");
}
```

### 返回值

整型数: - 0: 解绑失败 - 1: 解绑成功

---

# 设置剪贴板 - SetClipboard

### 函数简介

设置剪贴板的内容

### 接口名称

```
SetClipboard
```

### DLL调用

```
int SetClipboard(long ola, string value)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `value` (字符串): 要设置到剪贴板的内容。

#### 示例:

```
int ret = SetClipboard(ola, "Hello World!");
if (ret == 1) {
printf("Set clipboard content successful\n");
} else {
printf("Set clipboard content failed\n");
}
```

### 返回值

整型数: - 0: 设置失败 - 1: 设置成功

---

# 设置客户区大小 -
SetClientSize

### 函数简介

设置窗口客户区域（不包括标题栏和边框）的宽度和高度。此函数允许精确控制窗口的内容显示区域大小。

### 接口名称

```
SetClientSize
```

### DLL调用

```
int SetClientSize(long ola, long hwnd, int width, int height)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数):
指定的窗口句柄，必须是有效的窗口句柄。

- `width` (整型数):
客户区域的目标宽度（像素），必须大于0。

- `height` (整型数):
客户区域的目标高度（像素），必须大于0。

#### 示例:

```
[](#cb3-1)// 设置窗口客户区大小为800x600像素
[](#cb3-2)int ret = SetClientSize(ola, hwnd, 800, 600);
[](#cb3-3)if (ret == 1) {
[](#cb3-4)    printf("Client area size set to 800x600 successfully\n");
[](#cb3-5)
[](#cb3-6)    // 验证设置是否生效
[](#cb3-7)    RECT rect;
[](#cb3-8)    GetClientRect(hwnd, &rect);
[](#cb3-9)    printf("Actual client size: %dx%d\n",
[](#cb3-10)           rect.right - rect.left,
[](#cb3-11)           rect.bottom - rect.top);
[](#cb3-12)} else {
[](#cb3-13)    printf("Failed to set client area size\n");
[](#cb3-14)}
[](#cb3-15)
[](#cb3-16)// 设置窗口客户区大小为1024x768像素（标准XGA分辨率）
[](#cb3-17)ret = SetClientSize(ola, hwnd, 1024, 768);
[](#cb3-18)if (ret == 1) {
[](#cb3-19)    printf("Client area size set to 1024x768 successfully\n");
[](#cb3-20)} else {
[](#cb3-21)    printf("Failed to set client area size - window may be maximized or minimized\n");
[](#cb3-22)}
```

### 返回值

整型数: - `0`:
设置失败（可能原因：无效的窗口句柄、无效的尺寸值、窗口最大化或最小化等）
- `1`: 设置成功

### 注意事项

- 客户区大小不包括窗口的标题栏、菜单栏、工具栏、状态栏和边框

- 如果窗口处于最大化或最小化状态，设置可能不会生效

- 设置的尺寸不能超过屏幕的工作区大小

- 某些窗口可能有最小或最大尺寸限制

- 建议在设置尺寸前先检查窗口状态

---

# 设置窗口大小 - SetWindowSize

### 函数简介

设置窗口的整体大小，包括标题栏和边框。此函数用于调整窗口的完整外部尺寸。

### 接口名称

```
SetWindowSize
```

### DLL调用

```
int SetWindowSize(long ola, long hwnd, int width, int height)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数):
指定的窗口句柄，必须是有效的窗口句柄。

- `width` (整型数):
窗口的目标宽度（像素），包括边框，必须大于0。

- `height` (整型数):
窗口的目标高度（像素），包括标题栏和边框，必须大于0。

#### 示例:

```
[](#cb3-1)// 设置窗口大小为800x600像素
[](#cb3-2)int ret = SetWindowSize(ola, hwnd, 800, 600);
[](#cb3-3)if (ret == 1) {
[](#cb3-4)    printf("Window size set to 800x600 successfully\n");
[](#cb3-5)
[](#cb3-6)    // 验证设置是否生效
[](#cb3-7)    RECT rect;
[](#cb3-8)    GetWindowRect(hwnd, &rect);
[](#cb3-9)    printf("Actual window size: %dx%d\n",
[](#cb3-10)           rect.right - rect.left,
[](#cb3-11)           rect.bottom - rect.top);
[](#cb3-12)} else {
[](#cb3-13)    printf("Failed to set window size\n");
[](#cb3-14)}
[](#cb3-15)
[](#cb3-16)// 设置窗口大小为1024x768像素（标准XGA分辨率）
[](#cb3-17)ret = SetWindowSize(ola, hwnd, 1024, 768);
[](#cb3-18)if (ret == 1) {
[](#cb3-19)    printf("Window size set to 1024x768 successfully\n");
[](#cb3-20)
[](#cb3-21)    // 获取实际的客户区大小
[](#cb3-22)    RECT clientRect;
[](#cb3-23)    GetClientRect(hwnd, &clientRect);
[](#cb3-24)    printf("Resulting client area: %dx%d\n",
[](#cb3-25)           clientRect.right - clientRect.left,
[](#cb3-26)           clientRect.bottom - clientRect.top);
[](#cb3-27)} else {
[](#cb3-28)    printf("Failed to set window size - window may be maximized or minimized\n");
[](#cb3-29)}
```

### 返回值

整型数: - `0`:
设置失败（可能原因：无效的窗口句柄、无效的尺寸值、窗口最大化或最小化等）
- `1`: 设置成功

### 注意事项

- 此函数设置的是窗口的外部尺寸，包括标题栏、边框等装饰元素

- 实际的客户区大小会小于设置的窗口大小

- 如果窗口处于最大化或最小化状态，设置可能不会生效

- 设置的尺寸不应超过屏幕的物理分辨率

- 某些窗口可能有最小或最大尺寸限制

- 建议在设置尺寸前先检查窗口状态

- 如果需要精确控制内容区域大小，请使用 [SetClientSize](/窗口/设置客户区大小%20-%20SetClientSize.html)
函数

---

# 设置窗口标题 - SetWindowText

### 函数简介

设置窗口的标题栏文本。此函数用于动态修改窗口的显示标题，支持Unicode字符。

### 接口名称

```
SetWindowText
```

### DLL调用

```
int SetWindowText(long ola, long hwnd, string title)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数):
指定的窗口句柄，必须是有效的窗口句柄。

- `title` (字符串):
要设置的窗口标题文本，支持Unicode字符，长度不超过256个字符。

#### 示例:

```
[](#cb3-1)// 设置基本窗口标题
[](#cb3-2)int ret = SetWindowText(ola, hwnd, "My Application - Main Window");
[](#cb3-3)if (ret == 1) {
[](#cb3-4)    printf("Window title set successfully\n");
[](#cb3-5)} else {
[](#cb3-6)    printf("Failed to set window title\n");
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 设置包含动态时间的窗口标题
[](#cb3-10)char timeStr[100];
[](#cb3-11)time_t now = time(NULL);
[](#cb3-12)strftime(timeStr, sizeof(timeStr), "Window - %Y-%m-%d %H:%M:%S", localtime(&now));
[](#cb3-13)ret = SetWindowText(ola, hwnd, timeStr);
[](#cb3-14)if (ret == 1) {
[](#cb3-15)    printf("Window title updated with current time\n");
[](#cb3-16)} else {
[](#cb3-17)    printf("Failed to update window title\n");
[](#cb3-18)}
[](#cb3-19)
[](#cb3-20)// 设置包含Unicode字符的标题
[](#cb3-21)ret = SetWindowText(ola, hwnd, "应用程序 - 主窗口 - アプリ");
[](#cb3-22)if (ret == 1) {
[](#cb3-23)    printf("Unicode window title set successfully\n");
[](#cb3-24)} else {
[](#cb3-25)    printf("Failed to set Unicode window title\n");
[](#cb3-26)}
```

### 返回值

整型数: - `0`:
设置失败（可能原因：无效的窗口句柄、无效的标题文本、窗口已被销毁等） -
`1`: 设置成功

### 注意事项

- 标题文本长度不应超过256个字符

- 支持Unicode字符集，可以显示多语言文本

- 频繁更新窗口标题可能会影响性能

- 某些系统窗口可能会限制标题的修改

- 建议在设置标题前先检查窗口是否存在

- 标题更改可能会触发窗口的WM_SETTEXT消息

- 如果需要监视窗口标题变化，可以使用 [GetWindowState](/窗口/获取窗口状态%20-%20GetWindowState.html)
函数

---

# 设置窗口状态 -
SetWindowState

### 函数简介

设置窗口的显示状态、激活状态、置顶状态等。此函数提供了全面的窗口状态控制功能。

### 接口名称

```
SetWindowState
```

### DLL调用

```
int SetWindowState(long ola, long hwnd, int flag)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数):
指定的窗口句柄，必须是有效的窗口句柄。

- `flag` (整型数): 窗口状态标志，可选值如下：

`0`: 关闭指定窗口（发送WM_CLOSE消息）

- `1`: 激活指定窗口（设为前台窗口）

- `2`: 最小化指定窗口，但不激活

- `3`: 最小化指定窗口，并释放内存（适用于长期最小化）

- `4`: 最大化指定窗口，同时激活窗口

- `5`: 恢复指定窗口到正常大小，但不激活

- `6`: 隐藏指定窗口（窗口不可见但仍在运行）

- `7`: 显示指定窗口（使隐藏的窗口重新可见）

- `8`: 置顶指定窗口（窗口始终保持在最前）

- `9`: 取消置顶指定窗口（恢复正常Z序）

- `10`: 禁止指定窗口（使窗口无法接收输入）

- `11`: 取消禁止指定窗口（恢复窗口输入功能）

- `12`: 恢复并激活指定窗口（从最小化状态）

- `13`: 强制结束窗口所在进程（谨慎使用）

- `14`: 闪烁指定的窗口（吸引用户注意）

- `15`: 使指定的窗口获取输入焦点

#### 示例:

```
[](#cb3-1)// 最大化并激活窗口
[](#cb3-2)int ret = SetWindowState(ola, hwnd, 4);
[](#cb3-3)if (ret == 1) {
[](#cb3-4)    printf("Window maximized and activated successfully\n");
[](#cb3-5)} else {
[](#cb3-6)    printf("Failed to maximize and activate window\n");
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 置顶窗口并禁止输入
[](#cb3-10)ret = SetWindowState(ola, hwnd, 8);  // 先置顶
[](#cb3-11)if (ret == 1) {
[](#cb3-12)    printf("Window set to top-most successfully\n");
[](#cb3-13)    ret = SetWindowState(ola, hwnd, 10);  // 再禁止输入
[](#cb3-14)    if (ret == 1) {
[](#cb3-15)        printf("Window input disabled successfully\n");
[](#cb3-16)    }
[](#cb3-17)}
[](#cb3-18)
[](#cb3-19)// 恢复窗口正常状态
[](#cb3-20)ret = SetWindowState(ola, hwnd, 5);  // 恢复正常大小
[](#cb3-21)if (ret == 1) {
[](#cb3-22)    ret = SetWindowState(ola, hwnd, 11);  // 恢复输入
[](#cb3-23)    if (ret == 1) {
[](#cb3-24)        ret = SetWindowState(ola, hwnd, 9);  // 取消置顶
[](#cb3-25)        if (ret == 1) {
[](#cb3-26)            printf("Window restored to normal state successfully\n");
[](#cb3-27)        }
[](#cb3-28)    }
[](#cb3-29)}
```

### 返回值

整型数: - `0`:
设置失败（可能原因：无效的窗口句柄、无效的状态标志、窗口已被销毁等） -
`1`: 设置成功

### 注意事项

- 在使用强制结束进程（flag=13）时要特别谨慎，确保已保存相关数据

- 某些状态组合可能会相互影响，建议按照逻辑顺序设置

- 窗口状态的改变可能会触发窗口的相关事件和回调

- 部分状态设置可能会受到系统或应用程序的安全策略限制

---

# 设置透明度 -
SetWindowTransparent

### 函数简介

设置窗口的透明度，支持从完全透明到完全不透明的渐变效果。此函数可用于创建半透明窗口效果，增强用户界面的视觉体验。

### 接口名称

```
SetWindowTransparent
```

### DLL调用

```
int SetWindowTransparent(long ola, long hwnd, int trans)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数):
指定的窗口句柄，必须是有效的窗口句柄。

- `trans` (整型数): 透明度值，范围0-255：

`0`: 完全透明（窗口不可见，但仍然存在）

- `1-254`: 半透明（数值越小越透明）

- `255`: 完全不透明（正常显示）

#### 示例:

```
[](#cb3-1)// 设置窗口为50%透明度（trans = 128）
[](#cb3-2)int ret = SetWindowTransparent(ola, hwnd, 128);
[](#cb3-3)if (ret == 1) {
[](#cb3-4)    printf("Window transparency set to 50%%\n");
[](#cb3-5)} else {
[](#cb3-6)    printf("Failed to set window transparency\n");
[](#cb3-7)}
[](#cb3-8)
[](#cb3-9)// 创建渐变透明效果
[](#cb3-10)for (int trans = 255; trans >= 128; trans -= 16) {
[](#cb3-11)    ret = SetWindowTransparent(ola, hwnd, trans);
[](#cb3-12)    if (ret == 1) {
[](#cb3-13)        printf("Window transparency set to %d%%\n",
[](#cb3-14)               (int)((255 - trans) / 255.0 * 100));
[](#cb3-15)        Sleep(50);  // 短暂延迟以创建动画效果
[](#cb3-16)    } else {
[](#cb3-17)        printf("Failed to set transparency to %d\n", trans);
[](#cb3-18)        break;
[](#cb3-19)    }
[](#cb3-20)}
[](#cb3-21)
[](#cb3-22)// 设置窗口为80%不透明（trans = 204）
[](#cb3-23)ret = SetWindowTransparent(ola, hwnd, 204);
[](#cb3-24)if (ret == 1) {
[](#cb3-25)    printf("Window transparency set to 20%%\n");
[](#cb3-26)
[](#cb3-27)    // 验证窗口状态
[](#cb3-28)    if (GetWindowState(ola, hwnd, 2) == 1) {  // 检查是否可见
[](#cb3-29)        printf("Window is still visible with transparency\n");
[](#cb3-30)    }
[](#cb3-31)} else {
[](#cb3-32)    printf("Failed to set window transparency\n");
[](#cb3-33)}
```

### 返回值

整型数: - `0`:
设置失败（可能原因：无效的窗口句柄、不支持的系统版本、无效的透明度值等）
- `1`: 设置成功

### 注意事项

- 此功能在Windows 98操作系统上不可用

- 透明度值必须在0-255范围内，超出范围将导致设置失败

- 频繁更改透明度可能会影响系统性能

- 完全透明（trans=0）的窗口仍然可以接收鼠标事件

- 建议在设置透明度前先保存原始值，以便需要时恢复

- 某些特殊窗口（如系统窗口）可能不支持透明度设置

- 透明效果可能会影响窗口中的文本可读性

- 在使用渐变效果时，建议适当控制更新频率以平衡性能和视觉效果

---

# 通过进程找窗口 -
FindWindowByProcess

### 函数简介

根据进程名称、窗口类名和标题查找可见窗口。此函数提供了一种灵活的方式来定位特定进程的窗口。

### 接口名称

```
FindWindowByProcess
```

### DLL调用

```
long FindWindowByProcess(long ola, string process_name, string class, string title)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `process_name` (字符串):
进程名称（如”notepad.exe”），精确匹配但不区分大小写。

- `class` (字符串):
窗口类名，支持模糊匹配。如果为空字符串(““)，则匹配所有类名。

- `title` (字符串):
窗口标题，支持模糊匹配。如果为空字符串(““)，则匹配所有标题。

#### 示例:

```
[](#cb3-1)// 查找记事本进程的主窗口
[](#cb3-2)long hwnd = FindWindowByProcess(ola, "notepad.exe", "", "记事本");
[](#cb3-3)if (hwnd != 0) {
[](#cb3-4)    printf("Found Notepad window: %ld\n", hwnd);
[](#cb3-5)
[](#cb3-6)    // 验证找到的窗口
[](#cb3-7)    if (GetWindowState(ola, hwnd, 2) == 1) {  // 检查是否可见
[](#cb3-8)        printf("Window is visible\n");
[](#cb3-9)
[](#cb3-10)        // 获取完整的窗口标题
[](#cb3-11)        char title[256];
[](#cb3-12)        GetWindowText(hwnd, title, sizeof(title));
[](#cb3-13)        printf("Full window title: %s\n", title);
[](#cb3-14)    }
[](#cb3-15)} else {
[](#cb3-16)    printf("Notepad window not found\n");
[](#cb3-17)}
[](#cb3-18)
[](#cb3-19)// 查找Chrome浏览器的特定窗口
[](#cb3-20)hwnd = FindWindowByProcess(ola, "chrome.exe", "Chrome_WidgetWin_1", "Google");
[](#cb3-21)if (hwnd != 0) {
[](#cb3-22)    printf("Found Chrome window: %ld\n", hwnd);
[](#cb3-23)
[](#cb3-24)    // 检查窗口状态
[](#cb3-25)    if (GetWindowState(ola, hwnd, 1) == 1) {  // 检查是否激活
[](#cb3-26)        printf("Chrome window is active\n");
[](#cb3-27)    } else {
[](#cb3-28)        printf("Chrome window is not active\n");
[](#cb3-29)    }
[](#cb3-30)} else {
[](#cb3-31)    printf("Chrome window not found\n");
[](#cb3-32)}
[](#cb3-33)
[](#cb3-34)// 查找所有记事本窗口
[](#cb3-35)long hwndArray[10];  // 假设最多存储10个窗口句柄
[](#cb3-36)int count = 0;
[](#cb3-37)hwnd = FindWindowByProcess(ola, "notepad.exe", "", "");
[](#cb3-38)while (hwnd != 0 && count < 10) {
[](#cb3-39)    hwndArray[count++] = hwnd;
[](#cb3-40)    printf("Found Notepad window %d: %ld\n", count, hwnd);
[](#cb3-41)
[](#cb3-42)    // 继续查找下一个窗口
[](#cb3-43)    hwnd = FindWindowByProcess(ola, "notepad.exe", "", "");
[](#cb3-44)}
[](#cb3-45)printf("Total Notepad windows found: %d\n", count);
```

### 返回值

长整型数: - 非零值: 返回找到的窗口句柄 - `0`:
未找到匹配的窗口

### 注意事项

- 进程名称必须包含扩展名（如”.exe”），且不区分大小写

- 类名和标题支持模糊匹配，可以只包含部分文本

- 空字符串参数会匹配任意值，可用于通配搜索

- 如果有多个匹配的窗口，函数返回第一个找到的窗口

- 建议使用更具体的搜索条件以提高查找准确性

- 某些系统进程的窗口可能无法被找到

- 进程必须具有可见的主窗口才能被找到

- 可以结合 [GetWindowState](/窗口/获取窗口状态%20-%20GetWindowState.html)
验证找到的窗口

---

# 通过进程找窗口 -
FindWindowByProcessId

### 函数简介

根据进程ID、窗口类名和标题查找可见窗口。此函数提供了一种精确的方式来定位特定进程ID的窗口。

### 接口名称

```
FindWindowByProcessId
```

### DLL调用

```
long FindWindowByProcessId(long ola, long process_id, string class, string title)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `process_id` (长整型数):
要查找的进程ID，必须是有效的进程ID。

- `class` (字符串):
窗口类名，支持模糊匹配。如果为空字符串(““)，则匹配所有类名。

- `title` (字符串):
窗口标题，支持模糊匹配。如果为空字符串(““)，则匹配所有标题。

#### 示例:

```
[](#cb3-1)// 查找指定进程ID的主窗口
[](#cb3-2)long hwnd = FindWindowByProcessId(ola, 1234, "", "");
[](#cb3-3)if (hwnd != 0) {
[](#cb3-4)    printf("Found window for process ID 1234: %ld\n", hwnd);
[](#cb3-5)
[](#cb3-6)    // 验证窗口状态
[](#cb3-7)    if (GetWindowState(ola, hwnd, 2) == 1) {  // 检查是否可见
[](#cb3-8)        printf("Window is visible\n");
[](#cb3-9)
[](#cb3-10)        // 获取窗口信息
[](#cb3-11)        char title[256];
[](#cb3-12)        char className[256];
[](#cb3-13)        GetWindowText(hwnd, title, sizeof(title));
[](#cb3-14)        GetClassName(hwnd, className, sizeof(className));
[](#cb3-15)        printf("Window Title: %s\n", title);
[](#cb3-16)        printf("Window Class: %s\n", className);
[](#cb3-17)    }
[](#cb3-18)} else {
[](#cb3-19)    printf("No window found for process ID 1234\n");
[](#cb3-20)}
[](#cb3-21)
[](#cb3-22)// 查找指定进程ID的特定类名窗口
[](#cb3-23)hwnd = FindWindowByProcessId(ola, 5678, "Chrome_WidgetWin_1", "");
[](#cb3-24)if (hwnd != 0) {
[](#cb3-25)    printf("Found Chrome window for process ID 5678: %ld\n", hwnd);
[](#cb3-26)
[](#cb3-27)    // 检查窗口状态
[](#cb3-28)    int isActive = GetWindowState(ola, hwnd, 1);
[](#cb3-29)    int isMaximized = GetWindowState(ola, hwnd, 4);
[](#cb3-30)    printf("Window is %sactive and %smaximized\n",
[](#cb3-31)           isActive ? "" : "not ",
[](#cb3-32)           isMaximized ? "" : "not ");
[](#cb3-33)} else {
[](#cb3-34)    printf("No Chrome window found for process ID 5678\n");
[](#cb3-35)}
[](#cb3-36)
[](#cb3-37)// 查找进程的所有窗口
[](#cb3-38)void FindAllWindowsForProcess(long pid) {
[](#cb3-39)    long hwndArray[10];  // 假设最多存储10个窗口句柄
[](#cb3-40)    int count = 0;
[](#cb3-41)    long hwnd = FindWindowByProcessId(ola, pid, "", "");
[](#cb3-42)
[](#cb3-43)    while (hwnd != 0 && count < 10) {
[](#cb3-44)        hwndArray[count++] = hwnd;
[](#cb3-45)        printf("Found window %d for process %ld: %ld\n", count, pid, hwnd);
[](#cb3-46)
[](#cb3-47)        // 继续查找下一个窗口
[](#cb3-48)        hwnd = FindWindowByProcessId(ola, pid, "", "");
[](#cb3-49)    }
[](#cb3-50)
[](#cb3-51)    printf("Total windows found for process %ld: %d\n", pid, count);
[](#cb3-52)}
```

### 返回值

长整型数: - 非零值: 返回找到的窗口句柄 - `0`:
未找到匹配的窗口

### 注意事项

- 进程ID必须是当前运行的有效进程ID

- 类名和标题支持模糊匹配，可以只包含部分文本

- 空字符串参数会匹配任意值，可用于通配搜索

- 如果有多个匹配的窗口，函数返回第一个找到的窗口

- 建议先验证进程ID是否有效再进行查找

- 某些系统进程的窗口可能因权限问题无法被找到

- 进程必须具有可见的窗口才能被找到

- 可以结合 [GetWindowState](/窗口/获取窗口状态%20-%20GetWindowState.html) 和
[SetWindowState](/窗口/设置窗口状态%20-%20SetWindowState.html)
进行窗口操作

---

## 算法

# 创建图 - CreateGraph

## 函数简介

创建一个新的图数据结构，可以通过JSON格式初始化图的节点和边。
JSON数据类型解析:

```
[{
"directed": false,//是否单向,为false表示能从上海到北京,也可以从北京到上海
"from": "上海",//起点
"to": "北京",//终点
"weight": 3.0//距离权重
},
{
"directed": true,//是否单向,为true表示只能从上海到深圳,无法从深圳到上海
"from": "深圳",//起点
"to": "上海",//终点
"weight": 3.0//距离权重
}
]
```

## 接口名称

```
CreateGraph
```

## DLL调用

```
int64_t CreateGraph(int64_t instance, char* json);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
json |
字符串 |
图的JSON表示，包含节点和边的信息,传空创建一个空的图对象 |
|

### 示例

```
[](#cb4-1)// 创建OLA实例
[](#cb4-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb4-3)
[](#cb4-4)// 定义图的JSON表示
[](#cb4-5)char* json =  "[{\"directed\":true,\"from\":\"北京\",\"to\":\"上海\",\"weight\":5.0},{\"directed\":false,\"from\":\"上海\",\"to\":\"广州\",\"weight\":3.0},{\"directed\":true,\"from\":\"广州\",\"to\":\"深圳\",\"weight\":3.0}]";
[](#cb4-6)
[](#cb4-7)// 创建图
[](#cb4-8)int64_t graphPtr = CreateGraph(instance, json);
[](#cb4-9)
[](#cb4-10)// 释放资源
[](#cb4-11)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回图的指针，用于后续的图操作。如果创建失败返回0。

## 注意事项

- 返回的图指针需要调用DeleteGraph释放内存

- 确保JSON格式正确，否则可能导致创建失败

---

# 删除图 - DeleteGraph

## 函数简介

删除指定的图对象，释放相关的内存资源。

## 接口名称

```
DeleteGraph
```

## DLL调用

```
int32_t DeleteGraph(int64_t instance, int64_t graphPtr);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针，由CreateGraph接口返回 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建图
[](#cb3-5)int64_t graphPtr = CreateGraph(instance, "");
[](#cb3-6)
[](#cb3-7)// 添加一些边
[](#cb3-8)AddEdge(instance, graphPtr, "A", "B", 1.0, false);
[](#cb3-9)AddEdge(instance, graphPtr, "B", "C", 2.0, false);
[](#cb3-10)
[](#cb3-11)// 删除图
[](#cb3-12)int32_t result = DeleteGraph(instance, graphPtr);
[](#cb3-13)
[](#cb3-14)if (result == 1) {
[](#cb3-15)    printf("图删除成功\n");
[](#cb3-16)} else {
[](#cb3-17)    printf("图删除失败\n");
[](#cb3-18)}
[](#cb3-19)
[](#cb3-20)// 释放OLA实例
[](#cb3-21)DestroyCOLAPlugInterFace(instance);
```

## 返回值

成功返回1，失败返回0。

## 注意事项

- 删除操作会释放图对象占用的所有内存资源

- 删除后不能再使用该图指针进行任何操作

- 建议在程序结束前删除所有创建的图对象

- 删除操作不可逆，请确保不再需要该图对象

- 删除图对象后，相关的路径计算结果也会失效

---

# 坐标点排序 - SortPosDistance

### 函数简介

根据坐标点距离排序,用于颜色识别结果及图像识别

### 接口名称

```
SortPosDistance
```

### DLL调用

```
long SortPosDistance(long ola, string json, int type, int x, int y)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `json` (字符串): 识别结果返回值

- `type` (整型数): 1颜色识别,2图像识别

- `x` (整型数): 锚点的X坐标

- `y` (整型数): 锚点的Y坐标

#### 示例:

待补充…

### 返回值

字符串： 按顺序排列后的坐标点列表（字符串形式）

**注意**：

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 查找最近坐标点 -
FindNearestPos

### 函数简介

返回离坐标点最近的结果,用于颜色识别结果及图像识别

### 接口名称

```
FindNearestPos
```

### DLL调用

```
long FindNearestPos(long ola, string json, int type, int x, int y)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `json` (字符串): 识别结果返回值

- `type` (整型数): 识别类型：

1: 颜色识别

- 2: 图像识别

- `x` (整型数): 返回结果的X坐标

- `y` (整型数): 返回结果的Y坐标

#### 示例:

待补充…

### 返回值

字符串:

根据传入的数据返回结果如

传入颜色识别时返回{“x”:10,“y”:20}

传入图象识别时返回

```
{
"MatchVal": 0.85,
"MatchState": true,
"Index": 0,
"Angle": 45.0,
"X": 100,
"Y": 200,
"Width":100,
"Height":100
}
```

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 添加坐标节点 -
AddCoordinateNode

## 函数简介

向现有图添加或更新一个坐标节点，可按阈值将新节点连接到现有节点，并可选择使用欧几里得距离作为权重。

## 接口名称

```
AddCoordinateNode
```

## DLL调用

```
int32_t AddCoordinateNode(int64_t instance, int64_t graphPtr, char* name,
double x, double y, bool connectToExisting,
double maxDistance, bool useEuclideanDistance);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针，由 CreateGraph 或 CreateGraphFromCoordinates 返回。 |
|

|
name |
字符串 |
节点名称，若已存在则更新其坐标。 |
|

|
x |
双精度型 |
X 坐标。 |
|

|
y |
双精度型 |
Y 坐标。 |
|

|
connectToExisting |
布尔型 |
是否连接到现有节点，默认 true。 |
|

|
maxDistance |
双精度型 |
最大连接距离阈值，默认无穷大。 |
|

|
useEuclideanDistance |
布尔型 |
是否使用欧几里得距离作为边权重，默认 true。 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 先创建一张图
[](#cb3-5)int64_t graphPtr = CreateGraphFromCoordinates(instance,
[](#cb3-6)    "[{\"name\":\"A\",\"x\":0,\"y\":0},{\"name\":\"B\",\"x\":3,\"y\":4}]",
[](#cb3-7)    true, 10.0, true);
[](#cb3-8)
[](#cb3-9)// 添加新节点C，并自动连接到距离小于5的节点
[](#cb3-10)int32_t ok = AddCoordinateNode(instance, graphPtr, "C", 1.0, 1.0, true, 5.0, true);
[](#cb3-11)
[](#cb3-12)printf("AddCoordinateNode: %d\n", ok);
[](#cb3-13)
[](#cb3-14)// 释放
[](#cb3-15)DeleteGraph(instance, graphPtr);
[](#cb3-16)DestroyCOLAPlugInterFace(instance);
```

## 返回值

成功返回1，失败返回0。

## 注意事项

- 确保 graphPtr 是有效的图指针。

- 如果节点名称已存在，会更新坐标信息。

- connectToExisting 为 true 时，新节点会连接到距离小于 maxDistance
的现有节点。

---

# 添加边 - AddEdge

## 函数简介

向指定的图中添加一条边，支持有向边和无向边，可以设置边的权重。

## 接口名称

```
AddEdge
```

## DLL调用

```
int32_t AddEdge(int64_t instance, int64_t graphPtr, char* from, char* to,
double weight, bool isDirected);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针，由CreateGraph接口返回 |
|

|
from |
字符串 |
边的起点节点名称 |
|

|
to |
字符串 |
边的终点节点名称 |
|

|
weight |
双精度 |
边的权重，用于最短路径计算,当权重为0时删除对应边 |
|

|
isDirected |
布尔型 |
是否为有向边，true表示有向边，false表示无向边 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建图
[](#cb3-5)int64_t graphPtr = CreateGraph(instance, "");
[](#cb3-6)
[](#cb3-7)// 添加有向边 A->B，权重为1.0
[](#cb3-8)int32_t result1 = AddEdge(instance, graphPtr, "A", "B", 1.0, true);
[](#cb3-9)
[](#cb3-10)// 添加无向边 B-C，权重为2.0
[](#cb3-11)int32_t result2 = AddEdge(instance, graphPtr, "B", "C", 2.0, false);
[](#cb3-12)
[](#cb3-13)if (result1 == 1 && result2 == 1) {
[](#cb3-14)    printf("边添加成功\n");
[](#cb3-15)} else {
[](#cb3-16)    printf("边添加失败\n");
[](#cb3-17)}
[](#cb3-18)
[](#cb3-19)// 释放资源
[](#cb3-20)DeleteGraph(instance, graphPtr);
[](#cb3-21)DestroyCOLAPlugInterFace(instance);
```

## 返回值

成功返回1，失败返回0。

## 注意事项

- 确保from和to节点在图中存在

- 权重值应为正数，用于最短路径计算

- 有向边只允许从from到to的方向，无向边允许双向通行

- 重复添加相同的边可能会覆盖之前的权重设置

---

# 清空图 - ClearGraph

## 函数简介

清空指定图中的所有节点和边，保留图的基本结构。

## 接口名称

```
ClearGraph
```

## DLL调用

```
int32_t ClearGraph(int64_t instance, int64_t graphPtr);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针，由CreateGraph接口返回 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建图并添加边
[](#cb3-5)int64_t graphPtr = CreateGraph(instance, "");
[](#cb3-6)AddEdge(instance, graphPtr, "A", "B", 1.0, false);
[](#cb3-7)AddEdge(instance, graphPtr, "B", "C", 2.0, false);
[](#cb3-8)
[](#cb3-9)// 获取边数量
[](#cb3-10)int32_t edgeCount = GetEdgeCount(instance, graphPtr);
[](#cb3-11)printf("清空前边数量: %d\n", edgeCount);
[](#cb3-12)
[](#cb3-13)// 清空图
[](#cb3-14)int32_t result = ClearGraph(instance, graphPtr);
[](#cb3-15)
[](#cb3-16)if (result == 1) {
[](#cb3-17)    printf("图清空成功\n");
[](#cb3-18)    edgeCount = GetEdgeCount(instance, graphPtr);
[](#cb3-19)    printf("清空后边数量: %d\n", edgeCount);
[](#cb3-20)} else {
[](#cb3-21)    printf("图清空失败\n");
[](#cb3-22)}
[](#cb3-23)
[](#cb3-24)// 释放资源
[](#cb3-25)DeleteGraph(instance, graphPtr);
[](#cb3-26)DestroyCOLAPlugInterFace(instance);
```

## 返回值

成功返回1，失败返回0。

## 注意事项

- 清空操作会删除所有节点和边，但保留图的基本结构

- 清空后可以重新添加节点和边

- 清空操作不可逆，请谨慎使用

- 建议在清空前备份重要的图数据

---

# 获取图 - GetGraph

## 函数简介

获取指定图指针对应的图对象，用于验证图的有效性和获取图的基本信息。

## 接口名称

```
GetGraph
```

## DLL调用

```
int64_t GetGraph(int64_t instance, int64_t graphPtr);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针，由CreateGraph接口返回 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建图
[](#cb3-5)int64_t graphPtr = CreateGraph(instance, "");
[](#cb3-6)
[](#cb3-7)// 添加边
[](#cb3-8)AddEdge(instance, graphPtr, "A", "B", 1.0, false);
[](#cb3-9)AddEdge(instance, graphPtr, "B", "C", 2.0, false);
[](#cb3-10)AddEdge(instance, graphPtr, "C", "D", 1.5, false);
[](#cb3-11)
[](#cb3-12)// 获取图对象
[](#cb3-13)int64_t graph = GetGraph(instance, graphPtr);
[](#cb3-14)
[](#cb3-15)if (graph != 0) {
[](#cb3-16)    printf("图获取成功\n");
[](#cb3-17)} else {
[](#cb3-18)    printf("图获取失败\n");
[](#cb3-19)}
[](#cb3-20)
[](#cb3-21)// 释放资源
[](#cb3-22)DeleteGraph(instance, graphPtr);
[](#cb3-23)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回图的指针，如果图不存在或无效返回0。

## 注意事项

- 确保传入的graphPtr是有效的图指针

- 返回的指针用于验证图的有效性，不需要额外释放内存

- 在调用其他图操作函数前，建议先调用此函数验证图的有效性

---

# 获取密集矩形 - GetDenseRect

## 函数简介

查找二值化图片中像素最密集区域，可以配合找色块等功能做二次分析。

## 接口名称

```
GetDenseRect
```

## DLL调用

```
int GetDenseRect(long instance, long image, int width, int height, int* x1, int* y1, int* x2, int* y2)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
image |
长整数型 |
图像 |
|

|
width |
整数型 |
宽度 |
|

|
height |
整数型 |
高度 |
|

|
x1 |
整数型指针 |
返回左上角x坐标 |
|

|
y1 |
整数型指针 |
返回左上角y坐标 |
|

|
x2 |
整数型指针 |
返回右下角x坐标 |
|

|
y2 |
整数型指针 |
返回右下角y坐标 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1，失败返回0

---

# 获取最小生成树 -
GetMinimumSpanningTree

## 函数简介

在指定的图中计算最小生成树（Minimum Spanning
Tree），使用Kruskal或Prim算法实现。最小生成树是连接图中所有节点的树，其总权重最小。

## 接口名称

```
GetMinimumSpanningTree
```

## DLL调用

```
long GetMinimumSpanningTree(long instance, long graphPtr);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针，由CreateGraph接口返回 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建图并添加边
[](#cb3-5)int64_t graphPtr = CreateGraph(instance, "");
[](#cb3-6)AddEdge(instance, graphPtr, "A", "B", 4.0, false);
[](#cb3-7)AddEdge(instance, graphPtr, "A", "C", 2.0, false);
[](#cb3-8)AddEdge(instance, graphPtr, "B", "C", 1.0, false);
[](#cb3-9)AddEdge(instance, graphPtr, "B", "D", 5.0, false);
[](#cb3-10)AddEdge(instance, graphPtr, "C", "D", 8.0, false);
[](#cb3-11)AddEdge(instance, graphPtr, "C", "E", 10.0, false);
[](#cb3-12)AddEdge(instance, graphPtr, "D", "E", 2.0, false);
[](#cb3-13)
[](#cb3-14)// 获取最小生成树
[](#cb3-15)int64_t mstPtr = GetMinimumSpanningTree(instance, graphPtr);
[](#cb3-16)
[](#cb3-17)if (mstPtr != 0) {
[](#cb3-18)    printf("最小生成树信息:\n%s\n", (char*)mstPtr);
[](#cb3-19)    // 释放返回的字符串内存
[](#cb3-20)    FreeStringPtr(mstPtr);
[](#cb3-21)} else {
[](#cb3-22)    printf("无法生成最小生成树\n");
[](#cb3-23)}
[](#cb3-24)
[](#cb3-25)// 释放资源
[](#cb3-26)DeleteGraph(instance, graphPtr);
[](#cb3-27)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回最小生成树信息的字符串指针，格式为JSON：

```
[](#cb4-1){
[](#cb4-2)  "totalWeight": 9.0,
[](#cb4-3)  "edges": [
[](#cb4-4)    {"from": "A", "to": "C", "weight": 2.0},
[](#cb4-5)    {"from": "B", "to": "C", "weight": 1.0},
[](#cb4-6)    {"from": "D", "to": "E", "weight": 2.0},
[](#cb4-7)    {"from": "A", "to": "B", "weight": 4.0}
[](#cb4-8)  ]
[](#cb4-9)}
```

如果无法生成最小生成树返回0。

## 注意事项

- 返回的字符串指针需要调用FreeStringPtr释放内存

- 最小生成树要求图是连通的

- 如果图不连通，函数返回0

- 最小生成树包含n-1条边（n为节点数）

- 算法会考虑边的权重，选择总权重最小的树

- 适用于网络设计、电路设计等需要最小成本连接的场景

- 对于无向图，最小生成树是唯一的（当所有边权重不同时）

- 返回的JSON包含总权重和所有边的详细信息

---

# 获取最短距离 -
GetShortestDistance

## 函数简介

在指定的图中计算从起点到终点的最短距离，使用Dijkstra算法实现。

## 接口名称

```
GetShortestDistance
```

## DLL调用

```
double GetShortestDistance(int64_t instance, int64_t graphPtr, char* from, char* to);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针，由CreateGraph接口返回 |
|

|
from |
字符串 |
起点节点名称 |
|

|
to |
字符串 |
终点节点名称 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建图并添加边
[](#cb3-5)int64_t graphPtr = CreateGraph(instance, "");
[](#cb3-6)AddEdge(instance, graphPtr, "A", "B", 1.0, false);
[](#cb3-7)AddEdge(instance, graphPtr, "B", "C", 2.0, false);
[](#cb3-8)AddEdge(instance, graphPtr, "C", "D", 1.0, false);
[](#cb3-9)AddEdge(instance, graphPtr, "A", "D", 5.0, false);
[](#cb3-10)
[](#cb3-11)// 获取从A到D的最短距离
[](#cb3-12)double distance = GetShortestDistance(instance, graphPtr, "A", "D");
[](#cb3-13)
[](#cb3-14)if (distance >= 0) {
[](#cb3-15)    printf("最短距离: %.2f\n", distance);
[](#cb3-16)} else {
[](#cb3-17)    printf("未找到路径\n");
[](#cb3-18)}
[](#cb3-19)
[](#cb3-20)// 释放资源
[](#cb3-21)DeleteGraph(instance, graphPtr);
[](#cb3-22)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回从起点到终点的最短距离（双精度浮点数）。如果不存在路径返回-1。

## 注意事项

- 距离是路径上所有边权重的总和

- 如果两点间不存在路径，函数返回-1

- 确保from和to节点在图中存在

- 算法会考虑边的权重，寻找总权重最小的路径

- 对于无向图，from到to的距离等于to到from的距离

---

# 获取最短路径 -
GetShortestPath

## 函数简介

在指定的图中计算从起点到终点的最短路径，使用Dijkstra算法实现。

## 接口名称

```
GetShortestPath
```

## DLL调用

```
int64_t GetShortestPath(int64_t instance, int64_t graphPtr, char* from, char* to);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针，由CreateGraph接口返回 |
|

|
from |
字符串 |
起点节点名称 |
|

|
to |
字符串 |
终点节点名称 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建图并添加边
[](#cb3-5)int64_t graphPtr = CreateGraph(instance, "");
[](#cb3-6)AddEdge(instance, graphPtr, "A", "B", 1.0, false);
[](#cb3-7)AddEdge(instance, graphPtr, "B", "C", 2.0, false);
[](#cb3-8)AddEdge(instance, graphPtr, "C", "D", 1.0, false);
[](#cb3-9)AddEdge(instance, graphPtr, "A", "D", 5.0, false);
[](#cb3-10)
[](#cb3-11)// 获取从A到D的最短路径
[](#cb3-12)int64_t pathPtr = GetShortestPath(instance, graphPtr, "A", "D");
[](#cb3-13)
[](#cb3-14)if (pathPtr != 0) {
[](#cb3-15)    printf("最短路径: %s\n", (char*)pathPtr);
[](#cb3-16)    // 释放返回的字符串内存
[](#cb3-17)    FreeStringPtr(pathPtr);
[](#cb3-18)} else {
[](#cb3-19)    printf("未找到路径\n");
[](#cb3-20)}
[](#cb3-21)
[](#cb3-22)// 释放资源
[](#cb3-23)DeleteGraph(instance, graphPtr);
[](#cb3-24)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回最短路径的字符串指针，格式为：

```
"A|B|C|D"
```

如果不存在路径返回0。

## 注意事项

- 返回的字符串指针需要调用FreeStringPtr释放内存

- 确保from和to节点在图中存在

- 如果两点间不存在路径，函数返回0

- 路径按顺序返回从起点到终点的所有节点

- 算法会考虑边的权重，寻找总权重最小的路径

---

# 获取最短路径到所有节点
- GetShortestPathToAllNodes

## 函数简介

在指定的图中计算从起点到所有其他节点的最短路径，使用Dijkstra算法实现。此函数可以一次性获取从指定起点到图中所有可达节点的最短路径信息。

## 接口名称

```
GetShortestPathToAllNodes
```

## DLL调用

```
long GetShortestPathToAllNodes(long instance, long graphPtr, string startNode);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针，由CreateGraph接口返回 |
|

|
startNode |
字符串 |
起点节点名称 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建图并添加边
[](#cb3-5)int64_t graphPtr = CreateGraph(instance, "");
[](#cb3-6)AddEdge(instance, graphPtr, "A", "B", 1.0, false);
[](#cb3-7)AddEdge(instance, graphPtr, "B", "C", 2.0, false);
[](#cb3-8)AddEdge(instance, graphPtr, "C", "D", 1.0, false);
[](#cb3-9)AddEdge(instance, graphPtr, "A", "D", 5.0, false);
[](#cb3-10)AddEdge(instance, graphPtr, "B", "E", 3.0, false);
[](#cb3-11)AddEdge(instance, graphPtr, "E", "F", 1.0, false);
[](#cb3-12)
[](#cb3-13)// 获取从A到所有节点的最短路径
[](#cb3-14)int64_t pathsPtr = GetShortestPathToAllNodes(instance, graphPtr, "A");
[](#cb3-15)
[](#cb3-16)if (pathsPtr != 0) {
[](#cb3-17)    printf("从A到所有节点的最短路径:\n%s\n", (char*)pathsPtr);
[](#cb3-18)    // 释放返回的字符串内存
[](#cb3-19)    FreeStringPtr(pathsPtr);
[](#cb3-20)} else {
[](#cb3-21)    printf("未找到路径\n");
[](#cb3-22)}
[](#cb3-23)
[](#cb3-24)// 释放资源
[](#cb3-25)DeleteGraph(instance, graphPtr);
[](#cb3-26)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回包含所有最短路径信息的字符串指针，格式为字符串：

```
[](#cb4-1){
[](#cb4-2)  "A": {"distance": 0, "path": "A"},
[](#cb4-3)  "B": {"distance": 1, "path": "A|B"},
[](#cb4-4)  "C": {"distance": 3, "path": "A|B|C"},
[](#cb4-5)  "D": {"distance": 4, "path": "A|B|C|D"},
[](#cb4-6)  "E": {"distance": 4, "path": "A|B|E"},
[](#cb4-7)  "F": {"distance": 5, "path": "A|B|E|F"}
[](#cb4-8)}
```

如果不存在路径返回0。

## 注意事项

- 返回的字符串指针需要调用FreeStringPtr释放内存

- 确保startNode节点在图中存在

- 如果起点无法到达某些节点，这些节点将不会出现在结果中

- 返回的JSON格式包含每个可达节点的距离和路径信息

- 算法会考虑边的权重，寻找总权重最小的路径

- 适用于需要分析图中所有节点可达性的场景

- 对于大型图，计算时间可能较长

---

# 获取有向图最小生成树
- GetMinimumArborescence

## 函数简介

在指定的有向图中计算最小树形图（Minimum
Arborescence），使用Edmonds算法实现。最小树形图是从根节点出发，能够到达所有其他节点的有向树，其总权重最小。

## 接口名称

```
GetMinimumArborescence
```

## DLL调用

```
long GetMinimumArborescence(long instance, long graphPtr, string root);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针，由CreateGraph接口返回 |
|

|
root |
字符串 |
根节点名称 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建有向图并添加边
[](#cb3-5)int64_t graphPtr = CreateGraph(instance, "");
[](#cb3-6)AddEdge(instance, graphPtr, "A", "B", 4.0, true);
[](#cb3-7)AddEdge(instance, graphPtr, "A", "C", 2.0, true);
[](#cb3-8)AddEdge(instance, graphPtr, "B", "C", 1.0, true);
[](#cb3-9)AddEdge(instance, graphPtr, "B", "D", 5.0, true);
[](#cb3-10)AddEdge(instance, graphPtr, "C", "D", 8.0, true);
[](#cb3-11)AddEdge(instance, graphPtr, "C", "E", 10.0, true);
[](#cb3-12)AddEdge(instance, graphPtr, "D", "E", 2.0, true);
[](#cb3-13)AddEdge(instance, graphPtr, "E", "A", 3.0, true);
[](#cb3-14)
[](#cb3-15)// 获取以A为根的最小树形图
[](#cb3-16)int64_t mstPtr = GetMinimumArborescence(instance, graphPtr, "A");
[](#cb3-17)
[](#cb3-18)if (mstPtr != 0) {
[](#cb3-19)    printf("最小树形图信息:\n%s\n", (char*)mstPtr);
[](#cb3-20)    // 释放返回的字符串内存
[](#cb3-21)    FreeStringPtr(mstPtr);
[](#cb3-22)} else {
[](#cb3-23)    printf("无法生成最小树形图\n");
[](#cb3-24)}
[](#cb3-25)
[](#cb3-26)// 释放资源
[](#cb3-27)DeleteGraph(instance, graphPtr);
[](#cb3-28)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回最小生成树信息的字符串指针，格式为JSON：

```
[](#cb4-1){
[](#cb4-2)  "totalWeight": 9.0,
[](#cb4-3)  "edges": [
[](#cb4-4)    {"from": "A", "to": "C", "weight": 2.0},
[](#cb4-5)    {"from": "B", "to": "C", "weight": 1.0},
[](#cb4-6)    {"from": "D", "to": "E", "weight": 2.0},
[](#cb4-7)    {"from": "A", "to": "B", "weight": 4.0}
[](#cb4-8)  ]
[](#cb4-9)}
```

如果无法生成最小树形图返回0。

## 注意事项

- 返回的字符串指针需要调用FreeStringPtr释放内存

- 最小树形图要求从根节点能够到达所有其他节点

- 如果根节点无法到达某些节点，函数返回0

- 最小树形图包含n-1条边（n为节点数）

- 算法会考虑边的权重，选择总权重最小的有向树

- 适用于网络设计、依赖关系分析等需要最小成本有向连接的场景

- 对于有向图，最小树形图可能不唯一

- 返回的字符串格式为”起点->终点(权重)“的列表

---

# 获取有向路径到所有节点
- GetDirectedPathToAllNodes

## 函数简介

在指定的有向图中计算从起点到所有其他节点的有向路径，使用有向图最短路径算法实现。此函数可以一次性获取从指定起点到图中所有可达节点的有向路径信息。

## 接口名称

```
GetDirectedPathToAllNodes
```

## DLL调用

```
long GetDirectedPathToAllNodes(long instance, long graphPtr, string startNode);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针，由CreateGraph接口返回 |
|

|
startNode |
字符串 |
起点节点名称 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建有向图并添加边
[](#cb3-5)int64_t graphPtr = CreateGraph(instance, "");
[](#cb3-6)AddEdge(instance, graphPtr, "A", "B", 4.0, true);
[](#cb3-7)AddEdge(instance, graphPtr, "A", "C", 2.0, true);
[](#cb3-8)AddEdge(instance, graphPtr, "B", "C", 1.0, true);
[](#cb3-9)AddEdge(instance, graphPtr, "B", "D", 5.0, true);
[](#cb3-10)AddEdge(instance, graphPtr, "C", "D", 8.0, true);
[](#cb3-11)AddEdge(instance, graphPtr, "C", "E", 10.0, true);
[](#cb3-12)AddEdge(instance, graphPtr, "D", "E", 2.0, true);
[](#cb3-13)AddEdge(instance, graphPtr, "E", "A", 3.0, true);
[](#cb3-14)
[](#cb3-15)// 获取从A到所有节点的有向路径
[](#cb3-16)int64_t pathsPtr = GetDirectedPathToAllNodes(instance, graphPtr, "A");
[](#cb3-17)
[](#cb3-18)if (pathsPtr != 0) {
[](#cb3-19)    printf("从A到所有节点的有向路径:\n%s\n", (char*)pathsPtr);
[](#cb3-20)    // 释放返回的字符串内存
[](#cb3-21)    FreeStringPtr(pathsPtr);
[](#cb3-22)} else {
[](#cb3-23)    printf("未找到路径\n");
[](#cb3-24)}
[](#cb3-25)
[](#cb3-26)// 释放资源
[](#cb3-27)DeleteGraph(instance, graphPtr);
[](#cb3-28)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回包含所有最短路径信息的字符串指针，格式为字符串：

```
[](#cb4-1){
[](#cb4-2)  "A": {"distance": 0, "path": "A"},
[](#cb4-3)  "B": {"distance": 1, "path": "A|B"},
[](#cb4-4)  "C": {"distance": 3, "path": "A|B|C"},
[](#cb4-5)  "D": {"distance": 4, "path": "A|B|C|D"},
[](#cb4-6)  "E": {"distance": 4, "path": "A|B|E"},
[](#cb4-7)  "F": {"distance": 5, "path": "A|B|E|F"}
[](#cb4-8)}
```

如果不存在路径返回0。

## 注意事项

- 返回的字符串指针需要调用FreeStringPtr释放内存

- 确保startNode节点在图中存在

- 如果起点无法到达某些节点，这些节点将不会出现在结果中

- 返回的字符串包含每个可达节点的有向路径和距离信息

- 算法会考虑边的权重，寻找总权重最小的有向路径

- 适用于需要分析有向图中所有节点可达性的场景

- 对于大型有向图，计算时间可能较长

- 有向路径考虑了边的方向性，与无向图的最短路径不同

---

# 获取节点坐标 -
GetNodeCoordinates

## 函数简介

获取指定节点的坐标信息，返回 JSON 字符串。

返回格式：`{"name":"节点名","x":坐标X,"y":坐标Y}`。

## 接口名称

```
GetNodeCoordinates
```

## DLL调用

```
int64_t GetNodeCoordinates(int64_t instance, int64_t graphPtr, char* name);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针。 |
|

|
name |
字符串 |
节点名称。 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)int64_t g = CreateGraphFromCoordinates(instance,
[](#cb3-5)    "[{\"name\":\"A\",\"x\":0,\"y\":0}]", false, 0.0, true);
[](#cb3-6)
[](#cb3-7)int64_t sp = GetNodeCoordinates(instance, g, "A");
[](#cb3-8)if (sp) {
[](#cb3-9)    printf("%s\n", (char*)sp);
[](#cb3-10)    FreeStringPtr(sp);
[](#cb3-11)}
[](#cb3-12)
[](#cb3-13)DeleteGraph(instance, g);
[](#cb3-14)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回节点坐标信息的 JSON 字符串指针；节点不存在返回0。

## 注意事项

- 返回的字符串指针需要调用 FreeStringPtr 释放内存。

- 确保 graphPtr 是有效的图指针。

- 如果节点不存在，返回0。

---

# 获取节点数量 - GetNodeCount

## 函数简介

获取指定图中节点的总数量。

## 接口名称

```
GetNodeCount
```

## DLL调用

```
int32_t GetNodeCount(int64_t instance, int64_t graphPtr);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针，由CreateGraph接口返回 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建图
[](#cb3-5)int64_t graphPtr = CreateGraph(instance, "");
[](#cb3-6)
[](#cb3-7)// 获取节点数量
[](#cb3-8)int32_t nodeCount = GetNodeCount(instance, graphPtr);
[](#cb3-9)printf("节点数量: %d\n", nodeCount);
[](#cb3-10)
[](#cb3-11)// 添加边
[](#cb3-12)AddEdge(instance, graphPtr, "A", "B", 1.0, false);
[](#cb3-13)AddEdge(instance, graphPtr, "B", "C", 2.0, false);
[](#cb3-14)
[](#cb3-15)// 再次获取节点数量（应该相同）
[](#cb3-16)nodeCount = GetNodeCount(instance, graphPtr);
[](#cb3-17)printf("添加边后节点数量: %d\n", nodeCount);
[](#cb3-18)
[](#cb3-19)// 释放资源
[](#cb3-20)DeleteGraph(instance, graphPtr);
[](#cb3-21)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回图中节点的总数量（整数）。

## 注意事项

- 节点数量在创建图时确定，添加边不会改变节点数量

- 如果图指针无效，可能返回0或错误值

- 节点数量反映了图的基本规模

- 建议在创建图后立即检查节点数量以验证图的正确性

---

# 获取边数量 - GetEdgeCount

## 函数简介

获取指定图中边的总数量。

## 接口名称

```
GetEdgeCount
```

## DLL调用

```
int32_t GetEdgeCount(int64_t instance, int64_t graphPtr);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针，由CreateGraph接口返回 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 创建图
[](#cb3-5)int64_t graphPtr = CreateGraph(instance, "");
[](#cb3-6)
[](#cb3-7)// 获取初始边数量
[](#cb3-8)int32_t edgeCount = GetEdgeCount(instance, graphPtr);
[](#cb3-9)printf("初始边数量: %d\n", edgeCount);
[](#cb3-10)
[](#cb3-11)// 添加边
[](#cb3-12)AddEdge(instance, graphPtr, "A", "B", 1.0, false);
[](#cb3-13)AddEdge(instance, graphPtr, "B", "C", 2.0, false);
[](#cb3-14)AddEdge(instance, graphPtr, "C", "D", 1.5, false);
[](#cb3-15)
[](#cb3-16)// 获取添加边后的数量
[](#cb3-17)edgeCount = GetEdgeCount(instance, graphPtr);
[](#cb3-18)printf("添加边后边数量: %d\n", edgeCount);
[](#cb3-19)
[](#cb3-20)// 释放资源
[](#cb3-21)DeleteGraph(instance, graphPtr);
[](#cb3-22)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回图中边的总数量（整数）。

## 注意事项

- 边数量会随着AddEdge操作而增加

- 对于无向图，一条边只计算一次

- 如果图指针无效，可能返回0或错误值

- 边数量反映了图的连接复杂度

- 建议在添加边后检查边数量以验证操作是否成功

---

# 获取连接状态 -
GetNodeConnectionStatus

## 函数简介

查询两个节点之间是否存在连接。

返回值：1 表示可以连接；0 表示不能连接；-1
表示节点不存在或图指针无效。

## 接口名称

```
GetNodeConnectionStatus
```

## DLL调用

```
int32_t GetNodeConnectionStatus(int64_t instance, int64_t graphPtr,
char* from, char* to);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针。 |
|

|
from |
字符串 |
起始节点名称。 |
|

|
to |
字符串 |
目标节点名称。 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)int64_t g = CreateGraphFromCoordinates(instance,
[](#cb3-5)    "[{\"name\":\"A\",\"x\":0,\"y\":0},{\"name\":\"B\",\"x\":3,\"y\":4}]",
[](#cb3-6)    false, 0.0, true);
[](#cb3-7)
[](#cb3-8)// 建立连接
[](#cb3-9)SetNodeConnection(instance, g, "A", "B", true, -1.0);
[](#cb3-10)
[](#cb3-11)// 查询连接状态
[](#cb3-12)int32_t st = GetNodeConnectionStatus(instance, g, "A", "B");
[](#cb3-13)printf("status: %d\n", st); // 1
[](#cb3-14)
[](#cb3-15)DeleteGraph(instance, g);
[](#cb3-16)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1：可以连接；0：不能连接；-1：节点不存在或图指针无效。

## 注意事项

- 确保 graphPtr 是有效的图指针。

- 节点需已存在于图中。

---

# 获取随机整数 -
GetRandomNumber

## 函数简介

获取指定范围内的随机整数。此函数使用线程独立的随机种子，确保每个线程的随机数生成都是独立的，避免多线程环境下的随机数冲突问题。

## 接口名称

```
GetRandomNumber
```

## DLL调用

```
int GetRandomNumber(long instance, int min, int max)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
min |
整数型 |
随机数的最小值（包含） |
|

|
max |
整数型 |
随机数的最大值（包含） |
|

### 示例

```
[](#cb3-1)// 生成1到100之间的随机整数
[](#cb3-2)int32_t randomNum = GetRandomNumber(ola, 1, 100);
[](#cb3-3)printf("随机数: %d\n", randomNum);
[](#cb3-4)
[](#cb3-5)// 生成-50到50之间的随机整数
[](#cb3-6)int32_t randomRange = GetRandomNumber(ola, -50, 50);
[](#cb3-7)printf("随机范围数: %d\n", randomRange);
[](#cb3-8)
[](#cb3-9)// 生成0到9之间的随机整数（用于验证码）
[](#cb3-10)int32_t verifyCode = GetRandomNumber(ola, 0, 9);
[](#cb3-11)printf("验证码: %d\n", verifyCode);
[](#cb3-12)
[](#cb3-13)// 生成坐标范围内的随机位置
[](#cb3-14)int32_t randomX = GetRandomNumber(ola, 100, 800);
[](#cb3-15)int32_t randomY = GetRandomNumber(ola, 100, 600);
[](#cb3-16)printf("随机坐标: (%d, %d)\n", randomX, randomY);
```

## 返回值

int32_t: 返回指定范围内的随机整数

## 注意事项

- 返回的随机数包含最小值和最大值

- 每个线程使用独立的随机种子，确保多线程环境下的随机性

- 适用于需要生成随机整数用于测试、游戏、模拟等场景

- 与 [GetRandomDouble](/算法/获取随机浮点数%20-%20GetRandomDouble.html)
函数配合使用可以实现更复杂的随机数需求

- 建议在程序初始化时调用一次，确保随机种子正确初始化

---

# 获取随机浮点数 -
GetRandomDouble

## 函数简介

获取指定范围内的随机浮点数。此函数使用线程独立的随机种子，确保每个线程的随机数生成都是独立的，避免多线程环境下的随机数冲突问题。适用于需要高精度随机数的场景。

## 接口名称

```
GetRandomDouble
```

## DLL调用

```
double GetRandomDouble(long instance, double min, double max)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
min |
双精度浮点数 |
随机数的最小值（包含） |
|

|
max |
双精度浮点数 |
随机数的最大值（包含） |
|

### 示例

```
[](#cb3-1)// 生成0.0到1.0之间的随机浮点数
[](#cb3-2)double randomDouble = GetRandomDouble(ola, 0.0, 1.0);
[](#cb3-3)printf("随机浮点数: %f\n", randomDouble);
[](#cb3-4)
[](#cb3-5)// 生成-1.0到1.0之间的随机浮点数
[](#cb3-6)double randomRange = GetRandomDouble(ola, -1.0, 1.0);
[](#cb3-7)printf("随机范围数: %f\n", randomRange);
[](#cb3-8)
[](#cb3-9)// 生成概率值（0.0到1.0）
[](#cb3-10)double probability = GetRandomDouble(ola, 0.0, 1.0);
[](#cb3-11)if (probability < 0.5) {
[](#cb3-12)    printf("概率小于50%%\n");
[](#cb3-13)} else {
[](#cb3-14)    printf("概率大于等于50%%\n");
[](#cb3-15)}
[](#cb3-16)
[](#cb3-17)// 生成坐标范围内的随机位置（浮点精度）
[](#cb3-18)double randomX = GetRandomDouble(ola, 100.0, 800.0);
[](#cb3-19)double randomY = GetRandomDouble(ola, 100.0, 600.0);
[](#cb3-20)printf("随机坐标: (%.2f, %.2f)\n", randomX, randomY);
[](#cb3-21)
[](#cb3-22)// 生成角度值（0到360度）
[](#cb3-23)double randomAngle = GetRandomDouble(ola, 0.0, 360.0);
[](#cb3-24)printf("随机角度: %.2f度\n", randomAngle);
```

## 返回值

double: 返回指定范围内的随机浮点数

## 注意事项

- 返回的随机数包含最小值和最大值

- 每个线程使用独立的随机种子，确保多线程环境下的随机性

- 适用于需要高精度随机数的场景，如概率计算、模拟仿真等

- 与 [GetRandomNumber](/算法/获取随机整数%20-%20GetRandomNumber.html)
函数配合使用可以实现更复杂的随机数需求

- 浮点数精度取决于系统实现，通常为双精度（64位）

- 建议在程序初始化时调用一次，确保随机种子正确初始化

---

# 设置节点连接 -
SetNodeConnection

## 函数简介

设置两个节点间的连接关系。可新增/更新边（并设置权重），或删除对应的边。

当 canConnect 为 true 且 weight 为 -1
时，自动使用欧几里得距离作为边权重。

## 接口名称

```
SetNodeConnection
```

## DLL调用

```
int32_t SetNodeConnection(int64_t instance, int64_t graphPtr, char* from,
char* to, bool canConnect, double weight);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
graphPtr |
长整数型 |
图的指针。 |
|

|
from |
字符串 |
起始节点名称。 |
|

|
to |
字符串 |
目标节点名称。 |
|

|
canConnect |
布尔型 |
是否可以连接（true 创建/更新边；false 删除边）。 |
|

|
weight |
双精度型 |
连接权重（canConnect 为 true 时使用；-1 表示使用欧氏距离）。 |
|

### 示例

```
[](#cb3-1)// 创建OLA实例
[](#cb3-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)int64_t g = CreateGraphFromCoordinates(instance,
[](#cb3-5)    "[{\"name\":\"A\",\"x\":0,\"y\":0},{\"name\":\"B\",\"x\":3,\"y\":4}]",
[](#cb3-6)    false, 0.0, true);
[](#cb3-7)
[](#cb3-8)// 建立 A->B 的连接，使用欧氏距离作为权重
[](#cb3-9)int32_t ok = SetNodeConnection(instance, g, "A", "B", true, -1.0);
[](#cb3-10)printf("SetNodeConnection: %d\n", ok);
[](#cb3-11)
[](#cb3-12)// 断开 A->B 的连接
[](#cb3-13)ok = SetNodeConnection(instance, g, "A", "B", false, 0.0);
[](#cb3-14)
[](#cb3-15)DeleteGraph(instance, g);
[](#cb3-16)DestroyCOLAPlugInterFace(instance);
```

## 返回值

成功返回1，失败返回0。

## 注意事项

- 确保 graphPtr 是有效的图指针。

- 节点必须已存在于图中。

- 设置连接关系会影响路径计算。

- 如果 canConnect 为 false，会删除对应的边。

---

# 识别图片排除指定区域 -
ExcludePos

### 函数简介

排除掉指定区域结果,用于颜色识别结果及图像识别

### 接口名称

```
ExcludePos
```

### DLL调用

```
long ExcludePos(long ola, string json, int type, int x1, int y1, int x2, int y2)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `json` (字符串): 识别返回的结果

- `type` (整型数): 1颜色识别,2图像识别

- `x1` (整型数): 排除区域左上角的X坐标

- `y1` (整型数): 排除区域左上角的Y坐标

- `x2` (整型数): 排除区域右下角的X坐标

- `y2` (整型数): 排除区域右下角的Y坐标

#### 示例:

待补充…

### 返回值

字符串:

返回排除掉指定区域结果的json数据

**注意**：

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 通过坐标创建图 -
CreateGraphFromCoordinates

## 函数简介

根据坐标点数据创建图（支持自动连接）。支持数组与对象两种 JSON
格式；可按最大距离阈值连接，并可选择使用欧几里得距离作为边权重。

支持的 JSON 格式：

```
// 数组格式
[{"name":"A","x":0,"y":0},{"name":"B","x":1,"y":1}]

// 对象格式
{"A":{"x":0,"y":0},"B":{"x":1,"y":1}}
```

## 接口名称

```
CreateGraphFromCoordinates
```

## DLL调用

```
int64_t CreateGraphFromCoordinates(int64_t instance, char* json,
bool connectAll, double maxDistance,
bool useEuclideanDistance);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
json |
字符串 |
坐标节点 JSON 数据，支持数组与对象两种格式。 |
|

|
connectAll |
布尔型 |
是否连接所有节点，默认 true。 |
|

|
maxDistance |
双精度型 |
最大连接距离阈值，默认无穷大（不限制）。 |
|

|
useEuclideanDistance |
布尔型 |
是否使用欧几里得距离作为边权重，默认 true。 |
|

### 示例

```
[](#cb4-1)// 创建OLA实例
[](#cb4-2)int64_t instance = CreateCOLAPlugInterFace();
[](#cb4-3)
[](#cb4-4)// 使用数组格式坐标数据
[](#cb4-5)char* json = "[{\"name\":\"A\",\"x\":0,\"y\":0},{\"name\":\"B\",\"x\":3,\"y\":4},{\"name\":\"C\",\"x\":6,\"y\":8}]";
[](#cb4-6)
[](#cb4-7)// 按欧氏距离、阈值10自动连接全部可连节点
[](#cb4-8)int64_t graphPtr = CreateGraphFromCoordinates(instance, json, true, 10.0, true);
[](#cb4-9)
[](#cb4-10)if (graphPtr == 0) {
[](#cb4-11)    printf("创建失败\n");
[](#cb4-12)} else {
[](#cb4-13)    printf("创建成功\n");
[](#cb4-14)}
[](#cb4-15)
[](#cb4-16)// 释放资源
[](#cb4-17)DeleteGraph(instance, graphPtr);
[](#cb4-18)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回图的指针，失败返回0。

## 注意事项

- 返回的图指针需要调用 DeleteGraph 释放内存。

- connectAll 为 true 时，所有节点间距离小于 maxDistance
的会被连接。

- useEuclideanDistance 为 true 时，边权重为节点间的欧几里得距离。

- 确保 JSON 格式正确；节点名需唯一。

---

## 系统

# 关闭内核对象 - CloseHandle

## 函数简介

关闭一个内核对象句柄。内核对象包括文件、线程、进程、互斥量、事件等系统资源。此函数用于释放系统资源，防止句柄泄漏。

## 接口名称

```
CloseHandle
```

## DLL调用

```
int CloseHandle(long instance, long handle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
handle |
长整数型 |
要关闭的对象句柄 |
|

### 示例

```
[](#cb3-1)// 关闭文件句柄
[](#cb3-2)long file_handle = CreateFile(ola, "test.txt", GENERIC_READ, 0, OPEN_EXISTING, 0, 0);
[](#cb3-3)if (file_handle != 0) {
[](#cb3-4)    // 使用文件句柄进行操作
[](#cb3-5)    // ...
[](#cb3-6)
[](#cb3-7)    // 关闭文件句柄
[](#cb3-8)    int result = CloseHandle(ola, file_handle);
[](#cb3-9)    if (result == 1) {
[](#cb3-10)        printf("文件句柄关闭成功\n");
[](#cb3-11)    } else {
[](#cb3-12)        printf("文件句柄关闭失败\n");
[](#cb3-13)    }
[](#cb3-14)}
[](#cb3-15)
[](#cb3-16)// 关闭线程句柄
[](#cb3-17)long thread_handle = CreateRemoteThread(ola, target_hwnd, start_address, parameter, 0, &thread_id);
[](#cb3-18)if (thread_handle != 0) {
[](#cb3-19)    // 等待线程完成
[](#cb3-20)    // ...
[](#cb3-21)
[](#cb3-22)    // 关闭线程句柄
[](#cb3-23)    int result = CloseHandle(ola, thread_handle);
[](#cb3-24)    if (result == 1) {
[](#cb3-25)        printf("线程句柄关闭成功\n");
[](#cb3-26)    }
[](#cb3-27)}
[](#cb3-28)
[](#cb3-29)// 关闭进程句柄
[](#cb3-30)long process_handle = OpenProcess(ola, PROCESS_ALL_ACCESS, FALSE, process_id);
[](#cb3-31)if (process_handle != 0) {
[](#cb3-32)    // 对进程进行操作
[](#cb3-33)    // ...
[](#cb3-34)
[](#cb3-35)    // 关闭进程句柄
[](#cb3-36)    int result = CloseHandle(ola, process_handle);
[](#cb3-37)    if (result == 1) {
[](#cb3-38)        printf("进程句柄关闭成功\n");
[](#cb3-39)    }
[](#cb3-40)}
[](#cb3-41)
[](#cb3-42)// 关闭互斥量句柄
[](#cb3-43)long mutex_handle = CreateMutex(ola, NULL, FALSE, "MyMutex");
[](#cb3-44)if (mutex_handle != 0) {
[](#cb3-45)    // 使用互斥量
[](#cb3-46)    // ...
[](#cb3-47)
[](#cb3-48)    // 关闭互斥量句柄
[](#cb3-49)    int result = CloseHandle(ola, mutex_handle);
[](#cb3-50)    if (result == 1) {
[](#cb3-51)        printf("互斥量句柄关闭成功\n");
[](#cb3-52)    }
[](#cb3-53)}
[](#cb3-54)
[](#cb3-55)// 批量关闭句柄
[](#cb3-56)long handles[] = {handle1, handle2, handle3, handle4};
[](#cb3-57)int handle_count = sizeof(handles) / sizeof(handles[0]);
[](#cb3-58)
[](#cb3-59)for (int i = 0; i < handle_count; i++) {
[](#cb3-60)    if (handles[i] != 0) {
[](#cb3-61)        int result = CloseHandle(ola, handles[i]);
[](#cb3-62)        if (result == 1) {
[](#cb3-63)            printf("句柄 %d 关闭成功\n", i);
[](#cb3-64)        } else {
[](#cb3-65)            printf("句柄 %d 关闭失败\n", i);
[](#cb3-66)        }
[](#cb3-67)    }
[](#cb3-68)}
```

## 返回值

整数型: - 1: 关闭成功 - 0: 关闭失败

## 注意事项

- 关闭句柄后，该句柄将不再有效，不能再次使用

- 关闭无效句柄不会导致错误，但会返回失败

- 建议在不再需要句柄时立即关闭，避免句柄泄漏

- 某些系统对象（如进程、线程）在关闭句柄后仍可能继续运行

- 关闭句柄不会影响其他引用同一对象的句柄

- 在程序退出前应确保所有句柄都已正确关闭

---

# 创建子进程 -
CreateChildProcess

## 函数简介

创建子进程。

## 接口名称

```
CreateChildProcess
```

## DLL调用

```
int CreateChildProcess(long instance, string applicationName, string commandLine, string currentDirectory, int showType, int parentProcessId)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
applicationName |
字符串 |
进程路径，如C:.exe |
|

|
commandLine |
字符串 |
命令行 如:aabbcc |
|

|
currentDirectory |
字符串 |
启动目录, 可空 |
|

|
showType |
整数型 |
显示方式 1隐藏 2普通激活 3最小化激活 4最大化激活 5普通不激活
6最小化不激活，省略默认为普通激活 |
|

|
parentProcessId |
整数型 |
父进程ID，支持系统进程ID，只要是调试权限能Open的进程 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回子进程ID,失败返回0

---

# 创建远程线程 -
CreateRemoteThread

## 函数简介

在指定的窗口所在进程中创建一个线程。此函数可以在目标进程中创建新线程来执行代码，常用于进程注入、代码注入等高级系统编程场景。

## 接口名称

```
CreateRemoteThread
```

## DLL调用

```
long CreateRemoteThread(long instance, long hwnd, long lpStartAddress, long lpParameter, int dwCreationFlags, long* lpThreadId)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄或者进程ID |
|

|
lpStartAddress |
长整数型 |
线程入口地址 |
|

|
lpParameter |
长整数型 |
线程参数 |
|

|
dwCreationFlags |
整数型 |
创建标志，控制线程的创建方式 |
|

|
lpThreadId |
长整数型指针 |
返回线程ID的指针 |
|

### 示例

```
[](#cb3-1)// 在目标进程中创建简单线程
[](#cb3-2)long target_hwnd = FindWindow(ola, "Notepad", "");
[](#cb3-3)if (target_hwnd != 0) {
[](#cb3-4)    long thread_id = 0;
[](#cb3-5)    long start_address = 0x10000000; // 线程入口地址
[](#cb3-6)    long parameter = 123; // 线程参数
[](#cb3-7)
[](#cb3-8)    long thread_handle = CreateRemoteThread(ola, target_hwnd, start_address, parameter, 0, &thread_id);
[](#cb3-9)    if (thread_handle != 0) {
[](#cb3-10)        printf("远程线程创建成功，线程ID: %ld\n", thread_id);
[](#cb3-11)
[](#cb3-12)        // 等待线程完成
[](#cb3-13)        // ...
[](#cb3-14)
[](#cb3-15)        // 关闭线程句柄
[](#cb3-16)        CloseHandle(ola, thread_handle);
[](#cb3-17)    } else {
[](#cb3-18)        printf("远程线程创建失败\n");
[](#cb3-19)    }
[](#cb3-20)}
[](#cb3-21)
[](#cb3-22)// 使用进程ID创建远程线程
[](#cb3-23)long process_id = GetWindowProcessId(ola, target_hwnd);
[](#cb3-24)if (process_id != 0) {
[](#cb3-25)    long thread_id = 0;
[](#cb3-26)    long start_address = 0x20000000;
[](#cb3-27)    long parameter = 456;
[](#cb3-28)
[](#cb3-29)    long thread_handle = CreateRemoteThread(ola, process_id, start_address, parameter, 0, &thread_id);
[](#cb3-30)    if (thread_handle != 0) {
[](#cb3-31)        printf("使用进程ID创建线程成功，线程ID: %ld\n", thread_id);
[](#cb3-32)        CloseHandle(ola, thread_handle);
[](#cb3-33)    }
[](#cb3-34)}
[](#cb3-35)
[](#cb3-36)// 创建挂起状态的线程
[](#cb3-37)long target_hwnd = FindWindow(ola, "Calculator", "");
[](#cb3-38)if (target_hwnd != 0) {
[](#cb3-39)    long thread_id = 0;
[](#cb3-40)    long start_address = 0x30000000;
[](#cb3-41)    long parameter = 789;
[](#cb3-42)    int creation_flags = CREATE_SUSPENDED; // 创建挂起状态的线程
[](#cb3-43)
[](#cb3-44)    long thread_handle = CreateRemoteThread(ola, target_hwnd, start_address, parameter, creation_flags, &thread_id);
[](#cb3-45)    if (thread_handle != 0) {
[](#cb3-46)        printf("挂起线程创建成功，线程ID: %ld\n", thread_id);
[](#cb3-47)
[](#cb3-48)        // 恢复线程执行
[](#cb3-49)        // ResumeThread(ola, thread_handle);
[](#cb3-50)
[](#cb3-51)        CloseHandle(ola, thread_handle);
[](#cb3-52)    }
[](#cb3-53)}
[](#cb3-54)
[](#cb3-55)// 批量创建多个线程
[](#cb3-56)long target_hwnd = FindWindow(ola, "TargetApp", "");
[](#cb3-57)if (target_hwnd != 0) {
[](#cb3-58)    long thread_handles[5];
[](#cb3-59)    long thread_ids[5];
[](#cb3-60)
[](#cb3-61)    for (int i = 0; i < 5; i++) {
[](#cb3-62)        long start_address = 0x10000000 + i * 0x1000;
[](#cb3-63)        long parameter = i * 100;
[](#cb3-64)
[](#cb3-65)        thread_handles[i] = CreateRemoteThread(ola, target_hwnd, start_address, parameter, 0, &thread_ids[i]);
[](#cb3-66)        if (thread_handles[i] != 0) {
[](#cb3-67)            printf("线程 %d 创建成功，ID: %ld\n", i, thread_ids[i]);
[](#cb3-68)        }
[](#cb3-69)    }
[](#cb3-70)
[](#cb3-71)    // 等待所有线程完成
[](#cb3-72)    // ...
[](#cb3-73)
[](#cb3-74)    // 关闭所有线程句柄
[](#cb3-75)    for (int i = 0; i < 5; i++) {
[](#cb3-76)        if (thread_handles[i] != 0) {
[](#cb3-77)            CloseHandle(ola, thread_handles[i]);
[](#cb3-78)        }
[](#cb3-79)    }
[](#cb3-80)}
```

## 返回值

长整数型: - 成功返回线程句柄 - 失败返回0

## 注意事项

- 创建远程线程需要相应的进程权限

- 线程入口地址必须在目标进程的地址空间内有效

- 建议在不再需要线程句柄时调用CloseHandle关闭

- 创建挂起状态的线程可以使用CREATE_SUSPENDED标志

- 线程参数会传递给线程函数作为参数

- 此函数适用于进程注入、代码注入等高级应用

- 使用不当可能导致目标进程崩溃或系统不稳定

- 建议在测试环境中充分验证后再用于生产环境

---

# 启动安全守护 -
StartSecurityGuard

### 函数简介

启动安全守护功能。可以简单防止程序被调试破解

### 接口名称

```
StartSecurityGuard
```

### DLL调用

```
int StartSecurityGuard(long instance)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

整型数:

1 : 成功

其他 : 失败

---

# 启用调试权限 -
EnableDebugPrivilege

## 函数简介

启用调试权限。

## 接口名称

```
EnableDebugPrivilege
```

## DLL调用

```
int EnableDebugPrivilege(long instance)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1,失败返回0

---

# 延时指定毫秒 - Delay

### 函数简介

延时指定的毫秒,过程中不阻塞UI操作. 一般高级语言使用.按键用不到.

### 接口名称

```
Delay
```

### DLL调用

```
int Delay(int delay)
```

#### 参数定义:

- `delay` (整型数): 延时时间（毫秒）。

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 延时指定随机时间 - Delays

### 函数简介

延时指定范围内随机毫秒,过程中不阻塞UI操作.
一般高级语言使用.按键用不到.

### 接口名称

```
Delays
```

### DLL调用

```
int Delays(int min, int max)
```

#### 参数定义:

- `min` (整型数): 最小延时时间（毫秒）

- `max` (整型数): 最大延时时间（毫秒）

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 拖动文件到窗口 -
SendDropFiles

### 函数简介

拖动文件到指定窗口

### 接口名称

```
SendDropFiles
```

### DLL调用

```
int SendDropFiles(long instance, long hwnd, string file_path)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `hwnd` (长整型数): 窗口句柄

- `file_path` (字符串): 文件路径

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 控制窗口任务栏图标 -
ShowTaskBarIcon

### 函数简介

显示或者隐藏指定窗口在任务栏的图标

### 接口名称

```
ShowTaskBarIcon
```

### DLL调用

```
int ShowTaskBarIcon(long ola, long hwnd, int show)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `hwnd` (长整型数): 窗口句柄。

- `show` (布尔值): 是否显示任务栏图标。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 检查字体平滑 -
CheckFontSmooth

## 函数简介

检查字体平滑。

## 接口名称

```
CheckFontSmooth
```

## DLL调用

```
int CheckFontSmooth(long instance)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1,失败返回0

---

# 检测UAC状态 - CheckUAC

### 函数简介

检测当前系统是否有开启UAC(用户账户控制).

### 接口名称

```
CheckUAC
```

### DLL调用

```
int CheckUAC(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

整型数:

0 : 关闭

1 : 开启

---

# 系统权限启动 - SystemStart

## 函数简介

以系统用户启动进程

## 接口名称

```
SystemStart
```

## DLL调用

```
int SystemStart(long instance, string applicationName, string commandLine)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
applicationName |
字符串 |
应用程序名称 |
|

|
commandLine |
字符串 |
命令行 如:aabbcc |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回子进程ID,失败返回0

---

# 终止进程 - TerminateProcess

## 函数简介

终止进程。

## 接口名称

```
TerminateProcess
```

## DLL调用

```
int TerminateProcess(long instance, long pid)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
pid |
长整数型 |
进程ID |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1,失败返回0

---

# 终止进程树 -
TerminateProcessTree

## 函数简介

终止进程树。

## 接口名称

```
TerminateProcessTree
```

## DLL调用

```
int TerminateProcessTree(long instance, long pid)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
pid |
长整数型 |
进程ID |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1,失败返回0

## 注意事项

- 终止进程树会终止所有子进程

---

# 获取进程启动命令行 -
GetCommandLine

## 函数简介

获取进程启动命令行。

## 接口名称

```
GetCommandLine
```

## DLL调用

```
long GetCommandLine(long instance, long hwnd)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

返回二进制字符串的指针

## 注意事项

- 返回的字符串指针需调用FreeStringPtr释放内存

---

# 设置UAC状态 - SetUAC

### 函数简介

开启/关闭UAC

### 接口名称

```
SetUAC
```

### DLL调用

```
int SetUAC(long ola, int enable)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `enable` (布尔值): 是否启用UAC。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 设置字体平滑 - SetFontSmooth

## 函数简介

设置字体平滑。

## 接口名称

```
SetFontSmooth
```

## DLL调用

```
int SetFontSmooth(long instance, int enable)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
enable |
整数型 |
是否启用 |
|

### 示例

```
[](#cb3-1)// 示例代码待补充
```

## 返回值

成功返回1,失败返回0

---

# 运行指定程序 - RunApp

### 函数简介

运行指定的应用程序

### 接口名称

```
RunApp
```

### DLL调用

```
int RunApp(long ola, string appPath, int mode)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `appPath` (字符串): 要运行的程序路径

- `mode` (整型数): 运行模式：

0: 普通模式

- 1: 加强模式

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

## 视频处理

# 从图片序列创建视频 -
CreateVideoFromImages

## 函数简介

从图片序列创建视频。

## 接口名称

```
CreateVideoFromImages
```

## DLL调用

```
int32_t CreateVideoFromImages(int64_t instance, string imageDir, string outputPath, double fps, string codec)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
imageDir |
字符串 |
图片目录路径 |
|

|
outputPath |
字符串 |
输出视频路径 |
|

|
fps |
双精度 |
帧率 |
|

|
codec |
字符串 |
编解码器（“H264”等） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t result = CreateVideoFromImages(instance, "C:/images", "output.mp4", 30.0, "H264");
[](#cb3-3)if (result == 1) {
[](#cb3-4)    printf("视频创建成功\n");
[](#cb3-5)} else {
[](#cb3-6)    printf("视频创建失败\n");
[](#cb3-7)}
[](#cb3-8)DestroyCOLAPlugInterFace(instance);
```

## 返回值

- 0: 失败

- 1: 成功

## 注意事项

- 图片文件名应按字母顺序排列

---

# 保存当前帧为图片文件 -
SaveCurrentFrame

## 函数简介

保存当前帧为图片文件。

## 接口名称

```
SaveCurrentFrame
```

## DLL调用

```
int32_t SaveCurrentFrame(int64_t instance, int64_t videoHandle, string outputPath, int32_t quality)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

|
outputPath |
字符串 |
输出文件路径 |
|

|
quality |
整数型 |
图片质量（对于JPEG，范围0-100） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int32_t result = SaveCurrentFrame(instance, videoHandle, "C:/frame.png", 90);
[](#cb3-4)if (result == 1) {
[](#cb3-5)    printf("保存当前帧成功\n");
[](#cb3-6)} else {
[](#cb3-7)    printf("保存失败\n");
[](#cb3-8)}
[](#cb3-9)CloseVideo(instance, videoHandle);
[](#cb3-10)DestroyCOLAPlugInterFace(instance);
```

## 返回值

- 0: 失败

- 1: 成功

---

# 保存指定帧为图片文件 -
SaveFrameAtIndex

## 函数简介

保存指定帧为图片文件。

## 接口名称

```
SaveFrameAtIndex
```

## DLL调用

```
int32_t SaveFrameAtIndex(int64_t instance, int64_t videoHandle, int32_t frameIndex,
string outputPath, int32_t quality)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

|
frameIndex |
整数型 |
帧索引 |
|

|
outputPath |
字符串 |
输出文件路径 |
|

|
quality |
整数型 |
图片质量（对于JPEG，范围0-100） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int32_t result = SaveFrameAtIndex(instance, videoHandle, 100, "C:/frame100.png", 90);
[](#cb3-4)if (result == 1) {
[](#cb3-5)    printf("保存第100帧成功\n");
[](#cb3-6)} else {
[](#cb3-7)    printf("保存失败\n");
[](#cb3-8)}
[](#cb3-9)CloseVideo(instance, videoHandle);
[](#cb3-10)DestroyCOLAPlugInterFace(instance);
```

## 返回值

- 0: 失败

- 1: 成功

---

# 关闭视频 - CloseVideo

## 函数简介

关闭视频并释放资源。

## 接口名称

```
CloseVideo
```

## DLL调用

```
int32_t CloseVideo(int64_t instance, int64_t videoHandle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)// ... 使用视频 ...
[](#cb3-4)int32_t result = CloseVideo(instance, videoHandle);
[](#cb3-5)if (result == 1) {
[](#cb3-6)    printf("视频关闭成功\n");
[](#cb3-7)} else {
[](#cb3-8)    printf("视频关闭失败\n");
[](#cb3-9)}
[](#cb3-10)DestroyCOLAPlugInterFace(instance);
```

## 返回值

- 0: 失败

- 1: 成功

## 注意事项

- 使用完视频后必须调用此函数释放资源

- 关闭后不能再使用该视频句柄进行任何操作

---

# 剪切视频片段 - TrimVideo

## 函数简介

剪切视频片段。

## 接口名称

```
TrimVideo
```

## DLL调用

```
int32_t TrimVideo(int64_t instance, string inputPath, string outputPath, double startTime, double endTime)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
inputPath |
字符串 |
输入视频路径 |
|

|
outputPath |
字符串 |
输出视频路径 |
|

|
startTime |
双精度 |
起始时间（秒） |
|

|
endTime |
双精度 |
结束时间（秒） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t result = TrimVideo(instance, "input.mp4", "output.mp4", 10.0, 30.0);
[](#cb3-3)if (result == 1) {
[](#cb3-4)    printf("视频剪切成功\n");
[](#cb3-5)} else {
[](#cb3-6)    printf("视频剪切失败\n");
[](#cb3-7)}
[](#cb3-8)DestroyCOLAPlugInterFace(instance);
```

## 返回值

- 0: 失败

- 1: 成功

---

# 将当前帧转换为Base64字符串
- FrameToBase64

## 函数简介

将当前帧转换为Base64字符串。

## 接口名称

```
FrameToBase64
```

## DLL调用

```
int64_t FrameToBase64(int64_t instance, int64_t videoHandle, string format)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

|
format |
字符串 |
图片格式（“png”、“jpg”等） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int64_t base64Ptr = FrameToBase64(instance, videoHandle, "png");
[](#cb3-4)if (base64Ptr != 0) {
[](#cb3-5)    printf("Base64字符串: %s\n", (char*)base64Ptr);
[](#cb3-6)    FreeStringPtr(instance, base64Ptr);
[](#cb3-7)}
[](#cb3-8)CloseVideo(instance, videoHandle);
[](#cb3-9)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回Base64编码的图片数据字符串指针，需调用FreeStringPtr释放；失败返回0。

## 注意事项

- 返回的字符串指针必须调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放内存

---

# 快速提取单帧 -
ExtractSingleFrame

## 函数简介

快速提取单帧（无需保持视频打开状态）。

## 接口名称

```
ExtractSingleFrame
```

## DLL调用

```
int64_t ExtractSingleFrame(int64_t instance, string videoPath, int32_t frameIndex)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoPath |
字符串 |
视频文件路径 |
|

|
frameIndex |
整数型 |
帧索引 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t imageHandle = ExtractSingleFrame(instance, "test.mp4", 100);
[](#cb3-3)if (imageHandle != 0) {
[](#cb3-4)    printf("提取第100帧成功，图像句柄: %lld\n", (long long)imageHandle);
[](#cb3-5)    // 使用图像句柄...
[](#cb3-6)    FreeImagePtr(instance, imageHandle);
[](#cb3-7)} else {
[](#cb3-8)    printf("提取失败\n");
[](#cb3-9)}
[](#cb3-10)DestroyCOLAPlugInterFace(instance);
```

## 返回值

图像句柄（BGRA格式），失败返回0。

## 注意事项

- 返回的图像句柄需调用FreeImagePtr释放

- 此方法无需保持视频打开状态，适合单次提取

---

# 快速提取视频第一帧 -
ExtractThumbnail

## 函数简介

快速提取视频第一帧（常用于缩略图）。

## 接口名称

```
ExtractThumbnail
```

## DLL调用

```
int64_t ExtractThumbnail(int64_t instance, string videoPath)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoPath |
字符串 |
视频文件路径 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t imageHandle = ExtractThumbnail(instance, "test.mp4");
[](#cb3-3)if (imageHandle != 0) {
[](#cb3-4)    printf("提取缩略图成功，图像句柄: %lld\n", (long long)imageHandle);
[](#cb3-5)    // 使用图像句柄...
[](#cb3-6)    FreeImagePtr(instance, imageHandle);
[](#cb3-7)} else {
[](#cb3-8)    printf("提取失败\n");
[](#cb3-9)}
[](#cb3-10)DestroyCOLAPlugInterFace(instance);
```

## 返回值

图像句柄（BGRA格式），失败返回0。

## 注意事项

- 返回的图像句柄需调用FreeImagePtr释放

- 常用于生成视频缩略图

---

# 快速获取视频文件信息 -
GetVideoInfoFromPath

## 函数简介

快速获取视频文件信息（无需打开整个视频）。

## 接口名称

```
GetVideoInfoFromPath
```

## DLL调用

```
int64_t GetVideoInfoFromPath(int64_t instance, string videoPath)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoPath |
字符串 |
视频文件路径 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t jsonPtr = GetVideoInfoFromPath(instance, "test.mp4");
[](#cb3-3)if (jsonPtr != 0) {
[](#cb3-4)    printf("视频信息: %s\n", (char*)jsonPtr);
[](#cb3-5)    FreeStringPtr(instance, jsonPtr);
[](#cb3-6)}
[](#cb3-7)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回包含视频信息的JSON字符串指针，需调用FreeStringPtr释放；失败返回0。

## 注意事项

- 返回的字符串指针必须调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放内存

- 此方法无需打开整个视频，速度较快

---

# 打开摄像头设备 - OpenCamera

## 函数简介

打开摄像头设备，返回视频句柄。

## 接口名称

```
OpenCamera
```

## DLL调用

```
int64_t OpenCamera(int64_t instance, int32_t deviceIndex)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
deviceIndex |
整数型 |
摄像头设备索引（默认0） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenCamera(instance, 0);
[](#cb3-3)if (videoHandle != 0) {
[](#cb3-4)    printf("摄像头打开成功，句柄: %lld\n", (long long)videoHandle);
[](#cb3-5)    // 使用完毕后需调用CloseVideo释放
[](#cb3-6)    CloseVideo(instance, videoHandle);
[](#cb3-7)} else {
[](#cb3-8)    printf("摄像头打开失败\n");
[](#cb3-9)}
[](#cb3-10)DestroyCOLAPlugInterFace(instance);
```

## 返回值

视频句柄，失败返回0。

## 注意事项

- 返回的句柄用于后续的视频操作，使用完毕后需调用CloseVideo释放

- deviceIndex通常从0开始，表示第一个摄像头设备

- 确保摄像头设备已连接且未被其他程序占用

---

# 打开视频文件 - OpenVideo

## 函数简介

打开视频文件，返回视频句柄。支持本地文件和网络流。

## 接口名称

```
OpenVideo
```

## DLL调用

```
int64_t OpenVideo(int64_t instance, string videoPath)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoPath |
字符串 |
视频文件路径（支持本地文件和网络流） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "C:/videos/test.mp4");
[](#cb3-3)if (videoHandle != 0) {
[](#cb3-4)    printf("视频打开成功，句柄: %lld\n", (long long)videoHandle);
[](#cb3-5)    // 使用完毕后需调用CloseVideo释放
[](#cb3-6)    CloseVideo(instance, videoHandle);
[](#cb3-7)} else {
[](#cb3-8)    printf("视频打开失败\n");
[](#cb3-9)}
[](#cb3-10)DestroyCOLAPlugInterFace(instance);
```

## 返回值

视频句柄，失败返回0。

## 注意事项

- 返回的句柄用于后续的视频操作，使用完毕后需调用CloseVideo释放

- 支持本地文件路径和网络流URL

- 确保视频文件格式被支持

- 网络流需要稳定的网络连接

---

# 批量提取视频帧并保存为文件
- ExtractFramesToFiles

## 函数简介

批量提取视频帧并保存为文件。

## 接口名称

```
ExtractFramesToFiles
```

## DLL调用

```
int32_t ExtractFramesToFiles(int64_t instance, int64_t videoHandle, int32_t startFrame,
int32_t endFrame, int32_t step, string outputDir,
string imageFormat, int32_t jpegQuality)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

|
startFrame |
整数型 |
起始帧索引 |
|

|
endFrame |
整数型 |
结束帧索引（-1表示到视频末尾） |
|

|
step |
整数型 |
帧间隔（1表示每帧都提取） |
|

|
outputDir |
字符串 |
输出目录 |
|

|
imageFormat |
字符串 |
图像格式（“png”、“jpg”等） |
|

|
jpegQuality |
整数型 |
JPEG质量（0-100） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int32_t count = ExtractFramesToFiles(instance, videoHandle, 0, 100, 5, "C:/frames", "png", 90);
[](#cb3-4)printf("提取了 %d 帧\n", count);
[](#cb3-5)CloseVideo(instance, videoHandle);
[](#cb3-6)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回提取的帧数，失败返回0。

---

# 按时间间隔提取帧并保存为文件
- ExtractFramesByInterval

## 函数简介

按时间间隔提取帧并保存为文件。

## 接口名称

```
ExtractFramesByInterval
```

## DLL调用

```
int32_t ExtractFramesByInterval(int64_t instance, int64_t videoHandle, double intervalSeconds,
string outputDir, string imageFormat)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

|
intervalSeconds |
双精度 |
时间间隔（秒） |
|

|
outputDir |
字符串 |
输出目录 |
|

|
imageFormat |
字符串 |
图像格式（“png”、“jpg”等） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int32_t count = ExtractFramesByInterval(instance, videoHandle, 1.0, "C:/frames", "png");
[](#cb3-4)printf("提取了 %d 帧\n", count);
[](#cb3-5)CloseVideo(instance, videoHandle);
[](#cb3-6)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回提取的帧数，失败返回0。

---

# 提取关键帧 -
ExtractKeyFrames

## 函数简介

提取关键帧（基于场景变化检测）。

## 接口名称

```
ExtractKeyFrames
```

## DLL调用

```
int32_t ExtractKeyFrames(int64_t instance, int64_t videoHandle, double threshold,
int32_t maxFrames, string outputDir, string imageFormat)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

|
threshold |
双精度 |
场景变化阈值（0-1） |
|

|
maxFrames |
整数型 |
最大提取帧数（0表示不限制） |
|

|
outputDir |
字符串 |
输出目录 |
|

|
imageFormat |
字符串 |
图像格式（“png”、“jpg”等） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int32_t count = ExtractKeyFrames(instance, videoHandle, 0.3, 100, "C:/frames", "png");
[](#cb3-4)printf("提取了 %d 个关键帧\n", count);
[](#cb3-5)CloseVideo(instance, videoHandle);
[](#cb3-6)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回提取的关键帧数，失败返回0。

---

# 检查视频文件是否有效 -
IsValidVideoFile

## 函数简介

检查视频文件是否有效。

## 接口名称

```
IsValidVideoFile
```

## DLL调用

```
int32_t IsValidVideoFile(int64_t instance, string videoPath)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoPath |
字符串 |
视频文件路径 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t isValid = IsValidVideoFile(instance, "test.mp4");
[](#cb3-3)if (isValid == 1) {
[](#cb3-4)    printf("视频文件有效\n");
[](#cb3-5)} else {
[](#cb3-6)    printf("视频文件无效\n");
[](#cb3-7)}
[](#cb3-8)DestroyCOLAPlugInterFace(instance);
```

## 返回值

- 0: 无效

- 1: 有效

---

# 检查视频是否已打开 -
IsVideoOpened

## 函数简介

检查视频是否已打开。

## 接口名称

```
IsVideoOpened
```

## DLL调用

```
int32_t IsVideoOpened(int64_t instance, int64_t videoHandle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int32_t isOpened = IsVideoOpened(instance, videoHandle);
[](#cb3-4)if (isOpened == 1) {
[](#cb3-5)    printf("视频已打开\n");
[](#cb3-6)} else {
[](#cb3-7)    printf("视频未打开\n");
[](#cb3-8)}
[](#cb3-9)DestroyCOLAPlugInterFace(instance);
```

## 返回值

- 0: 未打开

- 1: 已打开

---

# 检测视频中的场景变化点
- DetectSceneChanges

## 函数简介

检测视频中的场景变化点。

## 接口名称

```
DetectSceneChanges
```

## DLL调用

```
int64_t DetectSceneChanges(int64_t instance, string videoPath, double threshold)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoPath |
字符串 |
视频文件路径 |
|

|
threshold |
双精度 |
场景变化阈值（0-1） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t jsonPtr = DetectSceneChanges(instance, "test.mp4", 0.3);
[](#cb3-3)if (jsonPtr != 0) {
[](#cb3-4)    printf("场景变化帧索引: %s\n", (char*)jsonPtr);
[](#cb3-5)    // JSON格式：[0, 123, 456, ...]
[](#cb3-6)    FreeStringPtr(instance, jsonPtr);
[](#cb3-7)}
[](#cb3-8)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回场景变化帧索引的JSON数组字符串，需调用FreeStringPtr释放；失败返回0。

JSON格式：[0, 123, 456, …]

## 注意事项

- 返回的字符串指针必须调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放内存

---

# 检测视频中的运动 -
DetectMotion

## 函数简介

检测视频中的运动。

## 接口名称

```
DetectMotion
```

## DLL调用

```
int64_t DetectMotion(int64_t instance, string videoPath, double threshold)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoPath |
字符串 |
视频文件路径 |
|

|
threshold |
双精度 |
运动检测阈值（建议值：30.0） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t jsonPtr = DetectMotion(instance, "test.mp4", 30.0);
[](#cb3-3)if (jsonPtr != 0) {
[](#cb3-4)    printf("运动帧索引: %s\n", (char*)jsonPtr);
[](#cb3-5)    // JSON格式：[10, 25, 67, ...]
[](#cb3-6)    FreeStringPtr(instance, jsonPtr);
[](#cb3-7)}
[](#cb3-8)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回包含运动的帧索引的JSON数组字符串，需调用FreeStringPtr释放；失败返回0。

JSON格式：[10, 25, 67, …]

## 注意事项

- 返回的字符串指针必须调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放内存

---

# 获取当前帧位置 -
GetCurrentFrameIndex

## 函数简介

获取当前帧位置。

## 接口名称

```
GetCurrentFrameIndex
```

## DLL调用

```
int32_t GetCurrentFrameIndex(int64_t instance, int64_t videoHandle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int32_t frameIndex = GetCurrentFrameIndex(instance, videoHandle);
[](#cb3-4)printf("当前帧索引: %d\n", frameIndex);
[](#cb3-5)CloseVideo(instance, videoHandle);
[](#cb3-6)DestroyCOLAPlugInterFace(instance);
```

## 返回值

当前帧索引，失败返回-1。

---

# 获取当前时间戳 -
GetCurrentTimestamp

## 函数简介

获取当前时间戳。

## 接口名称

```
GetCurrentTimestamp
```

## DLL调用

```
double GetCurrentTimestamp(int64_t instance, int64_t videoHandle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)double timestamp = GetCurrentTimestamp(instance, videoHandle);
[](#cb3-4)printf("当前时间戳: %.2f 秒\n", timestamp);
[](#cb3-5)CloseVideo(instance, videoHandle);
[](#cb3-6)DestroyCOLAPlugInterFace(instance);
```

## 返回值

当前时间戳（秒），失败返回0.0。

---

# 获取视频基本信息 -
GetVideoInfo

## 函数简介

获取视频基本信息（JSON格式）。

## 接口名称

```
GetVideoInfo
```

## DLL调用

```
int64_t GetVideoInfo(int64_t instance, int64_t videoHandle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int64_t jsonPtr = GetVideoInfo(instance, videoHandle);
[](#cb3-4)if (jsonPtr != 0) {
[](#cb3-5)    printf("视频信息: %s\n", (char*)jsonPtr);
[](#cb3-6)    // JSON包含：width, height, fps, totalFrames, duration, codecName, fileSize
[](#cb3-7)    FreeStringPtr(instance, jsonPtr);
[](#cb3-8)}
[](#cb3-9)CloseVideo(instance, videoHandle);
[](#cb3-10)DestroyCOLAPlugInterFace(instance);
```

## 返回值

返回包含视频信息的JSON字符串指针，需调用FreeStringPtr释放；失败返回0。

JSON包含：width, height, fps, totalFrames, duration, codecName,
fileSize

## 注意事项

- 返回的字符串指针必须调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放内存

---

# 获取视频宽度 - GetVideoWidth

## 函数简介

获取视频宽度。

## 接口名称

```
GetVideoWidth
```

## DLL调用

```
int32_t GetVideoWidth(int64_t instance, int64_t videoHandle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int32_t width = GetVideoWidth(instance, videoHandle);
[](#cb3-4)printf("视频宽度: %d 像素\n", width);
[](#cb3-5)CloseVideo(instance, videoHandle);
[](#cb3-6)DestroyCOLAPlugInterFace(instance);
```

## 返回值

视频宽度（像素），失败返回0。

---

# 获取视频帧率 - GetVideoFPS

## 函数简介

获取视频帧率。

## 接口名称

```
GetVideoFPS
```

## DLL调用

```
double GetVideoFPS(int64_t instance, int64_t videoHandle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)double fps = GetVideoFPS(instance, videoHandle);
[](#cb3-4)printf("视频帧率: %.2f FPS\n", fps);
[](#cb3-5)CloseVideo(instance, videoHandle);
[](#cb3-6)DestroyCOLAPlugInterFace(instance);
```

## 返回值

视频帧率（FPS），失败返回0.0。

---

# 获取视频总帧数 -
GetVideoTotalFrames

## 函数简介

获取视频总帧数。

## 接口名称

```
GetVideoTotalFrames
```

## DLL调用

```
int32_t GetVideoTotalFrames(int64_t instance, int64_t videoHandle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int32_t totalFrames = GetVideoTotalFrames(instance, videoHandle);
[](#cb3-4)printf("视频总帧数: %d\n", totalFrames);
[](#cb3-5)CloseVideo(instance, videoHandle);
[](#cb3-6)DestroyCOLAPlugInterFace(instance);
```

## 返回值

视频总帧数，失败返回0。

---

# 获取视频时长 -
GetVideoDuration

## 函数简介

获取视频时长。

## 接口名称

```
GetVideoDuration
```

## DLL调用

```
double GetVideoDuration(int64_t instance, int64_t videoHandle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)double duration = GetVideoDuration(instance, videoHandle);
[](#cb3-4)printf("视频时长: %.2f 秒\n", duration);
[](#cb3-5)CloseVideo(instance, videoHandle);
[](#cb3-6)DestroyCOLAPlugInterFace(instance);
```

## 返回值

视频时长（秒），失败返回0.0。

---

# 获取视频高度 -
GetVideoHeight

## 函数简介

获取视频高度。

## 接口名称

```
GetVideoHeight
```

## DLL调用

```
int32_t GetVideoHeight(int64_t instance, int64_t videoHandle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int32_t height = GetVideoHeight(instance, videoHandle);
[](#cb3-4)printf("视频高度: %d 像素\n", height);
[](#cb3-5)CloseVideo(instance, videoHandle);
[](#cb3-6)DestroyCOLAPlugInterFace(instance);
```

## 返回值

视频高度（像素），失败返回0。

---

# 计算两帧之间的相似度
- CalculateFrameSimilarity

## 函数简介

计算两帧之间的相似度。

## 接口名称

```
CalculateFrameSimilarity
```

## DLL调用

```
double CalculateFrameSimilarity(int64_t instance, int64_t frame1, int64_t frame2)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
frame1 |
长整数型 |
第一帧图像句柄 |
|

|
frame2 |
长整数型 |
第二帧图像句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int64_t frame1 = ReadNextFrame(instance, videoHandle);
[](#cb3-4)int64_t frame2 = ReadNextFrame(instance, videoHandle);
[](#cb3-5)double similarity = CalculateFrameSimilarity(instance, frame1, frame2);
[](#cb3-6)printf("两帧相似度: %.2f\n", similarity);
[](#cb3-7)CloseVideo(instance, videoHandle);
[](#cb3-8)DestroyCOLAPlugInterFace(instance);
```

## 返回值

相似度（0-1，1表示完全相同）。

---

# 计算视频平均亮度
- CalculateAverageBrightness

## 函数简介

计算视频平均亮度。

## 接口名称

```
CalculateAverageBrightness
```

## DLL调用

```
double CalculateAverageBrightness(int64_t instance, string videoPath)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoPath |
字符串 |
视频文件路径 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)double brightness = CalculateAverageBrightness(instance, "test.mp4");
[](#cb3-3)printf("视频平均亮度: %.2f\n", brightness);
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

平均亮度（0-255），失败返回-1。

---

# 读取下一帧 - ReadNextFrame

## 函数简介

读取下一帧。

## 接口名称

```
ReadNextFrame
```

## DLL调用

```
int64_t ReadNextFrame(int64_t instance, int64_t videoHandle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int64_t imageHandle = ReadNextFrame(instance, videoHandle);
[](#cb3-4)if (imageHandle != 0) {
[](#cb3-5)    printf("读取下一帧成功，图像句柄: %lld\n", (long long)imageHandle);
[](#cb3-6)    // 返回的图像句柄由内部管理，不需要手动释放
[](#cb3-7)} else {
[](#cb3-8)    printf("读取下一帧失败（可能已到末尾）\n");
[](#cb3-9)}
[](#cb3-10)CloseVideo(instance, videoHandle);
[](#cb3-11)DestroyCOLAPlugInterFace(instance);
```

## 返回值

图像句柄（BGRA格式），失败返回0。

## 注意事项

- 返回的图像句柄由内部管理，不需要手动释放

- 如果已到视频末尾，返回0

---

# 读取当前帧 -
ReadCurrentFrame

## 函数简介

读取当前帧（不移动位置）。

## 接口名称

```
ReadCurrentFrame
```

## DLL调用

```
int64_t ReadCurrentFrame(int64_t instance, int64_t videoHandle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int64_t imageHandle = ReadCurrentFrame(instance, videoHandle);
[](#cb3-4)if (imageHandle != 0) {
[](#cb3-5)    printf("读取当前帧成功，图像句柄: %lld\n", (long long)imageHandle);
[](#cb3-6)    // 返回的图像句柄由内部管理，不需要手动释放
[](#cb3-7)} else {
[](#cb3-8)    printf("读取当前帧失败\n");
[](#cb3-9)}
[](#cb3-10)CloseVideo(instance, videoHandle);
[](#cb3-11)DestroyCOLAPlugInterFace(instance);
```

## 返回值

图像句柄（BGRA格式），失败返回0。

## 注意事项

- 返回的图像句柄由内部管理，不需要手动释放

- 此函数不会改变视频的当前位置

---

# 读取指定时间戳的帧 -
ReadFrameAtTime

## 函数简介

读取指定时间戳的帧。

## 接口名称

```
ReadFrameAtTime
```

## DLL调用

```
int64_t ReadFrameAtTime(int64_t instance, int64_t videoHandle, double timestamp)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

|
timestamp |
双精度 |
时间戳（秒） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int64_t imageHandle = ReadFrameAtTime(instance, videoHandle, 5.5);
[](#cb3-4)if (imageHandle != 0) {
[](#cb3-5)    printf("读取5.5秒处的帧成功，图像句柄: %lld\n", (long long)imageHandle);
[](#cb3-6)    // 返回的图像句柄由内部管理，不需要手动释放
[](#cb3-7)} else {
[](#cb3-8)    printf("读取帧失败\n");
[](#cb3-9)}
[](#cb3-10)CloseVideo(instance, videoHandle);
[](#cb3-11)DestroyCOLAPlugInterFace(instance);
```

## 返回值

图像句柄（BGRA格式），失败返回0。

## 注意事项

- 返回的图像句柄由内部管理，不需要手动释放

- timestamp必须在视频时长范围内

---

# 读取指定索引的帧 -
ReadFrameAtIndex

## 函数简介

读取指定索引的帧。

## 接口名称

```
ReadFrameAtIndex
```

## DLL调用

```
int64_t ReadFrameAtIndex(int64_t instance, int64_t videoHandle, int32_t frameIndex)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

|
frameIndex |
整数型 |
帧索引（从0开始） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int64_t imageHandle = ReadFrameAtIndex(instance, videoHandle, 100);
[](#cb3-4)if (imageHandle != 0) {
[](#cb3-5)    printf("读取第100帧成功，图像句柄: %lld\n", (long long)imageHandle);
[](#cb3-6)    // 返回的图像句柄由内部管理，不需要手动释放
[](#cb3-7)} else {
[](#cb3-8)    printf("读取帧失败\n");
[](#cb3-9)}
[](#cb3-10)CloseVideo(instance, videoHandle);
[](#cb3-11)DestroyCOLAPlugInterFace(instance);
```

## 返回值

图像句柄（BGRA格式），失败返回0。

## 注意事项

- 返回的图像句柄由内部管理，不需要手动释放

- frameIndex从0开始，必须小于总帧数

---

# 调整视频尺寸 - ResizeVideo

## 函数简介

调整视频尺寸。

## 接口名称

```
ResizeVideo
```

## DLL调用

```
int32_t ResizeVideo(int64_t instance, string inputPath, string outputPath, int32_t width, int32_t height)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
inputPath |
字符串 |
输入视频路径 |
|

|
outputPath |
字符串 |
输出视频路径 |
|

|
width |
整数型 |
目标宽度 |
|

|
height |
整数型 |
目标高度 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t result = ResizeVideo(instance, "input.mp4", "output.mp4", 1280, 720);
[](#cb3-3)if (result == 1) {
[](#cb3-4)    printf("视频尺寸调整成功\n");
[](#cb3-5)} else {
[](#cb3-6)    printf("视频尺寸调整失败\n");
[](#cb3-7)}
[](#cb3-8)DestroyCOLAPlugInterFace(instance);
```

## 返回值

- 0: 失败

- 1: 成功

---

# 跳转到指定帧 - SeekToFrame

## 函数简介

跳转到指定帧。

## 接口名称

```
SeekToFrame
```

## DLL调用

```
int32_t SeekToFrame(int64_t instance, int64_t videoHandle, int32_t frameIndex)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

|
frameIndex |
整数型 |
目标帧索引 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int32_t result = SeekToFrame(instance, videoHandle, 100);
[](#cb3-4)if (result == 1) {
[](#cb3-5)    printf("跳转到第100帧成功\n");
[](#cb3-6)} else {
[](#cb3-7)    printf("跳转失败\n");
[](#cb3-8)}
[](#cb3-9)CloseVideo(instance, videoHandle);
[](#cb3-10)DestroyCOLAPlugInterFace(instance);
```

## 返回值

- 0: 失败

- 1: 成功

---

# 跳转到指定时间 - SeekToTime

## 函数简介

跳转到指定时间。

## 接口名称

```
SeekToTime
```

## DLL调用

```
int32_t SeekToTime(int64_t instance, int64_t videoHandle, double timestamp)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

|
timestamp |
双精度 |
目标时间戳（秒） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int32_t result = SeekToTime(instance, videoHandle, 5.5);
[](#cb3-4)if (result == 1) {
[](#cb3-5)    printf("跳转到5.5秒成功\n");
[](#cb3-6)} else {
[](#cb3-7)    printf("跳转失败\n");
[](#cb3-8)}
[](#cb3-9)CloseVideo(instance, videoHandle);
[](#cb3-10)DestroyCOLAPlugInterFace(instance);
```

## 返回值

- 0: 失败

- 1: 成功

---

# 跳转到视频开头 -
SeekToBeginning

## 函数简介

跳转到视频开头。

## 接口名称

```
SeekToBeginning
```

## DLL调用

```
int32_t SeekToBeginning(int64_t instance, int64_t videoHandle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int32_t result = SeekToBeginning(instance, videoHandle);
[](#cb3-4)if (result == 1) {
[](#cb3-5)    printf("跳转到视频开头成功\n");
[](#cb3-6)} else {
[](#cb3-7)    printf("跳转失败\n");
[](#cb3-8)}
[](#cb3-9)CloseVideo(instance, videoHandle);
[](#cb3-10)DestroyCOLAPlugInterFace(instance);
```

## 返回值

- 0: 失败

- 1: 成功

---

# 跳转到视频结尾 - SeekToEnd

## 函数简介

跳转到视频结尾。

## 接口名称

```
SeekToEnd
```

## DLL调用

```
int32_t SeekToEnd(int64_t instance, int64_t videoHandle)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
videoHandle |
长整数型 |
视频句柄 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int64_t videoHandle = OpenVideo(instance, "test.mp4");
[](#cb3-3)int32_t result = SeekToEnd(instance, videoHandle);
[](#cb3-4)if (result == 1) {
[](#cb3-5)    printf("跳转到视频结尾成功\n");
[](#cb3-6)} else {
[](#cb3-7)    printf("跳转失败\n");
[](#cb3-8)}
[](#cb3-9)CloseVideo(instance, videoHandle);
[](#cb3-10)DestroyCOLAPlugInterFace(instance);
```

## 返回值

- 0: 失败

- 1: 成功

---

# 转换视频格式 - ConvertVideo

## 函数简介

转换视频格式。

## 接口名称

```
ConvertVideo
```

## DLL调用

```
int32_t ConvertVideo(int64_t instance, string inputPath, string outputPath, string codec, double fps)
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
inputPath |
字符串 |
输入视频路径 |
|

|
outputPath |
字符串 |
输出视频路径 |
|

|
codec |
字符串 |
编解码器（“H264”, “XVID”, “MJPG”等） |
|

|
fps |
双精度 |
输出帧率（-1表示使用原始帧率） |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t result = ConvertVideo(instance, "input.avi", "output.mp4", "H264", 30.0);
[](#cb3-3)if (result == 1) {
[](#cb3-4)    printf("视频转换成功\n");
[](#cb3-5)} else {
[](#cb3-6)    printf("视频转换失败\n");
[](#cb3-7)}
[](#cb3-8)DestroyCOLAPlugInterFace(instance);
```

## 返回值

- 0: 失败

- 1: 成功

---

## 设置

# 修改用户自定义设置 -
SetConfig

### 函数简介

修改用户自定义设置

可用配置:

DefaultEncoding 整数型 配置接口调用参数默认中文编码
(*全局唯一,所有欧拉对象共享) - 0.GBK (默认) - 1.UTF8

- 2.Unicode

DefaultReturnEncoding 整数型 配置接口调用返回值默认中文编码
(*全局唯一,所有欧拉对象共享) - 0.GBK - 1.UTF8 (默认)

- 2.Unicode

SimModeType 整数型 可配置前台鼠标的仿真类型
(*全局唯一,所有欧拉对象共享) - 0.标准模式 - 1.Logitech驱动 -
2.LogitechGHub驱动 - 3.Razer驱动 - 4.欧拉驱动

EnableRealMouse bool型 是否启用鼠标轨迹模拟

RealMouseMode 整数型 默认值1 鼠标模式 -
1.具有平均速度和移动错误的标准计算机用户。 -
2.具有快速反应和快速鼠标移动的游戏玩家。 - 3.非光学鼠标模式,移动慢. -
4.平衡版本鼠标模式 - 5.机器人模式(直线移动) - 6.自定义模式

RealMouseBaseTimePer100Pixels 整数型 默认值200
每100像素的基础移动时间（毫秒）

RealMouseFlowFlag 整数型 默认值767 移动时间控制：组合不同的速度曲线 -
1: 变化速度曲线 - 创建自然的速度变化 - 2: 中断移动 -
在移动过程中添加暂停 - 4: 另一种中断移动模式 - 8: 慢启动 -
缓慢开始，逐渐加速 - 16: 另一种慢启动模式 - 32: 锯齿状移动 -
添加不规则的移动 - 64: 停止移动 - 在移动结束时减速 - 128: 调整移动 -
用于微调移动 - 256: 随机移动 - 使用随机数生成器创建随机移动 - 512:
恒定速度 - 保持恒定速度移动 - 注：取值可以为这些值相加，如1+2+4+8

RealMouseNoise 双精度浮点数 默认值:5.0 噪声控制：影响轨迹的随机性 -
值越大 = 噪声越小，轨迹越平滑 - 值越小 = 噪声越大，移动越自然 -
建议范围：3.0-8.0

RealMouseDeviation 整数型 默认值:25 偏差控制：影响路径的曲率 - 值越大
= 路径越直，偏差越小 - 值越小 = 路径越弯曲，移动越自然 -
建议范围：20-40

RealMouseMinSteps 整数型 默认值:150 最小步数：控制移动中的点数 -
值越大 = 点数越多，移动越平滑 - 值越小 = 点数越少，移动越快 -
建议范围：50-500

RealMouseTimeToSteps 双精度浮点数 默认值:1.5 控制步之间的时间间隔 -
值越大 = 步长越长，移动越快 - 值越小 = 步长越短，移动越平滑 -
建议范围：1.0-5.0

RealMouseOvershoots 整数型 默认值3 过冲点数：控制移动中的点数 -
在到达终点前要经过附近的坐标点数 - 为0时直接到达坐标

MouseDriftCheckTime 整数型
鼠标飘移检测延时,鼠标到达指定区域后在规定时间内锁定位置
;//鼠标漂移检测时间单位毫秒 0不检测

EnableRealKeypad bool型 是否启用真实键盘输入延时

KeyDownInterval 整数型 键盘单击间隔

MouseClickInterval 整数型 鼠标单击间隔

MouseDoubleClickInterval 整数型 鼠标双击间隔

WorkPath 字符串型 工作路径 (*全局唯一,所有欧拉对象共享)

DbPath 字符串型 图片数据库路径 (*全局唯一,所有欧拉对象共享)

DbPassword 字符串型 图片数据库密码 (*全局唯一,所有欧拉对象共享)

MaxOverlap 双精度浮点数 多图识别最大重叠范围,0完全不重叠 默认值0.5
(*全局唯一,所有欧拉对象共享)

MatchColorWeight 双精度浮点数 彩色模式色彩权重默认0.7 取值范围0~1.0
(*全局唯一,所有欧拉对象共享)

VncServer 字符串型 默认值”127.0.0.1” 链接VNC的IP
绑定模式为VNC时启用

VncPort 整数型 默认值5900 链接VNC的端口 绑定模式为VNC时启用

VncPassword 字符串型 链接VNC的密码 绑定模式为VNC时启用

CheckDisplayDeadInterval 整数型 默认值50ms 检测卡屏的时间间隔

KeyboardHwnd 长整数型
配置绑定键盘的窗口句柄,与显示窗口句柄不一致时使用

MouseHwnd 长整数型
配置绑定鼠标的窗口句柄,与显示窗口句柄不一致时使用

InputLock bool型 后台绑定时是否锁定前台键盘鼠标,默认值false不锁定

ImageStitchMatchValue 双精度浮点数 图片拼接接口识别率0~1 默认0
(*全局唯一,所有欧拉对象共享)

SymbolServer 字符串型 PDB服务器地址 如https://msdl.microsoft.com
(*全局唯一,所有欧拉对象共享)

ForwarderPath 字符串型 x64 转发进程路径，默认当前exe运行目录
(*全局唯一,所有欧拉对象共享)

DriverPath 字符串型 自定义驱动路径 (*全局唯一,所有欧拉对象共享)

EnableOcrOverlapCounting bool型 找字时是否允许重叠统计,默认false
(*全局唯一,所有欧拉对象共享)

FindWindowMode 整数型 查找窗口模式 0.只查询可见窗口 1.查询所有窗口
2.查询不可见窗口 默认值0 (*全局唯一,所有欧拉对象共享)

### 接口名称

```
SetConfig
```

### DLL调用

```
int SetConfig(long ola, string configStr)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `configStr` (字符串):
配置项字符串，格式为{"RealMouseMode":2,"EnablerealMouse":"True"}

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 修改用户自定义设置 -
SetConfigByKey

### 函数简介

修改用户自定义设置

可用配置:

DefaultEncoding 整数型 配置接口调用参数默认中文编码
(*全局唯一,所有欧拉对象共享) - 0.GBK (默认) - 1.UTF8

- 2.Unicode

DefaultReturnEncoding 整数型 配置接口调用返回值默认中文编码
(*全局唯一,所有欧拉对象共享) - 0.GBK - 1.UTF8 (默认)

- 2.Unicode

SimModeType 整数型 可配置前台鼠标的仿真类型
(*全局唯一,所有欧拉对象共享) - 0.标准模式 - 1.Logitech驱动 -
2.LogitechGHub驱动 - 3.Razer驱动 - 4.欧拉驱动

EnableRealMouse bool型 是否启用鼠标轨迹模拟

RealMouseMode 整数型 默认值1 鼠标模式 -
1.具有平均速度和移动错误的标准计算机用户。 -
2.具有快速反应和快速鼠标移动的游戏玩家。 - 3.非光学鼠标模式,移动慢. -
4.平衡版本鼠标模式 - 5.机器人模式(直线移动) - 6.自定义模式

RealMouseBaseTimePer100Pixels 整数型 默认值200
每100像素的基础移动时间（毫秒）

RealMouseFlowFlag 整数型 默认值767 移动时间控制：组合不同的速度曲线 -
1: 变化速度曲线 - 创建自然的速度变化 - 2: 中断移动 -
在移动过程中添加暂停 - 4: 另一种中断移动模式 - 8: 慢启动 -
缓慢开始，逐渐加速 - 16: 另一种慢启动模式 - 32: 锯齿状移动 -
添加不规则的移动 - 64: 停止移动 - 在移动结束时减速 - 128: 调整移动 -
用于微调移动 - 256: 随机移动 - 使用随机数生成器创建随机移动 - 512:
恒定速度 - 保持恒定速度移动 - 注：取值可以为这些值相加，如1+2+4+8

RealMouseNoise 双精度浮点数 默认值:5.0 噪声控制：影响轨迹的随机性 -
值越大 = 噪声越小，轨迹越平滑 - 值越小 = 噪声越大，移动越自然 -
建议范围：3.0-8.0

RealMouseDeviation 整数型 默认值:25 偏差控制：影响路径的曲率 - 值越大
= 路径越直，偏差越小 - 值越小 = 路径越弯曲，移动越自然 -
建议范围：20-40

RealMouseMinSteps 整数型 默认值:150 最小步数：控制移动中的点数 -
值越大 = 点数越多，移动越平滑 - 值越小 = 点数越少，移动越快 -
建议范围：50-500

RealMouseTimeToSteps 双精度浮点数 默认值:1.5 控制步之间的时间间隔 -
值越大 = 步长越长，移动越快 - 值越小 = 步长越短，移动越平滑 -
建议范围：1.0-5.0

RealMouseOvershoots 整数型 默认值3 过冲点数：控制移动中的点数 -
在到达终点前要经过附近的坐标点数 - 为0时直接到达坐标

MouseDriftCheckTime 整数型
鼠标飘移检测延时,鼠标到达指定区域后在规定时间内锁定位置
;//鼠标漂移检测时间单位毫秒 0不检测

EnableRealKeypad bool型 是否启用真实键盘输入延时

KeyDownInterval 整数型 键盘单击间隔

MouseClickInterval 整数型 鼠标单击间隔

MouseDoubleClickInterval 整数型 鼠标双击间隔

WorkPath 字符串型 工作路径 (*全局唯一,所有欧拉对象共享)

DbPath 字符串型 图片数据库路径 (*全局唯一,所有欧拉对象共享)

DbPassword 字符串型 图片数据库密码 (*全局唯一,所有欧拉对象共享)

MaxOverlap 双精度浮点数 多图识别最大重叠范围,0完全不重叠 默认值0.5
(*全局唯一,所有欧拉对象共享)

MatchColorWeight 双精度浮点数 彩色模式色彩权重默认0.7 取值范围0~1.0
(*全局唯一,所有欧拉对象共享)

VncServer 字符串型 默认值”127.0.0.1” 链接VNC的IP
绑定模式为VNC时启用

VncPort 整数型 默认值5900 链接VNC的端口 绑定模式为VNC时启用

VncPassword 字符串型 链接VNC的密码 绑定模式为VNC时启用

CheckDisplayDeadInterval 整数型 默认值50ms 检测卡屏的时间间隔

KeyboardHwnd 长整数型
配置绑定键盘的窗口句柄,与显示窗口句柄不一致时使用

MouseHwnd 长整数型
配置绑定鼠标的窗口句柄,与显示窗口句柄不一致时使用

InputLock bool型 后台绑定时是否锁定前台键盘鼠标,默认值false不锁定

ImageStitchMatchValue 双精度浮点数 图片拼接接口识别率0~1 默认0
(*全局唯一,所有欧拉对象共享)

SymbolServer 字符串型 PDB服务器地址 如https://msdl.microsoft.com
(*全局唯一,所有欧拉对象共享)

ForwarderPath 字符串型 x64 转发进程路径，默认当前exe运行目录
(*全局唯一,所有欧拉对象共享)

DriverPath 字符串型 自定义驱动路径 (*全局唯一,所有欧拉对象共享)

EnableOcrOverlapCounting bool型 找字时是否允许重叠统计,默认false
(*全局唯一,所有欧拉对象共享)

FindWindowMode 整数型 查找窗口模式 0.只查询可见窗口 1.查询所有窗口
2.查询不可见窗口 默认值0 (*全局唯一,所有欧拉对象共享)

### 接口名称

```
SetConfigByKey
```

### DLL调用

```
int SetConfigByKey(long ola, string key,string value)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `key` (字符串): 配置项字符串，如:RealMouseMode

- `value`(字符串): 配置项值字符串，如:true

#### 示例:

ola.SetConfigByKey(“VncServer”,“127.0.0.1”);

ola.SetConfigByKey(“VncPort”,“5900”);

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 版本 - Ver

### 函数简介

返回当前插件版本号

### 接口名称

```
Ver
```

### DLL调用

```
long Ver()
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

字符串:

当前插件的版本描述字符串

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 获取全局路径 - GetPath

### 函数简介

获取全局路径.(可用于调试) 建议使用[GetConfig](/设置/读取用户自定义设置%20-%20GetConfig.html)
接口

### 接口名称

```
GetPath
```

### DLL调用

```
long GetPath(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

字符串:

以字符串的形式返回当前设置的全局路径

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 获取插件路径 - GetBasePath

### 函数简介

获取注册在系统中的OLAPlug.dll的路径.

### 接口名称

```
GetBasePath
```

### DLL调用

```
long GetBasePath(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

字符串:

返回OLAPlug.dll所在路径

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 获取机器码 - GetMachineCode

### 函数简介

获取本机的机器码. 此机器码用于网站后台. 要求调用进程必须有管理员权限.
否则返回空串

### 接口名称

```
GetMachineCode
```

### DLL调用

```
long GetMachineCode(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

字符串:

字符串表达的机器机器码

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

此机器码包含的硬件设备有硬盘,显卡,网卡等. 其它不便透露.
重装系统不会改变此值.

另要注意,插拔任何USB设备,(U盘，U盾,USB移动硬盘,USB键鼠等),以及安装任何网卡驱动程序,(开启或者关闭无线网卡等)都会导致机器码改变.

---

# 设置全局路径 - SetPath

### 函数简介

设置全局路径. 建议使用[SetConfig](/设置/修改用户自定义设置%20-%20SetConfig.html)
接口

### 接口名称

```
SetPath
```

### DLL调用

```
int SetPath(long ola, string Path)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `path` (字符串): 要设置的路径值。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 设置默认编码 -
SetDefaultEncode

### 函数简介

设置全局字符串编码,支持0.GBK 1.UTF8 2.Unicode 编码传参和返回

### 接口名称

```
SetDefaultEncode
```

### DLL调用

```
int SetDefaultEncode(int inputEncoding, int outputEncoding);
```

#### 参数定义:

- `inputEncoding` (整型数):传入参数字符串编码 0.GBK 1.UTF8
2.Unicode 默认0

- `outputEncoding` (整型数):返回参数字符串编码 0.GBK 1.UTF8
2.Unicode 默认1

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 读取用户自定义设置 -
GetConfig

### 函数简介

读取用户自定义设置

可用配置:

DefaultEncoding 整数型 配置接口调用参数默认中文编码
(*全局唯一,所有欧拉对象共享) - 0.GBK (默认) - 1.UTF8

- 2.Unicode

DefaultReturnEncoding 整数型 配置接口调用返回值默认中文编码
(*全局唯一,所有欧拉对象共享) - 0.GBK - 1.UTF8 (默认)

- 2.Unicode

SimModeType 整数型 可配置前台鼠标的仿真类型
(*全局唯一,所有欧拉对象共享) - 0.标准模式 - 1.Logitech驱动 -
2.LogitechGHub驱动 - 3.Razer驱动 - 4.欧拉驱动

EnableRealMouse bool型 是否启用鼠标轨迹模拟

RealMouseMode 整数型 默认值1 鼠标模式 -
1.具有平均速度和移动错误的标准计算机用户。 -
2.具有快速反应和快速鼠标移动的游戏玩家。 - 3.非光学鼠标模式,移动慢. -
4.平衡版本鼠标模式 - 5.机器人模式(直线移动) - 6.自定义模式

RealMouseBaseTimePer100Pixels 整数型 默认值200
每100像素的基础移动时间（毫秒）

RealMouseFlowFlag 整数型 默认值767 移动时间控制：组合不同的速度曲线 -
1: 变化速度曲线 - 创建自然的速度变化 - 2: 中断移动 -
在移动过程中添加暂停 - 4: 另一种中断移动模式 - 8: 慢启动 -
缓慢开始，逐渐加速 - 16: 另一种慢启动模式 - 32: 锯齿状移动 -
添加不规则的移动 - 64: 停止移动 - 在移动结束时减速 - 128: 调整移动 -
用于微调移动 - 256: 随机移动 - 使用随机数生成器创建随机移动 - 512:
恒定速度 - 保持恒定速度移动 - 注：取值可以为这些值相加，如1+2+4+8

RealMouseNoise 双精度浮点数 默认值:5.0 噪声控制：影响轨迹的随机性 -
值越大 = 噪声越小，轨迹越平滑 - 值越小 = 噪声越大，移动越自然 -
建议范围：3.0-8.0

RealMouseDeviation 整数型 默认值:25 偏差控制：影响路径的曲率 - 值越大
= 路径越直，偏差越小 - 值越小 = 路径越弯曲，移动越自然 -
建议范围：20-40

RealMouseMinSteps 整数型 默认值:150 最小步数：控制移动中的点数 -
值越大 = 点数越多，移动越平滑 - 值越小 = 点数越少，移动越快 -
建议范围：50-500

RealMouseTimeToSteps 双精度浮点数 默认值:1.5 控制步之间的时间间隔 -
值越大 = 步长越长，移动越快 - 值越小 = 步长越短，移动越平滑 -
建议范围：1.0-5.0

RealMouseOvershoots 整数型 默认值3 过冲点数：控制移动中的点数 -
在到达终点前要经过附近的坐标点数 - 为0时直接到达坐标

MouseDriftCheckTime 整数型
鼠标飘移检测延时,鼠标到达指定区域后在规定时间内锁定位置
;//鼠标漂移检测时间单位毫秒 0不检测

EnableRealKeypad bool型 是否启用真实键盘输入延时

KeyDownInterval 整数型 键盘单击间隔

MouseClickInterval 整数型 鼠标单击间隔

MouseDoubleClickInterval 整数型 鼠标双击间隔

WorkPath 字符串型 工作路径 (*全局唯一,所有欧拉对象共享)

DbPath 字符串型 图片数据库路径 (*全局唯一,所有欧拉对象共享)

DbPassword 字符串型 图片数据库密码 (*全局唯一,所有欧拉对象共享)

MaxOverlap 双精度浮点数 多图识别最大重叠范围,0完全不重叠 默认值0.5
(*全局唯一,所有欧拉对象共享)

MatchColorWeight 双精度浮点数 彩色模式色彩权重默认0.7 取值范围0~1.0
(*全局唯一,所有欧拉对象共享)

VncServer 字符串型 默认值”127.0.0.1” 链接VNC的IP
绑定模式为VNC时启用

VncPort 整数型 默认值5900 链接VNC的端口 绑定模式为VNC时启用

VncPassword 字符串型 链接VNC的密码 绑定模式为VNC时启用

CheckDisplayDeadInterval 整数型 默认值50ms 检测卡屏的时间间隔

KeyboardHwnd 长整数型
配置绑定键盘的窗口句柄,与显示窗口句柄不一致时使用

MouseHwnd 长整数型
配置绑定鼠标的窗口句柄,与显示窗口句柄不一致时使用

InputLock bool型 后台绑定时是否锁定前台键盘鼠标,默认值false不锁定

ImageStitchMatchValue 双精度浮点数 图片拼接接口识别率0~1 默认0
(*全局唯一,所有欧拉对象共享)

SymbolServer 字符串型 PDB服务器地址 如https://msdl.microsoft.com
(*全局唯一,所有欧拉对象共享)

ForwarderPath 字符串型 x64 转发进程路径，默认当前exe运行目录
(*全局唯一,所有欧拉对象共享)

DriverPath 字符串型 自定义驱动路径 (*全局唯一,所有欧拉对象共享)

EnableOcrOverlapCounting bool型 找字时是否允许重叠统计,默认false
(*全局唯一,所有欧拉对象共享)

FindWindowMode 整数型 查找窗口模式 0.只查询可见窗口 1.查询所有窗口
2.查询不可见窗口 默认值0 (*全局唯一,所有欧拉对象共享)

### 接口名称

```
GetConfig
```

### DLL调用

```
long GetConfig(long ola, string configKey)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `configKey` (字符串): 配置项名称

#### 示例:

待补充…

### 返回值

字符串:

返回匹配结果，如

```
{
"EnableRealKeypad":false,
"EnableRealMouse":true,
"KeyDownInterval":50,
"MouseClickInterval":40,
"MouseDoubleClickInterval":200,
"MouseDriftCheckTime":0,
"RealMouseMode":1,
"WorkPath":""
}
```

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

## 键盘

# 按键 - KeyPress

### 函数简介

按下指定的虚拟键码

### 接口名称

```
KeyPress
```

### DLL调用

```
int KeyPress(long ola, int vk_code)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key` (整型数): 按键码。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 按键char - KeyPressChar

### 函数简介

按住指定的虚拟键码key_str

### 接口名称

```
KeyPressChar
```

### DLL调用

```
int KeyPressChar(long ola, string key_str)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key_str` (字符串): 按键字符。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 按键str - KeyPressStr

### 函数简介

根据指定的字符串序列，依次按顺序按下其中的字符.

### 接口名称

```
KeyPressStr
```

### DLL调用

```
int KeyPressStr(long ola, string key_str,int delay)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key_str` (字符串): 需要按下的字符串序列.
比如”1234”,“abcd”,“7389,1462”等.

- `delay` (整型数):
每按下一个按键，需要延时多久。单位毫秒（ms），这个值越大，按的速度越慢。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

**注意**：在某些情况下，SendString和SendString2都无法输入文字时，可以考虑用这个来输入。但这个接口只支持”a-z
0-9 ~-=[];’,./“和空格,其它字符一律不支持.(包括中国)

---

# 等待按键 - WaitKey

### 函数简介:

等待指定的按键按下 (前台,不是后台)

### 接口名称

```
WaitKey
```

### DLL调用

```
int WaitKey(long ola, int vk_code,int time_out)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `vk_code` (整型数): 等待的按键码。

- `time_out` (整型数): 等待超时时间，单位毫秒。

#### 示例:

待补充…

### 返回值

整型数:

0 : 超时

1 : 指定的按键按下

---

# 键盘弹起 - KeyUp

### 函数简介

弹起来虚拟键vk_code

### 接口名称

```
KeyUp
```

### DLL调用

```
int KeyUp(long ola, int vk_code)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `vk_code` (整型数): 按键码。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 键盘弹起char - KeyUpChar

### 函数简介

弹起来虚拟键key_str

#### 接口名称

```
KeyUpChar
```

### DLL调用

```
int KeyUpChar(long ola, string key_str)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key_str` (字符串): 按键字符。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 键盘按住 - KeyDown

### 函数简介:

按住指定的虚拟键码

### 接口名称

```
KeyDown
```

### DLL调用

```
int KeyDown(long ola, int vk_code)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `vk_code` (整型数): 按键码。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 键盘按住char - KeyDownChar

### 函数简介

按住指定的虚拟键码key_str

### 接口名称

```
KeyDownChar
```

### DLL调用

```
int KeyDownChar(long ola, string key_str)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `key_str` (字符串): 按键字符。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

## 驱动内核

# 伪装进程 - FakeProcess

## 函数简介

将目标进程伪装为另一个进程（以目标进程ID为标识）。

## 接口名称

```
FakeProcess
```

## DLL调用

```
int32_t FakeProcess(int64_t instance, int64_t pid, int64_t fake_pid);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
pid |
长整数型 |
需要伪装的目标进程ID。 |
|

|
fake_pid |
长整数型 |
被伪装成的进程ID。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t ok = FakeProcess(instance, 5678, 9999);
[](#cb3-3)printf("FakeProcess: %d\n", ok);
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1 成功，其他失败。

## 注意事项

- 需要驱动支持与管理员权限。

- 请确保遵循当地法律法规与软件使用协议。

---

# 保护窗口 - ProtectWindow

## 函数简介

设置指定窗口保护状态,防止被截图

## 接口名称

```
ProtectWindow
```

## DLL调用

```
int32_t ProtectWindow(int64_t instance, int64_t hwnd, int32_t flag);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
hwnd |
长整数型 |
窗口句柄 |
|

|
flag |
整数型 |
是否保护（0:取消保护 1:截图黑屏 2:截图透明）。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t ok = ProtectWindow(instance, 1234, 1);
[](#cb3-3)printf("ProtectWindow: %d\n", ok);
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1 成功，其他失败。

## 注意事项

- 需要驱动支持与管理员权限。

---

# 保护进程 - ProtectProcess

## 函数简介

设置指定进程是否受到保护。

## 接口名称

```
ProtectProcess
```

## DLL调用

```
int32_t ProtectProcess(int64_t instance, int64_t pid, int32_t enable);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
pid |
长整数型 |
进程ID。 |
|

|
enable |
整数型 |
是否保护（1 保护，0 取消保护）。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t ok = ProtectProcess(instance, 1234, 1);
[](#cb3-3)printf("ProtectProcess: %d\n", ok);
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1 成功，其他失败。

## 注意事项

- 需要驱动支持与管理员权限。

---

# 加载PDB - LoadPdb

## 函数简介

尝试加载 PDB 符号文件，用于驱动初始化失败时的辅助诊断或初始化。

## 接口名称

```
LoadPdb
```

## DLL调用

```
int32_t LoadPdb(int64_t instance);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t ok = LoadPdb(instance);
[](#cb3-3)printf("LoadPdb: %d\n", ok);
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1 成功，其他失败。

## 注意事项

- 一般在驱动加载失败时调用。

---

# 加载驱动 - LoadDriver

## 函数简介

加载指定驱动；当驱动名称为空时，初始化欧拉驱动。

## 接口名称

```
LoadDriver
```

## DLL调用

```
int32_t LoadDriver(int64_t instance, char* driver_name, char* driver_path);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
driver_name |
字符串 |
驱动名称；为空表示初始化欧拉驱动。 |
|

|
driver_path |
字符串 |
驱动文件路径。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t ok = LoadDriver(instance, "", "C:/temp/ola_driver.sys");
[](#cb3-3)printf("LoadDriver: %d\n", ok);
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1 成功，其他失败。

## 注意事项

- 需要管理员权限加载驱动。

- 请确保驱动签名与系统策略允许加载。

---

# 卸载驱动 - UnloadDriver

## 函数简介

卸载指定名称的驱动。

## 接口名称

```
UnloadDriver
```

## DLL调用

```
int32_t UnloadDriver(int64_t instance, char* driver_name);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
driver_name |
字符串 |
驱动名称。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t ok = UnloadDriver(instance, "ola_driver");
[](#cb3-3)printf("UnloadDriver: %d\n", ok);
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1 成功，其他失败。

## 注意事项

- 驱动需已加载。

---

# 导出驱动 - ExportDriver

## 函数简介

将内置或指定驱动导出到目标路径。

## 接口名称

```
ExportDriver
```

## DLL调用

```
int32_t ExportDriver(int64_t instance, char* driver_path, int32_t type);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
driver_path |
字符串 |
导出驱动保存路径。 |
|

|
type |
整数型 |
驱动类型。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t ok = ExportDriver(instance, "C:/temp/ola_driver.sys", 0);
[](#cb3-3)printf("ExportDriver: %d\n", ok);
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1 成功，其他失败。

## 注意事项

- 目标路径需具备写入权限。

---

# 打开线程句柄 - KeOpenThread

## 函数简介

打开指定线程的内核句柄，用于后续读写或控制等操作。

## 接口名称

```
KeOpenThread
```

## DLL调用

```
int32_t KeOpenThread(int64_t instance, int64_t thread_id, int64_t* thread_handle);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
thread_id |
长整数型 |
目标线程ID。 |
|

|
thread_handle |
长整数型指针 |
输出参数，返回打开的线程句柄。 |
|

### 示例

```
[](#cb3-1)#include <stdio.h>
[](#cb3-2)#include <stdint.h>
[](#cb3-3)
[](#cb3-4)int main() {
[](#cb3-5)    int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-6)    int64_t thread_handle = 0;
[](#cb3-7)
[](#cb3-8)    int32_t ok = KeOpenThread(ola, 5678, &thread_handle);
[](#cb3-9)    printf("KeOpenThread ok=%d, handle=%lld\n", ok, (long long)thread_handle);
[](#cb3-10)
[](#cb3-11)    if (ok == 1 && thread_handle != 0) {
[](#cb3-12)        // 使用完成后关闭句柄
[](#cb3-13)        CloseHandle(ola, thread_handle);
[](#cb3-14)    }
[](#cb3-15)
[](#cb3-16)    DestroyCOLAPlugInterFace(ola);
[](#cb3-17)    return 0;
[](#cb3-18)}
```

## 返回值

1 成功，其他失败。

## 注意事项

- 需要驱动支持与管理员权限。

- 打开成功后请在不再使用时调用 `CloseHandle`
关闭句柄。

- `thread_id` 必须有效且对应的线程存在。

---

# 打开进程句柄 - KeOpenProcess

## 函数简介

打开指定进程的内核句柄，用于后续读写或控制等操作。

## 接口名称

```
KeOpenProcess
```

## DLL调用

```
int32_t KeOpenProcess(int64_t instance, int64_t pid, int64_t* process_handle);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
pid |
长整数型 |
目标进程ID。 |
|

|
process_handle |
长整数型指针 |
输出参数，返回打开的进程句柄。 |
|

### 示例

```
[](#cb3-1)#include <stdio.h>
[](#cb3-2)#include <stdint.h>
[](#cb3-3)
[](#cb3-4)int main() {
[](#cb3-5)    int64_t ola = CreateCOLAPlugInterFace();
[](#cb3-6)    int64_t process_handle = 0;
[](#cb3-7)
[](#cb3-8)    int32_t ok = KeOpenProcess(ola, 1234, &process_handle);
[](#cb3-9)    printf("KeOpenProcess ok=%d, handle=%lld\n", ok, (long long)process_handle);
[](#cb3-10)
[](#cb3-11)    if (ok == 1 && process_handle != 0) {
[](#cb3-12)        // 使用完成后关闭句柄
[](#cb3-13)        CloseHandle(ola, process_handle);
[](#cb3-14)    }
[](#cb3-15)
[](#cb3-16)    DestroyCOLAPlugInterFace(ola);
[](#cb3-17)    return 0;
[](#cb3-18)}
```

## 返回值

1 成功，其他失败。

## 注意事项

- 需要驱动支持与管理员权限。

- 打开成功后请在不再使用时调用 `CloseHandle`
关闭句柄。

- `pid` 必须有效且对应的进程存在。

---

# 测试驱动 - DriverTest

## 函数简介

测试驱动是否正常加载和工作。

## 接口名称

```
DriverTest
```

## DLL调用

```
int32_t DriverTest(int64_t instance);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t ok = DriverTest(instance);
[](#cb3-3)printf("DriverTest: %d\n", ok);
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1 成功，其他失败。

## 注意事项

- 需在驱动加载后调用以验证状态。

---

# 添加保护进程 - AddProtectPID

## 函数简介

添加需要保护的进程，并配置保护模式与允许访问的进程。

## 接口名称

```
AddProtectPID
```

## DLL调用

```
int32_t AddProtectPID(int64_t instance, int64_t pid, int64_t mode, int64_t allow_pid);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
pid |
长整数型 |
保护的目标进程ID。 |
|

|
mode |
长整数型 |
保护模式。 |
|

|
allow_pid |
长整数型 |
允许访问的进程ID。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t ok = AddProtectPID(instance, 2345, 0, 0);
[](#cb3-3)printf("AddProtectPID: %d\n", ok);
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1 成功，其他失败。

## 注意事项

- 需要驱动支持与管理员权限。

---

# 添加白名单进程 - AddAllowPID

## 函数简介

将指定进程添加到白名单列表。

## 接口名称

```
AddAllowPID
```

## DLL调用

```
int32_t AddAllowPID(int64_t instance, int64_t pid);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
pid |
长整数型 |
白名单的进程ID。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t ok = AddAllowPID(instance, 3456);
[](#cb3-3)printf("AddAllowPID: %d\n", ok);
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1 成功，其他失败。

## 注意事项

- 需要驱动支持与管理员权限。

---

# 移除保护进程 -
RemoveProtectPID

## 函数简介

移除已添加的保护进程。

## 接口名称

```
RemoveProtectPID
```

## DLL调用

```
int32_t RemoveProtectPID(int64_t instance, int64_t pid);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
pid |
长整数型 |
需要移除保护的进程ID。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t ok = RemoveProtectPID(instance, 2345);
[](#cb3-3)printf("RemoveProtectPID: %d\n", ok);
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1 成功，其他失败。

## 注意事项

- 需要驱动支持与管理员权限。

---

# 移除白名单进程 -
RemoveAllowPID

## 函数简介

将指定进程从白名单列表移除。

## 接口名称

```
RemoveAllowPID
```

## DLL调用

```
int32_t RemoveAllowPID(int64_t instance, int64_t pid);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
pid |
长整数型 |
需要移除的进程ID。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t ok = RemoveAllowPID(instance, 3456);
[](#cb3-3)printf("RemoveAllowPID: %d\n", ok);
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1 成功，其他失败。

## 注意事项

- 需要驱动支持与管理员权限。

---

# 设置内存读写模式 -
SetMemoryMode

## 函数简介

设置当前实例的内存读写模式。

模式说明： - 0：远程模式 - 1：本地模式（需要DLL注入） - 2：驱动 API
方式读写内存 - 3：驱动 MDL 方式读写内存

## 接口名称

```
SetMemoryMode
```

## DLL调用

```
int32_t SetMemoryMode(int64_t instance, int32_t mode);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
mode |
整数型 |
内存模式（0/1/2/3）。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)
[](#cb3-3)// 设置为驱动API模式
[](#cb3-4)int32_t ok = SetMemoryMode(instance, 2);
[](#cb3-5)printf("SetMemoryMode: %d\n", ok);
[](#cb3-6)
[](#cb3-7)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1 成功，其他失败。

## 注意事项

- 本地模式需要提前完成 DLL 注入。

- 驱动相关模式需要驱动已正确加载。

---

# 隐藏进程 - HideProcess

## 函数简介

设置指定进程是否隐藏。(内部版功能,普通版无法使用)

## 接口名称

```
HideProcess
```

## DLL调用

```
int32_t HideProcess(int64_t instance, int64_t pid, int32_t enable);
```

### 参数说明

|
参数名 |
类型 |
说明 |
|

|
instance |
长整数型 |
OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。 |
|

|
pid |
长整数型 |
进程ID。 |
|

|
enable |
整数型 |
是否隐藏（1 隐藏，0 取消隐藏）。 |
|

### 示例

```
[](#cb3-1)int64_t instance = CreateCOLAPlugInterFace();
[](#cb3-2)int32_t ok = HideProcess(instance, 1234, 1);
[](#cb3-3)printf("HideProcess: %d\n", ok);
[](#cb3-4)DestroyCOLAPlugInterFace(instance);
```

## 返回值

1 成功，其他失败。

## 注意事项

- 需要驱动支持与管理员权限。

---

## 鼠标

# 中键上滚 - WheelUp

### 函数简介

滚轮向上滚

### 接口名称

```
WheelUp
```

### DLL调用

```
int WheelUp(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 中键下滚 - WheelDown

### 函数简介

滚轮向下滚

### 接口名称

```
WheelDown
```

### DLL调用

```
int WheelDown(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 滚轮双击 - MiddleDoubleClick

### 函数简介

滚轮双击，执行完整的鼠标中键双击操作（按下并释放）。

### 接口名称

```
MiddleDoubleClick
```

### DLL调用

```
int MiddleDoubleClick(long instance)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

### 注意事项

- 此函数执行完整的鼠标中键双击操作（按下并释放）。

- 如果需要单独控制按下和释放，请使用 MiddleDown 和 MiddleUp
函数。

- 点击操作会使用当前鼠标位置。

- 如果需要移动到特定位置后点击，请先使用 MoveTo 函数。

- 在调用此函数前，确保鼠标中键未被其他程序占用。

---

# 中键弹起 - MiddleUp

### 函数简介

弹起鼠标中键

### 接口名称

```
int MiddleUp()
```

### DLL调用

```
int MiddleUp(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 中键按下 - MiddleDown

### 函数简介

按住鼠标中键。此函数模拟用户按下鼠标中键（滚轮按钮）的操作。

### 接口名称

```
MiddleDown
```

### DLL调用

```
int MiddleDown(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

#### 示例:

// 创建OLA对象 long ola = CreateCOLAPlugInterFace();

// 按下鼠标中键 int ret = MiddleDown(ola);

// 检查操作是否成功 if (ret == 1) { // 中键按下成功 } else { //
中键按下失败 }

### 返回值

整型数: - 0: 失败 - 1: 成功

### 注意事项

- 此函数仅模拟按下中键，不会自动释放

- 如果需要释放中键，需要调用 [MiddleUp](/鼠标/中键弹起%20-%20MiddleUp.html) 函数

- 建议在操作完成后及时释放中键，避免影响后续操作

- 如果系统不支持中键操作，函数将返回失败

- 在调用此函数前，确保鼠标中键未被其他程序占用

### 相关函数

- [MiddleUp](/鼠标/中键弹起%20-%20MiddleUp.html):
释放鼠标中键

- [MiddleClick](/鼠标/中键点击%20-%20MiddleClick.html):
点击鼠标中键

---

# 中键点击 - MiddleClick

### 函数简介

滚轮点击

### 接口名称

```
MiddleClick
```

### DLL调用

```
int MiddleClick(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 右键弹起 - RightUp

### 函数简介

弹起鼠标右键

### 接口名称

```
int RightUp()
```

### DLL调用

```
int RightUp(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 右键按下 - RightDown

### 函数简介

按住鼠标右键

### 接口名称

```
RightDown
```

### DLL调用

```
int RightDown(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 右键点击 - RightClick

### 函数简介

执行鼠标右键点击操作。此函数模拟用户按下并释放鼠标右键的完整点击过程。

### 接口名称

```
RightClick
```

### DLL调用

```
int RightClick(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)long ola = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 执行右键点击
[](#cb3-5)int ret = RightClick(ola);
[](#cb3-6)
[](#cb3-7)// 检查操作是否成功
[](#cb3-8)if (ret == 1) {
[](#cb3-9)    // 右键点击成功
[](#cb3-10)} else {
[](#cb3-11)    // 右键点击失败
[](#cb3-12)}
```

### 返回值

整型数: - 0: 失败 - 1: 成功

### 注意事项

- 此函数执行完整的右键点击操作（按下并释放）

- 如果需要单独控制按下和释放，请使用 [RightDown](/鼠标/右键按下%20-%20RightDown.html) 和 [RightUp](/鼠标/右键弹起%20-%20RightUp.html) 函数

- 点击操作会使用当前鼠标位置

- 如果需要移动到特定位置后点击，请先使用 [MoveTo](/鼠标/移动%20-%20MoveTo.html) 函数

- 在调用此函数前，确保鼠标右键未被其他程序占用

### 相关函数

- [RightDown](/鼠标/右键按下%20-%20RightDown.html):
按下鼠标右键

- [RightUp](/鼠标/右键弹起%20-%20RightUp.html):
释放鼠标右键

- [MoveTo](/鼠标/移动%20-%20MoveTo.html):
移动鼠标到指定位置

---

# 左键双击 - LeftDoubleClick

### 函数简介

鼠标左键双击

### 接口名称

```
LeftDoubleClick
```

### DLL调用

```
int LeftDoubleClick(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 左键弹起 - LeftUp

### 函数简介

弹起鼠标左键

### 接口名称

```
LeftUp
```

### DLL调用

```
int LeftUp(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 左键按下 - LeftDown

### 函数简介

按住鼠标左键

### 接口名称

```
LeftDown
```

### DLL调用

```
int LeftDown(long ola)
```

#### 参数定义:

ola 长整型数 : OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 左键点击 - LeftClick

### 函数简介

鼠标左键点击

### 接口名称

```
LeftClick
```

### DLL调用

```
int LeftClick(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 生成鼠标移动轨迹 -
GenerateMouseTrajectory

### 函数简介

生成鼠标移动轨迹数据,用于二次开发 返回数据类型解析:

```
{
int x; // X 轴坐标
int y; // Y 轴坐标
int deltaX; // X 轴移动距离
int deltaY; // X 轴移动距离
int time; // 移动时间
}
```

### 接口名称

```
GenerateMouseTrajectory
```

### DLL调用

```
long GenerateMouseTrajectory(long ola, int startX, int startY, int endX, int endY)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `startX` 起点X坐标

- `startY` 起点Y坐标

- `endX` 终点X坐标

- `endY` 终点Y坐标

### 返回值

字符串:

返回轨迹数据,如

```
[{
"deltaX": 8,
"deltaY": 5,
"time": 7,
"x": 108,
"y": 105
}, {
"deltaX": 7,
"deltaY": 3,
"time": 7,
"x": 115,
"y": 108
}, {
"deltaX": 0,
"deltaY": 0,
"time": 7,
"x": 115,
"y": 108
}, {
"deltaX": 0,
"deltaY": 0,
"time": 7,
"x": 115,
"y": 108
}, {
"deltaX": 0,
"deltaY": 0,
"time": 7,
"x": 115,
"y": 108
}, {
"deltaX": 0,
"deltaY": 0,
"time": 7,
"x": 115,
"y": 108
}, {
"deltaX": 0,
"deltaY": 0,
"time": 7,
"x": 115,
"y": 108
}]
```

**注意：** DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 直接移动 -
MoveToWithoutSimulator

### 函数简介

把鼠标移动到目的点(x,
y),不使用鼠标轨迹,即使开启鼠标轨迹这个接口也不会生效

### 接口名称

```
int MoveToWithoutSimulator(int x, int y)
```

### DLL调用

```
int MoveToWithoutSimulator(long ola, int x, int y)
```

#### 参数定义:

- `ola` (长整数型): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `x` (整数型): X坐标

- `y` (整数型): Y坐标

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 相对移动 - MoveR

### 函数简介

鼠标相对于上次的位置移动rx, ry,
前台模式鼠标相对移动时相对当前鼠标位置

### 接口名称

```
MoveR
```

### DLL调用

```
int MoveR(long ola, int rx, int ry)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `rx` (整型数): 相对于上次的X偏移。

- `ry` (整型数): 相对于上次的Y偏移。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 移动 - MoveTo

### 函数简介

把鼠标移动到目的点(x, y)

### 接口名称

```
int MoveTo(int x, int y)
```

### DLL调用

```
int MoveTo(long ola, int x, int y)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x` (整型数): 目标X坐标。

- `y` (整型数): 目标Y坐标。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

# 范围鼠标移动 - MoveToEx

### 函数简介

将鼠标移动到指定范围内的随机位置。此函数用于模拟更自然的鼠标移动，避免固定坐标可能带来的检测问题。

### 接口名称

```
MoveToEx
```

### DLL调用

```
long MoveToEx(long ola, int x, int y, int w, int h)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由DLL版本 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成

- `x` (整型数): 目标区域左上角的X坐标

- `y` (整型数): 目标区域左上角的Y坐标

- `w` (整型数): 目标区域的宽度（从x计算起）

- `h` (整型数): 目标区域的高度（从y计算起）

#### 示例:

```
[](#cb3-1)// 创建OLA对象
[](#cb3-2)long ola = CreateCOLAPlugInterFace();
[](#cb3-3)
[](#cb3-4)// 移动鼠标到(100,100)到(110,110)这个矩形范围内的随机位置
[](#cb3-5)long ret = MoveToEx(ola, 100, 100, 10, 10);
[](#cb3-6)
[](#cb3-7)// 检查操作是否成功
[](#cb3-8)if (ret != 0) {
[](#cb3-9)    // 获取移动后的坐标
[](#cb3-10)    char* coords = (char*)ret;
[](#cb3-11)    printf("移动后的坐标: %s\n", coords);
[](#cb3-12)
[](#cb3-13)    // 释放返回的字符串内存
[](#cb3-14)    FreeStringPtr(coords);
[](#cb3-15)} else {
[](#cb3-16)    // 移动失败
[](#cb3-17)}
```

### 返回值

- DLL调用: 返回字符串指针，包含移动后的坐标，格式为”x,y”。需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)
释放内存

### 注意事项

- 此函数会在指定范围内随机选择一个点作为目标位置

- 坐标系统原点(0,0)在屏幕左上角

- 确保指定的范围在屏幕可见区域内

- 如果范围参数无效（如负数），函数将返回失败

- 移动操作是即时的，没有动画效果

- 建议在移动后添加适当的延时，使操作更自然

### 相关函数

- [MoveTo](/鼠标/移动%20-%20MoveTo.html):
移动鼠标到指定坐标

- [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html):
释放字符串内存

---

# 获取鼠标位置 - GetCursorPos

### 函数简介:

获取鼠标位置.

### 接口名称

```
GetCursorPos
```

### DLL调用

```
int GetCursorPos(long ola, int* x,int* y)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `x` (整型数指针): 返回的鼠标X坐标。

- `y` (整型数指针): 返回的鼠标Y坐标。

#### 示例:

待补充…

### 返回值

整型数:

0 ：失败

1 ：成功

**注意**:此接口绑定后使用，获取的是相当游戏窗口的鼠标坐标

---

# 获取鼠标图标 -
GetCursorImage

### 函数简介

获取鼠标图标.

### 接口名称

```
GetCursorImage
```

### DLL调用

```
long GetCursorImage(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

长整型数:

OLAImage对象的地址

**注意**：图片使用完后需要调用 [FreeImagePtr](/图像处理/释放指定图片内存%20-%20FreeImagePtr.html)
接口进行释放

---

# 获取鼠标特征码 -
GetCursorShape

### 函数简介

获取鼠标特征码.

### 接口名称

```
GetCursorShape
```

### DLL调用

```
long GetCursorShape(long ola)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

字符串：返回鼠标特征码

**注意**:并非所有的游戏都支持后台鼠标特征码,在获取特征码之前,需先操作鼠标

**注意：**

DLL调用返回字符串指针地址,需要调用 [FreeStringPtr](/其他/释放字符串内存%20-%20FreeStringPtr.html)接口释放内存

---

# 设置系统鼠标精度 -
EnableMouseAccuracy

### 函数简介

设置当前系统鼠标的精确度开关。如图所示

### 接口名称

```
EnableMouseAccuracy
```

### DLL调用

```
int EnableMouseAccuracy(long ola, int enable)
```

#### 参数定义:

- `ola` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

- `enable` 0 关闭指针精确度开关. 1打开指针精确度开关.
一般推荐关闭.

### 返回值

整型数:

设置之前的精确度开关.

---

# 鼠标右键双击 -
RightDoubleClick

### 函数简介

鼠标右键双击，执行完整的鼠标右键双击操作（按下并释放）。

### 接口名称

```
RightDoubleClick
```

### DLL调用

```
int RightDoubleClick(long instance)
```

#### 参数定义:

- `instance` (长整型数): OLAPlug对象的指针，由 [CreateCOLAPlugInterFace](/其他/创建OLA对象.html) 接口生成。

#### 示例:

待补充…

### 返回值

整型数:

0 : 失败

1 : 成功

---

