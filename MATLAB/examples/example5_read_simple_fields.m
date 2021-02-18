% example5_read_simple_fields.m Read in a "Simple Fields" file

% filename = fullfile('..','..','Python','examples','out','example2.h5');
filename = fullfile('..','Python','examples','out','example2-o1.h5');

fld = prad_load(filename);

% Save to file
[status, msg, msgID] = mkdir('outs');
h5filename = fullfile('outs', 'example3.h5');
prad_save(fld, h5filename);