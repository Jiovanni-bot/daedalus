add_subdirectory(Debug)
add_subdirectory(DynaRec)
add_subdirectory(Graphics)
add_subdirectory(HLEAudio)
add_subdirectory(HLEGraphics)
add_subdirectory(Input)
add_subdirectory(PRX)
add_subdirectory(UI)
add_subdirectory(Utility)

# Create and install Plugin files

install(DIRECTORY DESTINATION DaedalusX64/Plugins) 
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/PRX/MediaEngine/mediaengine.prx DESTINATION DaedalusX64/Plugins)
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/PRX/DveMgr/dvemgr.prx DESTINATION DaedalusX64/Plugins)
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}//PRX/ExceptionHandler/exception.prx DESTINATION DaedalusX64/Plugins)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/../EBOOT.PBP DESTINATION DaedalusX64)

#PSP Resources
install(DIRECTORY ${PROJECT_BINARY_DIR}/../Data/ DESTINATION DaedalusX64)

list(APPEND daed_libs)
set(daed_libs ${daed_libs} PARENT_SCOPE)
 list(APPEND sys_libraries pspfpu psppower pspkubridge pspdebug pspctrl intrafont pspge pspgu pspaudiolib pspaudio pspdisplay )
## PSP_SDL Additional Requirements - pspvram psphprm GL pspvfpu)
set(sys_libraries ${sys_libraries} PARENT_SCOPE)

set(plat_main SysPSP/main.cpp PARENT_SCOPE)
