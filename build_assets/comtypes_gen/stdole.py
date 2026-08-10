from enum import IntFlag

import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 as __wrapper_module__
from comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 import (
    OLE_YSIZE_CONTAINER, FONTUNDERSCORE, EXCEPINFO, _lcid,
    IPictureDisp, typelib_path, IUnknown, OLE_XSIZE_PIXELS, StdFont,
    StdPicture, CoClass, FontEvents, Monochrome, OLE_YSIZE_PIXELS,
    FONTSIZE, _check_version, OLE_XPOS_CONTAINER, BSTR, OLE_HANDLE,
    DISPMETHOD, VARIANT_BOOL, OLE_XPOS_PIXELS, IFont, FONTNAME,
    Picture, IFontEventsDisp, Color, OLE_CANCELBOOL,
    FONTSTRIKETHROUGH, DISPPROPERTY, IFontDisp, OLE_YPOS_HIMETRIC,
    Unchecked, OLE_YPOS_PIXELS, IEnumVARIANT, dispid, Font, Default,
    OLE_XSIZE_CONTAINER, Library, VgaColor, FONTBOLD, Checked,
    IPicture, OLE_ENABLEDEFAULTBOOL, Gray, HRESULT,
    OLE_XSIZE_HIMETRIC, FONTITALIC, COMMETHOD, OLE_YPOS_CONTAINER,
    DISPPARAMS, OLE_COLOR, OLE_YSIZE_HIMETRIC, OLE_OPTEXCLUSIVE,
    IDispatch, GUID, OLE_XPOS_HIMETRIC
)


class OLE_TRISTATE(IntFlag):
    Unchecked = 0
    Checked = 1
    Gray = 2


class LoadPictureConstants(IntFlag):
    Default = 0
    Monochrome = 1
    VgaColor = 2
    Color = 4


__all__ = [
    'OLE_YSIZE_CONTAINER', 'FONTSTRIKETHROUGH', 'FONTUNDERSCORE',
    'IFontDisp', 'OLE_YPOS_HIMETRIC', 'Unchecked', 'IPictureDisp',
    'OLE_YPOS_PIXELS', 'typelib_path', 'OLE_TRISTATE',
    'OLE_XSIZE_PIXELS', 'StdFont', 'Font', 'Default',
    'OLE_XSIZE_CONTAINER', 'Library', 'StdPicture', 'FontEvents',
    'Monochrome', 'OLE_YSIZE_PIXELS', 'FONTSIZE', 'VgaColor',
    'FONTBOLD', 'Checked', 'IPicture', 'OLE_XPOS_CONTAINER',
    'OLE_ENABLEDEFAULTBOOL', 'Gray', 'OLE_XSIZE_HIMETRIC',
    'FONTITALIC', 'OLE_HANDLE', 'LoadPictureConstants',
    'OLE_YPOS_CONTAINER', 'OLE_COLOR', 'OLE_YSIZE_HIMETRIC',
    'OLE_OPTEXCLUSIVE', 'OLE_XPOS_PIXELS', 'IFont', 'FONTNAME',
    'Picture', 'IFontEventsDisp', 'OLE_XPOS_HIMETRIC', 'Color',
    'OLE_CANCELBOOL'
]

