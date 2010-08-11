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
ID=   'VELOCITY'
NAME= 'Velocity'
PLUG= 'RenderChannelVelocity'
DESC= "TODO."

PARAMS= (
	'name',
	'clamp_velocity',
	'max_velocity',
	'max_velocity_last_frame',
	'ignore_z',
	'filtering'
)

import bpy

from vb25.utils import *


class RenderChannelVelocity(bpy.types.IDPropertyGroup):
	pass

def add_properties(parent_struct):
	parent_struct.PointerProperty(
		attr= 'RenderChannelVelocity',
		type=  RenderChannelVelocity,
		name= "Velocity",
		description= "V-Ray render channel \"Velocity\" settings."
	)

	# name: string
	RenderChannelVelocity.StringProperty(
		attr= 'name',
		name= "Name",
		description= "TODO.",
		default= "Velocity"
	)

	# clamp_velocity: bool
	RenderChannelVelocity.BoolProperty(
		attr= 'clamp_velocity',
		name= "Clamp",
		description= "TODO.",
		default= True
	)
	
	# max_velocity: float
	RenderChannelVelocity.FloatProperty(
		attr= 'max_velocity',
		name= "Max velocity",
		description= "Max velocity",
		min= 0.0,
		max= 100.0,
		soft_min= 0.0,
		soft_max= 10.0,
		precision= 3,
		default= 1
	)
	
	# max_velocity_last_frame: float
	RenderChannelVelocity.FloatProperty(
		attr= 'max_velocity_last_frame',
		name= "Max velocity last frame",
		description= "Max velocity last frame",
		min= 0.0,
		max= 100.0,
		soft_min= 0.0,
		soft_max= 10.0,
		precision= 3,
		default= 0
	)
	
	# ignore_z: bool
	RenderChannelVelocity.BoolProperty(
		attr= 'ignore_z',
		name= "Ignore Z",
		description= "TODO.",
		default= True
	)
	
	# filtering: bool
	RenderChannelVelocity.BoolProperty(
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
	col.prop(rna_pointer, 'max_velocity')
	col.prop(rna_pointer, 'max_velocity_last_frame', text="Max last")
	if wide_ui:
		col = split.column()
	col.prop(rna_pointer, 'clamp_velocity')
	col.prop(rna_pointer, 'ignore_z')
	col.prop(rna_pointer, 'filtering')

