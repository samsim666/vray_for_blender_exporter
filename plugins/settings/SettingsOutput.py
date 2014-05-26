#
# V-Ray For Blender
#
# http://chaosgroup.com
#
# Author: Andrei Izrantcev
# E-Mail: andrei.izrantcev@chaosgroup.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# All Rights Reserved. V-Ray(R) is a registered trademark of Chaos Software.
#

from vb30.lib import ExportUtils
from vb30.lib import PathUtils
from vb30.lib import LibUtils

from vb30 import debug


TYPE = 'SETTINGS'
ID   = 'SettingsOutput'
NAME = 'Output'
DESC = ""

PluginParams = (
    {
        'attr' : 'img_width',
        'desc' : "Output image width",
        'type' : 'INT',
        'default' : 640,
    },
    {
        'attr' : 'img_height',
        'desc' : "Output image height",
        'type' : 'INT',
        'default' : 480,
    },
    {
        'attr' : 'img_pixelAspect',
        'desc' : "Output image pixel aspect",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'img_file',
        'desc' : "Render file name (Variables: %C - camera name; %S - scene name; %F - blendfile name)",
        'type' : 'STRING',
        'default' : "%F_%C",
    },
    {
        'attr' : 'img_dir',
        'desc' : "Render file directory (Variables: %C - camera name; %S - scene name; %F - blendfile name)",
        'type' : 'STRING',
        'subtype' : 'DIR_PATH',
        'default' : "//render/%F/",
    },
    {
        'attr' : 'img_file_needFrameNumber',
        'desc' : "Add frame number to the image file name",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'img_separateAlpha',
        'desc' : "Write the alpha channel to a separate file",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'img_noAlpha',
        'desc' : "Don't write the alpha channel to the final image",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'img_dontSaveRgbChannel',
        'desc' : "If true, the RGB channel will not be saved to disk",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'img_deepFile',
        'desc' : "If true, V-Ray will will generate deep image file (valid for vrst and exr)",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'img_rawFile',
        'desc' : "If true, V-Ray will render to a tiled file format (.vrimg or .exr). This is automatically turned on for file formats that only support tiled writing (like .vrimg)",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'img_rawFileVFB',
        'desc' : "If writing to a tiled file format, specifies whether a memory VFB window should be displayed (0 - no memory VFB, 1 - full memory VFB, 2 - preview)",
        'type' : 'INT',
        'default' : 1,
    },
    {
        'attr' : 'anim_start',
        'desc' : "Start of animation range in time units",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'anim_end',
        'desc' : "End of animation range in time units",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'anim_frame_padding',
        'desc' : "Animation Frame Name Padding",
        'type' : 'INT',
        'default' : 4,
    },
    {
        'attr' : 'anim_renumber_on',
        'desc' : "If true, frame renumbering is used",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'anim_renumber_start',
        'desc' : "Start number for renumber frames",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'anim_renumber_step',
        'desc' : "Renumber frames step",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'anim_ren_frame_start',
        'desc' : "First frame of animation range",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'frame_start',
        'desc' : "The frame number at the start of the animation range",
        'type' : 'INT',
        'default' : 0,
    },
    {
        'attr' : 'frames_per_second',
        'desc' : "Number of frames per unit time",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'frames',
        'desc' : "List of frames to be rendered. May contain intervals in the form of lists with start and end frame",
        'type' : 'LIST',
        'default' : "",
    },
    {
        'attr' : 'rgn_left',
        'desc' : "Image output region left coord",
        'type' : 'FLOAT',
        'skip' : True,
        'default' : 0,
    },
    {
        'attr' : 'rgn_width',
        'desc' : "Image output region width",
        'type' : 'FLOAT',
        'skip' : True,
        'default' : 640,
    },
    {
        'attr' : 'rgn_top',
        'desc' : "Image output region top coord",
        'type' : 'FLOAT',
        'skip' : True,
        'default' : 0,
    },
    {
        'attr' : 'rgn_height',
        'desc' : "Image output region height",
        'type' : 'FLOAT',
        'skip' : True,
        'default' : 480,
    },
    {
        'attr' : 'bmp_width',
        'desc' : "Output bitmap width",
        'type' : 'INT',
        'skip' : True,
        'default' : 640,
    },
    {
        'attr' : 'bmp_height',
        'desc' : "Output bitmap height",
        'type' : 'INT',
        'skip' : True,
        'default' : 480,
    },
    {
        'attr' : 'r_left',
        'desc' : "Bitmap output region left coord",
        'type' : 'INT',
        'skip' : True,
        'default' : 0,
    },
    {
        'attr' : 'r_width',
        'desc' : "Bitmap output region width",
        'type' : 'INT',
        'skip' : True,
        'default' : 640,
    },
    {
        'attr' : 'r_top',
        'desc' : "Bitmap output region top coord",
        'type' : 'INT',
        'skip' : True,
        'default' : 0,
    },
    {
        'attr' : 'r_height',
        'desc' : "Bitmap output region height",
        'type' : 'INT',
        'skip' : True,
        'default' : 480,
    },
    {
        'attr' : 'frame_stamp_enabled',
        'desc' : "true to enable the VFB frame stamp",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'frame_stamp_text',
        'desc' : "Frame stamp text",
        'type' : 'STRING',
        'default' : "V-Ray %vraycore | %rendertime",
    },
    {
        'attr' : 'relements_separateFolders',
        'desc' : "Save render channels in separate folders",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'relements_separate_rgba',
        'desc' : "true to save the main RGBA elment in a separate folder too, if relements_separateFolders is specified",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'relements_divider',
        'desc' : "Render elements name separator",
        'type' : 'STRING',
        'default' : "",
    },
    {
        'attr' : 'film_offset_x',
        'desc' : "Horizontal film offset",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'film_offset_y',
        'desc' : "Vertical film offset",
        'type' : 'FLOAT',
        'default' : 0,
    },

    {
        'attr' : 'img_format',
        'name' : "Image Format",
        'desc' : "Output image format",
        'type' : 'ENUM',
        'items' : (
            ('PNG',  "PNG",       ""),
            ('JPG',  "JPEG",      ""),
            ('TIFF', "TIFF",      ""),
            ('TGA',  "TGA",       ""),
            ('SGI',  "SGI",       ""),
            ('EXR',  "OpenEXR",   ""),
            ('VRST', "VRayImage", "V-Ray Image Format"),
        ),
        'skip' : True,
        'default' : 'JPG',
    },
)

PluginWidget = """
{ "widgets": [
]}
"""


def writeDatablock(bus, pluginModule, pluginName, propGroup, overrideParams):
    scene = bus['scene']
    o     = bus['output']

    VRayScene = scene.vray
    VRayExporter = VRayScene.Exporter

    img_width  = int(scene.render.resolution_x * scene.render.resolution_percentage * 0.01)
    img_height = int(scene.render.resolution_y * scene.render.resolution_percentage * 0.01)
    
    if VRayScene.RTEngine.enabled:
        if VRayScene.SettingsRTEngine.stereo_mode:
            img_width *= 2.0

    overrideParams['img_width']  = img_width
    overrideParams['img_height'] = img_height

    if o.isPreviewRender() or VRayExporter.auto_save_render:
        pm = o.getFileManager().getPathManager()
        img_file = pm.getImgFilename()
        img_dir  = pm.getImgDirpath()

        if not img_file:
            debug.Debug("Image output filename is not set!", msgType='ERROR')
            return None

        if not img_dir:
            debug.Debug("Image output directory is not set!", msgType='ERROR')
            return None

        overrideParams['img_file'] = img_file
        overrideParams['img_dir']  = img_dir

        if o.isPreviewRender():
            overrideParams['img_file_needFrameNumber'] = False

    return ExportUtils.WritePluginCustom(bus, pluginModule, pluginName, propGroup, overrideParams)
