% write_simple_fields.m: Template for writing your own Simple Fields

%% Construct object
fld = SimpleFields;

%% Create some 3D test matrices
nx = 100;
ny = 150;
nz = 125;
x = linspace(-10.0, 10.0, nx);
y = linspace(-15.0, 15.0, ny);
z = linspace(-12.5, 12.5, nz);
[X,Y,Z] = meshgrid(x,y,z);

%% Set datasets and attributes
fld.X = X; % required | X values | meters
fld.Y = Y; % required | Y values | meters
fld.Z = Z; % required | Z values | meters
fld.Ex = X.^2 + Y.^2; % required | Electric field, x-component | Volts/meter
fld.Ey = 0.0; % required | Electric field, y-component | Volts/meter
fld.Ez = 5.823 * X.^2 + Z.^2; % required | Electric field, z-component | Volts/meter
fld.Bx = X.^4 + Z.^2; % required | Magnetic field, x-component | Tesla
fld.By = 2.191 + Y + Z.^2; % required | Magnetic field, y-component | Tesla
fld.Bz = 8.123; % required | Magnetic field, z-component | Tesla
fld.rho = X + Y + Z; % optional | Mass density | kg / m**3

% disp(fld.object_type) % already-set | Specification of the HDF5 object type | "fields" (always this value)
% disp(fld.fields_type) % already-set | Specification of the fields sub-type | "simple" (always this value)
% disp(fld.pradformat_version) % already-set | HDF5 pradformat file format version followed | e.g. "0.1.0"

fld.rho_description = "Six-ionized CH plasma and chamber walls";
fld.label = "Fields_10"; % optional | Short, identifying label for this file (with no spaces or crazy characters). This can be stamped onto plots, etc.
fld.description = "Fields test example with lots of X, Y, and Z dependence."; % optional | Longer description of this file. This can be read by people trying to figure out where this file came from.
% disp(fld.file_date); % automatically-set | Date the (future) file will be created, in the format "YYYY-MM-DD" | You don't need to set this, it will be set automatically
% fld.raw_data_filename = "SimulationMain/DISC_OMEGA/chk0013"; % optional | Filename of the raw data file (e.g. simulation output) from which this derivative file was created, if applicable.

%% Pretty print your newly-minted fields object
disp(fld)

%% Save to file
[status, msg, msgID] = mkdir('outs');
h5filename = fullfile('outs', 'myfields.h5');
prad_save(fld, h5filename);