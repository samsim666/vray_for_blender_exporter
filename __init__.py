'''

  V-Ray/Blender 2.5

  http://vray.cgdo.ru

  Author: Andrey M. Izrantsev (aka bdancer)
  E-Mail: izrantsev@cgdo.ru

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  as published by the Free Software Foundation; either version 2
  of the License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

  All Rights Reserved. V-Ray(R) is a registered trademark of Chaos Software.

'''

# TODO: move to Add-ons
# bl_info= {
# 	"name":        "V-Ray (git)",
# 	"author":      "Andrey M. Izrantsev",
# 	"version":     (0, 0, 1),
# 	"blender":     (2, 5, 6),
# 	"api":         34471,
# 	"location":    "Info Header (engine dropdown)",
# 	"description": "V-Ray Standalone integration for Blender",
# 	"warning":     "",
# 	"wiki_url":    "http://github.com/bdancer/vb25/wiki",
# 	"tracker_url": "http://github.com/bdancer/vb25/issues",
# 	"category":    "Render"
# }

from vb25 import properties_camera
from vb25 import properties_lamp
from vb25 import properties_material
from vb25 import properties_texture
from vb25 import properties_world
from vb25 import properties_object
from vb25 import properties_data
from vb25 import properties_render
from vb25 import plugins
from vb25 import shaders
from vb25 import render
from vb25 import preset

def register():
	plugins.add_properties()

def unregister():
	plugins.remove_properties()
