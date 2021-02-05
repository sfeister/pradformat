% example2_simple_fields.m Write and read the simple fields format for
% HDF5 pradtools

% Example 100 x 300 x 400 spatial grid
% Covering the XYZ spatial coordinate ranges (-5.0, 5.0) meters, (-15.0, 15.0) meters,
% and (-20.0, 20.0) meters, respectively.

% Construct object
fld = simple_fields;

nx = 100;
ny = 300;
nz = 400;
x = linspace(-5.0, 5.0, nx);
y = linspace(-10.0, 10.0, ny);
z = linspace(-20.0, 20.0, nz);
[X,Y,Z] = meshgrid(x,y,z);
fld.X = X;
fld.Y = Y;
fld.Z = Z;
fld.Ex = X.^2 + Y.^2; % Electric fields that depend on X, Y, and Z
fld.Ey = 0.0; % Electric fields that depend on X, Y, and Z
fld.Ez = 5.823 * X.^2 + Z.^2; % Electric fields that depend on X, Y, and Z
fld.Bx = X.^4 + Z.^2; % Magnetic fields that depend on X, Y, and Z
fld.By = 2.191 + Y + Z.^2; % Magnetic fields that depend on X, Y, and Z
fld.Bz = 8.123; % Magnetic fields that depend on X, Y, and Z

% Save to file
[status, msg, msgID] = mkdir('outs');
h5filename = fullfile('outs', 'example2.h5');
prad_save(fld, h5filename);

% For demo purposes, read back in the file you just saved, then write it
% again
fld2 = prad_load(h5filename);
prad_save(fld2, h5filename);