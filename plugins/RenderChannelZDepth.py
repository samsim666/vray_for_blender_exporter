'''

 V-Ray/Blender 2.5

 http://vray.cgdo.ru

 Author: Andrey M. Izrantsev (aka bdancer)
 E-Mail: izrantsev@gmail.com

 This plugin is protected by the GNU General Public License v.2

 This program is free software: you can redioutibute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is dioutibuted in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.

 All Rights Reserved. V-Ray(R) is a registered trademark of Chaos Software.

'''

TYPE= 'RENDERCHANNEL'

ID=   'ZDEPTH'
NAME= 'ZDepth'
PLUG= 'RenderChannelZDepth'
DESC= "TODO."

PARAMS= (
	'name',
	'depth_from_camera',
	'depth_black',
	'depth_white',
	'depth_clamp',
	'filtering'
)


import bpy

from vb25.utils import *


class RenderChannelZDepth(bpy.types.IDPropertyGroup):
    pass

def add_properties(parent_struct):
	parent_struct.PointerProperty(
		attr= 'RenderChannelZDepth',
		type= RenderChannelZDepth,
		name= "Z-Depth",
		description= "V-Ray render channel \"Z-Depth\" settings."
	)

	FloatProperty= RenderChannelZDepth.FloatProperty
	IntProperty= RenderChannelZDepth.IntProperty
	BoolProperty= RenderChannelZDepth.BoolProperty
	EnumProperty= RenderChannelZDepth.EnumProperty
	FloatVectorProperty= RenderChannelZDepth.FloatVectorProperty
	StringProperty= RenderChannelZDepth.StringProperty

	# name: string
	StringProperty(
		attr= 'name',
		name= "Name",
		description= "Render channel name",
		maxlen= 64,
		default= "ZDepth"
	)

	# depth_from_camera: bool
	RenderChannelZDepth.BoolProperty(
		attr= 'depth_from_camera',
		name= "From camera",
		description= "TODO.",
		default= False
	)

	# depth_black: float
	RenderChannelZDepth.FloatProperty(
		attr= 'depth_black',
		name= "Black distance",
		description= "TODO.",
		min= 0.0,
		max= 100.0,
		soft_min= 0.0,
		soft_max= 10.0,
		precision= 3,
		default= 0
	)

	# depth_white: float
	RenderChannelZDepth.FloatProperty(
		attr= 'depth_white',
		name= "White distance",
		description= "TODO.",
		min= 0.0,
		max= 100.0,
		soft_min= 0.0,
		soft_max= 10.0,
		precision= 3,
		default= 1000
	)

	# depth_clamp: bool
	RenderChannelZDepth.BoolProperty(
		attr= 'depth_clamp',
		name= "Clamp",
		description= "TODO.",
		default= True
	)

	# filtering: bool
	RenderChannelZDepth.BoolProperty(
		attr= 'filtering',
		name= "Filtering",
		description= "TODO.",
		default= True
	)



'''
  OUTPUT
'''
def write(ofile, render_channel, sce= None, name= None):
	channel_name= "%s"%(clean_string(render_channel.name))
	if name is not None:
		channel_name= name

	ofile.write("\n%s %s {"%(PLUG, channel_name))
	for param in PARAMS:
		if param == 'name':
			value= "\"%s\"" % getattr(render_channel, param)
		else:
			value= getattr(render_channel, param)
		ofile.write("\n\t%s= %s;"%(param, p(value)))
	ofile.write("\n}\n")



'''
  GUI
'''
def draw(rna_pointer, layout, wide_ui):
	split= layout.split()
	col= split.column()
	col.prop(rna_pointer, 'depth_black', text="Black dist")
	col.prop(rna_pointer, 'depth_white', text="White dist")
	if wide_ui:
		col = split.column()
	col.prop(rna_pointer, 'depth_from_camera')
	col.prop(rna_pointer, 'depth_clamp')
	col.prop(rna_pointer, 'filtering')
