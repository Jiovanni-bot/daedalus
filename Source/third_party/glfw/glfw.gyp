{
	'targets': [
		{
			'target_name': 'glfw',
			'type': 'static_library',
			'include_dirs': [
				'lib/',
				'lib/cocoa/',
			],
			'sources': [
				'lib/cocoa/cocoa_enable.m',
				'lib/cocoa/cocoa_fullscreen.m',
				'lib/cocoa/cocoa_glext.m',
				'lib/cocoa/cocoa_init.m',
				'lib/cocoa/cocoa_joystick.m',
				'lib/cocoa/cocoa_thread.c',
				'lib/cocoa/cocoa_time.m',
				'lib/cocoa/cocoa_window.m',
				'lib/enable.c',
				'lib/fullscreen.c',
				'lib/glext.c',
				'lib/image.c',
				'lib/init.c',
				'lib/input.c',
				'lib/internal.h',
				'lib/joystick.c',
				'lib/stream.c',
				'lib/tga.c',
				'lib/thread.c',
				'lib/time.c',
			],
		}
	],
}
