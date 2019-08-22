%module lttoolbox

%{
#define SWIG_FILE_WITH_INIT
#include <lttoolbox/fst_processor.h>
#include <lttoolbox/lt_locale.h>
%}

%include <lttoolbox/fst_processor.h>
%include <lttoolbox/lt_locale.h>

FILE *fopen(const char *filename, const char *mode);

int fclose(FILE *);
