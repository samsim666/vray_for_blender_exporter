#
# V-Ray For Blender
#
# http://vray.cgdo.ru
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

import bpy


########  ######## ######## #### ##    ## ########  ######
##     ## ##       ##        ##  ###   ## ##       ##    ##
##     ## ##       ##        ##  ####  ## ##       ##
##     ## ######   ######    ##  ## ## ## ######    ######
##     ## ##       ##        ##  ##  #### ##             ##
##     ## ##       ##        ##  ##   ### ##       ##    ##
########  ######## ##       #### ##    ## ########  ######

VRayEngines = {
	'VRAY_RENDER',
	'VRAY_RENDER_PREVIEW',
	'VRAY_RENDER_RT',
	'VRAY_RENDERER'
}

narrowui = 200


##     ## ######## #### ##        ######
##     ##    ##     ##  ##       ##    ##
##     ##    ##     ##  ##       ##
##     ##    ##     ##  ##        ######
##     ##    ##     ##  ##             ##
##     ##    ##     ##  ##       ##    ##
 #######     ##    #### ########  ######

def GetContextType(context):
	if hasattr(context, 'node'):
		return 'NODE'
	if hasattr(context, 'material'):
		return 'MATERIAL'
	return None


def GetRegionWidthFromContext(context):
	contextType = GetContextType(context)
	if contextType == 'NODE':
		return context.node.width
	elif hasattr(context, 'region'):
		return context.region.width
	# Assume wide region width
	return 1024


def PollEngine(cls, context):
	rd = context.scene.render
	return rd.engine in cls.COMPAT_ENGINES


########     ###     ######  ########     ######  ##          ###     ######   ######  ########  ######
##     ##   ## ##   ##    ## ##          ##    ## ##         ## ##   ##    ## ##    ## ##       ##    ##
##     ##  ##   ##  ##       ##          ##       ##        ##   ##  ##       ##       ##       ##
########  ##     ##  ######  ######      ##       ##       ##     ##  ######   ######  ######    ######
##     ## #########       ## ##          ##       ##       #########       ##       ## ##             ##
##     ## ##     ## ##    ## ##          ##    ## ##       ##     ## ##    ## ##    ## ##       ##    ##
########  ##     ##  ######  ########     ######  ######## ##     ##  ######   ######  ########  ######

class VRayPanel(bpy.types.Panel):
	COMPAT_ENGINES = VRayEngines


class VRayDataPanel(VRayPanel):
	bl_space_type  = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context     = 'data'

	@classmethod
	def poll(cls, context):
		return PollEngine(cls, context)


class VRayGeomPanel(VRayDataPanel):
	incompatTypes  = {'LAMP', 'CAMERA', 'ARMATURE', 'EMPTY'}

	@classmethod
	def poll(cls, context):
		return context.object and context.object.type not in cls.incompatTypes and PollEngine(cls, context)


class VRayCameraPanel(VRayDataPanel):
	@classmethod
	def poll(cls, context):
		return context.camera and PollEngine(cls, context)


class VRayLampPanel(VRayDataPanel):
	@classmethod
	def poll(cls, context):
		return context.lamp and PollEngine(cls, context)


class VRayMaterialPanel(VRayPanel):
	bl_space_type  = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context     = 'material'

	@classmethod
	def poll(cls, context):
		return context.material and PollEngine(cls, context)


class VRayObjectPanel(VRayPanel):
	bl_space_type  = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context     = 'object'

	incompatTypes  = {'LAMP', 'CAMERA', 'ARMATURE', 'EMPTY'}

	@classmethod
	def poll(cls, context):
		return context.object and context.object.type not in cls.incompatTypes and PollEngine(cls, context)


class VRayParticlePanel(VRayPanel):
	bl_space_type  = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context     = 'particle'

	@classmethod
	def poll(cls, context):
		return context.particle_system and PollEngine(cls, context)


class VRayRenderPanel(VRayPanel):
	bl_space_type  = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context     = 'render'

	@classmethod
	def poll(cls, context):
		return PollEngine(cls, context)


class VRayRenderLayersPanel(VRayPanel):
	bl_space_type  = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context     = 'render_layer'

	@classmethod
	def poll(cls, context):
		return PollEngine(cls, context)


class VRayScenePanel(VRayPanel):
	bl_space_type  = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context     = 'scene'

	@classmethod
	def poll(cls, context):
		return PollEngine(cls, context)


class VRayTexturePanel(VRayPanel):
	bl_space_type  = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context     = 'texture'

	@classmethod
	def poll(cls, context):
		return context.texture and PollEngine(cls, context)


class VRayWorldPanel(VRayPanel):
	bl_space_type  = 'PROPERTIES'
	bl_region_type = 'WINDOW'
	bl_context     = 'world'

	@classmethod
	def poll(cls, context):
		return context.world and PollEngine(cls, context)


##       ####  ######  ########
##        ##  ##    ##    ##
##        ##  ##          ##
##        ##   ######     ##
##        ##        ##    ##
##        ##  ##    ##    ##
######## ####  ######     ##

# The draw_item function is called for each item of the collection that is visible in the list.
#   data is the RNA object containing the collection,
#   item is the current drawn item of the collection,
#   icon is the "computed" icon for the item (as an integer, because some objects like materials or textures
#   have custom icons ID, which are not available as enum items).
#   active_data is the RNA object containing the active property for the collection (i.e. integer pointing to the
#   active item of the collection).
#   active_propname is the name of the active property (use 'getattr(active_data, active_propname)').
#   index is index of the current item in the collection.

class VRayListUse(bpy.types.UIList):
	def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
		layout.label(item.name)
		layout.prop(item, 'use')


class VRayList(bpy.types.UIList):
	def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
		layout.label(item.name)


class VRayListMaterialSlots(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        ob   = data
        slot = item
        ma   = slot.material

        split = layout.split(percentage=0.75)

        if ma:
            split.label(text=ma.name, translate=False, icon_value=icon)
            split.prop(slot, 'link', text="", emboss=False, translate=False)
        else:
            split.label(text="")


########  ########  ######   ####  ######  ######## ########     ###    ######## ####  #######  ##    ##
##     ## ##       ##    ##   ##  ##    ##    ##    ##     ##   ## ##      ##     ##  ##     ## ###   ##
##     ## ##       ##         ##  ##          ##    ##     ##  ##   ##     ##     ##  ##     ## ####  ##
########  ######   ##   ####  ##   ######     ##    ########  ##     ##    ##     ##  ##     ## ## ## ##
##   ##   ##       ##    ##   ##        ##    ##    ##   ##   #########    ##     ##  ##     ## ##  ####
##    ##  ##       ##    ##   ##  ##    ##    ##    ##    ##  ##     ##    ##     ##  ##     ## ##   ###
##     ## ########  ######   ####  ######     ##    ##     ## ##     ##    ##    ####  #######  ##    ##

def GetRegClasses():
	return (
		VRayListMaterialSlots,
		VRayListUse,
		VRayList,
	)


def register():
	for regClass in GetRegClasses():
		bpy.utils.register_class(regClass)


def unregister():
	for regClass in GetRegClasses():
		bpy.utils.unregister_class(regClass)