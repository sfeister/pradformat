% read_extended.m: Example of reading in an extended pradformat HDF5 file
%   That is, reading in your own non-pradformat datasets and attributes
%       that you added to a pradformat HDF5 file

%% Load pradformat object as usual (only reads in the pradformat HDF5 items)
h5filename = fullfile('outs', 'myextendedfields.h5');
fld = prad_load(h5filename);

%% Load in any custom datasets and attributes you added to the HDF5 file
nele = h5read(h5filename, '/nele');
nion = h5read(h5filename, '/nion');
run_number = h5readatt(h5filename, '/', 'run_number');

%% Utilize datasets and attributes in your own scripts
assert(isa(fld, 'SimpleFields'));

disp(fld.pradformat_version)
disp(mean(fld.Ex, 'all'))
disp(mean(nele, 'all'))
disp(mean(nion, 'all'))
disp(run_number)