#
# V-Ray/Blender
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

import re

import bpy

from pynodes_framework import idref

from vb25.debug import Debug, PrintDict


PluginTypes = {
    'BRDF',
    'MATERIAL',
    'PLUGIN',
    'TEXTURE',
    'UVWGEN',
}

SkippedTypes = {
    'LIST',
    'INT_LIST',
    'MATRIX',
    'TRANSFORM',
    'TRANSFORM_TEXTURE',
}

InputTypes = {
    'BRDF',
    'COLOR',
    'FLOAT_TEXTURE',
    'MATERIAL',
    'GEOMETRY',
    'PLUGIN',
    'TEXTURE',
    'VECTOR',
    'UVWGEN',
}

OutputTypes = {
    'OUTPUT_PLUGIN',
    'OUTPUT_COLOR',
    'OUTPUT_FLOAT_TEXTURE',
    'OUTPUT_VECTOR_TEXTURE',
    'OUTPUT_TRANSFORM_TEXTURE',
    'OUTPUT_TEXTURE',
}

TypeToSocket = {
    'COLOR'  : 'VRaySocketColor',
    'VECTOR' : 'VRaySocketVector',
    'FLOAT'  : 'VRaySocketFloat',
    'INT'    : 'VRaySocketInt',

    'BRDF'     : 'VRaySocketBRDF',
    'GEOMETRY' : 'VRaySocketGeom',
    'MATERIAL' : 'VRaySocketMtl',
    'PLUGIN'   : 'VRaySocketObject',
    'UVWGEN'   : 'VRaySocketCoords',

    'TEXTURE'       : 'VRaySocketColor',
    'FLOAT_TEXTURE' : 'VRaySocketFloatColor',
    'INT_TEXTURE'   : 'VRaySocketFloatColor',

    'OUTPUT_COLOR'             : 'VRaySocketColor',
    'OUTPUT_PLUGIN'            : 'VRaySocketObject',
    'OUTPUT_FLOAT_TEXTURE'     : 'VRaySocketFloatColor',
    'OUTPUT_TEXTURE'           : 'VRaySocketColor',
    'OUTPUT_VECTOR_TEXTURE'    : 'VRaySocketFloatColor',
    'OUTPUT_TRANSFORM_TEXTURE' : 'VRaySocketVector',
}

TypeToProp = {
    'BOOL'   : bpy.props.BoolProperty,
    'COLOR'  : bpy.props.FloatVectorProperty,
    'VECTOR' : bpy.props.FloatVectorProperty,
    'ENUM'   : bpy.props.EnumProperty,
    'FLOAT'  : bpy.props.FloatProperty,
    'INT'    : bpy.props.IntProperty,
    'STRING' : bpy.props.StringProperty,

    'BRDF'     : bpy.props.StringProperty,
    'GEOMETRY' : bpy.props.StringProperty,
    'MATERIAL' : bpy.props.StringProperty,
    'PLUGIN'   : bpy.props.StringProperty,
    'UVWGEN'   : bpy.props.StringProperty,

    'INT_TEXTURE'   : bpy.props.IntProperty,
    'FLOAT_TEXTURE' : bpy.props.FloatProperty,
    'TEXTURE'       : bpy.props.FloatVectorProperty,

    'OUTPUT_COLOR'             : bpy.props.FloatVectorProperty,
    'OUTPUT_PLUGIN'            : bpy.props.StringProperty,
    'OUTPUT_FLOAT_TEXTURE'     : bpy.props.FloatProperty,
    'OUTPUT_TEXTURE'           : bpy.props.FloatVectorProperty,
    'OUTPUT_VECTOR_TEXTURE'    : bpy.props.FloatVectorProperty,
    'OUTPUT_TRANSFORM_TEXTURE' : bpy.props.FloatVectorProperty,
}


def GetNameFromAttr(attr):
    attr_name = attr.replace("_", " ")
    attr_name = re.sub(r"\B([A-Z])", r" \1", attr_name)
    
    return attr_name.title()


def GenerateAttribute(classMembers, attrDesc):
    if attrDesc['type'] in SkippedTypes:
        return

    attrArgs = {
        'attr'        : attrDesc['attr'],
        'name'        : attrDesc.get('name', GetNameFromAttr(attrDesc['attr'])).title(),
        'description' : attrDesc['desc'],
        'default'     : attrDesc['default'],
    }

    if attrDesc['type'] in {'IMAGE', 'NODETREE', 'TEXTURE'}:
        options = {'FAKE_USER'}
        if 'options' in attrDesc:
            for opt in attrDesc['options']:
                options.add(opt)

        classMembers[attrDesc['attr']] = idref.IDRefProperty(
            attrArgs['name'],
            attrArgs['description'],
            idtype = attrDesc['type'],
            options = options,
        )
        return

    defUi    = None
    attrFunc = TypeToProp[attrDesc['type']]

    if attrDesc['type'] in {'STRING'}:
        pass

    elif attrDesc['type'] in {'COLOR', 'ACOLOR', 'TEXTURE'}:
        attrArgs['subtype'] = 'COLOR'
        attrArgs['size']    = len(attrDesc['default'])

    elif attrDesc['type'] in {'VECTOR'}:
        if 'subtype' not in attrDesc:
            attrArgs['subtype'] = 'TRANSLATION'

    elif attrDesc['type'] in {'FLOAT', 'FLOAT_TEXTURE'}:
        defUi = {
            'min' : -1024.0,
            'max' :  1024.0,
            'soft_min' : 0.0,
            'soft_max' : 1.0,
        }

    elif attrDesc['type'] in {'INT', 'INT_TEXTURE'}:
        defUi = {
            'min' : -1024,
            'max' :  1024,
            'soft_min' : 0,
            'soft_max' : 8,
        }

    elif attrDesc['type'] in {'ENUM'}:
        attrArgs['items'] = attrDesc['items']

    for optionalKey in ('size', 'options', 'precision', 'subtype'):
        if optionalKey in attrDesc:
            attrArgs[optionalKey] = attrDesc[optionalKey]

    if attrDesc['type'] in {'INT', 'INT_TEXTURE', 'FLOAT', 'FLOAT_TEXTURE'}:
        if 'ui' not in attrDesc:
            attrDesc['ui'] = defUi

        attrArgs['min'] = attrDesc['ui'].get('min', defUi['min'])
        attrArgs['max'] = attrDesc['ui'].get('max', defUi['max'])
        attrArgs['soft_min'] = attrDesc['ui'].get('soft_min', defUi['soft_min'])
        attrArgs['soft_max'] = attrDesc['ui'].get('soft_max', defUi['soft_max'])

    classMembers[attrDesc['attr']] = attrFunc(**attrArgs)
