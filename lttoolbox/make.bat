set utf8_INC=-I..\utf8
set libxml_INC=-I..\..\externallibs\win64\libxml2-2.9.3-win32-x86_64\include\libxml2
set iconv_INC=-I..\..\externallibs\win64\iconv-1.14-win32-x86_64\include 
set libxml_LIB=-L..\..\externallibs\win64\libxml2-2.9.3-win32-x86_64\lib
set lttoolbox_INC=-I.. -I.
set cc_sources=alphabet.cc att_compiler.cc compiler.cc compression.cc entry_token.cc expander.cc fst_processor.cc lt_locale.cc match_exe.cc match_node.cc match_state.cc node.cc pattern_list.cc regexp_compiler.cc sorted_vector.cc state.cc transducer.cc trans_exe.cc xml_parse_util.cc tmx_compiler.cc
g++ -fPIC -shared -o liblttoolbox3.dll %cc_sources% %lttoolbox_INC% %utf8_INC% %libxml_INC% %iconv_INC% %libxml_LIB% -lxml2
