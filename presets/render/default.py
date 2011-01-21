import bpy
bpy.context.scene.vray.exporter.autorun = True
bpy.context.scene.vray.exporter.animation = False
bpy.context.scene.vray.exporter.auto_meshes = False
bpy.context.scene.vray.exporter.debug = False
bpy.context.scene.vray.exporter.use_material_nodes = False
bpy.context.scene.vray.exporter.compat_mode = False
bpy.context.scene.vray.exporter.image_to_blender = False
bpy.context.scene.vray.exporter.active_layers = True
bpy.context.scene.vray.exporter.mesh_active_layers = True
bpy.context.scene.vray.exporter.check_animated = False
bpy.context.scene.vray.exporter.use_displace = True
bpy.context.scene.vray.exporter.use_instances = True
bpy.context.scene.vray.exporter.use_hair = True
bpy.context.scene.vray.exporter.detect_vray = True
bpy.context.scene.vray.exporter.vray_binary = ''
bpy.context.scene.vray.exporter.output = 'TMP'
bpy.context.scene.vray.exporter.output_dir = ''
bpy.context.scene.vray.exporter.output_unique = False
bpy.context.scene.vray.SettingsOptions.geom_displacement = True
bpy.context.scene.vray.SettingsOptions.geom_doHidden = False
bpy.context.scene.vray.SettingsOptions.light_doLights = True
bpy.context.scene.vray.SettingsOptions.light_doDefaultLights = False
bpy.context.scene.vray.SettingsOptions.light_doHiddenLights = False
bpy.context.scene.vray.SettingsOptions.light_doShadows = True
bpy.context.scene.vray.SettingsOptions.light_onlyGI = False
bpy.context.scene.vray.SettingsOptions.gi_dontRenderImage = False
bpy.context.scene.vray.SettingsOptions.mtl_reflectionRefraction = True
bpy.context.scene.vray.SettingsOptions.mtl_limitDepth = False
bpy.context.scene.vray.SettingsOptions.mtl_maxDepth = 5
bpy.context.scene.vray.SettingsOptions.mtl_doMaps = True
bpy.context.scene.vray.SettingsOptions.mtl_filterMaps = True
bpy.context.scene.vray.SettingsOptions.mtl_filterMapsForSecondaryRays = False
bpy.context.scene.vray.SettingsOptions.mtl_transpMaxLevels = 50
bpy.context.scene.vray.SettingsOptions.mtl_transpCutoff = 0.0010000000474974513
bpy.context.scene.vray.SettingsOptions.mtl_override_on = False
bpy.context.scene.vray.SettingsOptions.mtl_glossy = True
bpy.context.scene.vray.SettingsOptions.geom_backfaceCull = False
bpy.context.scene.vray.SettingsOptions.ray_bias = 0.0
bpy.context.scene.vray.SettingsOptions.misc_lowThreadPriority = True
bpy.context.scene.vray.SettingsCaustics.on = False
bpy.context.scene.vray.SettingsCaustics.max_photons = 30
bpy.context.scene.vray.SettingsCaustics.search_distance = 0.10000000149011612
bpy.context.scene.vray.SettingsCaustics.max_density = 0.0
bpy.context.scene.vray.SettingsCaustics.multiplier = 1.0
bpy.context.scene.vray.SettingsCaustics.mode = 'NEW'
bpy.context.scene.vray.SettingsCaustics.file = ''
bpy.context.scene.vray.SettingsCaustics.auto_save = False
bpy.context.scene.vray.SettingsCaustics.auto_save_file = ''
bpy.context.scene.vray.SettingsCaustics.show_calc_phase = False
bpy.context.scene.vray.SettingsGI.on = False
bpy.context.scene.vray.SettingsGI.refract_caustics = True
bpy.context.scene.vray.SettingsGI.reflect_caustics = False
bpy.context.scene.vray.SettingsGI.saturation = 1.0
bpy.context.scene.vray.SettingsGI.contrast = 1.0
bpy.context.scene.vray.SettingsGI.contrast_base = 0.5
bpy.context.scene.vray.SettingsGI.primary_engine = 'IM'
bpy.context.scene.vray.SettingsGI.primary_multiplier = 1.0
bpy.context.scene.vray.SettingsGI.secondary_engine = 'LC'
bpy.context.scene.vray.SettingsGI.secondary_multiplier = 1.0
bpy.context.scene.vray.SettingsGI.SettingsDMCGI.subdivs = 8
bpy.context.scene.vray.SettingsGI.SettingsDMCGI.depth = 3
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.min_rate = -3
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.max_rate = 0
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.subdivs = 50
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.interp_samples = 20
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.calc_interp_samples = 10
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.interp_frames = 2
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.color_threshold = 0.30000001192092896
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.normal_threshold = 0.10000000149011612
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.distance_threshold = 0.10000000149011612
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.detail_enhancement = False
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.detail_radius = 0.05999999865889549
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.detail_subdivs_mult = 0.30000001192092896
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.detail_scale = 'SCREEN'
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.randomize_samples = True
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.interpolation_mode = 'LEAST'
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.lookup_mode = 'OVERLAP'
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.mode = 'SINGLE'
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.file = ''
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.show_samples = False
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.show_calc_phase = True
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.show_direct_light = True
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.multiple_views = False
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.multipass = False
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.check_sample_visibility = False
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.auto_save = False
bpy.context.scene.vray.SettingsGI.SettingsIrradianceMap.auto_save_file = ''
bpy.context.scene.vray.SettingsGI.SettingsLightCache.subdivs = 1000
bpy.context.scene.vray.SettingsGI.SettingsLightCache.sample_size = 0.019999999552965164
bpy.context.scene.vray.SettingsGI.SettingsLightCache.filter_type = 'NEAREST'
bpy.context.scene.vray.SettingsGI.SettingsLightCache.filter_samples = 10
bpy.context.scene.vray.SettingsGI.SettingsLightCache.filter_size = 0.019999999552965164
bpy.context.scene.vray.SettingsGI.SettingsLightCache.prefilter = False
bpy.context.scene.vray.SettingsGI.SettingsLightCache.prefilter_samples = 40
bpy.context.scene.vray.SettingsGI.SettingsLightCache.depth = 100
bpy.context.scene.vray.SettingsGI.SettingsLightCache.show_calc_phase = True
bpy.context.scene.vray.SettingsGI.SettingsLightCache.store_direct_light = True
bpy.context.scene.vray.SettingsGI.SettingsLightCache.world_scale = 'SCREEN'
bpy.context.scene.vray.SettingsGI.SettingsLightCache.mode = 'SINGLE'
bpy.context.scene.vray.SettingsGI.SettingsLightCache.file = ''
bpy.context.scene.vray.SettingsGI.SettingsLightCache.auto_save = False
bpy.context.scene.vray.SettingsGI.SettingsLightCache.auto_save_file = ''
bpy.context.scene.vray.SettingsGI.SettingsLightCache.num_passes = 4
bpy.context.scene.vray.SettingsGI.SettingsLightCache.use_for_glossy_rays = False
bpy.context.scene.vray.SettingsGI.SettingsLightCache.adaptive_sampling = False
bpy.context.scene.vray.SettingsGI.SettingsLightCache.multiple_views = False
bpy.context.scene.vray.SettingsDefaultDisplacement.override_on = False
bpy.context.scene.vray.SettingsDefaultDisplacement.edgeLength = 4.0
bpy.context.scene.vray.SettingsDefaultDisplacement.viewDependent = True
bpy.context.scene.vray.SettingsDefaultDisplacement.maxSubdivs = 256
bpy.context.scene.vray.SettingsDefaultDisplacement.tightBounds = True
bpy.context.scene.vray.SettingsDefaultDisplacement.amount = 1.0
bpy.context.scene.vray.SettingsDefaultDisplacement.relative = False
bpy.context.scene.vray.SettingsRegionsGenerator.xc = 32
bpy.context.scene.vray.SettingsRegionsGenerator.yc = 32
bpy.context.scene.vray.SettingsRegionsGenerator.reverse = False
bpy.context.scene.vray.SettingsRegionsGenerator.seqtype = 'TRIANGLE'
bpy.context.scene.vray.SettingsRegionsGenerator.xymeans = 'SIZE'
bpy.context.scene.vray.SettingsImageSampler.type = 'DMC'
bpy.context.scene.vray.SettingsImageSampler.fixed_subdivs = 1
bpy.context.scene.vray.SettingsImageSampler.dmc_minSubdivs = 1
bpy.context.scene.vray.SettingsImageSampler.dmc_threshold = 0.009999999776482582
bpy.context.scene.vray.SettingsImageSampler.dmc_show_samples = False
bpy.context.scene.vray.SettingsImageSampler.subdivision_minRate = -1
bpy.context.scene.vray.SettingsImageSampler.subdivision_maxRate = 2
bpy.context.scene.vray.SettingsImageSampler.subdivision_threshold = 0.10000000149011612
bpy.context.scene.vray.SettingsImageSampler.subdivision_edges = False
bpy.context.scene.vray.SettingsImageSampler.subdivision_normals = False
bpy.context.scene.vray.SettingsImageSampler.subdivision_normals_threshold = 0.05000000074505806
bpy.context.scene.vray.SettingsImageSampler.subdivision_jitter = True
bpy.context.scene.vray.SettingsImageSampler.subdivision_show_samples = False
bpy.context.scene.vray.SettingsRaycaster.maxLevels = 80
bpy.context.scene.vray.SettingsRaycaster.minLeafSize = 0.0
bpy.context.scene.vray.SettingsRaycaster.faceLevelCoef = 1.0
bpy.context.scene.vray.SettingsRaycaster.dynMemLimit = 1024
bpy.context.scene.vray.SettingsDMCSampler.time_dependent = False
bpy.context.scene.vray.SettingsDMCSampler.adaptive_amount = 0.8500000238418579
bpy.context.scene.vray.SettingsDMCSampler.adaptive_threshold = 0.009999999776482582
bpy.context.scene.vray.SettingsDMCSampler.adaptive_min_samples = 8
bpy.context.scene.vray.SettingsDMCSampler.subdivs_mult = 1.0
bpy.context.scene.vray.SettingsUnitsInfo.meters_scale = 1.0
bpy.context.scene.vray.SettingsUnitsInfo.photometric_scale = 0.0020000000949949026
bpy.context.scene.vray.SettingsColorMapping.affect_background = True
bpy.context.scene.vray.SettingsColorMapping.dark_mult = 1.0
bpy.context.scene.vray.SettingsColorMapping.bright_mult = 1.0
bpy.context.scene.vray.SettingsColorMapping.gamma = 1.0
bpy.context.scene.vray.SettingsColorMapping.input_gamma = 1.0
bpy.context.scene.vray.SettingsColorMapping.subpixel_mapping = False
bpy.context.scene.vray.SettingsColorMapping.clamp_output = True
bpy.context.scene.vray.SettingsColorMapping.clamp_level = 1.0
bpy.context.scene.vray.SettingsColorMapping.adaptation_only = False
bpy.context.scene.vray.SettingsColorMapping.linearWorkflow = False
bpy.context.scene.vray.VRayDR.on = False
bpy.context.scene.vray.VRayDR.shared_dir = ''
bpy.context.scene.vray.VRayDR.type = 'WU'
bpy.context.scene.vray.VRayDR.port = 20204
bpy.context.scene.render.threads_mode = 'AUTO'
bpy.context.scene.render.threads = 4