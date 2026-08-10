# -*- coding: mbcs -*-

from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import BSTR, CoClass, COMMETHOD, dispid, GUID
from ctypes import HRESULT
from comtypes.automation import VARIANT
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from comtypes import hints


_lcid = 0  # change this if required
typelib_path = 'C:\\Users\\LS\\Desktop\\LCA\\OLA\\OLAPlug_x64.dll'



class IOlaPlug(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{40BD9474-1605-4628-A759-728AA1A60FE6}')
    _idlflags_ = ['dual', 'oleautomation']

    if TYPE_CHECKING:  # commembers
        def GetRandomNumber(self, min: hints.Incomplete, max: hints.Incomplete) -> hints.Incomplete: ...
        def GetRandomDouble(self, min: hints.Incomplete, max: hints.Incomplete) -> hints.Incomplete: ...
        def ExcludePos(self, json: hints.Incomplete, type: hints.Incomplete, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete) -> hints.Incomplete: ...
        def FindNearestPos(self, json: hints.Incomplete, type: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete) -> hints.Incomplete: ...
        def SortPosDistance(self, json: hints.Incomplete, type: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete) -> hints.Incomplete: ...
        def GetDenseRect(self, image: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def PathPlanning(self, image: hints.Incomplete, startX: hints.Incomplete, startY: hints.Incomplete, endX: hints.Incomplete, endY: hints.Incomplete, potentialRadius: hints.Incomplete, searchRadius: hints.Incomplete) -> hints.Incomplete: ...
        def CreateGraph(self, json: hints.Incomplete) -> hints.Incomplete: ...
        def GetGraph(self, graphPtr: hints.Incomplete) -> hints.Incomplete: ...
        def AddEdge(self, *args: hints.Any, **kwargs: hints.Any) -> hints.Incomplete: ...
        def GetShortestPath(self, *args: hints.Any, **kwargs: hints.Any) -> hints.Incomplete: ...
        def GetShortestDistance(self, *args: hints.Any, **kwargs: hints.Any) -> hints.Incomplete: ...
        def ClearGraph(self, graphPtr: hints.Incomplete) -> hints.Incomplete: ...
        def DeleteGraph(self, graphPtr: hints.Incomplete) -> hints.Incomplete: ...
        def GetNodeCount(self, graphPtr: hints.Incomplete) -> hints.Incomplete: ...
        def GetEdgeCount(self, graphPtr: hints.Incomplete) -> hints.Incomplete: ...
        def GetShortestPathToAllNodes(self, graphPtr: hints.Incomplete, startNode: hints.Incomplete) -> hints.Incomplete: ...
        def GetMinimumSpanningTree(self, graphPtr: hints.Incomplete) -> hints.Incomplete: ...
        def GetMinimumArborescence(self, graphPtr: hints.Incomplete, root: hints.Incomplete) -> hints.Incomplete: ...
        def GetDirectedPathToAllNodes(self, graphPtr: hints.Incomplete, startNode: hints.Incomplete) -> hints.Incomplete: ...
        def CreateGraphFromCoordinates(self, json: hints.Incomplete, connectAll: hints.Incomplete, maxDistance: hints.Incomplete, useEuclideanDistance: hints.Incomplete) -> hints.Incomplete: ...
        def AddCoordinateNode(self, graphPtr: hints.Incomplete, name: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete, connectToExisting: hints.Incomplete, maxDistance: hints.Incomplete, useEuclideanDistance: hints.Incomplete) -> hints.Incomplete: ...
        def GetNodeCoordinates(self, graphPtr: hints.Incomplete, name: hints.Incomplete) -> hints.Incomplete: ...
        def SetNodeConnection(self, *args: hints.Any, **kwargs: hints.Any) -> hints.Incomplete: ...
        def GetNodeConnectionStatus(self, *args: hints.Any, **kwargs: hints.Any) -> hints.Incomplete: ...
        def Assemble(self, asmStr: hints.Incomplete, baseAddr: hints.Incomplete, arch: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def Disassemble(self, asmCode: hints.Incomplete, baseAddr: hints.Incomplete, arch: hints.Incomplete, mode: hints.Incomplete, showType: hints.Incomplete) -> hints.Incomplete: ...
        def AsmCall(self, hwnd: hints.Incomplete, asmStr: hints.Incomplete, type: hints.Incomplete, baseAddr: hints.Incomplete) -> hints.Incomplete: ...
        def Login(self, userCode: hints.Incomplete, softCode: hints.Incomplete, featureList: hints.Incomplete, softVersion: hints.Incomplete, dealerCode: hints.Incomplete) -> hints.Incomplete: ...
        def Activate(self, userCode: hints.Incomplete, softCode: hints.Incomplete, softVersion: hints.Incomplete, dealerCode: hints.Incomplete, licenseKey: hints.Incomplete) -> hints.Incomplete: ...
        def DmaAddDevice(self, vmId: hints.Incomplete) -> hints.Incomplete: ...
        def DmaAddDeviceEx(self, connectionString: hints.Incomplete) -> hints.Incomplete: ...
        def DmaRemoveDevice(self, deviceId: hints.Incomplete) -> hints.Incomplete: ...
        def DmaGetPidFromName(self, deviceId: hints.Incomplete, processName: hints.Incomplete) -> hints.Incomplete: ...
        def DmaGetPidList(self, deviceId: hints.Incomplete) -> hints.Incomplete: ...
        def DmaGetProcessInfo(self, deviceId: hints.Incomplete, pid: hints.Incomplete) -> hints.Incomplete: ...
        def DmaGetModuleBase(self, deviceId: hints.Incomplete, pid: hints.Incomplete, moduleName: hints.Incomplete) -> hints.Incomplete: ...
        def DmaGetModuleSize(self, deviceId: hints.Incomplete, pid: hints.Incomplete, moduleName: hints.Incomplete) -> hints.Incomplete: ...
        def DmaGetProcAddress(self, deviceId: hints.Incomplete, pid: hints.Incomplete, moduleName: hints.Incomplete, functionName: hints.Incomplete) -> hints.Incomplete: ...
        def DmaScatterCreate(self, deviceId: hints.Incomplete, pid: hints.Incomplete) -> hints.Incomplete: ...
        def DmaScatterPrepare(self, scatterHandle: hints.Incomplete, address: hints.Incomplete, size: hints.Incomplete) -> hints.Incomplete: ...
        def DmaScatterExecute(self, scatterHandle: hints.Incomplete) -> hints.Incomplete: ...
        def DmaScatterRead(self, scatterHandle: hints.Incomplete, address: hints.Incomplete, buffer: hints.Incomplete, size: hints.Incomplete) -> hints.Incomplete: ...
        def DmaScatterClear(self, scatterHandle: hints.Incomplete) -> hints.Incomplete: ...
        def DmaScatterClose(self, scatterHandle: hints.Incomplete) -> hints.Incomplete: ...
        def DmaFindData(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr_range: hints.Incomplete, data: hints.Incomplete) -> hints.Incomplete: ...
        def DmaFindDataEx(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr_range: hints.Incomplete, data: hints.Incomplete, step: hints.Incomplete, multi_thread: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def DmaFindDouble(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr_range: hints.Incomplete, double_value_min: hints.Incomplete, double_value_max: hints.Incomplete) -> hints.Incomplete: ...
        def DmaFindDoubleEx(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr_range: hints.Incomplete, double_value_min: hints.Incomplete, double_value_max: hints.Incomplete, step: hints.Incomplete, multi_thread: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def DmaFindFloat(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr_range: hints.Incomplete, float_value_min: hints.Incomplete, float_value_max: hints.Incomplete) -> hints.Incomplete: ...
        def DmaFindFloatEx(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr_range: hints.Incomplete, float_value_min: hints.Incomplete, float_value_max: hints.Incomplete, step: hints.Incomplete, multi_thread: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def DmaFindInt(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr_range: hints.Incomplete, int_value_min: hints.Incomplete, int_value_max: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def DmaFindIntEx(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr_range: hints.Incomplete, int_value_min: hints.Incomplete, int_value_max: hints.Incomplete, type: hints.Incomplete, step: hints.Incomplete, multi_thread: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def DmaFindString(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr_range: hints.Incomplete, string_value: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def DmaFindStringEx(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr_range: hints.Incomplete, string_value: hints.Incomplete, type: hints.Incomplete, step: hints.Incomplete, multi_thread: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def DmaReadData(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def DmaReadDataAddr(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def DmaReadDataAddrToBin(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def DmaReadDataToBin(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def DmaReadDouble(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete) -> hints.Incomplete: ...
        def DmaReadDoubleAddr(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete) -> hints.Incomplete: ...
        def DmaReadFloat(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete) -> hints.Incomplete: ...
        def DmaReadFloatAddr(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete) -> hints.Incomplete: ...
        def DmaReadInt(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def DmaReadIntAddr(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def DmaReadString(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def DmaReadStringAddr(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def DmaWriteData(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, data: hints.Incomplete) -> hints.Incomplete: ...
        def DmaWriteDataFromBin(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, data: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def DmaWriteDataAddr(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, data: hints.Incomplete) -> hints.Incomplete: ...
        def DmaWriteDataAddrFromBin(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, data: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def DmaWriteDouble(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, double_value: hints.Incomplete) -> hints.Incomplete: ...
        def DmaWriteDoubleAddr(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, double_value: hints.Incomplete) -> hints.Incomplete: ...
        def DmaWriteFloat(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, float_value: hints.Incomplete) -> hints.Incomplete: ...
        def DmaWriteFloatAddr(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, float_value: hints.Incomplete) -> hints.Incomplete: ...
        def DmaWriteInt(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def DmaWriteIntAddr(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def DmaWriteString(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def DmaWriteStringAddr(self, deviceId: hints.Incomplete, pid: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiCleanup(self) -> hints.Incomplete: ...
        def DrawGuiRectangle(self, x: hints.Incomplete, y: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete, mode: hints.Incomplete, lineThickness: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiCircle(self, x: hints.Incomplete, y: hints.Incomplete, radius: hints.Incomplete, mode: hints.Incomplete, lineThickness: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiLine(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, lineThickness: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiText(self, text: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete, fontPath: hints.Incomplete, fontSize: hints.Incomplete, align: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiImage(self, imagePath: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiImagePtr(self, imagePtr: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiWindow(self, title: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete, style: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiPanel(self, parentHandle: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiButton(self, parentHandle: hints.Incomplete, text: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiDeleteObject(self, handle: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiClearAll(self) -> hints.Incomplete: ...
        def DrawGuiSetGuiActive(self, active: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiIsGuiActive(self) -> hints.Incomplete: ...
        def DrawGuiSetGuiClickThrough(self, enabled: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiIsGuiClickThrough(self) -> hints.Incomplete: ...
        def DrawGuiSetPosition(self, handle: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetSize(self, handle: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetColor(self, handle: hints.Incomplete, r: hints.Incomplete, g: hints.Incomplete, b: hints.Incomplete, a: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetAlpha(self, handle: hints.Incomplete, alpha: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetDrawMode(self, handle: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetLineThickness(self, handle: hints.Incomplete, thickness: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetFont(self, handle: hints.Incomplete, fontPath: hints.Incomplete, fontSize: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetTextAlign(self, handle: hints.Incomplete, align: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetText(self, handle: hints.Incomplete, text: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetVisible(self, handle: hints.Incomplete, visible: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiGetPosition(self, handle: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def DrawGuiGetSize(self, handle: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def DrawGuiSetZOrder(self, handle: hints.Incomplete, zOrder: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetParent(self, handle: hints.Incomplete, parentHandle: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiIsPointInObject(self, handle: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetWindowTitle(self, handle: hints.Incomplete, title: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetWindowStyle(self, handle: hints.Incomplete, style: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetWindowTopMost(self, handle: hints.Incomplete, topMost: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetWindowTransparency(self, handle: hints.Incomplete, alpha: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetButtonCallback(self, handle: hints.Incomplete, callback: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiSetMouseCallback(self, handle: hints.Incomplete, callback: hints.Incomplete) -> hints.Incomplete: ...
        def DrawGuiGetDrawObjectType(self, handle: hints.Incomplete) -> hints.Incomplete: ...
        def LoadDriver(self, driver_name: hints.Incomplete, driver_path: hints.Incomplete) -> hints.Incomplete: ...
        def UnloadDriver(self, driver_name: hints.Incomplete) -> hints.Incomplete: ...
        def DriverTest(self) -> hints.Incomplete: ...
        def LoadPdb(self) -> hints.Incomplete: ...
        def GetPdbDownloadUrls(self) -> hints.Incomplete: ...
        def AddProtectPID(self, pid: hints.Incomplete, mode: hints.Incomplete, allow_pid: hints.Incomplete) -> hints.Incomplete: ...
        def RemoveProtectPID(self, pid: hints.Incomplete) -> hints.Incomplete: ...
        def AddAllowPID(self, pid: hints.Incomplete) -> hints.Incomplete: ...
        def RemoveAllowPID(self, pid: hints.Incomplete) -> hints.Incomplete: ...
        def HideProcess(self, pid: hints.Incomplete, enable: hints.Incomplete) -> hints.Incomplete: ...
        def ProtectProcess(self, pid: hints.Incomplete, enable: hints.Incomplete) -> hints.Incomplete: ...
        def ProtectProcess2(self, pid: hints.Incomplete, enable: hints.Incomplete) -> hints.Incomplete: ...
        def SetMemoryMode(self, mode: hints.Incomplete) -> hints.Incomplete: ...
        def ExportDriver(self, driver_path: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def FakeProcess(self, pid: hints.Incomplete, fake_pid: hints.Incomplete) -> hints.Incomplete: ...
        def ProtectWindow(self, hwnd: hints.Incomplete, flag: hints.Incomplete) -> hints.Incomplete: ...
        def KeOpenThread(self, thread_id: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def KeOpenProcess(self, pid: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def StartSecurityGuard(self) -> hints.Incomplete: ...
        def ProtectFileTestDriver(self) -> hints.Incomplete: ...
        def ProtectFileEnableDriver(self) -> hints.Incomplete: ...
        def ProtectFileDisableDriver(self) -> hints.Incomplete: ...
        def ProtectFileStartFilter(self) -> hints.Incomplete: ...
        def ProtectFileStopFilter(self) -> hints.Incomplete: ...
        def ProtectFileAddProtectedPath(self, path: hints.Incomplete, mode: hints.Incomplete, is_directory: hints.Incomplete) -> hints.Incomplete: ...
        def ProtectFileRemoveProtectedPath(self, path: hints.Incomplete) -> hints.Incomplete: ...
        def ProtectFileClearProtectedPaths(self) -> hints.Incomplete: ...
        def ProtectFileQueryProtectedPath(self, path: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def ProtectFileAddWhitelist(self, pid: hints.Incomplete) -> hints.Incomplete: ...
        def ProtectFileRemoveWhitelist(self, pid: hints.Incomplete) -> hints.Incomplete: ...
        def ProtectFileClearWhitelist(self) -> hints.Incomplete: ...
        def ProtectFileQueryWhitelist(self, pid: hints.Incomplete) -> hints.Incomplete: ...
        def ProtectFileAddBlacklist(self, pid: hints.Incomplete) -> hints.Incomplete: ...
        def ProtectFileRemoveBlacklist(self, pid: hints.Incomplete) -> hints.Incomplete: ...
        def ProtectFileClearBlacklist(self) -> hints.Incomplete: ...
        def ProtectFileQueryBlacklist(self, pid: hints.Incomplete) -> hints.Incomplete: ...
        def VipProtectEnableDriver(self) -> hints.Incomplete: ...
        def VipProtectDisableDriver(self) -> hints.Incomplete: ...
        def VipProtectAddProtect(self, pid: hints.Incomplete, path: hints.Incomplete, mode: hints.Incomplete, permission: hints.Incomplete) -> hints.Incomplete: ...
        def VipProtectRemoveProtect(self, pid: hints.Incomplete, path: hints.Incomplete) -> hints.Incomplete: ...
        def VipProtectClearAll(self) -> hints.Incomplete: ...
        def VipProtectAddWhitelist(self, pid: hints.Incomplete, path: hints.Incomplete) -> hints.Incomplete: ...
        def VipProtectRemoveWhitelist(self, pid: hints.Incomplete, path: hints.Incomplete) -> hints.Incomplete: ...
        def VipProtectClearWhitelist(self) -> hints.Incomplete: ...
        def VipProtectAddBlacklist(self, pid: hints.Incomplete, path: hints.Incomplete) -> hints.Incomplete: ...
        def VipProtectRemoveBlacklist(self, pid: hints.Incomplete, path: hints.Incomplete) -> hints.Incomplete: ...
        def VipProtectClearBlacklist(self) -> hints.Incomplete: ...
        def EnabletVtDriver(self, enable: hints.Incomplete) -> hints.Incomplete: ...
        def VtFakeWriteData(self, hwnd: hints.Incomplete, addr: hints.Incomplete, data: hints.Incomplete) -> hints.Incomplete: ...
        def VtFakeWriteDataFromBin(self, hwnd: hints.Incomplete, addr: hints.Incomplete, data: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def VtFakeWriteDataAddr(self, hwnd: hints.Incomplete, addr: hints.Incomplete, data: hints.Incomplete) -> hints.Incomplete: ...
        def VtFakeWriteDataAddrFromBin(self, hwnd: hints.Incomplete, addr: hints.Incomplete, data: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def VtUnFakeMemoryAddr(self, hwnd: hints.Incomplete, addr: hints.Incomplete) -> hints.Incomplete: ...
        def VtUnFakeMemory(self, hwnd: hints.Incomplete, addr: hints.Incomplete) -> hints.Incomplete: ...
        def GenerateRSAKey(self, publicKeyPath: hints.Incomplete, privateKeyPath: hints.Incomplete, type: hints.Incomplete, keySize: hints.Incomplete) -> hints.Incomplete: ...
        def ConvertRSAPublicKey(self, publicKey: hints.Incomplete, inputType: hints.Incomplete, outputType: hints.Incomplete) -> hints.Incomplete: ...
        def ConvertRSAPrivateKey(self, privateKey: hints.Incomplete, inputType: hints.Incomplete, outputType: hints.Incomplete) -> hints.Incomplete: ...
        def EncryptWithRsa(self, message: hints.Incomplete, publicKey: hints.Incomplete, paddingType: hints.Incomplete) -> hints.Incomplete: ...
        def DecryptWithRsa(self, cipher: hints.Incomplete, privateKey: hints.Incomplete, paddingType: hints.Incomplete) -> hints.Incomplete: ...
        def SignWithRsa(self, message: hints.Incomplete, privateCer: hints.Incomplete, shaType: hints.Incomplete, paddingType: hints.Incomplete) -> hints.Incomplete: ...
        def VerifySignWithRsa(self, message: hints.Incomplete, signature: hints.Incomplete, shaType: hints.Incomplete, paddingType: hints.Incomplete, publicCer: hints.Incomplete) -> hints.Incomplete: ...
        def AESEncrypt(self, source: hints.Incomplete, key: hints.Incomplete) -> hints.Incomplete: ...
        def AESDecrypt(self, source: hints.Incomplete, key: hints.Incomplete) -> hints.Incomplete: ...
        def AESEncryptEx(self, source: hints.Incomplete, key: hints.Incomplete, iv: hints.Incomplete, mode: hints.Incomplete, paddingType: hints.Incomplete) -> hints.Incomplete: ...
        def AESDecryptEx(self, source: hints.Incomplete, key: hints.Incomplete, iv: hints.Incomplete, mode: hints.Incomplete, paddingType: hints.Incomplete) -> hints.Incomplete: ...
        def MD5Encrypt(self, source: hints.Incomplete) -> hints.Incomplete: ...
        def SHAHash(self, source: hints.Incomplete, shaType: hints.Incomplete) -> hints.Incomplete: ...
        def HMAC(self, source: hints.Incomplete, key: hints.Incomplete, shaType: hints.Incomplete) -> hints.Incomplete: ...
        def GenerateRandomBytes(self, length: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def GenerateGuid(self, type: hints.Incomplete) -> hints.Incomplete: ...
        def Base64Encode(self, source: hints.Incomplete) -> hints.Incomplete: ...
        def Base64Decode(self, source: hints.Incomplete) -> hints.Incomplete: ...
        def PBKDF2(self, password: hints.Incomplete, salt: hints.Incomplete, iterations: hints.Incomplete, keyLength: hints.Incomplete, shaType: hints.Incomplete) -> hints.Incomplete: ...
        def MD5File(self, filePath: hints.Incomplete) -> hints.Incomplete: ...
        def SHAFile(self, filePath: hints.Incomplete, shaType: hints.Incomplete) -> hints.Incomplete: ...
        def CreateFolder(self, path: hints.Incomplete) -> hints.Incomplete: ...
        def DeleteFolder(self, path: hints.Incomplete) -> hints.Incomplete: ...
        def GetFolderList(self, path: hints.Incomplete, baseDir: hints.Incomplete) -> hints.Incomplete: ...
        def IsDirectory(self, path: hints.Incomplete) -> hints.Incomplete: ...
        def IsFile(self, path: hints.Incomplete) -> hints.Incomplete: ...
        def CreateFile(self, path: hints.Incomplete) -> hints.Incomplete: ...
        def DeleteFile(self, path: hints.Incomplete) -> hints.Incomplete: ...
        def CopyFile(self, src: hints.Incomplete, dst: hints.Incomplete) -> hints.Incomplete: ...
        def MoveFile(self, src: hints.Incomplete, dst: hints.Incomplete) -> hints.Incomplete: ...
        def RenameFile(self, src: hints.Incomplete, dst: hints.Incomplete) -> hints.Incomplete: ...
        def GetFileSize(self, path: hints.Incomplete) -> hints.Incomplete: ...
        def GetFileList(self, path: hints.Incomplete, baseDir: hints.Incomplete) -> hints.Incomplete: ...
        def GetFileName(self, path: hints.Incomplete, withExtension: hints.Incomplete) -> hints.Incomplete: ...
        def ToAbsolutePath(self, path: hints.Incomplete) -> hints.Incomplete: ...
        def ToRelativePath(self, path: hints.Incomplete) -> hints.Incomplete: ...
        def FileOrDirectoryExists(self, path: hints.Incomplete) -> hints.Incomplete: ...
        def ReadFileString(self, filePath: hints.Incomplete, encoding: hints.Incomplete) -> hints.Incomplete: ...
        def ReadBytesFromFile(self, filePath: hints.Incomplete, offset: hints.Incomplete, size: hints.Incomplete) -> hints.Incomplete: ...
        def WriteStringToFile(self, filePath: hints.Incomplete, data: hints.Incomplete, encoding: hints.Incomplete) -> hints.Incomplete: ...
        def WriteBytesToFile(self, filePath: hints.Incomplete, dataAddr: hints.Incomplete, dataSize: hints.Incomplete) -> hints.Incomplete: ...
        def StartHotkeyHook(self) -> hints.Incomplete: ...
        def StopHotkeyHook(self) -> hints.Incomplete: ...
        def RegisterHotkey(self, keycode: hints.Incomplete, modifiers: hints.Incomplete, callback: hints.Incomplete) -> hints.Incomplete: ...
        def UnregisterHotkey(self, keycode: hints.Incomplete, modifiers: hints.Incomplete) -> hints.Incomplete: ...
        def RegisterMouseButton(self, button: hints.Incomplete, type: hints.Incomplete, callback: hints.Incomplete) -> hints.Incomplete: ...
        def UnregisterMouseButton(self, button: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def RegisterMouseWheel(self, callback: hints.Incomplete) -> hints.Incomplete: ...
        def UnregisterMouseWheel(self) -> hints.Incomplete: ...
        def RegisterMouseMove(self, callback: hints.Incomplete) -> hints.Incomplete: ...
        def UnregisterMouseMove(self) -> hints.Incomplete: ...
        def RegisterMouseDrag(self, callback: hints.Incomplete) -> hints.Incomplete: ...
        def UnregisterMouseDrag(self) -> hints.Incomplete: ...
        def Inject(self, hwnd: hints.Incomplete, dll_path: hints.Incomplete, type: hints.Incomplete, bypassGuard: hints.Incomplete) -> hints.Incomplete: ...
        def InjectFromUrl(self, hwnd: hints.Incomplete, url: hints.Incomplete, type: hints.Incomplete, bypassGuard: hints.Incomplete) -> hints.Incomplete: ...
        def InjectFromBuffer(self, hwnd: hints.Incomplete, bufferAddr: hints.Incomplete, bufferSize: hints.Incomplete, type: hints.Incomplete, bypassGuard: hints.Incomplete) -> hints.Incomplete: ...
        def JsonCreateObject(self) -> hints.Incomplete: ...
        def JsonCreateArray(self) -> hints.Incomplete: ...
        def JsonParse(self, str: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def JsonFree(self, obj: hints.Incomplete) -> hints.Incomplete: ...
        def JsonStringify(self, obj: hints.Incomplete, indent: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def JsonGetSize(self, obj: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def JsonSetValue(self, obj: hints.Incomplete, key: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def JsonArrayAppend(self, arr: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def JsonClear(self, obj: hints.Incomplete) -> hints.Incomplete: ...
        def JsonDeleteKey(self, obj: hints.Incomplete, key: hints.Incomplete) -> hints.Incomplete: ...
        def JsonGetValue(self, obj: hints.Incomplete, key: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def JsonGetArrayItem(self, arr: hints.Incomplete, index: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def JsonGetString(self, obj: hints.Incomplete, key: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def JsonGetNumber(self, obj: hints.Incomplete, key: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def JsonGetBool(self, obj: hints.Incomplete, key: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def JsonSetString(self, obj: hints.Incomplete, key: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def JsonSetNumber(self, obj: hints.Incomplete, key: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def JsonSetBool(self, obj: hints.Incomplete, key: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def ParseMatchImageJson(self, str: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def GetMatchImageAllCount(self, str: hints.Incomplete) -> hints.Incomplete: ...
        def ParseMatchImageAllJson(self, str: hints.Incomplete, parseIndex: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def GetResultCount(self, resultStr: hints.Incomplete) -> hints.Incomplete: ...
        def KeyDown(self, vk_code: hints.Incomplete) -> hints.Incomplete: ...
        def KeyUp(self, vk_code: hints.Incomplete) -> hints.Incomplete: ...
        def KeyPress(self, vk_code: hints.Incomplete) -> hints.Incomplete: ...
        def LeftDown(self) -> hints.Incomplete: ...
        def LeftUp(self) -> hints.Incomplete: ...
        def MoveTo(self, x: hints.Incomplete, y: hints.Incomplete) -> hints.Incomplete: ...
        def MoveToWithoutSimulator(self, x: hints.Incomplete, y: hints.Incomplete) -> hints.Incomplete: ...
        def RightClick(self) -> hints.Incomplete: ...
        def RightDoubleClick(self) -> hints.Incomplete: ...
        def RightDown(self) -> hints.Incomplete: ...
        def RightUp(self) -> hints.Incomplete: ...
        def GetCursorShape(self) -> hints.Incomplete: ...
        def GetCursorImage(self) -> hints.Incomplete: ...
        def KeyPressStr(self, keyStr: hints.Incomplete, delay: hints.Incomplete) -> hints.Incomplete: ...
        def SendString(self, hwnd: hints.Incomplete, str: hints.Incomplete) -> hints.Incomplete: ...
        def SendStringEx(self, hwnd: hints.Incomplete, addr: hints.Incomplete, len: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def KeyPressChar(self, keyStr: hints.Incomplete) -> hints.Incomplete: ...
        def KeyDownChar(self, keyStr: hints.Incomplete) -> hints.Incomplete: ...
        def KeyUpChar(self, keyStr: hints.Incomplete) -> hints.Incomplete: ...
        def MoveR(self, rx: hints.Incomplete, ry: hints.Incomplete) -> hints.Incomplete: ...
        def MiddleClick(self) -> hints.Incomplete: ...
        def MiddleDoubleClick(self) -> hints.Incomplete: ...
        def MoveToEx(self, x: hints.Incomplete, y: hints.Incomplete, w: hints.Incomplete, h: hints.Incomplete) -> hints.Incomplete: ...
        def GetCursorPos(self) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def MiddleUp(self) -> hints.Incomplete: ...
        def MiddleDown(self) -> hints.Incomplete: ...
        def LeftClick(self) -> hints.Incomplete: ...
        def LeftDoubleClick(self) -> hints.Incomplete: ...
        def WheelUp(self) -> hints.Incomplete: ...
        def WheelDown(self) -> hints.Incomplete: ...
        def WaitKey(self, vk_code: hints.Incomplete, time_out: hints.Incomplete) -> hints.Incomplete: ...
        def EnableMouseAccuracy(self, enable: hints.Incomplete) -> hints.Incomplete: ...
        def GenerateMouseTrajectory(self, startX: hints.Incomplete, startY: hints.Incomplete, endX: hints.Incomplete, endY: hints.Incomplete) -> hints.Incomplete: ...
        def GenerateInvoluteMouseTrajectory(self, startX: hints.Incomplete, startY: hints.Incomplete, radius: hints.Incomplete, stepDistance: hints.Incomplete, curvature: hints.Incomplete, noiseAmplitude: hints.Incomplete) -> hints.Incomplete: ...
        def LogShutdown(self, loggerHandle: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetFilePath(self, loggerHandle: hints.Incomplete, logFilePath: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetPattern(self, loggerHandle: hints.Incomplete, logPattern: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetMaxFileSize(self, loggerHandle: hints.Incomplete, maxFileSizeMb: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetMaxFiles(self, loggerHandle: hints.Incomplete, maxFiles: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetLevel(self, loggerHandle: hints.Incomplete, level: hints.Incomplete) -> hints.Incomplete: ...
        def LogGetLevel(self, loggerHandle: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetTarget(self, loggerHandle: hints.Incomplete, targetFlags: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetAsync(self, loggerHandle: hints.Incomplete, enableAsync: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetColorMode(self, loggerHandle: hints.Incomplete, colorMode: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetLevelColor(self, loggerHandle: hints.Incomplete, level: hints.Incomplete, color: hints.Incomplete) -> hints.Incomplete: ...
        def LogResetLevelColors(self, loggerHandle: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetFlushInterval(self, loggerHandle: hints.Incomplete, flushIntervalSeconds: hints.Incomplete) -> hints.Incomplete: ...
        def LogTrace(self, message: hints.Incomplete) -> hints.Incomplete: ...
        def LogDebug(self, message: hints.Incomplete) -> hints.Incomplete: ...
        def LogInfo(self, message: hints.Incomplete) -> hints.Incomplete: ...
        def LogWarn(self, message: hints.Incomplete) -> hints.Incomplete: ...
        def LogError(self, message: hints.Incomplete) -> hints.Incomplete: ...
        def LogCritical(self, message: hints.Incomplete) -> hints.Incomplete: ...
        def LogFlush(self, loggerHandle: hints.Incomplete) -> hints.Incomplete: ...
        def LogCreateInstance(self, instanceName: hints.Incomplete) -> hints.Incomplete: ...
        def LogDestroyInstance(self, loggerHandle: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetBaseDirectory(self, loggerHandle: hints.Incomplete, baseDirectory: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetDirMode(self, loggerHandle: hints.Incomplete, dirMode: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetModuleName(self, loggerHandle: hints.Incomplete, moduleName: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetFileNamePattern(self, loggerHandle: hints.Incomplete, fileNamePattern: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetRotationMode(self, loggerHandle: hints.Incomplete, rotationMode: hints.Incomplete) -> hints.Incomplete: ...
        def LogSetAppendMode(self, loggerHandle: hints.Incomplete, enableAppend: hints.Incomplete) -> hints.Incomplete: ...
        def LogTraceEx(self, loggerHandle: hints.Incomplete, message: hints.Incomplete) -> hints.Incomplete: ...
        def LogDebugEx(self, loggerHandle: hints.Incomplete, message: hints.Incomplete) -> hints.Incomplete: ...
        def LogInfoEx(self, loggerHandle: hints.Incomplete, message: hints.Incomplete) -> hints.Incomplete: ...
        def LogWarnEx(self, loggerHandle: hints.Incomplete, message: hints.Incomplete) -> hints.Incomplete: ...
        def LogErrorEx(self, loggerHandle: hints.Incomplete, message: hints.Incomplete) -> hints.Incomplete: ...
        def LogCriticalEx(self, loggerHandle: hints.Incomplete, message: hints.Incomplete) -> hints.Incomplete: ...
        def LogRotateFile(self, loggerHandle: hints.Incomplete) -> hints.Incomplete: ...
        def LogCleanupOldFiles(self, loggerHandle: hints.Incomplete, keepCount: hints.Incomplete) -> hints.Incomplete: ...
        def LogGetCurrentFilePath(self, loggerHandle: hints.Incomplete) -> hints.Incomplete: ...
        def LogGetCurrentFileSize(self, loggerHandle: hints.Incomplete) -> hints.Incomplete: ...
        def LogGetTotalFilesCount(self, loggerHandle: hints.Incomplete) -> hints.Incomplete: ...
        def CloseConsole(self, type: hints.Incomplete) -> hints.Incomplete: ...
        def OpenConsole(self, type: hints.Incomplete) -> hints.Incomplete: ...
        def DoubleToData(self, double_value: hints.Incomplete) -> hints.Incomplete: ...
        def FloatToData(self, float_value: hints.Incomplete) -> hints.Incomplete: ...
        def StringToData(self, string_value: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def Int64ToInt32(self, v: hints.Incomplete) -> hints.Incomplete: ...
        def Int32ToInt64(self, v: hints.Incomplete) -> hints.Incomplete: ...
        def FindData(self, hwnd: hints.Incomplete, addr_range: hints.Incomplete, data: hints.Incomplete) -> hints.Incomplete: ...
        def FindDataEx(self, hwnd: hints.Incomplete, addr_range: hints.Incomplete, data: hints.Incomplete, step: hints.Incomplete, multi_thread: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def FindDouble(self, hwnd: hints.Incomplete, addr_range: hints.Incomplete, double_value_min: hints.Incomplete, double_value_max: hints.Incomplete) -> hints.Incomplete: ...
        def FindDoubleEx(self, hwnd: hints.Incomplete, addr_range: hints.Incomplete, double_value_min: hints.Incomplete, double_value_max: hints.Incomplete, step: hints.Incomplete, multi_thread: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def FindFloat(self, hwnd: hints.Incomplete, addr_range: hints.Incomplete, float_value_min: hints.Incomplete, float_value_max: hints.Incomplete) -> hints.Incomplete: ...
        def FindFloatEx(self, hwnd: hints.Incomplete, addr_range: hints.Incomplete, float_value_min: hints.Incomplete, float_value_max: hints.Incomplete, step: hints.Incomplete, multi_thread: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def FindInt(self, hwnd: hints.Incomplete, addr_range: hints.Incomplete, int_value_min: hints.Incomplete, int_value_max: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def FindIntEx(self, hwnd: hints.Incomplete, addr_range: hints.Incomplete, int_value_min: hints.Incomplete, int_value_max: hints.Incomplete, type: hints.Incomplete, step: hints.Incomplete, multi_thread: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def FindString(self, hwnd: hints.Incomplete, addr_range: hints.Incomplete, string_value: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def FindStringEx(self, hwnd: hints.Incomplete, addr_range: hints.Incomplete, string_value: hints.Incomplete, type: hints.Incomplete, step: hints.Incomplete, multi_thread: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def ReadData(self, hwnd: hints.Incomplete, addr: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def ReadDataToBin(self, hwnd: hints.Incomplete, addr: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def ReadDataAddr(self, hwnd: hints.Incomplete, addr: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def ReadDataAddrToBin(self, hwnd: hints.Incomplete, addr: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def ReadDouble(self, hwnd: hints.Incomplete, addr: hints.Incomplete) -> hints.Incomplete: ...
        def ReadDoubleAddr(self, hwnd: hints.Incomplete, addr: hints.Incomplete) -> hints.Incomplete: ...
        def ReadFloat(self, hwnd: hints.Incomplete, addr: hints.Incomplete) -> hints.Incomplete: ...
        def ReadFloatAddr(self, hwnd: hints.Incomplete, addr: hints.Incomplete) -> hints.Incomplete: ...
        def ReadInt(self, hwnd: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def ReadIntAddr(self, hwnd: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def ReadString(self, hwnd: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def ReadStringAddr(self, hwnd: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def WriteData(self, hwnd: hints.Incomplete, addr: hints.Incomplete, data: hints.Incomplete) -> hints.Incomplete: ...
        def WriteDataFromBin(self, hwnd: hints.Incomplete, addr: hints.Incomplete, data: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def WriteDataAddr(self, hwnd: hints.Incomplete, addr: hints.Incomplete, data: hints.Incomplete) -> hints.Incomplete: ...
        def WriteDataAddrFromBin(self, hwnd: hints.Incomplete, addr: hints.Incomplete, data: hints.Incomplete, len: hints.Incomplete) -> hints.Incomplete: ...
        def WriteDouble(self, hwnd: hints.Incomplete, addr: hints.Incomplete, double_value: hints.Incomplete) -> hints.Incomplete: ...
        def WriteDoubleAddr(self, hwnd: hints.Incomplete, addr: hints.Incomplete, double_value: hints.Incomplete) -> hints.Incomplete: ...
        def WriteFloat(self, hwnd: hints.Incomplete, addr: hints.Incomplete, float_value: hints.Incomplete) -> hints.Incomplete: ...
        def WriteFloatAddr(self, hwnd: hints.Incomplete, addr: hints.Incomplete, float_value: hints.Incomplete) -> hints.Incomplete: ...
        def WriteInt(self, hwnd: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def WriteIntAddr(self, hwnd: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def WriteString(self, hwnd: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def WriteStringAddr(self, hwnd: hints.Incomplete, addr: hints.Incomplete, type: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def SetMemoryHwndAsProcessId(self, enable: hints.Incomplete) -> hints.Incomplete: ...
        def FreeProcessMemory(self, hwnd: hints.Incomplete) -> hints.Incomplete: ...
        def GetModuleBaseAddr(self, hwnd: hints.Incomplete, module_name: hints.Incomplete) -> hints.Incomplete: ...
        def GetModuleSize(self, hwnd: hints.Incomplete, module_name: hints.Incomplete) -> hints.Incomplete: ...
        def GetRemoteApiAddress(self, hwnd: hints.Incomplete, module_name: hints.Incomplete, fun_name: hints.Incomplete) -> hints.Incomplete: ...
        def VirtualAllocEx(self, hwnd: hints.Incomplete, addr: hints.Incomplete, size: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def VirtualFreeEx(self, hwnd: hints.Incomplete, addr: hints.Incomplete) -> hints.Incomplete: ...
        def VirtualProtectEx(self, hwnd: hints.Incomplete, addr: hints.Incomplete, size: hints.Incomplete, newProtect: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def VirtualQueryEx(self, hwnd: hints.Incomplete, addr: hints.Incomplete, pmbi: hints.Incomplete) -> hints.Incomplete: ...
        def CloseHandle(self, handle: hints.Incomplete) -> hints.Incomplete: ...
        def CreateRemoteThread(self, hwnd: hints.Incomplete, lpStartAddress: hints.Incomplete, lpParameter: hints.Incomplete, dwCreationFlags: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def HookRemoteApi(self, hwnd: hints.Incomplete, targetAddr: hints.Incomplete, size: hints.Incomplete, hook_proc: hints.Incomplete) -> hints.Incomplete: ...
        def UnhookRemoteApi(self, hwnd: hints.Incomplete, targetAddr: hints.Incomplete) -> hints.Incomplete: ...
        def HttpDownloadFile(self, url: hints.Incomplete, save_path: hints.Incomplete, callback: hints.Incomplete, user_data: hints.Incomplete) -> hints.Incomplete: ...
        def HttpDownloadFileEx(self, url: hints.Incomplete, save_path: hints.Incomplete, callback: hints.Incomplete, user_data: hints.Incomplete, max_retries: hints.Incomplete, connect_timeout_sec: hints.Incomplete, read_timeout_sec: hints.Incomplete) -> hints.Incomplete: ...
        def HttpGet(self, url: hints.Incomplete) -> hints.Incomplete: ...
        def HttpPost(self, url: hints.Incomplete, body: hints.Incomplete, content_type: hints.Incomplete) -> hints.Incomplete: ...
        def HttpRequestEx(self, method: hints.Incomplete, url: hints.Incomplete, headers: hints.Incomplete, body: hints.Incomplete, content_type: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def TcpClientCreate(self, callback: hints.Incomplete, user_data: hints.Incomplete, enable_packet_protocol: hints.Incomplete) -> hints.Incomplete: ...
        def TcpClientConnect(self, client_handle: hints.Incomplete, host: hints.Incomplete, port: hints.Incomplete) -> hints.Incomplete: ...
        def TcpClientSend(self, client_handle: hints.Incomplete, data: hints.Incomplete, data_len: hints.Incomplete) -> hints.Incomplete: ...
        def TcpClientDisconnect(self, client_handle: hints.Incomplete) -> hints.Incomplete: ...
        def TcpClientDestroy(self, client_handle: hints.Incomplete) -> hints.Incomplete: ...
        def TcpServerCreate(self, bind_addr: hints.Incomplete, port: hints.Incomplete, callback: hints.Incomplete, user_data: hints.Incomplete, enable_packet_protocol: hints.Incomplete) -> hints.Incomplete: ...
        def TcpServerSend(self, server_handle: hints.Incomplete, conn_id: hints.Incomplete, data: hints.Incomplete, data_len: hints.Incomplete) -> hints.Incomplete: ...
        def TcpServerDisconnect(self, server_handle: hints.Incomplete, conn_id: hints.Incomplete) -> hints.Incomplete: ...
        def TcpServerStop(self, server_handle: hints.Incomplete) -> hints.Incomplete: ...
        def TcpServerDestroy(self, server_handle: hints.Incomplete) -> hints.Incomplete: ...
        def TcpServerGetClientAddress(self, server_handle: hints.Incomplete, conn_id: hints.Incomplete) -> hints.Incomplete: ...
        def TcpServerGetAllConnectionIds(self, server_handle: hints.Incomplete) -> hints.Incomplete: ...
        def Ocr(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete) -> hints.Incomplete: ...
        def OcrFromPtr(self, ptr: hints.Incomplete) -> hints.Incomplete: ...
        def OcrDetails(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete) -> hints.Incomplete: ...
        def OcrFromPtrDetails(self, ptr: hints.Incomplete) -> hints.Incomplete: ...
        def OcrFromBmpData(self, ptr: hints.Incomplete, size: hints.Incomplete) -> hints.Incomplete: ...
        def OcrFromBmpDataDetails(self, ptr: hints.Incomplete, size: hints.Incomplete) -> hints.Incomplete: ...
        def OcrV5(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete) -> hints.Incomplete: ...
        def OcrV5Details(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete) -> hints.Incomplete: ...
        def OcrV5FromPtr(self, ptr: hints.Incomplete) -> hints.Incomplete: ...
        def OcrV5FromPtrDetails(self, ptr: hints.Incomplete) -> hints.Incomplete: ...
        def OcrFromDict(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorJson: hints.Incomplete, dict_name: hints.Incomplete, matchVal: hints.Incomplete) -> hints.Incomplete: ...
        def OcrFromDictDetails(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorJson: hints.Incomplete, dict_name: hints.Incomplete, matchVal: hints.Incomplete) -> hints.Incomplete: ...
        def OcrFromDictPtr(self, ptr: hints.Incomplete, colorJson: hints.Incomplete, dict_name: hints.Incomplete, matchVal: hints.Incomplete) -> hints.Incomplete: ...
        def OcrFromDictPtrDetails(self, ptr: hints.Incomplete, colorJson: hints.Incomplete, dict_name: hints.Incomplete, matchVal: hints.Incomplete) -> hints.Incomplete: ...
        def SetOcrConfigByKey(self, key: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def SetOcrConfig(self, configStr: hints.Incomplete) -> hints.Incomplete: ...
        def GetOcrConfig(self, configKey: hints.Incomplete) -> hints.Incomplete: ...
        def FindStr(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, str: hints.Incomplete, colorJson: hints.Incomplete, dict: hints.Incomplete, matchVal: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def FindStrDetail(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, str: hints.Incomplete, colorJson: hints.Incomplete, dict: hints.Incomplete, matchVal: hints.Incomplete) -> hints.Incomplete: ...
        def FindStrAll(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, str: hints.Incomplete, colorJson: hints.Incomplete, dict: hints.Incomplete, matchVal: hints.Incomplete) -> hints.Incomplete: ...
        def FindStrFromPtr(self, source: hints.Incomplete, str: hints.Incomplete, colorJson: hints.Incomplete, dict: hints.Incomplete, matchVal: hints.Incomplete) -> hints.Incomplete: ...
        def FindStrFromPtrAll(self, source: hints.Incomplete, str: hints.Incomplete, colorJson: hints.Incomplete, dict: hints.Incomplete, matchVal: hints.Incomplete) -> hints.Incomplete: ...
        def FastNumberOcr(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, numbers: hints.Incomplete, colorJson: hints.Incomplete, matchVal: hints.Incomplete) -> hints.Incomplete: ...
        def FastNumberOcrFromPtr(self, source: hints.Incomplete, numbers: hints.Incomplete, colorJson: hints.Incomplete, matchVal: hints.Incomplete) -> hints.Incomplete: ...
        def ImportTxtDict(self, dictName: hints.Incomplete, dictPath: hints.Incomplete) -> hints.Incomplete: ...
        def ExportTxtDict(self, dictName: hints.Incomplete, dictPath: hints.Incomplete) -> hints.Incomplete: ...
        def Capture(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, file: hints.Incomplete) -> hints.Incomplete: ...
        def GetScreenDataBmp(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def GetScreenData(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def GetScreenDataPtr(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete) -> hints.Incomplete: ...
        def CaptureGif(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, file: hints.Incomplete, delay: hints.Incomplete, time: hints.Incomplete) -> hints.Incomplete: ...
        def LockDisplay(self, enable: hints.Incomplete) -> hints.Incomplete: ...
        def SetSnapCacheTime(self, cacheTime: hints.Incomplete) -> hints.Incomplete: ...
        def GetImageData(self, imgPtr: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def MatchImageFromPath(self, source: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, type: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def MatchImageFromPathAll(self, source: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, type: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def MatchImagePtrFromPath(self, source: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, type: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def MatchImagePtrFromPathAll(self, source: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, type: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def GetColor(self, x: hints.Incomplete, y: hints.Incomplete) -> hints.Incomplete: ...
        def GetColorPtr(self, source: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete) -> hints.Incomplete: ...
        def CopyImage(self, sourcePtr: hints.Incomplete) -> hints.Incomplete: ...
        def FreeImageAll(self) -> hints.Incomplete: ...
        def FreeImagePath(self, path: hints.Incomplete) -> hints.Incomplete: ...
        def LoadImage(self, path: hints.Incomplete) -> hints.Incomplete: ...
        def LoadImageFromBmpData(self, data: hints.Incomplete, dataSize: hints.Incomplete) -> hints.Incomplete: ...
        def LoadImageFromRGBData(self, width: hints.Incomplete, height: hints.Incomplete, scan0: hints.Incomplete, stride: hints.Incomplete) -> hints.Incomplete: ...
        def FreeImagePtr(self, screenPtr: hints.Incomplete) -> hints.Incomplete: ...
        def MatchWindowsFromPtr(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, type: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def MatchImageFromPtr(self, source: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, type: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def MatchImageFromPtrAll(self, source: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, type: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def MatchWindowsFromPtrAll(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, type: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def MatchWindowsFromPath(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, type: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def MatchWindowsFromPathAll(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, type: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def MatchWindowsThresholdFromPtr(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorJson: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def MatchWindowsThresholdFromPtrAll(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorJson: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def MatchWindowsThresholdFromPath(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorJson: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def MatchWindowsThresholdFromPathAll(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorJson: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def ShowMatchWindow(self, flag: hints.Incomplete) -> hints.Incomplete: ...
        def CalculateSSIM(self, image1: hints.Incomplete, image2: hints.Incomplete) -> hints.Incomplete: ...
        def CalculateHistograms(self, image1: hints.Incomplete, image2: hints.Incomplete) -> hints.Incomplete: ...
        def CalculateMSE(self, image1: hints.Incomplete, image2: hints.Incomplete) -> hints.Incomplete: ...
        def SaveImageFromPtr(self, ptr: hints.Incomplete, path: hints.Incomplete) -> hints.Incomplete: ...
        def ReSize(self, ptr: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete) -> hints.Incomplete: ...
        def FindColor(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, color1: hints.Incomplete, color2: hints.Incomplete, dir: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def FindColorList(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, color1: hints.Incomplete, color2: hints.Incomplete) -> hints.Incomplete: ...
        def FindColorEx(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorJson: hints.Incomplete, dir: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def FindColorListEx(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorJson: hints.Incomplete) -> hints.Incomplete: ...
        def FindMultiColor(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorJson: hints.Incomplete, pointJson: hints.Incomplete, sim: hints.Incomplete, dir: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def FindMultiColorList(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorJson: hints.Incomplete, pointJson: hints.Incomplete, sim: hints.Incomplete) -> hints.Incomplete: ...
        def FindMultiColorFromPtr(self, ptr: hints.Incomplete, colorJson: hints.Incomplete, pointJson: hints.Incomplete, sim: hints.Incomplete, dir: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def FindMultiColorListFromPtr(self, ptr: hints.Incomplete, colorJson: hints.Incomplete, pointJson: hints.Incomplete, sim: hints.Incomplete) -> hints.Incomplete: ...
        def GetImageSize(self, ptr: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def FindColorBlock(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorList: hints.Incomplete, count: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def FindColorBlockPtr(self, ptr: hints.Incomplete, colorList: hints.Incomplete, count: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def FindColorBlockList(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorList: hints.Incomplete, count: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def FindColorBlockListPtr(self, ptr: hints.Incomplete, colorList: hints.Incomplete, count: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def FindColorBlockEx(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorList: hints.Incomplete, count: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete, dir: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def FindColorBlockPtrEx(self, ptr: hints.Incomplete, colorList: hints.Incomplete, count: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete, dir: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def FindColorBlockListEx(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorList: hints.Incomplete, count: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete, type: hints.Incomplete, dir: hints.Incomplete) -> hints.Incomplete: ...
        def FindColorBlockListPtrEx(self, ptr: hints.Incomplete, colorList: hints.Incomplete, count: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete, type: hints.Incomplete, dir: hints.Incomplete) -> hints.Incomplete: ...
        def GetColorNum(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorList: hints.Incomplete) -> hints.Incomplete: ...
        def GetColorNumPtr(self, ptr: hints.Incomplete, colorList: hints.Incomplete) -> hints.Incomplete: ...
        def Cropped(self, image: hints.Incomplete, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete) -> hints.Incomplete: ...
        def GetThresholdImageFromMultiColorPtr(self, ptr: hints.Incomplete, colorJson: hints.Incomplete) -> hints.Incomplete: ...
        def GetThresholdImageFromMultiColor(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, colorJson: hints.Incomplete) -> hints.Incomplete: ...
        def IsSameImage(self, ptr: hints.Incomplete, ptr2: hints.Incomplete) -> hints.Incomplete: ...
        def ShowImage(self, ptr: hints.Incomplete) -> hints.Incomplete: ...
        def ShowImageFromFile(self, file: hints.Incomplete) -> hints.Incomplete: ...
        def SetColorsToNewColor(self, ptr: hints.Incomplete, colorJson: hints.Incomplete, color: hints.Incomplete) -> hints.Incomplete: ...
        def RemoveOtherColors(self, ptr: hints.Incomplete, colorJson: hints.Incomplete) -> hints.Incomplete: ...
        def DrawRectangle(self, ptr: hints.Incomplete, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, thickness: hints.Incomplete, color: hints.Incomplete) -> hints.Incomplete: ...
        def DrawCircle(self, ptr: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete, radius: hints.Incomplete, thickness: hints.Incomplete, color: hints.Incomplete) -> hints.Incomplete: ...
        def DrawFillPoly(self, ptr: hints.Incomplete, pointJson: hints.Incomplete, color: hints.Incomplete) -> hints.Incomplete: ...
        def DecodeQRCode(self, ptr: hints.Incomplete) -> hints.Incomplete: ...
        def CreateQRCode(self, str: hints.Incomplete, pixelsPerModule: hints.Incomplete) -> hints.Incomplete: ...
        def CreateQRCodeEx(self, str: hints.Incomplete, pixelsPerModule: hints.Incomplete, version: hints.Incomplete, correction_level: hints.Incomplete, mode: hints.Incomplete, structure_number: hints.Incomplete) -> hints.Incomplete: ...
        def MatchAnimationFromPtr(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, type: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete, delay: hints.Incomplete, time: hints.Incomplete, threadCount: hints.Incomplete) -> hints.Incomplete: ...
        def MatchAnimationFromPath(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, templ: hints.Incomplete, matchVal: hints.Incomplete, type: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete, delay: hints.Incomplete, time: hints.Incomplete, threadCount: hints.Incomplete) -> hints.Incomplete: ...
        def RemoveImageDiff(self, image1: hints.Incomplete, image2: hints.Incomplete) -> hints.Incomplete: ...
        def GetImageBmpData(self, imgPtr: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def FreeImageData(self, screenPtr: hints.Incomplete) -> hints.Incomplete: ...
        def ScalePixels(self, ptr: hints.Incomplete, pixelsPerModule: hints.Incomplete) -> hints.Incomplete: ...
        def CreateImage(self, width: hints.Incomplete, height: hints.Incomplete, color: hints.Incomplete) -> hints.Incomplete: ...
        def SetPixel(self, image: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete, color: hints.Incomplete) -> hints.Incomplete: ...
        def SetPixelList(self, image: hints.Incomplete, points: hints.Incomplete, color: hints.Incomplete) -> hints.Incomplete: ...
        def ConcatImage(self, image1: hints.Incomplete, image2: hints.Incomplete, gap: hints.Incomplete, color: hints.Incomplete, dir: hints.Incomplete) -> hints.Incomplete: ...
        def CoverImage(self, image1: hints.Incomplete, image2: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete, alpha: hints.Incomplete) -> hints.Incomplete: ...
        def RotateImage(self, image: hints.Incomplete, angle: hints.Incomplete) -> hints.Incomplete: ...
        def ImageToBase64(self, image: hints.Incomplete) -> hints.Incomplete: ...
        def Base64ToImage(self, base64: hints.Incomplete) -> hints.Incomplete: ...
        def Hex2ARGB(self, hex: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def Hex2RGB(self, hex: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def ARGB2Hex(self, a: hints.Incomplete, r: hints.Incomplete, g: hints.Incomplete, b: hints.Incomplete) -> hints.Incomplete: ...
        def RGB2Hex(self, r: hints.Incomplete, g: hints.Incomplete, b: hints.Incomplete) -> hints.Incomplete: ...
        def CmpColor(self, x1: hints.Incomplete, y1: hints.Incomplete, colorStart: hints.Incomplete, colorEnd: hints.Incomplete) -> hints.Incomplete: ...
        def CmpColorPtr(self, ptr: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete, colorStart: hints.Incomplete, colorEnd: hints.Incomplete) -> hints.Incomplete: ...
        def CmpColorHex(self, hex: hints.Incomplete, colorStart: hints.Incomplete, colorEnd: hints.Incomplete) -> hints.Incomplete: ...
        def CmpMultiColor(self, pointJson: hints.Incomplete, sim: hints.Incomplete) -> hints.Incomplete: ...
        def CmpMultiColorPtr(self, image: hints.Incomplete, pointJson: hints.Incomplete, sim: hints.Incomplete) -> hints.Incomplete: ...
        def GetConnectedComponents(self, ptr: hints.Incomplete, points: hints.Incomplete, tolerance: hints.Incomplete) -> hints.Incomplete: ...
        def DetectPointerDirection(self, ptr: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete) -> hints.Incomplete: ...
        def DetectPointerDirectionByFeatures(self, ptr: hints.Incomplete, templatePtr: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete, useTemplate: hints.Incomplete) -> hints.Incomplete: ...
        def FastMatch(self, ptr: hints.Incomplete, templatePtr: hints.Incomplete, matchVal: hints.Incomplete, type: hints.Incomplete, angle: hints.Incomplete, scale: hints.Incomplete) -> hints.Incomplete: ...
        def GetROIRegion(self, ptr: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def FastROI(self, ptr: hints.Incomplete) -> hints.Incomplete: ...
        def Hex2HSV(self, hex: hints.Incomplete) -> hints.Incomplete: ...
        def RGB2HSV(self, r: hints.Incomplete, g: hints.Incomplete, b: hints.Incomplete) -> hints.Incomplete: ...
        def GetForegroundPoints(self, ptr: hints.Incomplete) -> hints.Incomplete: ...
        def ConvertColor(self, ptr: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def Threshold(self, ptr: hints.Incomplete, thresh: hints.Incomplete, maxVal: hints.Incomplete, type: hints.Incomplete) -> hints.Incomplete: ...
        def RemoveIslands(self, ptr: hints.Incomplete, minArea: hints.Incomplete) -> hints.Incomplete: ...
        def MorphGradient(self, ptr: hints.Incomplete, kernelSize: hints.Incomplete) -> hints.Incomplete: ...
        def ImageStitchFromPath(self, path: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def ImageStitchCreate(self) -> hints.Incomplete: ...
        def ImageStitchFree(self, imageStitch: hints.Incomplete) -> hints.Incomplete: ...
        def ImageStitchAppend(self, imageStitch: hints.Incomplete, image: hints.Incomplete) -> hints.Incomplete: ...
        def ImageStitchGetResult(self, imageStitch: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def MorphTophat(self, ptr: hints.Incomplete, kernelSize: hints.Incomplete) -> hints.Incomplete: ...
        def MorphBlackhat(self, ptr: hints.Incomplete, kernelSize: hints.Incomplete) -> hints.Incomplete: ...
        def Dilation(self, ptr: hints.Incomplete, kernelSize: hints.Incomplete) -> hints.Incomplete: ...
        def Erosion(self, ptr: hints.Incomplete, kernelSize: hints.Incomplete) -> hints.Incomplete: ...
        def GaussianBlur(self, ptr: hints.Incomplete, kernelSize: hints.Incomplete) -> hints.Incomplete: ...
        def Sharpen(self, ptr: hints.Incomplete) -> hints.Incomplete: ...
        def CannyEdge(self, ptr: hints.Incomplete, kernelSize: hints.Incomplete) -> hints.Incomplete: ...
        def Flip(self, ptr: hints.Incomplete, flipCode: hints.Incomplete) -> hints.Incomplete: ...
        def MorphOpen(self, ptr: hints.Incomplete, kernelSize: hints.Incomplete) -> hints.Incomplete: ...
        def MorphClose(self, ptr: hints.Incomplete, kernelSize: hints.Incomplete) -> hints.Incomplete: ...
        def Skeletonize(self, ptr: hints.Incomplete) -> hints.Incomplete: ...
        def GetImagePngData(self, imgPtr: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def CmpColorEx(self, x1: hints.Incomplete, y1: hints.Incomplete, colorJson: hints.Incomplete) -> hints.Incomplete: ...
        def CmpColorPtrEx(self, ptr: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete, colorJson: hints.Incomplete) -> hints.Incomplete: ...
        def CmpColorHexEx(self, hex: hints.Incomplete, colorJson: hints.Incomplete) -> hints.Incomplete: ...
        def BitPacking(self, image: hints.Incomplete) -> hints.Incomplete: ...
        def BitUnpacking(self, imageStr: hints.Incomplete) -> hints.Incomplete: ...
        def SetImageCache(self, enable: hints.Incomplete) -> hints.Incomplete: ...
        def FindImageFromPtr(self, source: hints.Incomplete, templ: hints.Incomplete, deltaColor: hints.Incomplete, matchVal: hints.Incomplete, dir: hints.Incomplete) -> hints.Incomplete: ...
        def FindImageFromPtrAll(self, source: hints.Incomplete, templ: hints.Incomplete, deltaColor: hints.Incomplete, matchVal: hints.Incomplete) -> hints.Incomplete: ...
        def FindImageFromPath(self, source: hints.Incomplete, templ: hints.Incomplete, deltaColor: hints.Incomplete, matchVal: hints.Incomplete, dir: hints.Incomplete) -> hints.Incomplete: ...
        def FindImageFromPathAll(self, source: hints.Incomplete, templ: hints.Incomplete, deltaColor: hints.Incomplete, matchVal: hints.Incomplete) -> hints.Incomplete: ...
        def FindWindowsFromPtr(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, templ: hints.Incomplete, deltaColor: hints.Incomplete, matchVal: hints.Incomplete, dir: hints.Incomplete) -> hints.Incomplete: ...
        def FindWindowsFromPtrAll(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, templ: hints.Incomplete, deltaColor: hints.Incomplete, matchVal: hints.Incomplete) -> hints.Incomplete: ...
        def FindWindowsFromPath(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, templ: hints.Incomplete, deltaColor: hints.Incomplete, matchVal: hints.Incomplete, dir: hints.Incomplete) -> hints.Incomplete: ...
        def FindWindowsFromPathAll(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, templ: hints.Incomplete, deltaColor: hints.Incomplete, matchVal: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryOpenKey(self, rootKey: hints.Incomplete, subKey: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryCreateKey(self, rootKey: hints.Incomplete, subKey: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryCloseKey(self, key: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryKeyExists(self, rootKey: hints.Incomplete, subKey: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryDeleteKey(self, rootKey: hints.Incomplete, subKey: hints.Incomplete, recursive: hints.Incomplete) -> hints.Incomplete: ...
        def RegistrySetString(self, key: hints.Incomplete, valueName: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryGetString(self, key: hints.Incomplete, valueName: hints.Incomplete) -> hints.Incomplete: ...
        def RegistrySetDword(self, key: hints.Incomplete, valueName: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryGetDword(self, key: hints.Incomplete, valueName: hints.Incomplete) -> hints.Incomplete: ...
        def RegistrySetQword(self, key: hints.Incomplete, valueName: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryGetQword(self, key: hints.Incomplete, valueName: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryDeleteValue(self, key: hints.Incomplete, valueName: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryEnumSubKeys(self, key: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryEnumValues(self, key: hints.Incomplete) -> hints.Incomplete: ...
        def RegistrySetEnvironmentVariable(self, name: hints.Incomplete, value: hints.Incomplete, systemWide: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryGetEnvironmentVariable(self, name: hints.Incomplete, systemWide: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryGetUserRegistryPath(self) -> hints.Incomplete: ...
        def RegistryGetSystemRegistryPath(self) -> hints.Incomplete: ...
        def RegistryBackupToFile(self, rootKey: hints.Incomplete, subKey: hints.Incomplete, filePath: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryRestoreFromFile(self, filePath: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryCompareKeys(self, rootKey1: hints.Incomplete, subKey1: hints.Incomplete, rootKey2: hints.Incomplete, subKey2: hints.Incomplete) -> hints.Incomplete: ...
        def RegistrySearchKeys(self, rootKey: hints.Incomplete, searchPath: hints.Incomplete, searchPattern: hints.Incomplete, recursive: hints.Incomplete) -> hints.Incomplete: ...
        def RegistryGetInstalledSoftware(self) -> hints.Incomplete: ...
        def RegistryGetWindowsVersion(self) -> hints.Incomplete: ...
        def OpenDatabase(self, dbName: hints.Incomplete, password: hints.Incomplete) -> hints.Incomplete: ...
        def OpenMemoryDatabase(self, address: hints.Incomplete, size: hints.Incomplete, password: hints.Incomplete) -> hints.Incomplete: ...
        def GetDatabaseError(self, db: hints.Incomplete) -> hints.Incomplete: ...
        def CloseDatabase(self, db: hints.Incomplete) -> hints.Incomplete: ...
        def GetAllTableNames(self, db: hints.Incomplete) -> hints.Incomplete: ...
        def GetTableInfo(self, db: hints.Incomplete, tableName: hints.Incomplete) -> hints.Incomplete: ...
        def GetTableInfoDetail(self, db: hints.Incomplete, tableName: hints.Incomplete) -> hints.Incomplete: ...
        def ExecuteSql(self, db: hints.Incomplete, sql: hints.Incomplete) -> hints.Incomplete: ...
        def ExecuteScalar(self, db: hints.Incomplete, sql: hints.Incomplete) -> hints.Incomplete: ...
        def ExecuteReader(self, db: hints.Incomplete, sql: hints.Incomplete) -> hints.Incomplete: ...
        def Read(self, stmt: hints.Incomplete) -> hints.Incomplete: ...
        def GetDataCount(self, stmt: hints.Incomplete) -> hints.Incomplete: ...
        def GetColumnCount(self, stmt: hints.Incomplete) -> hints.Incomplete: ...
        def GetColumnName(self, stmt: hints.Incomplete, iCol: hints.Incomplete) -> hints.Incomplete: ...
        def GetColumnIndex(self, stmt: hints.Incomplete, columnName: hints.Incomplete) -> hints.Incomplete: ...
        def GetColumnType(self, stmt: hints.Incomplete, iCol: hints.Incomplete) -> hints.Incomplete: ...
        def Finalize(self, stmt: hints.Incomplete) -> hints.Incomplete: ...
        def GetDouble(self, stmt: hints.Incomplete, iCol: hints.Incomplete) -> hints.Incomplete: ...
        def GetInt32(self, stmt: hints.Incomplete, iCol: hints.Incomplete) -> hints.Incomplete: ...
        def GetInt64(self, stmt: hints.Incomplete, iCol: hints.Incomplete) -> hints.Incomplete: ...
        def GetString(self, stmt: hints.Incomplete, iCol: hints.Incomplete) -> hints.Incomplete: ...
        def GetDoubleByColumnName(self, stmt: hints.Incomplete, columnName: hints.Incomplete) -> hints.Incomplete: ...
        def GetInt32ByColumnName(self, stmt: hints.Incomplete, columnName: hints.Incomplete) -> hints.Incomplete: ...
        def GetInt64ByColumnName(self, stmt: hints.Incomplete, columnName: hints.Incomplete) -> hints.Incomplete: ...
        def GetStringByColumnName(self, stmt: hints.Incomplete, columnName: hints.Incomplete) -> hints.Incomplete: ...
        def InitOlaDatabase(self, db: hints.Incomplete) -> hints.Incomplete: ...
        def InitOlaImageFromDir(self, db: hints.Incomplete, dir: hints.Incomplete, cover: hints.Incomplete) -> hints.Incomplete: ...
        def RemoveOlaImageFromDir(self, db: hints.Incomplete, dir: hints.Incomplete) -> hints.Incomplete: ...
        def ExportOlaImageDir(self, db: hints.Incomplete, dir: hints.Incomplete, exportDir: hints.Incomplete) -> hints.Incomplete: ...
        def ImportOlaImage(self, db: hints.Incomplete, dir: hints.Incomplete, fileName: hints.Incomplete, cover: hints.Incomplete) -> hints.Incomplete: ...
        def GetOlaImage(self, db: hints.Incomplete, dir: hints.Incomplete, fileName: hints.Incomplete) -> hints.Incomplete: ...
        def RemoveOlaImage(self, db: hints.Incomplete, dir: hints.Incomplete, fileName: hints.Incomplete) -> hints.Incomplete: ...
        def SetDbConfig(self, db: hints.Incomplete, key: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def GetDbConfig(self, db: hints.Incomplete, key: hints.Incomplete) -> hints.Incomplete: ...
        def RemoveDbConfig(self, db: hints.Incomplete, key: hints.Incomplete) -> hints.Incomplete: ...
        def SetDbConfigEx(self, key: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def GetDbConfigEx(self, key: hints.Incomplete) -> hints.Incomplete: ...
        def RemoveDbConfigEx(self, key: hints.Incomplete) -> hints.Incomplete: ...
        def InitDictFromDir(self, db: hints.Incomplete, dict_name: hints.Incomplete, dict_path: hints.Incomplete, cover: hints.Incomplete) -> hints.Incomplete: ...
        def ImportDictWord(self, db: hints.Incomplete, dict_name: hints.Incomplete, pic_file_name: hints.Incomplete, cover: hints.Incomplete) -> hints.Incomplete: ...
        def ExportDict(self, db: hints.Incomplete, dict_name: hints.Incomplete, export_dir: hints.Incomplete) -> hints.Incomplete: ...
        def RemoveDict(self, db: hints.Incomplete, dict_name: hints.Incomplete) -> hints.Incomplete: ...
        def RemoveDictWord(self, db: hints.Incomplete, dict_name: hints.Incomplete, word: hints.Incomplete) -> hints.Incomplete: ...
        def GetDictImage(self, db: hints.Incomplete, dict_name: hints.Incomplete, word: hints.Incomplete, gap: hints.Incomplete, dir: hints.Incomplete) -> hints.Incomplete: ...
        def CreateDatabase(self, dbName: hints.Incomplete, password: hints.Incomplete) -> hints.Incomplete: ...
        def InitDictFromTxt(self, db: hints.Incomplete, dict_name: hints.Incomplete, dict_path: hints.Incomplete, cover: hints.Incomplete) -> hints.Incomplete: ...
        def OpenVideo(self, videoPath: hints.Incomplete) -> hints.Incomplete: ...
        def OpenCamera(self, deviceIndex: hints.Incomplete) -> hints.Incomplete: ...
        def CloseVideo(self, videoHandle: hints.Incomplete) -> hints.Incomplete: ...
        def IsVideoOpened(self, videoHandle: hints.Incomplete) -> hints.Incomplete: ...
        def GetVideoInfo(self, videoHandle: hints.Incomplete) -> hints.Incomplete: ...
        def GetVideoWidth(self, videoHandle: hints.Incomplete) -> hints.Incomplete: ...
        def GetVideoHeight(self, videoHandle: hints.Incomplete) -> hints.Incomplete: ...
        def GetVideoFPS(self, videoHandle: hints.Incomplete) -> hints.Incomplete: ...
        def GetVideoTotalFrames(self, videoHandle: hints.Incomplete) -> hints.Incomplete: ...
        def GetVideoDuration(self, videoHandle: hints.Incomplete) -> hints.Incomplete: ...
        def GetCurrentFrameIndex(self, videoHandle: hints.Incomplete) -> hints.Incomplete: ...
        def GetCurrentTimestamp(self, videoHandle: hints.Incomplete) -> hints.Incomplete: ...
        def ReadNextFrame(self, videoHandle: hints.Incomplete) -> hints.Incomplete: ...
        def ReadFrameAtIndex(self, videoHandle: hints.Incomplete, frameIndex: hints.Incomplete) -> hints.Incomplete: ...
        def ReadFrameAtTime(self, videoHandle: hints.Incomplete, timestamp: hints.Incomplete) -> hints.Incomplete: ...
        def ReadCurrentFrame(self, videoHandle: hints.Incomplete) -> hints.Incomplete: ...
        def SeekToFrame(self, videoHandle: hints.Incomplete, frameIndex: hints.Incomplete) -> hints.Incomplete: ...
        def SeekToTime(self, videoHandle: hints.Incomplete, timestamp: hints.Incomplete) -> hints.Incomplete: ...
        def SeekToBeginning(self, videoHandle: hints.Incomplete) -> hints.Incomplete: ...
        def SeekToEnd(self, videoHandle: hints.Incomplete) -> hints.Incomplete: ...
        def ExtractFramesToFiles(self, videoHandle: hints.Incomplete, startFrame: hints.Incomplete, endFrame: hints.Incomplete, step: hints.Incomplete, outputDir: hints.Incomplete, imageFormat: hints.Incomplete, jpegQuality: hints.Incomplete) -> hints.Incomplete: ...
        def ExtractFramesByInterval(self, videoHandle: hints.Incomplete, intervalSeconds: hints.Incomplete, outputDir: hints.Incomplete, imageFormat: hints.Incomplete) -> hints.Incomplete: ...
        def ExtractKeyFrames(self, videoHandle: hints.Incomplete, Threshold: hints.Incomplete, maxFrames: hints.Incomplete, outputDir: hints.Incomplete, imageFormat: hints.Incomplete) -> hints.Incomplete: ...
        def SaveCurrentFrame(self, videoHandle: hints.Incomplete, outputPath: hints.Incomplete, quality: hints.Incomplete) -> hints.Incomplete: ...
        def SaveFrameAtIndex(self, videoHandle: hints.Incomplete, frameIndex: hints.Incomplete, outputPath: hints.Incomplete, quality: hints.Incomplete) -> hints.Incomplete: ...
        def FrameToBase64(self, videoHandle: hints.Incomplete, format: hints.Incomplete) -> hints.Incomplete: ...
        def CalculateFrameSimilarity(self, frame1: hints.Incomplete, frame2: hints.Incomplete) -> hints.Incomplete: ...
        def GetVideoInfoFromPath(self, videoPath: hints.Incomplete) -> hints.Incomplete: ...
        def IsValidVideoFile(self, videoPath: hints.Incomplete) -> hints.Incomplete: ...
        def ExtractSingleFrame(self, videoPath: hints.Incomplete, frameIndex: hints.Incomplete) -> hints.Incomplete: ...
        def ExtractThumbnail(self, videoPath: hints.Incomplete) -> hints.Incomplete: ...
        def ConvertVideo(self, inputPath: hints.Incomplete, outputPath: hints.Incomplete, codec: hints.Incomplete, fps: hints.Incomplete) -> hints.Incomplete: ...
        def ResizeVideo(self, inputPath: hints.Incomplete, outputPath: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete) -> hints.Incomplete: ...
        def TrimVideo(self, inputPath: hints.Incomplete, outputPath: hints.Incomplete, startTime: hints.Incomplete, endTime: hints.Incomplete) -> hints.Incomplete: ...
        def CreateVideoFromImages(self, imageDir: hints.Incomplete, outputPath: hints.Incomplete, fps: hints.Incomplete, codec: hints.Incomplete) -> hints.Incomplete: ...
        def DetectSceneChanges(self, videoPath: hints.Incomplete, Threshold: hints.Incomplete) -> hints.Incomplete: ...
        def CalculateAverageBrightness(self, videoPath: hints.Incomplete) -> hints.Incomplete: ...
        def DetectMotion(self, videoPath: hints.Incomplete, Threshold: hints.Incomplete) -> hints.Incomplete: ...
        def SetWindowState(self, hwnd: hints.Incomplete, state: hints.Incomplete) -> hints.Incomplete: ...
        def FindWindow(self, class_name: hints.Incomplete, title: hints.Incomplete) -> hints.Incomplete: ...
        def GetClipboard(self) -> hints.Incomplete: ...
        def SetClipboard(self, text: hints.Incomplete) -> hints.Incomplete: ...
        def SendPaste(self, hwnd: hints.Incomplete) -> hints.Incomplete: ...
        def GetWindow(self, hwnd: hints.Incomplete, flag: hints.Incomplete) -> hints.Incomplete: ...
        def GetWindowTitle(self, hwnd: hints.Incomplete) -> hints.Incomplete: ...
        def GetWindowClass(self, hwnd: hints.Incomplete) -> hints.Incomplete: ...
        def GetWindowRect(self, hwnd: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def GetWindowProcessPath(self, hwnd: hints.Incomplete) -> hints.Incomplete: ...
        def GetWindowState(self, hwnd: hints.Incomplete, flag: hints.Incomplete) -> hints.Incomplete: ...
        def GetForegroundWindow(self) -> hints.Incomplete: ...
        def GetWindowProcessId(self, hwnd: hints.Incomplete) -> hints.Incomplete: ...
        def GetClientSize(self, hwnd: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def GetMousePointWindow(self) -> hints.Incomplete: ...
        def GetSpecialWindow(self, flag: hints.Incomplete) -> hints.Incomplete: ...
        def GetClientRect(self, hwnd: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def SetWindowText(self, hwnd: hints.Incomplete, title: hints.Incomplete) -> hints.Incomplete: ...
        def SetWindowSize(self, hwnd: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete) -> hints.Incomplete: ...
        def SetClientSize(self, hwnd: hints.Incomplete, width: hints.Incomplete, height: hints.Incomplete) -> hints.Incomplete: ...
        def SetWindowTransparent(self, hwnd: hints.Incomplete, alpha: hints.Incomplete) -> hints.Incomplete: ...
        def FindWindowEx(self, parent: hints.Incomplete, class_name: hints.Incomplete, title: hints.Incomplete) -> hints.Incomplete: ...
        def FindWindowByProcess(self, process_name: hints.Incomplete, class_name: hints.Incomplete, title: hints.Incomplete) -> hints.Incomplete: ...
        def MoveWindow(self, hwnd: hints.Incomplete, x: hints.Incomplete, y: hints.Incomplete) -> hints.Incomplete: ...
        def GetScaleFromWindows(self, hwnd: hints.Incomplete) -> hints.Incomplete: ...
        def GetWindowDpiAwarenessScale(self, hwnd: hints.Incomplete) -> hints.Incomplete: ...
        def EnumProcess(self, name: hints.Incomplete) -> hints.Incomplete: ...
        def EnumWindow(self, parent: hints.Incomplete, title: hints.Incomplete, className: hints.Incomplete, filter: hints.Incomplete) -> hints.Incomplete: ...
        def EnumWindowByProcess(self, process_name: hints.Incomplete, title: hints.Incomplete, class_name: hints.Incomplete, filter: hints.Incomplete) -> hints.Incomplete: ...
        def EnumWindowByProcessId(self, pid: hints.Incomplete, title: hints.Incomplete, class_name: hints.Incomplete, filter: hints.Incomplete) -> hints.Incomplete: ...
        def EnumWindowSuper(self, spec1: hints.Incomplete, flag1: hints.Incomplete, type1: hints.Incomplete, spec2: hints.Incomplete, flag2: hints.Incomplete, type2: hints.Incomplete, sort: hints.Incomplete) -> hints.Incomplete: ...
        def GetPointWindow(self, x: hints.Incomplete, y: hints.Incomplete) -> hints.Incomplete: ...
        def GetProcessInfo(self, pid: hints.Incomplete) -> hints.Incomplete: ...
        def ShowTaskBarIcon(self, hwnd: hints.Incomplete, show: hints.Incomplete) -> hints.Incomplete: ...
        def FindWindowByProcessId(self, process_id: hints.Incomplete, className: hints.Incomplete, title: hints.Incomplete) -> hints.Incomplete: ...
        def GetWindowThreadId(self, hwnd: hints.Incomplete) -> hints.Incomplete: ...
        def FindWindowSuper(self, spec1: hints.Incomplete, flag1: hints.Incomplete, type1: hints.Incomplete, spec2: hints.Incomplete, flag2: hints.Incomplete, type2: hints.Incomplete) -> hints.Incomplete: ...
        def ClientToScreen(self, hwnd: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def ScreenToClient(self, hwnd: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete, hints.Incomplete]: ...
        def GetForegroundFocus(self) -> hints.Incomplete: ...
        def SetWindowDisplay(self, hwnd: hints.Incomplete, affinity: hints.Incomplete) -> hints.Incomplete: ...
        def IsDisplayDead(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, time: hints.Incomplete) -> hints.Incomplete: ...
        def GetWindowsFps(self, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete) -> hints.Incomplete: ...
        def SetFontSmooth(self, enable: hints.Incomplete) -> hints.Incomplete: ...
        def CheckFontSmooth(self) -> hints.Incomplete: ...
        def GetCommandLine(self, hwnd: hints.Incomplete) -> hints.Incomplete: ...
        def TerminateProcess(self, pid: hints.Incomplete) -> hints.Incomplete: ...
        def TerminateProcessTree(self, pid: hints.Incomplete) -> hints.Incomplete: ...
        def EnableDebugPrivilege(self) -> hints.Incomplete: ...
        def SystemStart(self, applicationName: hints.Incomplete, commandLine: hints.Incomplete) -> hints.Incomplete: ...
        def CreateChildProcess(self, applicationName: hints.Incomplete, commandLine: hints.Incomplete, currentDirectory: hints.Incomplete, showType: hints.Incomplete, parentProcessId: hints.Incomplete) -> hints.Incomplete: ...
        def GetProcessIconImage(self, pid: hints.Incomplete, targetWidth: hints.Incomplete, targetHeight: hints.Incomplete) -> hints.Incomplete: ...
        def XmlCreateDocument(self) -> hints.Incomplete: ...
        def XmlParse(self, str: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlParseFile(self, filePath: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlToString(self, doc: hints.Incomplete, compact: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlSaveToFile(self, doc: hints.Incomplete, filePath: hints.Incomplete, compact: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlFree(self, doc: hints.Incomplete) -> hints.Incomplete: ...
        def XmlGetRootElement(self, doc: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlCreateElement(self, doc: hints.Incomplete, name: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlInsertRootElement(self, doc: hints.Incomplete, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlAppendChild(self, parent: hints.Incomplete, child: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetFirstChild(self, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetNextSibling(self, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlFindElement(self, parent: hints.Incomplete, name: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetElementName(self, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetElementText(self, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlSetElementText(self, element: hints.Incomplete, text: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlRemoveChild(self, parent: hints.Incomplete, child: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlInsertBefore(self, parent: hints.Incomplete, newChild: hints.Incomplete, refChild: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlInsertAfter(self, parent: hints.Incomplete, newChild: hints.Incomplete, refChild: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetParent(self, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetPreviousSibling(self, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetLastChild(self, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlCloneElement(self, doc: hints.Incomplete, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlHasChildren(self, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetAttribute(self, element: hints.Incomplete, name: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlSetAttribute(self, element: hints.Incomplete, name: hints.Incomplete, value: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetAttributeInt(self, element: hints.Incomplete, name: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlSetAttributeInt(self, element: hints.Incomplete, name: hints.Incomplete, value: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetAttributeDouble(self, element: hints.Incomplete, name: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlSetAttributeDouble(self, element: hints.Incomplete, name: hints.Incomplete, value: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetAttributeBool(self, element: hints.Incomplete, name: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlSetAttributeBool(self, element: hints.Incomplete, name: hints.Incomplete, value: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetAttributeInt64(self, element: hints.Incomplete, name: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlSetAttributeInt64(self, element: hints.Incomplete, name: hints.Incomplete, value: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlHasAttribute(self, element: hints.Incomplete, name: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetAttributeNames(self, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetAttributeCount(self, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlDeleteAttribute(self, element: hints.Incomplete, name: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlSetCDATA(self, doc: hints.Incomplete, element: hints.Incomplete, content: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlAddComment(self, doc: hints.Incomplete, element: hints.Incomplete, comment: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlSetDeclaration(self, doc: hints.Incomplete, version: hints.Incomplete, encoding: hints.Incomplete, standalone: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlQueryElement(self, doc: hints.Incomplete, path: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetChildCount(self, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetChildCountByName(self, parent: hints.Incomplete, name: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetChildByIndex(self, parent: hints.Incomplete, index: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetChildByNameAndIndex(self, parent: hints.Incomplete, name: hints.Incomplete, index: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlFindElementByAttribute(self, parent: hints.Incomplete, elementName: hints.Incomplete, attrName: hints.Incomplete, attrValue: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetElementDepth(self, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetElementPath(self, element: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlCompareElements(self, element1: hints.Incomplete, element2: hints.Incomplete, deep: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlMergeDocuments(self, targetDoc: hints.Incomplete, sourceDoc: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlValidate(self, doc: hints.Incomplete) -> tuple[hints.Incomplete, hints.Incomplete]: ...
        def XmlGetObjectCount(self) -> hints.Incomplete: ...
        def XmlCleanupAll(self) -> hints.Incomplete: ...
        def YoloInfer(self, handle: hints.Incomplete, imagePtr: hints.Incomplete) -> hints.Incomplete: ...
        def YoloLoadModel(self, modelPath: hints.Incomplete, outputPath: hints.Incomplete, names_label: hints.Incomplete, password: hints.Incomplete, modelType: hints.Incomplete, inferenceType: hints.Incomplete, inferenceDevice: hints.Incomplete) -> hints.Incomplete: ...
        def YoloLoadModelMemory(self, memoryAddr: hints.Incomplete, size: hints.Incomplete, modelType: hints.Incomplete, inferenceType: hints.Incomplete, inferenceDevice: hints.Incomplete) -> hints.Incomplete: ...
        def YoloReleaseModel(self, modelHandle: hints.Incomplete) -> hints.Incomplete: ...
        def YoloIsModelValid(self, modelHandle: hints.Incomplete) -> hints.Incomplete: ...
        def YoloListModels(self) -> hints.Incomplete: ...
        def YoloGetModelInfo(self, modelHandle: hints.Incomplete) -> hints.Incomplete: ...
        def YoloSetModelConfig(self, modelHandle: hints.Incomplete, configJson: hints.Incomplete) -> hints.Incomplete: ...
        def YoloGetModelConfig(self, modelHandle: hints.Incomplete) -> hints.Incomplete: ...
        def YoloWarmup(self, modelHandle: hints.Incomplete, iterations: hints.Incomplete) -> hints.Incomplete: ...
        def YoloDetect(self, modelHandle: hints.Incomplete, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, classes: hints.Incomplete, confidence: hints.Incomplete, iou: hints.Incomplete, maxDetections: hints.Incomplete) -> hints.Incomplete: ...
        def YoloDetectSimple(self, modelHandle: hints.Incomplete, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete) -> hints.Incomplete: ...
        def YoloDetectFromPtr(self, modelHandle: hints.Incomplete, imagePtr: hints.Incomplete, classes: hints.Incomplete, confidence: hints.Incomplete, iou: hints.Incomplete, maxDetections: hints.Incomplete) -> hints.Incomplete: ...
        def YoloDetectFromFile(self, modelHandle: hints.Incomplete, imagePath: hints.Incomplete, classes: hints.Incomplete, confidence: hints.Incomplete, iou: hints.Incomplete, maxDetections: hints.Incomplete) -> hints.Incomplete: ...
        def YoloDetectFromBase64(self, modelHandle: hints.Incomplete, base64Data: hints.Incomplete, classes: hints.Incomplete, confidence: hints.Incomplete, iou: hints.Incomplete, maxDetections: hints.Incomplete) -> hints.Incomplete: ...
        def YoloDetectBatch(self, modelHandle: hints.Incomplete, imagesJson: hints.Incomplete, classes: hints.Incomplete, confidence: hints.Incomplete, iou: hints.Incomplete, maxDetections: hints.Incomplete) -> hints.Incomplete: ...
        def YoloClassify(self, modelHandle: hints.Incomplete, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, topK: hints.Incomplete) -> hints.Incomplete: ...
        def YoloClassifyFromPtr(self, modelHandle: hints.Incomplete, imagePtr: hints.Incomplete, topK: hints.Incomplete) -> hints.Incomplete: ...
        def YoloClassifyFromFile(self, modelHandle: hints.Incomplete, imagePath: hints.Incomplete, topK: hints.Incomplete) -> hints.Incomplete: ...
        def YoloSegment(self, modelHandle: hints.Incomplete, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, confidence: hints.Incomplete, iou: hints.Incomplete) -> hints.Incomplete: ...
        def YoloSegmentFromPtr(self, modelHandle: hints.Incomplete, imagePtr: hints.Incomplete, confidence: hints.Incomplete, iou: hints.Incomplete) -> hints.Incomplete: ...
        def YoloPose(self, modelHandle: hints.Incomplete, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, confidence: hints.Incomplete, iou: hints.Incomplete) -> hints.Incomplete: ...
        def YoloPoseFromPtr(self, modelHandle: hints.Incomplete, imagePtr: hints.Incomplete, confidence: hints.Incomplete, iou: hints.Incomplete) -> hints.Incomplete: ...
        def YoloObb(self, modelHandle: hints.Incomplete, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, confidence: hints.Incomplete, iou: hints.Incomplete) -> hints.Incomplete: ...
        def YoloObbFromPtr(self, modelHandle: hints.Incomplete, imagePtr: hints.Incomplete, confidence: hints.Incomplete, iou: hints.Incomplete) -> hints.Incomplete: ...
        def YoloKeyPoint(self, modelHandle: hints.Incomplete, x1: hints.Incomplete, y1: hints.Incomplete, x2: hints.Incomplete, y2: hints.Incomplete, confidence: hints.Incomplete, iou: hints.Incomplete) -> hints.Incomplete: ...
        def YoloKeyPointFromPtr(self, modelHandle: hints.Incomplete, imagePtr: hints.Incomplete, confidence: hints.Incomplete, iou: hints.Incomplete) -> hints.Incomplete: ...
        def YoloGetInferenceStats(self, modelHandle: hints.Incomplete) -> hints.Incomplete: ...
        def YoloResetStats(self, modelHandle: hints.Incomplete) -> hints.Incomplete: ...
        def YoloGetLastError(self) -> hints.Incomplete: ...
        def YoloClearError(self) -> hints.Incomplete: ...
        def CreateCOLAPlugInterFace(self) -> hints.Incomplete: ...
        def DestroyCOLAPlugInterFace(self) -> hints.Incomplete: ...
        def Reg(self, userCode: hints.Incomplete, softCode: hints.Incomplete, featureList: hints.Incomplete) -> hints.Incomplete: ...
        def Ver(self) -> hints.Incomplete: ...
        def SetPath(self, path: hints.Incomplete) -> hints.Incomplete: ...
        def GetPath(self) -> hints.Incomplete: ...
        def GetMachineCode(self) -> hints.Incomplete: ...
        def GetBasePath(self) -> hints.Incomplete: ...
        def BindWindow(self, hwnd: hints.Incomplete, display: hints.Incomplete, mouse: hints.Incomplete, keypad: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def BindWindowEx(self, hwnd: hints.Incomplete, display: hints.Incomplete, mouse: hints.Incomplete, keypad: hints.Incomplete, pubstr: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def UnBindWindow(self) -> hints.Incomplete: ...
        def GetBindWindow(self) -> hints.Incomplete: ...
        def ReleaseWindowsDll(self, hwnd: hints.Incomplete) -> hints.Incomplete: ...
        def FreeStringPtr(self, ptr: hints.Incomplete) -> hints.Incomplete: ...
        def GetStringSize(self, ptr: hints.Incomplete) -> hints.Incomplete: ...
        def GetStringFromPtr(self, ptr: hints.Incomplete, lpString: hints.Incomplete, size: hints.Incomplete) -> hints.Incomplete: ...
        def delay(self, millisecond: hints.Incomplete) -> hints.Incomplete: ...
        def Delays(self, minMillisecond: hints.Incomplete, maxMillisecond: hints.Incomplete) -> hints.Incomplete: ...
        def SetUAC(self, enable: hints.Incomplete) -> hints.Incomplete: ...
        def CheckUAC(self) -> hints.Incomplete: ...
        def RunApp(self, appPath: hints.Incomplete, mode: hints.Incomplete) -> hints.Incomplete: ...
        def ExecuteCmd(self, cmd: hints.Incomplete, current_dir: hints.Incomplete, time_out: hints.Incomplete) -> hints.Incomplete: ...
        def GetConfig(self, configKey: hints.Incomplete) -> hints.Incomplete: ...
        def SetConfig(self, configStr: hints.Incomplete) -> hints.Incomplete: ...
        def SetConfigByKey(self, key: hints.Incomplete, value: hints.Incomplete) -> hints.Incomplete: ...
        def SendDropFiles(self, hwnd: hints.Incomplete, file_path: hints.Incomplete) -> hints.Incomplete: ...
        def FreeMemoryPtr(self, ptr: hints.Incomplete) -> hints.Incomplete: ...
        def SetDefaultEncode(self, inputEncoding: hints.Incomplete, outputEncoding: hints.Incomplete) -> hints.Incomplete: ...
        def GetLastError(self) -> hints.Incomplete: ...
        def GetLastErrorString(self) -> hints.Incomplete: ...
        def HideModule(self, moduleName: hints.Incomplete) -> hints.Incomplete: ...
        def UnhideModule(self, ctx: hints.Incomplete) -> hints.Incomplete: ...
        def GetPlugInfo(self, type: hints.Incomplete) -> hints.Incomplete: ...


IOlaPlug._methods_ = [
    COMMETHOD(
        [dispid(1610743808)],
        HRESULT,
        'GetRandomNumber',
        (['in'], c_int, 'min'),
        (['in'], c_int, 'max'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743809)],
        HRESULT,
        'GetRandomDouble',
        (['in'], c_double, 'min'),
        (['in'], c_double, 'max'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743810)],
        HRESULT,
        'ExcludePos',
        (['in'], BSTR, 'json'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743811)],
        HRESULT,
        'FindNearestPos',
        (['in'], BSTR, 'json'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743812)],
        HRESULT,
        'SortPosDistance',
        (['in'], BSTR, 'json'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743813)],
        HRESULT,
        'GetDenseRect',
        (['in'], c_longlong, 'image'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['out'], POINTER(VARIANT), 'x1'),
        (['out'], POINTER(VARIANT), 'y1'),
        (['out'], POINTER(VARIANT), 'x2'),
        (['out'], POINTER(VARIANT), 'y2'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743814)],
        HRESULT,
        'PathPlanning',
        (['in'], c_longlong, 'image'),
        (['in'], c_int, 'startX'),
        (['in'], c_int, 'startY'),
        (['in'], c_int, 'endX'),
        (['in'], c_int, 'endY'),
        (['in'], c_double, 'potentialRadius'),
        (['in'], c_double, 'searchRadius'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743815)],
        HRESULT,
        'CreateGraph',
        (['in'], BSTR, 'json'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743816)],
        HRESULT,
        'GetGraph',
        (['in'], c_longlong, 'graphPtr'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743817)],
        HRESULT,
        'AddEdge',
        (['in'], c_longlong, 'graphPtr'),
        (['in'], BSTR, 'from'),
        (['in'], BSTR, 'to'),
        (['in'], c_double, 'weight'),
        (['in'], c_longlong, 'isDirected'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743818)],
        HRESULT,
        'GetShortestPath',
        (['in'], c_longlong, 'graphPtr'),
        (['in'], BSTR, 'from'),
        (['in'], BSTR, 'to'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743819)],
        HRESULT,
        'GetShortestDistance',
        (['in'], c_longlong, 'graphPtr'),
        (['in'], BSTR, 'from'),
        (['in'], BSTR, 'to'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743820)],
        HRESULT,
        'ClearGraph',
        (['in'], c_longlong, 'graphPtr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743821)],
        HRESULT,
        'DeleteGraph',
        (['in'], c_longlong, 'graphPtr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743822)],
        HRESULT,
        'GetNodeCount',
        (['in'], c_longlong, 'graphPtr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743823)],
        HRESULT,
        'GetEdgeCount',
        (['in'], c_longlong, 'graphPtr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743824)],
        HRESULT,
        'GetShortestPathToAllNodes',
        (['in'], c_longlong, 'graphPtr'),
        (['in'], BSTR, 'startNode'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743825)],
        HRESULT,
        'GetMinimumSpanningTree',
        (['in'], c_longlong, 'graphPtr'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743826)],
        HRESULT,
        'GetMinimumArborescence',
        (['in'], c_longlong, 'graphPtr'),
        (['in'], BSTR, 'root'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743827)],
        HRESULT,
        'GetDirectedPathToAllNodes',
        (['in'], c_longlong, 'graphPtr'),
        (['in'], BSTR, 'startNode'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743828)],
        HRESULT,
        'CreateGraphFromCoordinates',
        (['in'], BSTR, 'json'),
        (['in'], c_longlong, 'connectAll'),
        (['in'], c_double, 'maxDistance'),
        (['in'], c_longlong, 'useEuclideanDistance'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743829)],
        HRESULT,
        'AddCoordinateNode',
        (['in'], c_longlong, 'graphPtr'),
        (['in'], BSTR, 'name'),
        (['in'], c_double, 'x'),
        (['in'], c_double, 'y'),
        (['in'], c_longlong, 'connectToExisting'),
        (['in'], c_double, 'maxDistance'),
        (['in'], c_longlong, 'useEuclideanDistance'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743830)],
        HRESULT,
        'GetNodeCoordinates',
        (['in'], c_longlong, 'graphPtr'),
        (['in'], BSTR, 'name'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743831)],
        HRESULT,
        'SetNodeConnection',
        (['in'], c_longlong, 'graphPtr'),
        (['in'], BSTR, 'from'),
        (['in'], BSTR, 'to'),
        (['in'], c_longlong, 'canConnect'),
        (['in'], c_double, 'weight'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743832)],
        HRESULT,
        'GetNodeConnectionStatus',
        (['in'], c_longlong, 'graphPtr'),
        (['in'], BSTR, 'from'),
        (['in'], BSTR, 'to'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743833)],
        HRESULT,
        'Assemble',
        (['in'], BSTR, 'asmStr'),
        (['in'], c_longlong, 'baseAddr'),
        (['in'], c_int, 'arch'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743834)],
        HRESULT,
        'Disassemble',
        (['in'], BSTR, 'asmCode'),
        (['in'], c_longlong, 'baseAddr'),
        (['in'], c_int, 'arch'),
        (['in'], c_int, 'mode'),
        (['in'], c_int, 'showType'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743835)],
        HRESULT,
        'AsmCall',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'asmStr'),
        (['in'], c_int, 'type'),
        (['in'], c_longlong, 'baseAddr'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743836)],
        HRESULT,
        'Login',
        (['in'], BSTR, 'userCode'),
        (['in'], BSTR, 'softCode'),
        (['in'], BSTR, 'featureList'),
        (['in'], BSTR, 'softVersion'),
        (['in'], BSTR, 'dealerCode'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743837)],
        HRESULT,
        'Activate',
        (['in'], BSTR, 'userCode'),
        (['in'], BSTR, 'softCode'),
        (['in'], BSTR, 'softVersion'),
        (['in'], BSTR, 'dealerCode'),
        (['in'], BSTR, 'licenseKey'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743838)],
        HRESULT,
        'DmaAddDevice',
        (['in'], c_int, 'vmId'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743839)],
        HRESULT,
        'DmaAddDeviceEx',
        (['in'], BSTR, 'connectionString'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743840)],
        HRESULT,
        'DmaRemoveDevice',
        (['in'], c_longlong, 'deviceId'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743841)],
        HRESULT,
        'DmaGetPidFromName',
        (['in'], c_longlong, 'deviceId'),
        (['in'], BSTR, 'processName'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743842)],
        HRESULT,
        'DmaGetPidList',
        (['in'], c_longlong, 'deviceId'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743843)],
        HRESULT,
        'DmaGetProcessInfo',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743844)],
        HRESULT,
        'DmaGetModuleBase',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'moduleName'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743845)],
        HRESULT,
        'DmaGetModuleSize',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'moduleName'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743846)],
        HRESULT,
        'DmaGetProcAddress',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'moduleName'),
        (['in'], BSTR, 'functionName'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743847)],
        HRESULT,
        'DmaScatterCreate',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743848)],
        HRESULT,
        'DmaScatterPrepare',
        (['in'], c_longlong, 'scatterHandle'),
        (['in'], c_longlong, 'address'),
        (['in'], c_int, 'size'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743849)],
        HRESULT,
        'DmaScatterExecute',
        (['in'], c_longlong, 'scatterHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743850)],
        HRESULT,
        'DmaScatterRead',
        (['in'], c_longlong, 'scatterHandle'),
        (['in'], c_longlong, 'address'),
        (['in'], c_longlong, 'buffer'),
        (['in'], c_int, 'size'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743851)],
        HRESULT,
        'DmaScatterClear',
        (['in'], c_longlong, 'scatterHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743852)],
        HRESULT,
        'DmaScatterClose',
        (['in'], c_longlong, 'scatterHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743853)],
        HRESULT,
        'DmaFindData',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr_range'),
        (['in'], BSTR, 'data'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743854)],
        HRESULT,
        'DmaFindDataEx',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr_range'),
        (['in'], BSTR, 'data'),
        (['in'], c_int, 'step'),
        (['in'], c_int, 'multi_thread'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743855)],
        HRESULT,
        'DmaFindDouble',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr_range'),
        (['in'], c_double, 'double_value_min'),
        (['in'], c_double, 'double_value_max'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743856)],
        HRESULT,
        'DmaFindDoubleEx',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr_range'),
        (['in'], c_double, 'double_value_min'),
        (['in'], c_double, 'double_value_max'),
        (['in'], c_int, 'step'),
        (['in'], c_int, 'multi_thread'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743857)],
        HRESULT,
        'DmaFindFloat',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr_range'),
        (['in'], c_float, 'float_value_min'),
        (['in'], c_float, 'float_value_max'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743858)],
        HRESULT,
        'DmaFindFloatEx',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr_range'),
        (['in'], c_float, 'float_value_min'),
        (['in'], c_float, 'float_value_max'),
        (['in'], c_int, 'step'),
        (['in'], c_int, 'multi_thread'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743859)],
        HRESULT,
        'DmaFindInt',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr_range'),
        (['in'], c_longlong, 'int_value_min'),
        (['in'], c_longlong, 'int_value_max'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743860)],
        HRESULT,
        'DmaFindIntEx',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr_range'),
        (['in'], c_longlong, 'int_value_min'),
        (['in'], c_longlong, 'int_value_max'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'step'),
        (['in'], c_int, 'multi_thread'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743861)],
        HRESULT,
        'DmaFindString',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr_range'),
        (['in'], BSTR, 'string_value'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743862)],
        HRESULT,
        'DmaFindStringEx',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr_range'),
        (['in'], BSTR, 'string_value'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'step'),
        (['in'], c_int, 'multi_thread'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743863)],
        HRESULT,
        'DmaReadData',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743864)],
        HRESULT,
        'DmaReadDataAddr',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743865)],
        HRESULT,
        'DmaReadDataAddrToBin',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743866)],
        HRESULT,
        'DmaReadDataToBin',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743867)],
        HRESULT,
        'DmaReadDouble',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743868)],
        HRESULT,
        'DmaReadDoubleAddr',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], c_longlong, 'addr'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743869)],
        HRESULT,
        'DmaReadFloat',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr'),
        (['out', 'retval'], POINTER(c_float), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743870)],
        HRESULT,
        'DmaReadFloatAddr',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], c_longlong, 'addr'),
        (['out', 'retval'], POINTER(c_float), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743871)],
        HRESULT,
        'DmaReadInt',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743872)],
        HRESULT,
        'DmaReadIntAddr',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743873)],
        HRESULT,
        'DmaReadString',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743874)],
        HRESULT,
        'DmaReadStringAddr',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743875)],
        HRESULT,
        'DmaWriteData',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr'),
        (['in'], BSTR, 'data'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743876)],
        HRESULT,
        'DmaWriteDataFromBin',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr'),
        (['in'], c_longlong, 'data'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743877)],
        HRESULT,
        'DmaWriteDataAddr',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], c_longlong, 'addr'),
        (['in'], BSTR, 'data'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743878)],
        HRESULT,
        'DmaWriteDataAddrFromBin',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_longlong, 'data'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743879)],
        HRESULT,
        'DmaWriteDouble',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr'),
        (['in'], c_double, 'double_value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743880)],
        HRESULT,
        'DmaWriteDoubleAddr',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_double, 'double_value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743881)],
        HRESULT,
        'DmaWriteFloat',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr'),
        (['in'], c_float, 'float_value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743882)],
        HRESULT,
        'DmaWriteFloatAddr',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_float, 'float_value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743883)],
        HRESULT,
        'DmaWriteInt',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr'),
        (['in'], c_int, 'type'),
        (['in'], c_longlong, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743884)],
        HRESULT,
        'DmaWriteIntAddr',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'type'),
        (['in'], c_longlong, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743885)],
        HRESULT,
        'DmaWriteString',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], BSTR, 'addr'),
        (['in'], c_int, 'type'),
        (['in'], BSTR, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743886)],
        HRESULT,
        'DmaWriteStringAddr',
        (['in'], c_longlong, 'deviceId'),
        (['in'], c_int, 'pid'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'type'),
        (['in'], BSTR, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743887)],
        HRESULT,
        'DrawGuiCleanup',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743888)],
        HRESULT,
        'DrawGuiRectangle',
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['in'], c_int, 'mode'),
        (['in'], c_double, 'lineThickness'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743889)],
        HRESULT,
        'DrawGuiCircle',
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['in'], c_int, 'radius'),
        (['in'], c_int, 'mode'),
        (['in'], c_double, 'lineThickness'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743890)],
        HRESULT,
        'DrawGuiLine',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], c_double, 'lineThickness'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743891)],
        HRESULT,
        'DrawGuiText',
        (['in'], BSTR, 'text'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['in'], BSTR, 'fontPath'),
        (['in'], c_int, 'fontSize'),
        (['in'], c_int, 'align'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743892)],
        HRESULT,
        'DrawGuiImage',
        (['in'], BSTR, 'imagePath'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743893)],
        HRESULT,
        'DrawGuiImagePtr',
        (['in'], c_longlong, 'imagePtr'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743894)],
        HRESULT,
        'DrawGuiWindow',
        (['in'], BSTR, 'title'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['in'], c_int, 'style'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743895)],
        HRESULT,
        'DrawGuiPanel',
        (['in'], c_longlong, 'parentHandle'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743896)],
        HRESULT,
        'DrawGuiButton',
        (['in'], c_longlong, 'parentHandle'),
        (['in'], BSTR, 'text'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743897)],
        HRESULT,
        'DrawGuiDeleteObject',
        (['in'], c_longlong, 'handle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743898)],
        HRESULT,
        'DrawGuiClearAll',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743899)],
        HRESULT,
        'DrawGuiSetGuiActive',
        (['in'], c_int, 'active'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743900)],
        HRESULT,
        'DrawGuiIsGuiActive',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743901)],
        HRESULT,
        'DrawGuiSetGuiClickThrough',
        (['in'], c_int, 'enabled'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743902)],
        HRESULT,
        'DrawGuiIsGuiClickThrough',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743903)],
        HRESULT,
        'DrawGuiSetPosition',
        (['in'], c_longlong, 'handle'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743904)],
        HRESULT,
        'DrawGuiSetSize',
        (['in'], c_longlong, 'handle'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743905)],
        HRESULT,
        'DrawGuiSetColor',
        (['in'], c_longlong, 'handle'),
        (['in'], c_int, 'r'),
        (['in'], c_int, 'g'),
        (['in'], c_int, 'b'),
        (['in'], c_int, 'a'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743906)],
        HRESULT,
        'DrawGuiSetAlpha',
        (['in'], c_longlong, 'handle'),
        (['in'], c_int, 'alpha'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743907)],
        HRESULT,
        'DrawGuiSetDrawMode',
        (['in'], c_longlong, 'handle'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743908)],
        HRESULT,
        'DrawGuiSetLineThickness',
        (['in'], c_longlong, 'handle'),
        (['in'], c_double, 'thickness'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743909)],
        HRESULT,
        'DrawGuiSetFont',
        (['in'], c_longlong, 'handle'),
        (['in'], BSTR, 'fontPath'),
        (['in'], c_int, 'fontSize'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743910)],
        HRESULT,
        'DrawGuiSetTextAlign',
        (['in'], c_longlong, 'handle'),
        (['in'], c_int, 'align'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743911)],
        HRESULT,
        'DrawGuiSetText',
        (['in'], c_longlong, 'handle'),
        (['in'], BSTR, 'text'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743912)],
        HRESULT,
        'DrawGuiSetVisible',
        (['in'], c_longlong, 'handle'),
        (['in'], c_int, 'visible'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743913)],
        HRESULT,
        'DrawGuiGetPosition',
        (['in'], c_longlong, 'handle'),
        (['out'], POINTER(VARIANT), 'x'),
        (['out'], POINTER(VARIANT), 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743914)],
        HRESULT,
        'DrawGuiGetSize',
        (['in'], c_longlong, 'handle'),
        (['out'], POINTER(VARIANT), 'width'),
        (['out'], POINTER(VARIANT), 'height'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743915)],
        HRESULT,
        'DrawGuiSetZOrder',
        (['in'], c_longlong, 'handle'),
        (['in'], c_int, 'zOrder'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743916)],
        HRESULT,
        'DrawGuiSetParent',
        (['in'], c_longlong, 'handle'),
        (['in'], c_longlong, 'parentHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743917)],
        HRESULT,
        'DrawGuiIsPointInObject',
        (['in'], c_longlong, 'handle'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743918)],
        HRESULT,
        'DrawGuiSetWindowTitle',
        (['in'], c_longlong, 'handle'),
        (['in'], BSTR, 'title'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743919)],
        HRESULT,
        'DrawGuiSetWindowStyle',
        (['in'], c_longlong, 'handle'),
        (['in'], c_int, 'style'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743920)],
        HRESULT,
        'DrawGuiSetWindowTopMost',
        (['in'], c_longlong, 'handle'),
        (['in'], c_int, 'topMost'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743921)],
        HRESULT,
        'DrawGuiSetWindowTransparency',
        (['in'], c_longlong, 'handle'),
        (['in'], c_int, 'alpha'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743922)],
        HRESULT,
        'DrawGuiSetButtonCallback',
        (['in'], c_longlong, 'handle'),
        (['in'], c_longlong, 'callback'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743923)],
        HRESULT,
        'DrawGuiSetMouseCallback',
        (['in'], c_longlong, 'handle'),
        (['in'], c_longlong, 'callback'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743924)],
        HRESULT,
        'DrawGuiGetDrawObjectType',
        (['in'], c_longlong, 'handle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743925)],
        HRESULT,
        'LoadDriver',
        (['in'], BSTR, 'driver_name'),
        (['in'], BSTR, 'driver_path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743926)],
        HRESULT,
        'UnloadDriver',
        (['in'], BSTR, 'driver_name'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743927)],
        HRESULT,
        'DriverTest',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743928)],
        HRESULT,
        'LoadPdb',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743929)],
        HRESULT,
        'GetPdbDownloadUrls',
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743930)],
        HRESULT,
        'AddProtectPID',
        (['in'], c_longlong, 'pid'),
        (['in'], c_longlong, 'mode'),
        (['in'], c_longlong, 'allow_pid'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743931)],
        HRESULT,
        'RemoveProtectPID',
        (['in'], c_longlong, 'pid'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743932)],
        HRESULT,
        'AddAllowPID',
        (['in'], c_longlong, 'pid'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743933)],
        HRESULT,
        'RemoveAllowPID',
        (['in'], c_longlong, 'pid'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743934)],
        HRESULT,
        'HideProcess',
        (['in'], c_longlong, 'pid'),
        (['in'], c_int, 'enable'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743935)],
        HRESULT,
        'ProtectProcess',
        (['in'], c_longlong, 'pid'),
        (['in'], c_int, 'enable'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743936)],
        HRESULT,
        'ProtectProcess2',
        (['in'], c_longlong, 'pid'),
        (['in'], c_int, 'enable'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743937)],
        HRESULT,
        'SetMemoryMode',
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743938)],
        HRESULT,
        'ExportDriver',
        (['in'], BSTR, 'driver_path'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743939)],
        HRESULT,
        'FakeProcess',
        (['in'], c_longlong, 'pid'),
        (['in'], c_longlong, 'fake_pid'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743940)],
        HRESULT,
        'ProtectWindow',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_int, 'flag'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743941)],
        HRESULT,
        'KeOpenThread',
        (['in'], c_longlong, 'thread_id'),
        (['out'], POINTER(VARIANT), 'thread_handle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743942)],
        HRESULT,
        'KeOpenProcess',
        (['in'], c_longlong, 'pid'),
        (['out'], POINTER(VARIANT), 'process_handle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743943)],
        HRESULT,
        'StartSecurityGuard',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743944)],
        HRESULT,
        'ProtectFileTestDriver',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743945)],
        HRESULT,
        'ProtectFileEnableDriver',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743946)],
        HRESULT,
        'ProtectFileDisableDriver',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743947)],
        HRESULT,
        'ProtectFileStartFilter',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743948)],
        HRESULT,
        'ProtectFileStopFilter',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743949)],
        HRESULT,
        'ProtectFileAddProtectedPath',
        (['in'], BSTR, 'path'),
        (['in'], c_int, 'mode'),
        (['in'], c_int, 'is_directory'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743950)],
        HRESULT,
        'ProtectFileRemoveProtectedPath',
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743951)],
        HRESULT,
        'ProtectFileClearProtectedPaths',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743952)],
        HRESULT,
        'ProtectFileQueryProtectedPath',
        (['in'], BSTR, 'path'),
        (['out'], POINTER(VARIANT), 'mode'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743953)],
        HRESULT,
        'ProtectFileAddWhitelist',
        (['in'], c_longlong, 'pid'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743954)],
        HRESULT,
        'ProtectFileRemoveWhitelist',
        (['in'], c_longlong, 'pid'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743955)],
        HRESULT,
        'ProtectFileClearWhitelist',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743956)],
        HRESULT,
        'ProtectFileQueryWhitelist',
        (['in'], c_longlong, 'pid'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743957)],
        HRESULT,
        'ProtectFileAddBlacklist',
        (['in'], c_longlong, 'pid'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743958)],
        HRESULT,
        'ProtectFileRemoveBlacklist',
        (['in'], c_longlong, 'pid'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743959)],
        HRESULT,
        'ProtectFileClearBlacklist',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743960)],
        HRESULT,
        'ProtectFileQueryBlacklist',
        (['in'], c_longlong, 'pid'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743961)],
        HRESULT,
        'VipProtectEnableDriver',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743962)],
        HRESULT,
        'VipProtectDisableDriver',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743963)],
        HRESULT,
        'VipProtectAddProtect',
        (['in'], c_longlong, 'pid'),
        (['in'], BSTR, 'path'),
        (['in'], c_int, 'mode'),
        (['in'], c_int, 'permission'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743964)],
        HRESULT,
        'VipProtectRemoveProtect',
        (['in'], c_longlong, 'pid'),
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743965)],
        HRESULT,
        'VipProtectClearAll',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743966)],
        HRESULT,
        'VipProtectAddWhitelist',
        (['in'], c_longlong, 'pid'),
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743967)],
        HRESULT,
        'VipProtectRemoveWhitelist',
        (['in'], c_longlong, 'pid'),
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743968)],
        HRESULT,
        'VipProtectClearWhitelist',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743969)],
        HRESULT,
        'VipProtectAddBlacklist',
        (['in'], c_longlong, 'pid'),
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743970)],
        HRESULT,
        'VipProtectRemoveBlacklist',
        (['in'], c_longlong, 'pid'),
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743971)],
        HRESULT,
        'VipProtectClearBlacklist',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743972)],
        HRESULT,
        'EnabletVtDriver',
        (['in'], c_int, 'enable'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743973)],
        HRESULT,
        'VtFakeWriteData',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['in'], BSTR, 'data'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743974)],
        HRESULT,
        'VtFakeWriteDataFromBin',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['in'], c_longlong, 'data'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743975)],
        HRESULT,
        'VtFakeWriteDataAddr',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], BSTR, 'data'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743976)],
        HRESULT,
        'VtFakeWriteDataAddrFromBin',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_longlong, 'data'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743977)],
        HRESULT,
        'VtUnFakeMemoryAddr',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743978)],
        HRESULT,
        'VtUnFakeMemory',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743979)],
        HRESULT,
        'GenerateRSAKey',
        (['in'], BSTR, 'publicKeyPath'),
        (['in'], BSTR, 'privateKeyPath'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'keySize'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743980)],
        HRESULT,
        'ConvertRSAPublicKey',
        (['in'], BSTR, 'publicKey'),
        (['in'], c_int, 'inputType'),
        (['in'], c_int, 'outputType'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743981)],
        HRESULT,
        'ConvertRSAPrivateKey',
        (['in'], BSTR, 'privateKey'),
        (['in'], c_int, 'inputType'),
        (['in'], c_int, 'outputType'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743982)],
        HRESULT,
        'EncryptWithRsa',
        (['in'], BSTR, 'message'),
        (['in'], BSTR, 'publicKey'),
        (['in'], c_int, 'paddingType'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743983)],
        HRESULT,
        'DecryptWithRsa',
        (['in'], BSTR, 'cipher'),
        (['in'], BSTR, 'privateKey'),
        (['in'], c_int, 'paddingType'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743984)],
        HRESULT,
        'SignWithRsa',
        (['in'], BSTR, 'message'),
        (['in'], BSTR, 'privateCer'),
        (['in'], c_int, 'shaType'),
        (['in'], c_int, 'paddingType'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743985)],
        HRESULT,
        'VerifySignWithRsa',
        (['in'], BSTR, 'message'),
        (['in'], BSTR, 'signature'),
        (['in'], c_int, 'shaType'),
        (['in'], c_int, 'paddingType'),
        (['in'], BSTR, 'publicCer'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743986)],
        HRESULT,
        'AESEncrypt',
        (['in'], BSTR, 'source'),
        (['in'], BSTR, 'key'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743987)],
        HRESULT,
        'AESDecrypt',
        (['in'], BSTR, 'source'),
        (['in'], BSTR, 'key'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743988)],
        HRESULT,
        'AESEncryptEx',
        (['in'], BSTR, 'source'),
        (['in'], BSTR, 'key'),
        (['in'], BSTR, 'iv'),
        (['in'], c_int, 'mode'),
        (['in'], c_int, 'paddingType'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743989)],
        HRESULT,
        'AESDecryptEx',
        (['in'], BSTR, 'source'),
        (['in'], BSTR, 'key'),
        (['in'], BSTR, 'iv'),
        (['in'], c_int, 'mode'),
        (['in'], c_int, 'paddingType'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743990)],
        HRESULT,
        'MD5Encrypt',
        (['in'], BSTR, 'source'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743991)],
        HRESULT,
        'SHAHash',
        (['in'], BSTR, 'source'),
        (['in'], c_int, 'shaType'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743992)],
        HRESULT,
        'HMAC',
        (['in'], BSTR, 'source'),
        (['in'], BSTR, 'key'),
        (['in'], c_int, 'shaType'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743993)],
        HRESULT,
        'GenerateRandomBytes',
        (['in'], c_int, 'length'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743994)],
        HRESULT,
        'GenerateGuid',
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743995)],
        HRESULT,
        'Base64Encode',
        (['in'], BSTR, 'source'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743996)],
        HRESULT,
        'Base64Decode',
        (['in'], BSTR, 'source'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743997)],
        HRESULT,
        'PBKDF2',
        (['in'], BSTR, 'password'),
        (['in'], BSTR, 'salt'),
        (['in'], c_int, 'iterations'),
        (['in'], c_int, 'keyLength'),
        (['in'], c_int, 'shaType'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743998)],
        HRESULT,
        'MD5File',
        (['in'], BSTR, 'filePath'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610743999)],
        HRESULT,
        'SHAFile',
        (['in'], BSTR, 'filePath'),
        (['in'], c_int, 'shaType'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744000)],
        HRESULT,
        'CreateFolder',
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744001)],
        HRESULT,
        'DeleteFolder',
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744002)],
        HRESULT,
        'GetFolderList',
        (['in'], BSTR, 'path'),
        (['in'], BSTR, 'baseDir'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744003)],
        HRESULT,
        'IsDirectory',
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744004)],
        HRESULT,
        'IsFile',
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744005)],
        HRESULT,
        'CreateFile',
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744006)],
        HRESULT,
        'DeleteFile',
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744007)],
        HRESULT,
        'CopyFile',
        (['in'], BSTR, 'src'),
        (['in'], BSTR, 'dst'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744008)],
        HRESULT,
        'MoveFile',
        (['in'], BSTR, 'src'),
        (['in'], BSTR, 'dst'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744009)],
        HRESULT,
        'RenameFile',
        (['in'], BSTR, 'src'),
        (['in'], BSTR, 'dst'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744010)],
        HRESULT,
        'GetFileSize',
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744011)],
        HRESULT,
        'GetFileList',
        (['in'], BSTR, 'path'),
        (['in'], BSTR, 'baseDir'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744012)],
        HRESULT,
        'GetFileName',
        (['in'], BSTR, 'path'),
        (['in'], c_int, 'withExtension'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744013)],
        HRESULT,
        'ToAbsolutePath',
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744014)],
        HRESULT,
        'ToRelativePath',
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744015)],
        HRESULT,
        'FileOrDirectoryExists',
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744016)],
        HRESULT,
        'ReadFileString',
        (['in'], BSTR, 'filePath'),
        (['in'], c_int, 'encoding'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744017)],
        HRESULT,
        'ReadBytesFromFile',
        (['in'], BSTR, 'filePath'),
        (['in'], c_int, 'offset'),
        (['in'], c_longlong, 'size'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744018)],
        HRESULT,
        'WriteStringToFile',
        (['in'], BSTR, 'filePath'),
        (['in'], BSTR, 'data'),
        (['in'], c_int, 'encoding'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744019)],
        HRESULT,
        'WriteBytesToFile',
        (['in'], BSTR, 'filePath'),
        (['in'], c_longlong, 'dataAddr'),
        (['in'], c_int, 'dataSize'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744020)],
        HRESULT,
        'StartHotkeyHook',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744021)],
        HRESULT,
        'StopHotkeyHook',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744022)],
        HRESULT,
        'RegisterHotkey',
        (['in'], c_int, 'keycode'),
        (['in'], c_int, 'modifiers'),
        (['in'], c_longlong, 'callback'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744023)],
        HRESULT,
        'UnregisterHotkey',
        (['in'], c_int, 'keycode'),
        (['in'], c_int, 'modifiers'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744024)],
        HRESULT,
        'RegisterMouseButton',
        (['in'], c_int, 'button'),
        (['in'], c_int, 'type'),
        (['in'], c_longlong, 'callback'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744025)],
        HRESULT,
        'UnregisterMouseButton',
        (['in'], c_int, 'button'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744026)],
        HRESULT,
        'RegisterMouseWheel',
        (['in'], c_longlong, 'callback'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744027)],
        HRESULT,
        'UnregisterMouseWheel',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744028)],
        HRESULT,
        'RegisterMouseMove',
        (['in'], c_longlong, 'callback'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744029)],
        HRESULT,
        'UnregisterMouseMove',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744030)],
        HRESULT,
        'RegisterMouseDrag',
        (['in'], c_longlong, 'callback'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744031)],
        HRESULT,
        'UnregisterMouseDrag',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744032)],
        HRESULT,
        'Inject',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'dll_path'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'bypassGuard'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744033)],
        HRESULT,
        'InjectFromUrl',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'url'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'bypassGuard'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744034)],
        HRESULT,
        'InjectFromBuffer',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'bufferAddr'),
        (['in'], c_int, 'bufferSize'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'bypassGuard'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744035)],
        HRESULT,
        'JsonCreateObject',
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744036)],
        HRESULT,
        'JsonCreateArray',
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744037)],
        HRESULT,
        'JsonParse',
        (['in'], BSTR, 'str'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744038)],
        HRESULT,
        'JsonFree',
        (['in'], c_longlong, 'obj'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744039)],
        HRESULT,
        'JsonStringify',
        (['in'], c_longlong, 'obj'),
        (['in'], c_int, 'indent'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744040)],
        HRESULT,
        'JsonGetSize',
        (['in'], c_longlong, 'obj'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744041)],
        HRESULT,
        'JsonSetValue',
        (['in'], c_longlong, 'obj'),
        (['in'], BSTR, 'key'),
        (['in'], c_longlong, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744042)],
        HRESULT,
        'JsonArrayAppend',
        (['in'], c_longlong, 'arr'),
        (['in'], c_longlong, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744043)],
        HRESULT,
        'JsonClear',
        (['in'], c_longlong, 'obj'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744044)],
        HRESULT,
        'JsonDeleteKey',
        (['in'], c_longlong, 'obj'),
        (['in'], BSTR, 'key'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744045)],
        HRESULT,
        'JsonGetValue',
        (['in'], c_longlong, 'obj'),
        (['in'], BSTR, 'key'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744046)],
        HRESULT,
        'JsonGetArrayItem',
        (['in'], c_longlong, 'arr'),
        (['in'], c_int, 'index'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744047)],
        HRESULT,
        'JsonGetString',
        (['in'], c_longlong, 'obj'),
        (['in'], BSTR, 'key'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744048)],
        HRESULT,
        'JsonGetNumber',
        (['in'], c_longlong, 'obj'),
        (['in'], BSTR, 'key'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744049)],
        HRESULT,
        'JsonGetBool',
        (['in'], c_longlong, 'obj'),
        (['in'], BSTR, 'key'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744050)],
        HRESULT,
        'JsonSetString',
        (['in'], c_longlong, 'obj'),
        (['in'], BSTR, 'key'),
        (['in'], BSTR, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744051)],
        HRESULT,
        'JsonSetNumber',
        (['in'], c_longlong, 'obj'),
        (['in'], BSTR, 'key'),
        (['in'], c_double, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744052)],
        HRESULT,
        'JsonSetBool',
        (['in'], c_longlong, 'obj'),
        (['in'], BSTR, 'key'),
        (['in'], c_int, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744053)],
        HRESULT,
        'ParseMatchImageJson',
        (['in'], BSTR, 'str'),
        (['out'], POINTER(VARIANT), 'matchState'),
        (['out'], POINTER(VARIANT), 'x'),
        (['out'], POINTER(VARIANT), 'y'),
        (['out'], POINTER(VARIANT), 'width'),
        (['out'], POINTER(VARIANT), 'height'),
        (['out'], POINTER(VARIANT), 'matchVal'),
        (['out'], POINTER(VARIANT), 'angle'),
        (['out'], POINTER(VARIANT), 'index'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744054)],
        HRESULT,
        'GetMatchImageAllCount',
        (['in'], BSTR, 'str'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744055)],
        HRESULT,
        'ParseMatchImageAllJson',
        (['in'], BSTR, 'str'),
        (['in'], c_int, 'parseIndex'),
        (['out'], POINTER(VARIANT), 'matchState'),
        (['out'], POINTER(VARIANT), 'x'),
        (['out'], POINTER(VARIANT), 'y'),
        (['out'], POINTER(VARIANT), 'width'),
        (['out'], POINTER(VARIANT), 'height'),
        (['out'], POINTER(VARIANT), 'matchVal'),
        (['out'], POINTER(VARIANT), 'angle'),
        (['out'], POINTER(VARIANT), 'index'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744056)],
        HRESULT,
        'GetResultCount',
        (['in'], BSTR, 'resultStr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744057)],
        HRESULT,
        'KeyDown',
        (['in'], c_int, 'vk_code'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744058)],
        HRESULT,
        'KeyUp',
        (['in'], c_int, 'vk_code'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744059)],
        HRESULT,
        'KeyPress',
        (['in'], c_int, 'vk_code'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744060)],
        HRESULT,
        'LeftDown',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744061)],
        HRESULT,
        'LeftUp',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744062)],
        HRESULT,
        'MoveTo',
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744063)],
        HRESULT,
        'MoveToWithoutSimulator',
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744064)],
        HRESULT,
        'RightClick',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744065)],
        HRESULT,
        'RightDoubleClick',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744066)],
        HRESULT,
        'RightDown',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744067)],
        HRESULT,
        'RightUp',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744068)],
        HRESULT,
        'GetCursorShape',
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744069)],
        HRESULT,
        'GetCursorImage',
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744070)],
        HRESULT,
        'KeyPressStr',
        (['in'], BSTR, 'keyStr'),
        (['in'], c_int, 'delay'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744071)],
        HRESULT,
        'SendString',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'str'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744072)],
        HRESULT,
        'SendStringEx',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'len'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744073)],
        HRESULT,
        'KeyPressChar',
        (['in'], BSTR, 'keyStr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744074)],
        HRESULT,
        'KeyDownChar',
        (['in'], BSTR, 'keyStr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744075)],
        HRESULT,
        'KeyUpChar',
        (['in'], BSTR, 'keyStr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744076)],
        HRESULT,
        'MoveR',
        (['in'], c_int, 'rx'),
        (['in'], c_int, 'ry'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744077)],
        HRESULT,
        'MiddleClick',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744078)],
        HRESULT,
        'MiddleDoubleClick',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744079)],
        HRESULT,
        'MoveToEx',
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['in'], c_int, 'w'),
        (['in'], c_int, 'h'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744080)],
        HRESULT,
        'GetCursorPos',
        (['out'], POINTER(VARIANT), 'x'),
        (['out'], POINTER(VARIANT), 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744081)],
        HRESULT,
        'MiddleUp',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744082)],
        HRESULT,
        'MiddleDown',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744083)],
        HRESULT,
        'LeftClick',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744084)],
        HRESULT,
        'LeftDoubleClick',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744085)],
        HRESULT,
        'WheelUp',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744086)],
        HRESULT,
        'WheelDown',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744087)],
        HRESULT,
        'WaitKey',
        (['in'], c_int, 'vk_code'),
        (['in'], c_int, 'time_out'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744088)],
        HRESULT,
        'EnableMouseAccuracy',
        (['in'], c_int, 'enable'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744089)],
        HRESULT,
        'GenerateMouseTrajectory',
        (['in'], c_int, 'startX'),
        (['in'], c_int, 'startY'),
        (['in'], c_int, 'endX'),
        (['in'], c_int, 'endY'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744090)],
        HRESULT,
        'GenerateInvoluteMouseTrajectory',
        (['in'], c_int, 'startX'),
        (['in'], c_int, 'startY'),
        (['in'], c_int, 'radius'),
        (['in'], c_int, 'stepDistance'),
        (['in'], c_double, 'curvature'),
        (['in'], c_double, 'noiseAmplitude'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744091)],
        HRESULT,
        'LogShutdown',
        (['in'], c_longlong, 'loggerHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744092)],
        HRESULT,
        'LogSetFilePath',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], BSTR, 'logFilePath'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744093)],
        HRESULT,
        'LogSetPattern',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], BSTR, 'logPattern'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744094)],
        HRESULT,
        'LogSetMaxFileSize',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], c_int, 'maxFileSizeMb'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744095)],
        HRESULT,
        'LogSetMaxFiles',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], c_int, 'maxFiles'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744096)],
        HRESULT,
        'LogSetLevel',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], c_int, 'level'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744097)],
        HRESULT,
        'LogGetLevel',
        (['in'], c_longlong, 'loggerHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744098)],
        HRESULT,
        'LogSetTarget',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], c_int, 'targetFlags'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744099)],
        HRESULT,
        'LogSetAsync',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], c_int, 'enableAsync'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744100)],
        HRESULT,
        'LogSetColorMode',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], c_int, 'colorMode'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744101)],
        HRESULT,
        'LogSetLevelColor',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], c_int, 'level'),
        (['in'], c_int, 'color'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744102)],
        HRESULT,
        'LogResetLevelColors',
        (['in'], c_longlong, 'loggerHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744103)],
        HRESULT,
        'LogSetFlushInterval',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], c_int, 'flushIntervalSeconds'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744104)],
        HRESULT,
        'LogTrace',
        (['in'], BSTR, 'message'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744105)],
        HRESULT,
        'LogDebug',
        (['in'], BSTR, 'message'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744106)],
        HRESULT,
        'LogInfo',
        (['in'], BSTR, 'message'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744107)],
        HRESULT,
        'LogWarn',
        (['in'], BSTR, 'message'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744108)],
        HRESULT,
        'LogError',
        (['in'], BSTR, 'message'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744109)],
        HRESULT,
        'LogCritical',
        (['in'], BSTR, 'message'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744110)],
        HRESULT,
        'LogFlush',
        (['in'], c_longlong, 'loggerHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744111)],
        HRESULT,
        'LogCreateInstance',
        (['in'], BSTR, 'instanceName'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744112)],
        HRESULT,
        'LogDestroyInstance',
        (['in'], c_longlong, 'loggerHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744113)],
        HRESULT,
        'LogSetBaseDirectory',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], BSTR, 'baseDirectory'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744114)],
        HRESULT,
        'LogSetDirMode',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], c_int, 'dirMode'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744115)],
        HRESULT,
        'LogSetModuleName',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], BSTR, 'moduleName'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744116)],
        HRESULT,
        'LogSetFileNamePattern',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], BSTR, 'fileNamePattern'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744117)],
        HRESULT,
        'LogSetRotationMode',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], c_int, 'rotationMode'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744118)],
        HRESULT,
        'LogSetAppendMode',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], c_int, 'enableAppend'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744119)],
        HRESULT,
        'LogTraceEx',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], BSTR, 'message'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744120)],
        HRESULT,
        'LogDebugEx',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], BSTR, 'message'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744121)],
        HRESULT,
        'LogInfoEx',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], BSTR, 'message'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744122)],
        HRESULT,
        'LogWarnEx',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], BSTR, 'message'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744123)],
        HRESULT,
        'LogErrorEx',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], BSTR, 'message'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744124)],
        HRESULT,
        'LogCriticalEx',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], BSTR, 'message'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744125)],
        HRESULT,
        'LogRotateFile',
        (['in'], c_longlong, 'loggerHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744126)],
        HRESULT,
        'LogCleanupOldFiles',
        (['in'], c_longlong, 'loggerHandle'),
        (['in'], c_int, 'keepCount'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744127)],
        HRESULT,
        'LogGetCurrentFilePath',
        (['in'], c_longlong, 'loggerHandle'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744128)],
        HRESULT,
        'LogGetCurrentFileSize',
        (['in'], c_longlong, 'loggerHandle'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744129)],
        HRESULT,
        'LogGetTotalFilesCount',
        (['in'], c_longlong, 'loggerHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744130)],
        HRESULT,
        'CloseConsole',
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744131)],
        HRESULT,
        'OpenConsole',
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744132)],
        HRESULT,
        'DoubleToData',
        (['in'], c_double, 'double_value'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744133)],
        HRESULT,
        'FloatToData',
        (['in'], c_float, 'float_value'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744134)],
        HRESULT,
        'StringToData',
        (['in'], BSTR, 'string_value'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744135)],
        HRESULT,
        'Int64ToInt32',
        (['in'], c_longlong, 'v'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744136)],
        HRESULT,
        'Int32ToInt64',
        (['in'], c_int, 'v'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744137)],
        HRESULT,
        'FindData',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr_range'),
        (['in'], BSTR, 'data'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744138)],
        HRESULT,
        'FindDataEx',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr_range'),
        (['in'], BSTR, 'data'),
        (['in'], c_int, 'step'),
        (['in'], c_int, 'multi_thread'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744139)],
        HRESULT,
        'FindDouble',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr_range'),
        (['in'], c_double, 'double_value_min'),
        (['in'], c_double, 'double_value_max'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744140)],
        HRESULT,
        'FindDoubleEx',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr_range'),
        (['in'], c_double, 'double_value_min'),
        (['in'], c_double, 'double_value_max'),
        (['in'], c_int, 'step'),
        (['in'], c_int, 'multi_thread'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744141)],
        HRESULT,
        'FindFloat',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr_range'),
        (['in'], c_float, 'float_value_min'),
        (['in'], c_float, 'float_value_max'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744142)],
        HRESULT,
        'FindFloatEx',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr_range'),
        (['in'], c_float, 'float_value_min'),
        (['in'], c_float, 'float_value_max'),
        (['in'], c_int, 'step'),
        (['in'], c_int, 'multi_thread'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744143)],
        HRESULT,
        'FindInt',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr_range'),
        (['in'], c_longlong, 'int_value_min'),
        (['in'], c_longlong, 'int_value_max'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744144)],
        HRESULT,
        'FindIntEx',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr_range'),
        (['in'], c_longlong, 'int_value_min'),
        (['in'], c_longlong, 'int_value_max'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'step'),
        (['in'], c_int, 'multi_thread'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744145)],
        HRESULT,
        'FindString',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr_range'),
        (['in'], BSTR, 'string_value'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744146)],
        HRESULT,
        'FindStringEx',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr_range'),
        (['in'], BSTR, 'string_value'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'step'),
        (['in'], c_int, 'multi_thread'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744147)],
        HRESULT,
        'ReadData',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744148)],
        HRESULT,
        'ReadDataToBin',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744149)],
        HRESULT,
        'ReadDataAddr',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744150)],
        HRESULT,
        'ReadDataAddrToBin',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744151)],
        HRESULT,
        'ReadDouble',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744152)],
        HRESULT,
        'ReadDoubleAddr',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744153)],
        HRESULT,
        'ReadFloat',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['out', 'retval'], POINTER(c_float), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744154)],
        HRESULT,
        'ReadFloatAddr',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['out', 'retval'], POINTER(c_float), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744155)],
        HRESULT,
        'ReadInt',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744156)],
        HRESULT,
        'ReadIntAddr',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744157)],
        HRESULT,
        'ReadString',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744158)],
        HRESULT,
        'ReadStringAddr',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744159)],
        HRESULT,
        'WriteData',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['in'], BSTR, 'data'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744160)],
        HRESULT,
        'WriteDataFromBin',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['in'], c_longlong, 'data'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744161)],
        HRESULT,
        'WriteDataAddr',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], BSTR, 'data'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744162)],
        HRESULT,
        'WriteDataAddrFromBin',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_longlong, 'data'),
        (['in'], c_int, 'len'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744163)],
        HRESULT,
        'WriteDouble',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['in'], c_double, 'double_value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744164)],
        HRESULT,
        'WriteDoubleAddr',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_double, 'double_value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744165)],
        HRESULT,
        'WriteFloat',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['in'], c_float, 'float_value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744166)],
        HRESULT,
        'WriteFloatAddr',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_float, 'float_value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744167)],
        HRESULT,
        'WriteInt',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['in'], c_int, 'type'),
        (['in'], c_longlong, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744168)],
        HRESULT,
        'WriteIntAddr',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'type'),
        (['in'], c_longlong, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744169)],
        HRESULT,
        'WriteString',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'addr'),
        (['in'], c_int, 'type'),
        (['in'], BSTR, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744170)],
        HRESULT,
        'WriteStringAddr',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'type'),
        (['in'], BSTR, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744171)],
        HRESULT,
        'SetMemoryHwndAsProcessId',
        (['in'], c_int, 'enable'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744172)],
        HRESULT,
        'FreeProcessMemory',
        (['in'], c_longlong, 'hwnd'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744173)],
        HRESULT,
        'GetModuleBaseAddr',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'module_name'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744174)],
        HRESULT,
        'GetModuleSize',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'module_name'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744175)],
        HRESULT,
        'GetRemoteApiAddress',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'module_name'),
        (['in'], BSTR, 'fun_name'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744176)],
        HRESULT,
        'VirtualAllocEx',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'size'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744177)],
        HRESULT,
        'VirtualFreeEx',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744178)],
        HRESULT,
        'VirtualProtectEx',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_int, 'size'),
        (['in'], c_int, 'newProtect'),
        (['out'], POINTER(VARIANT), 'oldProtect'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744179)],
        HRESULT,
        'VirtualQueryEx',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'addr'),
        (['in'], c_longlong, 'pmbi'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744180)],
        HRESULT,
        'CloseHandle',
        (['in'], c_longlong, 'handle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744181)],
        HRESULT,
        'CreateRemoteThread',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'lpStartAddress'),
        (['in'], c_longlong, 'lpParameter'),
        (['in'], c_int, 'dwCreationFlags'),
        (['out'], POINTER(VARIANT), 'lpThreadId'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744182)],
        HRESULT,
        'HookRemoteApi',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'targetAddr'),
        (['in'], c_longlong, 'size'),
        (['in'], c_longlong, 'hook_proc'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744183)],
        HRESULT,
        'UnhookRemoteApi',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_longlong, 'targetAddr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744184)],
        HRESULT,
        'HttpDownloadFile',
        (['in'], BSTR, 'url'),
        (['in'], BSTR, 'save_path'),
        (['in'], c_longlong, 'callback'),
        (['in'], c_longlong, 'user_data'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744185)],
        HRESULT,
        'HttpDownloadFileEx',
        (['in'], BSTR, 'url'),
        (['in'], BSTR, 'save_path'),
        (['in'], c_longlong, 'callback'),
        (['in'], c_longlong, 'user_data'),
        (['in'], c_int, 'max_retries'),
        (['in'], c_int, 'connect_timeout_sec'),
        (['in'], c_int, 'read_timeout_sec'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744186)],
        HRESULT,
        'HttpGet',
        (['in'], BSTR, 'url'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744187)],
        HRESULT,
        'HttpPost',
        (['in'], BSTR, 'url'),
        (['in'], BSTR, 'body'),
        (['in'], BSTR, 'content_type'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744188)],
        HRESULT,
        'HttpRequestEx',
        (['in'], BSTR, 'method'),
        (['in'], BSTR, 'url'),
        (['in'], BSTR, 'headers'),
        (['in'], BSTR, 'body'),
        (['in'], BSTR, 'content_type'),
        (['out'], POINTER(VARIANT), 'status_code'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744189)],
        HRESULT,
        'TcpClientCreate',
        (['in'], c_longlong, 'callback'),
        (['in'], c_longlong, 'user_data'),
        (['in'], c_int, 'enable_packet_protocol'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744190)],
        HRESULT,
        'TcpClientConnect',
        (['in'], c_longlong, 'client_handle'),
        (['in'], BSTR, 'host'),
        (['in'], c_int, 'port'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744191)],
        HRESULT,
        'TcpClientSend',
        (['in'], c_longlong, 'client_handle'),
        (['in'], c_longlong, 'data'),
        (['in'], c_int, 'data_len'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744192)],
        HRESULT,
        'TcpClientDisconnect',
        (['in'], c_longlong, 'client_handle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744193)],
        HRESULT,
        'TcpClientDestroy',
        (['in'], c_longlong, 'client_handle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744194)],
        HRESULT,
        'TcpServerCreate',
        (['in'], BSTR, 'bind_addr'),
        (['in'], c_int, 'port'),
        (['in'], c_longlong, 'callback'),
        (['in'], c_longlong, 'user_data'),
        (['in'], c_int, 'enable_packet_protocol'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744195)],
        HRESULT,
        'TcpServerSend',
        (['in'], c_longlong, 'server_handle'),
        (['in'], c_longlong, 'conn_id'),
        (['in'], c_longlong, 'data'),
        (['in'], c_int, 'data_len'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744196)],
        HRESULT,
        'TcpServerDisconnect',
        (['in'], c_longlong, 'server_handle'),
        (['in'], c_longlong, 'conn_id'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744197)],
        HRESULT,
        'TcpServerStop',
        (['in'], c_longlong, 'server_handle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744198)],
        HRESULT,
        'TcpServerDestroy',
        (['in'], c_longlong, 'server_handle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744199)],
        HRESULT,
        'TcpServerGetClientAddress',
        (['in'], c_longlong, 'server_handle'),
        (['in'], c_longlong, 'conn_id'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744200)],
        HRESULT,
        'TcpServerGetAllConnectionIds',
        (['in'], c_longlong, 'server_handle'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744201)],
        HRESULT,
        'Ocr',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744202)],
        HRESULT,
        'OcrFromPtr',
        (['in'], c_longlong, 'ptr'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744203)],
        HRESULT,
        'OcrDetails',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744204)],
        HRESULT,
        'OcrFromPtrDetails',
        (['in'], c_longlong, 'ptr'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744205)],
        HRESULT,
        'OcrFromBmpData',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'size'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744206)],
        HRESULT,
        'OcrFromBmpDataDetails',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'size'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744207)],
        HRESULT,
        'OcrV5',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744208)],
        HRESULT,
        'OcrV5Details',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744209)],
        HRESULT,
        'OcrV5FromPtr',
        (['in'], c_longlong, 'ptr'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744210)],
        HRESULT,
        'OcrV5FromPtrDetails',
        (['in'], c_longlong, 'ptr'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744211)],
        HRESULT,
        'OcrFromDict',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'dict_name'),
        (['in'], c_double, 'matchVal'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744212)],
        HRESULT,
        'OcrFromDictDetails',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'dict_name'),
        (['in'], c_double, 'matchVal'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744213)],
        HRESULT,
        'OcrFromDictPtr',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'dict_name'),
        (['in'], c_double, 'matchVal'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744214)],
        HRESULT,
        'OcrFromDictPtrDetails',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'dict_name'),
        (['in'], c_double, 'matchVal'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744215)],
        HRESULT,
        'SetOcrConfigByKey',
        (['in'], BSTR, 'key'),
        (['in'], BSTR, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744216)],
        HRESULT,
        'SetOcrConfig',
        (['in'], BSTR, 'configStr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744217)],
        HRESULT,
        'GetOcrConfig',
        (['in'], BSTR, 'configKey'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744218)],
        HRESULT,
        'FindStr',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'str'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'dict'),
        (['in'], c_double, 'matchVal'),
        (['out'], POINTER(VARIANT), 'outX'),
        (['out'], POINTER(VARIANT), 'outY'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744219)],
        HRESULT,
        'FindStrDetail',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'str'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'dict'),
        (['in'], c_double, 'matchVal'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744220)],
        HRESULT,
        'FindStrAll',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'str'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'dict'),
        (['in'], c_double, 'matchVal'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744221)],
        HRESULT,
        'FindStrFromPtr',
        (['in'], c_longlong, 'source'),
        (['in'], BSTR, 'str'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'dict'),
        (['in'], c_double, 'matchVal'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744222)],
        HRESULT,
        'FindStrFromPtrAll',
        (['in'], c_longlong, 'source'),
        (['in'], BSTR, 'str'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'dict'),
        (['in'], c_double, 'matchVal'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744223)],
        HRESULT,
        'FastNumberOcr',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'numbers'),
        (['in'], BSTR, 'colorJson'),
        (['in'], c_double, 'matchVal'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744224)],
        HRESULT,
        'FastNumberOcrFromPtr',
        (['in'], c_longlong, 'source'),
        (['in'], BSTR, 'numbers'),
        (['in'], BSTR, 'colorJson'),
        (['in'], c_double, 'matchVal'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744225)],
        HRESULT,
        'ImportTxtDict',
        (['in'], BSTR, 'dictName'),
        (['in'], BSTR, 'dictPath'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744226)],
        HRESULT,
        'ExportTxtDict',
        (['in'], BSTR, 'dictName'),
        (['in'], BSTR, 'dictPath'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744227)],
        HRESULT,
        'Capture',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'file'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744228)],
        HRESULT,
        'GetScreenDataBmp',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['out'], POINTER(VARIANT), 'data'),
        (['out'], POINTER(VARIANT), 'dataLen'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744229)],
        HRESULT,
        'GetScreenData',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['out'], POINTER(VARIANT), 'data'),
        (['out'], POINTER(VARIANT), 'dataLen'),
        (['out'], POINTER(VARIANT), 'stride'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744230)],
        HRESULT,
        'GetScreenDataPtr',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744231)],
        HRESULT,
        'CaptureGif',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'file'),
        (['in'], c_int, 'delay'),
        (['in'], c_int, 'time'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744232)],
        HRESULT,
        'LockDisplay',
        (['in'], c_int, 'enable'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744233)],
        HRESULT,
        'SetSnapCacheTime',
        (['in'], c_int, 'cacheTime'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744234)],
        HRESULT,
        'GetImageData',
        (['in'], c_longlong, 'imgPtr'),
        (['out'], POINTER(VARIANT), 'data'),
        (['out'], POINTER(VARIANT), 'size'),
        (['out'], POINTER(VARIANT), 'stride'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744235)],
        HRESULT,
        'MatchImageFromPath',
        (['in'], BSTR, 'source'),
        (['in'], BSTR, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'type'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744236)],
        HRESULT,
        'MatchImageFromPathAll',
        (['in'], BSTR, 'source'),
        (['in'], BSTR, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'type'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744237)],
        HRESULT,
        'MatchImagePtrFromPath',
        (['in'], c_longlong, 'source'),
        (['in'], BSTR, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'type'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744238)],
        HRESULT,
        'MatchImagePtrFromPathAll',
        (['in'], c_longlong, 'source'),
        (['in'], BSTR, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'type'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744239)],
        HRESULT,
        'GetColor',
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744240)],
        HRESULT,
        'GetColorPtr',
        (['in'], c_longlong, 'source'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744241)],
        HRESULT,
        'CopyImage',
        (['in'], c_longlong, 'sourcePtr'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744242)],
        HRESULT,
        'FreeImageAll',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744243)],
        HRESULT,
        'FreeImagePath',
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744244)],
        HRESULT,
        'LoadImage',
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744245)],
        HRESULT,
        'LoadImageFromBmpData',
        (['in'], c_longlong, 'data'),
        (['in'], c_int, 'dataSize'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744246)],
        HRESULT,
        'LoadImageFromRGBData',
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['in'], c_longlong, 'scan0'),
        (['in'], c_int, 'stride'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744247)],
        HRESULT,
        'FreeImagePtr',
        (['in'], c_longlong, 'screenPtr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744248)],
        HRESULT,
        'MatchWindowsFromPtr',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], c_longlong, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'type'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744249)],
        HRESULT,
        'MatchImageFromPtr',
        (['in'], c_longlong, 'source'),
        (['in'], c_longlong, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'type'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744250)],
        HRESULT,
        'MatchImageFromPtrAll',
        (['in'], c_longlong, 'source'),
        (['in'], c_longlong, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'type'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744251)],
        HRESULT,
        'MatchWindowsFromPtrAll',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], c_longlong, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'type'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744252)],
        HRESULT,
        'MatchWindowsFromPath',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'type'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744253)],
        HRESULT,
        'MatchWindowsFromPathAll',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'type'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744254)],
        HRESULT,
        'MatchWindowsThresholdFromPtr',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorJson'),
        (['in'], c_longlong, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744255)],
        HRESULT,
        'MatchWindowsThresholdFromPtrAll',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorJson'),
        (['in'], c_longlong, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744256)],
        HRESULT,
        'MatchWindowsThresholdFromPath',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744257)],
        HRESULT,
        'MatchWindowsThresholdFromPathAll',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744258)],
        HRESULT,
        'ShowMatchWindow',
        (['in'], c_int, 'flag'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744259)],
        HRESULT,
        'CalculateSSIM',
        (['in'], c_longlong, 'image1'),
        (['in'], c_longlong, 'image2'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744260)],
        HRESULT,
        'CalculateHistograms',
        (['in'], c_longlong, 'image1'),
        (['in'], c_longlong, 'image2'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744261)],
        HRESULT,
        'CalculateMSE',
        (['in'], c_longlong, 'image1'),
        (['in'], c_longlong, 'image2'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744262)],
        HRESULT,
        'SaveImageFromPtr',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744263)],
        HRESULT,
        'ReSize',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744264)],
        HRESULT,
        'FindColor',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'color1'),
        (['in'], BSTR, 'color2'),
        (['in'], c_int, 'dir'),
        (['out'], POINTER(VARIANT), 'x'),
        (['out'], POINTER(VARIANT), 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744265)],
        HRESULT,
        'FindColorList',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'color1'),
        (['in'], BSTR, 'color2'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744266)],
        HRESULT,
        'FindColorEx',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorJson'),
        (['in'], c_int, 'dir'),
        (['out'], POINTER(VARIANT), 'x'),
        (['out'], POINTER(VARIANT), 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744267)],
        HRESULT,
        'FindColorListEx',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorJson'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744268)],
        HRESULT,
        'FindMultiColor',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'pointJson'),
        (['in'], c_double, 'sim'),
        (['in'], c_int, 'dir'),
        (['out'], POINTER(VARIANT), 'x'),
        (['out'], POINTER(VARIANT), 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744269)],
        HRESULT,
        'FindMultiColorList',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'pointJson'),
        (['in'], c_double, 'sim'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744270)],
        HRESULT,
        'FindMultiColorFromPtr',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'pointJson'),
        (['in'], c_double, 'sim'),
        (['in'], c_int, 'dir'),
        (['out'], POINTER(VARIANT), 'x'),
        (['out'], POINTER(VARIANT), 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744271)],
        HRESULT,
        'FindMultiColorListFromPtr',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'pointJson'),
        (['in'], c_double, 'sim'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744272)],
        HRESULT,
        'GetImageSize',
        (['in'], c_longlong, 'ptr'),
        (['out'], POINTER(VARIANT), 'width'),
        (['out'], POINTER(VARIANT), 'height'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744273)],
        HRESULT,
        'FindColorBlock',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorList'),
        (['in'], c_int, 'count'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['out'], POINTER(VARIANT), 'x'),
        (['out'], POINTER(VARIANT), 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744274)],
        HRESULT,
        'FindColorBlockPtr',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'colorList'),
        (['in'], c_int, 'count'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['out'], POINTER(VARIANT), 'x'),
        (['out'], POINTER(VARIANT), 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744275)],
        HRESULT,
        'FindColorBlockList',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorList'),
        (['in'], c_int, 'count'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744276)],
        HRESULT,
        'FindColorBlockListPtr',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'colorList'),
        (['in'], c_int, 'count'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744277)],
        HRESULT,
        'FindColorBlockEx',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorList'),
        (['in'], c_int, 'count'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['in'], c_int, 'dir'),
        (['out'], POINTER(VARIANT), 'x'),
        (['out'], POINTER(VARIANT), 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744278)],
        HRESULT,
        'FindColorBlockPtrEx',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'colorList'),
        (['in'], c_int, 'count'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['in'], c_int, 'dir'),
        (['out'], POINTER(VARIANT), 'x'),
        (['out'], POINTER(VARIANT), 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744279)],
        HRESULT,
        'FindColorBlockListEx',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorList'),
        (['in'], c_int, 'count'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'dir'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744280)],
        HRESULT,
        'FindColorBlockListPtrEx',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'colorList'),
        (['in'], c_int, 'count'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['in'], c_int, 'type'),
        (['in'], c_int, 'dir'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744281)],
        HRESULT,
        'GetColorNum',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorList'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744282)],
        HRESULT,
        'GetColorNumPtr',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'colorList'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744283)],
        HRESULT,
        'Cropped',
        (['in'], c_longlong, 'image'),
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744284)],
        HRESULT,
        'GetThresholdImageFromMultiColorPtr',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'colorJson'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744285)],
        HRESULT,
        'GetThresholdImageFromMultiColor',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'colorJson'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744286)],
        HRESULT,
        'IsSameImage',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_longlong, 'ptr2'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744287)],
        HRESULT,
        'ShowImage',
        (['in'], c_longlong, 'ptr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744288)],
        HRESULT,
        'ShowImageFromFile',
        (['in'], BSTR, 'file'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744289)],
        HRESULT,
        'SetColorsToNewColor',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'colorJson'),
        (['in'], BSTR, 'color'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744290)],
        HRESULT,
        'RemoveOtherColors',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'colorJson'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744291)],
        HRESULT,
        'DrawRectangle',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], c_int, 'thickness'),
        (['in'], BSTR, 'color'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744292)],
        HRESULT,
        'DrawCircle',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['in'], c_int, 'radius'),
        (['in'], c_int, 'thickness'),
        (['in'], BSTR, 'color'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744293)],
        HRESULT,
        'DrawFillPoly',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'pointJson'),
        (['in'], BSTR, 'color'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744294)],
        HRESULT,
        'DecodeQRCode',
        (['in'], c_longlong, 'ptr'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744295)],
        HRESULT,
        'CreateQRCode',
        (['in'], BSTR, 'str'),
        (['in'], c_int, 'pixelsPerModule'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744296)],
        HRESULT,
        'CreateQRCodeEx',
        (['in'], BSTR, 'str'),
        (['in'], c_int, 'pixelsPerModule'),
        (['in'], c_int, 'version'),
        (['in'], c_int, 'correction_level'),
        (['in'], c_int, 'mode'),
        (['in'], c_int, 'structure_number'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744297)],
        HRESULT,
        'MatchAnimationFromPtr',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], c_longlong, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'type'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['in'], c_int, 'delay'),
        (['in'], c_int, 'time'),
        (['in'], c_int, 'threadCount'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744298)],
        HRESULT,
        'MatchAnimationFromPath',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'templ'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'type'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['in'], c_int, 'delay'),
        (['in'], c_int, 'time'),
        (['in'], c_int, 'threadCount'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744299)],
        HRESULT,
        'RemoveImageDiff',
        (['in'], c_longlong, 'image1'),
        (['in'], c_longlong, 'image2'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744300)],
        HRESULT,
        'GetImageBmpData',
        (['in'], c_longlong, 'imgPtr'),
        (['out'], POINTER(VARIANT), 'data'),
        (['out'], POINTER(VARIANT), 'size'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744301)],
        HRESULT,
        'FreeImageData',
        (['in'], c_longlong, 'screenPtr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744302)],
        HRESULT,
        'ScalePixels',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'pixelsPerModule'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744303)],
        HRESULT,
        'CreateImage',
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['in'], BSTR, 'color'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744304)],
        HRESULT,
        'SetPixel',
        (['in'], c_longlong, 'image'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['in'], BSTR, 'color'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744305)],
        HRESULT,
        'SetPixelList',
        (['in'], c_longlong, 'image'),
        (['in'], BSTR, 'points'),
        (['in'], BSTR, 'color'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744306)],
        HRESULT,
        'ConcatImage',
        (['in'], c_longlong, 'image1'),
        (['in'], c_longlong, 'image2'),
        (['in'], c_int, 'gap'),
        (['in'], BSTR, 'color'),
        (['in'], c_int, 'dir'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744307)],
        HRESULT,
        'CoverImage',
        (['in'], c_longlong, 'image1'),
        (['in'], c_longlong, 'image2'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['in'], c_double, 'alpha'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744308)],
        HRESULT,
        'RotateImage',
        (['in'], c_longlong, 'image'),
        (['in'], c_double, 'angle'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744309)],
        HRESULT,
        'ImageToBase64',
        (['in'], c_longlong, 'image'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744310)],
        HRESULT,
        'Base64ToImage',
        (['in'], BSTR, 'base64'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744311)],
        HRESULT,
        'Hex2ARGB',
        (['in'], BSTR, 'hex'),
        (['out'], POINTER(VARIANT), 'a'),
        (['out'], POINTER(VARIANT), 'r'),
        (['out'], POINTER(VARIANT), 'g'),
        (['out'], POINTER(VARIANT), 'b'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744312)],
        HRESULT,
        'Hex2RGB',
        (['in'], BSTR, 'hex'),
        (['out'], POINTER(VARIANT), 'r'),
        (['out'], POINTER(VARIANT), 'g'),
        (['out'], POINTER(VARIANT), 'b'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744313)],
        HRESULT,
        'ARGB2Hex',
        (['in'], c_int, 'a'),
        (['in'], c_int, 'r'),
        (['in'], c_int, 'g'),
        (['in'], c_int, 'b'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744314)],
        HRESULT,
        'RGB2Hex',
        (['in'], c_int, 'r'),
        (['in'], c_int, 'g'),
        (['in'], c_int, 'b'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744315)],
        HRESULT,
        'CmpColor',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], BSTR, 'colorStart'),
        (['in'], BSTR, 'colorEnd'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744316)],
        HRESULT,
        'CmpColorPtr',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['in'], BSTR, 'colorStart'),
        (['in'], BSTR, 'colorEnd'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744317)],
        HRESULT,
        'CmpColorHex',
        (['in'], BSTR, 'hex'),
        (['in'], BSTR, 'colorStart'),
        (['in'], BSTR, 'colorEnd'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744318)],
        HRESULT,
        'CmpMultiColor',
        (['in'], BSTR, 'pointJson'),
        (['in'], c_double, 'sim'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744319)],
        HRESULT,
        'CmpMultiColorPtr',
        (['in'], c_longlong, 'image'),
        (['in'], BSTR, 'pointJson'),
        (['in'], c_double, 'sim'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744320)],
        HRESULT,
        'GetConnectedComponents',
        (['in'], c_longlong, 'ptr'),
        (['in'], BSTR, 'points'),
        (['in'], c_int, 'tolerance'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744321)],
        HRESULT,
        'DetectPointerDirection',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744322)],
        HRESULT,
        'DetectPointerDirectionByFeatures',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_longlong, 'templatePtr'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['in'], c_longlong, 'useTemplate'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744323)],
        HRESULT,
        'FastMatch',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_longlong, 'templatePtr'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'type'),
        (['in'], c_double, 'angle'),
        (['in'], c_double, 'scale'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744324)],
        HRESULT,
        'GetROIRegion',
        (['in'], c_longlong, 'ptr'),
        (['out'], POINTER(VARIANT), 'x1'),
        (['out'], POINTER(VARIANT), 'y1'),
        (['out'], POINTER(VARIANT), 'x2'),
        (['out'], POINTER(VARIANT), 'y2'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744325)],
        HRESULT,
        'FastROI',
        (['in'], c_longlong, 'ptr'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744326)],
        HRESULT,
        'Hex2HSV',
        (['in'], BSTR, 'hex'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744327)],
        HRESULT,
        'RGB2HSV',
        (['in'], c_int, 'r'),
        (['in'], c_int, 'g'),
        (['in'], c_int, 'b'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744328)],
        HRESULT,
        'GetForegroundPoints',
        (['in'], c_longlong, 'ptr'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744329)],
        HRESULT,
        'ConvertColor',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744330)],
        HRESULT,
        'Threshold',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_double, 'thresh'),
        (['in'], c_double, 'maxVal'),
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744331)],
        HRESULT,
        'RemoveIslands',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'minArea'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744332)],
        HRESULT,
        'MorphGradient',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'kernelSize'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744333)],
        HRESULT,
        'ImageStitchFromPath',
        (['in'], BSTR, 'path'),
        (['out'], POINTER(VARIANT), 'trajectory'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744334)],
        HRESULT,
        'ImageStitchCreate',
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744335)],
        HRESULT,
        'ImageStitchFree',
        (['in'], c_longlong, 'imageStitch'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744336)],
        HRESULT,
        'ImageStitchAppend',
        (['in'], c_longlong, 'imageStitch'),
        (['in'], c_longlong, 'image'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744337)],
        HRESULT,
        'ImageStitchGetResult',
        (['in'], c_longlong, 'imageStitch'),
        (['out'], POINTER(VARIANT), 'trajectory'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744338)],
        HRESULT,
        'MorphTophat',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'kernelSize'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744339)],
        HRESULT,
        'MorphBlackhat',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'kernelSize'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744340)],
        HRESULT,
        'Dilation',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'kernelSize'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744341)],
        HRESULT,
        'Erosion',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'kernelSize'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744342)],
        HRESULT,
        'GaussianBlur',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'kernelSize'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744343)],
        HRESULT,
        'Sharpen',
        (['in'], c_longlong, 'ptr'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744344)],
        HRESULT,
        'CannyEdge',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'kernelSize'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744345)],
        HRESULT,
        'Flip',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'flipCode'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744346)],
        HRESULT,
        'MorphOpen',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'kernelSize'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744347)],
        HRESULT,
        'MorphClose',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'kernelSize'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744348)],
        HRESULT,
        'Skeletonize',
        (['in'], c_longlong, 'ptr'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744349)],
        HRESULT,
        'GetImagePngData',
        (['in'], c_longlong, 'imgPtr'),
        (['out'], POINTER(VARIANT), 'data'),
        (['out'], POINTER(VARIANT), 'size'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744350)],
        HRESULT,
        'CmpColorEx',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], BSTR, 'colorJson'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744351)],
        HRESULT,
        'CmpColorPtrEx',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['in'], BSTR, 'colorJson'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744352)],
        HRESULT,
        'CmpColorHexEx',
        (['in'], BSTR, 'hex'),
        (['in'], BSTR, 'colorJson'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744353)],
        HRESULT,
        'BitPacking',
        (['in'], c_longlong, 'image'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744354)],
        HRESULT,
        'BitUnpacking',
        (['in'], BSTR, 'imageStr'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744355)],
        HRESULT,
        'SetImageCache',
        (['in'], c_int, 'enable'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744356)],
        HRESULT,
        'FindImageFromPtr',
        (['in'], c_longlong, 'source'),
        (['in'], c_longlong, 'templ'),
        (['in'], BSTR, 'deltaColor'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'dir'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744357)],
        HRESULT,
        'FindImageFromPtrAll',
        (['in'], c_longlong, 'source'),
        (['in'], c_longlong, 'templ'),
        (['in'], BSTR, 'deltaColor'),
        (['in'], c_double, 'matchVal'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744358)],
        HRESULT,
        'FindImageFromPath',
        (['in'], BSTR, 'source'),
        (['in'], BSTR, 'templ'),
        (['in'], BSTR, 'deltaColor'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'dir'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744359)],
        HRESULT,
        'FindImageFromPathAll',
        (['in'], BSTR, 'source'),
        (['in'], BSTR, 'templ'),
        (['in'], BSTR, 'deltaColor'),
        (['in'], c_double, 'matchVal'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744360)],
        HRESULT,
        'FindWindowsFromPtr',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], c_longlong, 'templ'),
        (['in'], BSTR, 'deltaColor'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'dir'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744361)],
        HRESULT,
        'FindWindowsFromPtrAll',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], c_longlong, 'templ'),
        (['in'], BSTR, 'deltaColor'),
        (['in'], c_double, 'matchVal'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744362)],
        HRESULT,
        'FindWindowsFromPath',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'templ'),
        (['in'], BSTR, 'deltaColor'),
        (['in'], c_double, 'matchVal'),
        (['in'], c_int, 'dir'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744363)],
        HRESULT,
        'FindWindowsFromPathAll',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'templ'),
        (['in'], BSTR, 'deltaColor'),
        (['in'], c_double, 'matchVal'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744364)],
        HRESULT,
        'RegistryOpenKey',
        (['in'], c_int, 'rootKey'),
        (['in'], BSTR, 'subKey'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744365)],
        HRESULT,
        'RegistryCreateKey',
        (['in'], c_int, 'rootKey'),
        (['in'], BSTR, 'subKey'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744366)],
        HRESULT,
        'RegistryCloseKey',
        (['in'], c_longlong, 'key'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744367)],
        HRESULT,
        'RegistryKeyExists',
        (['in'], c_int, 'rootKey'),
        (['in'], BSTR, 'subKey'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744368)],
        HRESULT,
        'RegistryDeleteKey',
        (['in'], c_int, 'rootKey'),
        (['in'], BSTR, 'subKey'),
        (['in'], c_int, 'recursive'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744369)],
        HRESULT,
        'RegistrySetString',
        (['in'], c_longlong, 'key'),
        (['in'], BSTR, 'valueName'),
        (['in'], BSTR, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744370)],
        HRESULT,
        'RegistryGetString',
        (['in'], c_longlong, 'key'),
        (['in'], BSTR, 'valueName'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744371)],
        HRESULT,
        'RegistrySetDword',
        (['in'], c_longlong, 'key'),
        (['in'], BSTR, 'valueName'),
        (['in'], c_int, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744372)],
        HRESULT,
        'RegistryGetDword',
        (['in'], c_longlong, 'key'),
        (['in'], BSTR, 'valueName'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744373)],
        HRESULT,
        'RegistrySetQword',
        (['in'], c_longlong, 'key'),
        (['in'], BSTR, 'valueName'),
        (['in'], c_longlong, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744374)],
        HRESULT,
        'RegistryGetQword',
        (['in'], c_longlong, 'key'),
        (['in'], BSTR, 'valueName'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744375)],
        HRESULT,
        'RegistryDeleteValue',
        (['in'], c_longlong, 'key'),
        (['in'], BSTR, 'valueName'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744376)],
        HRESULT,
        'RegistryEnumSubKeys',
        (['in'], c_longlong, 'key'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744377)],
        HRESULT,
        'RegistryEnumValues',
        (['in'], c_longlong, 'key'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744378)],
        HRESULT,
        'RegistrySetEnvironmentVariable',
        (['in'], BSTR, 'name'),
        (['in'], BSTR, 'value'),
        (['in'], c_int, 'systemWide'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744379)],
        HRESULT,
        'RegistryGetEnvironmentVariable',
        (['in'], BSTR, 'name'),
        (['in'], c_int, 'systemWide'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744380)],
        HRESULT,
        'RegistryGetUserRegistryPath',
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744381)],
        HRESULT,
        'RegistryGetSystemRegistryPath',
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744382)],
        HRESULT,
        'RegistryBackupToFile',
        (['in'], c_int, 'rootKey'),
        (['in'], BSTR, 'subKey'),
        (['in'], BSTR, 'filePath'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744383)],
        HRESULT,
        'RegistryRestoreFromFile',
        (['in'], BSTR, 'filePath'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744384)],
        HRESULT,
        'RegistryCompareKeys',
        (['in'], c_int, 'rootKey1'),
        (['in'], BSTR, 'subKey1'),
        (['in'], c_int, 'rootKey2'),
        (['in'], BSTR, 'subKey2'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744385)],
        HRESULT,
        'RegistrySearchKeys',
        (['in'], c_int, 'rootKey'),
        (['in'], BSTR, 'searchPath'),
        (['in'], BSTR, 'searchPattern'),
        (['in'], c_int, 'recursive'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744386)],
        HRESULT,
        'RegistryGetInstalledSoftware',
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744387)],
        HRESULT,
        'RegistryGetWindowsVersion',
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744388)],
        HRESULT,
        'OpenDatabase',
        (['in'], BSTR, 'dbName'),
        (['in'], BSTR, 'password'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744389)],
        HRESULT,
        'OpenMemoryDatabase',
        (['in'], c_longlong, 'address'),
        (['in'], c_int, 'size'),
        (['in'], BSTR, 'password'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744390)],
        HRESULT,
        'GetDatabaseError',
        (['in'], c_longlong, 'db'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744391)],
        HRESULT,
        'CloseDatabase',
        (['in'], c_longlong, 'db'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744392)],
        HRESULT,
        'GetAllTableNames',
        (['in'], c_longlong, 'db'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744393)],
        HRESULT,
        'GetTableInfo',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'tableName'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744394)],
        HRESULT,
        'GetTableInfoDetail',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'tableName'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744395)],
        HRESULT,
        'ExecuteSql',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'sql'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744396)],
        HRESULT,
        'ExecuteScalar',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'sql'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744397)],
        HRESULT,
        'ExecuteReader',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'sql'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744398)],
        HRESULT,
        'Read',
        (['in'], c_longlong, 'stmt'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744399)],
        HRESULT,
        'GetDataCount',
        (['in'], c_longlong, 'stmt'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744400)],
        HRESULT,
        'GetColumnCount',
        (['in'], c_longlong, 'stmt'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744401)],
        HRESULT,
        'GetColumnName',
        (['in'], c_longlong, 'stmt'),
        (['in'], c_int, 'iCol'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744402)],
        HRESULT,
        'GetColumnIndex',
        (['in'], c_longlong, 'stmt'),
        (['in'], BSTR, 'columnName'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744403)],
        HRESULT,
        'GetColumnType',
        (['in'], c_longlong, 'stmt'),
        (['in'], c_int, 'iCol'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744404)],
        HRESULT,
        'Finalize',
        (['in'], c_longlong, 'stmt'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744405)],
        HRESULT,
        'GetDouble',
        (['in'], c_longlong, 'stmt'),
        (['in'], c_int, 'iCol'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744406)],
        HRESULT,
        'GetInt32',
        (['in'], c_longlong, 'stmt'),
        (['in'], c_int, 'iCol'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744407)],
        HRESULT,
        'GetInt64',
        (['in'], c_longlong, 'stmt'),
        (['in'], c_int, 'iCol'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744408)],
        HRESULT,
        'GetString',
        (['in'], c_longlong, 'stmt'),
        (['in'], c_int, 'iCol'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744409)],
        HRESULT,
        'GetDoubleByColumnName',
        (['in'], c_longlong, 'stmt'),
        (['in'], BSTR, 'columnName'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744410)],
        HRESULT,
        'GetInt32ByColumnName',
        (['in'], c_longlong, 'stmt'),
        (['in'], BSTR, 'columnName'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744411)],
        HRESULT,
        'GetInt64ByColumnName',
        (['in'], c_longlong, 'stmt'),
        (['in'], BSTR, 'columnName'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744412)],
        HRESULT,
        'GetStringByColumnName',
        (['in'], c_longlong, 'stmt'),
        (['in'], BSTR, 'columnName'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744413)],
        HRESULT,
        'InitOlaDatabase',
        (['in'], c_longlong, 'db'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744414)],
        HRESULT,
        'InitOlaImageFromDir',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'dir'),
        (['in'], c_int, 'cover'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744415)],
        HRESULT,
        'RemoveOlaImageFromDir',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'dir'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744416)],
        HRESULT,
        'ExportOlaImageDir',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'dir'),
        (['in'], BSTR, 'exportDir'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744417)],
        HRESULT,
        'ImportOlaImage',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'dir'),
        (['in'], BSTR, 'fileName'),
        (['in'], c_int, 'cover'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744418)],
        HRESULT,
        'GetOlaImage',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'dir'),
        (['in'], BSTR, 'fileName'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744419)],
        HRESULT,
        'RemoveOlaImage',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'dir'),
        (['in'], BSTR, 'fileName'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744420)],
        HRESULT,
        'SetDbConfig',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'key'),
        (['in'], BSTR, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744421)],
        HRESULT,
        'GetDbConfig',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'key'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744422)],
        HRESULT,
        'RemoveDbConfig',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'key'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744423)],
        HRESULT,
        'SetDbConfigEx',
        (['in'], BSTR, 'key'),
        (['in'], BSTR, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744424)],
        HRESULT,
        'GetDbConfigEx',
        (['in'], BSTR, 'key'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744425)],
        HRESULT,
        'RemoveDbConfigEx',
        (['in'], BSTR, 'key'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744426)],
        HRESULT,
        'InitDictFromDir',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'dict_name'),
        (['in'], BSTR, 'dict_path'),
        (['in'], c_int, 'cover'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744427)],
        HRESULT,
        'ImportDictWord',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'dict_name'),
        (['in'], BSTR, 'pic_file_name'),
        (['in'], c_int, 'cover'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744428)],
        HRESULT,
        'ExportDict',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'dict_name'),
        (['in'], BSTR, 'export_dir'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744429)],
        HRESULT,
        'RemoveDict',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'dict_name'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744430)],
        HRESULT,
        'RemoveDictWord',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'dict_name'),
        (['in'], BSTR, 'word'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744431)],
        HRESULT,
        'GetDictImage',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'dict_name'),
        (['in'], BSTR, 'word'),
        (['in'], c_int, 'gap'),
        (['in'], c_int, 'dir'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744432)],
        HRESULT,
        'CreateDatabase',
        (['in'], BSTR, 'dbName'),
        (['in'], BSTR, 'password'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744433)],
        HRESULT,
        'InitDictFromTxt',
        (['in'], c_longlong, 'db'),
        (['in'], BSTR, 'dict_name'),
        (['in'], BSTR, 'dict_path'),
        (['in'], c_int, 'cover'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744434)],
        HRESULT,
        'OpenVideo',
        (['in'], BSTR, 'videoPath'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744435)],
        HRESULT,
        'OpenCamera',
        (['in'], c_int, 'deviceIndex'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744436)],
        HRESULT,
        'CloseVideo',
        (['in'], c_longlong, 'videoHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744437)],
        HRESULT,
        'IsVideoOpened',
        (['in'], c_longlong, 'videoHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744438)],
        HRESULT,
        'GetVideoInfo',
        (['in'], c_longlong, 'videoHandle'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744439)],
        HRESULT,
        'GetVideoWidth',
        (['in'], c_longlong, 'videoHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744440)],
        HRESULT,
        'GetVideoHeight',
        (['in'], c_longlong, 'videoHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744441)],
        HRESULT,
        'GetVideoFPS',
        (['in'], c_longlong, 'videoHandle'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744442)],
        HRESULT,
        'GetVideoTotalFrames',
        (['in'], c_longlong, 'videoHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744443)],
        HRESULT,
        'GetVideoDuration',
        (['in'], c_longlong, 'videoHandle'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744444)],
        HRESULT,
        'GetCurrentFrameIndex',
        (['in'], c_longlong, 'videoHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744445)],
        HRESULT,
        'GetCurrentTimestamp',
        (['in'], c_longlong, 'videoHandle'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744446)],
        HRESULT,
        'ReadNextFrame',
        (['in'], c_longlong, 'videoHandle'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744447)],
        HRESULT,
        'ReadFrameAtIndex',
        (['in'], c_longlong, 'videoHandle'),
        (['in'], c_int, 'frameIndex'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744448)],
        HRESULT,
        'ReadFrameAtTime',
        (['in'], c_longlong, 'videoHandle'),
        (['in'], c_double, 'timestamp'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744449)],
        HRESULT,
        'ReadCurrentFrame',
        (['in'], c_longlong, 'videoHandle'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744450)],
        HRESULT,
        'SeekToFrame',
        (['in'], c_longlong, 'videoHandle'),
        (['in'], c_int, 'frameIndex'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744451)],
        HRESULT,
        'SeekToTime',
        (['in'], c_longlong, 'videoHandle'),
        (['in'], c_double, 'timestamp'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744452)],
        HRESULT,
        'SeekToBeginning',
        (['in'], c_longlong, 'videoHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744453)],
        HRESULT,
        'SeekToEnd',
        (['in'], c_longlong, 'videoHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744454)],
        HRESULT,
        'ExtractFramesToFiles',
        (['in'], c_longlong, 'videoHandle'),
        (['in'], c_int, 'startFrame'),
        (['in'], c_int, 'endFrame'),
        (['in'], c_int, 'step'),
        (['in'], BSTR, 'outputDir'),
        (['in'], BSTR, 'imageFormat'),
        (['in'], c_int, 'jpegQuality'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744455)],
        HRESULT,
        'ExtractFramesByInterval',
        (['in'], c_longlong, 'videoHandle'),
        (['in'], c_double, 'intervalSeconds'),
        (['in'], BSTR, 'outputDir'),
        (['in'], BSTR, 'imageFormat'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744456)],
        HRESULT,
        'ExtractKeyFrames',
        (['in'], c_longlong, 'videoHandle'),
        (['in'], c_double, 'Threshold'),
        (['in'], c_int, 'maxFrames'),
        (['in'], BSTR, 'outputDir'),
        (['in'], BSTR, 'imageFormat'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744457)],
        HRESULT,
        'SaveCurrentFrame',
        (['in'], c_longlong, 'videoHandle'),
        (['in'], BSTR, 'outputPath'),
        (['in'], c_int, 'quality'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744458)],
        HRESULT,
        'SaveFrameAtIndex',
        (['in'], c_longlong, 'videoHandle'),
        (['in'], c_int, 'frameIndex'),
        (['in'], BSTR, 'outputPath'),
        (['in'], c_int, 'quality'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744459)],
        HRESULT,
        'FrameToBase64',
        (['in'], c_longlong, 'videoHandle'),
        (['in'], BSTR, 'format'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744460)],
        HRESULT,
        'CalculateFrameSimilarity',
        (['in'], c_longlong, 'frame1'),
        (['in'], c_longlong, 'frame2'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744461)],
        HRESULT,
        'GetVideoInfoFromPath',
        (['in'], BSTR, 'videoPath'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744462)],
        HRESULT,
        'IsValidVideoFile',
        (['in'], BSTR, 'videoPath'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744463)],
        HRESULT,
        'ExtractSingleFrame',
        (['in'], BSTR, 'videoPath'),
        (['in'], c_int, 'frameIndex'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744464)],
        HRESULT,
        'ExtractThumbnail',
        (['in'], BSTR, 'videoPath'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744465)],
        HRESULT,
        'ConvertVideo',
        (['in'], BSTR, 'inputPath'),
        (['in'], BSTR, 'outputPath'),
        (['in'], BSTR, 'codec'),
        (['in'], c_double, 'fps'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744466)],
        HRESULT,
        'ResizeVideo',
        (['in'], BSTR, 'inputPath'),
        (['in'], BSTR, 'outputPath'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744467)],
        HRESULT,
        'TrimVideo',
        (['in'], BSTR, 'inputPath'),
        (['in'], BSTR, 'outputPath'),
        (['in'], c_double, 'startTime'),
        (['in'], c_double, 'endTime'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744468)],
        HRESULT,
        'CreateVideoFromImages',
        (['in'], BSTR, 'imageDir'),
        (['in'], BSTR, 'outputPath'),
        (['in'], c_double, 'fps'),
        (['in'], BSTR, 'codec'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744469)],
        HRESULT,
        'DetectSceneChanges',
        (['in'], BSTR, 'videoPath'),
        (['in'], c_double, 'Threshold'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744470)],
        HRESULT,
        'CalculateAverageBrightness',
        (['in'], BSTR, 'videoPath'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744471)],
        HRESULT,
        'DetectMotion',
        (['in'], BSTR, 'videoPath'),
        (['in'], c_double, 'Threshold'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744472)],
        HRESULT,
        'SetWindowState',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_int, 'state'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744473)],
        HRESULT,
        'FindWindow',
        (['in'], BSTR, 'class_name'),
        (['in'], BSTR, 'title'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744474)],
        HRESULT,
        'GetClipboard',
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744475)],
        HRESULT,
        'SetClipboard',
        (['in'], BSTR, 'text'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744476)],
        HRESULT,
        'SendPaste',
        (['in'], c_longlong, 'hwnd'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744477)],
        HRESULT,
        'GetWindow',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_int, 'flag'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744478)],
        HRESULT,
        'GetWindowTitle',
        (['in'], c_longlong, 'hwnd'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744479)],
        HRESULT,
        'GetWindowClass',
        (['in'], c_longlong, 'hwnd'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744480)],
        HRESULT,
        'GetWindowRect',
        (['in'], c_longlong, 'hwnd'),
        (['out'], POINTER(VARIANT), 'x1'),
        (['out'], POINTER(VARIANT), 'y1'),
        (['out'], POINTER(VARIANT), 'x2'),
        (['out'], POINTER(VARIANT), 'y2'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744481)],
        HRESULT,
        'GetWindowProcessPath',
        (['in'], c_longlong, 'hwnd'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744482)],
        HRESULT,
        'GetWindowState',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_int, 'flag'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744483)],
        HRESULT,
        'GetForegroundWindow',
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744484)],
        HRESULT,
        'GetWindowProcessId',
        (['in'], c_longlong, 'hwnd'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744485)],
        HRESULT,
        'GetClientSize',
        (['in'], c_longlong, 'hwnd'),
        (['out'], POINTER(VARIANT), 'width'),
        (['out'], POINTER(VARIANT), 'height'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744486)],
        HRESULT,
        'GetMousePointWindow',
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744487)],
        HRESULT,
        'GetSpecialWindow',
        (['in'], c_int, 'flag'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744488)],
        HRESULT,
        'GetClientRect',
        (['in'], c_longlong, 'hwnd'),
        (['out'], POINTER(VARIANT), 'x1'),
        (['out'], POINTER(VARIANT), 'y1'),
        (['out'], POINTER(VARIANT), 'x2'),
        (['out'], POINTER(VARIANT), 'y2'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744489)],
        HRESULT,
        'SetWindowText',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'title'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744490)],
        HRESULT,
        'SetWindowSize',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744491)],
        HRESULT,
        'SetClientSize',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_int, 'width'),
        (['in'], c_int, 'height'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744492)],
        HRESULT,
        'SetWindowTransparent',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_int, 'alpha'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744493)],
        HRESULT,
        'FindWindowEx',
        (['in'], c_longlong, 'parent'),
        (['in'], BSTR, 'class_name'),
        (['in'], BSTR, 'title'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744494)],
        HRESULT,
        'FindWindowByProcess',
        (['in'], BSTR, 'process_name'),
        (['in'], BSTR, 'class_name'),
        (['in'], BSTR, 'title'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744495)],
        HRESULT,
        'MoveWindow',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744496)],
        HRESULT,
        'GetScaleFromWindows',
        (['in'], c_longlong, 'hwnd'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744497)],
        HRESULT,
        'GetWindowDpiAwarenessScale',
        (['in'], c_longlong, 'hwnd'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744498)],
        HRESULT,
        'EnumProcess',
        (['in'], BSTR, 'name'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744499)],
        HRESULT,
        'EnumWindow',
        (['in'], c_longlong, 'parent'),
        (['in'], BSTR, 'title'),
        (['in'], BSTR, 'className'),
        (['in'], c_int, 'filter'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744500)],
        HRESULT,
        'EnumWindowByProcess',
        (['in'], BSTR, 'process_name'),
        (['in'], BSTR, 'title'),
        (['in'], BSTR, 'class_name'),
        (['in'], c_int, 'filter'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744501)],
        HRESULT,
        'EnumWindowByProcessId',
        (['in'], c_longlong, 'pid'),
        (['in'], BSTR, 'title'),
        (['in'], BSTR, 'class_name'),
        (['in'], c_int, 'filter'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744502)],
        HRESULT,
        'EnumWindowSuper',
        (['in'], BSTR, 'spec1'),
        (['in'], c_int, 'flag1'),
        (['in'], c_int, 'type1'),
        (['in'], BSTR, 'spec2'),
        (['in'], c_int, 'flag2'),
        (['in'], c_int, 'type2'),
        (['in'], c_int, 'sort'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744503)],
        HRESULT,
        'GetPointWindow',
        (['in'], c_int, 'x'),
        (['in'], c_int, 'y'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744504)],
        HRESULT,
        'GetProcessInfo',
        (['in'], c_longlong, 'pid'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744505)],
        HRESULT,
        'ShowTaskBarIcon',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_int, 'show'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744506)],
        HRESULT,
        'FindWindowByProcessId',
        (['in'], c_longlong, 'process_id'),
        (['in'], BSTR, 'className'),
        (['in'], BSTR, 'title'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744507)],
        HRESULT,
        'GetWindowThreadId',
        (['in'], c_longlong, 'hwnd'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744508)],
        HRESULT,
        'FindWindowSuper',
        (['in'], BSTR, 'spec1'),
        (['in'], c_int, 'flag1'),
        (['in'], c_int, 'type1'),
        (['in'], BSTR, 'spec2'),
        (['in'], c_int, 'flag2'),
        (['in'], c_int, 'type2'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744509)],
        HRESULT,
        'ClientToScreen',
        (['in'], c_longlong, 'hwnd'),
        (['out'], POINTER(VARIANT), 'x'),
        (['out'], POINTER(VARIANT), 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744510)],
        HRESULT,
        'ScreenToClient',
        (['in'], c_longlong, 'hwnd'),
        (['out'], POINTER(VARIANT), 'x'),
        (['out'], POINTER(VARIANT), 'y'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744511)],
        HRESULT,
        'GetForegroundFocus',
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744512)],
        HRESULT,
        'SetWindowDisplay',
        (['in'], c_longlong, 'hwnd'),
        (['in'], c_int, 'affinity'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744513)],
        HRESULT,
        'IsDisplayDead',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], c_int, 'time'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744514)],
        HRESULT,
        'GetWindowsFps',
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744515)],
        HRESULT,
        'SetFontSmooth',
        (['in'], c_int, 'enable'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744516)],
        HRESULT,
        'CheckFontSmooth',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744517)],
        HRESULT,
        'GetCommandLine',
        (['in'], c_longlong, 'hwnd'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744518)],
        HRESULT,
        'TerminateProcess',
        (['in'], c_longlong, 'pid'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744519)],
        HRESULT,
        'TerminateProcessTree',
        (['in'], c_longlong, 'pid'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744520)],
        HRESULT,
        'EnableDebugPrivilege',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744521)],
        HRESULT,
        'SystemStart',
        (['in'], BSTR, 'applicationName'),
        (['in'], BSTR, 'commandLine'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744522)],
        HRESULT,
        'CreateChildProcess',
        (['in'], BSTR, 'applicationName'),
        (['in'], BSTR, 'commandLine'),
        (['in'], BSTR, 'currentDirectory'),
        (['in'], c_int, 'showType'),
        (['in'], c_int, 'parentProcessId'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744523)],
        HRESULT,
        'GetProcessIconImage',
        (['in'], c_longlong, 'pid'),
        (['in'], c_int, 'targetWidth'),
        (['in'], c_int, 'targetHeight'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744524)],
        HRESULT,
        'XmlCreateDocument',
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744525)],
        HRESULT,
        'XmlParse',
        (['in'], BSTR, 'str'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744526)],
        HRESULT,
        'XmlParseFile',
        (['in'], BSTR, 'filePath'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744527)],
        HRESULT,
        'XmlToString',
        (['in'], c_longlong, 'doc'),
        (['in'], c_int, 'compact'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744528)],
        HRESULT,
        'XmlSaveToFile',
        (['in'], c_longlong, 'doc'),
        (['in'], BSTR, 'filePath'),
        (['in'], c_int, 'compact'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744529)],
        HRESULT,
        'XmlFree',
        (['in'], c_longlong, 'doc'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744530)],
        HRESULT,
        'XmlGetRootElement',
        (['in'], c_longlong, 'doc'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744531)],
        HRESULT,
        'XmlCreateElement',
        (['in'], c_longlong, 'doc'),
        (['in'], BSTR, 'name'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744532)],
        HRESULT,
        'XmlInsertRootElement',
        (['in'], c_longlong, 'doc'),
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744533)],
        HRESULT,
        'XmlAppendChild',
        (['in'], c_longlong, 'parent'),
        (['in'], c_longlong, 'child'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744534)],
        HRESULT,
        'XmlGetFirstChild',
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744535)],
        HRESULT,
        'XmlGetNextSibling',
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744536)],
        HRESULT,
        'XmlFindElement',
        (['in'], c_longlong, 'parent'),
        (['in'], BSTR, 'name'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744537)],
        HRESULT,
        'XmlGetElementName',
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744538)],
        HRESULT,
        'XmlGetElementText',
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744539)],
        HRESULT,
        'XmlSetElementText',
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'text'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744540)],
        HRESULT,
        'XmlRemoveChild',
        (['in'], c_longlong, 'parent'),
        (['in'], c_longlong, 'child'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744541)],
        HRESULT,
        'XmlInsertBefore',
        (['in'], c_longlong, 'parent'),
        (['in'], c_longlong, 'newChild'),
        (['in'], c_longlong, 'refChild'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744542)],
        HRESULT,
        'XmlInsertAfter',
        (['in'], c_longlong, 'parent'),
        (['in'], c_longlong, 'newChild'),
        (['in'], c_longlong, 'refChild'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744543)],
        HRESULT,
        'XmlGetParent',
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744544)],
        HRESULT,
        'XmlGetPreviousSibling',
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744545)],
        HRESULT,
        'XmlGetLastChild',
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744546)],
        HRESULT,
        'XmlCloneElement',
        (['in'], c_longlong, 'doc'),
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744547)],
        HRESULT,
        'XmlHasChildren',
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744548)],
        HRESULT,
        'XmlGetAttribute',
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'name'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744549)],
        HRESULT,
        'XmlSetAttribute',
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'name'),
        (['in'], BSTR, 'value'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744550)],
        HRESULT,
        'XmlGetAttributeInt',
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'name'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744551)],
        HRESULT,
        'XmlSetAttributeInt',
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'name'),
        (['in'], c_int, 'value'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744552)],
        HRESULT,
        'XmlGetAttributeDouble',
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'name'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_double), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744553)],
        HRESULT,
        'XmlSetAttributeDouble',
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'name'),
        (['in'], c_double, 'value'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744554)],
        HRESULT,
        'XmlGetAttributeBool',
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'name'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744555)],
        HRESULT,
        'XmlSetAttributeBool',
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'name'),
        (['in'], c_int, 'value'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744556)],
        HRESULT,
        'XmlGetAttributeInt64',
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'name'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744557)],
        HRESULT,
        'XmlSetAttributeInt64',
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'name'),
        (['in'], c_longlong, 'value'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744558)],
        HRESULT,
        'XmlHasAttribute',
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'name'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744559)],
        HRESULT,
        'XmlGetAttributeNames',
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744560)],
        HRESULT,
        'XmlGetAttributeCount',
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744561)],
        HRESULT,
        'XmlDeleteAttribute',
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'name'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744562)],
        HRESULT,
        'XmlSetCDATA',
        (['in'], c_longlong, 'doc'),
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'content'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744563)],
        HRESULT,
        'XmlAddComment',
        (['in'], c_longlong, 'doc'),
        (['in'], c_longlong, 'element'),
        (['in'], BSTR, 'comment'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744564)],
        HRESULT,
        'XmlSetDeclaration',
        (['in'], c_longlong, 'doc'),
        (['in'], BSTR, 'version'),
        (['in'], BSTR, 'encoding'),
        (['in'], c_int, 'standalone'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744565)],
        HRESULT,
        'XmlQueryElement',
        (['in'], c_longlong, 'doc'),
        (['in'], BSTR, 'path'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744566)],
        HRESULT,
        'XmlGetChildCount',
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744567)],
        HRESULT,
        'XmlGetChildCountByName',
        (['in'], c_longlong, 'parent'),
        (['in'], BSTR, 'name'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744568)],
        HRESULT,
        'XmlGetChildByIndex',
        (['in'], c_longlong, 'parent'),
        (['in'], c_int, 'index'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744569)],
        HRESULT,
        'XmlGetChildByNameAndIndex',
        (['in'], c_longlong, 'parent'),
        (['in'], BSTR, 'name'),
        (['in'], c_int, 'index'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744570)],
        HRESULT,
        'XmlFindElementByAttribute',
        (['in'], c_longlong, 'parent'),
        (['in'], BSTR, 'elementName'),
        (['in'], BSTR, 'attrName'),
        (['in'], BSTR, 'attrValue'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744571)],
        HRESULT,
        'XmlGetElementDepth',
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744572)],
        HRESULT,
        'XmlGetElementPath',
        (['in'], c_longlong, 'element'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744573)],
        HRESULT,
        'XmlCompareElements',
        (['in'], c_longlong, 'element1'),
        (['in'], c_longlong, 'element2'),
        (['in'], c_int, 'deep'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744574)],
        HRESULT,
        'XmlMergeDocuments',
        (['in'], c_longlong, 'targetDoc'),
        (['in'], c_longlong, 'sourceDoc'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744575)],
        HRESULT,
        'XmlValidate',
        (['in'], c_longlong, 'doc'),
        (['out'], POINTER(VARIANT), 'err'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744576)],
        HRESULT,
        'XmlGetObjectCount',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744577)],
        HRESULT,
        'XmlCleanupAll',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744578)],
        HRESULT,
        'YoloInfer',
        (['in'], c_longlong, 'handle'),
        (['in'], c_longlong, 'imagePtr'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744579)],
        HRESULT,
        'YoloLoadModel',
        (['in'], BSTR, 'modelPath'),
        (['in'], BSTR, 'outputPath'),
        (['in'], BSTR, 'names_label'),
        (['in'], BSTR, 'password'),
        (['in'], c_int, 'modelType'),
        (['in'], c_int, 'inferenceType'),
        (['in'], c_int, 'inferenceDevice'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744580)],
        HRESULT,
        'YoloLoadModelMemory',
        (['in'], c_longlong, 'memoryAddr'),
        (['in'], c_int, 'size'),
        (['in'], c_int, 'modelType'),
        (['in'], c_int, 'inferenceType'),
        (['in'], c_int, 'inferenceDevice'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744581)],
        HRESULT,
        'YoloReleaseModel',
        (['in'], c_longlong, 'modelHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744582)],
        HRESULT,
        'YoloIsModelValid',
        (['in'], c_longlong, 'modelHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744583)],
        HRESULT,
        'YoloListModels',
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744584)],
        HRESULT,
        'YoloGetModelInfo',
        (['in'], c_longlong, 'modelHandle'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744585)],
        HRESULT,
        'YoloSetModelConfig',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], BSTR, 'configJson'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744586)],
        HRESULT,
        'YoloGetModelConfig',
        (['in'], c_longlong, 'modelHandle'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744587)],
        HRESULT,
        'YoloWarmup',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], c_int, 'iterations'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744588)],
        HRESULT,
        'YoloDetect',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], BSTR, 'classes'),
        (['in'], c_double, 'confidence'),
        (['in'], c_double, 'iou'),
        (['in'], c_int, 'maxDetections'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744589)],
        HRESULT,
        'YoloDetectSimple',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744590)],
        HRESULT,
        'YoloDetectFromPtr',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], c_longlong, 'imagePtr'),
        (['in'], BSTR, 'classes'),
        (['in'], c_double, 'confidence'),
        (['in'], c_double, 'iou'),
        (['in'], c_int, 'maxDetections'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744591)],
        HRESULT,
        'YoloDetectFromFile',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], BSTR, 'imagePath'),
        (['in'], BSTR, 'classes'),
        (['in'], c_double, 'confidence'),
        (['in'], c_double, 'iou'),
        (['in'], c_int, 'maxDetections'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744592)],
        HRESULT,
        'YoloDetectFromBase64',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], BSTR, 'base64Data'),
        (['in'], BSTR, 'classes'),
        (['in'], c_double, 'confidence'),
        (['in'], c_double, 'iou'),
        (['in'], c_int, 'maxDetections'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744593)],
        HRESULT,
        'YoloDetectBatch',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], BSTR, 'imagesJson'),
        (['in'], BSTR, 'classes'),
        (['in'], c_double, 'confidence'),
        (['in'], c_double, 'iou'),
        (['in'], c_int, 'maxDetections'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744594)],
        HRESULT,
        'YoloClassify',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], c_int, 'topK'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744595)],
        HRESULT,
        'YoloClassifyFromPtr',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], c_longlong, 'imagePtr'),
        (['in'], c_int, 'topK'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744596)],
        HRESULT,
        'YoloClassifyFromFile',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], BSTR, 'imagePath'),
        (['in'], c_int, 'topK'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744597)],
        HRESULT,
        'YoloSegment',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], c_double, 'confidence'),
        (['in'], c_double, 'iou'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744598)],
        HRESULT,
        'YoloSegmentFromPtr',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], c_longlong, 'imagePtr'),
        (['in'], c_double, 'confidence'),
        (['in'], c_double, 'iou'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744599)],
        HRESULT,
        'YoloPose',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], c_double, 'confidence'),
        (['in'], c_double, 'iou'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744600)],
        HRESULT,
        'YoloPoseFromPtr',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], c_longlong, 'imagePtr'),
        (['in'], c_double, 'confidence'),
        (['in'], c_double, 'iou'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744601)],
        HRESULT,
        'YoloObb',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], c_double, 'confidence'),
        (['in'], c_double, 'iou'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744602)],
        HRESULT,
        'YoloObbFromPtr',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], c_longlong, 'imagePtr'),
        (['in'], c_double, 'confidence'),
        (['in'], c_double, 'iou'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744603)],
        HRESULT,
        'YoloKeyPoint',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], c_int, 'x1'),
        (['in'], c_int, 'y1'),
        (['in'], c_int, 'x2'),
        (['in'], c_int, 'y2'),
        (['in'], c_double, 'confidence'),
        (['in'], c_double, 'iou'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744604)],
        HRESULT,
        'YoloKeyPointFromPtr',
        (['in'], c_longlong, 'modelHandle'),
        (['in'], c_longlong, 'imagePtr'),
        (['in'], c_double, 'confidence'),
        (['in'], c_double, 'iou'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744605)],
        HRESULT,
        'YoloGetInferenceStats',
        (['in'], c_longlong, 'modelHandle'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744606)],
        HRESULT,
        'YoloResetStats',
        (['in'], c_longlong, 'modelHandle'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744607)],
        HRESULT,
        'YoloGetLastError',
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744608)],
        HRESULT,
        'YoloClearError',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744609)],
        HRESULT,
        'CreateCOLAPlugInterFace',
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744610)],
        HRESULT,
        'DestroyCOLAPlugInterFace',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744611)],
        HRESULT,
        'Reg',
        (['in'], BSTR, 'userCode'),
        (['in'], BSTR, 'softCode'),
        (['in'], BSTR, 'featureList'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744612)],
        HRESULT,
        'Ver',
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744613)],
        HRESULT,
        'SetPath',
        (['in'], BSTR, 'path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744614)],
        HRESULT,
        'GetPath',
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744615)],
        HRESULT,
        'GetMachineCode',
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744616)],
        HRESULT,
        'GetBasePath',
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744617)],
        HRESULT,
        'BindWindow',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'display'),
        (['in'], BSTR, 'mouse'),
        (['in'], BSTR, 'keypad'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744618)],
        HRESULT,
        'BindWindowEx',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'display'),
        (['in'], BSTR, 'mouse'),
        (['in'], BSTR, 'keypad'),
        (['in'], BSTR, 'pubstr'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744619)],
        HRESULT,
        'UnBindWindow',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744620)],
        HRESULT,
        'GetBindWindow',
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744621)],
        HRESULT,
        'ReleaseWindowsDll',
        (['in'], c_longlong, 'hwnd'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744622)],
        HRESULT,
        'FreeStringPtr',
        (['in'], c_longlong, 'ptr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744623)],
        HRESULT,
        'GetStringSize',
        (['in'], c_longlong, 'ptr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744624)],
        HRESULT,
        'GetStringFromPtr',
        (['in'], c_longlong, 'ptr'),
        (['in'], c_longlong, 'lpString'),
        (['in'], c_int, 'size'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744625)],
        HRESULT,
        'delay',
        (['in'], c_int, 'millisecond'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744626)],
        HRESULT,
        'Delays',
        (['in'], c_int, 'minMillisecond'),
        (['in'], c_int, 'maxMillisecond'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744627)],
        HRESULT,
        'SetUAC',
        (['in'], c_int, 'enable'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744628)],
        HRESULT,
        'CheckUAC',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744629)],
        HRESULT,
        'RunApp',
        (['in'], BSTR, 'appPath'),
        (['in'], c_int, 'mode'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744630)],
        HRESULT,
        'ExecuteCmd',
        (['in'], BSTR, 'cmd'),
        (['in'], BSTR, 'current_dir'),
        (['in'], c_int, 'time_out'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744631)],
        HRESULT,
        'GetConfig',
        (['in'], BSTR, 'configKey'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744632)],
        HRESULT,
        'SetConfig',
        (['in'], BSTR, 'configStr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744633)],
        HRESULT,
        'SetConfigByKey',
        (['in'], BSTR, 'key'),
        (['in'], BSTR, 'value'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744634)],
        HRESULT,
        'SendDropFiles',
        (['in'], c_longlong, 'hwnd'),
        (['in'], BSTR, 'file_path'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744635)],
        HRESULT,
        'FreeMemoryPtr',
        (['in'], c_longlong, 'ptr'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744636)],
        HRESULT,
        'SetDefaultEncode',
        (['in'], c_int, 'inputEncoding'),
        (['in'], c_int, 'outputEncoding'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744637)],
        HRESULT,
        'GetLastError',
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744638)],
        HRESULT,
        'GetLastErrorString',
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744639)],
        HRESULT,
        'HideModule',
        (['in'], BSTR, 'moduleName'),
        (['out', 'retval'], POINTER(c_longlong), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744640)],
        HRESULT,
        'UnhideModule',
        (['in'], c_longlong, 'ctx'),
        (['out', 'retval'], POINTER(c_int), 'nret')
    ),
    COMMETHOD(
        [dispid(1610744641)],
        HRESULT,
        'GetPlugInfo',
        (['in'], c_int, 'type'),
        (['out', 'retval'], POINTER(BSTR), 'nret')
    ),
]

################################################################
# code template for IOlaPlug implementation
# class IOlaPlug_Impl(object):
#     def GetRandomNumber(self, min, max):
#         '-no docstring-'
#         #return nret
#
#     def GetRandomDouble(self, min, max):
#         '-no docstring-'
#         #return nret
#
#     def ExcludePos(self, json, type, x1, y1, x2, y2):
#         '-no docstring-'
#         #return nret
#
#     def FindNearestPos(self, json, type, x, y):
#         '-no docstring-'
#         #return nret
#
#     def SortPosDistance(self, json, type, x, y):
#         '-no docstring-'
#         #return nret
#
#     def GetDenseRect(self, image, width, height):
#         '-no docstring-'
#         #return x1, y1, x2, y2, nret
#
#     def PathPlanning(self, image, startX, startY, endX, endY, potentialRadius, searchRadius):
#         '-no docstring-'
#         #return nret
#
#     def CreateGraph(self, json):
#         '-no docstring-'
#         #return nret
#
#     def GetGraph(self, graphPtr):
#         '-no docstring-'
#         #return nret
#
#     def AddEdge(self, graphPtr, from, to, weight, isDirected):
#         '-no docstring-'
#         #return nret
#
#     def GetShortestPath(self, graphPtr, from, to):
#         '-no docstring-'
#         #return nret
#
#     def GetShortestDistance(self, graphPtr, from, to):
#         '-no docstring-'
#         #return nret
#
#     def ClearGraph(self, graphPtr):
#         '-no docstring-'
#         #return nret
#
#     def DeleteGraph(self, graphPtr):
#         '-no docstring-'
#         #return nret
#
#     def GetNodeCount(self, graphPtr):
#         '-no docstring-'
#         #return nret
#
#     def GetEdgeCount(self, graphPtr):
#         '-no docstring-'
#         #return nret
#
#     def GetShortestPathToAllNodes(self, graphPtr, startNode):
#         '-no docstring-'
#         #return nret
#
#     def GetMinimumSpanningTree(self, graphPtr):
#         '-no docstring-'
#         #return nret
#
#     def GetMinimumArborescence(self, graphPtr, root):
#         '-no docstring-'
#         #return nret
#
#     def GetDirectedPathToAllNodes(self, graphPtr, startNode):
#         '-no docstring-'
#         #return nret
#
#     def CreateGraphFromCoordinates(self, json, connectAll, maxDistance, useEuclideanDistance):
#         '-no docstring-'
#         #return nret
#
#     def AddCoordinateNode(self, graphPtr, name, x, y, connectToExisting, maxDistance, useEuclideanDistance):
#         '-no docstring-'
#         #return nret
#
#     def GetNodeCoordinates(self, graphPtr, name):
#         '-no docstring-'
#         #return nret
#
#     def SetNodeConnection(self, graphPtr, from, to, canConnect, weight):
#         '-no docstring-'
#         #return nret
#
#     def GetNodeConnectionStatus(self, graphPtr, from, to):
#         '-no docstring-'
#         #return nret
#
#     def Assemble(self, asmStr, baseAddr, arch, mode):
#         '-no docstring-'
#         #return nret
#
#     def Disassemble(self, asmCode, baseAddr, arch, mode, showType):
#         '-no docstring-'
#         #return nret
#
#     def AsmCall(self, hwnd, asmStr, type, baseAddr):
#         '-no docstring-'
#         #return nret
#
#     def Login(self, userCode, softCode, featureList, softVersion, dealerCode):
#         '-no docstring-'
#         #return nret
#
#     def Activate(self, userCode, softCode, softVersion, dealerCode, licenseKey):
#         '-no docstring-'
#         #return nret
#
#     def DmaAddDevice(self, vmId):
#         '-no docstring-'
#         #return nret
#
#     def DmaAddDeviceEx(self, connectionString):
#         '-no docstring-'
#         #return nret
#
#     def DmaRemoveDevice(self, deviceId):
#         '-no docstring-'
#         #return nret
#
#     def DmaGetPidFromName(self, deviceId, processName):
#         '-no docstring-'
#         #return nret
#
#     def DmaGetPidList(self, deviceId):
#         '-no docstring-'
#         #return nret
#
#     def DmaGetProcessInfo(self, deviceId, pid):
#         '-no docstring-'
#         #return nret
#
#     def DmaGetModuleBase(self, deviceId, pid, moduleName):
#         '-no docstring-'
#         #return nret
#
#     def DmaGetModuleSize(self, deviceId, pid, moduleName):
#         '-no docstring-'
#         #return nret
#
#     def DmaGetProcAddress(self, deviceId, pid, moduleName, functionName):
#         '-no docstring-'
#         #return nret
#
#     def DmaScatterCreate(self, deviceId, pid):
#         '-no docstring-'
#         #return nret
#
#     def DmaScatterPrepare(self, scatterHandle, address, size):
#         '-no docstring-'
#         #return nret
#
#     def DmaScatterExecute(self, scatterHandle):
#         '-no docstring-'
#         #return nret
#
#     def DmaScatterRead(self, scatterHandle, address, buffer, size):
#         '-no docstring-'
#         #return nret
#
#     def DmaScatterClear(self, scatterHandle):
#         '-no docstring-'
#         #return nret
#
#     def DmaScatterClose(self, scatterHandle):
#         '-no docstring-'
#         #return nret
#
#     def DmaFindData(self, deviceId, pid, addr_range, data):
#         '-no docstring-'
#         #return nret
#
#     def DmaFindDataEx(self, deviceId, pid, addr_range, data, step, multi_thread, mode):
#         '-no docstring-'
#         #return nret
#
#     def DmaFindDouble(self, deviceId, pid, addr_range, double_value_min, double_value_max):
#         '-no docstring-'
#         #return nret
#
#     def DmaFindDoubleEx(self, deviceId, pid, addr_range, double_value_min, double_value_max, step, multi_thread, mode):
#         '-no docstring-'
#         #return nret
#
#     def DmaFindFloat(self, deviceId, pid, addr_range, float_value_min, float_value_max):
#         '-no docstring-'
#         #return nret
#
#     def DmaFindFloatEx(self, deviceId, pid, addr_range, float_value_min, float_value_max, step, multi_thread, mode):
#         '-no docstring-'
#         #return nret
#
#     def DmaFindInt(self, deviceId, pid, addr_range, int_value_min, int_value_max, type):
#         '-no docstring-'
#         #return nret
#
#     def DmaFindIntEx(self, deviceId, pid, addr_range, int_value_min, int_value_max, type, step, multi_thread, mode):
#         '-no docstring-'
#         #return nret
#
#     def DmaFindString(self, deviceId, pid, addr_range, string_value, type):
#         '-no docstring-'
#         #return nret
#
#     def DmaFindStringEx(self, deviceId, pid, addr_range, string_value, type, step, multi_thread, mode):
#         '-no docstring-'
#         #return nret
#
#     def DmaReadData(self, deviceId, pid, addr, len):
#         '-no docstring-'
#         #return nret
#
#     def DmaReadDataAddr(self, deviceId, pid, addr, len):
#         '-no docstring-'
#         #return nret
#
#     def DmaReadDataAddrToBin(self, deviceId, pid, addr, len):
#         '-no docstring-'
#         #return nret
#
#     def DmaReadDataToBin(self, deviceId, pid, addr, len):
#         '-no docstring-'
#         #return nret
#
#     def DmaReadDouble(self, deviceId, pid, addr):
#         '-no docstring-'
#         #return nret
#
#     def DmaReadDoubleAddr(self, deviceId, pid, addr):
#         '-no docstring-'
#         #return nret
#
#     def DmaReadFloat(self, deviceId, pid, addr):
#         '-no docstring-'
#         #return nret
#
#     def DmaReadFloatAddr(self, deviceId, pid, addr):
#         '-no docstring-'
#         #return nret
#
#     def DmaReadInt(self, deviceId, pid, addr, type):
#         '-no docstring-'
#         #return nret
#
#     def DmaReadIntAddr(self, deviceId, pid, addr, type):
#         '-no docstring-'
#         #return nret
#
#     def DmaReadString(self, deviceId, pid, addr, type, len):
#         '-no docstring-'
#         #return nret
#
#     def DmaReadStringAddr(self, deviceId, pid, addr, type, len):
#         '-no docstring-'
#         #return nret
#
#     def DmaWriteData(self, deviceId, pid, addr, data):
#         '-no docstring-'
#         #return nret
#
#     def DmaWriteDataFromBin(self, deviceId, pid, addr, data, len):
#         '-no docstring-'
#         #return nret
#
#     def DmaWriteDataAddr(self, deviceId, pid, addr, data):
#         '-no docstring-'
#         #return nret
#
#     def DmaWriteDataAddrFromBin(self, deviceId, pid, addr, data, len):
#         '-no docstring-'
#         #return nret
#
#     def DmaWriteDouble(self, deviceId, pid, addr, double_value):
#         '-no docstring-'
#         #return nret
#
#     def DmaWriteDoubleAddr(self, deviceId, pid, addr, double_value):
#         '-no docstring-'
#         #return nret
#
#     def DmaWriteFloat(self, deviceId, pid, addr, float_value):
#         '-no docstring-'
#         #return nret
#
#     def DmaWriteFloatAddr(self, deviceId, pid, addr, float_value):
#         '-no docstring-'
#         #return nret
#
#     def DmaWriteInt(self, deviceId, pid, addr, type, value):
#         '-no docstring-'
#         #return nret
#
#     def DmaWriteIntAddr(self, deviceId, pid, addr, type, value):
#         '-no docstring-'
#         #return nret
#
#     def DmaWriteString(self, deviceId, pid, addr, type, value):
#         '-no docstring-'
#         #return nret
#
#     def DmaWriteStringAddr(self, deviceId, pid, addr, type, value):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiCleanup(self):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiRectangle(self, x, y, width, height, mode, lineThickness):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiCircle(self, x, y, radius, mode, lineThickness):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiLine(self, x1, y1, x2, y2, lineThickness):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiText(self, text, x, y, fontPath, fontSize, align):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiImage(self, imagePath, x, y):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiImagePtr(self, imagePtr, x, y):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiWindow(self, title, x, y, width, height, style):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiPanel(self, parentHandle, x, y, width, height):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiButton(self, parentHandle, text, x, y, width, height):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiDeleteObject(self, handle):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiClearAll(self):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetGuiActive(self, active):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiIsGuiActive(self):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetGuiClickThrough(self, enabled):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiIsGuiClickThrough(self):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetPosition(self, handle, x, y):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetSize(self, handle, width, height):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetColor(self, handle, r, g, b, a):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetAlpha(self, handle, alpha):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetDrawMode(self, handle, mode):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetLineThickness(self, handle, thickness):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetFont(self, handle, fontPath, fontSize):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetTextAlign(self, handle, align):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetText(self, handle, text):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetVisible(self, handle, visible):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiGetPosition(self, handle):
#         '-no docstring-'
#         #return x, y, nret
#
#     def DrawGuiGetSize(self, handle):
#         '-no docstring-'
#         #return width, height, nret
#
#     def DrawGuiSetZOrder(self, handle, zOrder):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetParent(self, handle, parentHandle):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiIsPointInObject(self, handle, x, y):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetWindowTitle(self, handle, title):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetWindowStyle(self, handle, style):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetWindowTopMost(self, handle, topMost):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetWindowTransparency(self, handle, alpha):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetButtonCallback(self, handle, callback):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiSetMouseCallback(self, handle, callback):
#         '-no docstring-'
#         #return nret
#
#     def DrawGuiGetDrawObjectType(self, handle):
#         '-no docstring-'
#         #return nret
#
#     def LoadDriver(self, driver_name, driver_path):
#         '-no docstring-'
#         #return nret
#
#     def UnloadDriver(self, driver_name):
#         '-no docstring-'
#         #return nret
#
#     def DriverTest(self):
#         '-no docstring-'
#         #return nret
#
#     def LoadPdb(self):
#         '-no docstring-'
#         #return nret
#
#     def GetPdbDownloadUrls(self):
#         '-no docstring-'
#         #return nret
#
#     def AddProtectPID(self, pid, mode, allow_pid):
#         '-no docstring-'
#         #return nret
#
#     def RemoveProtectPID(self, pid):
#         '-no docstring-'
#         #return nret
#
#     def AddAllowPID(self, pid):
#         '-no docstring-'
#         #return nret
#
#     def RemoveAllowPID(self, pid):
#         '-no docstring-'
#         #return nret
#
#     def HideProcess(self, pid, enable):
#         '-no docstring-'
#         #return nret
#
#     def ProtectProcess(self, pid, enable):
#         '-no docstring-'
#         #return nret
#
#     def ProtectProcess2(self, pid, enable):
#         '-no docstring-'
#         #return nret
#
#     def SetMemoryMode(self, mode):
#         '-no docstring-'
#         #return nret
#
#     def ExportDriver(self, driver_path, type):
#         '-no docstring-'
#         #return nret
#
#     def FakeProcess(self, pid, fake_pid):
#         '-no docstring-'
#         #return nret
#
#     def ProtectWindow(self, hwnd, flag):
#         '-no docstring-'
#         #return nret
#
#     def KeOpenThread(self, thread_id):
#         '-no docstring-'
#         #return thread_handle, nret
#
#     def KeOpenProcess(self, pid):
#         '-no docstring-'
#         #return process_handle, nret
#
#     def StartSecurityGuard(self):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileTestDriver(self):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileEnableDriver(self):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileDisableDriver(self):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileStartFilter(self):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileStopFilter(self):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileAddProtectedPath(self, path, mode, is_directory):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileRemoveProtectedPath(self, path):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileClearProtectedPaths(self):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileQueryProtectedPath(self, path):
#         '-no docstring-'
#         #return mode, nret
#
#     def ProtectFileAddWhitelist(self, pid):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileRemoveWhitelist(self, pid):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileClearWhitelist(self):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileQueryWhitelist(self, pid):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileAddBlacklist(self, pid):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileRemoveBlacklist(self, pid):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileClearBlacklist(self):
#         '-no docstring-'
#         #return nret
#
#     def ProtectFileQueryBlacklist(self, pid):
#         '-no docstring-'
#         #return nret
#
#     def VipProtectEnableDriver(self):
#         '-no docstring-'
#         #return nret
#
#     def VipProtectDisableDriver(self):
#         '-no docstring-'
#         #return nret
#
#     def VipProtectAddProtect(self, pid, path, mode, permission):
#         '-no docstring-'
#         #return nret
#
#     def VipProtectRemoveProtect(self, pid, path):
#         '-no docstring-'
#         #return nret
#
#     def VipProtectClearAll(self):
#         '-no docstring-'
#         #return nret
#
#     def VipProtectAddWhitelist(self, pid, path):
#         '-no docstring-'
#         #return nret
#
#     def VipProtectRemoveWhitelist(self, pid, path):
#         '-no docstring-'
#         #return nret
#
#     def VipProtectClearWhitelist(self):
#         '-no docstring-'
#         #return nret
#
#     def VipProtectAddBlacklist(self, pid, path):
#         '-no docstring-'
#         #return nret
#
#     def VipProtectRemoveBlacklist(self, pid, path):
#         '-no docstring-'
#         #return nret
#
#     def VipProtectClearBlacklist(self):
#         '-no docstring-'
#         #return nret
#
#     def EnabletVtDriver(self, enable):
#         '-no docstring-'
#         #return nret
#
#     def VtFakeWriteData(self, hwnd, addr, data):
#         '-no docstring-'
#         #return nret
#
#     def VtFakeWriteDataFromBin(self, hwnd, addr, data, len):
#         '-no docstring-'
#         #return nret
#
#     def VtFakeWriteDataAddr(self, hwnd, addr, data):
#         '-no docstring-'
#         #return nret
#
#     def VtFakeWriteDataAddrFromBin(self, hwnd, addr, data, len):
#         '-no docstring-'
#         #return nret
#
#     def VtUnFakeMemoryAddr(self, hwnd, addr):
#         '-no docstring-'
#         #return nret
#
#     def VtUnFakeMemory(self, hwnd, addr):
#         '-no docstring-'
#         #return nret
#
#     def GenerateRSAKey(self, publicKeyPath, privateKeyPath, type, keySize):
#         '-no docstring-'
#         #return nret
#
#     def ConvertRSAPublicKey(self, publicKey, inputType, outputType):
#         '-no docstring-'
#         #return nret
#
#     def ConvertRSAPrivateKey(self, privateKey, inputType, outputType):
#         '-no docstring-'
#         #return nret
#
#     def EncryptWithRsa(self, message, publicKey, paddingType):
#         '-no docstring-'
#         #return nret
#
#     def DecryptWithRsa(self, cipher, privateKey, paddingType):
#         '-no docstring-'
#         #return nret
#
#     def SignWithRsa(self, message, privateCer, shaType, paddingType):
#         '-no docstring-'
#         #return nret
#
#     def VerifySignWithRsa(self, message, signature, shaType, paddingType, publicCer):
#         '-no docstring-'
#         #return nret
#
#     def AESEncrypt(self, source, key):
#         '-no docstring-'
#         #return nret
#
#     def AESDecrypt(self, source, key):
#         '-no docstring-'
#         #return nret
#
#     def AESEncryptEx(self, source, key, iv, mode, paddingType):
#         '-no docstring-'
#         #return nret
#
#     def AESDecryptEx(self, source, key, iv, mode, paddingType):
#         '-no docstring-'
#         #return nret
#
#     def MD5Encrypt(self, source):
#         '-no docstring-'
#         #return nret
#
#     def SHAHash(self, source, shaType):
#         '-no docstring-'
#         #return nret
#
#     def HMAC(self, source, key, shaType):
#         '-no docstring-'
#         #return nret
#
#     def GenerateRandomBytes(self, length, type):
#         '-no docstring-'
#         #return nret
#
#     def GenerateGuid(self, type):
#         '-no docstring-'
#         #return nret
#
#     def Base64Encode(self, source):
#         '-no docstring-'
#         #return nret
#
#     def Base64Decode(self, source):
#         '-no docstring-'
#         #return nret
#
#     def PBKDF2(self, password, salt, iterations, keyLength, shaType):
#         '-no docstring-'
#         #return nret
#
#     def MD5File(self, filePath):
#         '-no docstring-'
#         #return nret
#
#     def SHAFile(self, filePath, shaType):
#         '-no docstring-'
#         #return nret
#
#     def CreateFolder(self, path):
#         '-no docstring-'
#         #return nret
#
#     def DeleteFolder(self, path):
#         '-no docstring-'
#         #return nret
#
#     def GetFolderList(self, path, baseDir):
#         '-no docstring-'
#         #return nret
#
#     def IsDirectory(self, path):
#         '-no docstring-'
#         #return nret
#
#     def IsFile(self, path):
#         '-no docstring-'
#         #return nret
#
#     def CreateFile(self, path):
#         '-no docstring-'
#         #return nret
#
#     def DeleteFile(self, path):
#         '-no docstring-'
#         #return nret
#
#     def CopyFile(self, src, dst):
#         '-no docstring-'
#         #return nret
#
#     def MoveFile(self, src, dst):
#         '-no docstring-'
#         #return nret
#
#     def RenameFile(self, src, dst):
#         '-no docstring-'
#         #return nret
#
#     def GetFileSize(self, path):
#         '-no docstring-'
#         #return nret
#
#     def GetFileList(self, path, baseDir):
#         '-no docstring-'
#         #return nret
#
#     def GetFileName(self, path, withExtension):
#         '-no docstring-'
#         #return nret
#
#     def ToAbsolutePath(self, path):
#         '-no docstring-'
#         #return nret
#
#     def ToRelativePath(self, path):
#         '-no docstring-'
#         #return nret
#
#     def FileOrDirectoryExists(self, path):
#         '-no docstring-'
#         #return nret
#
#     def ReadFileString(self, filePath, encoding):
#         '-no docstring-'
#         #return nret
#
#     def ReadBytesFromFile(self, filePath, offset, size):
#         '-no docstring-'
#         #return nret
#
#     def WriteStringToFile(self, filePath, data, encoding):
#         '-no docstring-'
#         #return nret
#
#     def WriteBytesToFile(self, filePath, dataAddr, dataSize):
#         '-no docstring-'
#         #return nret
#
#     def StartHotkeyHook(self):
#         '-no docstring-'
#         #return nret
#
#     def StopHotkeyHook(self):
#         '-no docstring-'
#         #return nret
#
#     def RegisterHotkey(self, keycode, modifiers, callback):
#         '-no docstring-'
#         #return nret
#
#     def UnregisterHotkey(self, keycode, modifiers):
#         '-no docstring-'
#         #return nret
#
#     def RegisterMouseButton(self, button, type, callback):
#         '-no docstring-'
#         #return nret
#
#     def UnregisterMouseButton(self, button, type):
#         '-no docstring-'
#         #return nret
#
#     def RegisterMouseWheel(self, callback):
#         '-no docstring-'
#         #return nret
#
#     def UnregisterMouseWheel(self):
#         '-no docstring-'
#         #return nret
#
#     def RegisterMouseMove(self, callback):
#         '-no docstring-'
#         #return nret
#
#     def UnregisterMouseMove(self):
#         '-no docstring-'
#         #return nret
#
#     def RegisterMouseDrag(self, callback):
#         '-no docstring-'
#         #return nret
#
#     def UnregisterMouseDrag(self):
#         '-no docstring-'
#         #return nret
#
#     def Inject(self, hwnd, dll_path, type, bypassGuard):
#         '-no docstring-'
#         #return nret
#
#     def InjectFromUrl(self, hwnd, url, type, bypassGuard):
#         '-no docstring-'
#         #return nret
#
#     def InjectFromBuffer(self, hwnd, bufferAddr, bufferSize, type, bypassGuard):
#         '-no docstring-'
#         #return nret
#
#     def JsonCreateObject(self):
#         '-no docstring-'
#         #return nret
#
#     def JsonCreateArray(self):
#         '-no docstring-'
#         #return nret
#
#     def JsonParse(self, str):
#         '-no docstring-'
#         #return err, nret
#
#     def JsonFree(self, obj):
#         '-no docstring-'
#         #return nret
#
#     def JsonStringify(self, obj, indent):
#         '-no docstring-'
#         #return err, nret
#
#     def JsonGetSize(self, obj):
#         '-no docstring-'
#         #return err, nret
#
#     def JsonSetValue(self, obj, key, value):
#         '-no docstring-'
#         #return nret
#
#     def JsonArrayAppend(self, arr, value):
#         '-no docstring-'
#         #return nret
#
#     def JsonClear(self, obj):
#         '-no docstring-'
#         #return nret
#
#     def JsonDeleteKey(self, obj, key):
#         '-no docstring-'
#         #return nret
#
#     def JsonGetValue(self, obj, key):
#         '-no docstring-'
#         #return err, nret
#
#     def JsonGetArrayItem(self, arr, index):
#         '-no docstring-'
#         #return err, nret
#
#     def JsonGetString(self, obj, key):
#         '-no docstring-'
#         #return err, nret
#
#     def JsonGetNumber(self, obj, key):
#         '-no docstring-'
#         #return err, nret
#
#     def JsonGetBool(self, obj, key):
#         '-no docstring-'
#         #return err, nret
#
#     def JsonSetString(self, obj, key, value):
#         '-no docstring-'
#         #return nret
#
#     def JsonSetNumber(self, obj, key, value):
#         '-no docstring-'
#         #return nret
#
#     def JsonSetBool(self, obj, key, value):
#         '-no docstring-'
#         #return nret
#
#     def ParseMatchImageJson(self, str):
#         '-no docstring-'
#         #return matchState, x, y, width, height, matchVal, angle, index, nret
#
#     def GetMatchImageAllCount(self, str):
#         '-no docstring-'
#         #return nret
#
#     def ParseMatchImageAllJson(self, str, parseIndex):
#         '-no docstring-'
#         #return matchState, x, y, width, height, matchVal, angle, index, nret
#
#     def GetResultCount(self, resultStr):
#         '-no docstring-'
#         #return nret
#
#     def KeyDown(self, vk_code):
#         '-no docstring-'
#         #return nret
#
#     def KeyUp(self, vk_code):
#         '-no docstring-'
#         #return nret
#
#     def KeyPress(self, vk_code):
#         '-no docstring-'
#         #return nret
#
#     def LeftDown(self):
#         '-no docstring-'
#         #return nret
#
#     def LeftUp(self):
#         '-no docstring-'
#         #return nret
#
#     def MoveTo(self, x, y):
#         '-no docstring-'
#         #return nret
#
#     def MoveToWithoutSimulator(self, x, y):
#         '-no docstring-'
#         #return nret
#
#     def RightClick(self):
#         '-no docstring-'
#         #return nret
#
#     def RightDoubleClick(self):
#         '-no docstring-'
#         #return nret
#
#     def RightDown(self):
#         '-no docstring-'
#         #return nret
#
#     def RightUp(self):
#         '-no docstring-'
#         #return nret
#
#     def GetCursorShape(self):
#         '-no docstring-'
#         #return nret
#
#     def GetCursorImage(self):
#         '-no docstring-'
#         #return nret
#
#     def KeyPressStr(self, keyStr, delay):
#         '-no docstring-'
#         #return nret
#
#     def SendString(self, hwnd, str):
#         '-no docstring-'
#         #return nret
#
#     def SendStringEx(self, hwnd, addr, len, type):
#         '-no docstring-'
#         #return nret
#
#     def KeyPressChar(self, keyStr):
#         '-no docstring-'
#         #return nret
#
#     def KeyDownChar(self, keyStr):
#         '-no docstring-'
#         #return nret
#
#     def KeyUpChar(self, keyStr):
#         '-no docstring-'
#         #return nret
#
#     def MoveR(self, rx, ry):
#         '-no docstring-'
#         #return nret
#
#     def MiddleClick(self):
#         '-no docstring-'
#         #return nret
#
#     def MiddleDoubleClick(self):
#         '-no docstring-'
#         #return nret
#
#     def MoveToEx(self, x, y, w, h):
#         '-no docstring-'
#         #return nret
#
#     def GetCursorPos(self):
#         '-no docstring-'
#         #return x, y, nret
#
#     def MiddleUp(self):
#         '-no docstring-'
#         #return nret
#
#     def MiddleDown(self):
#         '-no docstring-'
#         #return nret
#
#     def LeftClick(self):
#         '-no docstring-'
#         #return nret
#
#     def LeftDoubleClick(self):
#         '-no docstring-'
#         #return nret
#
#     def WheelUp(self):
#         '-no docstring-'
#         #return nret
#
#     def WheelDown(self):
#         '-no docstring-'
#         #return nret
#
#     def WaitKey(self, vk_code, time_out):
#         '-no docstring-'
#         #return nret
#
#     def EnableMouseAccuracy(self, enable):
#         '-no docstring-'
#         #return nret
#
#     def GenerateMouseTrajectory(self, startX, startY, endX, endY):
#         '-no docstring-'
#         #return nret
#
#     def GenerateInvoluteMouseTrajectory(self, startX, startY, radius, stepDistance, curvature, noiseAmplitude):
#         '-no docstring-'
#         #return nret
#
#     def LogShutdown(self, loggerHandle):
#         '-no docstring-'
#         #return nret
#
#     def LogSetFilePath(self, loggerHandle, logFilePath):
#         '-no docstring-'
#         #return nret
#
#     def LogSetPattern(self, loggerHandle, logPattern):
#         '-no docstring-'
#         #return nret
#
#     def LogSetMaxFileSize(self, loggerHandle, maxFileSizeMb):
#         '-no docstring-'
#         #return nret
#
#     def LogSetMaxFiles(self, loggerHandle, maxFiles):
#         '-no docstring-'
#         #return nret
#
#     def LogSetLevel(self, loggerHandle, level):
#         '-no docstring-'
#         #return nret
#
#     def LogGetLevel(self, loggerHandle):
#         '-no docstring-'
#         #return nret
#
#     def LogSetTarget(self, loggerHandle, targetFlags):
#         '-no docstring-'
#         #return nret
#
#     def LogSetAsync(self, loggerHandle, enableAsync):
#         '-no docstring-'
#         #return nret
#
#     def LogSetColorMode(self, loggerHandle, colorMode):
#         '-no docstring-'
#         #return nret
#
#     def LogSetLevelColor(self, loggerHandle, level, color):
#         '-no docstring-'
#         #return nret
#
#     def LogResetLevelColors(self, loggerHandle):
#         '-no docstring-'
#         #return nret
#
#     def LogSetFlushInterval(self, loggerHandle, flushIntervalSeconds):
#         '-no docstring-'
#         #return nret
#
#     def LogTrace(self, message):
#         '-no docstring-'
#         #return nret
#
#     def LogDebug(self, message):
#         '-no docstring-'
#         #return nret
#
#     def LogInfo(self, message):
#         '-no docstring-'
#         #return nret
#
#     def LogWarn(self, message):
#         '-no docstring-'
#         #return nret
#
#     def LogError(self, message):
#         '-no docstring-'
#         #return nret
#
#     def LogCritical(self, message):
#         '-no docstring-'
#         #return nret
#
#     def LogFlush(self, loggerHandle):
#         '-no docstring-'
#         #return nret
#
#     def LogCreateInstance(self, instanceName):
#         '-no docstring-'
#         #return nret
#
#     def LogDestroyInstance(self, loggerHandle):
#         '-no docstring-'
#         #return nret
#
#     def LogSetBaseDirectory(self, loggerHandle, baseDirectory):
#         '-no docstring-'
#         #return nret
#
#     def LogSetDirMode(self, loggerHandle, dirMode):
#         '-no docstring-'
#         #return nret
#
#     def LogSetModuleName(self, loggerHandle, moduleName):
#         '-no docstring-'
#         #return nret
#
#     def LogSetFileNamePattern(self, loggerHandle, fileNamePattern):
#         '-no docstring-'
#         #return nret
#
#     def LogSetRotationMode(self, loggerHandle, rotationMode):
#         '-no docstring-'
#         #return nret
#
#     def LogSetAppendMode(self, loggerHandle, enableAppend):
#         '-no docstring-'
#         #return nret
#
#     def LogTraceEx(self, loggerHandle, message):
#         '-no docstring-'
#         #return nret
#
#     def LogDebugEx(self, loggerHandle, message):
#         '-no docstring-'
#         #return nret
#
#     def LogInfoEx(self, loggerHandle, message):
#         '-no docstring-'
#         #return nret
#
#     def LogWarnEx(self, loggerHandle, message):
#         '-no docstring-'
#         #return nret
#
#     def LogErrorEx(self, loggerHandle, message):
#         '-no docstring-'
#         #return nret
#
#     def LogCriticalEx(self, loggerHandle, message):
#         '-no docstring-'
#         #return nret
#
#     def LogRotateFile(self, loggerHandle):
#         '-no docstring-'
#         #return nret
#
#     def LogCleanupOldFiles(self, loggerHandle, keepCount):
#         '-no docstring-'
#         #return nret
#
#     def LogGetCurrentFilePath(self, loggerHandle):
#         '-no docstring-'
#         #return nret
#
#     def LogGetCurrentFileSize(self, loggerHandle):
#         '-no docstring-'
#         #return nret
#
#     def LogGetTotalFilesCount(self, loggerHandle):
#         '-no docstring-'
#         #return nret
#
#     def CloseConsole(self, type):
#         '-no docstring-'
#         #return nret
#
#     def OpenConsole(self, type):
#         '-no docstring-'
#         #return nret
#
#     def DoubleToData(self, double_value):
#         '-no docstring-'
#         #return nret
#
#     def FloatToData(self, float_value):
#         '-no docstring-'
#         #return nret
#
#     def StringToData(self, string_value, type):
#         '-no docstring-'
#         #return nret
#
#     def Int64ToInt32(self, v):
#         '-no docstring-'
#         #return nret
#
#     def Int32ToInt64(self, v):
#         '-no docstring-'
#         #return nret
#
#     def FindData(self, hwnd, addr_range, data):
#         '-no docstring-'
#         #return nret
#
#     def FindDataEx(self, hwnd, addr_range, data, step, multi_thread, mode):
#         '-no docstring-'
#         #return nret
#
#     def FindDouble(self, hwnd, addr_range, double_value_min, double_value_max):
#         '-no docstring-'
#         #return nret
#
#     def FindDoubleEx(self, hwnd, addr_range, double_value_min, double_value_max, step, multi_thread, mode):
#         '-no docstring-'
#         #return nret
#
#     def FindFloat(self, hwnd, addr_range, float_value_min, float_value_max):
#         '-no docstring-'
#         #return nret
#
#     def FindFloatEx(self, hwnd, addr_range, float_value_min, float_value_max, step, multi_thread, mode):
#         '-no docstring-'
#         #return nret
#
#     def FindInt(self, hwnd, addr_range, int_value_min, int_value_max, type):
#         '-no docstring-'
#         #return nret
#
#     def FindIntEx(self, hwnd, addr_range, int_value_min, int_value_max, type, step, multi_thread, mode):
#         '-no docstring-'
#         #return nret
#
#     def FindString(self, hwnd, addr_range, string_value, type):
#         '-no docstring-'
#         #return nret
#
#     def FindStringEx(self, hwnd, addr_range, string_value, type, step, multi_thread, mode):
#         '-no docstring-'
#         #return nret
#
#     def ReadData(self, hwnd, addr, len):
#         '-no docstring-'
#         #return nret
#
#     def ReadDataToBin(self, hwnd, addr, len):
#         '-no docstring-'
#         #return nret
#
#     def ReadDataAddr(self, hwnd, addr, len):
#         '-no docstring-'
#         #return nret
#
#     def ReadDataAddrToBin(self, hwnd, addr, len):
#         '-no docstring-'
#         #return nret
#
#     def ReadDouble(self, hwnd, addr):
#         '-no docstring-'
#         #return nret
#
#     def ReadDoubleAddr(self, hwnd, addr):
#         '-no docstring-'
#         #return nret
#
#     def ReadFloat(self, hwnd, addr):
#         '-no docstring-'
#         #return nret
#
#     def ReadFloatAddr(self, hwnd, addr):
#         '-no docstring-'
#         #return nret
#
#     def ReadInt(self, hwnd, addr, type):
#         '-no docstring-'
#         #return nret
#
#     def ReadIntAddr(self, hwnd, addr, type):
#         '-no docstring-'
#         #return nret
#
#     def ReadString(self, hwnd, addr, type, len):
#         '-no docstring-'
#         #return nret
#
#     def ReadStringAddr(self, hwnd, addr, type, len):
#         '-no docstring-'
#         #return nret
#
#     def WriteData(self, hwnd, addr, data):
#         '-no docstring-'
#         #return nret
#
#     def WriteDataFromBin(self, hwnd, addr, data, len):
#         '-no docstring-'
#         #return nret
#
#     def WriteDataAddr(self, hwnd, addr, data):
#         '-no docstring-'
#         #return nret
#
#     def WriteDataAddrFromBin(self, hwnd, addr, data, len):
#         '-no docstring-'
#         #return nret
#
#     def WriteDouble(self, hwnd, addr, double_value):
#         '-no docstring-'
#         #return nret
#
#     def WriteDoubleAddr(self, hwnd, addr, double_value):
#         '-no docstring-'
#         #return nret
#
#     def WriteFloat(self, hwnd, addr, float_value):
#         '-no docstring-'
#         #return nret
#
#     def WriteFloatAddr(self, hwnd, addr, float_value):
#         '-no docstring-'
#         #return nret
#
#     def WriteInt(self, hwnd, addr, type, value):
#         '-no docstring-'
#         #return nret
#
#     def WriteIntAddr(self, hwnd, addr, type, value):
#         '-no docstring-'
#         #return nret
#
#     def WriteString(self, hwnd, addr, type, value):
#         '-no docstring-'
#         #return nret
#
#     def WriteStringAddr(self, hwnd, addr, type, value):
#         '-no docstring-'
#         #return nret
#
#     def SetMemoryHwndAsProcessId(self, enable):
#         '-no docstring-'
#         #return nret
#
#     def FreeProcessMemory(self, hwnd):
#         '-no docstring-'
#         #return nret
#
#     def GetModuleBaseAddr(self, hwnd, module_name):
#         '-no docstring-'
#         #return nret
#
#     def GetModuleSize(self, hwnd, module_name):
#         '-no docstring-'
#         #return nret
#
#     def GetRemoteApiAddress(self, hwnd, module_name, fun_name):
#         '-no docstring-'
#         #return nret
#
#     def VirtualAllocEx(self, hwnd, addr, size, type):
#         '-no docstring-'
#         #return nret
#
#     def VirtualFreeEx(self, hwnd, addr):
#         '-no docstring-'
#         #return nret
#
#     def VirtualProtectEx(self, hwnd, addr, size, newProtect):
#         '-no docstring-'
#         #return oldProtect, nret
#
#     def VirtualQueryEx(self, hwnd, addr, pmbi):
#         '-no docstring-'
#         #return nret
#
#     def CloseHandle(self, handle):
#         '-no docstring-'
#         #return nret
#
#     def CreateRemoteThread(self, hwnd, lpStartAddress, lpParameter, dwCreationFlags):
#         '-no docstring-'
#         #return lpThreadId, nret
#
#     def HookRemoteApi(self, hwnd, targetAddr, size, hook_proc):
#         '-no docstring-'
#         #return nret
#
#     def UnhookRemoteApi(self, hwnd, targetAddr):
#         '-no docstring-'
#         #return nret
#
#     def HttpDownloadFile(self, url, save_path, callback, user_data):
#         '-no docstring-'
#         #return nret
#
#     def HttpDownloadFileEx(self, url, save_path, callback, user_data, max_retries, connect_timeout_sec, read_timeout_sec):
#         '-no docstring-'
#         #return nret
#
#     def HttpGet(self, url):
#         '-no docstring-'
#         #return nret
#
#     def HttpPost(self, url, body, content_type):
#         '-no docstring-'
#         #return nret
#
#     def HttpRequestEx(self, method, url, headers, body, content_type):
#         '-no docstring-'
#         #return status_code, nret
#
#     def TcpClientCreate(self, callback, user_data, enable_packet_protocol):
#         '-no docstring-'
#         #return nret
#
#     def TcpClientConnect(self, client_handle, host, port):
#         '-no docstring-'
#         #return nret
#
#     def TcpClientSend(self, client_handle, data, data_len):
#         '-no docstring-'
#         #return nret
#
#     def TcpClientDisconnect(self, client_handle):
#         '-no docstring-'
#         #return nret
#
#     def TcpClientDestroy(self, client_handle):
#         '-no docstring-'
#         #return nret
#
#     def TcpServerCreate(self, bind_addr, port, callback, user_data, enable_packet_protocol):
#         '-no docstring-'
#         #return nret
#
#     def TcpServerSend(self, server_handle, conn_id, data, data_len):
#         '-no docstring-'
#         #return nret
#
#     def TcpServerDisconnect(self, server_handle, conn_id):
#         '-no docstring-'
#         #return nret
#
#     def TcpServerStop(self, server_handle):
#         '-no docstring-'
#         #return nret
#
#     def TcpServerDestroy(self, server_handle):
#         '-no docstring-'
#         #return nret
#
#     def TcpServerGetClientAddress(self, server_handle, conn_id):
#         '-no docstring-'
#         #return nret
#
#     def TcpServerGetAllConnectionIds(self, server_handle):
#         '-no docstring-'
#         #return nret
#
#     def Ocr(self, x1, y1, x2, y2):
#         '-no docstring-'
#         #return nret
#
#     def OcrFromPtr(self, ptr):
#         '-no docstring-'
#         #return nret
#
#     def OcrDetails(self, x1, y1, x2, y2):
#         '-no docstring-'
#         #return nret
#
#     def OcrFromPtrDetails(self, ptr):
#         '-no docstring-'
#         #return nret
#
#     def OcrFromBmpData(self, ptr, size):
#         '-no docstring-'
#         #return nret
#
#     def OcrFromBmpDataDetails(self, ptr, size):
#         '-no docstring-'
#         #return nret
#
#     def OcrV5(self, x1, y1, x2, y2):
#         '-no docstring-'
#         #return nret
#
#     def OcrV5Details(self, x1, y1, x2, y2):
#         '-no docstring-'
#         #return nret
#
#     def OcrV5FromPtr(self, ptr):
#         '-no docstring-'
#         #return nret
#
#     def OcrV5FromPtrDetails(self, ptr):
#         '-no docstring-'
#         #return nret
#
#     def OcrFromDict(self, x1, y1, x2, y2, colorJson, dict_name, matchVal):
#         '-no docstring-'
#         #return nret
#
#     def OcrFromDictDetails(self, x1, y1, x2, y2, colorJson, dict_name, matchVal):
#         '-no docstring-'
#         #return nret
#
#     def OcrFromDictPtr(self, ptr, colorJson, dict_name, matchVal):
#         '-no docstring-'
#         #return nret
#
#     def OcrFromDictPtrDetails(self, ptr, colorJson, dict_name, matchVal):
#         '-no docstring-'
#         #return nret
#
#     def SetOcrConfigByKey(self, key, value):
#         '-no docstring-'
#         #return nret
#
#     def SetOcrConfig(self, configStr):
#         '-no docstring-'
#         #return nret
#
#     def GetOcrConfig(self, configKey):
#         '-no docstring-'
#         #return nret
#
#     def FindStr(self, x1, y1, x2, y2, str, colorJson, dict, matchVal):
#         '-no docstring-'
#         #return outX, outY, nret
#
#     def FindStrDetail(self, x1, y1, x2, y2, str, colorJson, dict, matchVal):
#         '-no docstring-'
#         #return nret
#
#     def FindStrAll(self, x1, y1, x2, y2, str, colorJson, dict, matchVal):
#         '-no docstring-'
#         #return nret
#
#     def FindStrFromPtr(self, source, str, colorJson, dict, matchVal):
#         '-no docstring-'
#         #return nret
#
#     def FindStrFromPtrAll(self, source, str, colorJson, dict, matchVal):
#         '-no docstring-'
#         #return nret
#
#     def FastNumberOcr(self, x1, y1, x2, y2, numbers, colorJson, matchVal):
#         '-no docstring-'
#         #return nret
#
#     def FastNumberOcrFromPtr(self, source, numbers, colorJson, matchVal):
#         '-no docstring-'
#         #return nret
#
#     def ImportTxtDict(self, dictName, dictPath):
#         '-no docstring-'
#         #return nret
#
#     def ExportTxtDict(self, dictName, dictPath):
#         '-no docstring-'
#         #return nret
#
#     def Capture(self, x1, y1, x2, y2, file):
#         '-no docstring-'
#         #return nret
#
#     def GetScreenDataBmp(self, x1, y1, x2, y2):
#         '-no docstring-'
#         #return data, dataLen, nret
#
#     def GetScreenData(self, x1, y1, x2, y2):
#         '-no docstring-'
#         #return data, dataLen, stride, nret
#
#     def GetScreenDataPtr(self, x1, y1, x2, y2):
#         '-no docstring-'
#         #return nret
#
#     def CaptureGif(self, x1, y1, x2, y2, file, delay, time):
#         '-no docstring-'
#         #return nret
#
#     def LockDisplay(self, enable):
#         '-no docstring-'
#         #return nret
#
#     def SetSnapCacheTime(self, cacheTime):
#         '-no docstring-'
#         #return nret
#
#     def GetImageData(self, imgPtr):
#         '-no docstring-'
#         #return data, size, stride, nret
#
#     def MatchImageFromPath(self, source, templ, matchVal, type, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def MatchImageFromPathAll(self, source, templ, matchVal, type, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def MatchImagePtrFromPath(self, source, templ, matchVal, type, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def MatchImagePtrFromPathAll(self, source, templ, matchVal, type, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def GetColor(self, x, y):
#         '-no docstring-'
#         #return nret
#
#     def GetColorPtr(self, source, x, y):
#         '-no docstring-'
#         #return nret
#
#     def CopyImage(self, sourcePtr):
#         '-no docstring-'
#         #return nret
#
#     def FreeImageAll(self):
#         '-no docstring-'
#         #return nret
#
#     def FreeImagePath(self, path):
#         '-no docstring-'
#         #return nret
#
#     def LoadImage(self, path):
#         '-no docstring-'
#         #return nret
#
#     def LoadImageFromBmpData(self, data, dataSize):
#         '-no docstring-'
#         #return nret
#
#     def LoadImageFromRGBData(self, width, height, scan0, stride):
#         '-no docstring-'
#         #return nret
#
#     def FreeImagePtr(self, screenPtr):
#         '-no docstring-'
#         #return nret
#
#     def MatchWindowsFromPtr(self, x1, y1, x2, y2, templ, matchVal, type, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def MatchImageFromPtr(self, source, templ, matchVal, type, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def MatchImageFromPtrAll(self, source, templ, matchVal, type, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def MatchWindowsFromPtrAll(self, x1, y1, x2, y2, templ, matchVal, type, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def MatchWindowsFromPath(self, x1, y1, x2, y2, templ, matchVal, type, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def MatchWindowsFromPathAll(self, x1, y1, x2, y2, templ, matchVal, type, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def MatchWindowsThresholdFromPtr(self, x1, y1, x2, y2, colorJson, templ, matchVal, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def MatchWindowsThresholdFromPtrAll(self, x1, y1, x2, y2, colorJson, templ, matchVal, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def MatchWindowsThresholdFromPath(self, x1, y1, x2, y2, colorJson, templ, matchVal, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def MatchWindowsThresholdFromPathAll(self, x1, y1, x2, y2, colorJson, templ, matchVal, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def ShowMatchWindow(self, flag):
#         '-no docstring-'
#         #return nret
#
#     def CalculateSSIM(self, image1, image2):
#         '-no docstring-'
#         #return nret
#
#     def CalculateHistograms(self, image1, image2):
#         '-no docstring-'
#         #return nret
#
#     def CalculateMSE(self, image1, image2):
#         '-no docstring-'
#         #return nret
#
#     def SaveImageFromPtr(self, ptr, path):
#         '-no docstring-'
#         #return nret
#
#     def ReSize(self, ptr, width, height):
#         '-no docstring-'
#         #return nret
#
#     def FindColor(self, x1, y1, x2, y2, color1, color2, dir):
#         '-no docstring-'
#         #return x, y, nret
#
#     def FindColorList(self, x1, y1, x2, y2, color1, color2):
#         '-no docstring-'
#         #return nret
#
#     def FindColorEx(self, x1, y1, x2, y2, colorJson, dir):
#         '-no docstring-'
#         #return x, y, nret
#
#     def FindColorListEx(self, x1, y1, x2, y2, colorJson):
#         '-no docstring-'
#         #return nret
#
#     def FindMultiColor(self, x1, y1, x2, y2, colorJson, pointJson, sim, dir):
#         '-no docstring-'
#         #return x, y, nret
#
#     def FindMultiColorList(self, x1, y1, x2, y2, colorJson, pointJson, sim):
#         '-no docstring-'
#         #return nret
#
#     def FindMultiColorFromPtr(self, ptr, colorJson, pointJson, sim, dir):
#         '-no docstring-'
#         #return x, y, nret
#
#     def FindMultiColorListFromPtr(self, ptr, colorJson, pointJson, sim):
#         '-no docstring-'
#         #return nret
#
#     def GetImageSize(self, ptr):
#         '-no docstring-'
#         #return width, height, nret
#
#     def FindColorBlock(self, x1, y1, x2, y2, colorList, count, width, height):
#         '-no docstring-'
#         #return x, y, nret
#
#     def FindColorBlockPtr(self, ptr, colorList, count, width, height):
#         '-no docstring-'
#         #return x, y, nret
#
#     def FindColorBlockList(self, x1, y1, x2, y2, colorList, count, width, height, type):
#         '-no docstring-'
#         #return nret
#
#     def FindColorBlockListPtr(self, ptr, colorList, count, width, height, type):
#         '-no docstring-'
#         #return nret
#
#     def FindColorBlockEx(self, x1, y1, x2, y2, colorList, count, width, height, dir):
#         '-no docstring-'
#         #return x, y, nret
#
#     def FindColorBlockPtrEx(self, ptr, colorList, count, width, height, dir):
#         '-no docstring-'
#         #return x, y, nret
#
#     def FindColorBlockListEx(self, x1, y1, x2, y2, colorList, count, width, height, type, dir):
#         '-no docstring-'
#         #return nret
#
#     def FindColorBlockListPtrEx(self, ptr, colorList, count, width, height, type, dir):
#         '-no docstring-'
#         #return nret
#
#     def GetColorNum(self, x1, y1, x2, y2, colorList):
#         '-no docstring-'
#         #return nret
#
#     def GetColorNumPtr(self, ptr, colorList):
#         '-no docstring-'
#         #return nret
#
#     def Cropped(self, image, x1, y1, x2, y2):
#         '-no docstring-'
#         #return nret
#
#     def GetThresholdImageFromMultiColorPtr(self, ptr, colorJson):
#         '-no docstring-'
#         #return nret
#
#     def GetThresholdImageFromMultiColor(self, x1, y1, x2, y2, colorJson):
#         '-no docstring-'
#         #return nret
#
#     def IsSameImage(self, ptr, ptr2):
#         '-no docstring-'
#         #return nret
#
#     def ShowImage(self, ptr):
#         '-no docstring-'
#         #return nret
#
#     def ShowImageFromFile(self, file):
#         '-no docstring-'
#         #return nret
#
#     def SetColorsToNewColor(self, ptr, colorJson, color):
#         '-no docstring-'
#         #return nret
#
#     def RemoveOtherColors(self, ptr, colorJson):
#         '-no docstring-'
#         #return nret
#
#     def DrawRectangle(self, ptr, x1, y1, x2, y2, thickness, color):
#         '-no docstring-'
#         #return nret
#
#     def DrawCircle(self, ptr, x, y, radius, thickness, color):
#         '-no docstring-'
#         #return nret
#
#     def DrawFillPoly(self, ptr, pointJson, color):
#         '-no docstring-'
#         #return nret
#
#     def DecodeQRCode(self, ptr):
#         '-no docstring-'
#         #return nret
#
#     def CreateQRCode(self, str, pixelsPerModule):
#         '-no docstring-'
#         #return nret
#
#     def CreateQRCodeEx(self, str, pixelsPerModule, version, correction_level, mode, structure_number):
#         '-no docstring-'
#         #return nret
#
#     def MatchAnimationFromPtr(self, x1, y1, x2, y2, templ, matchVal, type, angle, scale, delay, time, threadCount):
#         '-no docstring-'
#         #return nret
#
#     def MatchAnimationFromPath(self, x1, y1, x2, y2, templ, matchVal, type, angle, scale, delay, time, threadCount):
#         '-no docstring-'
#         #return nret
#
#     def RemoveImageDiff(self, image1, image2):
#         '-no docstring-'
#         #return nret
#
#     def GetImageBmpData(self, imgPtr):
#         '-no docstring-'
#         #return data, size, nret
#
#     def FreeImageData(self, screenPtr):
#         '-no docstring-'
#         #return nret
#
#     def ScalePixels(self, ptr, pixelsPerModule):
#         '-no docstring-'
#         #return nret
#
#     def CreateImage(self, width, height, color):
#         '-no docstring-'
#         #return nret
#
#     def SetPixel(self, image, x, y, color):
#         '-no docstring-'
#         #return nret
#
#     def SetPixelList(self, image, points, color):
#         '-no docstring-'
#         #return nret
#
#     def ConcatImage(self, image1, image2, gap, color, dir):
#         '-no docstring-'
#         #return nret
#
#     def CoverImage(self, image1, image2, x, y, alpha):
#         '-no docstring-'
#         #return nret
#
#     def RotateImage(self, image, angle):
#         '-no docstring-'
#         #return nret
#
#     def ImageToBase64(self, image):
#         '-no docstring-'
#         #return nret
#
#     def Base64ToImage(self, base64):
#         '-no docstring-'
#         #return nret
#
#     def Hex2ARGB(self, hex):
#         '-no docstring-'
#         #return a, r, g, b, nret
#
#     def Hex2RGB(self, hex):
#         '-no docstring-'
#         #return r, g, b, nret
#
#     def ARGB2Hex(self, a, r, g, b):
#         '-no docstring-'
#         #return nret
#
#     def RGB2Hex(self, r, g, b):
#         '-no docstring-'
#         #return nret
#
#     def CmpColor(self, x1, y1, colorStart, colorEnd):
#         '-no docstring-'
#         #return nret
#
#     def CmpColorPtr(self, ptr, x, y, colorStart, colorEnd):
#         '-no docstring-'
#         #return nret
#
#     def CmpColorHex(self, hex, colorStart, colorEnd):
#         '-no docstring-'
#         #return nret
#
#     def CmpMultiColor(self, pointJson, sim):
#         '-no docstring-'
#         #return nret
#
#     def CmpMultiColorPtr(self, image, pointJson, sim):
#         '-no docstring-'
#         #return nret
#
#     def GetConnectedComponents(self, ptr, points, tolerance):
#         '-no docstring-'
#         #return nret
#
#     def DetectPointerDirection(self, ptr, x, y):
#         '-no docstring-'
#         #return nret
#
#     def DetectPointerDirectionByFeatures(self, ptr, templatePtr, x, y, useTemplate):
#         '-no docstring-'
#         #return nret
#
#     def FastMatch(self, ptr, templatePtr, matchVal, type, angle, scale):
#         '-no docstring-'
#         #return nret
#
#     def GetROIRegion(self, ptr):
#         '-no docstring-'
#         #return x1, y1, x2, y2, nret
#
#     def FastROI(self, ptr):
#         '-no docstring-'
#         #return nret
#
#     def Hex2HSV(self, hex):
#         '-no docstring-'
#         #return nret
#
#     def RGB2HSV(self, r, g, b):
#         '-no docstring-'
#         #return nret
#
#     def GetForegroundPoints(self, ptr):
#         '-no docstring-'
#         #return nret
#
#     def ConvertColor(self, ptr, type):
#         '-no docstring-'
#         #return nret
#
#     def Threshold(self, ptr, thresh, maxVal, type):
#         '-no docstring-'
#         #return nret
#
#     def RemoveIslands(self, ptr, minArea):
#         '-no docstring-'
#         #return nret
#
#     def MorphGradient(self, ptr, kernelSize):
#         '-no docstring-'
#         #return nret
#
#     def ImageStitchFromPath(self, path):
#         '-no docstring-'
#         #return trajectory, nret
#
#     def ImageStitchCreate(self):
#         '-no docstring-'
#         #return nret
#
#     def ImageStitchFree(self, imageStitch):
#         '-no docstring-'
#         #return nret
#
#     def ImageStitchAppend(self, imageStitch, image):
#         '-no docstring-'
#         #return nret
#
#     def ImageStitchGetResult(self, imageStitch):
#         '-no docstring-'
#         #return trajectory, nret
#
#     def MorphTophat(self, ptr, kernelSize):
#         '-no docstring-'
#         #return nret
#
#     def MorphBlackhat(self, ptr, kernelSize):
#         '-no docstring-'
#         #return nret
#
#     def Dilation(self, ptr, kernelSize):
#         '-no docstring-'
#         #return nret
#
#     def Erosion(self, ptr, kernelSize):
#         '-no docstring-'
#         #return nret
#
#     def GaussianBlur(self, ptr, kernelSize):
#         '-no docstring-'
#         #return nret
#
#     def Sharpen(self, ptr):
#         '-no docstring-'
#         #return nret
#
#     def CannyEdge(self, ptr, kernelSize):
#         '-no docstring-'
#         #return nret
#
#     def Flip(self, ptr, flipCode):
#         '-no docstring-'
#         #return nret
#
#     def MorphOpen(self, ptr, kernelSize):
#         '-no docstring-'
#         #return nret
#
#     def MorphClose(self, ptr, kernelSize):
#         '-no docstring-'
#         #return nret
#
#     def Skeletonize(self, ptr):
#         '-no docstring-'
#         #return nret
#
#     def GetImagePngData(self, imgPtr):
#         '-no docstring-'
#         #return data, size, nret
#
#     def CmpColorEx(self, x1, y1, colorJson):
#         '-no docstring-'
#         #return nret
#
#     def CmpColorPtrEx(self, ptr, x, y, colorJson):
#         '-no docstring-'
#         #return nret
#
#     def CmpColorHexEx(self, hex, colorJson):
#         '-no docstring-'
#         #return nret
#
#     def BitPacking(self, image):
#         '-no docstring-'
#         #return nret
#
#     def BitUnpacking(self, imageStr):
#         '-no docstring-'
#         #return nret
#
#     def SetImageCache(self, enable):
#         '-no docstring-'
#         #return nret
#
#     def FindImageFromPtr(self, source, templ, deltaColor, matchVal, dir):
#         '-no docstring-'
#         #return nret
#
#     def FindImageFromPtrAll(self, source, templ, deltaColor, matchVal):
#         '-no docstring-'
#         #return nret
#
#     def FindImageFromPath(self, source, templ, deltaColor, matchVal, dir):
#         '-no docstring-'
#         #return nret
#
#     def FindImageFromPathAll(self, source, templ, deltaColor, matchVal):
#         '-no docstring-'
#         #return nret
#
#     def FindWindowsFromPtr(self, x1, y1, x2, y2, templ, deltaColor, matchVal, dir):
#         '-no docstring-'
#         #return nret
#
#     def FindWindowsFromPtrAll(self, x1, y1, x2, y2, templ, deltaColor, matchVal):
#         '-no docstring-'
#         #return nret
#
#     def FindWindowsFromPath(self, x1, y1, x2, y2, templ, deltaColor, matchVal, dir):
#         '-no docstring-'
#         #return nret
#
#     def FindWindowsFromPathAll(self, x1, y1, x2, y2, templ, deltaColor, matchVal):
#         '-no docstring-'
#         #return nret
#
#     def RegistryOpenKey(self, rootKey, subKey):
#         '-no docstring-'
#         #return nret
#
#     def RegistryCreateKey(self, rootKey, subKey):
#         '-no docstring-'
#         #return nret
#
#     def RegistryCloseKey(self, key):
#         '-no docstring-'
#         #return nret
#
#     def RegistryKeyExists(self, rootKey, subKey):
#         '-no docstring-'
#         #return nret
#
#     def RegistryDeleteKey(self, rootKey, subKey, recursive):
#         '-no docstring-'
#         #return nret
#
#     def RegistrySetString(self, key, valueName, value):
#         '-no docstring-'
#         #return nret
#
#     def RegistryGetString(self, key, valueName):
#         '-no docstring-'
#         #return nret
#
#     def RegistrySetDword(self, key, valueName, value):
#         '-no docstring-'
#         #return nret
#
#     def RegistryGetDword(self, key, valueName):
#         '-no docstring-'
#         #return nret
#
#     def RegistrySetQword(self, key, valueName, value):
#         '-no docstring-'
#         #return nret
#
#     def RegistryGetQword(self, key, valueName):
#         '-no docstring-'
#         #return nret
#
#     def RegistryDeleteValue(self, key, valueName):
#         '-no docstring-'
#         #return nret
#
#     def RegistryEnumSubKeys(self, key):
#         '-no docstring-'
#         #return nret
#
#     def RegistryEnumValues(self, key):
#         '-no docstring-'
#         #return nret
#
#     def RegistrySetEnvironmentVariable(self, name, value, systemWide):
#         '-no docstring-'
#         #return nret
#
#     def RegistryGetEnvironmentVariable(self, name, systemWide):
#         '-no docstring-'
#         #return nret
#
#     def RegistryGetUserRegistryPath(self):
#         '-no docstring-'
#         #return nret
#
#     def RegistryGetSystemRegistryPath(self):
#         '-no docstring-'
#         #return nret
#
#     def RegistryBackupToFile(self, rootKey, subKey, filePath):
#         '-no docstring-'
#         #return nret
#
#     def RegistryRestoreFromFile(self, filePath):
#         '-no docstring-'
#         #return nret
#
#     def RegistryCompareKeys(self, rootKey1, subKey1, rootKey2, subKey2):
#         '-no docstring-'
#         #return nret
#
#     def RegistrySearchKeys(self, rootKey, searchPath, searchPattern, recursive):
#         '-no docstring-'
#         #return nret
#
#     def RegistryGetInstalledSoftware(self):
#         '-no docstring-'
#         #return nret
#
#     def RegistryGetWindowsVersion(self):
#         '-no docstring-'
#         #return nret
#
#     def OpenDatabase(self, dbName, password):
#         '-no docstring-'
#         #return nret
#
#     def OpenMemoryDatabase(self, address, size, password):
#         '-no docstring-'
#         #return nret
#
#     def GetDatabaseError(self, db):
#         '-no docstring-'
#         #return nret
#
#     def CloseDatabase(self, db):
#         '-no docstring-'
#         #return nret
#
#     def GetAllTableNames(self, db):
#         '-no docstring-'
#         #return nret
#
#     def GetTableInfo(self, db, tableName):
#         '-no docstring-'
#         #return nret
#
#     def GetTableInfoDetail(self, db, tableName):
#         '-no docstring-'
#         #return nret
#
#     def ExecuteSql(self, db, sql):
#         '-no docstring-'
#         #return nret
#
#     def ExecuteScalar(self, db, sql):
#         '-no docstring-'
#         #return nret
#
#     def ExecuteReader(self, db, sql):
#         '-no docstring-'
#         #return nret
#
#     def Read(self, stmt):
#         '-no docstring-'
#         #return nret
#
#     def GetDataCount(self, stmt):
#         '-no docstring-'
#         #return nret
#
#     def GetColumnCount(self, stmt):
#         '-no docstring-'
#         #return nret
#
#     def GetColumnName(self, stmt, iCol):
#         '-no docstring-'
#         #return nret
#
#     def GetColumnIndex(self, stmt, columnName):
#         '-no docstring-'
#         #return nret
#
#     def GetColumnType(self, stmt, iCol):
#         '-no docstring-'
#         #return nret
#
#     def Finalize(self, stmt):
#         '-no docstring-'
#         #return nret
#
#     def GetDouble(self, stmt, iCol):
#         '-no docstring-'
#         #return nret
#
#     def GetInt32(self, stmt, iCol):
#         '-no docstring-'
#         #return nret
#
#     def GetInt64(self, stmt, iCol):
#         '-no docstring-'
#         #return nret
#
#     def GetString(self, stmt, iCol):
#         '-no docstring-'
#         #return nret
#
#     def GetDoubleByColumnName(self, stmt, columnName):
#         '-no docstring-'
#         #return nret
#
#     def GetInt32ByColumnName(self, stmt, columnName):
#         '-no docstring-'
#         #return nret
#
#     def GetInt64ByColumnName(self, stmt, columnName):
#         '-no docstring-'
#         #return nret
#
#     def GetStringByColumnName(self, stmt, columnName):
#         '-no docstring-'
#         #return nret
#
#     def InitOlaDatabase(self, db):
#         '-no docstring-'
#         #return nret
#
#     def InitOlaImageFromDir(self, db, dir, cover):
#         '-no docstring-'
#         #return nret
#
#     def RemoveOlaImageFromDir(self, db, dir):
#         '-no docstring-'
#         #return nret
#
#     def ExportOlaImageDir(self, db, dir, exportDir):
#         '-no docstring-'
#         #return nret
#
#     def ImportOlaImage(self, db, dir, fileName, cover):
#         '-no docstring-'
#         #return nret
#
#     def GetOlaImage(self, db, dir, fileName):
#         '-no docstring-'
#         #return nret
#
#     def RemoveOlaImage(self, db, dir, fileName):
#         '-no docstring-'
#         #return nret
#
#     def SetDbConfig(self, db, key, value):
#         '-no docstring-'
#         #return nret
#
#     def GetDbConfig(self, db, key):
#         '-no docstring-'
#         #return nret
#
#     def RemoveDbConfig(self, db, key):
#         '-no docstring-'
#         #return nret
#
#     def SetDbConfigEx(self, key, value):
#         '-no docstring-'
#         #return nret
#
#     def GetDbConfigEx(self, key):
#         '-no docstring-'
#         #return nret
#
#     def RemoveDbConfigEx(self, key):
#         '-no docstring-'
#         #return nret
#
#     def InitDictFromDir(self, db, dict_name, dict_path, cover):
#         '-no docstring-'
#         #return nret
#
#     def ImportDictWord(self, db, dict_name, pic_file_name, cover):
#         '-no docstring-'
#         #return nret
#
#     def ExportDict(self, db, dict_name, export_dir):
#         '-no docstring-'
#         #return nret
#
#     def RemoveDict(self, db, dict_name):
#         '-no docstring-'
#         #return nret
#
#     def RemoveDictWord(self, db, dict_name, word):
#         '-no docstring-'
#         #return nret
#
#     def GetDictImage(self, db, dict_name, word, gap, dir):
#         '-no docstring-'
#         #return nret
#
#     def CreateDatabase(self, dbName, password):
#         '-no docstring-'
#         #return nret
#
#     def InitDictFromTxt(self, db, dict_name, dict_path, cover):
#         '-no docstring-'
#         #return nret
#
#     def OpenVideo(self, videoPath):
#         '-no docstring-'
#         #return nret
#
#     def OpenCamera(self, deviceIndex):
#         '-no docstring-'
#         #return nret
#
#     def CloseVideo(self, videoHandle):
#         '-no docstring-'
#         #return nret
#
#     def IsVideoOpened(self, videoHandle):
#         '-no docstring-'
#         #return nret
#
#     def GetVideoInfo(self, videoHandle):
#         '-no docstring-'
#         #return nret
#
#     def GetVideoWidth(self, videoHandle):
#         '-no docstring-'
#         #return nret
#
#     def GetVideoHeight(self, videoHandle):
#         '-no docstring-'
#         #return nret
#
#     def GetVideoFPS(self, videoHandle):
#         '-no docstring-'
#         #return nret
#
#     def GetVideoTotalFrames(self, videoHandle):
#         '-no docstring-'
#         #return nret
#
#     def GetVideoDuration(self, videoHandle):
#         '-no docstring-'
#         #return nret
#
#     def GetCurrentFrameIndex(self, videoHandle):
#         '-no docstring-'
#         #return nret
#
#     def GetCurrentTimestamp(self, videoHandle):
#         '-no docstring-'
#         #return nret
#
#     def ReadNextFrame(self, videoHandle):
#         '-no docstring-'
#         #return nret
#
#     def ReadFrameAtIndex(self, videoHandle, frameIndex):
#         '-no docstring-'
#         #return nret
#
#     def ReadFrameAtTime(self, videoHandle, timestamp):
#         '-no docstring-'
#         #return nret
#
#     def ReadCurrentFrame(self, videoHandle):
#         '-no docstring-'
#         #return nret
#
#     def SeekToFrame(self, videoHandle, frameIndex):
#         '-no docstring-'
#         #return nret
#
#     def SeekToTime(self, videoHandle, timestamp):
#         '-no docstring-'
#         #return nret
#
#     def SeekToBeginning(self, videoHandle):
#         '-no docstring-'
#         #return nret
#
#     def SeekToEnd(self, videoHandle):
#         '-no docstring-'
#         #return nret
#
#     def ExtractFramesToFiles(self, videoHandle, startFrame, endFrame, step, outputDir, imageFormat, jpegQuality):
#         '-no docstring-'
#         #return nret
#
#     def ExtractFramesByInterval(self, videoHandle, intervalSeconds, outputDir, imageFormat):
#         '-no docstring-'
#         #return nret
#
#     def ExtractKeyFrames(self, videoHandle, Threshold, maxFrames, outputDir, imageFormat):
#         '-no docstring-'
#         #return nret
#
#     def SaveCurrentFrame(self, videoHandle, outputPath, quality):
#         '-no docstring-'
#         #return nret
#
#     def SaveFrameAtIndex(self, videoHandle, frameIndex, outputPath, quality):
#         '-no docstring-'
#         #return nret
#
#     def FrameToBase64(self, videoHandle, format):
#         '-no docstring-'
#         #return nret
#
#     def CalculateFrameSimilarity(self, frame1, frame2):
#         '-no docstring-'
#         #return nret
#
#     def GetVideoInfoFromPath(self, videoPath):
#         '-no docstring-'
#         #return nret
#
#     def IsValidVideoFile(self, videoPath):
#         '-no docstring-'
#         #return nret
#
#     def ExtractSingleFrame(self, videoPath, frameIndex):
#         '-no docstring-'
#         #return nret
#
#     def ExtractThumbnail(self, videoPath):
#         '-no docstring-'
#         #return nret
#
#     def ConvertVideo(self, inputPath, outputPath, codec, fps):
#         '-no docstring-'
#         #return nret
#
#     def ResizeVideo(self, inputPath, outputPath, width, height):
#         '-no docstring-'
#         #return nret
#
#     def TrimVideo(self, inputPath, outputPath, startTime, endTime):
#         '-no docstring-'
#         #return nret
#
#     def CreateVideoFromImages(self, imageDir, outputPath, fps, codec):
#         '-no docstring-'
#         #return nret
#
#     def DetectSceneChanges(self, videoPath, Threshold):
#         '-no docstring-'
#         #return nret
#
#     def CalculateAverageBrightness(self, videoPath):
#         '-no docstring-'
#         #return nret
#
#     def DetectMotion(self, videoPath, Threshold):
#         '-no docstring-'
#         #return nret
#
#     def SetWindowState(self, hwnd, state):
#         '-no docstring-'
#         #return nret
#
#     def FindWindow(self, class_name, title):
#         '-no docstring-'
#         #return nret
#
#     def GetClipboard(self):
#         '-no docstring-'
#         #return nret
#
#     def SetClipboard(self, text):
#         '-no docstring-'
#         #return nret
#
#     def SendPaste(self, hwnd):
#         '-no docstring-'
#         #return nret
#
#     def GetWindow(self, hwnd, flag):
#         '-no docstring-'
#         #return nret
#
#     def GetWindowTitle(self, hwnd):
#         '-no docstring-'
#         #return nret
#
#     def GetWindowClass(self, hwnd):
#         '-no docstring-'
#         #return nret
#
#     def GetWindowRect(self, hwnd):
#         '-no docstring-'
#         #return x1, y1, x2, y2, nret
#
#     def GetWindowProcessPath(self, hwnd):
#         '-no docstring-'
#         #return nret
#
#     def GetWindowState(self, hwnd, flag):
#         '-no docstring-'
#         #return nret
#
#     def GetForegroundWindow(self):
#         '-no docstring-'
#         #return nret
#
#     def GetWindowProcessId(self, hwnd):
#         '-no docstring-'
#         #return nret
#
#     def GetClientSize(self, hwnd):
#         '-no docstring-'
#         #return width, height, nret
#
#     def GetMousePointWindow(self):
#         '-no docstring-'
#         #return nret
#
#     def GetSpecialWindow(self, flag):
#         '-no docstring-'
#         #return nret
#
#     def GetClientRect(self, hwnd):
#         '-no docstring-'
#         #return x1, y1, x2, y2, nret
#
#     def SetWindowText(self, hwnd, title):
#         '-no docstring-'
#         #return nret
#
#     def SetWindowSize(self, hwnd, width, height):
#         '-no docstring-'
#         #return nret
#
#     def SetClientSize(self, hwnd, width, height):
#         '-no docstring-'
#         #return nret
#
#     def SetWindowTransparent(self, hwnd, alpha):
#         '-no docstring-'
#         #return nret
#
#     def FindWindowEx(self, parent, class_name, title):
#         '-no docstring-'
#         #return nret
#
#     def FindWindowByProcess(self, process_name, class_name, title):
#         '-no docstring-'
#         #return nret
#
#     def MoveWindow(self, hwnd, x, y):
#         '-no docstring-'
#         #return nret
#
#     def GetScaleFromWindows(self, hwnd):
#         '-no docstring-'
#         #return nret
#
#     def GetWindowDpiAwarenessScale(self, hwnd):
#         '-no docstring-'
#         #return nret
#
#     def EnumProcess(self, name):
#         '-no docstring-'
#         #return nret
#
#     def EnumWindow(self, parent, title, className, filter):
#         '-no docstring-'
#         #return nret
#
#     def EnumWindowByProcess(self, process_name, title, class_name, filter):
#         '-no docstring-'
#         #return nret
#
#     def EnumWindowByProcessId(self, pid, title, class_name, filter):
#         '-no docstring-'
#         #return nret
#
#     def EnumWindowSuper(self, spec1, flag1, type1, spec2, flag2, type2, sort):
#         '-no docstring-'
#         #return nret
#
#     def GetPointWindow(self, x, y):
#         '-no docstring-'
#         #return nret
#
#     def GetProcessInfo(self, pid):
#         '-no docstring-'
#         #return nret
#
#     def ShowTaskBarIcon(self, hwnd, show):
#         '-no docstring-'
#         #return nret
#
#     def FindWindowByProcessId(self, process_id, className, title):
#         '-no docstring-'
#         #return nret
#
#     def GetWindowThreadId(self, hwnd):
#         '-no docstring-'
#         #return nret
#
#     def FindWindowSuper(self, spec1, flag1, type1, spec2, flag2, type2):
#         '-no docstring-'
#         #return nret
#
#     def ClientToScreen(self, hwnd):
#         '-no docstring-'
#         #return x, y, nret
#
#     def ScreenToClient(self, hwnd):
#         '-no docstring-'
#         #return x, y, nret
#
#     def GetForegroundFocus(self):
#         '-no docstring-'
#         #return nret
#
#     def SetWindowDisplay(self, hwnd, affinity):
#         '-no docstring-'
#         #return nret
#
#     def IsDisplayDead(self, x1, y1, x2, y2, time):
#         '-no docstring-'
#         #return nret
#
#     def GetWindowsFps(self, x1, y1, x2, y2):
#         '-no docstring-'
#         #return nret
#
#     def SetFontSmooth(self, enable):
#         '-no docstring-'
#         #return nret
#
#     def CheckFontSmooth(self):
#         '-no docstring-'
#         #return nret
#
#     def GetCommandLine(self, hwnd):
#         '-no docstring-'
#         #return nret
#
#     def TerminateProcess(self, pid):
#         '-no docstring-'
#         #return nret
#
#     def TerminateProcessTree(self, pid):
#         '-no docstring-'
#         #return nret
#
#     def EnableDebugPrivilege(self):
#         '-no docstring-'
#         #return nret
#
#     def SystemStart(self, applicationName, commandLine):
#         '-no docstring-'
#         #return nret
#
#     def CreateChildProcess(self, applicationName, commandLine, currentDirectory, showType, parentProcessId):
#         '-no docstring-'
#         #return nret
#
#     def GetProcessIconImage(self, pid, targetWidth, targetHeight):
#         '-no docstring-'
#         #return nret
#
#     def XmlCreateDocument(self):
#         '-no docstring-'
#         #return nret
#
#     def XmlParse(self, str):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlParseFile(self, filePath):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlToString(self, doc, compact):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlSaveToFile(self, doc, filePath, compact):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlFree(self, doc):
#         '-no docstring-'
#         #return nret
#
#     def XmlGetRootElement(self, doc):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlCreateElement(self, doc, name):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlInsertRootElement(self, doc, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlAppendChild(self, parent, child):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetFirstChild(self, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetNextSibling(self, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlFindElement(self, parent, name):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetElementName(self, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetElementText(self, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlSetElementText(self, element, text):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlRemoveChild(self, parent, child):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlInsertBefore(self, parent, newChild, refChild):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlInsertAfter(self, parent, newChild, refChild):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetParent(self, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetPreviousSibling(self, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetLastChild(self, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlCloneElement(self, doc, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlHasChildren(self, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetAttribute(self, element, name):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlSetAttribute(self, element, name, value):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetAttributeInt(self, element, name):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlSetAttributeInt(self, element, name, value):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetAttributeDouble(self, element, name):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlSetAttributeDouble(self, element, name, value):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetAttributeBool(self, element, name):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlSetAttributeBool(self, element, name, value):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetAttributeInt64(self, element, name):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlSetAttributeInt64(self, element, name, value):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlHasAttribute(self, element, name):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetAttributeNames(self, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetAttributeCount(self, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlDeleteAttribute(self, element, name):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlSetCDATA(self, doc, element, content):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlAddComment(self, doc, element, comment):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlSetDeclaration(self, doc, version, encoding, standalone):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlQueryElement(self, doc, path):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetChildCount(self, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetChildCountByName(self, parent, name):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetChildByIndex(self, parent, index):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetChildByNameAndIndex(self, parent, name, index):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlFindElementByAttribute(self, parent, elementName, attrName, attrValue):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetElementDepth(self, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetElementPath(self, element):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlCompareElements(self, element1, element2, deep):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlMergeDocuments(self, targetDoc, sourceDoc):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlValidate(self, doc):
#         '-no docstring-'
#         #return err, nret
#
#     def XmlGetObjectCount(self):
#         '-no docstring-'
#         #return nret
#
#     def XmlCleanupAll(self):
#         '-no docstring-'
#         #return nret
#
#     def YoloInfer(self, handle, imagePtr):
#         '-no docstring-'
#         #return nret
#
#     def YoloLoadModel(self, modelPath, outputPath, names_label, password, modelType, inferenceType, inferenceDevice):
#         '-no docstring-'
#         #return nret
#
#     def YoloLoadModelMemory(self, memoryAddr, size, modelType, inferenceType, inferenceDevice):
#         '-no docstring-'
#         #return nret
#
#     def YoloReleaseModel(self, modelHandle):
#         '-no docstring-'
#         #return nret
#
#     def YoloIsModelValid(self, modelHandle):
#         '-no docstring-'
#         #return nret
#
#     def YoloListModels(self):
#         '-no docstring-'
#         #return nret
#
#     def YoloGetModelInfo(self, modelHandle):
#         '-no docstring-'
#         #return nret
#
#     def YoloSetModelConfig(self, modelHandle, configJson):
#         '-no docstring-'
#         #return nret
#
#     def YoloGetModelConfig(self, modelHandle):
#         '-no docstring-'
#         #return nret
#
#     def YoloWarmup(self, modelHandle, iterations):
#         '-no docstring-'
#         #return nret
#
#     def YoloDetect(self, modelHandle, x1, y1, x2, y2, classes, confidence, iou, maxDetections):
#         '-no docstring-'
#         #return nret
#
#     def YoloDetectSimple(self, modelHandle, x1, y1, x2, y2):
#         '-no docstring-'
#         #return nret
#
#     def YoloDetectFromPtr(self, modelHandle, imagePtr, classes, confidence, iou, maxDetections):
#         '-no docstring-'
#         #return nret
#
#     def YoloDetectFromFile(self, modelHandle, imagePath, classes, confidence, iou, maxDetections):
#         '-no docstring-'
#         #return nret
#
#     def YoloDetectFromBase64(self, modelHandle, base64Data, classes, confidence, iou, maxDetections):
#         '-no docstring-'
#         #return nret
#
#     def YoloDetectBatch(self, modelHandle, imagesJson, classes, confidence, iou, maxDetections):
#         '-no docstring-'
#         #return nret
#
#     def YoloClassify(self, modelHandle, x1, y1, x2, y2, topK):
#         '-no docstring-'
#         #return nret
#
#     def YoloClassifyFromPtr(self, modelHandle, imagePtr, topK):
#         '-no docstring-'
#         #return nret
#
#     def YoloClassifyFromFile(self, modelHandle, imagePath, topK):
#         '-no docstring-'
#         #return nret
#
#     def YoloSegment(self, modelHandle, x1, y1, x2, y2, confidence, iou):
#         '-no docstring-'
#         #return nret
#
#     def YoloSegmentFromPtr(self, modelHandle, imagePtr, confidence, iou):
#         '-no docstring-'
#         #return nret
#
#     def YoloPose(self, modelHandle, x1, y1, x2, y2, confidence, iou):
#         '-no docstring-'
#         #return nret
#
#     def YoloPoseFromPtr(self, modelHandle, imagePtr, confidence, iou):
#         '-no docstring-'
#         #return nret
#
#     def YoloObb(self, modelHandle, x1, y1, x2, y2, confidence, iou):
#         '-no docstring-'
#         #return nret
#
#     def YoloObbFromPtr(self, modelHandle, imagePtr, confidence, iou):
#         '-no docstring-'
#         #return nret
#
#     def YoloKeyPoint(self, modelHandle, x1, y1, x2, y2, confidence, iou):
#         '-no docstring-'
#         #return nret
#
#     def YoloKeyPointFromPtr(self, modelHandle, imagePtr, confidence, iou):
#         '-no docstring-'
#         #return nret
#
#     def YoloGetInferenceStats(self, modelHandle):
#         '-no docstring-'
#         #return nret
#
#     def YoloResetStats(self, modelHandle):
#         '-no docstring-'
#         #return nret
#
#     def YoloGetLastError(self):
#         '-no docstring-'
#         #return nret
#
#     def YoloClearError(self):
#         '-no docstring-'
#         #return nret
#
#     def CreateCOLAPlugInterFace(self):
#         '-no docstring-'
#         #return nret
#
#     def DestroyCOLAPlugInterFace(self):
#         '-no docstring-'
#         #return nret
#
#     def Reg(self, userCode, softCode, featureList):
#         '-no docstring-'
#         #return nret
#
#     def Ver(self):
#         '-no docstring-'
#         #return nret
#
#     def SetPath(self, path):
#         '-no docstring-'
#         #return nret
#
#     def GetPath(self):
#         '-no docstring-'
#         #return nret
#
#     def GetMachineCode(self):
#         '-no docstring-'
#         #return nret
#
#     def GetBasePath(self):
#         '-no docstring-'
#         #return nret
#
#     def BindWindow(self, hwnd, display, mouse, keypad, mode):
#         '-no docstring-'
#         #return nret
#
#     def BindWindowEx(self, hwnd, display, mouse, keypad, pubstr, mode):
#         '-no docstring-'
#         #return nret
#
#     def UnBindWindow(self):
#         '-no docstring-'
#         #return nret
#
#     def GetBindWindow(self):
#         '-no docstring-'
#         #return nret
#
#     def ReleaseWindowsDll(self, hwnd):
#         '-no docstring-'
#         #return nret
#
#     def FreeStringPtr(self, ptr):
#         '-no docstring-'
#         #return nret
#
#     def GetStringSize(self, ptr):
#         '-no docstring-'
#         #return nret
#
#     def GetStringFromPtr(self, ptr, lpString, size):
#         '-no docstring-'
#         #return nret
#
#     def delay(self, millisecond):
#         '-no docstring-'
#         #return nret
#
#     def Delays(self, minMillisecond, maxMillisecond):
#         '-no docstring-'
#         #return nret
#
#     def SetUAC(self, enable):
#         '-no docstring-'
#         #return nret
#
#     def CheckUAC(self):
#         '-no docstring-'
#         #return nret
#
#     def RunApp(self, appPath, mode):
#         '-no docstring-'
#         #return nret
#
#     def ExecuteCmd(self, cmd, current_dir, time_out):
#         '-no docstring-'
#         #return nret
#
#     def GetConfig(self, configKey):
#         '-no docstring-'
#         #return nret
#
#     def SetConfig(self, configStr):
#         '-no docstring-'
#         #return nret
#
#     def SetConfigByKey(self, key, value):
#         '-no docstring-'
#         #return nret
#
#     def SendDropFiles(self, hwnd, file_path):
#         '-no docstring-'
#         #return nret
#
#     def FreeMemoryPtr(self, ptr):
#         '-no docstring-'
#         #return nret
#
#     def SetDefaultEncode(self, inputEncoding, outputEncoding):
#         '-no docstring-'
#         #return nret
#
#     def GetLastError(self):
#         '-no docstring-'
#         #return nret
#
#     def GetLastErrorString(self):
#         '-no docstring-'
#         #return nret
#
#     def HideModule(self, moduleName):
#         '-no docstring-'
#         #return nret
#
#     def UnhideModule(self, ctx):
#         '-no docstring-'
#         #return nret
#
#     def GetPlugInfo(self, type):
#         '-no docstring-'
#         #return nret
#


class Library(object):
    name = 'OLAPlugLib'
    _reg_typelib_ = ('{FCEFDCCE-1CC8-405F-9470-B891D87F9A36}', 1, 0)


class OlaPlug(CoClass):
    _reg_clsid_ = GUID('{343C6A20-9CBF-41C0-BC30-5A5889E206CA}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{FCEFDCCE-1CC8-405F-9470-B891D87F9A36}', 1, 0)


OlaPlug._com_interfaces_ = [IOlaPlug]

__all__ = ['IOlaPlug', 'OlaPlug', 'Library', 'typelib_path']


